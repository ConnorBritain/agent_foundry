# Deployment Guide -- Recruitment & HR Team

## Prerequisites

### Required
- **Claude API access** with the following models enabled:
  - `claude-opus-4-6` (Coordinator agent)
  - `claude-sonnet-4-5` (Talent Acquisition, Onboarding, Culture, Performance agents)
  - `claude-haiku-4-5` (Compensation & Benefits agent)
- **MCP server framework** installed and configured
- **Git** for version-controlled deliverables
- **Node.js 18+** for MCP server runtime

### Optional (Recommended)
- **Lever API key** for ATS integration (posting jobs, tracking candidates)
- **BambooHR API key** for HRIS integration (employee data, time-off, performance)
- **Slack/Teams webhook** for agent notifications and status updates

### API Rate Limits
Ensure your API plan supports:
- At least 4 concurrent agent sessions (Phase 2 and 3 run agents in parallel)
- Minimum 100K tokens per minute throughput
- Opus 4.6 access (may require specific plan tier)

---

## Step 1: Repository Setup

### Initialize the deliverables repository

```bash
# Create a new repository for People operations deliverables
mkdir people-ops && cd people-ops
git init

# Create the directory structure for deliverables
mkdir -p deliverables/{people-strategy,hiring-playbook/{job-descriptions,interview-guides,scorecards,sourcing,offers,candidate-experience},onboarding-program/{training-paths,surveys},compensation-package,culture-launch,performance-system,recruiting-operations}

# Create a .gitignore
cat > .gitignore << 'EOF'
# Environment and secrets
.env
.env.local
*.key
*.pem

# MCP server credentials
mcp-servers/*.secret

# Node modules
node_modules/

# OS files
.DS_Store
Thumbs.db

# Temporary files
*.tmp
*.draft
EOF

git add .
git commit -m "feat(people): initialize people operations repository"
```

### Configure branch protection

```bash
# Create the main working branches
git checkout -b people-ops/foundation
git checkout -b people-ops/hiring-infrastructure
git checkout -b people-ops/onboarding-program
git checkout -b people-ops/culture-framework
git checkout -b people-ops/performance-system
git checkout -b people-ops/compensation-package
git checkout -b people-ops/optimization
git checkout main
```

---

## Step 2: Configuration

### Populate CONFIG.md

```bash
# Copy the configuration template
cp /path/to/agent_templates/teams/recruitment-hr/CONFIG.md ./config.yaml

# Edit with your company-specific details
# IMPORTANT: Fill in ALL bracketed values. The team will produce generic
# outputs if configuration is incomplete.
```

**Critical configuration fields:**
1. `company_stage` -- Determines the complexity and formality of outputs
2. `current_headcount` and `target_headcount` -- Drives org design and hiring plan
3. `culture.values` -- Must be specific behavioral descriptions, not generic words
4. `compensation_philosophy.salary_positioning` -- Affects all salary band calculations
5. `hiring_priorities.open_roles` -- Determines which job descriptions get created

### Validate configuration

Before running the team, verify:
- [ ] No bracketed placeholder values remain
- [ ] Headcount numbers are realistic for the stated company stage
- [ ] Values are specific enough to differentiate your company from others
- [ ] Compensation positioning is consistent with funding and stage
- [ ] At least one open role is listed with urgency level

---

## Step 3: MCP Server Setup

### Install MCP server dependencies

```bash
# Navigate to MCP servers directory
cd /path/to/agent_templates/teams/recruitment-hr/mcp-servers

# Install dependencies (if using npm-based MCP framework)
npm install @anthropic/mcp-server
```

### Configure Lever ATS integration (optional)

```bash
# Set Lever API credentials
export LEVER_API_KEY="your-lever-api-key"

# Or create a .env file
echo "LEVER_API_KEY=your-lever-api-key" >> .env

# Test the connection
curl -s -u "$LEVER_API_KEY:" https://api.lever.co/v1/postings | head -c 200
```

The Lever MCP server provides:
- `postings` -- Create and manage job postings
- `candidates` -- Search and manage candidate profiles
- `applications` -- Track application status
- `interviews` -- Schedule and manage interviews
- `offers` -- Create and track offers

