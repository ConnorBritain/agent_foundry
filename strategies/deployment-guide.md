# Deployment Guide

> How to deploy Agent Foundry in local development, team CI/CD, and enterprise self-hosted environments.

## Overview

Agent Foundry runs wherever you can execute a shell and call the Claude API. But the configuration, security requirements, and operational concerns differ significantly between a solo developer running agents on a laptop, a team integrating agents into CI/CD pipelines, and an enterprise deploying across a fleet of managed servers.

This guide covers three deployment tiers: local development (single machine, one user), team CI/CD (shared pipelines, multiple contributors), and enterprise self-hosted (managed infrastructure, compliance requirements). Each tier builds on the previous one, adding the configuration and controls needed for that context.

Regardless of tier, the core requirements are the same: a Claude API key, a compatible harness (Claude Code recommended), and a workspace for agents to operate in.

## Prerequisites

### Common Requirements (All Tiers)

| Requirement | Version / Spec | Notes |
|---|---|---|
| Node.js | 18+ | Required for Claude Code SDK |
| Git | 2.30+ | Agent workflows depend on git |
| Claude API Key | Anthropic API | At minimum, tier 1 rate limits |
| Claude Code | Latest | Primary agent harness |
| Disk Space | 1GB+ free | For workspace, logs, checkpoints |
| Network | HTTPS outbound | Access to api.anthropic.com |

### Optional Components

| Component | When Needed |
|---|---|
| Docker | Sandboxed agent execution |
| MCP Servers | External tool integration |
| Redis / SQLite | Shared state persistence |
| Nginx / Caddy | Enterprise reverse proxy |

## Tier 1: Local Development

### Setup

Local deployment is the simplest: one machine, one developer, agents running in terminal sessions.

**Step 1: Install Claude Code**

```bash
npm install -g @anthropic-ai/claude-code
```

**Step 2: Configure API Key**

```bash
# Option A: Environment variable (recommended for local dev)
export ANTHROPIC_API_KEY="sk-ant-api03-..."

# Option B: Configuration file
mkdir -p ~/.config/agent-foundry
cat > ~/.config/agent-foundry/config.yaml << 'EOF'
api:
  provider: anthropic
  key_source: env  # reads from ANTHROPIC_API_KEY
  default_model: claude-sonnet-4-5-20250929
EOF
```

**Step 3: Clone Agent Foundry Templates**

```bash
git clone https://github.com/your-org/agent-foundry-templates.git
cd agent-foundry-templates
```

**Step 4: Initialize a Workspace**

```bash
# Create a workspace for your project
./initialize.sh my-project

# This creates:
# my-project/
#   shared-workspace/    -- agents read/write code here
#   shared-state/        -- checkpoints, logs, coordination files
#   teams/               -- team configurations
#   logs/                -- agent session logs
```

**Step 5: Launch a Team**

```bash
# Launch a team using a launch script
./launch-scripts/launch-team.sh teams/backend-api.yaml
```

### Local Development Best Practices

- **Use a dedicated workspace directory**: Never point agents at your main development directory. Clone or copy the project into the Agent Foundry workspace.
- **Set budget limits**: Even locally, configure per-session cost caps to avoid surprise bills during experimentation.
- **Monitor token usage**: Check `logs/` after each run to understand cost patterns before scaling up.
- **Use Sonnet as default**: Reserve Opus for orchestrator roles; Haiku for test/formatting roles.
- **Start serial**: Run agents one at a time until you understand the workflow, then enable parallelism.

### Local Configuration Example

```yaml
# teams/local-dev.yaml
team:
  name: local-backend
  environment: local
  workspace: ./shared-workspace

  defaults:
    model: claude-sonnet-4-5-20250929
    harness: claude-code
    timeout: 1800  # 30 minutes per agent session
    budget:
      max_per_session: 2.00
      max_total: 20.00

  agents:
    coordinator:
      model: claude-sonnet-4-5-20250929  # Sonnet, not Opus, for local dev
      role: "Plan tasks and coordinate"
    developer:
      model: claude-sonnet-4-5-20250929
      role: "Implement features"
    tester:
      model: claude-haiku-4-5-20251001
      role: "Write and run tests"
```

