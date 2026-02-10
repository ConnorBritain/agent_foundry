#!/usr/bin/env python3
"""
Sforza Control Plane -- terminal dashboard for monitoring projects.

Reads from shared-workspace/project-status.json and related files to display
an auto-refreshing terminal dashboard with:

  - Active teams with status, phase, progress, and cost
  - Budget summary with visual progress bar
  - Inter-team dependency table
  - Recent cross-team activity log

Uses the ``rich`` library when available for polished rendering; falls back
to plain ANSI escape codes and Unicode box-drawing characters otherwise.

Usage:
    python3 control-plane.py --project /path/to/project
    python3 control-plane.py                              # auto-detect from cwd

Controls:
    r   force refresh
    q   quit
    d   toggle detail view
"""

import argparse
import json
import os
import re
import select
import signal
import sys
import termios
import time
import tty
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Path constants (relative to project root)
# ---------------------------------------------------------------------------

STATUS_FILE = "shared-workspace/project-status.json"
COMMUNICATION_FILE = "shared-workspace/cross-team-communication.md"
DEPENDENCY_FILE = "shared-workspace/dependency-tracker.md"
AGENT_STATUS_FILE = "shared-state/agent-status.json"

# ---------------------------------------------------------------------------
# Rich detection
# ---------------------------------------------------------------------------

_USE_RICH = False
try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.text import Text
    from rich.columns import Columns
    from rich.layout import Layout
    from rich import box

    _USE_RICH = True
except ImportError:
    pass

# ---------------------------------------------------------------------------
# ANSI helpers (fallback when rich is unavailable)
# ---------------------------------------------------------------------------

_RESET = "\033[0m"
_BOLD = "\033[1m"
_DIM = "\033[2m"
_RED = "\033[31m"
_GREEN = "\033[32m"
_YELLOW = "\033[33m"
_BLUE = "\033[34m"
_MAGENTA = "\033[35m"
_CYAN = "\033[36m"
_WHITE = "\033[37m"
_BG_BLUE = "\033[44m"
_BG_GREEN = "\033[42m"
_BG_RED = "\033[41m"
_BG_YELLOW = "\033[43m"


def _clear_screen():
    """Clear terminal and move cursor to top-left."""
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()


def _term_width():
    """Return the current terminal width, defaulting to 80."""
    try:
        columns = os.get_terminal_size().columns
        return max(columns, 60)
    except OSError:
        return 80


# ---------------------------------------------------------------------------
# Data reading
# ---------------------------------------------------------------------------

def _find_project_root(project_path=None):
    """Locate the project root containing shared-workspace/.

    Searches *project_path* (if given), then CWD, then walks up the directory
    tree from CWD, and finally tries relative to this script's location.

    Returns:
        Path | None: The project root, or None if not found.
    """
    candidates = []

    if project_path:
        candidates.append(Path(project_path))

    candidates.append(Path.cwd())

    # Walk up from CWD
    current = Path.cwd()
    for _ in range(10):
        candidates.append(current)
        if current.parent == current:
            break
        current = current.parent

    # Script-relative fallback (common/utilities/ -> project root)
    script_dir = Path(__file__).resolve().parent
    candidates.append(script_dir.parent.parent)

    for candidate in candidates:
        candidate = candidate.resolve()
        if (candidate / STATUS_FILE).is_file():
            return candidate

    return None


