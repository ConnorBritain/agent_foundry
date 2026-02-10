# Deployment Guide

Step-by-step instructions for setting up the environment, configuring services, and running the Project Planning Team.

---

## Prerequisites

### Required Accounts

Create accounts on at least one task management tool before running the team:

| Service | URL | Purpose | Required Tier |
|---------|-----|---------|--------------|
| Linear | linear.app | Issue tracking, cycle management | Free |
| Jira | atlassian.com | Enterprise issue tracking, sprint management | Free |

### Optional Accounts

| Service | URL | Purpose | Required Tier |
|---------|-----|---------|--------------|
| Google Calendar | calendar.google.com | Milestone events, sprint boundaries, deadlines | Free |
| Notion | notion.so | Documentation export (alternative to markdown) | Free |

### Required CLI Tools

```bash
# Node.js 20+ (LTS) -- required for MCP servers
nvm install 20
nvm use 20

# Verify
node --version  # Should be >= 20.0.0
npm --version   # Should be >= 10.0.0
```

### Authentication

Set up API keys for your chosen tools:

```bash
# Linear
# Go to linear.app > Settings > API > Personal API keys
# Create a key and copy it

# Jira (alternative to Linear)
# Go to id.atlassian.com > Security > API tokens
# Create a token and copy it

# Google Calendar (optional)
# Set up OAuth credentials in Google Cloud Console
# or use a service account for server-to-server access
```

---

## Environment Variables

### Step 1: Generate API Keys

#### Linear

1. Go to https://linear.app/settings/api
2. Click "Create key"
3. Name it "project-planning-team"
4. Copy the key (starts with `lin_api_`)

#### Jira (Alternative)

1. Go to https://id.atlassian.com/manage-profile/security/api-tokens
2. Click "Create API token"
3. Name it "project-planning-team"
4. Copy the token
5. Note your Jira domain (e.g., `your-company.atlassian.net`)
6. Note your Atlassian account email

#### Google Calendar (Optional)

1. Go to https://console.cloud.google.com
2. Create or select a project
3. Enable the Google Calendar API
4. Create OAuth 2.0 credentials or a service account
5. Copy the token or download the service account key
6. Note the Calendar ID you want events created in

### Step 2: Set Environment Variables

Create a `.env.team` file in the project root (this file should be gitignored):

```bash
# Required -- at least one task management tool
LINEAR_API_KEY="lin_api_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
# OR
JIRA_API_TOKEN="xxxxxxxxxxxxxxxxxxxxxxxx"
JIRA_DOMAIN="your-company.atlassian.net"
JIRA_EMAIL="your-email@company.com"

# Optional but recommended
GOOGLE_CALENDAR_TOKEN="your-oauth-token"
GOOGLE_CALENDAR_ID="primary"  # or specific calendar ID
```

Load the environment variables:

```bash
# Option 1: Source the file
source .env.team

# Option 2: Use direnv (recommended)
cp .env.team .envrc
direnv allow
```

### Step 3: Verify Environment

```bash
# Quick verification
echo "Linear: ${LINEAR_API_KEY:+SET}"
echo "Jira: ${JIRA_API_TOKEN:+SET}"
echo "Google Calendar: ${GOOGLE_CALENDAR_TOKEN:+SET}"
```

At least one task management tool should show "SET".

---

## MCP Server Setup

The team uses MCP (Model Context Protocol) servers to interact with external task management and calendar services. Configure each server before running the team.

### Linear MCP Server

The Linear MCP server provides direct access to issue creation, cycle management, and project tracking.

```bash
# Verify Linear API key is set
echo "Linear: ${LINEAR_API_KEY:+SET}"

# The MCP server configuration is at:
# mcp-servers/linear.json
```

The Integration Planner uses this to:
- Create issues with titles, descriptions, estimates, and labels
- Set issue dependencies and priorities
- Assign issues to cycles (sprints)
- Create project milestones

### Jira MCP Server

```bash
# Verify Jira credentials are set
echo "Jira: ${JIRA_API_TOKEN:+SET}"
echo "Domain: ${JIRA_DOMAIN:+SET}"

# The MCP server configuration is at:
# mcp-servers/jira.json
```

The Integration Planner uses this to:
- Create issues (epics, stories, tasks, subtasks)
- Set issue links (dependencies)
- Assign issues to sprints
- Set priorities, labels, and custom fields

### Google Calendar MCP Server

```bash
# Verify Google Calendar token is set
echo "Calendar: ${GOOGLE_CALENDAR_TOKEN:+SET}"

# The MCP server configuration is at:
# mcp-servers/google-calendar.json
```

The Integration Planner and Scheduler use this to:
- Create milestone events
- Set sprint boundary events
- Create recurring ceremony events (standups, retros, demos)
- Set deadline reminders

---

## Running the Team

### Step 1: Configure the Project

```bash
# Navigate to the template directory
cd teams/project-planning

# Copy and edit the configuration
cp CONFIG.md CONFIG.local.md

# Edit CONFIG.local.md with your project settings
# At minimum, fill in:
#   - project_name
#   - project_description
#   - project_type
#   - framework (or leave for Coordinator to suggest)
#   - team_size
#   - duration_weeks
#   - task_management (linear or jira)
```

### Step 2: Select Model Configuration

Choose your model configuration in `CONFIG.local.md`:

```yaml
agent_budget:
  model_config: default  # Options: budget, default, premium
```

See `MODEL_CONFIGS.md` for detailed comparison of each configuration.

### Step 3: Run the Full Planning Session

