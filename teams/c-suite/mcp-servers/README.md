# MCP Servers for C-Suite Team

## Overview

The C-Suite Team uses Model Context Protocol (MCP) servers to connect agent outputs to real-world tools. MCP servers allow agents to read from and write to external services -- creating live, editable artifacts instead of static text.

This directory contains configuration files for each recommended MCP server integration.

---

## Recommended Servers

| Server | Purpose | Primary Agent(s) | Priority |
|--------|---------|-------------------|----------|
| Google Sheets | Financial models, budgets, cap tables, pipeline models | CFO, VP Sales | Required |
| Notion | Business plans, playbooks, compliance docs, go-to-market plans | All agents | Required |
| Linear | Product roadmaps, issue tracking, sprint planning | CTO | Optional |
| Google Slides | Pitch deck generation | CEO | Optional |

---

## Server Configurations

### google-sheets.json

Enables the CFO to produce live financial models with formulas, charts, and linked sheets. Also used by VP Sales for pipeline models and compensation calculators.

**Key use cases:**
- P&L projection with monthly and annual views
- Cash flow analysis with runway calculation
- Cap table with dilution scenario modeling
- Unit economics dashboard (CAC, LTV, payback period)
- Sales pipeline model with conversion rate formulas
- Sensitivity analysis with data tables

### notion.json

Enables all agents to produce structured business planning documents in a shared Notion workspace. The primary output destination for narrative documents, checklists, and operational plans.

**Key use cases:**
- Executive summary and business plan narrative
- Go-to-market plan with channel strategy
- Sales playbook with objection handling matrix
- Compliance checklist and calendar
- Customer persona documents
- Process maps and org chart descriptions
- Content calendar and campaign briefs

---

## Setup Instructions

### 1. Install MCP Server Dependencies

Each server config specifies its `command` and `args`. Most use `npx` for zero-install execution:

```bash
# Google Sheets -- runs via npx, no install needed
npx -y @anthropic/mcp-google-sheets

# Notion -- runs via npx, no install needed
npx -y @anthropic/mcp-notion
```

### 2. Configure Environment Variables

Each server requires API credentials set as environment variables. Copy the template and fill in your values:

```bash
# Google Sheets
export GOOGLE_SHEETS_API_KEY="your-google-api-key"
export GOOGLE_SHEETS_SPREADSHEET_ID="your-spreadsheet-id"

# Notion
export NOTION_API_KEY="your-notion-integration-token"
export NOTION_WORKSPACE_ID="your-workspace-id"
```

### 3. Verify Connectivity

Before running the C-Suite Team, verify each MCP server can connect:

```bash
# Test Google Sheets connection
npx -y @anthropic/mcp-google-sheets --test

# Test Notion connection
npx -y @anthropic/mcp-notion --test
```

### 4. Register in Agent Configuration

Add the MCP server configs to your agent runtime configuration:

```json
{
  "mcp_servers": [
    "./mcp-servers/google-sheets.json",
    "./mcp-servers/notion.json"
  ]
}
```

---

## Fallback Behavior

If an MCP server is unavailable at runtime, agents fall back to producing markdown-formatted output:

| Server | Fallback Format | Quality Impact |
|--------|----------------|----------------|
| Google Sheets | Markdown tables with formulas as comments | No live formulas or charts; manual copy to spreadsheet |
| Notion | Markdown documents with page structure as headers | No database properties or linked views; manual import |
| Linear | Markdown task lists with epic/feature hierarchy | No issue tracking or sprint views; manual import |
| Google Slides | Markdown slide outlines with speaker notes | No visual design or layout; manual slide creation |

Agents detect MCP server availability at Phase 6 startup and adjust their output format accordingly. The content quality is identical; only the delivery format changes.

---

## Cost Impact

MCP servers themselves are free and open-source. The external services they connect to may have costs:

| Service | Free Tier | Paid Tier | Notes |
|---------|-----------|-----------|-------|
| Google Sheets | Free with Google account | $7/user/mo (Workspace) | Free tier sufficient for planning |
| Notion | Free for personal use | $10/user/mo (Plus) | Free tier sufficient for single founder |
| Linear | Free up to 250 issues | $8/user/mo (Standard) | Free tier sufficient for MVP roadmap |
| Google Slides | Free with Google account | $7/user/mo (Workspace) | Free tier sufficient for pitch deck |

---

## Adding Custom MCP Servers

To add a new MCP server integration:

1. Create a JSON config file in this directory following the schema:
   ```json
   {
     "name": "server-name",
     "description": "What it does",
     "repository": "https://github.com/...",
     "configuration": {
       "command": "npx",
       "args": ["-y", "@package/name"],
       "env": {}
     },
     "use_cases": [],
     "team_integration": "How this team uses it"
   }
   ```
2. Register it in the agent runtime configuration
3. Test connectivity before running the team
4. Document fallback behavior for unavailable scenarios