### Configure BambooHR HRIS integration (optional)

```bash
# Set BambooHR credentials
export BAMBOOHR_API_KEY="your-bamboohr-api-key"
export BAMBOOHR_SUBDOMAIN="your-company"

# Test the connection
curl -s -H "Accept: application/json" \
  -u "$BAMBOOHR_API_KEY:x" \
  "https://api.bamboohr.com/api/gateway.php/$BAMBOOHR_SUBDOMAIN/v1/employees/directory" | head -c 200
```

The BambooHR MCP server provides:
- `employees` -- Employee directory and profiles
- `time-off` -- PTO balances and requests
- `performance` -- Performance review data
- `reports` -- Custom and standard reports

### Register MCP servers with the agent framework

```json
{
  "mcp_servers": [
    {
      "name": "lever",
      "config_path": "./mcp-servers/lever.json",
      "enabled": true,
      "credentials_env": "LEVER_API_KEY"
    },
    {
      "name": "bamboohr",
      "config_path": "./mcp-servers/bamboohr.json",
      "enabled": true,
      "credentials_env": "BAMBOOHR_API_KEY"
    }
  ]
}
```

---

## Step 4: Agent Initialization

### Load agent configurations

Each agent is initialized with its AGENTS.md system prompt and the shared configuration context.

```bash
# Agent initialization order matters for Phase 1
# Phase 1 agents must be initialized sequentially

# 1. Initialize Coordinator (always first)
claude-agent init \
  --name "coordinator" \
  --model "claude-opus-4-6" \
  --system-prompt "./agents/coordinator/AGENTS.md" \
  --context "./config.yaml" \
  --max-tokens 16384 \
  --temperature 0.6

# 2. Initialize Culture & Engagement (needs Coordinator output)
claude-agent init \
  --name "culture-engagement" \
  --model "claude-sonnet-4-5" \
  --system-prompt "./agents/culture-engagement/AGENTS.md" \
  --context "./config.yaml" \
  --max-tokens 12288 \
  --temperature 0.7

# 3. Initialize Performance Management (needs Coordinator + Culture output)
claude-agent init \
  --name "performance-management" \
  --model "claude-sonnet-4-5" \
  --system-prompt "./agents/performance-management/AGENTS.md" \
  --context "./config.yaml" \
  --max-tokens 12288 \
  --temperature 0.4

# 4-6. Initialize parallel agents (can run simultaneously)
claude-agent init \
  --name "talent-acquisition" \
  --model "claude-sonnet-4-5" \
  --system-prompt "./agents/talent-acquisition/AGENTS.md" \
  --context "./config.yaml" \
  --max-tokens 12288 \
  --temperature 0.7

claude-agent init \
  --name "onboarding-enablement" \
  --model "claude-sonnet-4-5" \
  --system-prompt "./agents/onboarding-enablement/AGENTS.md" \
  --context "./config.yaml" \
  --max-tokens 12288 \
  --temperature 0.5

claude-agent init \
  --name "compensation-benefits" \
  --model "claude-haiku-4-5" \
  --system-prompt "./agents/compensation-benefits/AGENTS.md" \
  --context "./config.yaml" \
  --max-tokens 8192 \
  --temperature 0.3
```

---

## Step 5: Phase Execution

### Phase 1: Foundation (Sequential)

```bash
# Step 1.1: People Strategy
claude-agent run coordinator \
  --task "Define people strategy based on configuration" \
  --output "deliverables/people-strategy/strategy.md" \
  --branch "people-ops/foundation"

# Wait for completion, then pass output to next agent

# Step 1.2: Values & Culture Design
claude-agent run culture-engagement \
  --task "Design culture framework based on people strategy" \
  --input "deliverables/people-strategy/strategy.md" \
  --output "deliverables/culture-launch/culture-framework.md" \
  --branch "people-ops/foundation"

# Wait for completion, then pass output to next agent

# Step 1.3: Role Frameworks & Career Ladders
claude-agent run performance-management \
  --task "Create role frameworks and career ladders" \
  --input "deliverables/people-strategy/strategy.md,deliverables/culture-launch/culture-framework.md" \
  --output "deliverables/performance-system/role-frameworks.md,deliverables/performance-system/career-ladders.md" \
  --branch "people-ops/foundation"

# Verify Phase 1 quality gates
claude-agent run coordinator \
  --task "Review Phase 1 outputs against quality gates" \
  --input "deliverables/people-strategy/,deliverables/culture-launch/,deliverables/performance-system/" \
  --output "deliverables/phase-1-review.md"
```

