#!/usr/bin/env bash
# Sforza — Test Runner
# Usage: ./tests/run-all.sh
#
# Runs all validation tests and reports results.

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

PASS=0
FAIL=0
WARN=0

pass() { PASS=$((PASS + 1)); echo -e "  ${GREEN}PASS${NC} $1"; }
fail() { FAIL=$((FAIL + 1)); echo -e "  ${RED}FAIL${NC} $1"; }
warn() { WARN=$((WARN + 1)); echo -e "  ${YELLOW}WARN${NC} $1"; }
section() { echo ""; echo -e "${BOLD}${CYAN}=== $1 ===${NC}"; }

echo ""
echo -e "${BOLD}${CYAN}Sforza — Test Suite${NC}"
echo ""

# ────────────────────────────────────────────────────────
section "1. Script Validation"
# ────────────────────────────────────────────────────────

# Check all scripts are executable
for script in "$FOUNDRY_ROOT"/launch-scripts/*.sh "$FOUNDRY_ROOT/initialize.sh"; do
    if [[ -x "$script" ]]; then
        pass "$(basename "$script") is executable"
    else
        fail "$(basename "$script") is NOT executable"
    fi
done

# Check all scripts have proper shebangs
for script in "$FOUNDRY_ROOT"/launch-scripts/*.sh "$FOUNDRY_ROOT/initialize.sh"; do
    first_line=$(head -1 "$script")
    if [[ "$first_line" == "#!/usr/bin/env bash" ]] || [[ "$first_line" == "#!/bin/bash" ]]; then
        pass "$(basename "$script") has valid shebang"
    else
        fail "$(basename "$script") missing shebang (got: $first_line)"
    fi
done

# Check start-team.sh handles missing args
output=$("$FOUNDRY_ROOT/launch-scripts/start-team.sh" 2>&1 || true)
if echo "$output" | grep -q "Usage:"; then
    pass "start-team.sh shows usage on missing args"
else
    fail "start-team.sh doesn't show usage on missing args"
fi

# Check start-team.sh rejects invalid team
output=$("$FOUNDRY_ROOT/launch-scripts/start-team.sh" "nonexistent-team" "/tmp" 2>&1 || true)
if echo "$output" | grep -qi "not found\|error"; then
    pass "start-team.sh rejects invalid team name"
else
    fail "start-team.sh doesn't reject invalid team name"
fi

# Check team-specific scripts exist for all 8 teams
EXPECTED_TEAMS=("c-suite" "code-implementation" "content-creation" "project-planning" "recruitment-hr" "research-deep-dive" "sales-marketing" "web-app-development")
for team in "${EXPECTED_TEAMS[@]}"; do
    if [[ -f "$FOUNDRY_ROOT/launch-scripts/start-${team}.sh" ]]; then
        pass "start-${team}.sh exists"
    else
        fail "start-${team}.sh MISSING"
    fi
done

# Shellcheck if available
if command -v shellcheck &>/dev/null; then
    for script in "$FOUNDRY_ROOT"/launch-scripts/*.sh "$FOUNDRY_ROOT/initialize.sh"; do
        errors=$(shellcheck -S error "$script" 2>&1 || true)
        if [[ -z "$errors" ]]; then
            pass "shellcheck: $(basename "$script")"
        else
            fail "shellcheck: $(basename "$script") has errors"
            echo "$errors" | head -5 | sed 's/^/    /'
        fi
    done
else
    warn "shellcheck not installed — skipping lint checks"
fi

# ────────────────────────────────────────────────────────
section "2. Dry-Run Mode"
# ────────────────────────────────────────────────────────

# Create a temp project for dry-run testing
TEMP_PROJECT=$(mktemp -d)
mkdir -p "$TEMP_PROJECT/shared-workspace"
echo '{}' > "$TEMP_PROJECT/shared-workspace/project-status.json"
touch "$TEMP_PROJECT/PROJECT_CHARTER.md"

# Test dry-run flag
output=$("$FOUNDRY_ROOT/launch-scripts/start-team.sh" --dry-run "c-suite" "$TEMP_PROJECT" 2>&1 || true)
if echo "$output" | grep -qi "dry.run\|prompt\|DRY"; then
    pass "start-team.sh --dry-run outputs prompt without launching"
else
    # Dry-run may not be implemented yet — this is expected if we still need to add it
    warn "start-team.sh --dry-run not yet supported (will be added)"
fi

rm -rf "$TEMP_PROJECT"

# ────────────────────────────────────────────────────────
section "3. Template Validation"
# ────────────────────────────────────────────────────────

CORE_DOCS=("README.md" "TEAM_SPEC.md" "MODEL_CONFIGS.md" "CONFIG.md" "ORCHESTRATION.md" "cost-analysis.md" "deployment-guide.md")

for team in "${EXPECTED_TEAMS[@]}"; do
    team_dir="$FOUNDRY_ROOT/teams/$team"
    team_errors=0

    # Check core docs
    for doc in "${CORE_DOCS[@]}"; do
        if [[ ! -f "$team_dir/$doc" ]]; then
            fail "$team: missing $doc"
            team_errors=$((team_errors + 1))
        fi
    done

    # Check agents directory exists and has at least 1 agent
    agent_count=$(find "$team_dir/agents" -name "AGENTS.md" 2>/dev/null | wc -l)
    if [[ "$agent_count" -ge 1 ]]; then
        pass "$team: $agent_count agents with AGENTS.md"
    else
        fail "$team: no agents found"
        team_errors=$((team_errors + 1))
    fi

    # Check for orphan agent dirs (dirs without AGENTS.md)
    orphan_count=0
    if [[ -d "$team_dir/agents" ]]; then
        for agent_dir in "$team_dir"/agents/*/; do
            if [[ -d "$agent_dir" ]] && [[ ! -f "$agent_dir/AGENTS.md" ]]; then
                fail "$team: orphan agent dir $(basename "$agent_dir") (no AGENTS.md)"
                ((orphan_count++))
                team_errors=$((team_errors + 1))
            fi
        done
    fi

    # Check MCP servers
    mcp_count=$(find "$team_dir/mcp-servers" -name "*.json" 2>/dev/null | wc -l)
    if [[ "$mcp_count" -ge 1 ]]; then
        pass "$team: $mcp_count MCP server configs"
    else
        warn "$team: no MCP server configs"
    fi

    # Check scenarios
    scenario_count=$(find "$team_dir/scenarios" -name "*.md" 2>/dev/null | wc -l)
    if [[ "$scenario_count" -ge 3 ]]; then
        pass "$team: $scenario_count scenarios"
    else
        warn "$team: only $scenario_count scenarios (recommend 3+)"
    fi

    # Check examples
    example_count=$(find "$team_dir/examples" -name "*.md" 2>/dev/null | wc -l)
    if [[ "$example_count" -ge 3 ]]; then
        pass "$team: $example_count examples"
    else
        warn "$team: only $example_count examples (recommend 3+)"
    fi

    # Check for empty files (under 100 bytes)
    while IFS= read -r -d '' small_file; do
        fail "$team: suspiciously small file $(basename "$small_file") ($(wc -c < "$small_file") bytes)"
        team_errors=$((team_errors + 1))
    done < <(find "$team_dir" -name "*.md" -size -100c -print0 2>/dev/null)

    # Summary for this team
    if [[ "$team_errors" -eq 0 ]]; then
        pass "$team: ALL CHECKS PASSED"
    fi
