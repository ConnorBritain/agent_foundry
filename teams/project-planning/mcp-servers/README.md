# MCP Servers for Project Planning

This directory contains Model Context Protocol (MCP) server configurations for the tools used by the Project Planning Team. MCP servers allow agents to interact with external services -- creating issues, scheduling events, and syncing project data -- without manual intervention.

---

## Available Servers

| Server | Purpose | Used By | Phase |
|--------|---------|---------|-------|
| [Linear](./linear.json) | Task and issue tracking | Integration Planner | 6, 7 |
| [Jira](./jira.json) | Project management and issue tracking | Integration Planner | 6, 7 |
| [Google Calendar](./google-calendar.json) | Scheduling and milestone tracking | Scheduler, Integration Planner | 5, 6, 7 |

## How MCP Servers Work

MCP servers expose tool capabilities to agents through a standardized protocol. When an agent needs to create a Linear issue or a Google Calendar event, it calls the MCP server with structured parameters. The server handles authentication, API communication, and error handling.

```
Agent (Integration Planner)
  → MCP Client (built into agent runtime)
    → MCP Server (e.g., linear-mcp-server)
      → External API (Linear REST API)
        → Response back through the chain
```

## Configuration

Each server configuration file (`.json`) contains:

- **name**: Server identifier used in agent tool calls
- **description**: What the server does
- **repository**: Source code for the MCP server
- **configuration**: How to start the server (`command`, `args`, `env`)
- **use_cases**: What the planning team uses it for
- **team_integration**: How it fits into the planning workflow

## Setup

### 1. Set Environment Variables

Before running the team, set the required environment variables for your chosen tools. See `CONFIG.md` for the full list.

```bash
# Linear (if using Linear for task management)
export LINEAR_API_KEY="lin_api_..."

# Jira (if using Jira for task management)
export JIRA_API_TOKEN="..."
export JIRA_DOMAIN="your-company.atlassian.net"
export JIRA_EMAIL="you@company.com"

# Google Calendar (if using calendar integration)
export GOOGLE_CALENDAR_TOKEN="..."
export GOOGLE_CALENDAR_ID="primary"
```

### 2. Server Installation

MCP servers are installed automatically via `npx` on first use. No manual installation is required. The `command` and `args` fields in each config handle this.

### 3. Tool Selection

The team uses **one** task management tool per session, configured in `CONFIG.local.md`:

```yaml
task_management: linear    # or: jira | none
calendar_integration: google_calendar  # or: outlook | none
```

The Integration Planner reads this configuration and activates the appropriate MCP server.

## Token Overhead

MCP server calls add minimal token overhead to the session:

| Server | Typical Calls | Tokens per Call | Total Overhead |
|--------|--------------|-----------------|----------------|
| Linear | 20-50 issue creates | ~200 | ~4K-10K |
| Jira | 20-50 issue creates | ~300 | ~6K-15K |
| Google Calendar | 5-15 event creates | ~150 | ~750-2.25K |

This overhead is included in the Integration Planner's ~30K token budget and typically accounts for less than 5% of total session cost.

## Adding New MCP Servers

To add a new MCP server for the project planning team:

1. Create a new `.json` file in this directory following the existing format
2. Add the server to the table above
3. Update `CONFIG.md` with any new environment variables
4. Update the Integration Planner's AGENTS.md if the server introduces new capabilities

## Troubleshooting

| Issue | Cause | Resolution |
|-------|-------|------------|
| Server fails to start | Missing environment variable | Check that all required `env` vars are exported |
| Authentication error | Invalid or expired API key | Regenerate the API key and re-export |
| Rate limit exceeded | Too many API calls in short period | The MCP server handles retry with backoff automatically |
| Issue creation fails | Invalid project or team ID | Verify `linear_settings.team_id` or `jira_settings.project_key` in CONFIG |
| Calendar event fails | Invalid calendar ID | Verify `GOOGLE_CALENDAR_ID` is set to a valid calendar |
