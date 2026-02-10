# Deployment Guide

Step-by-step instructions for setting up the environment, configuring the team, and running the Code Implementation Team.

---

## Prerequisites

### Required Accounts

| Service | URL | Purpose | Required Tier |
|---------|-----|---------|--------------|
| GitHub | github.com | Code repository, branches, PRs | Free |

### Optional Accounts

| Service | URL | Purpose | Required Tier |
|---------|-----|---------|--------------|
| Linear | linear.app | Task tracking integration | Free |
| Jira | atlassian.com/jira | Enterprise task tracking | Free |
| Sentry | sentry.io | Error tracking context for bug fixes | Developer (Free) |

### Required CLI Tools

```bash
# GitHub CLI
# macOS:
brew install gh
# Linux:
# See https://github.com/cli/cli/blob/trunk/docs/install_linux.md

# Verify
gh --version
gh auth status
```

### Language-Specific Tools

Install the tools for your project's language and framework:

```bash
# Node.js / TypeScript projects
node --version  # >= 20.0.0
npm --version   # >= 10.0.0

# Python projects
python --version  # >= 3.10
pip --version

# Rust projects
rustc --version
cargo --version

# Go projects
go version  # >= 1.21
```

---

## Environment Variables

### Step 1: Generate API Keys

#### GitHub

1. Go to https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Name it "code-implementation-team"
4. Select scopes: `repo`, `workflow`
5. Copy the token

#### Linear (Optional)

1. Go to Settings > API > Personal API keys
2. Create a new key
3. Copy the key

#### Sentry (Optional)

1. Go to Settings > Auth Tokens
2. Create a new token with `project:read` scope
3. Copy the token

### Step 2: Set Environment Variables

```bash
# Required
export GITHUB_TOKEN="ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Optional
export LINEAR_API_KEY=""
export JIRA_TOKEN=""
export SENTRY_AUTH_TOKEN=""
```

### Step 3: Verify Environment

```bash
echo "GitHub: ${GITHUB_TOKEN:+SET}"
gh auth status
```

Should print "SET" and show your authenticated GitHub account.

---

## Configuration

### Step 1: Configure the Project

```bash
cd teams/code-implementation

# Copy and edit the configuration
cp CONFIG.md CONFIG.local.md
```

Edit `CONFIG.local.md` with your project settings. At minimum, fill in:
- `repository.url` -- Your GitHub repository
- `feature.name` -- Short name for the feature
- `feature.spec_path` or `feature.description` -- What to build
- `primary_language` -- Your project's language
- `framework` -- Your project's framework
- `testing_framework` -- Your test runner

### Step 2: Select Model Configuration

In `CONFIG.local.md`, set the model configuration:

```yaml
agent_budget:
  model_config: default  # Options: budget, default, premium
```

See `MODEL_CONFIGS.md` for detailed comparison.

---

## Running the Team

### Full Run (Recommended)

```bash
claude-agent team run ./teams/code-implementation \
  --config CONFIG.local.md \
  --mode hybrid

# Expected duration: ~60-90 minutes
# Expected cost: ~$25-30 (default config)
```

The team pauses at each phase boundary for user confirmation. You can review progress and decide whether to continue.

### Phase-by-Phase Run

Run individual phases for more control:

```bash
# Phase 1: Planning
claude-agent team run ./teams/code-implementation \
  --config CONFIG.local.md \
  --mode hybrid \
  --phase 1

# Review the plan, then proceed:

# Phase 2: Implementation
claude-agent team run ./teams/code-implementation \
  --config CONFIG.local.md \
  --mode hybrid \
  --phase 2

# Phase 3: Code Review
claude-agent team run ./teams/code-implementation \
  --config CONFIG.local.md \
  --mode hybrid \
  --phase 3

# Phase 4: Testing + Documentation
claude-agent team run ./teams/code-implementation \
  --config CONFIG.local.md \
  --mode hybrid \
  --phase 4
```

### What Happens at Each Phase

**Phase 1 -- Planning (~10 min):**
1. Coordinator reads feature spec and analyzes codebase
2. Decomposes feature into tasks with dependency graph
3. Assigns tasks to Specialists A and B
4. Prompts user to review and approve the plan

**Phase 2 -- Implementation (~20-40 min):**
1. Specialist A implements primary tasks on `agent/impl-a/` branch
2. Specialist B implements secondary tasks on `agent/impl-b/` branch
3. Test Engineer writes holdout test scenarios in parallel
4. Prompts user to review implementation branches

**Phase 3 -- Code Review (~15-25 min):**
1. Code Reviewer examines both branches
2. Identifies blockers and suggestions
3. Specialists fix blockers, Reviewer re-reviews
4. Branches merge to `feature/[name]` branch
5. Prompts user to review findings

**Phase 4 -- Testing + Documentation (~15-20 min):**
1. Test Engineer runs holdout scenarios and generates tests
2. Documentation Writer updates docs and changelog
3. CI commands run (lint, typecheck, test, build)
4. Prompts user with results and merge decision

---

## Post-Run Verification

After the team completes, verify the output:

### 1. Review the Feature Branch

```bash
git checkout feature/[feature-name]
git log --oneline  # Review commit history
git diff main      # Review all changes
```

### 2. Run CI Locally

```bash
# Run the same checks the team ran
npm run lint
npx tsc --noEmit
npm run test
npm run build
```

### 3. Review the Pull Request

If `create_pr: true` in CONFIG, a pull request was created automatically. Review:
- PR description includes test results and coverage
- All CI checks pass
- Changes match the feature specification

### 4. Merge

After human review, merge the PR via your normal workflow.

---

## Troubleshooting

### Common Issues

**GitHub authentication fails:**
- Verify `GITHUB_TOKEN` is valid and has `repo` and `workflow` scopes
- Run `gh auth status` to check authentication

**Specialist branch conflicts:**
- The Coordinator assigns file ownership to prevent conflicts
- If a conflict occurs, the Code Reviewer resolves it during Phase 3
- Persistent conflicts indicate the feature needs better decomposition

**Code Reviewer cannot approve after max cycles:**
- Increase `max_review_cycles` in CONFIG, or
- Review the Reviewer's findings manually and decide which to defer
- Consider splitting the feature into smaller, more focused pieces

**Test coverage below threshold:**
- The Test Engineer flags coverage gaps in the Phase 4 report
- Lower the `coverage_threshold` in CONFIG, or
- Request additional tests by re-running Phase 4

**Cost exceeds budget:**
- The Coordinator alerts when approaching `max_total_cost_usd`
- Reduce feature scope or switch to Budget model configuration
- Review Phase 1 plan for tasks that can be deferred