### Phase 2: Infrastructure (Parallel)

```bash
# All three streams run simultaneously
# Collect Phase 1 outputs as shared context

PHASE1_CONTEXT="deliverables/people-strategy/strategy.md,deliverables/culture-launch/culture-framework.md,deliverables/performance-system/role-frameworks.md,deliverables/performance-system/career-ladders.md"

# Stream 2A: Hiring Playbook
claude-agent run talent-acquisition \
  --task "Build complete hiring playbook" \
  --input "$PHASE1_CONTEXT" \
  --output "deliverables/hiring-playbook/" \
  --branch "people-ops/hiring-infrastructure" &

# Stream 2B: Onboarding Program
claude-agent run onboarding-enablement \
  --task "Design end-to-end onboarding program" \
  --input "$PHASE1_CONTEXT" \
  --output "deliverables/onboarding-program/" \
  --branch "people-ops/onboarding-program" &

# Stream 2C: Compensation & Benefits
claude-agent run compensation-benefits \
  --task "Build compensation and benefits package" \
  --input "$PHASE1_CONTEXT" \
  --output "deliverables/compensation-package/" \
  --branch "people-ops/compensation-package" &

# Wait for all parallel streams to complete
wait

# Cross-check: Ensure salary bands align with job descriptions
claude-agent run coordinator \
  --task "Verify Phase 2 cross-functional consistency" \
  --input "deliverables/hiring-playbook/,deliverables/onboarding-program/,deliverables/compensation-package/" \
  --output "deliverables/phase-2-review.md"
```

### Phase 3: Execution (Parallel)

```bash
# All four streams run simultaneously
PHASE2_CONTEXT="$PHASE1_CONTEXT,deliverables/hiring-playbook/,deliverables/onboarding-program/,deliverables/compensation-package/"

# Stream 3A: Active Recruiting
claude-agent run talent-acquisition \
  --task "Create recruiting operations materials" \
  --input "$PHASE2_CONTEXT" \
  --output "deliverables/recruiting-operations/" \
  --branch "people-ops/hiring-infrastructure" &

# Stream 3B: Onboarding Execution
claude-agent run onboarding-enablement \
  --task "Build onboarding execution toolkit" \
  --input "$PHASE2_CONTEXT" \
  --output "deliverables/onboarding-program/" \
  --branch "people-ops/onboarding-program" &

# Stream 3C: Culture Launch
claude-agent run culture-engagement \
  --task "Create culture launch materials and engagement tools" \
  --input "$PHASE2_CONTEXT" \
  --output "deliverables/culture-launch/" \
  --branch "people-ops/culture-framework" &

# Stream 3D: Performance Activation
claude-agent run performance-management \
  --task "Build performance management tools and processes" \
  --input "$PHASE2_CONTEXT" \
  --output "deliverables/performance-system/" \
  --branch "people-ops/performance-system" &

wait
```

### Phase 4: Optimization (Parallel)

```bash
# Coordinator leads analysis, specialists refine
ALL_DELIVERABLES="deliverables/"

# Stream 4A: System-wide analysis
claude-agent run coordinator \
  --task "Analyze all deliverables, identify gaps, produce optimization report" \
  --input "$ALL_DELIVERABLES" \
  --output "deliverables/optimization-report.md" \
  --branch "people-ops/optimization" &

# Stream 4B: Agent refinements (lightweight)
for agent in talent-acquisition onboarding-enablement culture-engagement performance-management compensation-benefits; do
  claude-agent run $agent \
    --task "Review and refine own deliverables, add version notes" \
    --input "$ALL_DELIVERABLES" \
    --branch "people-ops/optimization" &
done

wait

# Final merge
git checkout main
for branch in foundation hiring-infrastructure onboarding-program culture-framework performance-system compensation-package optimization; do
  git merge "people-ops/$branch" --no-ff -m "feat(people): merge $branch deliverables"
done
```

