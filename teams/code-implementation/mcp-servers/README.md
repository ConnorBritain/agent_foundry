# MCP Server Configuration

This directory contains the Model Context Protocol (MCP) server configurations used by the Code Implementation Team agents to interact with external services.

---

## Overview

Each JSON file defines an MCP server connection that agents use to perform operations against external APIs. The configurations specify the service endpoint, capabilities, and required credentials.

| MCP Server | Config File | Used By | Purpose |
|-----------|-------------|---------|---------|
| GitHub | `github.json` | Coordinator, Code Reviewer | Branch management, PR creation, code review integration |

### Optional MCP Servers

| MCP Server | Config File | Used By | Purpose |
|-----------|-------------|---------|---------|
| Linear | `linear.json` | Coordinator | Task tracking, sprint management |
| Jira | `jira.json` | Coordinator | Enterprise task tracking |
| Sentry | `sentry.json` | Coordinator, Test Engineer | Error tracking context for bug fixes |

---

## Prerequisites

### GitHub (Required)

**Required environment variables:**
- `GITHUB_TOKEN` -- Personal access token with repository and workflow permissions

**How to obtain:**

1. Go to [github.com/settings/tokens](https://github.com/settings/tokens)
2. Click **Generate new token (classic)**
3. Name it (e.g., "code-implementation-team")
4. Select the following scopes:
   - `repo` -- Full control of private repositories
   - `workflow` -- Update GitHub Actions workflows
5. Click **Generate token**
6. Copy the token (starts with `ghp_`) -- this is your `GITHUB_TOKEN`

Alternatively, use a **fine-grained personal access token** with permissions:
- Repository access: your specific repository
- Permissions: Contents (read/write), Pull requests (read/write), Actions (read/write)

**What this MCP server provides:**
- **Branches:** Create, list, and delete branches
- **Commits:** Read commit history, compare branches
- **Pull Requests:** Create PRs, add reviewers, merge
- **Code Review:** Post review comments, approve/request changes
- **Actions:** Trigger workflows, inspect run results

**CLI verification:**

```bash
gh --version
gh auth status
```

---

### Linear (Optional)

**Required environment variables:**
- `LINEAR_API_KEY` -- Personal API key

**How to obtain:**

1. Go to Settings > API > Personal API keys in Linear
2. Create a new key with appropriate scopes
3. Copy the key

**What this MCP server provides:**
- **Issues:** Create and update issues from task decomposition
- **Projects:** Link work to projects and milestones
- **Labels:** Categorize tasks by type and priority

---

### Sentry (Optional)

**Required environment variables:**
- `SENTRY_AUTH_TOKEN` -- Authentication token with project:read scope

**How to obtain:**

1. Go to Settings > Auth Tokens in Sentry
2. Create a new token with `project:read` scope
3. Copy the token

**What this MCP server provides:**
- **Error context:** Recent errors and stack traces for bug fix workflows
- **Release tracking:** Link feature branches to Sentry releases

---

## Environment Variable Summary

```bash
# Required
export GITHUB_TOKEN=""              # ghp_... (personal access token)

# Optional
export LINEAR_API_KEY=""            # Linear personal API key
export JIRA_TOKEN=""                # Jira API token
export SENTRY_AUTH_TOKEN=""         # Sentry auth token
```

---

## Verification Checklist

Run this checklist before starting the team:

```bash
# GitHub (required)
echo "GitHub token: ${GITHUB_TOKEN:+SET}"
gh auth status 2>/dev/null && echo "GitHub CLI: OK" || echo "GitHub CLI: FAILED"
```

GitHub should show "SET" and "OK". Optional services only need verification if enabled in CONFIG.

---

## Security Notes

- **Never commit credentials** to the repository. Set environment variables in your shell or `.env.local` (gitignored).
- **Scope tokens narrowly.** Give each token only the permissions it needs.
- **Rotate tokens regularly.** If a token is exposed, revoke it immediately and generate a new one.
- **Use fine-grained tokens when possible.** Limit access to specific repositories rather than all repositories.