## Tier 2: Team CI/CD

### Setup

Team deployment integrates Agent Foundry into shared CI/CD pipelines so agents run automatically on pull requests, merges, or scheduled triggers.

**Step 1: Store API Key as CI/CD Secret**

```bash
# GitHub Actions
gh secret set ANTHROPIC_API_KEY --body "sk-ant-api03-..."

# GitLab CI
# Settings > CI/CD > Variables > Add: ANTHROPIC_API_KEY

# Jenkins
# Manage Jenkins > Credentials > Add: ANTHROPIC_API_KEY
```

**Step 2: Create CI/CD Workflow**

GitHub Actions example:

```yaml
# .github/workflows/agent-foundry.yml
name: Agent Foundry Review

on:
  pull_request:
    branches: [main]

permissions:
  contents: read
  pull-requests: write

jobs:
  agent-review:
    runs-on: ubuntu-latest
    timeout-minutes: 30

    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 0  # Full history for context

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install Claude Code
        run: npm install -g @anthropic-ai/claude-code

      - name: Run Code Review Agent
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          claude-code --print \
            --model claude-sonnet-4-5-20250929 \
            --allowedTools "Bash,Read,Grep,Glob" \
            "Review the changes in this PR. Focus on correctness, security,
             and performance. Output your review as a structured markdown report."

      - name: Run Test Coverage Agent
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          claude-code --print \
            --model claude-haiku-4-5-20251001 \
            --allowedTools "Bash,Read,Write,Edit" \
            "Check test coverage for changed files. If coverage is below 80%,
             write additional tests to improve it."
```

**Step 3: Configure Agent Permissions**

In CI/CD, agents should have restricted permissions:

```yaml
# Agent permissions for CI/CD (restrictive)
ci_agent_config:
  allowed_tools:
    code_review: ["Bash", "Read", "Grep", "Glob"]  # Read-only
    test_writer: ["Bash", "Read", "Write", "Edit", "Grep", "Glob"]  # Can write tests
    implementer: ["Bash", "Read", "Write", "Edit", "Grep", "Glob"]  # Full access

  restricted_paths:
    - ".env*"           # Never read or write env files
    - "**/*.key"        # Never access key files
    - "**/*.pem"        # Never access certificates
    - ".git/**"         # No direct git manipulation

  network:
    allowed_hosts:
      - "api.anthropic.com"
      - "registry.npmjs.org"
    blocked: ["*"]  # Block all other network access
```

### CI/CD Patterns

**Pattern 1: PR Review Agent**
Runs on every pull request. Reviews code, checks for issues, posts comments.

**Pattern 2: Post-Merge Enhancement**
Runs after merge to main. Generates documentation updates, checks for dependency issues, opens follow-up issues.

**Pattern 3: Scheduled Maintenance**
Runs on a cron schedule. Audits dependencies, checks for security vulnerabilities, generates reports.

**Pattern 4: On-Demand Team**
Triggered manually (workflow_dispatch) for large tasks like migrations or refactoring. Runs a full agent team with orchestration.

### Team CI/CD Best Practices

- **Set strict timeouts**: CI agents should never run indefinitely. Set 15-30 minute timeouts.
- **Use read-only agents for review**: Review agents should not have write permissions. This prevents accidental modifications.
- **Cache aggressively**: Cache node_modules, Claude Code installation, and any reusable context between runs.
- **Log everything**: Write agent outputs to CI artifacts for post-run debugging.
- **Separate API keys**: Use a dedicated API key for CI/CD, separate from developer keys, so you can track CI usage and set independent rate limits.

## Tier 3: Enterprise Self-Hosted

### Architecture

Enterprise deployment adds a control plane layer between Agent Foundry and the infrastructure.

