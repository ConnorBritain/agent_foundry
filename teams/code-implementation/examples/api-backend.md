# Example: Building a REST API Backend with Node.js and Express

## Scenario

A fintech company needs a backend API for their expense tracking application. The API handles user accounts, expense submissions, receipt image uploads, approval workflows, and reporting. The backend must be secure, well-tested, and production-ready with comprehensive API documentation.

## Project Charter Inputs

```yaml
project_type: backend_api
primary_language: typescript
framework: express
testing_framework: jest
package_manager: npm

repository:
  url: https://github.com/acme/expense-api
  default_branch: main

feature:
  name: expense-api-v1
  description: |
    REST API for expense management:
    - User registration and JWT authentication
    - Expense CRUD with category tagging and receipt attachment
    - Multi-step approval workflow (submit, review, approve/reject)
    - Receipt image upload to S3 with presigned URLs
    - Expense reporting endpoints (by user, team, date range, category)
    - Rate limiting, request validation, and structured error responses
    - PostgreSQL with Prisma ORM
    - Redis for session caching and rate limiting

code_style: google
agent_budget:
  model_config: default
  max_total_cost_usd: 35
```

## Team Execution

### Phase 1: API Design and Decomposition (10 min, $0.25)
- Coordinator designs the API resource hierarchy and endpoint map
- Defines database schema: `users`, `teams`, `expenses`, `receipts`, `approvals`, `categories`
- Plans middleware stack: auth, validation, rate limiting, error handling, request logging
- Assigns Specialist A: auth, expense CRUD, approval workflow, database layer
- Assigns Specialist B: receipt upload (S3), reporting endpoints, rate limiting, middleware
- Shared interfaces: Prisma models, API response types, error codes, middleware signatures

### Phase 2: Parallel Implementation (35 min, $19.80)
**Specialist A builds:**
- `src/routes/auth.ts` -- POST /register, POST /login, POST /refresh, POST /logout
- `src/routes/expenses.ts` -- Full CRUD with filtering, pagination, and sorting
- `src/routes/approvals.ts` -- Submit, review, approve, reject workflow endpoints
- `src/middleware/auth.ts` -- JWT verification and token refresh middleware
- `src/middleware/validate.ts` -- Zod schema validation middleware
- `src/services/expense.service.ts` -- Business logic for expense operations
- `src/services/approval.service.ts` -- State machine for approval workflow
- `prisma/schema.prisma` -- Full database schema with relations
- `prisma/migrations/` -- Initial migration files
- `prisma/seed.ts` -- Seed data for development

**Specialist B builds:**
- `src/routes/receipts.ts` -- Upload initiation, presigned URL generation, confirmation
- `src/routes/reports.ts` -- Aggregation endpoints (by user, team, date range, category)
- `src/middleware/rateLimit.ts` -- Redis-backed rate limiting with configurable windows
- `src/middleware/errorHandler.ts` -- Global error handler with structured responses
- `src/middleware/requestLogger.ts` -- Structured JSON request logging
- `src/services/storage.service.ts` -- S3 client with presigned URL generation
- `src/services/report.service.ts` -- Report aggregation queries with Prisma
- `src/config/index.ts` -- Environment configuration with validation

**Test Engineer writes:**
- Holdout scenarios for auth flow (register, login, token refresh, expired token)
- Holdout scenarios for expense lifecycle (create, update, submit for approval, approve)
- Holdout scenarios for receipt upload (initiate, upload to S3, confirm, retrieve)
- Holdout scenarios for reporting (date range filters, category aggregation, team totals)
- Holdout scenarios for error handling (invalid input, unauthorized access, not found)

### Phase 3: Code Review (15 min, $4.80)
- Reviewer flags 3 blockers:
  - BLOCKER: Expense update endpoint allows modification after approval submission
  - BLOCKER: Report endpoint missing team authorization check (user can query other teams)
  - BLOCKER: Receipt presigned URL has no expiration limit configured
- Reviewer notes 3 suggestions:
  - SUGGESTION: Add cursor-based pagination for expense list (offset pagination is less efficient at scale)
  - SUGGESTION: Use database transaction for approval state transitions
  - SUGGESTION: Add request ID header propagation for distributed tracing
- Specialist A fixes blocker 1 (adds status check middleware) and blocker 2 (adds team membership verification)
- Specialist B fixes blocker 3 (sets 15-minute expiration on presigned URLs)
- Reviewer approves on second pass

### Phase 4: Testing and Documentation (15 min, $0.55)
- Test Engineer runs holdout scenarios: 28/30 pass (93% satisfaction)
  - 2 failures: edge case with concurrent approval and report caching staleness
- Generates 52 Jest unit tests and 18 supertest integration tests
- Coverage: 87% on new code
- DevOps Specialist configures:
  - Dockerfile with multi-stage build (final image: 145MB)
  - docker-compose.yml with PostgreSQL, Redis, and LocalStack (S3 mock)
  - GitHub Actions: lint --> typecheck --> test --> build --> push image
  - Health check endpoint at GET /health
- Documentation Writer generates OpenAPI spec and README

## Deliverables

```
expense-api/
  src/
    routes/
      auth.ts, expenses.ts, approvals.ts, receipts.ts, reports.ts, health.ts
    middleware/
      auth.ts, validate.ts, rateLimit.ts, errorHandler.ts, requestLogger.ts
    services/
      expense.service.ts, approval.service.ts, storage.service.ts, report.service.ts
    config/
      index.ts
    types/
      api.ts, errors.ts
    app.ts
    server.ts
  prisma/
    schema.prisma
    migrations/001_initial/
    seed.ts
  tests/
    unit/ (52 files)
    integration/ (18 files)
    fixtures/
  docs/
    openapi.yaml
  .github/workflows/ci.yml
  Dockerfile
  docker-compose.yml
  .env.example
  README.md
```

## Cost Estimate

| Phase | Tokens | Cost |
|-------|--------|------|
| Planning | ~30K | $0.25 |
| Implementation | ~320K | $19.80 |
| Code Review | ~80K | $4.80 |
| Testing + Docs | ~60K | $0.55 |
| **Total** | **~490K** | **$25.40** |

## Expected Outcomes

- Production-ready REST API with 20+ endpoints
- JWT authentication with token refresh
- Multi-step approval workflow with state machine
- S3 receipt upload with secure presigned URLs
- Redis-backed rate limiting
- Prisma ORM with typed database access
- 87% test coverage with unit and integration tests
- Docker setup for local development and production deployment
- OpenAPI documentation for all endpoints
- CI/CD pipeline with automated testing and image builds
