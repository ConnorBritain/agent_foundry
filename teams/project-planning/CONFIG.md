# Project Planning Team Configuration

```yaml
# Project Planning Team Configuration
# Copy this file to CONFIG.local.md and fill in your values.
# CONFIG.local.md is gitignored and safe for project-specific settings.
#
# Initialized: 2026-02-10T00:00:00Z

# ──────────────────────────────────────────────
# Project Identity
# ──────────────────────────────────────────────
project_name: "my-project"
project_description: "A brief description of the project goals and intended outcomes."
project_type: software              # Options: software | marketing_campaign | event_planning | home_renovation | business_launch | research | other

# ──────────────────────────────────────────────
# Framework Selection
# ──────────────────────────────────────────────
# The Coordinator will present options and help select if not specified.
framework: agile_scrum              # Options: safe | agile_scrum | agile_kanban | shape_up | waterfall | family_chores | small_business | custom

# Framework-specific settings (populated after framework selection):
# -- SAFe: program_increment_length, number_of_teams, art_name
# -- Scrum: sprint_length_weeks, velocity_estimate, definition_of_done
# -- Kanban: wip_limits, service_classes, sla_targets
# -- Shape Up: cycle_length_weeks, cooldown_length_weeks, max_bets_per_cycle
# -- Waterfall: phase_gate_criteria, change_control_process

scrum_settings:
  sprint_length_weeks: 2
  velocity_estimate: 0              # Story points per sprint (0 = unknown, agent will estimate)
  definition_of_done: ""            # Leave blank for default; provide custom if you have one
  estimation_unit: story_points     # Options: story_points | hours | t_shirt_sizes

safe_settings:
  pi_length_weeks: 10
  number_of_teams: 1
  art_name: ""
  innovation_sprint: true

shape_up_settings:
  cycle_length_weeks: 6
  cooldown_length_weeks: 2
  max_bets_per_cycle: 3

kanban_settings:
  wip_limit_per_column: 3
  service_classes: [standard, expedite, fixed_date]

# ──────────────────────────────────────────────
# Team and Resources
# ──────────────────────────────────────────────
team_size: 5                        # Number of people on the execution team
team_members:                       # Optional: list team members for resource allocation
  # - name: "Alice"
  #   role: "Senior Backend Engineer"
  #   skills: [python, postgres, aws]
  #   capacity_percent: 100
  # - name: "Bob"
  #   role: "Frontend Engineer"
  #   skills: [react, typescript, css]
  #   capacity_percent: 80

duration_weeks: 12                  # Target project duration
start_date: ""                      # ISO date (leave blank for "start now")

# ──────────────────────────────────────────────
# Tool Integration
# ──────────────────────────────────────────────
task_management: linear             # Options: linear | jira | asana | notion | todoist | none
calendar_integration: google_calendar  # Options: google_calendar | outlook | none

linear_settings:
  team_id: ""                       # Linear team ID (leave blank to create new)
  project_name: ""                  # Defaults to project_name above
  label_scheme: [priority, workstream, type]

jira_settings:
  project_key: ""                   # Jira project key (e.g., "PROJ")
  board_type: scrum                 # Options: scrum | kanban
  issue_types: [epic, story, task, bug, subtask]

# ──────────────────────────────────────────────
# Stakeholders
# ──────────────────────────────────────────────
stakeholders:
  # - name: "Product Owner"
  #   role: "Decision maker for scope and priority"
  #   communication: "weekly_sync"
  #   detail_level: "high_level"     # Options: high_level | detailed | technical
  # - name: "Engineering Manager"
  #   role: "Resource allocation and team health"
  #   communication: "daily_standup"
  #   detail_level: "detailed"
  # - name: "VP Engineering"
  #   role: "Executive sponsor"
  #   communication: "monthly_review"
  #   detail_level: "high_level"

reporting_cadence: weekly           # Options: daily | weekly | biweekly | monthly

# ──────────────────────────────────────────────
# Cost and Budget
# ──────────────────────────────────────────────
agent_budget:
  model_config: default             # Options: budget | default | premium
  max_total_tokens: 340000          # Includes 15% buffer
  max_total_cost_usd: 30

# ──────────────────────────────────────────────
# Output Preferences
# ──────────────────────────────────────────────
output_format:
  dependency_graph: mermaid          # Options: mermaid | ascii | none
  risk_register: markdown_table      # Options: markdown_table | csv | json
  executive_summary: true
  stakeholder_comms_plan: true
  project_readme: true
```

## Usage

1. Copy this file:
   ```bash
   cp CONFIG.md CONFIG.local.md
   ```

2. Edit `CONFIG.local.md` with your project-specific values.

3. Pass it to the team runner:
   ```bash
   claude-agent team run ./teams/project-planning --config CONFIG.local.md
   ```

## Configuration Validation

The Coordinator agent validates the configuration at the start of Phase 1 and will report errors for:

- Missing required fields (`project_name`, `project_type`, `framework`)
- Invalid enum values (e.g., `framework: kangaroo` is not a valid option)
- Inconsistent settings (e.g., `sprint_length_weeks` set for a Kanban framework)
- Capacity issues (e.g., `team_size: 0` or `duration_weeks: 0`)
- Budget conflicts (e.g., `max_total_cost_usd` lower than the selected `model_config` estimate)

## Environment Variables

These must be set in your shell before running the team. They are never stored in config files.

```bash
# Required (at least one task management tool)
export LINEAR_API_KEY=""               # From linear.app > Settings > API
# OR
export JIRA_API_TOKEN=""               # From id.atlassian.com > Security > API tokens
export JIRA_DOMAIN=""                  # e.g., "your-company.atlassian.net"
export JIRA_EMAIL=""                   # Your Atlassian account email

# Optional but recommended
export GOOGLE_CALENDAR_TOKEN=""        # From Google Cloud Console OAuth
export GOOGLE_CALENDAR_ID=""           # Calendar ID to create events in
```