```
                    +------------------+
                    |  Control Plane   |
                    |  (Orchestration  |
                    |   API, Auth,     |
                    |   Monitoring)    |
                    +--------+---------+
                             |
              +--------------+--------------+
              |              |              |
       +------+------+ +----+----+ +-------+------+
       | Agent Pool  | | Agent   | | State Store  |
       | (Workers)   | | Queue   | | (Redis/PG)   |
       +------+------+ +----+----+ +-------+------+
              |              |              |
              +--------------+--------------+
                             |
                    +--------+---------+
                    |  Anthropic API   |
                    |  (via Proxy)     |
                    +------------------+
```

### API Key Management

Enterprise deployments require careful key management:

```yaml
# Enterprise API key configuration
api_keys:
  management:
    strategy: "vault"  # Options: env, file, vault, aws-secrets-manager
    vault_config:
      address: "https://vault.internal.company.com"
      path: "secret/data/agent-foundry/api-keys"
      role: "agent-foundry-reader"

  rotation:
    enabled: true
    interval: "30d"
    notification: "security-team@company.com"

  per_team_keys:
    enabled: true  # Each team gets its own API key for usage tracking
    naming: "af-{team_name}-{environment}"

  rate_limit_distribution:
    production_teams: 60%   # Share of overall rate limit
    staging_teams: 25%
    development: 15%
```

### MCP Server Setup

MCP (Model Context Protocol) servers extend agent capabilities by connecting them to external tools and data sources.

```yaml
# MCP server configuration
mcp_servers:
  # Database access for agents
  postgres:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-postgres"]
    env:
      DATABASE_URL: "${POSTGRES_CONNECTION_STRING}"
    allowed_agents: ["data-analyst", "backend-dev"]

  # File system access (sandboxed)
  filesystem:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/workspace"]
    allowed_agents: ["*"]  # All agents

  # GitHub integration
  github:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      GITHUB_TOKEN: "${GITHUB_TOKEN}"
    allowed_agents: ["orchestrator", "code-reviewer"]

  # Slack notifications
  slack:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-slack"]
    env:
      SLACK_BOT_TOKEN: "${SLACK_BOT_TOKEN}"
    allowed_agents: ["orchestrator"]
```

### Workspace Configuration

Enterprise workspaces need isolation and auditing:

```yaml
# Enterprise workspace configuration
workspace:
  base_path: "/opt/agent-foundry/workspaces"
  isolation: "container"  # Options: none, directory, container

  per_team:
    create_on_launch: true
    cleanup_after: "24h"
    max_disk: "10GB"

  git:
    clone_depth: 50  # Limit history for performance
    ssh_key_path: "/etc/agent-foundry/deploy-keys/{repo}.key"
    allowed_repos:
      - "github.com/company/*"
    blocked_repos:
      - "github.com/company/secrets-*"

  audit:
    log_all_file_operations: true
    log_all_commands: true
    retention: "90d"
    destination: "s3://company-audit-logs/agent-foundry/"
```

### Security Considerations

#### Network Security

```yaml
security:
  network:
    # Outbound allowlist
    allowed_outbound:
      - "api.anthropic.com:443"
      - "registry.npmjs.org:443"
      - "github.com:443"
    # Everything else blocked by default

    # Internal services
    allowed_internal:
      - "vault.internal:8200"
      - "postgres.internal:5432"
      - "redis.internal:6379"

  # Agent sandboxing
  sandboxing:
    enabled: true
    method: "docker"  # Options: docker, nsjail, firejail
    capabilities_drop: ["NET_RAW", "SYS_ADMIN"]
    read_only_paths: ["/etc", "/usr"]
    writable_paths: ["/workspace", "/tmp"]
    max_memory: "4GB"
    max_cpu: "2"
    max_pids: 100
```

#### Secret Management

```yaml
security:
  secrets:
    # Never expose these to agents
    blocked_env_vars:
      - "AWS_SECRET_ACCESS_KEY"
      - "DATABASE_PASSWORD"
      - "GITHUB_TOKEN"  # Use MCP server instead of raw token
      - "SLACK_BOT_TOKEN"  # Use MCP server instead

    # Scan agent output for leaked secrets
    output_scanning:
      enabled: true
      patterns:
        - "sk-ant-.*"       # Anthropic API keys
        - "ghp_.*"          # GitHub tokens
        - "AKIA.*"          # AWS access keys
        - "-----BEGIN.*KEY" # Private keys
      on_detection: "redact_and_alert"
```

