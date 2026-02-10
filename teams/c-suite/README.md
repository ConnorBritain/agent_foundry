# C-Suite Team

A 7-agent team template for creating comprehensive, executable business plans with integrated strategy, financials, pitch decks, org design, and go-to-market planning.

## What This Team Produces

This team delivers a complete, investor-ready business plan with executable artifacts in approximately 1-2 hours of agent execution time:

- **Business plan** -- Executive summary, market analysis, product strategy, operations, financials, risk mitigation (Notion)
- **Financial model** -- P&L projections, cash flow analysis, cap table, unit economics, hiring plan (Google Sheets)
- **Pitch deck** -- Problem, solution, market, traction, team, financials, the ask (Google Slides)
- **Product roadmap** -- Epics, features, dependencies, release timeline, MVP definition (Linear)
- **Sales playbook** -- ICP, sales process, pipeline model, objection handling, pricing strategy (Notion)
- **Marketing plan** -- Channel strategy, content calendar, campaign briefs, budget allocation (Notion)
- **Org chart** -- Current and future state, role definitions, hiring sequence, compensation bands
- **Legal checklist** -- Entity formation, compliance calendar, contract templates, IP strategy (Notion)

## When to Use This Template

Use this team when you need to:

- Launch a new startup and need a comprehensive business plan
- Prepare for fundraising with investor-ready artifacts
- Plan a new business unit or product line within an existing company
- Structure a pivot with cross-functional alignment
- Develop a go-to-market strategy requiring financial, legal, and operational coordination
- Create a business plan that other agent teams can execute against

Do **not** use this team for:

- Simple one-page business model canvases (use a single agent)
- Financial modeling only (use the CFO agent standalone or a spreadsheet tool)
- Technical architecture decisions only (use the Code Implementation team)
- Content marketing execution (use the Content Creation team -- this team produces the strategy)
- Ongoing operational management (this team plans; execution requires other teams)

## Team Composition

| Agent | Model | Role |
|-------|-------|------|
| CEO / Strategy Lead | Opus 4.6 | Vision, prioritization, strategic decisions, board facilitation, plan synthesis |
| CFO / Finance | Sonnet 4.5 | Financial modeling, projections, budgeting, unit economics, funding strategy |
| CMO / Marketing | Sonnet 4.5 | Market research, positioning, go-to-market, growth strategy, content planning |
| CTO / Product | Sonnet 4.5 | Product roadmap, technical feasibility, build vs buy, MVP definition |
| COO / Operations | Sonnet 4.5 | Process design, org structure, hiring plans, operational metrics |
| VP Sales | Sonnet 4.5 | Sales strategy, pipeline model, pricing, ICP, channel development |
| General Counsel | Sonnet 4.5 | Entity structure, compliance, contracts, IP strategy, risk mitigation |

## Quick Start

### 1. Prerequisites

Ensure you have accounts and API keys for:
- Google Workspace (Sheets and Slides for financial models and pitch decks)
- Notion (business plan, sales playbook, marketing plan, legal checklist)

Optional but recommended:
- Linear (product roadmap)
- Stripe (if setting up payment infrastructure)

### 2. Configure the Team

Copy and edit the configuration file:

```bash
cp CONFIG.md CONFIG.local.md
# Edit CONFIG.local.md with your business context
```

### 3. Run the Team

Execute in hybrid mode (recommended):

```bash
claude-agent team run ./teams/c-suite \
  --config CONFIG.local.md \
  --mode hybrid
```

Or in sequential mode for deeper founder involvement:

```bash
claude-agent team run ./teams/c-suite \
  --config CONFIG.local.md \
  --mode sequential
```

### 4. Monitor Progress

The CEO agent logs phase transitions and board meeting outcomes:

```
[Phase 1/6] Vision Alignment -- Starting...
  [ceo] Vision and mission defined
  [ceo] Key strategic questions distributed to specialists
  [ceo] Board brief created
[Phase 1/6] Vision Alignment -- Complete

[Phase 2/6] Specialist Deep-Dives -- Starting (parallel)...
  [cfo] Financial model: 3-year P&L draft complete
  [cmo] Market sizing: TAM/SAM/SOM calculated
  [cto] Product roadmap: MVP scope defined
  [coo] Org chart: 12-month hiring plan drafted
  [vp-sales] Sales strategy: ICP and pipeline model complete
  [general-counsel] Legal: Entity recommendation and compliance checklist ready
[Phase 2/6] Specialist Deep-Dives -- Complete
```

## Estimated Cost

With default model configuration: **approximately $80-150** for a complete business plan.

See `cost-analysis.md` for detailed breakdowns and alternative configurations.

## Directory Structure

```
teams/c-suite/
  README.md                     -- This file
  TEAM_SPEC.md                  -- Detailed architecture and specification
  MODEL_CONFIGS.md              -- Model selection and cost comparison
  CONFIG.md                     -- Project configuration template
  ORCHESTRATION.md              -- Multi-agent orchestration protocol
  cost-analysis.md              -- Token budget and cost analysis
  deployment-guide.md           -- Step-by-step setup instructions
  agents/
    ceo/AGENTS.md               -- CEO / Strategy Lead agent spec
    cfo/AGENTS.md               -- CFO / Finance agent spec
    cmo/AGENTS.md               -- CMO / Marketing agent spec
    cto/AGENTS.md               -- CTO / Product agent spec
    coo/AGENTS.md               -- COO / Operations agent spec
    vp-sales/AGENTS.md          -- VP Sales agent spec
    general-counsel/AGENTS.md   -- General Counsel agent spec
  mcp-servers/
    README.md                   -- MCP server setup guide
    google-sheets.json          -- Google Sheets MCP server config
    notion.json                 -- Notion MCP server config
  scenarios/
    business-plan-creation.md   -- Full business plan scenario
    financial-modeling.md       -- Financial modeling scenario
    pitch-deck-development.md   -- Pitch deck scenario
    market-entry-strategy.md    -- Market entry scenario
  examples/
    saas-startup.md             -- SaaS startup example
    marketplace-business.md     -- Marketplace example
    consulting-agency.md        -- Consulting agency example
```

## Key Design Principles

1. **Executable artifacts, not just advice.** Every output is designed to be acted upon by other agent teams or tools. The financial model feeds real tracking. The roadmap feeds real sprints.
2. **Cross-functional alignment by default.** The CEO synthesis phase ensures marketing budgets match financial projections, hiring plans match growth targets, and legal structures support the business model.
3. **Conflict resolution is a feature.** When the CMO wants a $500K marketing budget and the CFO says runway only supports $200K, the CEO facilitates a resolution. This mirrors how real executive teams operate.
4. **Progressive depth.** Start with a vision, then deep-dive in parallel, then integrate. Users can stop at any phase and get useful output.
5. **Cost awareness.** Every phase has a token budget. Users know costs before committing to the next phase.

## Cross-Team Integration

This team's outputs feed directly into other Agent Foundry teams:

| Output | Target Team | Input |
|--------|------------|-------|
| Product Roadmap (Linear) | Code Implementation | Feature requirements |
| Product Roadmap | Web App Development | Feature requirements |
| Marketing Plan | Content Creation | Content briefs and calendar |
| GTM Strategy | Sales & Marketing | Campaign briefs |
| Hiring Plan | Recruitment & HR | Role definitions |

## Related Documentation

- [TEAM_SPEC.md](TEAM_SPEC.md) -- Full architecture specification
- [ORCHESTRATION.md](ORCHESTRATION.md) -- Phase-by-phase execution protocol
- [deployment-guide.md](deployment-guide.md) -- How to set up and run
- [cost-analysis.md](cost-analysis.md) -- Budget planning
