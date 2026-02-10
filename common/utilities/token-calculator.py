#!/usr/bin/env python3
"""
Token usage calculator for agent template workflows.

Provides token counting, cost projection, and compression comparison
utilities for planning and budgeting multi-agent sessions.

Token counting uses the ``tiktoken`` library (cl100k_base encoding) when
available, and falls back to a simple word-based heuristic (words * 1.3)
when it is not installed.

Supported subcommands:
    count    Count tokens in a single file
    team     Count tokens across an entire team directory
    cost     Project monetary cost for a given token count and model
    compare  Compare token counts between two files (e.g. original vs compressed)

Examples:
    python token-calculator.py count path/to/file.md
    python token-calculator.py team teams/code-implementation/
    python token-calculator.py cost --tokens 340000 --model opus
    python token-calculator.py compare original.md compressed.md
"""

import argparse
import json
import os
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Token counting backends
# ---------------------------------------------------------------------------

_TIKTOKEN_AVAILABLE = False
_encoding = None

try:
    import tiktoken
    _encoding = tiktoken.get_encoding("cl100k_base")
    _TIKTOKEN_AVAILABLE = True
except ImportError:
    pass


def _count_tokens_tiktoken(text):
    """Count tokens using tiktoken cl100k_base encoding."""
    return len(_encoding.encode(text))


def _count_tokens_heuristic(text):
    """Approximate token count using a word-based heuristic.

    The multiplier of 1.3 accounts for sub-word tokenization that most
    modern tokenizers perform.
    """
    words = text.split()
    return max(1, int(len(words) * 1.3))


def count_tokens(text):
    """Count tokens in *text*, using the best available backend.

    Args:
        text (str): The text to tokenize.

    Returns:
        int: Estimated token count.
    """
    if _TIKTOKEN_AVAILABLE:
        return _count_tokens_tiktoken(text)
    return _count_tokens_heuristic(text)


def token_backend_name():
    """Return a human-readable name for the active tokenizer."""
    return "tiktoken (cl100k_base)" if _TIKTOKEN_AVAILABLE else "heuristic (words * 1.3)"


# ---------------------------------------------------------------------------
# Model pricing (per 1 million tokens)
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


def get_model_pricing(model_key):
    """Look up pricing for a model by short key.

    Args:
        model_key (str): One of ``opus``, ``sonnet``, ``haiku``.

    Returns:
        dict: Pricing entry or ``None`` if not found.
    """
    return MODEL_PRICING.get(model_key.lower())


# ---------------------------------------------------------------------------
# File / directory counting
# ---------------------------------------------------------------------------

# Extensions considered as text when walking directories
_TEXT_EXTENSIONS = {
    ".md", ".txt", ".py", ".js", ".ts", ".jsx", ".tsx", ".json", ".yaml",
    ".yml", ".toml", ".cfg", ".ini", ".sh", ".bash", ".zsh", ".html",
    ".css", ".xml", ".csv", ".rst", ".adoc", ".org",
}


def count_file_tokens(file_path):
    """Count tokens in a single file.

    Args:
        file_path (str | Path): Path to the file.

    Returns:
        dict: ``tokens``, ``characters``, ``lines``, ``words``, ``file``,
        ``backend``.
    """
    path = Path(file_path)
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except IOError as exc:
        return {"error": str(exc), "file": str(path)}

    tokens = count_tokens(text)
    return {
        "file": str(path),
        "tokens": tokens,
        "characters": len(text),
        "lines": text.count("\n") + (1 if text and not text.endswith("\n") else 0),
        "words": len(text.split()),
        "backend": token_backend_name(),
    }


