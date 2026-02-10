# Web App Development Team -- Technical Specification

## Overview

This document defines the architecture, agent composition, responsibilities, deliverables, and quality standards for the Web App Development Team. The team is designed to produce a complete, launch-ready SaaS application from a single project brief.

---

## 1. Team Composition

The team consists of 7 specialized agents. Two operate on Opus 4.6 for tasks requiring deep architectural reasoning. Five operate on Sonnet 4.5 for high-throughput execution tasks.

### 1.1 Coordinator / Tech Lead

- **Model:** Opus 4.6
- **Token budget:** ~150K tokens
- **Primary responsibilities:**
  - Receive and decompose the project brief into actionable work items
  - Make architecture decisions (monorepo vs polyrepo, routing strategy, state management)
  - Assign tasks to agents with clear acceptance criteria
  - Run quality gates between phases
  - Resolve conflicts between agents (e.g., schema disagreements, API contract mismatches)
  - Maintain the decision log with rationale for every non-trivial choice
  - Own the launch checklist and rollback plan
- **Decision authority:**
  - FINAL say on architecture, tech stack overrides, and scope
  - Can veto any agent's output that violates project constraints
  - Escalates to user only for: budget overruns, missing requirements, ambiguous business logic
- **Outputs:**
  - `ARCHITECTURE.md` -- System architecture decisions
  - `DECISIONS.md` -- Decision log with rationale
  - `LAUNCH_CHECKLIST.md` -- Pre-launch verification list
  - Phase gate reports (pass/fail with details)

### 1.2 Senior Full-Stack Developer

- **Model:** Opus 4.6
- **Token budget:** ~200K tokens
- **Primary responsibilities:**
  - Scaffold the Next.js 15 application with App Router
  - Implement authenticated application features (dashboard, settings, CRUD views)
  - Build API routes (Route Handlers) with proper validation and error handling
  - Create reusable React 19 component library with TypeScript
  - Integrate Supabase client (auth, database, storage, realtime)
  - Implement Stripe checkout UI, billing portal redirect, subscription status display
  - Apply responsive design with Tailwind CSS
  - Write inline documentation and JSDoc comments
- **Technical standards:**
  - All components are React Server Components by default; Client Components only when necessary
  - Server Actions for mutations; Route Handlers for webhooks and external API consumption
  - Zod schemas for all input validation
  - Proper error boundaries at route segment level
  - Loading and error states for every async operation
- **Outputs:**
  - `/app` directory with route segments
  - `/components` directory with shared UI components
  - `/lib` directory with utilities, Supabase client, Stripe helpers
  - `/types` directory with TypeScript type definitions

### 1.3 Cloud / DevOps Engineer

- **Model:** Sonnet 4.5
- **Token budget:** ~120K tokens
- **Primary responsibilities:**
  - Initialize Supabase project (via CLI or MCP)
  - Configure Vercel project with proper build settings
  - Set up GitHub repository with branch protection rules
  - Create GitHub Actions workflows (CI on PR, CD on merge to main)
  - Manage environment variables and secrets across all environments
  - Configure custom domain and DNS (if provided)
  - Set up Sentry project and integrate error tracking
  - Configure Vercel Analytics
  - Create infrastructure-as-code where applicable
  - Document the deployment architecture
- **Security standards:**
  - Secrets are NEVER committed to the repository
  - All secrets go into GitHub Secrets, Vercel Environment Variables, or Supabase Vault
  - Preview deployments use test/staging credentials
  - Production deployment requires passing CI and coordinator approval
- **Outputs:**
  - `.github/workflows/ci.yml` -- CI pipeline
  - `.github/workflows/cd.yml` -- CD pipeline
  - `vercel.json` -- Vercel configuration
  - `.env.example` -- Environment variable template (no real values)
  - `INFRASTRUCTURE.md` -- Deployment architecture documentation

### 1.4 Marketing Frontend Developer

