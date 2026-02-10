# MCP Servers for Code Implementation Team

This directory contains Model Context Protocol (MCP) server configurations used by the Code Implementation Team. MCP servers extend agent capabilities by providing structured access to external tools and services.

---

## Overview

| MCP Server | Config File | Purpose | Required |
|-----------|-------------|---------|----------|
| GitHub | `github.json` | Repository access, branch management, PR creation, issue tracking | Yes |
| Filesystem | `filesystem.json` | Local file read/write, directory traversal, project structure analysis | Yes |

## How MCP Servers Are Used

Each agent in the team connects to MCP servers based on its responsibilities:

| Agent | GitHub | Filesystem |
|-------|--------|-----------|
| Coordinator / Planner | Read issues, create PRs, manage branches | Read project structure, analyze codebase conventions |
| Implementation Specialist A | Push commits, create branches | Read and write source files |
| Implementation Specialist B | Push commits, create branches | Read and write source files |
| Code Reviewer | Read diffs, post review comments | Read source files for context |
| Test Engineer | Read test results from CI | Read source files, write test files |
| DevOps Specialist | Configure CI workflows, manage secrets | Read and write config files, Dockerfiles, CI manifests |

## Setup

### 1. Install MCP Server Dependencies

MCP servers are installed automatically via `npx` when the team runs. No pre-installation is needed. Ensure you have Node.js >= 20.0.0 installed.

### 2. Configure Environment Variables

Each MCP server requires specific environment variables. Set these before running the team:

```bash
# GitHub MCP Server (required)
export GITHUB_TOKEN="ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

### 3. Verify Configuration

The Coordinator validates MCP server connectivity at the start of Phase 1. If a required server is unreachable, the run will pause with a clear error message.

## Configuration Format

Each MCP server config file follows this structure:

```json
{
  "name": "server-name",
  "description": "What the server provides",
  "repository": "https://github.com/org/repo",
  "configuration": {
    "command": "npx",
    "args": ["-y", "@package/name"],
    "env": {
      "API_KEY": "${ENV_VAR_NAME}"
    }
  },
  "use_cases": [
    "Specific capability 1",
    "Specific capability 2"
  ],
  "team_integration": "How this team uses the server"
}
```

## Adding a New MCP Server

1. Create a new JSON config file in this directory (e.g., `sentry.json`)
2. Follow the configuration format above
3. Add the server to the `mcp_servers` section in `CONFIG.md`
4. Set the required environment variables
5. Document the server in the table at the top of this file

## Troubleshooting

**Server fails to start:**
- Verify Node.js >= 20.0.0 is installed: `node --version`
- Check that the `npx` command is available: `npx --version`
- Ensure the environment variable is set: `echo $GITHUB_TOKEN`

**Authentication errors:**
- Verify your GitHub token has `repo` and `workflow` scopes
- Regenerate the token if it has expired
- Run `gh auth status` to confirm GitHub CLI authentication

**Timeout errors:**
- MCP servers have a 30-second connection timeout
- Check network connectivity to the service (github.com)
- If behind a proxy, configure `HTTPS_PROXY` environment variable
