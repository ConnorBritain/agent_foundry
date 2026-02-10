# Multi-Agent Orchestration Protocol

This document defines the execution phases, communication protocols, quality gates, and decision-making framework for the Web App Development Team.

---

## Execution Modes

The team supports three execution modes. The mode is selected at runtime via the `--mode` flag.

### Sequential Mode

Agents execute one at a time in a defined order. Slowest but most predictable. Recommended for first-time users or debugging.

```
Coordinator → Cloud/DevOps → Database → Full-Stack → Marketing → RevOps → QA
```

**Total time:** ~5-6 hours
**When to use:** First run, debugging, when agent outputs depend heavily on each other.

### Hybrid Mode (Recommended)

Agents execute in parallel within phases but sequentially across phases. Quality gates between phases ensure coherence.

```
Phase 1 (parallel): Coordinator + Cloud/DevOps + Database + Full-Stack
  ↓ [Quality Gate 1]
Phase 2 (parallel): Full-Stack + Database + Marketing + QA
  ↓ [Quality Gate 2]
Phase 3 (parallel): Full-Stack + RevOps + Database + Cloud/DevOps + Marketing
  ↓ [Quality Gate 3]
Phase 4 (parallel): QA + RevOps + Cloud/DevOps + Marketing + Coordinator
  ↓ [Quality Gate 4 / Launch Decision]
```

**Total time:** ~2.75 hours
**When to use:** Standard development. Best balance of speed and reliability.

### Swarm Mode

All agents run concurrently with message-passing coordination. Fastest but requires robust conflict resolution. Experimental.

**Total time:** ~1.5-2 hours
**When to use:** Experienced users, projects with well-defined scope, when speed is critical.
**Warning:** Higher risk of conflicts and wasted tokens from retries.

---

## Phase Definitions

### Phase 1: Foundation (Parallel -- ~30 minutes)

**Goal:** Establish the project skeleton, infrastructure, and database schema so all agents have a shared foundation.

#### Coordinator / Tech Lead
- Parse project configuration and validate all settings
- Write `ARCHITECTURE.md` with:
  - System architecture diagram (text-based)
  - Route structure decision (route groups, layouts, middleware)
  - Data model overview (entities, relationships, access patterns)
  - API contract definitions (route handlers, request/response shapes)
  - Authentication flow decision
  - State management approach
- Write `DECISIONS.md` with initial decisions and rationale
- Produce task assignments for all agents with acceptance criteria
- Define the shared TypeScript types that other agents will consume

**Outputs:**
- `ARCHITECTURE.md`
- `DECISIONS.md`
- Task assignments (sent to all agents)
- `/types/shared.ts` (shared type definitions)

#### Cloud / DevOps Engineer
- Initialize GitHub repository with:
  - `.gitignore` (Next.js + Supabase + environment files)
  - Branch protection rules on `main`
  - Repository secrets for CI/CD
- Initialize Supabase project:
  - Create project via CLI or MCP
  - Configure auth providers per config
  - Set redirect URLs for auth callbacks
  - Record project URL and anon key
- Initialize Vercel project:
  - Link to GitHub repository
  - Configure build settings (`next build`)
  - Set environment variables for staging
  - Enable preview deployments
- Create GitHub Actions CI workflow (`.github/workflows/ci.yml`):
  - Trigger on pull request to `main`
  - Steps: checkout, install, typecheck, lint, test, build
- Create `.env.example` with all required variables (no values)

**Outputs:**
- GitHub repository (configured)
- Supabase project (configured)
- Vercel project (configured)
- `.github/workflows/ci.yml`
- `.env.example`

**Depends on:** Coordinator's auth and deployment decisions (available within first 5 minutes).

#### Database Engineer
- Design the initial Postgres schema based on coordinator's architecture:
  - `profiles` table (extends Supabase auth.users)
  - Core entity tables per project type
  - `subscriptions` table (synced with Stripe)
  - `prices` and `products` tables (synced with Stripe)