#### Audit and Compliance

```yaml
audit:
  # Log every agent action
  agent_actions:
    log_level: "full"  # Options: minimal, standard, full
    include:
      - "file_reads"
      - "file_writes"
      - "commands_executed"
      - "api_calls"
      - "model_interactions"

  # Compliance reporting
  compliance:
    frameworks: ["SOC2", "GDPR"]
    data_residency: "us-east-1"
    pii_scanning: true
    retention_policy: "90d"

  # Access control
  rbac:
    enabled: true
    roles:
      admin:
        permissions: ["*"]
      team_lead:
        permissions: ["launch_team", "view_logs", "set_budget"]
      developer:
        permissions: ["launch_team", "view_own_logs"]
      viewer:
        permissions: ["view_logs"]
```

### Docker Deployment

```dockerfile
# Dockerfile for Agent Foundry worker
FROM node:20-slim

# Install dependencies
RUN npm install -g @anthropic-ai/claude-code
RUN apt-get update && apt-get install -y git curl jq && rm -rf /var/lib/apt/lists/*

# Create non-root user for agent execution
RUN useradd -m -s /bin/bash agent
USER agent
WORKDIR /home/agent

# Copy configuration
COPY --chown=agent:agent config/ /home/agent/.config/agent-foundry/

# Workspace mount point
VOLUME ["/workspace"]

# Entry point
ENTRYPOINT ["claude-code"]
```

```yaml
# docker-compose.yml for local enterprise testing
version: '3.8'
services:
  agent-worker:
    build: .
    environment:
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
    volumes:
      - ./workspace:/workspace
      - ./logs:/home/agent/logs
    deploy:
      resources:
        limits:
          memory: 4G
          cpus: '2.0'
    networks:
      - agent-net

  state-store:
    image: redis:7-alpine
    networks:
      - agent-net

networks:
  agent-net:
    driver: bridge
```

## Environment Comparison

| Aspect | Local Dev | Team CI/CD | Enterprise |
|---|---|---|---|
| **API Key Storage** | Env variable | CI secret | Vault / Secrets Manager |
| **Agent Isolation** | None | CI runner | Container / sandbox |
| **Network Control** | Open | Runner network | Strict allowlist |
| **Audit Logging** | Optional | CI logs | Full audit trail |
| **Cost Control** | Manual | Per-workflow cap | Budget management system |
| **MCP Servers** | Local process | Runner process | Managed services |
| **State Storage** | Local files | CI artifacts | Redis / PostgreSQL |
| **Scaling** | Single machine | Runner pool | Worker fleet |

## Recommendations

### For solo developers
Use Tier 1 (local) with environment variable API key. Add a budget cap to your configuration. Focus on learning the workflow before adding infrastructure.

### For small teams (2-10 developers)
Use Tier 2 (CI/CD) for automated review and testing. Keep local development as Tier 1. Share a team API key through CI secrets. Set per-workflow cost limits.

### For larger teams (10-50 developers)
Transition to Tier 3 basics: centralized API key management, per-team keys, audit logging, and container-based agent isolation. Run MCP servers as managed services.

### For enterprise (50+ developers, compliance requirements)
Full Tier 3: vault-based secrets, container sandboxing, network allowlisting, RBAC, full audit logging, compliance reporting, and centralized budget management. Plan for 2-4 weeks of infrastructure setup before team onboarding.

### For air-gapped environments
Agent Foundry requires API access to Anthropic. For air-gapped environments, explore Anthropic's enterprise offerings for on-premises model hosting or use a secure proxy that bridges the gap.

## Related Resources

- [Harness Comparison](./harness-comparison.md) — Choosing the right harness for CI/CD vs. local development
- [Decision Framework](./decision-framework.md) — Team composition decisions for different deployment contexts
- [Optimization Guide](./optimization-guide.md) — Cost optimization across deployment tiers
- [Quality Assurance](./quality-assurance.md) — QA strategies for CI/CD-integrated agent teams