---

## Step 6: Post-Execution

### Review deliverables

```bash
# List all generated deliverables
find deliverables/ -name "*.md" | sort

# Check for completeness
claude-agent run coordinator \
  --task "Final quality review of all deliverables" \
  --input "deliverables/" \
  --output "deliverables/final-review.md"
```

### Export for team use

```bash
# Generate a table of contents
find deliverables/ -name "*.md" -exec echo "- {}" \; | sort > deliverables/INDEX.md

# If using Notion, export as markdown for import
# If using Google Docs, convert markdown to docs format
# If using Confluence, use the markdown import feature
```

### Schedule recurring processes

The following deliverables define recurring processes that need calendar scheduling:

| Process | Frequency | Owner |
|---------|-----------|-------|
| eNPS survey | Quarterly | Culture & Engagement |
| Pulse survey | Bi-weekly | Culture & Engagement |
| OKR setting | Quarterly | Performance Management |
| Performance reviews | Per review_cadence in config | Performance Management |
| Compensation review | Annual | Compensation & Benefits |
| Pay equity audit | Semi-annual | Compensation & Benefits |
| Pipeline review | Weekly | Talent Acquisition |
| Onboarding survey (Day 30) | Per new hire | Onboarding & Enablement |
| Onboarding survey (Day 90) | Per new hire | Onboarding & Enablement |
| People strategy review | Quarterly | Coordinator |

---

## Troubleshooting

### Common Issues

**Agent produces generic output**
- Check that CONFIG.md has specific values, not placeholders
- Ensure the values section contains behavioral descriptions, not single words
- Verify that open roles have detailed descriptions and urgency levels

**Phase 2 agents produce inconsistent outputs**
- Run the Phase 2 cross-check step (Coordinator review)
- Ensure all agents received the same Phase 1 context files
- Check that salary bands reference the same role frameworks as job descriptions

**Compensation numbers seem off**
- Verify `salary_positioning` and `reference_markets` in CONFIG
- Check that `company_stage` matches your actual funding situation
- Haiku may need more context for complex multi-geography compensation -- consider upgrading to Sonnet for this agent

**Onboarding plan is too generic**
- Provide more detail in the `departments` and `tools` sections of CONFIG
- Include specific training needs in `constraints` or `hiring_priorities`
- Consider running Onboarding on Sonnet instead of Haiku in budget mode

**Culture framework feels superficial**
- The `rewarded_behaviors` and `punished_behaviors` fields in CONFIG are critical
- Be honest about what your culture actually does, not what you wish it did
- Consider upgrading Culture agent to Opus for complex cultural situations

### Rate Limit Handling

If you hit API rate limits during parallel phases:

```bash
# Option 1: Add delay between agent starts
for agent in talent-acquisition onboarding-enablement compensation-benefits; do
  claude-agent run $agent --task "..." &
  sleep 5  # 5-second stagger
done

# Option 2: Reduce parallelism (run 2 agents at a time instead of 3-4)
claude-agent run talent-acquisition --task "..." &
claude-agent run compensation-benefits --task "..." &
wait
claude-agent run onboarding-enablement --task "..." &
claude-agent run culture-engagement --task "..." &
wait
```

### Recovery from Failed Phases

```bash
# If a phase fails partway through, check which deliverables exist
ls -la deliverables/

# Re-run only the failed agent(s) with the same inputs
# Phase outputs are idempotent -- re-running produces the same structure

# If Phase 1 fails, fix config and re-run from scratch
# If Phase 2 fails, re-run the failed stream only (others are independent)
# If Phase 3 fails, same as Phase 2
# If Phase 4 fails, it is safe to skip -- deliverables from Phases 1-3 are still usable
```