- Write migration `001_initial_schema.sql`:
  - Table definitions with proper types and constraints
  - Indexes on foreign keys and common query columns
  - `updated_at` trigger function
  - RLS policies (basic: users can read/write their own data)
- Write `seed.sql` with development test data
- Generate TypeScript types from schema (`/types/database.ts`)

**Outputs:**
- `/supabase/migrations/001_initial_schema.sql`
- `/supabase/seed.sql`
- `/types/database.ts`
- `DATABASE.md` (initial draft)

**Depends on:** Coordinator's data model overview.

#### Senior Full-Stack Developer
- Scaffold the Next.js 15 project:
  - `npx create-next-app@latest` with TypeScript, Tailwind, App Router
  - Configure `next.config.ts`
  - Configure `tsconfig.json` with strict mode
  - Configure Tailwind
- Set up the route structure:
  - `(marketing)` route group with layout
  - `(auth)` route group with layout
  - `(app)` route group with layout (authenticated)
- Create Supabase client utilities:
  - `/lib/supabase/client.ts` (browser client)
  - `/lib/supabase/server.ts` (server client)
  - `/lib/supabase/middleware.ts` (auth middleware)
- Create `middleware.ts` for auth protection
- Set up base UI components (`/components/ui/`):
  - Button, Input, Card, Badge, Avatar, Dialog, Dropdown
- Install and configure dependencies:
  - `@supabase/supabase-js`, `@supabase/ssr`
  - `stripe`, `@stripe/stripe-js`
  - `zod`
  - `@sentry/nextjs`

**Outputs:**
- Complete Next.js scaffold
- Route group structure
- Supabase client utilities
- Base UI component library
- `middleware.ts`
- `package.json` with all dependencies

**Depends on:** Coordinator's route structure and architecture decisions.

#### Quality Gate 1: Foundation Checkpoint

The Coordinator validates:

| Check | Criteria | Blocking |
|-------|----------|----------|
| Repository exists | GitHub repo accessible with correct branch protection | Yes |
| Supabase project live | Project URL responds, auth configured | Yes |
| Vercel project linked | Connected to GitHub, build settings correct | Yes |
| Schema valid | Migration applies without errors, RLS enabled | Yes |
| Next.js builds | `next build` succeeds | Yes |
| Types consistent | Database types match schema, shared types imported correctly | Yes |
| CI pipeline runs | GitHub Actions workflow triggers on PR | No (can fix in Phase 2) |
| Env vars documented | `.env.example` has all required variables | Yes |

**Pass criteria:** All blocking checks pass. Non-blocking issues logged for Phase 2.

---

### Phase 2: Core Features (Parallel -- ~60 minutes)

**Goal:** Build the core application features, marketing site, and test infrastructure.

#### Senior Full-Stack Developer
- Implement authentication flows:
  - Login page with OAuth buttons and/or email form
  - Signup page with same
  - OAuth callback handler (`/app/(auth)/callback/route.ts`)
  - Password reset flow (if email_password auth)
  - Email verification handling
- Build the authenticated dashboard:
  - Dashboard layout with sidebar navigation
  - Dashboard home page with summary/overview
  - Core CRUD views for primary entities:
    - List view with pagination, search, filters
    - Detail view
    - Create/edit forms with validation
    - Delete confirmation
  - Server Actions for all mutations
- Build user settings:
  - Profile editing (name, avatar)
  - Account settings
  - Notification preferences
- Implement error boundaries and loading states
- Add Sentry integration for error tracking

**Outputs:**
- Auth pages and callback handler
- Dashboard with CRUD views
- Settings pages
- Server Actions for mutations
- Error boundaries and loading states

**Depends on:** Phase 1 schema, Supabase client, route structure.

#### Database Engineer
- Write comprehensive RLS policies (migration `002_rls_policies.sql`):
  - SELECT policies: users see only their own data
  - INSERT policies: users can create records linked to their ID
  - UPDATE policies: users can update only their own records
  - DELETE policies: users can delete only their own records
  - Admin overrides where applicable
- Create database functions:
  - `handle_new_user()` trigger: creates profile on auth.users insert
  - `update_updated_at()` trigger: auto-updates timestamp
  - Any project-specific computed columns or views
