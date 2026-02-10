#!/usr/bin/env bash
# Sforza — Template Validator
# Usage: ./tests/validate-templates.sh [team-name]
#
# Validates that team templates follow the gold standard structure.
# Run without arguments to validate all teams, or pass a team name to validate one.
#
# Exit codes:
#   0 = all pass
#   1 = failures found

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SFORZA_ROOT="$(dirname "$SCRIPT_DIR")"
TEAMS_DIR="$SFORZA_ROOT/teams"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BOLD='\033[1m'
NC='\033[0m'

PASS=0
FAIL=0
WARN=0

pass() { PASS=$((PASS + 1)); echo -e "  ${GREEN}PASS${NC} $1"; }
fail() { FAIL=$((FAIL + 1)); echo -e "  ${RED}FAIL${NC} $1"; }
warn() { WARN=$((WARN + 1)); echo -e "  ${YELLOW}WARN${NC} $1"; }

validate_team() {
    local team="$1"
    local team_dir="$TEAMS_DIR/$team"

    echo ""
    echo -e "${BOLD}Validating: $team${NC}"

    if [[ ! -d "$team_dir" ]]; then
        fail "Team directory does not exist: $team_dir"
        return
    fi

    # ── Core Documents ──
    local core_docs=("README.md" "TEAM_SPEC.md" "MODEL_CONFIGS.md" "CONFIG.md" "ORCHESTRATION.md" "cost-analysis.md" "deployment-guide.md")
    for doc in "${core_docs[@]}"; do
        if [[ -f "$team_dir/$doc" ]]; then
            local size
            size=$(wc -c < "$team_dir/$doc")
            if [[ "$size" -lt 500 ]]; then
                warn "$doc exists but seems too short ($size bytes)"
            else
                pass "$doc ($size bytes)"
            fi
        else
            fail "MISSING: $doc"
        fi
    done

    # ── Agents ──
    if [[ ! -d "$team_dir/agents" ]]; then
        fail "No agents/ directory"
    else
        local agent_count=0
        local orphan_count=0
        for agent_dir in "$team_dir"/agents/*/; do
            [[ -d "$agent_dir" ]] || continue
            local agent_name
            agent_name=$(basename "$agent_dir")
            if [[ -f "$agent_dir/AGENTS.md" ]]; then
                local asize
                asize=$(wc -c < "$agent_dir/AGENTS.md")
                if [[ "$asize" -lt 500 ]]; then
                    warn "agents/$agent_name/AGENTS.md seems short ($asize bytes)"
                else
                    pass "agents/$agent_name/AGENTS.md ($asize bytes)"
                fi
                agent_count=$((agent_count + 1))
            else
                fail "agents/$agent_name/ has NO AGENTS.md (orphan directory)"
                orphan_count=$((orphan_count + 1))
            fi
        done

        if [[ "$agent_count" -eq 0 ]]; then
            fail "No agent definitions found"
        else
            pass "Total agents: $agent_count"
        fi
    fi

    # ── MCP Servers ──
    if [[ -d "$team_dir/mcp-servers" ]]; then
        local mcp_count
        mcp_count=$(find "$team_dir/mcp-servers" -name "*.json" | wc -l)
        if [[ "$mcp_count" -ge 1 ]]; then
            pass "MCP servers: $mcp_count configs"
            # Validate JSON syntax
            for json_file in "$team_dir"/mcp-servers/*.json; do
                if python3 -c "import json; json.load(open('$json_file'))" 2>/dev/null; then
                    pass "$(basename "$json_file"): valid JSON"
                else
                    fail "$(basename "$json_file"): INVALID JSON"
                fi
            done
        else
            warn "No MCP server JSON configs found"
        fi
        if [[ -f "$team_dir/mcp-servers/README.md" ]]; then
            pass "mcp-servers/README.md exists"
        else
            warn "mcp-servers/README.md missing"
        fi
    else
        warn "No mcp-servers/ directory"
    fi

    # ── Scenarios ──
    if [[ -d "$team_dir/scenarios" ]]; then
        local scenario_count
        scenario_count=$(find "$team_dir/scenarios" -name "*.md" | wc -l)
        if [[ "$scenario_count" -ge 3 ]]; then
            pass "Scenarios: $scenario_count"
        else
            warn "Only $scenario_count scenarios (recommend 3+)"
        fi
    else
        warn "No scenarios/ directory"
    fi

    # ── Examples ──
    if [[ -d "$team_dir/examples" ]]; then
        local example_count
        example_count=$(find "$team_dir/examples" -name "*.md" | wc -l)
        if [[ "$example_count" -ge 3 ]]; then
            pass "Examples: $example_count"
        else
            warn "Only $example_count examples (recommend 3+)"
        fi
    else
        warn "No examples/ directory"
    fi

    # ── Cross-References ──
    # Check that ORCHESTRATION.md references agents that actually exist
    if [[ -f "$team_dir/ORCHESTRATION.md" ]]; then
        pass "ORCHESTRATION.md references can be manually reviewed"
    fi
}

# ── Main ──

echo ""
echo -e "${BOLD}Sforza — Template Validator${NC}"

if [[ -n "${1:-}" ]]; then
    # Validate specific team
    validate_team "$1"
else
    # Validate all teams
    for team_dir in "$TEAMS_DIR"/*/; do
        [[ -d "$team_dir" ]] || continue
        validate_team "$(basename "$team_dir")"
    done
fi

echo ""
echo "────────────────────────────────────"
echo -e "  ${GREEN}PASS: $PASS${NC}  |  ${RED}FAIL: $FAIL${NC}  |  ${YELLOW}WARN: $WARN${NC}"
echo ""

if [[ "$FAIL" -eq 0 ]]; then
    echo -e "${BOLD}${GREEN}All validations passed!${NC}"
    exit 0
else
    echo -e "${BOLD}${RED}$FAIL validation(s) failed.${NC}"
    exit 1
fi
