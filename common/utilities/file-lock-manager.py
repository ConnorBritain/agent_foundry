#!/usr/bin/env python3
"""
File lock manager for parallel agent coordination.

Prevents write conflicts during multi-agent workflows by maintaining a
JSON-based file ownership registry. Each lock records which agent owns
which file, when the lock was acquired, and an optional reason.

Locks automatically expire after 30 minutes to prevent deadlocks from
crashed or abandoned agent sessions.

Usage:
    python file-lock-manager.py acquire <file_path> <agent_name> [reason]
    python file-lock-manager.py release <file_path> <agent_name>
    python file-lock-manager.py check   <file_path>

Examples:
    python file-lock-manager.py acquire src/main.py implementation-a "Refactoring entry point"
    python file-lock-manager.py check src/main.py
    python file-lock-manager.py release src/main.py implementation-a
"""

import argparse
import json
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path

# Path to the shared lock registry (relative to project root)
LOCK_FILE = "shared-state/file-ownership.json"

# Locks older than this are considered expired and can be reclaimed
LOCK_DURATION = timedelta(minutes=30)

# ISO format used for serializing timestamps
_ISO_FMT = "%Y-%m-%dT%H:%M:%S.%f"


def _resolve_lock_file():
    """Resolve the absolute path to the lock file.

    Walks up from the current working directory looking for the shared-state
    directory, falling back to a path relative to this script's location.
    """
    # Try relative to CWD first
    cwd_path = Path.cwd() / LOCK_FILE
    if cwd_path.parent.is_dir():
        return cwd_path

    # Try relative to the script's own location (common/utilities/)
    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent.parent  # up from common/utilities/
    root_path = project_root / LOCK_FILE
    if root_path.parent.is_dir():
        return root_path

    # Fallback: use CWD-relative and let callers handle missing dirs
    return cwd_path