- Create Supabase Edge Functions for server-side logic:
  - Any operations that need elevated privileges
  - Background processing tasks
- Set up Supabase Storage:
  - Create buckets (avatars, uploads)
  - Configure storage policies (authenticated users can upload to their folder)

**Outputs:**
- `/supabase/migrations/002_rls_policies.sql`
- `/supabase/migrations/003_functions_triggers.sql`
- `/supabase/functions/` (edge functions)
- Storage bucket configuration

**Depends on:** Phase 1 schema, coordinator's data model.

#### Marketing Frontend Developer
- Build the landing page (`/app/(marketing)/page.tsx`):
  - Hero section with headline, subheadline, CTA button
  - Features section (grid/bento layout)
  - Social proof section (testimonials, logos, metrics)
  - How-it-works section
  - Final CTA section
  - Footer with links
- Build the pricing page (`/app/(marketing)/pricing/page.tsx`):
  - Plan comparison cards
  - Feature comparison table
  - Monthly/annual toggle
  - CTA buttons (linked to checkout in Phase 3)
  - FAQ section
- Implement SEO:
  - Root `layout.tsx` metadata (title, description, OG tags)
  - Per-page metadata
  - `sitemap.ts` (dynamic sitemap generation)
  - `robots.ts` (robots configuration)
  - Structured data (JSON-LD for Organization, Product)
- Optimize Core Web Vitals:
  - Use `next/image` for all images
  - Use `next/font` for fonts
  - Minimize client-side JavaScript
  - Proper loading hierarchy (above-the-fold first)

**Outputs:**
- Landing page
- Pricing page
- Marketing layout and components
- SEO configuration (sitemap, robots, metadata)
- Open Graph image template

**Depends on:** Phase 1 Next.js scaffold, config subscription plans.

#### QA / Test Engineer
- Set up Playwright:
  - Install Playwright and browsers
  - Configure `playwright.config.ts` (base URL, retries, reporters)
  - Create test utilities and helpers
  - Create page object models for common pages
- Set up Vitest:
  - Install Vitest
  - Configure `vitest.config.ts` (TypeScript, path aliases)
  - Create test utilities
- Write initial E2E tests:
  - Auth flow: signup, login, logout, session persistence
  - Navigation: marketing pages load, app pages require auth
  - Dashboard: basic CRUD operations
- Set up test data:
  - Test user accounts (via Supabase seed)
  - Test fixtures for CRUD entities
- Configure CI quality gates:
  - Update CI workflow with test steps
  - Set up test result reporting

**Outputs:**
- `playwright.config.ts`
- `vitest.config.ts`
- `/tests/e2e/auth.spec.ts`
- `/tests/e2e/navigation.spec.ts`
- `/tests/e2e/crud.spec.ts`
- `/tests/fixtures/`
- Updated CI workflow

**Depends on:** Phase 1 scaffold, auth implementation plan.

#### Quality Gate 2: Core Features Checkpoint

The Coordinator validates:

| Check | Criteria | Blocking |
|-------|----------|----------|
| Auth works | Can sign up, log in, log out, sessions persist | Yes |
| CRUD works | Can create, read, update, delete core entities | Yes |
| RLS enforced | Users cannot access other users' data | Yes |
| Marketing pages render | Landing and pricing pages load with correct content | Yes |
| SEO tags present | Meta tags, OG tags, sitemap, robots.txt all correct | No |
| Tests pass | All current E2E and unit tests pass | Yes |
| Build succeeds | `next build` produces no errors | Yes |
| No TypeScript errors | `tsc --noEmit` passes | Yes |

---

### Phase 3: Integration & Revenue (Parallel -- ~45 minutes)

**Goal:** Wire up payments, connect all the pieces, and complete the revenue infrastructure.

#### Senior Full-Stack Developer
- Build payment UI components:
  - Upgrade/downgrade buttons on settings page
  - Subscription status display (current plan, next billing date)
  - Billing portal redirect button
  - Checkout success/cancel pages