def read_project_status(project_root):
    """Read and return the project-status.json data.

    Returns:
        dict: The parsed JSON, or a minimal empty structure on failure.
    """
    status_path = project_root / STATUS_FILE
    empty = {
        "project_name": "Unknown",
        "active_teams": [],
        "dependencies": [],
    }
    if not status_path.is_file():
        return empty
    try:
        with open(status_path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        if not isinstance(data, dict):
            return empty
        data.setdefault("project_name", "Unknown")
        data.setdefault("active_teams", [])
        data.setdefault("dependencies", [])
        return data
    except (json.JSONDecodeError, IOError):
        return empty


def read_agent_status(project_root):
    """Read the per-agent status registry if it exists.

    Returns:
        dict: The parsed agent-status.json, or an empty structure.
    """
    path = project_root / AGENT_STATUS_FILE
    empty = {"agents": {}, "team_metrics": {}}
    if not path.is_file():
        return empty
    try:
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        if isinstance(data, dict):
            data.setdefault("agents", {})
            data.setdefault("team_metrics", {})
            return data
        return empty
    except (json.JSONDecodeError, IOError):
        return empty


def read_communication_log(project_root, max_entries=8):
    """Parse the cross-team-communication.md for recent messages.

    Returns:
        list[dict]: Each entry has ``time``, ``from_team``, ``to_team``,
        ``message``, and optionally ``priority``.
    """
    path = project_root / COMMUNICATION_FILE
    if not path.is_file():
        return []
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except IOError:
        return []

    entries = []

    # Match headers like: ### [14:32] Business Planning -> Content
    # Also handles the arrow variants: ->, -->, =>, and the Unicode arrow
    header_re = re.compile(
        r"###\s*\[(\d{1,2}:\d{2})\]\s*(.+?)\s*(?:->|-->|=>|\u2192)\s*(.+)",
        re.IGNORECASE,
    )

    lines = text.splitlines()
    i = 0
    while i < len(lines):
        m = header_re.match(lines[i].strip())
        if m:
            timestamp = m.group(1)
            from_team = m.group(2).strip()
            to_team = m.group(3).strip()
            message_lines = []
            priority = None
            i += 1
            # Collect body lines until next header, section marker, or blank separator
            while i < len(lines):
                line = lines[i].strip()
                if line.startswith("###") or line.startswith("## ") or line == "---":
                    break
                if line.lower().startswith("priority:"):
                    priority = line.split(":", 1)[1].strip()
                elif line:
                    message_lines.append(line)
                i += 1
            entries.append({
                "time": timestamp,
                "from_team": from_team,
                "to_team": to_team,
                "message": " ".join(message_lines) if message_lines else "(no message)",
                "priority": priority,
            })
        else:
            i += 1

    # Return the most recent entries (last N)
    return entries[-max_entries:]


def read_dependency_tracker(project_root):
    """Parse the dependency-tracker.md markdown tables.

    Returns:
        list[dict]: Each entry has ``from_team``, ``to_team``,
        ``dependency``, ``status``, and optionally ``due_date``.
    """
    path = project_root / DEPENDENCY_FILE
    if not path.is_file():
        return []
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except IOError:
        return []

    entries = []
    # Match markdown table rows: | col1 | col2 | col3 | col4 | ... |
    row_re = re.compile(r"^\|(.+)\|$")

    in_current = False
    header_seen = False
    for line in text.splitlines():
        stripped = line.strip()

        # Track which section we are in
        if stripped.startswith("## Current"):
            in_current = True
            header_seen = False
            continue
        elif stripped.startswith("## Resolved"):
            in_current = False
            header_seen = False
            continue

        if not in_current:
            continue

        m = row_re.match(stripped)
        if not m:
            continue

        cells = [c.strip() for c in m.group(1).split("|")]

        # Skip header row and separator row
        if any(c.startswith("---") or c.startswith("===") for c in cells):
            header_seen = True
            continue
        if not header_seen:
            # This is the header text row itself
            header_seen = False  # separator row hasn't passed yet
            continue

        # Expect at least 4 columns: From, To, Dependency, Status
        if len(cells) < 4:
            continue

        # Skip placeholder rows
        if cells[0].startswith("[") and "empty" in cells[0].lower():
            continue

        entry = {
            "from_team": cells[0],
            "to_team": cells[1],
            "dependency": cells[2],
            "status": cells[3],
        }
        if len(cells) >= 5 and cells[4]:
            entry["due_date"] = cells[4]
        entries.append(entry)

    return entries


# ---------------------------------------------------------------------------
# Budget helpers
# ---------------------------------------------------------------------------

def _extract_cost(value):
    """Try to parse a dollar amount from a string like '$128.50' or '128.50'.

    Returns:
        float | None
    """
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        cleaned = value.replace("$", "").replace(",", "").strip()
        try:
            return float(cleaned)
        except ValueError:
            return None
    return None


def _extract_progress(value):
    """Parse a progress value like '65%' or 65 into an integer 0-100.

    Returns:
        int
    """
    if isinstance(value, (int, float)):
        return max(0, min(100, int(value)))
    if isinstance(value, str):
        cleaned = value.replace("%", "").strip()
        try:
            return max(0, min(100, int(float(cleaned))))
        except ValueError:
            return 0
    return 0


def compute_budget(project_data):
    """Compute budget summary from project data.

    Looks for ``budget`` top-level fields, and sums per-team ``cost`` fields.

    Returns:
        dict: With ``spent``, ``budget``, ``percentage``, ``status``.
    """
    teams = project_data.get("active_teams", [])

    total_spent = 0.0
    for team in teams:
        cost = _extract_cost(team.get("cost"))
        if cost is not None:
            total_spent += cost

    # Budget may be specified at the project level
    budget_total = _extract_cost(project_data.get("budget"))
    if budget_total is None:
        budget_total = _extract_cost(project_data.get("weekly_budget"))
    if budget_total is None:
        budget_info = project_data.get("budget_info", {})
        if isinstance(budget_info, dict):
            budget_total = _extract_cost(budget_info.get("total"))
            if budget_total is None:
                budget_total = _extract_cost(budget_info.get("weekly"))

    # Default budget if none specified
    if budget_total is None or budget_total <= 0:
        budget_total = 500.0  # default weekly budget

    percentage = (total_spent / budget_total * 100) if budget_total > 0 else 0.0

    if percentage > 90:
        status = "CRITICAL"
    elif percentage > 75:
        status = "Warning"
    elif total_spent == 0:
        status = "No cost data"
    else:
        status = "On track"

    return {
        "spent": total_spent,
        "budget": budget_total,
        "percentage": min(percentage, 100.0),
        "status": status,
    }


# ---------------------------------------------------------------------------
# Rendering: Rich
# ---------------------------------------------------------------------------

def _status_dot_rich(status):
    """Return a colored dot for rich output."""
    s = status.lower() if isinstance(status, str) else ""
    if s in ("active", "running"):
        return "[bold green]\u25cf[/bold green]"
    elif s in ("awaiting", "waiting", "pending"):
        return "[bold yellow]\u25cf[/bold yellow]"
    elif s in ("blocked", "error"):
        return "[bold red]\u25cf[/bold red]"
    elif s in ("completed", "complete", "done"):
        return "[bold blue]\u25cf[/bold blue]"
    elif s == "offline":
        return "[dim]\u25cf[/dim]"
    return "[dim]\u25cb[/dim]"


def _dep_status_rich(status):
    """Return styled dependency status text for rich output."""
    s = status.lower().strip() if isinstance(status, str) else ""
    if s in ("complete", "completed", "done", "resolved"):
        return "[green]Done[/green]"
    elif s in ("pending", "waiting", "awaiting"):
        return "[yellow]Waiting[/yellow]"
    elif s in ("blocked",):
        return "[red]Blocked[/red]"
    return f"[dim]{status}[/dim]"


def _progress_bar_rich(percentage, width=20):
    """Build a text-based progress bar for rich."""
    filled = int(width * percentage / 100)
    empty = width - filled
    if percentage > 90:
        color = "red"
    elif percentage > 75:
        color = "yellow"
    else:
        color = "green"
    bar = f"[{color}]{'█' * filled}[/{color}][dim]{'░' * empty}[/dim]"
    return bar


def render_rich(project_data, deps_md, comms, budget, agent_data, show_detail):
    """Render the full dashboard using the rich library."""
    console = Console()
    console.clear()
    width = console.width

    project_name = project_data.get("project_name", "Unknown")
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Header
    header_text = Text.from_markup(
        f"[bold white]SFORZA CONTROL PLANE[/bold white]\n"
        f"[dim]Project:[/dim] [bold cyan]{project_name}[/bold cyan]"
        f"    [dim]{now_str}[/dim]"
    )
    console.print(Panel(header_text, style="bold blue", expand=True))

    # --- Active Teams ---
    teams = project_data.get("active_teams", [])
    team_label = f"ACTIVE TEAMS ({len(teams)})" if teams else "ACTIVE TEAMS"

    if teams:
        table = Table(
            title=team_label,
            box=box.ROUNDED,
            title_style="bold white",
            header_style="bold cyan",
            expand=True,
        )
        table.add_column("Team", style="bold", min_width=16, ratio=3)
        table.add_column("Status", justify="center", min_width=6, ratio=1)
        table.add_column("Phase", min_width=12, ratio=2)
        table.add_column("Progress", justify="center", min_width=8, ratio=1)
        table.add_column("Cost", justify="right", min_width=8, ratio=1)
        if show_detail:
            table.add_column("Last Update", justify="right", min_width=16, ratio=2)

        for team in teams:
            name = team.get("team", "unknown").replace("-", " ").title()
            status = team.get("status", "offline")
            phase = team.get("phase", "-").replace("-", " ").title()
            progress = _extract_progress(team.get("progress", 0))
            cost = _extract_cost(team.get("cost"))
            cost_str = f"${cost:,.2f}" if cost is not None else "-"
            progress_str = f"{progress}%"
            last_update = team.get("last_update", "-")
            if show_detail and isinstance(last_update, str) and "T" in last_update:
                try:
                    dt = datetime.fromisoformat(last_update.replace("Z", "+00:00"))
                    last_update = dt.strftime("%H:%M:%S")
                except (ValueError, TypeError):
                    pass

            row = [
                name,
                _status_dot_rich(status),
                phase,
                progress_str,
                cost_str,
            ]
            if show_detail:
                row.append(str(last_update))
            table.add_row(*row)

        console.print(table)
    else:
        console.print(
            Panel("[dim]No teams active[/dim]", title=team_label, style="dim")
        )

    console.print()

    # --- Budget ---
    pct = budget["percentage"]
    pct_bar = _progress_bar_rich(pct, width=30)
    budget_color = "green"
    if pct > 90:
        budget_color = "red"
    elif pct > 75:
        budget_color = "yellow"

    if budget["spent"] > 0:
        budget_text = Text.from_markup(
            f"Used: [bold]${budget['spent']:,.2f}[/bold] / "
            f"${budget['budget']:,.2f} weekly budget "
            f"([{budget_color}]{pct:.0f}%[/{budget_color}])\n"
            f"{pct_bar}\n"
            f"Status: [{budget_color}]{budget['status']}[/{budget_color}]"
        )
    else:
        budget_text = Text.from_markup(
            f"Budget: ${budget['budget']:,.2f} weekly\n"
            f"[dim]No cost data reported yet[/dim]"
        )
    console.print(Panel(budget_text, title="BUDGET", title_align="left", style="dim"))

    console.print()

    # --- Dependencies ---
    # Merge dependencies from project-status.json and dependency-tracker.md
    all_deps = []
    json_deps = project_data.get("dependencies", [])
    for d in json_deps:
        all_deps.append({
            "from": d.get("from_team", "?"),
            "to": d.get("to_team", "?"),
            "need": d.get("dependency", "-"),
            "status": d.get("status", "unknown"),
        })
    for d in deps_md:
        # Avoid exact duplicates
        key = (d.get("from_team", ""), d.get("to_team", ""), d.get("dependency", ""))
        already = any(
            (x["from"] == key[0] and x["to"] == key[1] and x["need"] == key[2])
            for x in all_deps
        )
        if not already:
            all_deps.append({
                "from": d.get("from_team", "?"),
                "to": d.get("to_team", "?"),
                "need": d.get("dependency", "-"),
                "status": d.get("status", "unknown"),
            })

    dep_label = f"DEPENDENCIES ({len(all_deps)})" if all_deps else "DEPENDENCIES"

    if all_deps:
        dep_table = Table(
            title=dep_label,
            box=box.ROUNDED,
            title_style="bold white",
            header_style="bold cyan",
            expand=True,
        )
        dep_table.add_column("From", style="bold", min_width=12, ratio=2)
        dep_table.add_column("To", min_width=12, ratio=2)
        dep_table.add_column("Need", min_width=16, ratio=3)
        dep_table.add_column("Status", justify="center", min_width=8, ratio=1)

        for d in all_deps:
            from_name = d["from"].replace("-", " ").title()
            to_name = d["to"].replace("-", " ").title()
            dep_table.add_row(
                from_name,
                to_name,
                d["need"],
                _dep_status_rich(d["status"]),
            )
        console.print(dep_table)
    else:
        console.print(
            Panel("[dim]No dependencies tracked[/dim]", title=dep_label, style="dim")
        )

    console.print()

    # --- Agent Status (detail mode only) ---
    if show_detail and agent_data.get("agents"):
        agents = agent_data["agents"]
        agent_table = Table(
            title=f"AGENT STATUS ({len(agents)})",
            box=box.SIMPLE_HEAVY,
            title_style="bold white",
            header_style="bold cyan",
            expand=True,
        )
        agent_table.add_column("Agent", style="bold", ratio=2)
        agent_table.add_column("Status", justify="center", ratio=1)
        agent_table.add_column("Task", ratio=3)
        agent_table.add_column("Progress", justify="center", ratio=1)

        for name, info in sorted(agents.items()):
            status = info.get("status", "offline")
            task = info.get("current_task", "-")
            progress = info.get("progress", 0)
            agent_table.add_row(
                name,
                _status_dot_rich(status),
                str(task),
                f"{progress}%",
            )
        console.print(agent_table)
        console.print()

    # --- Recent Activity ---
    if comms:
        console.print("[bold white]RECENT ACTIVITY[/bold white]")
        for entry in comms:
            ts = entry.get("time", "??:??")
            fr = entry.get("from_team", "?")
            to = entry.get("to_team", "?")
            msg = entry.get("message", "")
            priority = entry.get("priority")

            priority_tag = ""
            if priority:
                p = priority.lower()
                if p == "high":
                    priority_tag = " [bold red][HIGH][/bold red]"
                elif p == "medium":
                    priority_tag = " [yellow][MED][/yellow]"
                elif p == "low":
                    priority_tag = " [dim][LOW][/dim]"

            console.print(
                f"  [dim][{ts}][/dim] [bold]{fr}[/bold] -> {to}: {msg}{priority_tag}"
            )
        console.print()
    else:
        console.print("[dim]RECENT ACTIVITY: No messages yet[/dim]")
        console.print()

    # Footer
    detail_hint = "'d' details ON" if show_detail else "'d' for details"
    console.print(
        f"[dim]Press 'r' to refresh | 'q' to quit | {detail_hint}  "
        f"(auto-refresh 5s)[/dim]"
    )


# ---------------------------------------------------------------------------
# Rendering: ANSI fallback
# ---------------------------------------------------------------------------

def _ansi_status_dot(status):
    """Return a colored Unicode dot using ANSI codes."""
    s = status.lower() if isinstance(status, str) else ""
    if s in ("active", "running"):
        return f"{_GREEN}\u25cf{_RESET}"
    elif s in ("awaiting", "waiting", "pending"):
        return f"{_YELLOW}\u25cf{_RESET}"
    elif s in ("blocked", "error"):
        return f"{_RED}\u25cf{_RESET}"
    elif s in ("completed", "complete", "done"):
        return f"{_BLUE}\u25cf{_RESET}"
    elif s == "offline":
        return f"{_DIM}\u25cf{_RESET}"
    return f"{_DIM}\u25cb{_RESET}"


def _ansi_dep_status(status):
    """Return colored dependency status text."""
    s = status.lower().strip() if isinstance(status, str) else ""
    if s in ("complete", "completed", "done", "resolved"):
        return f"{_GREEN}Done{_RESET}"
    elif s in ("pending", "waiting", "awaiting"):
        return f"{_YELLOW}Waiting{_RESET}"
    elif s in ("blocked",):
        return f"{_RED}Blocked{_RESET}"
    return f"{_DIM}{status}{_RESET}"


def _ansi_progress_bar(percentage, width=30):
    """Build a text-based progress bar with ANSI colors."""
    filled = int(width * percentage / 100)
    empty = width - filled
    if percentage > 90:
        color = _RED
    elif percentage > 75:
        color = _YELLOW
    else:
        color = _GREEN
    return f"{color}{'█' * filled}{_RESET}{_DIM}{'░' * empty}{_RESET}"


def _pad(text, width, strip_ansi=True):
    """Pad text to a fixed visible width, accounting for ANSI codes."""
    if strip_ansi:
        visible = re.sub(r"\033\[[0-9;]*m", "", text)
    else:
        visible = text
    padding = max(0, width - len(visible))
    return text + " " * padding


def _truncate(text, width):
    """Truncate text to a maximum visible width."""
    if len(text) <= width:
        return text
    return text[: width - 1] + "\u2026"


def _draw_box_top(width):
    return f"{_BOLD}{_BLUE}\u2554{'═' * (width - 2)}\u2557{_RESET}"


def _draw_box_mid(text, width):
    visible_len = len(re.sub(r"\033\[[0-9;]*m", "", text))
    padding = max(0, width - 4 - visible_len)
    return f"{_BOLD}{_BLUE}\u2551{_RESET} {text}{' ' * padding} {_BOLD}{_BLUE}\u2551{_RESET}"


def _draw_box_bottom(width):
    return f"{_BOLD}{_BLUE}\u255a{'═' * (width - 2)}\u255d{_RESET}"


def _draw_table_row(cells, widths, sep="\u2502"):
    """Format a row with given column widths."""
    parts = []
    for text, w in zip(cells, widths):
        parts.append(f" {_pad(text, w)} ")
    return f"{_DIM}{sep}{_RESET}" + f"{_DIM}{sep}{_RESET}".join(parts) + f"{_DIM}{sep}{_RESET}"


def _draw_table_separator(widths, left="\u251c", mid="\u253c", right="\u2524", fill="\u2500"):
    parts = []
    for w in widths:
        parts.append(fill * (w + 2))
    return f"{_DIM}{left}{mid.join(parts)}{right}{_RESET}"


def _draw_table_top(widths):
    return _draw_table_separator(widths, "\u250c", "\u252c", "\u2510", "\u2500")


def _draw_table_bottom(widths):
    return _draw_table_separator(widths, "\u2514", "\u2534", "\u2518", "\u2500")


def render_ansi(project_data, deps_md, comms, budget, agent_data, show_detail):
    """Render the dashboard using plain ANSI escape codes."""
    _clear_screen()
    w = _term_width()

    project_name = project_data.get("project_name", "Unknown")
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Header box
    print(_draw_box_top(w))
    title = f"{_BOLD}{_WHITE}SFORZA CONTROL PLANE{_RESET}"
    print(_draw_box_mid(title, w))
    sub = f"{_DIM}Project:{_RESET} {_BOLD}{_CYAN}{project_name}{_RESET}    {_DIM}{now_str}{_RESET}"
    print(_draw_box_mid(sub, w))
    print(_draw_box_bottom(w))
    print()

    # --- Active Teams ---
    teams = project_data.get("active_teams", [])
    team_count = len(teams)
    print(f"{_BOLD}{_WHITE}ACTIVE TEAMS ({team_count}){_RESET}")

    if teams:
        # Determine column widths
        col_team = max(16, min(24, w // 5))
        col_status = 8
        col_phase = max(12, min(20, w // 5))
        col_progress = 10
        col_cost = 10
        widths = [col_team, col_status, col_phase, col_progress, col_cost]

        # Header
        print(_draw_table_top(widths))
        headers = [
            f"{_BOLD}Team{_RESET}",
            f"{_BOLD}Status{_RESET}",
            f"{_BOLD}Phase{_RESET}",
            f"{_BOLD}Progress{_RESET}",
            f"{_BOLD}Cost{_RESET}",
        ]
        print(_draw_table_row(headers, widths))
        print(_draw_table_separator(widths))

        for team in teams:
            name = _truncate(
                team.get("team", "unknown").replace("-", " ").title(), col_team
            )
            status = team.get("status", "offline")
            dot = _ansi_status_dot(status)
            phase = _truncate(
                team.get("phase", "-").replace("-", " ").title(), col_phase
            )
            progress = _extract_progress(team.get("progress", 0))
            cost = _extract_cost(team.get("cost"))
            cost_str = f"${cost:,.2f}" if cost is not None else "-"
            progress_str = f"{progress}%"

            print(_draw_table_row(
                [name, dot, phase, progress_str, cost_str],
                widths,
            ))

        print(_draw_table_bottom(widths))
    else:
        print(f"  {_DIM}No teams active{_RESET}")
    print()

    # --- Budget ---
    print(f"{_BOLD}{_WHITE}BUDGET{_RESET}")
    pct = budget["percentage"]
    bar = _ansi_progress_bar(pct, width=30)

    if budget["spent"] > 0:
        if pct > 90:
            pct_color = _RED
        elif pct > 75:
            pct_color = _YELLOW
        else:
            pct_color = _GREEN
        print(
            f"  Used: {_BOLD}${budget['spent']:,.2f}{_RESET} / "
            f"${budget['budget']:,.2f} weekly budget "
            f"({pct_color}{pct:.0f}%{_RESET})"
        )
        print(f"  {bar}")
        print(f"  Status: {pct_color}{budget['status']}{_RESET}")
    else:
        print(f"  Budget: ${budget['budget']:,.2f} weekly")
        print(f"  {_DIM}No cost data reported yet{_RESET}")
    print()

    # --- Dependencies ---
    all_deps = []
    json_deps = project_data.get("dependencies", [])
    for d in json_deps:
        all_deps.append({
            "from": d.get("from_team", "?"),
            "to": d.get("to_team", "?"),
            "need": d.get("dependency", "-"),
            "status": d.get("status", "unknown"),
        })
    for d in deps_md:
        key = (d.get("from_team", ""), d.get("to_team", ""), d.get("dependency", ""))
        already = any(
            (x["from"] == key[0] and x["to"] == key[1] and x["need"] == key[2])
            for x in all_deps
        )
        if not already:
            all_deps.append({
                "from": d.get("from_team", "?"),
                "to": d.get("to_team", "?"),
                "need": d.get("dependency", "-"),
                "status": d.get("status", "unknown"),
            })

    dep_count = len(all_deps)
    print(f"{_BOLD}{_WHITE}DEPENDENCIES ({dep_count}){_RESET}")

    if all_deps:
        col_from = max(12, min(18, w // 5))
        col_to = max(12, min(18, w // 5))
        col_need = max(16, min(24, w // 4))
        col_dstatus = 10
        dwidths = [col_from, col_to, col_need, col_dstatus]

        print(_draw_table_top(dwidths))
        print(_draw_table_row(
            [
                f"{_BOLD}From{_RESET}",
                f"{_BOLD}To{_RESET}",
                f"{_BOLD}Need{_RESET}",
                f"{_BOLD}Status{_RESET}",
            ],
            dwidths,
        ))
        print(_draw_table_separator(dwidths))

        for d in all_deps:
            from_name = _truncate(d["from"].replace("-", " ").title(), col_from)
            to_name = _truncate(d["to"].replace("-", " ").title(), col_to)
            need = _truncate(d["need"], col_need)
            status_text = _ansi_dep_status(d["status"])

            print(_draw_table_row(
                [from_name, to_name, need, status_text],
                dwidths,
            ))

        print(_draw_table_bottom(dwidths))
    else:
        print(f"  {_DIM}No dependencies tracked{_RESET}")
    print()

    # --- Agent Status (detail mode) ---
    if show_detail and agent_data.get("agents"):
        agents = agent_data["agents"]
        print(f"{_BOLD}{_WHITE}AGENT STATUS ({len(agents)}){_RESET}")

        col_aname = max(16, min(22, w // 4))
        col_astatus = 8
        col_atask = max(20, min(30, w // 3))
        col_aprog = 10
        awidths = [col_aname, col_astatus, col_atask, col_aprog]

        print(_draw_table_top(awidths))
        print(_draw_table_row(
            [
                f"{_BOLD}Agent{_RESET}",
                f"{_BOLD}Status{_RESET}",
                f"{_BOLD}Task{_RESET}",
                f"{_BOLD}Progress{_RESET}",
            ],
            awidths,
        ))
        print(_draw_table_separator(awidths))

        for name, info in sorted(agents.items()):
            status = info.get("status", "offline")
            task = _truncate(str(info.get("current_task", "-")), col_atask)
            progress = info.get("progress", 0)
            print(_draw_table_row(
                [name, _ansi_status_dot(status), task, f"{progress}%"],
                awidths,
            ))

        print(_draw_table_bottom(awidths))
        print()

    # --- Recent Activity ---
    print(f"{_BOLD}{_WHITE}RECENT ACTIVITY{_RESET}")
    if comms:
        for entry in comms:
            ts = entry.get("time", "??:??")
            fr = entry.get("from_team", "?")
            to = entry.get("to_team", "?")
            msg = entry.get("message", "")
            priority = entry.get("priority")

            ptag = ""
            if priority:
                p = priority.lower()
                if p == "high":
                    ptag = f" {_RED}{_BOLD}[HIGH]{_RESET}"
                elif p == "medium":
                    ptag = f" {_YELLOW}[MED]{_RESET}"
                elif p == "low":
                    ptag = f" {_DIM}[LOW]{_RESET}"

            print(
                f"  {_DIM}[{ts}]{_RESET} {_BOLD}{fr}{_RESET} -> {to}: "
                f"{_truncate(msg, w - 40)}{ptag}"
            )
    else:
        print(f"  {_DIM}No messages yet{_RESET}")
    print()

    # Footer
    detail_hint = "'d' details ON" if show_detail else "'d' for details"
    print(
        f"{_DIM}Press 'r' to refresh | 'q' to quit | {detail_hint}  "
        f"(auto-refresh 5s){_RESET}"
    )


# ---------------------------------------------------------------------------
# Keyboard input helpers (non-blocking, no curses)
# ---------------------------------------------------------------------------

class _RawTerminal:
    """Context manager to set the terminal to raw (non-canonical) mode.

    Allows reading single keypresses without waiting for Enter.
    Falls back gracefully when stdin is not a TTY (e.g. piped input).
    """

    def __init__(self):
        self._fd = None
        self._old_settings = None

    def __enter__(self):
        try:
            self._fd = sys.stdin.fileno()
            self._old_settings = termios.tcgetattr(self._fd)
            tty.setcbreak(self._fd)
        except (termios.error, ValueError, io.UnsupportedOperation):
            self._fd = None
        return self

    def __exit__(self, *args):
        if self._fd is not None and self._old_settings is not None:
            try:
                termios.tcsetattr(self._fd, termios.TCSADRAIN, self._old_settings)
            except termios.error:
                pass

    def key_available(self, timeout=0.1):
        """Check if a keypress is available within *timeout* seconds."""
        if self._fd is None:
            time.sleep(timeout)
            return False
        try:
            rlist, _, _ = select.select([sys.stdin], [], [], timeout)
            return bool(rlist)
        except (ValueError, OSError):
            return False

    def read_key(self):
        """Read a single character from stdin."""
        if self._fd is None:
            return ""
        try:
            return sys.stdin.read(1)
        except (IOError, OSError):
            return ""


# We need io for the UnsupportedOperation reference in _RawTerminal
import io  # noqa: E402 (placed here to keep the class self-contained)


# ---------------------------------------------------------------------------
# Main dashboard loop
# ---------------------------------------------------------------------------

def _load_all_data(project_root):
    """Read all data sources and return them as a tuple."""
    project_data = read_project_status(project_root)
    deps_md = read_dependency_tracker(project_root)
    comms = read_communication_log(project_root)
    budget = compute_budget(project_data)
    agent_data = read_agent_status(project_root)
    return project_data, deps_md, comms, budget, agent_data


def run_dashboard(project_root, refresh_interval=5):
    """Run the auto-refreshing dashboard loop.

    Args:
        project_root (Path): Absolute path to the project directory.
        refresh_interval (int): Seconds between auto-refreshes.
    """
    show_detail = False

    # Handle Ctrl+C gracefully
    def _sigint_handler(sig, frame):
        _clear_screen()
        print("Control Plane exited.")
        sys.exit(0)

    signal.signal(signal.SIGINT, _sigint_handler)

    with _RawTerminal() as term:
        while True:
            # Load data
            project_data, deps_md, comms, budget, agent_data = _load_all_data(
                project_root
            )

            # Render
            if _USE_RICH:
                render_rich(
                    project_data, deps_md, comms, budget, agent_data, show_detail
                )
            else:
                render_ansi(
                    project_data, deps_md, comms, budget, agent_data, show_detail
                )

            # Wait for keypress or timeout
            elapsed = 0.0
            poll_interval = 0.15  # check keys every 150ms
            while elapsed < refresh_interval:
                if term.key_available(poll_interval):
                    key = term.read_key()
                    if key in ("q", "Q"):
                        _clear_screen()
                        print("Control Plane exited.")
                        return
                    elif key in ("r", "R"):
                        break  # force refresh
                    elif key in ("d", "D"):
                        show_detail = not show_detail
                        break  # re-render immediately
                elapsed += poll_interval


def run_once(project_root):
    """Render the dashboard a single time and exit (non-interactive mode).

    Useful when stdout is not a TTY (e.g. piped to a file or another program).
    """
    project_data, deps_md, comms, budget, agent_data = _load_all_data(project_root)

    if _USE_RICH:
        render_rich(project_data, deps_md, comms, budget, agent_data, show_detail=False)
    else:
        render_ansi(project_data, deps_md, comms, budget, agent_data, show_detail=False)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _build_parser():
    parser = argparse.ArgumentParser(
        description=(
            "Sforza Control Plane -- terminal dashboard for monitoring "
            "multi-agent projects."
        ),
        epilog=(
            "Examples:\n"
            "  %(prog)s --project /path/to/my-project\n"
            "  %(prog)s                                  # auto-detect from cwd\n"
            "  %(prog)s --once                           # single render, then exit\n"
            "  %(prog)s --refresh 10                     # refresh every 10 seconds\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--project", "-p",
        metavar="PATH",
        default=None,
        help=(
            "Path to the project root (must contain shared-workspace/). "
            "Defaults to auto-detection from the current working directory."
        ),
    )
    parser.add_argument(
        "--refresh", "-r",
        type=int,
        default=5,
        metavar="SEC",
        help="Auto-refresh interval in seconds (default: 5).",
    )
    parser.add_argument(
        "--once",
        action="store_true",
        help="Render the dashboard once and exit (non-interactive).",
    )
    parser.add_argument(
        "--no-color",
        action="store_true",
        help="Disable colored output.",
    )
    return parser


def main():
    parser = _build_parser()
    args = parser.parse_args()

    # Disable color if requested
    if args.no_color:
        global _USE_RICH, _BOLD, _DIM, _RED, _GREEN, _YELLOW, _BLUE
        global _MAGENTA, _CYAN, _WHITE, _RESET
        global _BG_BLUE, _BG_GREEN, _BG_RED, _BG_YELLOW
        _USE_RICH = False
        _BOLD = _DIM = _RED = _GREEN = _YELLOW = _BLUE = ""
        _MAGENTA = _CYAN = _WHITE = _RESET = ""
        _BG_BLUE = _BG_GREEN = _BG_RED = _BG_YELLOW = ""

    # Find project root
    project_root = _find_project_root(args.project)

    if project_root is None:
        hint_path = args.project if args.project else os.getcwd()
        print(
            f"Error: Could not find {STATUS_FILE} in or above '{hint_path}'.",
            file=sys.stderr,
        )
        print(
            "Hint: Use --project /path/to/project or run from within a project "
            "directory.",
            file=sys.stderr,
        )
        sys.exit(1)

    project_root = Path(project_root).resolve()

    if args.once or not sys.stdin.isatty():
        run_once(project_root)
    else:
        run_dashboard(project_root, refresh_interval=args.refresh)


if __name__ == "__main__":
    main()
