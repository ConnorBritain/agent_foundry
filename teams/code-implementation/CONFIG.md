# Code Implementation Team Configuration

```yaml
# Code Implementation Team Configuration
# Copy this file to CONFIG.local.md and fill in your values.
# CONFIG.local.md is gitignored and safe for sensitive defaults.
#
# Initialized: 2026-02-10T00:00:00Z

# ──────────────────────────────────────────────
# Project Context
# ──────────────────────────────────────────────
project_type: web_app                # Options: web_app | mobile_app | backend_api | library | cli_tool
primary_language: typescript         # Options: python | javascript | typescript | swift | kotlin | rust | go | other
framework: nextjs                    # Options: nextjs | react | fastapi | django | spring | swiftui | jetpack_compose | express | flask | other
testing_framework: vitest            # Options: pytest | jest | vitest | xctest | junit | mocha | other
package_manager: npm                 # Options: npm | yarn | pnpm | bun | pip | cargo | go_mod

# ──────────────────────────────────────────────
# Repository
# ──────────────────────────────────────────────
repository:
  url: ""                            # GitHub repository URL (e.g., https://github.com/org/repo)
  default_branch: main               # Branch to merge features into
  branch_prefix: agent               # Prefix for agent-created branches (e.g., agent/impl-a/feature-name)

# ──────────────────────────────────────────────
# Feature Specification
# ──────────────────────────────────────────────
feature:
  name: ""                           # Short feature name (used in branch names)
  spec_path: ""                      # Path to feature spec file or inline description
  description: ""                    # One-line description if no spec file
  priority: standard                 # Options: low | standard | high | critical

# ──────────────────────────────────────────────
# Code Style and Standards
# ──────────────────────────────────────────────
code_style: airbnb                   # Options: pep8 | airbnb | google | standard | custom
style_guide_path: ""                 # Path to custom style guide (used when code_style = custom)
review_strictness: standard          # Options: relaxed | standard | strict
  # relaxed: only blockers, no style enforcement
  # standard: blockers + major style violations
  # strict: blockers + all style violations + suggestions enforced

lint_command: "npm run lint"         # Command to run linting
format_command: "npm run format"     # Command to run formatting
typecheck_command: "npx tsc --noEmit"  # Command to run type checking (leave empty if not applicable)

# ──────────────────────────────────────────────
# Testing Configuration
# ──────────────────────────────────────────────
testing:
  unit_test_command: "npm run test"           # Command to run unit tests
  integration_test_command: ""                # Command to run integration tests (leave empty if none)
  e2e_test_command: ""                        # Command to run E2E tests (leave empty if none)
  coverage_command: "npm run test -- --coverage"  # Command to generate coverage report
  coverage_threshold: 80                      # Minimum coverage percentage for new code
  test_directory: "tests"                     # Directory for test files
  test_pattern: "**/*.test.ts"                # File pattern for test files

# ──────────────────────────────────────────────
# Documentation
# ──────────────────────────────────────────────
documentation:
  api_docs_path: "docs/api"          # Directory for API documentation
  changelog_path: "CHANGELOG.md"     # Path to changelog file
  readme_path: "README.md"           # Path to README file
  doc_style: jsdoc                   # Options: jsdoc | docstring | rustdoc | godoc | javadoc | custom
  update_readme: true                # Whether to update README for feature changes
  update_changelog: true             # Whether to generate changelog entries

# ──────────────────────────────────────────────
# Agent Budget
# ──────────────────────────────────────────────
agent_budget:
  model_config: default              # Options: budget | default | premium
  max_total_tokens: 490000           # 490K base budget
  max_total_cost_usd: 35             # Hard cost ceiling
  max_review_cycles: 3               # Maximum reviewer round-trips before escalation
  iteration_budget: 2                # Max number of test-fix-retest cycles

# ──────────────────────────────────────────────
# MCP Servers
# ──────────────────────────────────────────────
mcp_servers:
  github:
    enabled: true
    config: "mcp-servers/github.json"
  linear:
    enabled: false
    config: "mcp-servers/linear.json"
  jira:
    enabled: false
    config: "mcp-servers/jira.json"
  sentry:
    enabled: false
    config: "mcp-servers/sentry.json"

# ──────────────────────────────────────────────
# Output Configuration
# ──────────────────────────────────────────────
output:
  create_pr: true                    # Create a pull request after completion
  pr_template: ""                    # Path to PR template (leave empty for default)
  include_test_report: true          # Include test results in PR description
  include_coverage_report: true      # Include coverage report in PR description
  include_cost_summary: true         # Include token/cost summary in PR description
```

## Usage

1. Copy this file:
   ```bash
   cp CONFIG.md CONFIG.local.md
   ```

2. Edit `CONFIG.local.md` with your project-specific values.

3. Pass it to the team runner:
   ```bash
   claude-agent team run ./teams/code-implementation --config CONFIG.local.md
   ```

## Configuration Validation

The Coordinator agent validates the configuration at the start of Phase 1 and will report errors for:

- Missing required fields (`repository.url`, `feature.name`)
- Invalid enum values (e.g., `code_style: freestyle` is not valid)
- Inconsistent settings (e.g., `typecheck_command` set for a Python project)
- Budget conflicts (`max_total_cost_usd` lower than the selected `model_config` estimate)
- Missing test commands when `coverage_threshold` > 0
- Repository URL not accessible with provided `GITHUB_TOKEN`

## Environment Variables

These must be set in your shell before running the team:

```bash
# Required
export GITHUB_TOKEN=""              # Personal access token with repo and workflow permissions

# Optional (for task tracking integration)
export LINEAR_API_KEY=""            # Linear API key (if linear MCP enabled)
export JIRA_TOKEN=""                # Jira API token (if jira MCP enabled)
export SENTRY_AUTH_TOKEN=""         # Sentry auth token (if sentry MCP enabled)
```