- Integrate with RevOps's Stripe logic:
  - Call `createCheckoutSession()` from upgrade button
  - Call `createBillingPortalSession()` from billing settings
  - Display subscription status from database
- Build the onboarding wizard (if enabled in config):
  - Multi-step form
  - Progress indicator
  - Skip/complete logic with database persistence
- Polish error handling:
  - Toast notifications for user-facing errors
  - Retry logic for transient failures
  - Offline state detection

**Outputs:**
- Payment UI components
- Checkout success/cancel pages
- Onboarding wizard
- Polished error handling

**Depends on:** Phase 2 dashboard, RevOps Stripe configuration.

#### RevOps Specialist
- Configure Stripe products and prices:
  - Create Product for each plan in config
  - Create monthly and annual Price for each product
  - Configure trial period on applicable prices
  - Set up Stripe Tax (if applicable)
- Create Checkout Session handler:
  - `/app/api/checkout/route.ts`
  - Creates Stripe Checkout Session with correct price, trial, and metadata
  - Handles success and cancel redirects
- Create Billing Portal handler:
  - `/app/api/billing-portal/route.ts`
  - Creates Stripe Billing Portal Session
  - Configure portal: update payment method, cancel subscription, switch plans
- Create webhook handler (`/app/api/webhooks/stripe/route.ts`):
  - Verify webhook signature
  - Handle events:
    - `checkout.session.completed` -- Create/update subscription record
    - `customer.subscription.created` -- Sync subscription to database
    - `customer.subscription.updated` -- Handle plan changes, status changes
    - `customer.subscription.deleted` -- Mark subscription as canceled
    - `invoice.payment_succeeded` -- Record payment, update status
    - `invoice.payment_failed` -- Trigger dunning flow
    - `customer.subscription.trial_will_end` -- Queue notification
  - Idempotency: check event ID to prevent duplicate processing
  - Error handling: return 200 to Stripe even on processing errors (log and retry internally)
- Create subscription management library (`/lib/subscription.ts`):
  - `getSubscriptionStatus(userId)` -- Current plan and status
  - `canAccessFeature(userId, feature)` -- Feature gating
  - `getUsageLimits(userId)` -- Current limits based on plan
- Implement dunning flow:
  - Email notification on payment failure
  - Retry tracking
  - Grace period enforcement
  - Automatic downgrade after grace period

**Outputs:**
- Stripe products/prices (configured in Stripe)
- `/app/api/checkout/route.ts`
- `/app/api/billing-portal/route.ts`
- `/app/api/webhooks/stripe/route.ts`
- `/lib/stripe.ts`
- `/lib/subscription.ts`
- Dunning flow documentation

**Depends on:** Phase 1 schema, config subscription plans.

#### Database Engineer
- Write payment-related migration (`004_payment_tables.sql`):
  - `customers` table (Stripe customer ID mapping)
  - `subscriptions` table (synced with Stripe)
  - `prices` and `products` tables (synced with Stripe)
  - `invoices` table (payment history)
  - RLS policies for payment tables
  - Indexes on Stripe IDs for webhook lookup performance
- Create database views for revenue reporting:
  - `active_subscriptions` view
  - `mrr_summary` view
  - `churn_events` view
- Create webhook handler helper functions:
  - `upsert_subscription(stripe_subscription)` -- Upsert from Stripe data
  - `sync_customer(stripe_customer)` -- Sync customer data
  - `record_invoice(stripe_invoice)` -- Record payment

**Outputs:**
- `/supabase/migrations/004_payment_tables.sql`
- Revenue reporting views
- Webhook helper functions

**Depends on:** Phase 2 schema, RevOps Stripe product IDs.

#### Cloud / DevOps Engineer
- Configure Stripe webhook endpoint in Stripe Dashboard:
  - Point to production webhook URL
  - Select events to listen for
  - Record webhook signing secret
- Add webhook-related environment variables:
  - `STRIPE_WEBHOOK_SECRET` in Vercel and GitHub Secrets
- Create CD pipeline (`.github/workflows/cd.yml`):
  - Trigger on push to `main`
  - Run full CI suite
  - Deploy to Vercel production
  - Run Supabase migrations
  - Post-deployment health check
