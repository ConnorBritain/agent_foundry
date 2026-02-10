#!/usr/bin/env python3
"""
Cost estimation for multi-agent teams.

Reads a team's configuration directory to discover agents, estimate token
budgets, and project monetary costs across different Claude models.  Supports
sensitivity analysis and cross-model comparison tables.

The estimator inspects the team directory structure to find agents, their
SKILL.md files, agents.md files, and any configuration YAML/JSON.  Token
budgets are estimated from the actual file sizes found.

Model pricing (per 1 million tokens):
    Opus 4.6   -- $15.00 input / $75.00 output
    Sonnet 4.5 -- $3.00 input  / $15.00 output
    Haiku 4.5  -- $0.25 input  / $1.25 output

Usage:
    python cost-estimator.py <team-directory>
    python cost-estimator.py <team-directory> --sensitivity
    python cost-estimator.py <team-directory> --compare-models
    python cost-estimator.py <team-directory> --sensitivity --compare-models --json

Examples:
    python cost-estimator.py teams/code-implementation/
    python cost-estimator.py teams/research-deep-dive/ --compare-models
    python cost-estimator.py teams/business-in-a-box/ --sensitivity --json
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Token estimation (same heuristic used across the utility suite)
# ---------------------------------------------------------------------------

_TOKEN_MULTIPLIER = 1.3


def _estimate_tokens(text):
    """Estimate token count using a word-based heuristic."""
    return max(1, int(len(text.split()) * _TOKEN_MULTIPLIER))


def _count_file_tokens(file_path):
    """Count estimated tokens in a single file.

    Returns 0 on read errors.
    """
    try:
        text = Path(file_path).read_text(encoding="utf-8", errors="replace")
        return _estimate_tokens(text)
    except IOError:
        return 0


# ---------------------------------------------------------------------------
# Model pricing
# ---------------------------------------------------------------------------

MODEL_PRICING = {
    "opus": {
        "display_name": "Claude Opus 4.6",
        "input_per_million": 15.00,
        "output_per_million": 75.00,
    },
    "sonnet": {
        "display_name": "Claude Sonnet 4.5",
        "input_per_million": 3.00,
        "output_per_million": 15.00,
    },
    "haiku": {
        "display_name": "Claude Haiku 4.5",
        "input_per_million": 0.25,
        "output_per_million": 1.25,
    },
}

# Default output-to-input ratio for cost projections
DEFAULT_OUTPUT_RATIO = 0.5

# Multiplier applied to context tokens to estimate total session tokens
# (accounts for multi-turn conversation overhead)
SESSION_MULTIPLIER = 3.0

# Text file extensions to scan
_TEXT_EXTENSIONS = {
    ".md", ".txt", ".py", ".js", ".ts", ".jsx", ".tsx", ".json", ".yaml",
    ".yml", ".toml", ".cfg", ".ini", ".sh", ".bash", ".html", ".css",
    ".xml", ".rst", ".adoc", ".org",
}


# ---------------------------------------------------------------------------
# Team directory analysis
# ---------------------------------------------------------------------------

def _find_team_config(team_dir):
    """Search for a team configuration file (YAML or JSON).

    Returns:
        Path | None: Path to the config file, or None.
    """
    root = Path(team_dir)
    candidates = [
        root / "team.yaml",
        root / "team.yml",
        root / "team.json",
        root / "config.yaml",
        root / "config.yml",
        root / "config.json",
    ]
    for c in candidates:
        if c.is_file():
            return c
    return None


def _parse_config_agents(config_path):
    """Try to extract agent names from a YAML/JSON config file.

    Uses simple regex to avoid requiring PyYAML.

    Returns:
        list[str]: Agent names found, or empty list.
    """
    if config_path is None:
        return []

    try:
        text = config_path.read_text(encoding="utf-8", errors="replace")
    except IOError:
        return []

    # JSON
    if config_path.suffix == ".json":
        try:
            data = json.loads(text)
            if isinstance(data, dict):
                agents = data.get("agents", [])
                if isinstance(agents, list):
                    return [
                        a.get("name", a) if isinstance(a, dict) else str(a)
                        for a in agents
                    ]
        except (json.JSONDecodeError, TypeError):
            pass

    # YAML-ish: look for lines like "  - name: agent-name"
    names = re.findall(r"^\s*-?\s*name:\s*[\"']?([a-z0-9_-]+)", text, re.MULTILINE)
    return names


def analyze_team(team_dir):
    """Analyze a team directory and estimate token budgets.

    Discovers agents from the ``agents/`` subdirectory, counts tokens in
    all text files, and builds per-agent and aggregate estimates.

    Args:
        team_dir (str | Path): Path to the team directory.

    Returns:
        dict: Analysis results including agent roster, per-agent token counts,
        and aggregate totals.
    """
    root = Path(team_dir)
    if not root.is_dir():
        return {"error": f"Not a directory: {root}"}

    # Discover agents
    agents_dir = root / "agents"
    agent_names = []
    agent_details = {}

    if agents_dir.is_dir():
        for entry in sorted(agents_dir.iterdir()):
            if entry.is_dir() and not entry.name.startswith("."):
                agent_names.append(entry.name)
                # Count tokens in this agent's directory
                agent_tokens = 0
                agent_files = 0
                for f in entry.rglob("*"):
                    if f.is_file() and f.suffix.lower() in _TEXT_EXTENSIONS:
                        agent_tokens += _count_file_tokens(f)
                        agent_files += 1
                agent_details[entry.name] = {
                    "context_tokens": agent_tokens,
                    "file_count": agent_files,
                    "directory": str(entry),
                }

    # Also try to find agents from config
    config_path = _find_team_config(root)
    config_agents = _parse_config_agents(config_path)
    for ca in config_agents:
        if ca not in agent_details:
            agent_names.append(ca)
            agent_details[ca] = {
                "context_tokens": 0,
                "file_count": 0,
                "directory": None,
                "note": "Found in config only (no agent directory)",
            }

    # Count tokens in shared / top-level team files
    shared_tokens = 0
    shared_files = 0
    for f in root.iterdir():
        if f.is_file() and f.suffix.lower() in _TEXT_EXTENSIONS:
            shared_tokens += _count_file_tokens(f)
            shared_files += 1

    # Scenarios, examples, etc.
    extra_dirs = ["scenarios", "examples", "mcp-servers"]
    extra_tokens = 0
    for dname in extra_dirs:
        d = root / dname
        if d.is_dir():
            for f in d.rglob("*"):
                if f.is_file() and f.suffix.lower() in _TEXT_EXTENSIONS:
                    extra_tokens += _count_file_tokens(f)

    total_context_tokens = sum(
        a["context_tokens"] for a in agent_details.values()
    ) + shared_tokens + extra_tokens

    # Estimated session tokens (context * multiplier for multi-turn overhead)
    estimated_session_tokens = int(total_context_tokens * SESSION_MULTIPLIER)

    return {
        "team_directory": str(root),
        "config_file": str(config_path) if config_path else None,
        "agent_count": len(agent_details),
        "agents": agent_details,
        "shared_tokens": shared_tokens,
        "shared_files": shared_files,
        "extra_tokens": extra_tokens,
        "total_context_tokens": total_context_tokens,
        "session_multiplier": SESSION_MULTIPLIER,
        "estimated_session_tokens": estimated_session_tokens,
    }


# ---------------------------------------------------------------------------
# Cost calculation
# ---------------------------------------------------------------------------

def calculate_cost(tokens, model_key, output_ratio=DEFAULT_OUTPUT_RATIO):
    """Calculate cost for a given token count and model.

    Args:
        tokens (int): Total token budget.
        model_key (str): Model short name.
        output_ratio (float): Fraction of tokens that are output.

    Returns:
        dict: Cost breakdown.
    """
    pricing = MODEL_PRICING.get(model_key)
    if pricing is None:
        return {"error": f"Unknown model: {model_key}"}

    input_tokens = int(tokens * (1 - output_ratio))
    output_tokens = int(tokens * output_ratio)
    input_cost = (input_tokens / 1_000_000) * pricing["input_per_million"]
    output_cost = (output_tokens / 1_000_000) * pricing["output_per_million"]

    return {
        "model": pricing["display_name"],
        "model_key": model_key,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "input_cost": round(input_cost, 4),
        "output_cost": round(output_cost, 4),
        "total_cost": round(input_cost + output_cost, 4),
    }


def estimate_team_cost(analysis, model_key="sonnet", output_ratio=DEFAULT_OUTPUT_RATIO):
    """Estimate total cost for a team using the analysis results.

    Provides per-agent and aggregate cost breakdowns.

    Args:
        analysis (dict): Output from ``analyze_team``.
        model_key (str): Default model for all agents.
        output_ratio (float): Output token ratio.

    Returns:
        dict: Detailed cost estimate.
    """
    if "error" in analysis:
        return analysis

    # Per-agent costs (each agent gets shared context + its own context)
    shared = analysis["shared_tokens"]
    agent_costs = {}
    for name, details in analysis["agents"].items():
        agent_session = int((details["context_tokens"] + shared) * SESSION_MULTIPLIER)
        cost = calculate_cost(agent_session, model_key, output_ratio)
        cost["session_tokens"] = agent_session
        cost["context_tokens"] = details["context_tokens"]
        agent_costs[name] = cost

    # Aggregate
    total_tokens = analysis["estimated_session_tokens"]
    total = calculate_cost(total_tokens, model_key, output_ratio)

    return {
        "team_directory": analysis["team_directory"],
        "model": MODEL_PRICING[model_key]["display_name"],
        "model_key": model_key,
        "agent_count": analysis["agent_count"],
        "per_agent": agent_costs,
        "aggregate": {
            "total_context_tokens": analysis["total_context_tokens"],
            "estimated_session_tokens": total_tokens,
            "total_cost": total["total_cost"],
            "input_cost": total["input_cost"],
            "output_cost": total["output_cost"],
        },
    }


def compare_models(analysis, output_ratio=DEFAULT_OUTPUT_RATIO):
    """Compare costs across all supported models for the same team.

    Args:
        analysis (dict): Output from ``analyze_team``.
        output_ratio (float): Output token ratio.

    Returns:
        list[dict]: One entry per model with cost details.
    """
    tokens = analysis["estimated_session_tokens"]
    rows = []
    for key in ["haiku", "sonnet", "opus"]:
        cost = calculate_cost(tokens, key, output_ratio)
        rows.append(cost)
    return rows


def sensitivity_analysis(analysis, model_key="sonnet", output_ratio=DEFAULT_OUTPUT_RATIO,
                         variation=0.20):
    """Run sensitivity analysis with +/- variation on token estimates.

    Args:
        analysis (dict): Output from ``analyze_team``.
        model_key (str): Model for pricing.
        output_ratio (float): Output token ratio.
        variation (float): Percentage variation (default 0.20 = 20%).

    Returns:
        dict: Low, base, and high estimates.
    """
    base_tokens = analysis["estimated_session_tokens"]
    low_tokens = int(base_tokens * (1 - variation))
    high_tokens = int(base_tokens * (1 + variation))

    return {
        "variation_percent": int(variation * 100),
        "model": MODEL_PRICING[model_key]["display_name"],
        "low": {
            "tokens": low_tokens,
            **calculate_cost(low_tokens, model_key, output_ratio),
        },
        "base": {
            "tokens": base_tokens,
            **calculate_cost(base_tokens, model_key, output_ratio),
        },
        "high": {
            "tokens": high_tokens,
            **calculate_cost(high_tokens, model_key, output_ratio),
        },
    }


# ---------------------------------------------------------------------------
# Formatting helpers
# ---------------------------------------------------------------------------

def _format_currency(amount):
    """Format a dollar amount for display."""
    if amount < 0.01:
        return f"${amount:.4f}"
    return f"${amount:.2f}"


def _format_team_report(analysis, estimate, model_comparison=None, sensitivity=None):
    """Generate a human-readable cost report."""
    lines = []
    lines.append("=" * 70)
    lines.append("  AGENT TEAM COST ESTIMATE")
    lines.append("=" * 70)
    lines.append("")
    lines.append(f"  Team directory:  {analysis['team_directory']}")
    lines.append(f"  Agents:          {analysis['agent_count']}")
    lines.append(f"  Config file:     {analysis.get('config_file') or '(none found)'}")
    lines.append(f"  Default model:   {estimate['model']}")
    lines.append("")

    # Per-agent breakdown
    lines.append("  Per-Agent Breakdown:")
    lines.append(f"  {'Agent':<30} {'Context':>10} {'Session':>10} {'Cost':>10}")
    lines.append(f"  {'-'*30} {'-'*10} {'-'*10} {'-'*10}")

    for name, cost in estimate["per_agent"].items():
        lines.append(
            f"  {name:<30} {cost['context_tokens']:>10,} "
            f"{cost['session_tokens']:>10,} "
            f"{_format_currency(cost['total_cost']):>10}"
        )

    lines.append("")
    agg = estimate["aggregate"]
    lines.append(f"  Total context tokens:   {agg['total_context_tokens']:>12,}")
    lines.append(f"  Est. session tokens:    {agg['estimated_session_tokens']:>12,}")
    lines.append(f"  Session multiplier:     {analysis['session_multiplier']:>12.1f}x")
    lines.append(f"  Estimated total cost:   {_format_currency(agg['total_cost']):>12}")
    lines.append("")

    # Model comparison table
    if model_comparison:
        lines.append("-" * 70)
        lines.append("  Model Comparison (same workload):")
        lines.append(
            f"  {'Model':<22} {'Input Cost':>12} {'Output Cost':>12} {'Total':>12}"
        )
        lines.append(
            f"  {'-'*22} {'-'*12} {'-'*12} {'-'*12}"
        )
        for row in model_comparison:
            lines.append(
                f"  {row['model']:<22} "
                f"{_format_currency(row['input_cost']):>12} "
                f"{_format_currency(row['output_cost']):>12} "
                f"{_format_currency(row['total_cost']):>12}"
            )
        lines.append("")

    # Sensitivity analysis
    if sensitivity:
        lines.append("-" * 70)
        lines.append(
            f"  Sensitivity Analysis (+/- {sensitivity['variation_percent']}% token usage):"
        )
        lines.append(
            f"  {'Scenario':<12} {'Tokens':>14} {'Cost':>12}"
        )
        lines.append(
            f"  {'-'*12} {'-'*14} {'-'*12}"
        )
        for label in ["low", "base", "high"]:
            s = sensitivity[label]
            lines.append(
                f"  {label.capitalize():<12} {s['tokens']:>14,} "
                f"{_format_currency(s['total_cost']):>12}"
            )
        lines.append("")

    lines.append("=" * 70)
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _build_parser():
    parser = argparse.ArgumentParser(
        description="Estimate costs for multi-agent team workflows.",
        epilog=(
            "Model pricing (per 1M tokens):\n"
            "  Opus 4.6   -- $15.00 input / $75.00 output\n"
            "  Sonnet 4.5 -- $3.00 input  / $15.00 output\n"
            "  Haiku 4.5  -- $0.25 input  / $1.25 output\n"
            "\n"
            "Examples:\n"
            "  %(prog)s teams/code-implementation/\n"
            "  %(prog)s teams/research-deep-dive/ --compare-models\n"
            "  %(prog)s teams/business-in-a-box/ --sensitivity --json\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "team_directory",
        help="Path to the team directory to analyze",
    )
    parser.add_argument(
        "--model", "-m",
        choices=list(MODEL_PRICING.keys()),
        default="sonnet",
        help="Default model for cost estimates (default: sonnet)",
    )
    parser.add_argument(
        "--output-ratio",
        type=float,
        default=DEFAULT_OUTPUT_RATIO,
        help=f"Fraction of tokens that are output (default: {DEFAULT_OUTPUT_RATIO})",
    )
    parser.add_argument(
        "--sensitivity",
        action="store_true",
        help="Include +/- 20%% sensitivity analysis",
    )
    parser.add_argument(
        "--compare-models",
        action="store_true",
        help="Include model comparison table (Haiku/Sonnet/Opus)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results as JSON instead of formatted text",
    )
    return parser


def main():
    parser = _build_parser()
    args = parser.parse_args()

    # Analyze team
    analysis = analyze_team(args.team_directory)
    if "error" in analysis:
        print(f"Error: {analysis['error']}", file=sys.stderr)
        sys.exit(1)

    # Core estimate
    estimate = estimate_team_cost(analysis, args.model, args.output_ratio)

    # Optional analyses
    model_comp = None
    if args.compare_models:
        model_comp = compare_models(analysis, args.output_ratio)

    sens = None
    if args.sensitivity:
        sens = sensitivity_analysis(analysis, args.model, args.output_ratio)

    # Output
    if args.json:
        output = {
            "analysis": analysis,
            "estimate": estimate,
        }
        if model_comp is not None:
            output["model_comparison"] = model_comp
        if sens is not None:
            output["sensitivity"] = sens
        print(json.dumps(output, indent=2))
    else:
        report = _format_team_report(analysis, estimate, model_comp, sens)
        print(report)


if __name__ == "__main__":
    main()