```bash
# Recommended: Hybrid mode (parallel where possible)
claude-agent team run ./teams/project-planning \
  --config CONFIG.local.md \
  --mode hybrid

# Expected duration: ~1-1.5 hours
# Expected cost: ~$23 (default config)
```

**What happens:**
1. Coordinator configures the project framework and validates settings
2. Requirements Analyst decomposes the vision into workstreams
3. Task Decomposer creates granular tasks with estimates
4. Risk Assessor and Resource Allocator work in parallel
5. Scheduler maps the plan to a calendar
6. Integration Planner exports to Linear/Jira and creates documentation
7. Coordinator performs final review and issues delivery recommendation

### Step 4: Review the Output

After the team completes, review these deliverables:

```bash
# The team produces these outputs:
# 1. Requirements document (markdown)
# 2. Task list with estimates and acceptance criteria
# 3. Work Breakdown Structure
# 4. Risk register with mitigations
# 5. Prioritized backlog with trade-off recommendations
# 6. Resource allocation matrix
# 7. Calendar with milestones
# 8. Linear/Jira workspace (fully populated)
# 9. Stakeholder communication plan
# 10. Executive summary
# 11. Project README
```

### Running Phase by Phase

If you prefer to review each phase before proceeding:

```bash
# Phase 1: Configuration
claude-agent team run ./teams/project-planning \
  --config CONFIG.local.md \
  --mode sequential \
  --phase 1

# Review CONFIG.local.md, then proceed

# Phase 2: Requirements
claude-agent team run ./teams/project-planning \
  --config CONFIG.local.md \
  --mode sequential \
  --phase 2

# Review requirements, answer any clarifying questions, then proceed

# Phase 3: Task Decomposition
claude-agent team run ./teams/project-planning \
  --config CONFIG.local.md \
  --mode sequential \
  --phase 3

# Continue through remaining phases...
```

---

## Post-Run Verification

After the team completes, verify the outputs:

### 1. Task Management Tool

```bash
# For Linear:
# Visit linear.app and check your team/project
# Verify:
# - All tasks are created as issues
# - Dependencies are linked
# - Priorities are set correctly
# - Labels match workstreams
# - Cycles (sprints) are created with correct dates

# For Jira:
# Visit your-company.atlassian.net and check the project
# Verify:
# - Epics, stories, and tasks are created
# - Issue links show dependencies
# - Sprint backlog is populated
# - Priorities and labels are correct
```

### 2. Calendar

```bash
# Visit Google Calendar
# Verify:
# - Sprint/cycle boundary events exist
# - Milestone events are placed at correct dates
# - Recurring ceremonies are created (standups, retros, demos)
# - Reminder events for stakeholder reviews are set
```

### 3. Documentation

Review the generated markdown documents:
- **Requirements document** -- Are workstreams well-defined? Are success criteria measurable?
- **Risk register** -- Are the top risks realistic? Are mitigations actionable?
- **Executive summary** -- Is it suitable for stakeholder review?
- **Project README** -- Does it accurately describe the project?

### 4. Plan Consistency

Cross-check for internal consistency:
- Every workstream in the requirements has tasks in the backlog
- Every task dependency is reflected in the schedule
- Resource allocation does not exceed team capacity
- Milestones align with stakeholder reporting cadence
- Risk mitigations are assigned to specific owners

---

## Iterating on the Plan

### Re-running Specific Phases

If a phase output needs improvement:

```bash
# Re-run just the Requirements phase with updated vision
claude-agent team run ./teams/project-planning \
  --config CONFIG.local.md \
  --mode sequential \
  --phase 2 \
  --resume-from-checkpoint

# Re-run Resource Allocation with different priorities
claude-agent team run ./teams/project-planning \
  --config CONFIG.local.md \
  --mode sequential \
  --phase 4 \
  --resume-from-checkpoint
```

### Updating the Plan for a New Sprint

For recurring sprint planning (Scrum teams):

```bash
# Update CONFIG.local.md with new sprint details
# - Adjust start_date to the new sprint start
# - Update any team capacity changes
# - Add new vision/goals for the sprint

# Run just the relevant phases
claude-agent team run ./teams/project-planning \
  --config CONFIG.local.md \
  --mode hybrid \
  --phase 2-6
```

---

## Troubleshooting

### Common Issues

**Linear API key is invalid:**
- Verify the key starts with `lin_api_`
- Check that the key has not expired
- Ensure the key has write permissions to the target team

**Jira authentication fails:**
- Verify JIRA_DOMAIN is correct (e.g., `company.atlassian.net`, not `company.atlassian.com`)
- Check that JIRA_EMAIL matches the account that created the token
- Ensure the token has not been revoked

**Google Calendar events not created:**
- Verify the OAuth token is valid and not expired
- Check that the Calendar ID is correct (use `primary` for default calendar)
- Ensure the Google Calendar API is enabled in your Cloud Console project

**Quality gate fails repeatedly:**
- Check the gate failure message for specific issues
- Review the agent's output for the failing check
- If the vision statement is too vague, provide more detail in CONFIG.local.md
- If token budget is exhausted, switch to Budget config or increase max_total_cost_usd

**Framework terminology is wrong:**
- Verify the `framework` setting in CONFIG.local.md matches your intent
- If using Custom, provide framework details in the project_description

**Tasks are too granular or too coarse:**
- Adjust team_size and sprint_length in CONFIG.local.md
- The Task Decomposer calibrates granularity to "completable in one sprint"
- Smaller teams with longer sprints get coarser tasks; larger teams with shorter sprints get finer tasks

**MCP server connection timeout:**
- Check your internet connection
- Verify the MCP server configuration JSON is valid
- Restart the MCP server process
- Check for rate limiting on the target API