- **Model:** Sonnet 4.5
- **Token budget:** ~120K tokens
- **Primary responsibilities:**
  - Build the marketing landing page with hero, features, social proof, CTA
  - Build the pricing page with plan comparison and Stripe integration points
  - Implement SEO fundamentals (meta tags, Open Graph, structured data, sitemap, robots.txt)
  - Optimize for Core Web Vitals (LCP < 2.5s, FID < 100ms, CLS < 0.1)
  - Set up conversion tracking (signup funnel, pricing page visits, CTA clicks)
  - Create responsive layouts that work on mobile, tablet, and desktop
  - Implement cookie consent banner (if required by region)
  - Build blog/changelog infrastructure (optional, if in scope)
- **Design standards:**
  - Mobile-first responsive design
  - Semantic HTML for accessibility (WCAG 2.1 AA)
  - No layout shift on page load
  - Images use `next/image` with proper sizing and lazy loading
  - Above-the-fold content renders without JavaScript
- **Outputs:**
  - `/app/(marketing)/page.tsx` -- Landing page
  - `/app/(marketing)/pricing/page.tsx` -- Pricing page
  - `/app/(marketing)/layout.tsx` -- Marketing layout
  - `/app/sitemap.ts` -- Dynamic sitemap
  - `/app/robots.ts` -- Robots configuration
  - Marketing-specific components

### 1.5 Database Engineer

- **Model:** Sonnet 4.5
- **Token budget:** ~150K tokens
- **Primary responsibilities:**
  - Design the Postgres schema based on the project brief and coordinator's architecture
  - Write numbered migration files (`001_initial_schema.sql`, `002_add_subscriptions.sql`, etc.)
  - Implement Row Level Security (RLS) policies on every table
  - Create database functions and triggers (e.g., `handle_new_user`, `update_updated_at`)
  - Design and create indexes for common query patterns
  - Write Supabase Edge Functions for server-side logic
  - Set up Supabase Storage buckets with access policies
  - Configure Supabase Realtime subscriptions (if needed)
  - Create seed data scripts for development and testing
  - Document the data model with an Entity Relationship diagram
- **Data integrity standards:**
  - Every table has `id` (UUID, PK), `created_at`, `updated_at`
  - Foreign keys with appropriate CASCADE/RESTRICT behavior
  - RLS enabled on ALL tables, no exceptions
  - RLS policies follow principle of least privilege
  - Migrations are idempotent and reversible where possible
  - No raw SQL in application code; use Supabase client or typed queries
- **Outputs:**
  - `/supabase/migrations/` -- Numbered migration files
  - `/supabase/seed.sql` -- Seed data
  - `/supabase/functions/` -- Edge functions
  - `DATABASE.md` -- Schema documentation and ER diagram

### 1.6 Revenue Operations (RevOps) Specialist

- **Model:** Sonnet 4.5
- **Token budget:** ~130K tokens
- **Primary responsibilities:**
  - Configure Stripe products and prices (monthly/annual, tiers, usage-based if applicable)
  - Implement Stripe Checkout Sessions for subscription creation
  - Build the Stripe Customer Portal integration for self-service billing management
  - Create webhook handler for Stripe events:
    - `checkout.session.completed` -- Activate subscription
    - `customer.subscription.updated` -- Handle plan changes
    - `customer.subscription.deleted` -- Handle cancellation
    - `invoice.payment_succeeded` -- Record successful payment
    - `invoice.payment_failed` -- Trigger dunning flow
    - `customer.subscription.trial_will_end` -- Send trial ending notification
  - Implement dunning strategy (retry schedule, grace period, downgrade logic)
  - Set up MRR/ARR tracking queries
  - Configure Stripe billing portal appearance and behavior
  - Implement subscription status sync between Stripe and Supabase
  - Set up cost monitoring and budget alerts for infrastructure spend
  - Create revenue dashboard data (MRR, churn, LTV estimates)
