#!/usr/bin/env python3
"""
Display project-wide status across all active teams.
Reads from shared-workspace/project-status.json and renders
a formatted dashboard showing team progress, dependencies, and blockers.
"""

import json
import sys
import os
from datetime import datetime
from pathlib import Path

PROJECT_STATUS = "shared-workspace/project-status.json"

def show_dashboard():
    if not os.path.exists(PROJECT_STATUS):
        print(f"No project status file found at {PROJECT_STATUS}")
        print("Initialize with: python common/utilities/project-status-dashboard.py --init")
        sys.exit(1)

    with open(PROJECT_STATUS) as f:
        project = json.load(f)

    # Project header
    print(f"\n{'='*60}")
    print(f"  {project.get('project_name', 'Unknown')} - Project Status")
    print(f"  Initialized: {project.get('initialized', 'N/A')}")
    print(f"{'='*60}\n")

    # Active teams
    teams = project.get('active_teams', [])
    if teams:
        print("ACTIVE TEAMS")
        print(f"{'Team':<25} {'Status':<10} {'Phase':<25} {'Progress':<10}")
        print("-" * 70)
        for team in teams:
            status_icon = {'active': '[*]', 'awaiting': '[~]', 'offline': '[ ]'}.get(team.get('status', ''), '[ ]')
            print(f"{team.get('team', ''):<25} {status_icon:<10} {team.get('phase', ''):<25} {team.get('progress', ''):<10}")
        print()
    else:
        print("No active teams.\n")

    # Dependencies
    deps = project.get('dependencies', [])
    if deps:
        print("DEPENDENCIES")
        print(f"{'From':<20} {'To':<20} {'Need':<30} {'Status':<10}")
        print("-" * 80)
        for dep in deps:
            status_icon = 'DONE' if dep.get('status') == 'complete' else 'PENDING'
            print(f"{dep.get('from_team', ''):<20} {dep.get('to_team', ''):<20} {dep.get('dependency', ''):<30} {status_icon:<10}")
        print()

    # Summary
    active_count = sum(1 for t in teams if t.get('status') == 'active')
    awaiting_count = sum(1 for t in teams if t.get('status') == 'awaiting')
    pending_deps = sum(1 for d in deps if d.get('status') != 'complete')
    print(f"Summary: {active_count} active, {awaiting_count} awaiting, {pending_deps} pending dependencies")


def init_project(name):
    """Initialize a new project status file."""
    status = {
        "project_name": name,
        "initialized": datetime.now().isoformat(),
        "active_teams": [],
        "dependencies": []
    }
    os.makedirs(os.path.dirname(PROJECT_STATUS), exist_ok=True)
    with open(PROJECT_STATUS, 'w') as f:
        json.dump(status, f, indent=2)
    print(f"Initialized project: {name}")


def add_team(team_name, phase="setup"):
    """Add a team to the project."""
    with open(PROJECT_STATUS) as f:
        project = json.load(f)

    project['active_teams'].append({
        "team": team_name,
        "status": "active",
        "phase": phase,
        "progress": "0%",
        "artifacts_path": f"shared-workspace/artifacts/{team_name}/",
        "last_update": datetime.now().isoformat()
    })

    with open(PROJECT_STATUS, 'w') as f:
        json.dump(project, f, indent=2)
    print(f"Added team: {team_name}")


def add_dependency(from_team, to_team, dependency):
    """Add an inter-team dependency."""
    with open(PROJECT_STATUS) as f:
        project = json.load(f)

    project['dependencies'].append({
        "from_team": from_team,
        "to_team": to_team,
        "dependency": dependency,
        "status": "pending"
    })

    with open(PROJECT_STATUS, 'w') as f:
        json.dump(project, f, indent=2)
    print(f"Added dependency: {from_team} -> {to_team}: {dependency}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Multi-team project status dashboard")
    parser.add_argument("--init", metavar="PROJECT_NAME", help="Initialize a new project")
    parser.add_argument("--add-team", metavar="TEAM_NAME", help="Add a team")
    parser.add_argument("--add-dep", nargs=3, metavar=("FROM", "TO", "NEED"), help="Add dependency")
    parser.add_argument("--phase", default="setup", help="Initial phase for --add-team")

    args = parser.parse_args()

    if args.init:
        init_project(args.init)
    elif args.add_team:
        add_team(args.add_team, args.phase)
    elif args.add_dep:
        add_dependency(*args.add_dep)
    else:
        show_dashboard()