- Set up monitoring:
  - Sentry alerts for error spikes
  - Vercel Analytics configuration
  - Health check endpoint (`/api/health`)
- Configure secrets management:
  - Audit all environment variables
  - Ensure no secrets in code or logs
  - Document which secrets are in which service

**Outputs:**
- Stripe webhook endpoint (configured)
- `.github/workflows/cd.yml`
- `/app/api/health/route.ts`
- Monitoring configuration
- Secrets audit document

**Depends on:** Phase 2 infrastructure, RevOps webhook requirements.

#### Marketing Frontend Developer
- Integrate pricing page with Stripe:
  - Plan cards link to checkout endpoints
  - Monthly/annual price toggle with real prices
  - "Current plan" badge for logged-in users
- Add conversion tracking:
  - Signup funnel events
  - Pricing page view tracking
  - Checkout initiated tracking
  - CTA click tracking
- Implement cookie consent banner (if enabled in config)
- Final marketing page polish:
  - Responsive testing across breakpoints
  - Animation and transitions
  - Loading states for dynamic pricing data

**Outputs:**
- Updated pricing page with Stripe integration
- Conversion tracking implementation
- Cookie consent banner
- Final marketing polish

**Depends on:** Phase 2 marketing pages, RevOps checkout endpoints.

#### Quality Gate 3: Integration Checkpoint

| Check | Criteria | Blocking |
|-------|----------|----------|
| Checkout works | Can complete a test checkout with Stripe test card | Yes |
| Webhooks process | Checkout webhook creates subscription record in DB | Yes |
| Billing portal works | Can access Stripe billing portal and return | Yes |
| Subscription status correct | Dashboard shows correct plan after checkout | Yes |
| Pricing page integrated | Real prices displayed, checkout links work | Yes |
| Dunning logic tested | Simulated payment failure triggers retry | No |
| CD pipeline works | Merge to main triggers deployment | Yes |
| Health check passes | `/api/health` returns 200 | Yes |

---

### Phase 4: Launch Prep (Parallel -- ~30 minutes)

**Goal:** Final testing, quality assurance, and launch readiness.

#### QA / Test Engineer
- Run full E2E test suite:
  - Auth flows (all providers configured)
  - CRUD operations (create, read, update, delete)
  - Payment flows (checkout, billing portal, webhook processing)
  - Navigation (all routes, error pages, 404)
  - Responsive (mobile and desktop viewports)
- Run performance tests:
  - Lighthouse on marketing pages (target: >= 90)
  - Core Web Vitals check
  - Bundle size analysis
- Run security checks:
  - RLS bypass attempts
  - Auth bypass attempts
  - XSS and injection attempts
  - Stripe webhook without valid signature
- Generate test report:
  - Pass/fail summary
  - Coverage metrics
  - Performance scores
  - Issues found

**Outputs:**
- Full test results
- Performance report
- Security test results
- Test coverage report

#### RevOps Specialist
- Test complete payment lifecycle:
  - New customer checkout (monthly and annual)
  - Plan upgrade and downgrade
  - Subscription cancellation and reactivation
  - Trial conversion
  - Payment failure and dunning
- Verify MRR tracking queries:
  - Current MRR calculation
  - Churn rate calculation
  - LTV estimation
- Set up cost monitoring:
  - Infrastructure spend alerts
  - Stripe fee tracking
  - Budget threshold notifications
- Document revenue operations:
  - Stripe configuration summary
  - Webhook event flow diagram
  - Dunning schedule and escalation
  - Revenue metrics definitions

**Outputs:**
- Payment lifecycle test results
- MRR dashboard queries
- Cost monitoring configuration
- Revenue operations documentation

#### Cloud / DevOps Engineer
- Production deployment:
  - Final environment variable audit
  - Deploy to production via CD pipeline
  - Verify DNS and custom domain (if configured)
  - Enable Vercel Analytics in production
  - Configure Sentry for production (source maps, release tracking)