- **Revenue standards:**
  - Webhook handlers are idempotent (safe to replay)
  - Subscription state is always derived from Stripe as source of truth
  - Database subscription records are synced, not authoritative
  - All monetary values stored in cents (integers, never floats)
  - Webhook signature verification on every request
  - Test mode used for all development and staging
- **Outputs:**
  - `/app/api/webhooks/stripe/route.ts` -- Webhook handler
  - `/lib/stripe.ts` -- Stripe client and helpers
  - `/lib/subscription.ts` -- Subscription management logic
  - Stripe product/price configuration documentation
  - Dunning flow documentation
  - MRR tracking queries

### 1.7 QA / Test Engineer

- **Model:** Sonnet 4.5
- **Token budget:** ~130K tokens
- **Primary responsibilities:**
  - Set up Playwright for E2E testing
  - Write E2E tests for critical user flows:
    - Signup and login (email, OAuth)
    - Core CRUD operations
    - Payment checkout and subscription management
    - Settings and profile management
  - Create CI quality gates:
    - TypeScript type checking (`tsc --noEmit`)
    - Linting (`eslint`)
    - Unit tests (`vitest`)
    - E2E tests (`playwright`)
    - Build verification (`next build`)
    - Bundle size check
  - Set up test data factories and fixtures
  - Implement visual regression testing baseline (optional)
  - Create load testing scripts for critical endpoints
  - Write test documentation and coverage reports
- **Testing standards:**
  - E2E tests cover every critical user journey
  - Tests are deterministic (no flaky tests accepted)
  - Test data is isolated (no cross-test contamination)
  - Payment tests use Stripe test mode with test card numbers
  - CI must pass before any merge to main
  - Test failures block deployment
- **Outputs:**
  - `/tests/e2e/` -- Playwright E2E tests
  - `/tests/unit/` -- Vitest unit tests
  - `/tests/fixtures/` -- Test data and factories
  - `playwright.config.ts` -- Playwright configuration
  - `vitest.config.ts` -- Vitest configuration
  - CI quality gate configuration

---

## 2. Tech Stack Specification

### 2.1 Core Stack

| Component | Technology | Version | Purpose |
|-----------|-----------|---------|---------|
| Framework | Next.js | 15.x | Full-stack React framework |
| UI Library | React | 19.x | Component rendering |
| Language | TypeScript | 5.x | Type safety |
| Styling | Tailwind CSS | 4.x | Utility-first CSS |
| Database | PostgreSQL | 15.x | Primary data store (via Supabase) |
| Auth | Supabase Auth | Latest | Authentication and authorization |
| Edge Functions | Supabase Functions | Latest | Server-side logic (Deno runtime) |
| Storage | Supabase Storage | Latest | File and asset storage |
| Real-time | Supabase Realtime | Latest | Live data subscriptions |
| Payments | Stripe | Latest API | Billing and subscriptions |
| Hosting | Vercel | Latest | Edge deployment |
| CI/CD | GitHub Actions | Latest | Automation pipelines |
| Error Tracking | Sentry | Latest | Runtime error monitoring |
| Analytics | Vercel Analytics | Latest | Performance and usage analytics |

### 2.2 Development Dependencies

| Tool | Purpose |
|------|---------|
| ESLint | Code linting |
| Prettier | Code formatting |
| Vitest | Unit testing |
| Playwright | E2E testing |
| Zod | Runtime schema validation |
| Supabase CLI | Local development and migrations |
| Stripe CLI | Webhook testing |

### 2.3 Project Structure

