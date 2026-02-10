# Example: SaaS Starter — Project Management Tool

## Project Overview

Build "TaskForge" — a project management SaaS for small teams (5-20 people). Features: task boards, team collaboration, file attachments, and tiered subscription plans.

## Configuration

```yaml
project_type: saas
target_audience: b2b
auth_strategy: oauth_only  # Google + GitHub OAuth
payment_model: subscription  # Free / Pro $12/mo / Team $29/mo
deployment_region: us_east
stack:
  frontend_framework: nextjs
  backend: supabase
  hosting: vercel
  database: supabase_postgres
  auth_provider: supabase_auth
  payment_provider: stripe
```

## Phase 1: Foundation (~30 min)

### Coordinator
- Decides on data model: Workspaces → Projects → Tasks → Comments
- Selects App Router with Server Components for data-heavy views
- Sets file structure conventions and naming patterns

### Cloud/DevOps
- Creates Supabase project, configures Auth providers (Google, GitHub)
- Sets up Vercel project linked to GitHub repo
- Creates GitHub Actions pipeline: lint → test → deploy

### Database Engineer
- Designs schema: `workspaces`, `projects`, `tasks`, `comments`, `workspace_members`
- Creates initial migration with foreign keys and indexes
- Sets up RLS: users can only see workspaces they belong to

### Senior Full-Stack
- Scaffolds Next.js 15 with TypeScript, Tailwind, App Router
- Creates layout structure: `(auth)`, `(dashboard)`, `(marketing)`
- Implements auth callback route and session middleware

## Phase 2: Core Features (~60 min)

### Senior Full-Stack
- Builds dashboard: workspace selector, project list, task board (Kanban)
- Implements Server Actions for task CRUD
- Adds real-time task updates via Supabase Realtime subscriptions
- User settings page with profile management

### Database Engineer
- Implements RLS policies for multi-workspace isolation
- Creates Edge Functions for invitation emails and workspace creation
- Adds database triggers for `updated_at` timestamps and activity logging

### Marketing Frontend
- Builds landing page: hero section, feature grid, pricing table, FAQ, footer
- Optimizes for Core Web Vitals (LCP < 2.5s, CLS < 0.1)
- Implements SEO: meta tags, Open Graph, sitemap.xml, robots.txt
- Adds Vercel Analytics and conversion tracking

### QA/Test
- Sets up Playwright with test fixtures (seed data, test users)
- Writes auth flow tests (OAuth mock, session persistence)
- Creates task CRUD test suite

## Phase 3: Integration & Revenue (~45 min)

### Senior Full-Stack
- Builds pricing page with plan comparison and upgrade CTA
- Implements Stripe checkout redirect from dashboard
- Adds subscription status badges and feature gates

### RevOps
- Creates Stripe products: Free, Pro ($12/mo), Team ($29/mo)
- Configures subscription webhooks (created, updated, canceled, payment_failed)
- Sets up customer billing portal for self-service management
- Implements trial: 14-day Pro trial on signup

### Database Engineer
- Creates `subscriptions` and `payment_events` tables
- Implements webhook handler that syncs Stripe → Supabase
- Adds feature flag queries based on subscription tier

### Cloud/DevOps
- Configures webhook endpoint with Stripe signature verification
- Sets environment variables across Vercel environments
- Adds Sentry for error tracking

### Marketing Frontend
- Integrates pricing page with live Stripe prices
- Adds conversion tracking for plan selection clicks

## Phase 4: Launch Prep (~30 min)

### QA/Test
- Full E2E suite: signup → create workspace → add task → upgrade → verify Pro features
- Payment flow test with Stripe test cards
- Load test: 100 concurrent users creating tasks
- Accessibility audit (WCAG 2.1 AA)

### RevOps
- Verifies all webhook events process correctly
- Tests trial → paid conversion flow
- Sets up MRR dashboard and payment failure alerts

### Cloud/DevOps
- Configures production environment variables
- Sets up Vercel deployment protection (preview + production)
- Creates runbook for common issues

### Coordinator
- Final architecture review
- Creates rollback plan (Vercel instant rollback + Supabase migration revert)
- Publishes launch checklist

## Deliverables Produced

1. **Marketing site** at `taskforge.com` — landing, pricing, blog placeholder
2. **Web app** at `app.taskforge.com` — dashboard, task boards, settings
3. **Database** — 8 tables, full RLS, 3 Edge Functions
4. **CI/CD** — GitHub Actions with Playwright tests, auto-deploy on merge
5. **Payments** — 3 Stripe plans, webhooks, billing portal, 14-day trial
6. **Monitoring** — Sentry errors, Vercel analytics, payment alerts

## Cost Summary

| Phase | Cost |
|-------|------|
| Foundation | $20 |
| Core Features | $40 |
| Integration & Revenue | $30 |
| Launch Prep | $15 |
| **Total** | **~$105** |