- Create monitoring dashboard:
  - Error rate alerts
  - Response time alerts
  - Deployment status
- Set up uptime monitoring:
  - Health check endpoint monitoring
  - Alerting for downtime
- Document rollback procedure:
  - Vercel instant rollback steps
  - Database migration rollback steps
  - Stripe configuration rollback
  - DNS rollback

**Outputs:**
- Production deployment (live)
- Monitoring dashboard
- Uptime monitoring
- Rollback documentation

#### Marketing Frontend Developer
- Final SEO audit:
  - All pages have unique titles and descriptions
  - OG images render correctly
  - Structured data validates (Google Rich Results Test)
  - Sitemap is complete and accessible
  - robots.txt allows search engines
- Validate analytics:
  - Conversion events firing correctly
  - Vercel Analytics collecting data
  - Cookie consent working (if enabled)
- Final accessibility check:
  - Keyboard navigation works
  - Screen reader compatible
  - Color contrast meets WCAG AA
  - Focus indicators visible

**Outputs:**
- SEO audit report
- Analytics validation report
- Accessibility audit report

#### Coordinator / Tech Lead
- Final architecture review:
  - All components connected correctly
  - No orphaned routes or dead code
  - Error handling complete
  - Security checklist passed
- Write `LAUNCH_CHECKLIST.md`:
  - Pre-launch verification items
  - Go/no-go criteria
  - Rollback triggers
  - Post-launch monitoring plan
- Update `DECISIONS.md` with any Phase 3/4 decisions
- Final quality assessment:
  - Review all agent outputs
  - Verify all quality gates passed
  - Produce launch recommendation (go/no-go)

**Outputs:**
- `LAUNCH_CHECKLIST.md`
- Updated `DECISIONS.md`
- Launch recommendation

#### Quality Gate 4: Launch Decision

| Check | Criteria | Blocking |
|-------|----------|----------|
| All E2E tests pass | Zero test failures | Yes |
| Lighthouse >= 90 | Marketing pages score 90+ | Yes (marketing pages) |
| Security tests pass | No RLS bypasses, no auth bypasses | Yes |
| Payment lifecycle complete | All payment scenarios tested | Yes |
| Production deployed | App accessible at production URL | Yes |
| Monitoring active | Sentry and analytics collecting data | Yes |
| Documentation complete | Architecture, database, deployment, revenue docs | No |
| Rollback plan documented | Rollback procedure tested and documented | Yes |

**Launch decision:** Coordinator issues GO or NO-GO based on gate results.

---

## Communication Protocol

### Message Types

Agents communicate using structured messages with the following types:

| Type | Purpose | Example |
|------|---------|---------|
| `TASK` | Assign work to an agent | Coordinator assigns schema design to Database Engineer |
| `QUERY` | Ask another agent for information | Full-Stack asks Database for table schema |
| `RESPONSE` | Answer a query | Database provides schema definition |
| `ARTIFACT` | Deliver a completed output | Database delivers migration file |
| `CONFLICT` | Report a disagreement or incompatibility | Full-Stack reports schema mismatch with types |
| `GATE` | Quality gate result | Coordinator reports Phase 1 gate: PASS |
| `ESCALATE` | Escalate to user for decision | Coordinator escalates ambiguous business requirement |

### Message Format

```yaml
type: TASK
from: coordinator
to: database-engineer
phase: 1
priority: high
subject: "Design initial database schema"
body: |
  Based on the architecture decisions in ARCHITECTURE.md, design the initial
  Postgres schema including:
  - profiles table (extends auth.users)
  - [project-specific tables]
  - subscriptions table
  Enable RLS on all tables. Write migration 001_initial_schema.sql.
acceptance_criteria:
  - All tables have id, created_at, updated_at
  - RLS enabled on every table
  - Foreign keys with appropriate cascade behavior
  - Indexes on foreign keys
deadline: "Phase 1 completion"
```

### Conflict Resolution

When agents disagree (e.g., schema design vs API contract):