```
project-root/
  app/
    (marketing)/           -- Marketing pages (public)
      page.tsx             -- Landing page
      pricing/page.tsx     -- Pricing page
      layout.tsx           -- Marketing layout
    (auth)/                -- Auth pages
      login/page.tsx
      signup/page.tsx
      callback/route.ts    -- OAuth callback
    (app)/                 -- Authenticated app pages
      dashboard/page.tsx
      settings/page.tsx
      layout.tsx           -- App layout with sidebar
    api/
      webhooks/
        stripe/route.ts    -- Stripe webhook handler
    layout.tsx             -- Root layout
    sitemap.ts
    robots.ts
  components/
    ui/                    -- Base UI components (Button, Input, Card, etc.)
    marketing/             -- Marketing-specific components
    app/                   -- App-specific components
  lib/
    supabase/
      client.ts            -- Browser Supabase client
      server.ts            -- Server Supabase client
      middleware.ts         -- Auth middleware helper
    stripe.ts              -- Stripe client and helpers
    subscription.ts        -- Subscription management
    utils.ts               -- General utilities
  types/
    database.ts            -- Generated Supabase types
    stripe.ts              -- Stripe-related types
  supabase/
    migrations/            -- SQL migration files
    seed.sql               -- Development seed data
    functions/             -- Edge functions
    config.toml            -- Supabase local config
  tests/
    e2e/                   -- Playwright E2E tests
    unit/                  -- Vitest unit tests
    fixtures/              -- Test data
  .github/
    workflows/
      ci.yml               -- CI pipeline
      cd.yml               -- CD pipeline
  public/                  -- Static assets
  middleware.ts            -- Next.js middleware (auth check)
  next.config.ts           -- Next.js configuration
  tailwind.config.ts       -- Tailwind configuration
  tsconfig.json            -- TypeScript configuration
  package.json
  .env.example
  .env.local               -- Local env vars (gitignored)
```

---

## 3. Deliverables

### 3.1 Marketing Website

| Deliverable | Description | Owner |
|------------|-------------|-------|
| Landing page | Hero, features, social proof, CTA sections | Marketing Frontend |
| Pricing page | Plan comparison table, Stripe checkout links | Marketing Frontend + RevOps |
| SEO setup | Meta tags, OG images, structured data, sitemap | Marketing Frontend |
| Analytics | Conversion tracking, funnel analytics | Marketing Frontend + Cloud/DevOps |

### 3.2 Web Application

| Deliverable | Description | Owner |
|------------|-------------|-------|
| Auth flows | Login, signup, OAuth, password reset, email verification | Senior Full-Stack |
| Dashboard | Main app view with data display | Senior Full-Stack |
| CRUD features | Create, read, update, delete for core entities | Senior Full-Stack + Database Engineer |
| Settings | User profile, account settings, billing management | Senior Full-Stack + RevOps |
| Real-time features | Live data updates where applicable | Senior Full-Stack + Database Engineer |

### 3.3 Backend Infrastructure

| Deliverable | Description | Owner |
|------------|-------------|-------|
| Database schema | Tables, relationships, indexes, RLS | Database Engineer |
| Migrations | Versioned, reversible schema changes | Database Engineer |
| Edge functions | Server-side business logic | Database Engineer |
| Auth configuration | Providers, redirect URLs, email templates | Cloud/DevOps + Database Engineer |
| Storage buckets | File upload with access policies | Database Engineer |

### 3.4 Revenue Infrastructure

| Deliverable | Description | Owner |
|------------|-------------|-------|
| Stripe products/prices | Configured in Stripe Dashboard or via API | RevOps |
| Checkout flow | Stripe Checkout Sessions | RevOps + Senior Full-Stack |
| Billing portal | Self-service subscription management | RevOps |
| Webhook handlers | Event processing and state sync | RevOps + Database Engineer |
| Dunning flow | Payment failure retry and grace period | RevOps |
| MRR tracking | Revenue metrics queries | RevOps |

### 3.5 Deployment Pipeline

| Deliverable | Description | Owner |
|------------|-------------|-------|
| CI pipeline | Type check, lint, test, build on every PR | Cloud/DevOps + QA/Test |
| CD pipeline | Auto-deploy to Vercel on merge to main | Cloud/DevOps |
| Preview deployments | Per-PR preview URLs | Cloud/DevOps |
| Environment management | Staging and production env vars | Cloud/DevOps |
| Rollback plan | Documented rollback procedure | Cloud/DevOps + Coordinator |

