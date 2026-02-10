# Sales & Marketing Team Template

A 7-agent team for complete go-to-market execution, from strategy through pipeline building, customer acquisition, retention, and growth analytics. Built for B2B and B2C companies that need a systematic, data-driven approach to revenue generation.

## Quick Start

```bash
# 1. Clone and configure
cp CONFIG.md my-config.md
# Edit my-config.md with your business context

# 2. Initialize the team
claude-code team init --config my-config.md

# 3. Run full GTM execution
claude-code team run --phases all

# 4. Or run a specific phase
claude-code team run --phase strategy
claude-code team run --phase pipeline-building
claude-code team run --phase execution
claude-code team run --phase analysis
```

## When to Use This Template

This template is designed for teams that need to:

- **Launch a new product or feature** and need a complete GTM strategy, demand generation plan, sales enablement kit, and customer success playbooks
- **Scale an existing go-to-market motion** by systematizing what works and building repeatable processes across channels
- **Reduce customer acquisition cost (CAC)** through better attribution, channel optimization, and conversion rate improvements
- **Improve pipeline health** with proper CRM hygiene, stage definitions, deal velocity tracking, and forecast accuracy
- **Decrease churn and increase expansion** through structured onboarding, health scoring, and proactive intervention workflows
- **Build a data-driven marketing organization** with proper attribution models, cohort analysis, and experiment frameworks

## What This Team Produces

### Phase 1: Strategy & Foundation
- Go-to-market strategy document with target personas, positioning, and competitive differentiation
- Core messaging framework with value propositions, messaging hierarchy, and proof points
- Analytics foundation with attribution model design and KPI definitions

### Phase 2: Pipeline Building
- Demand generation campaigns across paid, organic, and direct channels
- Complete sales enablement kit: pitch decks, battle cards, demo scripts, ROI calculators
- CRM infrastructure with stage definitions, scoring models, and automated workflows
- Customer onboarding sequences, health scoring model, and expansion triggers

### Phase 3: Execution & Optimization
- Live campaign management with budget allocation and performance monitoring
- Sales training materials with objection handling guides and competitive positioning
- Pipeline review cadences with forecast methodology and stuck-deal coaching
- Customer journey maps with expansion playbooks and QBR templates
- Analytics dashboards with experiment tracking and channel performance views

### Phase 4: Analysis & Iteration
- Campaign performance analysis with attribution-weighted ROI by channel
- Budget reallocation recommendations based on marginal CAC analysis
- Updated playbooks incorporating learnings from execution phase
- Strategic recommendations for next planning cycle

## Team Composition

| Agent | Model | Role |
|-------|-------|------|
| Coordinator / VP Marketing | Opus 4.6 | GTM strategy, team orchestration, campaign planning |
| Demand Generation Specialist | Sonnet 4.5 | Lead gen, paid ads, SEO/SEM, conversion optimization |
| Sales Enablement Manager | Sonnet 4.5 | Pitch decks, battle cards, demo scripts, ROI calculators |
| Pipeline Manager | Sonnet 4.5 | CRM hygiene, stage definitions, deal velocity, forecasting |
| Customer Success Manager | Sonnet 4.5 | Onboarding, health scoring, expansion/upsell, churn prevention |
| Growth Analyst | Sonnet 4.5 | Attribution models, cohort analysis, A/B tests, CAC/LTV |
| Brand & Messaging Specialist | Haiku 4.5 | Positioning, value props, messaging hierarchy, brand voice |

## Cost Estimate

| Configuration | Estimated Cost | Duration |
|--------------|---------------|----------|
| Default | ~$93 | ~2.5 hours |
| Budget | ~$45 | ~2 hours |
| Premium | ~$160 | ~3 hours |

See [cost-analysis.md](cost-analysis.md) for detailed breakdowns.

## Directory Structure

```
teams/sales-marketing/
├── README.md                          # This file
├── TEAM_SPEC.md                       # Detailed team architecture
├── MODEL_CONFIGS.md                   # Model selection and configurations
├── CONFIG.md                          # Team configuration template
├── ORCHESTRATION.md                   # Phase execution and coordination
├── cost-analysis.md                   # Token usage and cost estimates
├── deployment-guide.md                # Setup and deployment instructions
├── agents/
│   ├── coordinator/AGENTS.md          # VP Marketing / Coordinator
│   ├── demand-generation/AGENTS.md    # Demand Generation Specialist
│   ├── sales-enablement/AGENTS.md     # Sales Enablement Manager
│   ├── pipeline-manager/AGENTS.md     # Pipeline Manager
│   ├── customer-success/AGENTS.md     # Customer Success Manager
│   ├── growth-analyst/AGENTS.md       # Growth Analyst
│   └── brand-messaging/AGENTS.md      # Brand & Messaging Specialist
├── mcp-servers/
│   ├── README.md                      # MCP server setup guide
│   ├── hubspot.json                   # HubSpot CRM integration
│   ├── google-ads.json                # Google Ads integration
│   └── linkedin-ads.json             # LinkedIn Ads integration
├── scenarios/
│   ├── lead-to-customer.md            # Full funnel conversion scenario
│   ├── campaign-optimization.md       # Multi-channel optimization scenario
│   └── churn-prevention.md            # Churn detection and prevention
└── examples/
    ├── b2b-saas-gtm.md               # B2B SaaS go-to-market example
    ├── product-led-growth.md          # PLG motion example
    └── enterprise-sales.md            # Enterprise sales example
```

## Prerequisites

- Claude Code CLI with multi-agent support
- MCP server access for CRM and ad platform integrations (optional but recommended)
- Access to your company's existing marketing data, CRM, and analytics platforms
- Business context: target market, product details, competitive landscape, pricing

## Related Templates

- **Content Production Team** - For content-heavy marketing strategies
- **Product Development Team** - For product-led growth motions where product and marketing are tightly coupled
- **Data Engineering Team** - For building the data infrastructure that powers marketing analytics
