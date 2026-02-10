# Example: Building a SaaS Dashboard with Next.js, Supabase, and Stripe

## Scenario

A solo founder needs an MVP for a project management SaaS. The application provides team workspaces, a Kanban task board, user authentication, and subscription billing. The goal is a deployable product that can onboard early beta users within a single team run.

## Project Charter Inputs

```yaml
project_type: web_app
primary_language: typescript
framework: nextjs
testing_framework: vitest
package_manager: pnpm

repository:
  url: https://github.com/acme/taskflow
  default_branch: main

feature:
  name: mvp-dashboard
  description: |
    Full SaaS MVP with:
    - Supabase Auth (email + Google OAuth)
    - Team workspace creation and member invitation
    - Kanban task board with drag-and-drop (To Do, In Progress, Review, Done)
    - Real-time board updates via Supabase Realtime
    - Stripe Checkout for Pro subscription ($29/mo)
    - Usage limits on free tier (max 3 projects, 10 members)

code_style: airbnb
agent_budget:
  model_config: default
  max_total_cost_usd: 40
```

## Team Execution

### Phase 1: Scaffolding and Decomposition (12 min, $0.30)
- Coordinator initializes Next.js 14 project with App Router, Tailwind, and Supabase client
- Creates Supabase migration files: `users`, `teams`, `projects`, `tasks`, `subscriptions` tables
- Defines Row Level Security policies for multi-tenant data isolation
- Assigns Specialist A: auth, API routes, Stripe, database logic, RLS policies
- Assigns Specialist B: layouts, pages, components, real-time hooks, drag-and-drop
- Shared interfaces: `Task`, `Team`, `Project`, `User`, `Subscription` types in `lib/types.ts`

### Phase 2: Parallel Implementation (45 min, $20.50)
**Specialist A builds:**
- `app/api/auth/callback/route.ts` -- Supabase OAuth callback handler
- `app/api/teams/route.ts` -- Team CRUD endpoints
- `app/api/projects/route.ts` -- Project CRUD with team scoping
- `app/api/tasks/route.ts` -- Task CRUD with project scoping
- `app/api/billing/checkout/route.ts` -- Stripe Checkout session creation
- `app/api/billing/webhook/route.ts` -- Stripe webhook handler (signature verification)
- `lib/supabase/server.ts` -- Server-side Supabase client
- `lib/stripe.ts` -- Stripe client configuration
- `supabase/migrations/001_initial_schema.sql` -- Full schema with RLS

**Specialist B builds:**
- `app/(dashboard)/layout.tsx` -- Sidebar navigation with team switcher
- `app/(dashboard)/projects/page.tsx` -- Project list with create dialog
- `app/(dashboard)/projects/[id]/board/page.tsx` -- Kanban board page
- `components/board/Board.tsx` -- Drag-and-drop board using dnd-kit
- `components/board/Column.tsx` -- Board column with task cards
- `components/board/TaskCard.tsx` -- Draggable task card
- `components/team/TeamSwitcher.tsx` -- Workspace dropdown selector
- `hooks/useRealtimeBoard.ts` -- Supabase Realtime subscription for board updates
- `hooks/useTeam.ts` -- Team context and member management

**Test Engineer writes:**
- Holdout scenarios for auth flow (login, logout, OAuth callback, session refresh)
- Holdout scenarios for task CRUD (create, move between columns, delete, assign)
- Holdout scenarios for billing (checkout redirect, webhook processing, plan limits)

### Phase 3: Code Review (18 min, $5.00)
- Reviewer flags 2 blockers:
  - BLOCKER: Stripe webhook endpoint missing signature verification on one code path
  - BLOCKER: RLS policy on `tasks` table allows cross-team read via missing team_id filter
- Reviewer notes 4 suggestions:
  - SUGGESTION: Extract board column logic into custom hook
  - SUGGESTION: Add loading skeleton to project list
  - SUGGESTION: Use Supabase generated types instead of manual type definitions
  - SUGGESTION: Add rate limiting to auth callback
- Specialist A fixes both blockers in 8 minutes
- Reviewer approves on second pass

### Phase 4: Testing and Deployment (16 min, $0.60)
- Test Engineer runs holdout scenarios: 22/24 pass (92% satisfaction)
  - 2 failures: edge case with empty board state and concurrent task moves
- Generates 38 Vitest unit tests and 6 Playwright E2E tests
- Coverage: 84% on new code
- DevOps Specialist configures:
  - Vercel project with environment variables
  - GitHub Actions: lint --> typecheck --> test --> deploy
  - Supabase project linking and migration automation
- Documentation Writer produces README with setup instructions, env var table, and architecture overview

## Deliverables

```
taskflow/
  app/
    (auth)/
      login/page.tsx
      callback/route.ts
    (dashboard)/
      layout.tsx
      projects/
        page.tsx
        [id]/board/page.tsx
    api/
      auth/callback/route.ts
      teams/route.ts
      projects/route.ts
      tasks/route.ts
      billing/
        checkout/route.ts
        webhook/route.ts
  components/
    board/Board.tsx, Column.tsx, TaskCard.tsx
    team/TeamSwitcher.tsx, InviteDialog.tsx
    ui/Button.tsx, Dialog.tsx, Skeleton.tsx
  hooks/
    useRealtimeBoard.ts, useTeam.ts, useSubscription.ts
  lib/
    supabase/server.ts, client.ts, middleware.ts
    stripe.ts
    types.ts
  supabase/
    migrations/001_initial_schema.sql
    seed.sql
  tests/
    unit/ (38 files)
    e2e/ (6 files)
  .github/workflows/ci.yml
  Dockerfile
  docker-compose.yml
  vercel.json
  README.md
```

## Cost Estimate

| Phase | Tokens | Cost |
|-------|--------|------|
| Planning | ~35K | $0.30 |
| Implementation | ~350K | $20.50 |
| Code Review | ~85K | $5.00 |
| Testing + Docs | ~70K | $0.60 |
| **Total** | **~540K** | **$26.40** |

## Expected Outcomes

- Deployable SaaS MVP in approximately 90 minutes
- Production-ready auth with OAuth and session management
- Multi-tenant data isolation via Supabase RLS
- Real-time Kanban board with drag-and-drop
- Stripe billing integration with webhook security
- 84% test coverage with E2E tests for critical paths
- CI/CD pipeline with automated deployment to Vercel