def _read_locks():
    """Read the current lock registry from disk.

    Returns:
        dict: Mapping of file paths to their lock records.  Each record has
        keys: ``agent``, ``acquired``, ``reason``.
    """
    lock_path = _resolve_lock_file()
    if not lock_path.exists():
        return {}

    try:
        with open(lock_path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
    except (json.JSONDecodeError, IOError):
        return {}

    if not isinstance(data, dict):
        return {}
    return data


def _write_locks(locks):
    """Persist the lock registry to disk.

    Args:
        locks (dict): The full lock registry to write.
    """
    lock_path = _resolve_lock_file()
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    with open(lock_path, "w", encoding="utf-8") as fh:
        json.dump(locks, fh, indent=2)


def _is_expired(lock_record):
    """Check whether a lock record has exceeded LOCK_DURATION.

    Args:
        lock_record (dict): A single lock entry with an ``acquired`` timestamp.

    Returns:
        bool: True if the lock is expired.
    """
    try:
        acquired = datetime.strptime(lock_record["acquired"], _ISO_FMT)
    except (KeyError, ValueError):
        return True  # malformed records are treated as expired
    return datetime.utcnow() - acquired > LOCK_DURATION


def acquire_lock(file_path, agent_name, reason=""):
    """Attempt to acquire an exclusive lock on *file_path* for *agent_name*.

    If the file is already locked by another (non-expired) agent the
    acquisition is rejected and the function returns information about the
    current holder.

    Args:
        file_path (str): Path of the file to lock (used as the registry key).
        agent_name (str): Identifier of the requesting agent.
        reason (str, optional): Human-readable reason for the lock.

    Returns:
        dict: A result dictionary with keys ``success`` (bool), ``message``
        (str), and optionally ``lock`` (the new or existing lock record).
    """
    locks = _read_locks()
    now = datetime.utcnow()

    if file_path in locks:
        existing = locks[file_path]

        # Same agent can re-acquire (refresh) its own lock
        if existing.get("agent") == agent_name:
            locks[file_path] = {
                "agent": agent_name,
                "acquired": now.strftime(_ISO_FMT),
                "reason": reason or existing.get("reason", ""),
            }
            _write_locks(locks)
            return {
                "success": True,
                "message": f"Lock refreshed for {agent_name} on {file_path}",
                "lock": locks[file_path],
            }

        # If the existing lock is expired, reclaim it
        if _is_expired(existing):
            old_agent = existing.get("agent", "unknown")
            locks[file_path] = {
                "agent": agent_name,
                "acquired": now.strftime(_ISO_FMT),
                "reason": reason,
            }
            _write_locks(locks)
            return {
                "success": True,
                "message": (
                    f"Expired lock from {old_agent} reclaimed by {agent_name} "
                    f"on {file_path}"
                ),
                "lock": locks[file_path],
            }

        # Active lock held by a different agent -- reject
        return {
            "success": False,
            "message": (
                f"File {file_path} is locked by {existing.get('agent', 'unknown')} "
                f"(reason: {existing.get('reason', 'none')}). "
                f"Lock acquired at {existing.get('acquired', 'unknown')}."
            ),
            "lock": existing,
        }

    # No existing lock -- grant a new one
    locks[file_path] = {
        "agent": agent_name,
        "acquired": now.strftime(_ISO_FMT),
        "reason": reason,
    }
    _write_locks(locks)
    return {
        "success": True,
        "message": f"Lock acquired by {agent_name} on {file_path}",
        "lock": locks[file_path],
    }


def release_lock(file_path, agent_name):
    """Release the lock on *file_path* if it is held by *agent_name*.

    Args:
        file_path (str): Path of the file to unlock.
        agent_name (str): Identifier of the agent releasing the lock.

    Returns:
        dict: A result dictionary with ``success`` (bool) and ``message`` (str).
    """
    locks = _read_locks()

    if file_path not in locks:
        return {
            "success": True,
            "message": f"No lock exists for {file_path} (nothing to release)",
        }

    existing = locks[file_path]
    holder = existing.get("agent", "unknown")

    if holder != agent_name:
        return {
            "success": False,
            "message": (
                f"Cannot release lock on {file_path}: held by {holder}, "
                f"not {agent_name}"
            ),
        }

    del locks[file_path]
    _write_locks(locks)
    return {
        "success": True,
        "message": f"Lock released by {agent_name} on {file_path}",
    }


def check_lock(file_path):
    """Check the lock status of *file_path*.

    Args:
        file_path (str): Path to query.

    Returns:
        dict: Lock status with ``locked`` (bool), ``expired`` (bool if locked),
        ``holder`` (str or None), ``reason`` (str or None), and
        ``acquired`` (str or None).
    """
    locks = _read_locks()

    if file_path not in locks:
        return {
            "locked": False,
            "holder": None,
            "reason": None,
            "acquired": None,
        }

    record = locks[file_path]
    expired = _is_expired(record)
    return {
        "locked": not expired,
        "expired": expired,
        "holder": record.get("agent"),
        "reason": record.get("reason", ""),
        "acquired": record.get("acquired"),
    }


def list_locks():
    """List all current locks with their status.

    Returns:
        list[dict]: A list of lock records augmented with the file path and
        expiration status.
    """
    locks = _read_locks()
    results = []
    for fpath, record in locks.items():
        results.append({
            "file": fpath,
            "agent": record.get("agent"),
            "reason": record.get("reason", ""),
            "acquired": record.get("acquired"),
            "expired": _is_expired(record),
        })
    return results


def clean_expired():
    """Remove all expired locks from the registry.

    Returns:
        dict: Summary with ``removed`` (int) and ``remaining`` (int).
    """
    locks = _read_locks()
    expired_keys = [fp for fp, rec in locks.items() if _is_expired(rec)]
    for key in expired_keys:
        del locks[key]
    _write_locks(locks)
    return {
        "removed": len(expired_keys),
        "remaining": len(locks),
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _build_parser():
    parser = argparse.ArgumentParser(
        description="File lock manager for parallel agent coordination.",
        epilog=(
            "Examples:\n"
            "  %(prog)s acquire src/main.py impl-a \"Refactoring\"\n"
            "  %(prog)s check   src/main.py\n"
            "  %(prog)s release src/main.py impl-a\n"
            "  %(prog)s list\n"
            "  %(prog)s clean\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="command", help="Lock operation to perform")

    # acquire
    acq = sub.add_parser("acquire", help="Acquire a lock on a file")
    acq.add_argument("file_path", help="File path to lock")
    acq.add_argument("agent_name", help="Name of the agent requesting the lock")
    acq.add_argument("reason", nargs="?", default="", help="Reason for the lock")

    # release
    rel = sub.add_parser("release", help="Release a lock on a file")
    rel.add_argument("file_path", help="File path to unlock")
    rel.add_argument("agent_name", help="Name of the agent releasing the lock")

    # check
    chk = sub.add_parser("check", help="Check lock status of a file")
    chk.add_argument("file_path", help="File path to check")

    # list
    sub.add_parser("list", help="List all current locks")

    # clean
    sub.add_parser("clean", help="Remove expired locks")

    return parser


def main():
    parser = _build_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    if args.command == "acquire":
        result = acquire_lock(args.file_path, args.agent_name, args.reason)
    elif args.command == "release":
        result = release_lock(args.file_path, args.agent_name)
    elif args.command == "check":
        result = check_lock(args.file_path)
    elif args.command == "list":
        result = list_locks()
    elif args.command == "clean":
        result = clean_expired()
    else:
        parser.print_help()
        sys.exit(1)

    print(json.dumps(result, indent=2))

    # Exit with non-zero if an acquire/release failed
    if isinstance(result, dict) and result.get("success") is False:
        sys.exit(1)


if __name__ == "__main__":
    main()
