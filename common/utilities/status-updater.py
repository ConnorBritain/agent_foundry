#!/usr/bin/env python3
"""
Agent status updater for multi-agent coordination.

Maintains a shared JSON registry of agent statuses so that every member of a
team can see what the others are doing.  Each call updates the calling agent's
entry and recomputes aggregate team metrics.

The status file lives at ``shared-state/agent-status.json`` relative to the
project root.

Usage:
    python status-updater.py <agent_name> <status> <task> <progress> [blocked_by]

Arguments:
    agent_name  Unique agent identifier (e.g. "implementation-a")
    status      One of: active, awaiting, blocked, completed, offline
    task        Short description of the current task
    progress    Integer 0-100 indicating completion percentage
    blocked_by  (optional) Name of the agent or resource this agent is waiting on

Examples:
    python status-updater.py coordinator active "Assigning tasks" 10
    python status-updater.py impl-a blocked "Waiting for API design" 30 coordinator
    python status-updater.py test-eng active "Running test suite" 80
    python status-updater.py impl-a completed "Feature implementation" 100
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path

# Path to the shared status registry (relative to project root)
STATUS_FILE = "shared-state/agent-status.json"

# Valid status values
VALID_STATUSES = {"active", "awaiting", "blocked", "completed", "offline"}


def _resolve_status_file():
    """Resolve the absolute path to the status file.

    Searches relative to CWD first, then falls back to the project root
    derived from this script's location (common/utilities/).
    """
    cwd_path = Path.cwd() / STATUS_FILE
    if cwd_path.parent.is_dir():
        return cwd_path

    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent.parent
    root_path = project_root / STATUS_FILE
    if root_path.parent.is_dir():
        return root_path

    return cwd_path


def _read_status():
    """Read the current status registry from disk.

    Returns:
        dict: The full status document with ``agents`` and ``team_metrics``.
    """
    status_path = _resolve_status_file()
    default = {
        "last_updated": None,
        "agents": {},
        "team_metrics": {
            "total_agents": 0,
            "active": 0,
            "awaiting": 0,
            "blocked": 0,
            "completed": 0,
            "offline": 0,
        },
    }
    if not status_path.exists():
        return default

    try:
        with open(status_path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
    except (json.JSONDecodeError, IOError):
        return default

    if not isinstance(data, dict):
        return default

    # Ensure required top-level keys exist
    data.setdefault("agents", {})
    data.setdefault("team_metrics", default["team_metrics"])
    return data


def _write_status(data):
    """Persist the status registry to disk.

    Args:
        data (dict): The full status document to write.
    """
    status_path = _resolve_status_file()
    status_path.parent.mkdir(parents=True, exist_ok=True)
    with open(status_path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2)


def _compute_metrics(agents):
    """Recompute aggregate team metrics from individual agent records.

    Args:
        agents (dict): Mapping of agent names to their status records.

    Returns:
        dict: Aggregate metric counts.
    """
    counts = {s: 0 for s in VALID_STATUSES}
    for record in agents.values():
        status = record.get("status", "offline")
        if status in counts:
            counts[status] += 1
        else:
            counts["offline"] += 1

    return {
        "total_agents": len(agents),
        "active": counts["active"],
        "awaiting": counts["awaiting"],
        "blocked": counts["blocked"],
        "completed": counts["completed"],
        "offline": counts["offline"],
    }


def update_status(agent_name, status, task, progress, blocked_by=None):
    """Update an agent's status in the shared registry.

    Args:
        agent_name (str): Unique agent identifier.
        status (str): One of ``active``, ``awaiting``, ``blocked``,
            ``completed``, ``offline``.
        task (str): Short description of the current task.
        progress (int): Percentage complete (0-100).
        blocked_by (str, optional): Agent or resource causing a block.

    Returns:
        dict: The updated full status document.

    Raises:
        ValueError: If *status* is not a recognized value or *progress* is
            out of range.
    """
    if status not in VALID_STATUSES:
        raise ValueError(
            f"Invalid status '{status}'. Must be one of: {', '.join(sorted(VALID_STATUSES))}"
        )

    progress = int(progress)
    if progress < 0 or progress > 100:
        raise ValueError(f"Progress must be 0-100, got {progress}")

    data = _read_status()
    now = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")

    # Build the agent's status record
    agent_record = {
        "status": status,
        "pid": os.environ.get("CLAUDE_SESSION_ID", str(os.getpid())),
        "current_task": task,
        "progress": progress,
        "last_heartbeat": now,
    }
    if blocked_by:
        agent_record["blocked_by"] = blocked_by

    data["agents"][agent_name] = agent_record
    data["last_updated"] = now
    data["team_metrics"] = _compute_metrics(data["agents"])

    _write_status(data)
    return data


def get_status(agent_name=None):
    """Retrieve the current status of one agent or the whole team.

    Args:
        agent_name (str, optional): If given, return just that agent's record.

    Returns:
        dict: The agent's record, or the full status document if
        *agent_name* is ``None``.
    """
    data = _read_status()
    if agent_name:
        return data["agents"].get(agent_name, {"error": f"Agent '{agent_name}' not found"})
    return data


def remove_agent(agent_name):
    """Remove an agent from the status registry entirely.

    Args:
        agent_name (str): The agent to remove.

    Returns:
        dict: Result with ``success`` and ``message``.
    """
    data = _read_status()
    if agent_name not in data["agents"]:
        return {"success": False, "message": f"Agent '{agent_name}' not found"}

    del data["agents"][agent_name]
    data["last_updated"] = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")
    data["team_metrics"] = _compute_metrics(data["agents"])
    _write_status(data)
    return {"success": True, "message": f"Agent '{agent_name}' removed"}


def reset_all():
    """Reset the entire status registry to an empty state.

    Returns:
        dict: The empty status document that was written.
    """
    data = {
        "last_updated": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f"),
        "agents": {},
        "team_metrics": {
            "total_agents": 0,
            "active": 0,
            "awaiting": 0,
            "blocked": 0,
            "completed": 0,
            "offline": 0,
        },
    }
    _write_status(data)
    return data


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _build_parser():
    parser = argparse.ArgumentParser(
        description="Update or query agent status in the shared registry.",
        epilog=(
            "Examples:\n"
            '  %(prog)s update coordinator active "Assigning tasks" 10\n'
            '  %(prog)s update impl-a blocked "Waiting for API" 30 coordinator\n'
            "  %(prog)s get coordinator\n"
            "  %(prog)s get\n"
            "  %(prog)s remove impl-b\n"
            "  %(prog)s reset\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="command", help="Operation to perform")

    # update
    up = sub.add_parser("update", help="Update an agent's status")
    up.add_argument("agent_name", help="Agent identifier")
    up.add_argument(
        "status",
        choices=sorted(VALID_STATUSES),
        help="Agent status",
    )
    up.add_argument("task", help="Short task description")
    up.add_argument("progress", type=int, help="Completion percentage (0-100)")
    up.add_argument("blocked_by", nargs="?", default=None, help="Blocking agent/resource")

    # get
    gt = sub.add_parser("get", help="Get status for one or all agents")
    gt.add_argument("agent_name", nargs="?", default=None, help="Agent name (omit for all)")

    # remove
    rm = sub.add_parser("remove", help="Remove an agent from the registry")
    rm.add_argument("agent_name", help="Agent to remove")

    # reset
    sub.add_parser("reset", help="Reset the entire status registry")

    return parser


def _try_legacy_invocation():
    """Attempt backward-compatible positional-only invocation.

    Legacy format:
        status-updater.py <agent_name> <status> <task> <progress> [blocked_by]

    Returns True if the invocation was handled, False otherwise.
    """
    subcommands = {"update", "get", "remove", "reset", "-h", "--help"}
    if len(sys.argv) >= 5 and sys.argv[1] not in subcommands:
        agent_name = sys.argv[1]
        status = sys.argv[2]
        task = sys.argv[3]
        progress = sys.argv[4]
        blocked_by = sys.argv[5] if len(sys.argv) > 5 else None
        try:
            result = update_status(agent_name, status, task, progress, blocked_by)
            print(json.dumps(result, indent=2))
        except ValueError as exc:
            print(f"Error: {exc}", file=sys.stderr)
            sys.exit(1)
        return True
    return False


def main():
    # Try legacy positional invocation first (before argparse processes args)
    if _try_legacy_invocation():
        return

    parser = _build_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    if args.command == "update":
        try:
            result = update_status(
                args.agent_name, args.status, args.task,
                args.progress, args.blocked_by,
            )
        except ValueError as exc:
            print(f"Error: {exc}", file=sys.stderr)
            sys.exit(1)
    elif args.command == "get":
        result = get_status(args.agent_name)
    elif args.command == "remove":
        result = remove_agent(args.agent_name)
    elif args.command == "reset":
        result = reset_all()
    else:
        parser.print_help()
        sys.exit(1)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
