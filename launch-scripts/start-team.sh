#!/usr/bin/env bash
# Sforza — Generic Team Launch Script
# Usage: ./launch-scripts/start-team.sh <team-name> <project-dir>
#
# This is the shared launcher used by all team-specific scripts.
# It can also be called directly for any team.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FOUNDRY_ROOT="$(dirname "$SCRIPT_DIR")"

# Colors
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

DRY_RUN=false
ARGS=()
for arg in "$@"; do
    case "$arg" in
        --dry-run) DRY_RUN=true ;;
        *) ARGS+=("$arg") ;;
    esac
done

TEAM_NAME="${ARGS[0]:-}"
PROJECT_DIR="${ARGS[1]:-}"

if [[ -z "$TEAM_NAME" ]]; then
    echo "Usage: $0 <team-name> <project-dir>"
    echo ""
    echo "Available teams:"
    echo "  c-suite              - Strategy, financials, pitch decks"
    echo "  web-app-development  - Full-stack SaaS applications"
    echo "  sales-marketing      - Go-to-market execution"
    echo "  recruitment-hr       - People operations"
    echo "  content-creation     - Research-backed content"
    echo "  code-implementation  - Feature development"
    echo "  project-planning     - Multi-team coordination"
    echo "  research-deep-dive   - Deep research"
    exit 1
fi

if [[ -z "$PROJECT_DIR" ]]; then
    # Try to auto-detect from cwd
    if [[ -f "PROJECT_CHARTER.md" ]]; then
        PROJECT_DIR="$(pwd)"
    elif [[ -f "shared-workspace/project-status.json" ]]; then
        PROJECT_DIR="$(pwd)"
    else
        error "No project directory specified and none detected in cwd.\nUsage: $0 <team-name> <project-dir>"
    fi
fi

# Validate team exists
TEAM_DIR="$FOUNDRY_ROOT/teams/$TEAM_NAME"
if [[ ! -d "$TEAM_DIR" ]]; then
    error "Team not found: $TEAM_NAME\nLook in $FOUNDRY_ROOT/teams/ for available teams."
fi

# Validate project exists
if [[ ! -f "$PROJECT_DIR/PROJECT_CHARTER.md" ]] && [[ ! -f "$PROJECT_DIR/shared-workspace/project-status.json" ]]; then
    warn "No PROJECT_CHARTER.md found in $PROJECT_DIR"
    warn "Run ./initialize.sh first to create a project."
fi

# Create team workspace and artifacts directory
TEAM_WORKSPACE="$PROJECT_DIR/${TEAM_NAME}-workspace"
ARTIFACTS_DIR="$PROJECT_DIR/shared-workspace/artifacts/$TEAM_NAME"
mkdir -p "$TEAM_WORKSPACE"
mkdir -p "$ARTIFACTS_DIR"

echo ""
echo -e "${BOLD}${CYAN}Sforza — Launching Team${NC}"
echo ""
echo "  Team:      $TEAM_NAME"
echo "  Template:  $TEAM_DIR"
echo "  Project:   $PROJECT_DIR"
echo "  Workspace: $TEAM_WORKSPACE"
echo "  Artifacts: $ARTIFACTS_DIR"
echo ""

# Build the initial prompt for Claude Code
CHARTER_PATH="$PROJECT_DIR/PROJECT_CHARTER.md"
STATUS_PATH="$PROJECT_DIR/shared-workspace/project-status.json"

PROMPT="You are launching the ${TEAM_NAME} team for an Sforza project.

TEAM TEMPLATE LOCATION: ${TEAM_DIR}
Read the following files to understand your team:
- ${TEAM_DIR}/TEAM_SPEC.md (team specification and agent roster)
- ${TEAM_DIR}/ORCHESTRATION.md (execution phases and coordination)
- ${TEAM_DIR}/CONFIG.md (configuration)
- ${TEAM_DIR}/MODEL_CONFIGS.md (model selection)

PROJECT CONTEXT:
- Project charter: ${CHARTER_PATH}
- Project status: ${STATUS_PATH}
- Your workspace: ${TEAM_WORKSPACE}
- Write deliverables to: ${ARTIFACTS_DIR}
- Cross-team communication: ${PROJECT_DIR}/shared-workspace/cross-team-communication.md
- Dependency tracker: ${PROJECT_DIR}/shared-workspace/dependency-tracker.md

INSTRUCTIONS:
1. Read the team spec and project charter
2. Start as the Coordinator agent for this team
3. Execute the phases defined in ORCHESTRATION.md
4. Write all deliverables to the artifacts directory
5. Update project-status.json at each phase transition
6. Post cross-team messages when producing artifacts other teams need
7. Track costs and report at phase completion

Begin by reading TEAM_SPEC.md and PROJECT_CHARTER.md, then introduce yourself and start Phase 1."

# Dry-run mode: print prompt and exit
if [[ "$DRY_RUN" == "true" ]]; then
    echo -e "${BOLD}${YELLOW}[DRY RUN]${NC} Would launch with this prompt:"
    echo ""
    echo "────────────────────────────────────"
    echo "$PROMPT"
    echo "────────────────────────────────────"
    echo ""
    echo -e "${YELLOW}[DRY RUN]${NC} No Claude Code session launched."
    echo "$PROMPT" > "$TEAM_WORKSPACE/.launch-prompt.md"
    success "Prompt saved to $TEAM_WORKSPACE/.launch-prompt.md"
    exit 0
fi

# Check if Claude Code CLI is available
if command -v claude &>/dev/null; then
    info "Launching Claude Code session..."
    echo ""
    cd "$TEAM_WORKSPACE"
    claude --print "$PROMPT"
else
    warn "Claude Code CLI not found."
    echo ""
    echo -e "${BOLD}Manual launch instructions:${NC}"
    echo ""
    echo "  1. Open Claude Code (web or CLI)"
    echo "  2. Navigate to: $TEAM_WORKSPACE"
    echo "  3. Paste this prompt:"
    echo ""
    echo "  ---"
    echo "$PROMPT" | head -20
    echo "  ..."
    echo "  ---"
    echo ""
    echo "  (Full prompt saved to $TEAM_WORKSPACE/.launch-prompt.md)"

    # Save full prompt for manual use
    echo "$PROMPT" > "$TEAM_WORKSPACE/.launch-prompt.md"
    success "Prompt saved to $TEAM_WORKSPACE/.launch-prompt.md"
fi
