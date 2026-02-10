# Web App Development Team

A 7-agent team template for building production-ready, full-stack SaaS applications using Next.js 15, Supabase, Vercel, and Stripe.

## What This Team Builds

This team delivers a complete, launch-ready SaaS product in approximately 2.75 hours of agent execution time:

- **Marketing website** -- Landing page, pricing page, SEO-optimized, conversion-tracked, Core Web Vitals compliant
- **Web application** -- Authenticated dashboard, CRUD features, real-time updates, responsive UI
- **Backend infrastructure** -- Postgres database with Row Level Security, edge functions, storage, auth
- **Revenue infrastructure** -- Stripe products, prices, subscriptions, billing portal, dunning, webhook handlers, MRR tracking
- **Deployment pipeline** -- GitHub Actions CI/CD, Vercel preview/production deployments, rollback capability
- **Monitoring and observability** -- Sentry error tracking, Vercel analytics, cost monitoring alerts

## When to Use This Template

Use this team when you need to:

- Launch a new SaaS product from scratch
- Build a marketplace with user accounts and payments
- Create a content platform with subscriptions
- Develop an internal tool with authentication and RBAC
- Prototype a full-stack app with production-grade infrastructure

Do **not** use this team for:

- Static websites with no backend (use a simpler template)
- Mobile-first apps (this is web-focused)
- ML/AI model training pipelines (different infrastructure needs)
- Legacy system migrations (requires different agent specializations)

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend Framework | Next.js 15 (App Router) |
| UI Library | React 19 |
| Language | TypeScript (strict mode) |
| Styling | Tailwind CSS v4 |
| Database | Supabase Postgres |
| Auth | Supabase Auth |
| Edge Functions | Supabase Edge Functions (Deno) |
| Storage | Supabase Storage |
| Real-time | Supabase Realtime |
| Payments | Stripe |
| Hosting | Vercel |
| CI/CD | GitHub Actions |
| Error Tracking | Sentry |
| Analytics | Vercel Analytics |

## Quick Start

### 1. Prerequisites

Ensure you have accounts and API keys for:
- GitHub (repository hosting)
- Supabase (database and auth)
- Vercel (hosting)
- Stripe (payments)

### 2. Configure the Team

Copy and edit the configuration file:

```bash
cp CONFIG.md CONFIG.local.md
# Edit CONFIG.local.md with your project settings
```

Set the required environment variables:

```bash
export SUPABASE_ACCESS_TOKEN="your-supabase-access-token"
export VERCEL_TOKEN="your-vercel-token"
export STRIPE_SECRET_KEY="sk_test_..."
export STRIPE_WEBHOOK_SECRET="whsec_..."
export GITHUB_TOKEN="ghp_..."
export SENTRY_DSN="https://...@sentry.io/..."
```

### 3. Run the Team

Execute in sequential mode (recommended for first run):

```bash
claude-agent team run ./teams/web-app-development \
  --config CONFIG.local.md \
  --mode sequential
```

Or in hybrid mode for faster execution:

```bash
claude-agent team run ./teams/web-app-development \
  --config CONFIG.local.md \
  --mode hybrid
```

### 4. Monitor Progress

The coordinator agent logs phase transitions and quality gate results. Watch the output for:

```
[Phase 1/4] Foundation -- Starting...
  [coordinator] Architecture decisions locked
  [cloud-devops] Supabase project initialized
  [database-engineer] Schema v001 applied
  [senior-fullstack] Next.js scaffold ready
[Phase 1/4] Foundation -- Complete (all gates passed)
```

## Team Composition

| Agent | Model | Role |
|-------|-------|------|
| Coordinator / Tech Lead | Opus 4.6 | Architecture, task decomposition, quality gates, conflict resolution |
| Senior Full-Stack Developer | Opus 4.6 | App features, API routes, Next.js patterns, component architecture |
| Cloud / DevOps Engineer | Sonnet 4.5 | Supabase init, Vercel setup, GitHub Actions, IaC, secrets |
| Marketing Frontend Developer | Sonnet 4.5 | Landing page, SEO, Core Web Vitals, conversion optimization |
| Database Engineer | Sonnet 4.5 | Postgres schema, RLS policies, migrations, edge functions, indexes |
| RevOps Specialist | Sonnet 4.5 | Stripe setup, subscription lifecycle, billing portal, dunning, MRR |
| QA / Test Engineer | Sonnet 4.5 | Playwright E2E, CI quality gates, load testing, test data |

## Estimated Cost

With default model configuration: **approximately $105** total across all phases.

See `cost-analysis.md` for detailed breakdowns and alternative configurations.

## Directory Structure

```
teams/web-app-development/
  README.md                    -- This file
  TEAM_SPEC.md                 -- Detailed architecture and specification
  MODEL_CONFIGS.md             -- Model selection and cost comparison
  CONFIG.md                    -- Project configuration template
  ORCHESTRATION.md             -- Multi-agent orchestration protocol
  cost-analysis.md             -- Token budget and cost analysis
  deployment-guide.md          -- Step-by-step deployment instructions
  agents/
    coordinator/AGENTS.md      -- Coordinator / Tech Lead agent spec
    senior-fullstack/AGENTS.md -- Senior Full-Stack Developer agent spec
    cloud-devops/AGENTS.md     -- Cloud / DevOps Engineer agent spec
    marketing-frontend/AGENTS.md -- Marketing Frontend Developer agent spec
    database-engineer/AGENTS.md  -- Database Engineer agent spec
    revops/AGENTS.md           -- Revenue Operations Specialist agent spec
    qa-test/AGENTS.md          -- QA / Test Engineer agent spec
  mcp-servers/
    README.md                  -- MCP server setup guide
    supabase.json              -- Supabase MCP server config
    vercel.json                -- Vercel MCP server config
    stripe.json                -- Stripe MCP server config
    github.json                -- GitHub MCP server config
  scenarios/
    auth-flow.md               -- Authentication flow scenario
    payment-flow.md            -- Payment and checkout scenario
    subscription-lifecycle.md  -- Full subscription lifecycle scenario
    data-crud.md               -- CRUD operations with RLS scenario
    deployment-rollback.md     -- Deployment failure and rollback scenario
  examples/
    saas-starter.md            -- SaaS starter app example
    marketplace-app.md         -- Marketplace app example
    internal-tool.md           -- Internal tool example
```

## Key Design Principles

1. **Boring technology wins.** Default to well-understood, battle-tested solutions. Exotic choices require explicit justification.
2. **Ship the MVP.** Every decision is filtered through "does this help us launch?" Scope creep is treated as a bug.
3. **Security by default.** RLS on every table. Auth on every route. Secrets in environment variables, never in code.
4. **Automated everything.** If a human has to remember to do it, automate it. CI/CD, migrations, deployments, monitoring.
5. **Cost awareness.** Every agent tracks token usage. Infrastructure costs are monitored from day one.

## Related Documentation

- [TEAM_SPEC.md](TEAM_SPEC.md) -- Full architecture specification
- [ORCHESTRATION.md](ORCHESTRATION.md) -- Phase-by-phase execution protocol
- [deployment-guide.md](deployment-guide.md) -- How to set up and run
- [cost-analysis.md](cost-analysis.md) -- Budget planning
