# Project Planning Team

A 7-agent team template for transforming high-level goals into actionable, scheduled project plans across multiple frameworks (SAFe, Agile Scrum, Agile Kanban, Shape Up, Waterfall, and custom).

## What This Team Produces

This team delivers a complete, structured project plan in approximately 1-2 hours of agent execution time:

- **Requirements documentation** -- Structured requirements with acceptance criteria, stakeholder mapping, and scope boundaries
- **Task breakdown structure** -- Granular tasks with effort estimates, dependencies, and ownership assignments
- **Dependency graph** -- Visual dependency map with critical path identification and bottleneck analysis
- **Prioritized backlog** -- Tasks ranked by business value, urgency, and resource constraints using framework-appropriate methods
- **Resource allocation plan** -- Team capacity mapping, skill-gap analysis, and workload distribution
- **Risk register** -- Identified risks with probability, impact, mitigation strategies, and contingency plans
- **Integration plan** -- Cross-team dependencies, API contracts, milestone synchronization, and communication protocols
- **Calendar with milestones** -- Sprint boundaries, release dates, and stakeholder checkpoints exported to Linear, Jira, or Google Calendar

## When to Use This Template

Use this team when you need to:

- Plan a new software project with more than 20 tasks across multiple workstreams
- Run SAFe PI Planning, Scrum sprint planning, or Shape Up betting table sessions
- Create a quarterly roadmap with cross-team dependencies
- Onboard a new engineering team to an existing project with structured handoffs
- Translate a business strategy into an engineering execution plan
- Plan a system migration with phased rollouts and risk management

Do **not** use this team for:

- Simple to-do lists with fewer than 10 tasks (use a single agent)
- Operational runbooks or documentation (use Content Creation team)
- Code implementation (use Code Implementation or Web App Development team)
- Business strategy formulation (use C-Suite team, then feed output here)

## Supported Frameworks

| Framework | Best For | Key Artifacts |
|-----------|----------|---------------|
| SAFe | Enterprise, multi-team programs | Program Board, PI Objectives, Feature Kanban |
| Agile Scrum | Small-medium teams, iterative delivery | Sprint Backlog, Burndown Chart, Definition of Done |
| Agile Kanban | Continuous flow, support/ops teams | Kanban Board, WIP Limits, Cumulative Flow Diagram |
| Shape Up | Product teams, 6-week cycles | Pitch Document, Hill Chart, Scope Map |
| Waterfall | Regulated industries, fixed-scope | Gantt Chart, Requirements Matrix, Phase Gates |
| Custom | Unique workflows | Negotiated with Coordinator at setup |

## Tool Integrations

| Tool | Purpose | Required |
|------|---------|----------|
| Linear | Issue creation, cycle management, project tracking | At least one task tool required |
| Jira | Enterprise issue tracking, sprint management | Alternative to Linear |
| Google Calendar | Milestone events, sprint boundaries, deadline reminders | Recommended |

## Quick Start

### 1. Prerequisites

Ensure you have accounts and API keys for at least one task management tool:
- Linear (recommended) or Jira
- Google Calendar (optional but recommended)

### 2. Configure the Team

Copy and edit the configuration file:

```bash
cp CONFIG.md CONFIG.local.md
# Edit CONFIG.local.md with your project settings
```

Set the required environment variables:

```bash
export LINEAR_API_KEY="lin_api_..."           # From Linear Settings > API
export GOOGLE_CALENDAR_TOKEN="your-token"     # From Google Cloud Console
# OR for Jira users:
export JIRA_API_TOKEN="your-jira-token"
export JIRA_DOMAIN="your-company.atlassian.net"
export JIRA_EMAIL="your-email@company.com"
```

### 3. Run the Team

Execute in hybrid mode (recommended):

```bash
claude-agent team run ./teams/project-planning \
  --config CONFIG.local.md \
  --mode hybrid
```

Or in sequential mode for more control:

```bash
claude-agent team run ./teams/project-planning \
  --config CONFIG.local.md \
  --mode sequential
```

### 4. Monitor Progress

The coordinator agent logs phase transitions and deliverables. Watch the output for:

```
[Phase 1/7] Configuration -- Starting...
  [coordinator] Framework selected: agile_scrum
  [coordinator] Configuration validated
[Phase 1/7] Configuration -- Complete

[Phase 2/7] Requirements Analysis -- Starting...
  [requirements-analyst] Analyzing project vision...
  [requirements-analyst] 5 workstreams identified, 3 questions for user
[Phase 2/7] Requirements Analysis -- Complete (user review requested)
```

## Team Composition

| Agent | Model | Role |
|-------|-------|------|
| Coordinator | Sonnet 4.5 | Framework selection, workflow orchestration, quality gates, user communication |
| Requirements Analyst | Sonnet 4.5 | Vision decomposition, scope definition, acceptance criteria, stakeholder mapping |
| Task Decomposer | Sonnet 4.5 | Granular task creation, effort estimation, work breakdown structure |
| Scheduler | Sonnet 4.5 | Calendar integration, milestone planning, sprint/cycle boundaries, timeline optimization |
| Resource Allocator | Opus 4.6 | Capacity planning, skill-gap analysis, workload balancing, trade-off decisions |
| Risk Assessor | Sonnet 4.5 | Risk identification, probability/impact analysis, mitigation planning |
| Integration Planner | Haiku 4.5 | Cross-team dependencies, API contracts, documentation generation, tool export |

## Estimated Cost

With default model configuration: **approximately $20-50** per planning session.

See `cost-analysis.md` for detailed breakdowns and alternative configurations.

## Directory Structure

```
teams/project-planning/
  README.md                          -- This file
  TEAM_SPEC.md                       -- Detailed architecture and specification
  MODEL_CONFIGS.md                   -- Model selection and cost comparison
  CONFIG.md                          -- Project configuration template
  ORCHESTRATION.md                   -- Multi-agent orchestration protocol
  cost-analysis.md                   -- Token budget and cost analysis
  deployment-guide.md                -- Step-by-step deployment instructions
  agents/
    coordinator/AGENTS.md            -- Coordinator agent spec
    requirements-analyst/AGENTS.md   -- Requirements Analyst agent spec
    task-decomposer/AGENTS.md        -- Task Decomposer agent spec
    scheduler/AGENTS.md              -- Scheduler agent spec
    resource-allocator/AGENTS.md     -- Resource Allocator agent spec
    risk-assessor/AGENTS.md          -- Risk Assessor agent spec
    integration-planner/AGENTS.md    -- Integration Planner agent spec
  mcp-servers/
    README.md                        -- MCP server setup guide
    linear.json                      -- Linear MCP server config
    jira.json                        -- Jira MCP server config
    google-calendar.json             -- Google Calendar MCP server config
  scenarios/
    sprint-planning.md               -- Sprint planning scenario
    quarterly-roadmap.md             -- Quarterly roadmap scenario
    cross-team-coordination.md       -- Cross-team coordination scenario
    risk-assessment.md               -- Risk assessment scenario
  examples/
    saas-mvp-plan.md                 -- SaaS MVP planning example
    team-scaling-plan.md             -- Team scaling example
    migration-project.md             -- System migration example
```

## Key Design Principles

1. **Framework-first configuration.** The Coordinator selects the right methodology before any planning begins. Terminology, ceremonies, and artifacts adapt to the chosen framework.
2. **Progressive disclosure.** Only load framework-specific knowledge when the framework is selected. SAFe skills are not loaded for a Scrum project.
3. **User control at decision points.** Agents run autonomously within phases, but the user approves scope boundaries, priority cuts, and calendar commitments.
4. **Executable outputs.** Every plan produces artifacts that can be directly imported into Linear, Jira, or Google Calendar -- not just documents.
5. **Cost predictability.** Every phase has a token budget. Users know costs before committing to the next phase.

## Related Documentation

- [TEAM_SPEC.md](TEAM_SPEC.md) -- Full architecture specification
- [ORCHESTRATION.md](ORCHESTRATION.md) -- Phase-by-phase execution protocol
- [deployment-guide.md](deployment-guide.md) -- How to set up and run
- [cost-analysis.md](cost-analysis.md) -- Budget planning
