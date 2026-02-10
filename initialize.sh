#!/usr/bin/env bash
# Agent Foundry — Project Initialization Script
# Usage: ./initialize.sh [project-name]
#
# This script:
#   1. Creates a project workspace directory
#   2. Initializes shared-workspace/ structure
#   3. Launches Claude Code with the Orchestrator Agent
#   4. Opens the initialization interview

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FOUNDRY_ROOT="$SCRIPT_DIR"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

banner() {
    echo ""
    echo -e "${BOLD}${CYAN}"
    echo "    █████╗  ██████╗ ███████╗███╗   ██╗████████╗"
    echo "   ██╔══██╗██╔════╝ ██╔════╝████╗  ██║╚══██╔══╝"
    echo "   ███████║██║  ███╗█████╗  ██╔██╗ ██║   ██║   "
    echo "   ██╔══██║██║   ██║██╔══╝  ██║╚██╗██║   ██║   "
    echo "   ██║  ██║╚██████╔╝███████╗██║ ╚████║   ██║   "
    echo "   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝   "
    echo ""
    echo "   ███████╗ ██████╗ ██╗   ██╗███╗   ██╗██████╗ ██████╗ ██╗   ██╗"
    echo "   ██╔════╝██╔═══██╗██║   ██║████╗  ██║██╔══██╗██╔══██╗╚██╗ ██╔╝"
    echo "   █████╗  ██║   ██║██║   ██║██╔██╗ ██║██║  ██║██████╔╝ ╚████╔╝ "
    echo "   ██╔══╝  ██║   ██║██║   ██║██║╚██╗██║██║  ██║██╔══██╗  ╚██╔╝  "
    echo "   ██║     ╚██████╔╝╚██████╔╝██║ ╚████║██████╔╝██║  ██║   ██║   "
    echo "   ╚═╝      ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝   ╚═╝   "
    echo -e "${NC}"
    echo -e "   ${BOLD}From idea to deployed business — all agents.${NC}"
    echo ""
}

info()    { echo -e "${BLUE}[INFO]${NC} $1"; }
success() { echo -e "${GREEN}[OK]${NC} $1"; }
warn()    { echo -e "${YELLOW}[WARN]${NC} $1"; }
error()   { echo -e "${RED}[ERROR]${NC} $1"; exit 1; }

check_dependencies() {
    info "Checking dependencies..."

    # Check for Claude Code CLI
    if command -v claude &>/dev/null; then
        success "Claude Code CLI found: $(claude --version 2>/dev/null || echo 'installed')"
    else
        warn "Claude Code CLI not found."
        echo "  Install it: https://docs.anthropic.com/en/docs/claude-code"
        echo "  You can still set up the project and launch manually."
        echo ""
        CLAUDE_AVAILABLE=false
    fi

    # Check for Python 3
    if command -v python3 &>/dev/null; then
        success "Python 3 found: $(python3 --version)"
    else
        error "Python 3 is required. Install it: https://python.org/downloads/"
    fi

    # Check for git
    if command -v git &>/dev/null; then
        success "Git found: $(git --version)"
    else
        error "Git is required. Install it: https://git-scm.com/"
    fi

    echo ""
}

prompt_project_name() {
    if [[ -n "${1:-}" ]]; then
        PROJECT_NAME="$1"
    else
        echo -e "${BOLD}What's your project name?${NC}"
        echo "  (This creates a workspace directory. Use lowercase with hyphens.)"
        echo ""
        read -rp "  Project name: " PROJECT_NAME
        echo ""
    fi

    # Sanitize: lowercase, replace spaces with hyphens, remove special chars
    PROJECT_SLUG=$(echo "$PROJECT_NAME" | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | sed 's/[^a-z0-9-]//g')

    if [[ -z "$PROJECT_SLUG" ]]; then
        error "Invalid project name. Use letters, numbers, and hyphens."
    fi

    PROJECT_DIR="$FOUNDRY_ROOT/projects/$PROJECT_SLUG"
}