def count_directory_tokens(directory):
    """Recursively count tokens across all text files in *directory*.

    Args:
        directory (str | Path): Root directory to walk.

    Returns:
        dict: Aggregate stats and per-file breakdown.
    """
    root = Path(directory)
    if not root.is_dir():
        return {"error": f"Not a directory: {root}"}

    files = []
    total_tokens = 0
    total_chars = 0
    total_lines = 0
    total_words = 0

    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix.lower() not in _TEXT_EXTENSIONS:
            continue
        # skip hidden directories / files
        parts = path.relative_to(root).parts
        if any(p.startswith(".") for p in parts):
            continue

        info = count_file_tokens(path)
        if "error" in info:
            continue
        files.append(info)
        total_tokens += info["tokens"]
        total_chars += info["characters"]
        total_lines += info["lines"]
        total_words += info["words"]

    return {
        "directory": str(root),
        "file_count": len(files),
        "total_tokens": total_tokens,
        "total_characters": total_chars,
        "total_lines": total_lines,
        "total_words": total_words,
        "backend": token_backend_name(),
        "files": files,
    }


# ---------------------------------------------------------------------------
# Cost projection
# ---------------------------------------------------------------------------

def project_cost(tokens, model_key, output_ratio=0.5):
    """Project monetary cost for a given token budget.

    Assumes a split between input and output tokens controlled by
    *output_ratio*.  For example, with 100 000 tokens and a 0.5 ratio,
    50 000 are counted as input and 50 000 as output.

    Args:
        tokens (int): Total token budget.
        model_key (str): Model short name (``opus``, ``sonnet``, ``haiku``).
        output_ratio (float): Fraction of tokens that are output (0.0-1.0).

    Returns:
        dict: Breakdown of input/output tokens and projected costs.
    """
    pricing = get_model_pricing(model_key)
    if pricing is None:
        return {"error": f"Unknown model '{model_key}'. Choose from: {', '.join(MODEL_PRICING)}"}

    input_tokens = int(tokens * (1 - output_ratio))
    output_tokens = int(tokens * output_ratio)

    input_cost = (input_tokens / 1_000_000) * pricing["input_per_million"]
    output_cost = (output_tokens / 1_000_000) * pricing["output_per_million"]

    return {
        "model": pricing["display_name"],
        "total_tokens": tokens,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "output_ratio": output_ratio,
        "input_cost_usd": round(input_cost, 4),
        "output_cost_usd": round(output_cost, 4),
        "total_cost_usd": round(input_cost + output_cost, 4),
        "pricing": {
            "input_per_million": pricing["input_per_million"],
            "output_per_million": pricing["output_per_million"],
        },
    }


# ---------------------------------------------------------------------------
# Comparison
# ---------------------------------------------------------------------------