### 3.6 Monitoring and Observability

| Deliverable | Description | Owner |
|------------|-------------|-------|
| Error tracking | Sentry integration with source maps | Cloud/DevOps |
| Performance analytics | Vercel Analytics and Web Vitals | Cloud/DevOps + Marketing Frontend |
| Cost monitoring | Infrastructure spend tracking and alerts | RevOps + Cloud/DevOps |
| Uptime monitoring | Health check endpoints | Cloud/DevOps |

### 3.7 Documentation

| Deliverable | Description | Owner |
|------------|-------------|-------|
| Architecture doc | System design and decisions | Coordinator |
| API documentation | Route handlers and their contracts | Senior Full-Stack |
| Database documentation | Schema, ER diagram, RLS policies | Database Engineer |
| Deployment docs | How to deploy, configure, rollback | Cloud/DevOps |
| Revenue docs | Stripe config, webhook events, dunning flow | RevOps |

---

## 4. Token Budget

### 4.1 Budget by Agent

| Agent | Model | Est. Tokens | Est. Cost |
|-------|-------|-------------|-----------|
| Coordinator / Tech Lead | Opus 4.6 | ~150K | ~$22.50 |
| Senior Full-Stack Developer | Opus 4.6 | ~200K | ~$30.00 |
| Cloud / DevOps Engineer | Sonnet 4.5 | ~120K | ~$7.20 |
| Marketing Frontend Developer | Sonnet 4.5 | ~120K | ~$7.20 |
| Database Engineer | Sonnet 4.5 | ~150K | ~$9.00 |
| RevOps Specialist | Sonnet 4.5 | ~130K | ~$7.80 |
| QA / Test Engineer | Sonnet 4.5 | ~130K | ~$7.80 |
| **Total** | | **~1,000K** | **~$91.50** |

Note: Estimates include ~15% buffer for retries and quality gate iterations, bringing the effective total to approximately $105.

### 4.2 Budget by Phase

| Phase | Duration | Agents | Tokens | Cost |
|-------|----------|--------|--------|------|
| Foundation | ~30 min | 4 | ~200K | ~$20 |
| Core Features | ~60 min | 4 | ~400K | ~$40 |
| Integration & Revenue | ~45 min | 5 | ~300K | ~$30 |
| Launch Prep | ~30 min | 5 | ~150K | ~$15 |
| **Total** | **~2.75 hrs** | | **~1,050K** | **~$105** |

---

## 5. Quality Standards

### 5.1 Code Quality

- TypeScript strict mode enabled, zero `any` types without explicit justification
- ESLint with Next.js recommended rules, zero warnings
- Prettier formatting enforced
- No console.log in production code (use structured logging)
- All async operations have error handling
- All user inputs validated with Zod

### 5.2 Security

- RLS enabled on every Supabase table
- Auth middleware on every protected route
- CSRF protection on all mutations
- Stripe webhook signature verification
- Environment variables for all secrets
- Content Security Policy headers
- Rate limiting on auth and API endpoints

### 5.3 Performance

- Lighthouse score >= 90 on all marketing pages
- LCP < 2.5 seconds
- FID < 100 milliseconds
- CLS < 0.1
- Bundle size monitored and budgeted
- Images optimized with next/image
- Fonts optimized with next/font

### 5.4 Testing

- E2E tests for every critical user journey
- Unit tests for business logic and utilities
- All tests pass in CI before merge
- No flaky tests (deterministic, isolated)
- Payment flow tests use Stripe test mode

### 5.5 Documentation

- Every non-obvious architecture decision documented with rationale
- API routes documented with request/response examples
- Database schema documented with descriptions
- Deployment and rollback procedures documented
- Revenue flow documented end-to-end
