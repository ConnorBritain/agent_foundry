#!/usr/bin/env bash
# Sforza — Launch All Teams in Parallel (tmux)
# Requires: tmux, Claude Code CLI
#
# Usage: ./launch-scripts/start-all-parallel.sh <project-dir> [team1 team2 ...]
#
# If no teams specified, reads from PROJECT_CHARTER.md (Phase 1 teams).
# Creates a tmux session per team and an orchestrator monitoring session.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SFORZA_ROOT="$(dirname "$SCRIPT_DIR")"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

info()    { echo -e "${BLUE}[INFO]${NC} $1"; }
success() { echo -e "${GREEN}[OK]${NC} $1"; }
warn()    { echo -e "${YELLOW}[WARN]${NC} $1"; }
error()   { echo -e "${RED}[ERROR]${NC} $1"; exit 1; }

# Check tmux
if ! command -v tmux &>/dev/null; then
    error "tmux is required for parallel execution.\n  Install: brew install tmux (macOS) or apt install tmux (Linux)\n\n  Alternative: Open multiple terminal tabs and run each team script separately."
fi

PROJECT_DIR="${1:-}"
shift 2>/dev/null || true
TEAMS=("$@")

if [[ -z "$PROJECT_DIR" ]]; then
    error "Usage: $0 <project-dir> [team1 team2 ...]\n  Example: $0 projects/my-startup c-suite research-deep-dive content-creation"
fi

PROJECT_DIR="$(cd "$PROJECT_DIR" && pwd)"

# If no teams specified, default to a common Phase 1 set
if [[ ${#TEAMS[@]} -eq 0 ]]; then
    warn "No teams specified. Launching default Phase 1 teams."
    TEAMS=("c-suite" "research-deep-dive" "content-creation")
fi

SESSION_NAME="sforza"

echo ""
echo -e "${BOLD}${CYAN}Sforza — Parallel Launch${NC}"
echo ""
echo "  Project: $PROJECT_DIR"
echo "  Teams:   ${TEAMS[*]}"
echo "  Session: tmux $SESSION_NAME"
echo ""

# Kill existing session if any
tmux kill-session -t "$SESSION_NAME" 2>/dev/null || true

# Create the tmux session with the first team
FIRST_TEAM="${TEAMS[0]}"
tmux new-session -d -s "$SESSION_NAME" -n "$FIRST_TEAM" \
    "$SCRIPT_DIR/start-team.sh $FIRST_TEAM $PROJECT_DIR; echo 'Team complete. Press Enter to close.'; read"
success "Launched $FIRST_TEAM"

# Add remaining teams as new windows
for TEAM in "${TEAMS[@]:1}"; do
    tmux new-window -t "$SESSION_NAME" -n "$TEAM" \
        "$SCRIPT_DIR/start-team.sh $TEAM $PROJECT_DIR; echo 'Team complete. Press Enter to close.'; read"
    success "Launched $TEAM"
done

# Add a monitoring window
tmux new-window -t "$SESSION_NAME" -n "monitor" \
    "echo 'Sforza Control Plane'; echo ''; python3 $SFORZA_ROOT/common/utilities/control-plane.py --project $PROJECT_DIR 2>/dev/null || (echo 'Control plane not available. Watching status file...'; echo ''; watch -n 5 cat $PROJECT_DIR/shared-workspace/project-status.json)"

echo ""
success "All teams launched in tmux session: $SESSION_NAME"
echo ""
echo -e "${BOLD}Commands:${NC}"
echo "  Attach to session:   tmux attach -t $SESSION_NAME"
echo "  List windows:        tmux list-windows -t $SESSION_NAME"
echo "  Switch to team:      tmux select-window -t $SESSION_NAME:<team-name>"
echo "  Switch to monitor:   tmux select-window -t $SESSION_NAME:monitor"
echo "  Stop all:            ./launch-scripts/stop-all.sh"
echo ""

# Attach to the session
tmux attach -t "$SESSION_NAME"