def compare_files(path_a, path_b):
    """Compare token counts between two files.

    Useful for evaluating compression effectiveness.

    Args:
        path_a (str | Path): Path to the original (larger) file.
        path_b (str | Path): Path to the compressed (smaller) file.

    Returns:
        dict: Side-by-side token counts, absolute savings, and percentage
        reduction.
    """
    info_a = count_file_tokens(path_a)
    info_b = count_file_tokens(path_b)

    if "error" in info_a or "error" in info_b:
        return {"original": info_a, "compressed": info_b}

    tokens_a = info_a["tokens"]
    tokens_b = info_b["tokens"]
    saved = tokens_a - tokens_b
    pct = (saved / tokens_a * 100) if tokens_a > 0 else 0.0

    return {
        "original": info_a,
        "compressed": info_b,
        "tokens_saved": saved,
        "reduction_percent": round(pct, 2),
        "backend": token_backend_name(),
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _build_parser():
    parser = argparse.ArgumentParser(
        description="Token usage calculator for agent template workflows.",
        epilog=(
            "Examples:\n"
            "  %(prog)s count path/to/file.md\n"
            "  %(prog)s team  teams/code-implementation/\n"
            "  %(prog)s cost  --tokens 340000 --model opus\n"
            "  %(prog)s compare original.md compressed.md\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="command", help="Subcommand")

    # count
    cnt = sub.add_parser("count", help="Count tokens in a single file")
    cnt.add_argument("file", help="Path to the file")

    # team
    tm = sub.add_parser("team", help="Count tokens across a team directory")
    tm.add_argument("directory", help="Team directory to scan")
    tm.add_argument(
        "--details", action="store_true",
        help="Show per-file breakdown",
    )

    # cost
    cst = sub.add_parser("cost", help="Project cost for a token budget")
    cst.add_argument("--tokens", type=int, required=True, help="Total token budget")
    cst.add_argument(
        "--model", required=True, choices=list(MODEL_PRICING.keys()),
        help="Model to price against",
    )
    cst.add_argument(
        "--output-ratio", type=float, default=0.5,
        help="Fraction of tokens that are output (default: 0.5)",
    )

    # compare
    cmp = sub.add_parser("compare", help="Compare tokens between two files")
    cmp.add_argument("original", help="Path to the original file")
    cmp.add_argument("compressed", help="Path to the compressed file")

    return parser


def _format_count(result):
    """Pretty-print a single-file token count."""
    if "error" in result:
        return f"Error: {result['error']}"
    lines = [
        f"File:       {result['file']}",
        f"Tokens:     {result['tokens']:,}",
        f"Words:      {result['words']:,}",
        f"Lines:      {result['lines']:,}",
        f"Characters: {result['characters']:,}",
        f"Backend:    {result['backend']}",
    ]
    return "\n".join(lines)


def _format_team(result, details=False):
    """Pretty-print a team directory scan."""
    if "error" in result:
        return f"Error: {result['error']}"
    lines = [
        f"Directory:        {result['directory']}",
        f"Files scanned:    {result['file_count']}",
        f"Total tokens:     {result['total_tokens']:,}",
        f"Total words:      {result['total_words']:,}",
        f"Total lines:      {result['total_lines']:,}",
        f"Total characters: {result['total_characters']:,}",
        f"Backend:          {result['backend']}",
    ]
    if details and result.get("files"):
        lines.append("")
        lines.append("Per-file breakdown:")
        lines.append(f"  {'File':<60} {'Tokens':>10}")
        lines.append(f"  {'-'*60} {'-'*10}")
        for f in sorted(result["files"], key=lambda x: x["tokens"], reverse=True):
            lines.append(f"  {f['file']:<60} {f['tokens']:>10,}")
    return "\n".join(lines)


def _format_cost(result):
    """Pretty-print a cost projection."""
    if "error" in result:
        return f"Error: {result['error']}"
    lines = [
        f"Model:         {result['model']}",
        f"Total tokens:  {result['total_tokens']:,}",
        f"  Input:       {result['input_tokens']:,}  (${result['input_cost_usd']:.4f})",
        f"  Output:      {result['output_tokens']:,}  (${result['output_cost_usd']:.4f})",
        f"Output ratio:  {result['output_ratio']:.0%}",
        f"",
        f"Estimated cost: ${result['total_cost_usd']:.4f}",
    ]
    return "\n".join(lines)


def _format_compare(result):
    """Pretty-print a comparison result."""
    orig = result.get("original", {})
    comp = result.get("compressed", {})
    if "error" in orig or "error" in comp:
        return json.dumps(result, indent=2)
    lines = [
        f"Original:    {orig['file']}  ({orig['tokens']:,} tokens)",
        f"Compressed:  {comp['file']}  ({comp['tokens']:,} tokens)",
        f"Saved:       {result['tokens_saved']:,} tokens  ({result['reduction_percent']:.1f}% reduction)",
        f"Backend:     {result['backend']}",
    ]
    return "\n".join(lines)


def main():
    parser = _build_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    if args.command == "count":
        result = count_file_tokens(args.file)
        print(_format_count(result))

    elif args.command == "team":
        result = count_directory_tokens(args.directory)
        print(_format_team(result, details=args.details))

    elif args.command == "cost":
        result = project_cost(args.tokens, args.model, args.output_ratio)
        print(_format_cost(result))

    elif args.command == "compare":
        result = compare_files(args.original, args.compressed)
        print(_format_compare(result))

    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
