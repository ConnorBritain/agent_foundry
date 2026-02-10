# Scenario: Greenfield Project -- Next.js + Supabase Application

## Context

A startup needs to build a new web application from scratch. The project is a task management SaaS with user authentication, team workspaces, real-time task boards, and Stripe billing. The tech stack is Next.js 14 (App Router), Supabase (auth, database, realtime), Tailwind CSS, and deployment to Vercel.

No existing codebase. The team starts from an empty repository and delivers a deployable MVP.

## Trigger

Product manager provides a feature specification document covering:
- User registration and login via Supabase Auth (email + Google OAuth)
- Team workspace creation and member invitation
- Task board with columns (To Do, In Progress, Done) and drag-and-drop
- Real-time updates when team members move tasks
- Stripe subscription integration (free tier + pro tier)

## Team Configuration

| Agent | Model | Role in This Scenario |
|-------|-------|-----------------------|
| Coordinator | Sonnet 4.5 | Scaffold project structure, decompose into parallel workstreams |
| Specialist A | Opus 4.6 | Auth system, database schema, API routes, Stripe integration |
| Specialist B | Opus 4.6 | UI components, task board, real-time subscriptions, drag-and-drop |
| Code Reviewer | Sonnet 4.5 | Review both workstreams, verify Supabase security rules |
| Test Engineer | Sonnet 4.5 | E2E auth flows, API tests, real-time subscription tests |
| DevOps Specialist | Sonnet 4.5 | Vercel deployment config, Supabase project setup, CI pipeline |

## Workflow

### Phase 1: Project Scaffolding and Planning (~15 min)
- Coordinator runs `npx create-next-app` with TypeScript and Tailwind
- Defines project structure: `/app`, `/components`, `/lib`, `/supabase`
- Creates Supabase migration files for initial schema (users, teams, tasks)
- Decomposes work: A gets backend + auth + billing, B gets frontend + real-time
- Defines shared interfaces: Task type, Team type, User type, API response shapes

### Phase 2: Parallel Implementation (~40-60 min)
- **Specialist A:** Supabase schema migrations, auth configuration, API route handlers for CRUD operations, Stripe webhook handler, Row Level Security policies
- **Specialist B:** Layout components, task board UI with drag-and-drop (dnd-kit), real-time subscription hooks, team workspace switcher, responsive design
- **Test Engineer:** Writes holdout scenarios for auth flows, task CRUD, team permissions, Stripe webhook handling

### Phase 3: Code Review (~20 min)
- Reviewer checks Supabase RLS policies for authorization gaps
- Verifies Stripe webhook signature validation
- Checks real-time subscription cleanup on unmount
- Validates form input sanitization on all user-facing inputs

### Phase 4: Testing and Deployment (~20 min)
- Test Engineer runs holdout scenarios, generates Vitest unit tests and Playwright E2E tests
- DevOps Specialist configures Vercel project, environment variables, preview deployments
- DevOps Specialist creates GitHub Actions workflow for lint, typecheck, test, deploy
- Documentation Writer updates README with setup instructions and environment variables

## Expected Outputs

- Complete Next.js 14 application with 30-50 files
- Supabase migration files and RLS policies
- Stripe integration with webhook handler
- Vitest unit tests and Playwright E2E tests (>= 80% coverage)
- GitHub Actions CI/CD pipeline
- Vercel deployment configuration
- README with local development setup instructions

## Estimated Cost

| Configuration | Est. Tokens | Est. Cost | Est. Time |
|--------------|-------------|-----------|-----------|
| Budget (all Sonnet) | ~600K | ~$15 | ~90 min |
| Default (mixed) | ~600K | ~$35 | ~75 min |
| Premium (all Opus) | ~600K | ~$55 | ~70 min |

Note: Greenfield projects use approximately 1.2x the token budget of a standard feature due to scaffolding and initial structure decisions. The Default configuration is recommended for greenfield work because Opus catches architectural issues early.