create_workspace() {
    info "Creating project workspace: $PROJECT_DIR"

    if [[ -d "$PROJECT_DIR" ]]; then
        warn "Project directory already exists: $PROJECT_DIR"
        read -rp "  Overwrite? (y/N): " OVERWRITE
        if [[ "$OVERWRITE" != "y" && "$OVERWRITE" != "Y" ]]; then
            info "Keeping existing project. Launching orchestrator..."
            return
        fi
        rm -rf "$PROJECT_DIR"
    fi

    # Create project directory structure
    mkdir -p "$PROJECT_DIR"
    mkdir -p "$PROJECT_DIR/shared-workspace/artifacts"
    mkdir -p "$PROJECT_DIR/shared-workspace/weekly-summaries"
    mkdir -p "$PROJECT_DIR/scenarios"
    mkdir -p "$PROJECT_DIR/logs"

    # Initialize project-status.json
    cat > "$PROJECT_DIR/shared-workspace/project-status.json" <<JSONEOF
{
  "project_name": "$PROJECT_NAME",
  "project_slug": "$PROJECT_SLUG",
  "initialized": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "foundry_root": "$FOUNDRY_ROOT",
  "active_teams": [],
  "completed_teams": [],
  "dependencies": [],
  "budget": {
    "daily_limit": null,
    "weekly_limit": null,
    "monthly_limit": null,
    "spent_today": 0,
    "spent_this_week": 0,
    "spent_this_month": 0
  },
  "phase": "initialization"
}
JSONEOF

    # Initialize cross-team communication log
    cat > "$PROJECT_DIR/shared-workspace/cross-team-communication.md" <<'COMMEOF'
# Cross-Team Communication Log

## Active Messages

_No active messages yet. Teams will post here during execution._

---

## Archived Messages

_Resolved messages are moved here._
COMMEOF

    # Initialize dependency tracker
    cat > "$PROJECT_DIR/shared-workspace/dependency-tracker.md" <<'DEPEOF'
# Inter-Team Dependency Tracker

## Current Dependencies

| From Team | To Team | Dependency | Status | Due Date |
|-----------|---------|------------|--------|----------|
| _none yet_ | | | | |

## Resolved Dependencies

| From Team | To Team | Dependency | Completed |
|-----------|---------|------------|-----------|
| _none yet_ | | | |
DEPEOF

    success "Project workspace created: $PROJECT_DIR"
    echo ""
}

generate_charter_template() {
    # Copy the charter template into the project for the orchestrator to fill in
    if [[ -f "$FOUNDRY_ROOT/templates/PROJECT_CHARTER.md" ]]; then
        cp "$FOUNDRY_ROOT/templates/PROJECT_CHARTER.md" "$PROJECT_DIR/PROJECT_CHARTER.md"
        success "Charter template copied to project"
    else
        warn "Charter template not found at templates/PROJECT_CHARTER.md"
        info "The orchestrator will create one during the interview."
    fi
}

launch_orchestrator() {
    echo -e "${BOLD}${GREEN}Project workspace is ready!${NC}"
    echo ""
    echo "  Project:   $PROJECT_NAME"
    echo "  Location:  $PROJECT_DIR"
    echo ""

    if [[ "${CLAUDE_AVAILABLE:-true}" == "false" ]]; then
        echo -e "${BOLD}Next steps (manual):${NC}"
        echo ""
        echo "  1. Open Claude Code (web or CLI)"
        echo "  2. Navigate to: $PROJECT_DIR"
        echo "  3. Paste this prompt to start the Orchestrator:"
        echo ""
        echo -e "  ${CYAN}---${NC}"
        echo "  You are the Agent Foundry Orchestrator. Read ORCHESTRATOR.md at"
        echo "  $FOUNDRY_ROOT/ORCHESTRATOR.md for your full instructions."
        echo "  The project workspace is at: $PROJECT_DIR"
        echo "  Begin the initialization interview."
        echo -e "  ${CYAN}---${NC}"
        echo ""
        return
    fi

    echo -e "${BOLD}Launching the Orchestrator...${NC}"
    echo ""
    echo "  The Orchestrator will interview you about your project"
    echo "  and create an execution plan. This takes about 10-15 minutes."
    echo ""

    read -rp "  Launch now? (Y/n): " LAUNCH_NOW
    if [[ "$LAUNCH_NOW" == "n" || "$LAUNCH_NOW" == "N" ]]; then
        info "You can launch later with:"
        echo "  cd $PROJECT_DIR"
        echo "  claude --print \"Read $FOUNDRY_ROOT/ORCHESTRATOR.md and begin the initialization interview for project at $PROJECT_DIR\""
        return
    fi

    # Launch Claude Code with the Orchestrator prompt
    cd "$PROJECT_DIR"
    claude --print "You are the Agent Foundry Orchestrator. Read $FOUNDRY_ROOT/ORCHESTRATOR.md for your full system prompt and instructions. The project workspace is at: $PROJECT_DIR. The foundry root (with all team templates) is at: $FOUNDRY_ROOT. Begin the initialization interview now." 2>/dev/null || {
        warn "Could not auto-launch Claude Code."
        echo ""
        echo "  Launch manually:"
        echo "  cd $PROJECT_DIR"
        echo "  claude"
        echo ""
        echo "  Then paste this prompt:"
        echo "  Read $FOUNDRY_ROOT/ORCHESTRATOR.md and begin the initialization interview."
    }
}

# --- Main ---

banner
check_dependencies
prompt_project_name "${1:-}"
create_workspace
generate_charter_template
launch_orchestrator

echo ""
echo -e "${BOLD}${GREEN}Setup complete.${NC}"
echo ""
echo "  Useful commands:"
echo "    Monitor progress:  python3 $FOUNDRY_ROOT/common/utilities/control-plane.py --project $PROJECT_DIR"
echo "    Launch a team:     ./launch-scripts/start-<team-name>.sh $PROJECT_DIR"
echo "    View status:       cat $PROJECT_DIR/shared-workspace/project-status.json"
echo ""