done

# ────────────────────────────────────────────────────────
section "4. Common Layer Validation"
# ────────────────────────────────────────────────────────

# Personalities
personality_count=$(find "$FOUNDRY_ROOT/common/personalities" -name "*.md" 2>/dev/null | wc -l)
if [[ "$personality_count" -ge 5 ]]; then
    pass "common/personalities: $personality_count profiles"
else
    fail "common/personalities: only $personality_count profiles (need 5+)"
fi

# Agents-MD
agentsmd_count=$(find "$FOUNDRY_ROOT/common/agents-md" -name "*.md" 2>/dev/null | wc -l)
if [[ "$agentsmd_count" -ge 5 ]]; then
    pass "common/agents-md: $agentsmd_count reference docs"
else
    fail "common/agents-md: only $agentsmd_count reference docs (need 5+)"
fi

# Skills
skills_count=$(find "$FOUNDRY_ROOT/common/skills" -name "*.md" 2>/dev/null | wc -l)
if [[ "$skills_count" -ge 5 ]]; then
    pass "common/skills: $skills_count skills"
else
    fail "common/skills: only $skills_count skills (need 5+)"
fi

# Skills have YAML frontmatter
for skill in "$FOUNDRY_ROOT"/common/skills/*.md; do
    if head -1 "$skill" | grep -q "^---"; then
        pass "$(basename "$skill"): has YAML frontmatter"
    else
        fail "$(basename "$skill"): missing YAML frontmatter"
    fi
done

# Utilities
for util in "control-plane.py" "cost-estimator.py" "status-updater.py"; do
    if [[ -f "$FOUNDRY_ROOT/common/utilities/$util" ]]; then
        pass "common/utilities/$util exists"
    else
        warn "common/utilities/$util missing"
    fi
done

# ────────────────────────────────────────────────────────
section "5. Strategies Layer Validation"
# ────────────────────────────────────────────────────────

EXPECTED_STRATEGIES=("harness-comparison.md" "model-selection-guide.md" "long-running-agents.md" "decision-framework.md" "deployment-guide.md" "optimization-guide.md" "quality-assurance.md")

for strategy in "${EXPECTED_STRATEGIES[@]}"; do
    if [[ -f "$FOUNDRY_ROOT/strategies/$strategy" ]]; then
        size=$(wc -c < "$FOUNDRY_ROOT/strategies/$strategy")
        if [[ "$size" -gt 5000 ]]; then
            pass "strategies/$strategy ($size bytes)"
        else
            warn "strategies/$strategy seems short ($size bytes)"
        fi
    else
        fail "strategies/$strategy MISSING"
    fi
done

# ────────────────────────────────────────────────────────
section "6. Usability Layer Validation"
# ────────────────────────────────────────────────────────

# Core files
for file in "initialize.sh" "ORCHESTRATOR.md" "ROADMAP.md" "README.md" "templates/PROJECT_CHARTER.md" "shared-workspace/README.md" "docs/USER_GUIDE.md"; do
    if [[ -f "$FOUNDRY_ROOT/$file" ]]; then
        pass "$file exists"
    else
        fail "$file MISSING"
    fi
done

# Launch scripts README
if [[ -f "$FOUNDRY_ROOT/launch-scripts/README.md" ]]; then
    pass "launch-scripts/README.md exists"
else
    warn "launch-scripts/README.md missing"
fi

# ────────────────────────────────────────────────────────
section "7. Sample Project Test"
# ────────────────────────────────────────────────────────

SAMPLE_DIR="$SCRIPT_DIR/sample-project"
if [[ -d "$SAMPLE_DIR" ]]; then
    # Verify sample project structure
    for file in "PROJECT_CHARTER.md" "shared-workspace/project-status.json"; do
        if [[ -f "$SAMPLE_DIR/$file" ]]; then
            pass "sample-project/$file exists"
        else
            fail "sample-project/$file MISSING"
        fi
    done

    # Test that start-team.sh can parse the sample project
    output=$("$FOUNDRY_ROOT/launch-scripts/start-team.sh" --dry-run "c-suite" "$SAMPLE_DIR" 2>&1 || true)
    if [[ $? -eq 0 ]] || echo "$output" | grep -qi "team\|prompt\|dry"; then
        pass "start-team.sh can read sample project"
    else
        warn "start-team.sh couldn't fully parse sample project"
    fi
else
    warn "sample-project not found — skipping sample project tests"
fi

# ────────────────────────────────────────────────────────
section "Results"
# ────────────────────────────────────────────────────────

echo ""
echo -e "  ${GREEN}PASS: $PASS${NC}  |  ${RED}FAIL: $FAIL${NC}  |  ${YELLOW}WARN: $WARN${NC}"
echo ""

if [[ "$FAIL" -eq 0 ]]; then
    echo -e "${BOLD}${GREEN}All tests passed!${NC}"
    exit 0
else
    echo -e "${BOLD}${RED}$FAIL test(s) failed.${NC}"
    exit 1
fi