1. The conflicting agents state their positions with rationale
2. The Coordinator evaluates both positions against project goals
3. The Coordinator makes a binding decision and records it in `DECISIONS.md`
4. Both agents proceed with the Coordinator's decision
5. If the Coordinator cannot resolve it, the issue is escalated to the user

### Shared State

All agents have read access to:
- Project configuration (`CONFIG.local.md`)
- Architecture decisions (`ARCHITECTURE.md`)
- Decision log (`DECISIONS.md`)
- Shared type definitions (`/types/`)
- The git repository (latest committed state)

Write access is scoped per agent to prevent conflicts:
- Each agent writes only to their designated directories
- Shared files (e.g., `package.json`, `middleware.ts`) are owned by the Senior Full-Stack developer
- Schema and migration files are owned by the Database Engineer
- Infrastructure files are owned by the Cloud/DevOps Engineer

---

## Git Strategy

### Branch Model

```
main (protected)
  └── feat/phase-1-foundation
  └── feat/phase-2-core-features
  └── feat/phase-3-integration
  └── feat/phase-4-launch-prep
```

Each phase creates a single branch. All agents in that phase commit to the phase branch. The Coordinator merges phase branches to `main` after quality gates pass.

### Commit Convention

```
<type>(<scope>): <subject>

<body>

Agent: <agent-name>
Phase: <phase-number>
```

Types: `feat`, `fix`, `refactor`, `test`, `docs`, `chore`, `ci`
Scopes: `auth`, `dashboard`, `billing`, `marketing`, `db`, `infra`, `test`

Example:
```
feat(db): add initial schema with profiles and subscriptions

- Created profiles table extending auth.users
- Created subscriptions table synced with Stripe
- Enabled RLS on all tables
- Added indexes on foreign keys

Agent: database-engineer
Phase: 1
```

### Merge Rules

- Phase branches merge to `main` only after quality gate passes
- Squash merge to keep `main` history clean
- Delete phase branches after merge
- No direct commits to `main`

---

## Autonomous vs User-Prompted Decisions

### Autonomous (No User Input Needed)

The team makes these decisions automatically:

- File and directory naming conventions
- Component structure and organization
- CSS class names and Tailwind utilities
- Database column types and index strategy
- RLS policy structure
- Test organization and naming
- CI/CD pipeline step ordering
- Git commit messages
- Error message wording
- Loading and error state design

### User-Prompted (Require User Input)

The team pauses and asks the user for:

- **Business logic ambiguity** -- "Should users be able to share projects with other users?"
- **Scope expansion** -- "The requested feature implies real-time collaboration. This is significant scope. Proceed?"
- **Budget overrun** -- "Phase 2 is projected to exceed budget by 15%. Continue or optimize?"
- **Security trade-offs** -- "Public API access requested but no rate limiting specified. Add rate limiting?"
- **Third-party service selection** -- "Email provider needed for notifications. Resend, SendGrid, or Postmark?"
- **Design decisions** -- "No brand guidelines provided. Use default blue/gray theme or wait for design input?"

### Escalation Triggers

The Coordinator escalates immediately when:

1. A quality gate fails twice consecutively
2. Two agents produce conflicting outputs that cannot be auto-resolved
3. A required environment variable is missing
4. Infrastructure costs exceed the configured alert threshold
5. A security vulnerability is detected
6. The project configuration has ambiguous or contradictory settings

---

## Scenario-Based Validation

After each phase, the Coordinator runs scenario-based validation against the scenarios defined in `/scenarios/`. Each scenario specifies:

- **Preconditions:** System state before the scenario
- **Steps:** User actions to perform
- **Expected outcomes:** What should happen at each step
- **Edge cases:** Unusual inputs or failure conditions

Phase validation mapping:

| Phase | Scenarios Validated |
|-------|-------------------|
| Phase 1 | None (foundation only) |
| Phase 2 | `auth-flow.md`, `data-crud.md` |
| Phase 3 | `payment-flow.md`, `subscription-lifecycle.md` |
| Phase 4 | All scenarios, `deployment-rollback.md` |

Scenario failures in Phase 4 are blocking for launch. Scenario failures in Phases 2-3 are logged as issues for the next phase.
