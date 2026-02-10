# Example: API Migration -- REST v1 to v2

## Feature Overview

Migrate a set of API endpoints from v1 to v2. The v2 endpoints introduce consistent response envelopes, cursor-based pagination replacing offset pagination, and standardized error responses. The v1 endpoints must continue to work during the migration period with a deprecation warning header.

## Configuration

```yaml
project_type: backend_api
primary_language: typescript
framework: express
testing_framework: jest
code_style: airbnb
review_strictness: standard

feature:
  name: api-v2-migration
  description: "Migrate /api/v1/users and /api/v1/projects to /api/v2 with new response format"
  priority: high

agent_budget:
  model_config: default
  max_total_cost_usd: 40
```

## Phase 1: Planning (~10 min)

### Coordinator
- Analyzes existing v1 routes: identifies 4 user endpoints and 5 project endpoints
- Defines the v2 response envelope and error format as shared interfaces
- Plans backward compatibility: v1 routes remain but add deprecation header
- Decomposes into parallel tracks: Specialist A handles user endpoints, Specialist B handles project endpoints

**Task Assignment:**

| Task | Specialist | Complexity | Dependencies |
|------|-----------|------------|-------------|
| V2 response envelope middleware | A (owner) | Medium | None |
| V2 error handler middleware | A (owner) | Medium | None |
| Cursor-based pagination utility | B (owner) | Medium | None |
| User endpoints v2 (5 routes) | A | High | Envelope + error middleware |
| Project endpoints v2 (5 routes) | B | High | Pagination utility |
| V1 deprecation middleware | A | Low | None |
| V1 route forwarding (proxy to v2 with transform) | B | Medium | V2 routes |
| API versioning router setup | A (owner) | Low | None |

**Shared Interfaces:**
```typescript
// types/api.ts (owned by Specialist A)
interface ApiResponse<T> {
  data: T;
  meta: {
    requestId: string;
    timestamp: string;
    pagination?: PaginationMeta;
  };
}

interface PaginationMeta {
  cursor: string | null;
  hasMore: boolean;
  totalCount: number;
}

interface ApiError {
  error: {
    code: string;
    message: string;
    details?: Record<string, string[]>;
    requestId: string;
  };
}
```

## Phase 2: Implementation (~40 min, parallel)

### Specialist A (Primary -- Users + Middleware)
- Creates v2 response envelope middleware that wraps handler responses
- Creates v2 error handler that catches errors and formats them consistently
- Creates API versioning router: `/api/v1/*` and `/api/v2/*`
- Migrates user endpoints to v2:
  - `GET /api/v2/users` (list with cursor pagination)
  - `GET /api/v2/users/:id` (detail)
  - `POST /api/v2/users` (create)
  - `PUT /api/v2/users/:id` (update)
  - `DELETE /api/v2/users/:id` (delete)
- Adds deprecation header middleware for v1 routes: `Deprecation: true` and `Sunset: 2026-06-01`

**Files created/modified:**
- `src/middleware/v2-envelope.ts` (new, 45 lines)
- `src/middleware/v2-error-handler.ts` (new, 65 lines)
- `src/middleware/deprecation.ts` (new, 20 lines)
- `src/routes/v2/users.ts` (new, 140 lines)
- `src/routes/index.ts` (modified, +15 lines)
- `types/api.ts` (new, 35 lines)

### Specialist B (Secondary -- Projects + Pagination)
- Creates cursor-based pagination utility that works with any Sequelize/Prisma query
- Migrates project endpoints to v2:
  - `GET /api/v2/projects` (list with cursor pagination)
  - `GET /api/v2/projects/:id` (detail)
  - `POST /api/v2/projects` (create)
  - `PUT /api/v2/projects/:id` (update)
  - `DELETE /api/v2/projects/:id` (delete)
- Creates v1-to-v2 response transformer for backward compatibility
- Updates v1 routes to internally call v2 handlers and transform responses back

**Files created/modified:**
- `src/utils/cursor-pagination.ts` (new, 80 lines)
- `src/routes/v2/projects.ts` (new, 145 lines)
- `src/utils/v1-compat.ts` (new, 55 lines)
- `src/routes/v1/users.ts` (modified, +25 lines)
- `src/routes/v1/projects.ts` (modified, +25 lines)

### Test Engineer (Scenario Writing)
- Designs scenarios for both v1 and v2 endpoints operating simultaneously
- Edge cases: v1 clients receiving deprecation headers, cursor with deleted records, empty pages
- Backward compatibility: v1 response format unchanged for existing clients

## Phase 3: Code Review (~20 min)

### Code Reviewer
- Reviews Specialist A: validates middleware composition, error handler completeness
- Reviews Specialist B: validates cursor pagination correctness, v1 compatibility layer
- Cross-references: ensures both Specialists use the same response envelope

**Findings:**
- BLOCKER: Cursor pagination breaks when a record is deleted between pages (cursor points to nonexistent record)
- BLOCKER: V1 compatibility layer does not transform v2 pagination back to offset format
- SUGGESTION: Add `X-API-Version` response header for debugging
- SUGGESTION: Add OpenAPI schema for v2 endpoints

**Resolution:**
- Specialist B fixes cursor to handle deleted records (uses `>=` instead of `=`)
- Specialist B adds offset-format transformation in v1 compatibility layer
- Both blockers resolved on second review pass

## Phase 4: Testing + Documentation (~15 min, parallel)

### Test Engineer
- Runs holdout scenarios: 18/19 pass (94.7% satisfaction)
- Failed scenario: concurrent pagination with real-time inserts (deferred as known limitation)
- Generates 22 unit tests (middleware, pagination, transformers) and 14 integration tests (endpoint-level)
- Coverage: 89% lines, 85% branches
- Backward compatibility tests: all v1 clients receive identical response format

### Documentation Writer
- Creates v2 API migration guide for consumers
- Documents deprecation timeline and sunset date
- Adds inline docs for middleware and pagination utility
- Updates README with v2 endpoint list and migration notes
- Changelog entry: v2 API launch with backward-compatible v1 support

## Deliverables Produced

1. **V2 API endpoints** -- 10 endpoints (5 user, 5 project) with new response format
2. **Response middleware** -- Envelope wrapper, error handler, deprecation headers
3. **Cursor pagination** -- Reusable utility for any query
4. **V1 compatibility** -- Existing v1 routes continue to work with deprecation warnings
5. **Tests** -- 22 unit, 14 integration, backward compatibility suite
6. **Documentation** -- Migration guide, API docs, deprecation timeline

## Cost Summary

| Phase | Agent | Tokens | Cost |
|-------|-------|--------|------|
| Planning | Coordinator | 28K | $0.22 |
| Implementation | Specialist A | 140K | $9.10 |
| Implementation | Specialist B | 135K | $8.78 |
| Implementation | Test Engineer (scenarios) | 14K | $0.11 |
| Review | Code Reviewer | 72K | $4.68 |
| Testing | Test Engineer | 55K | $0.44 |
| Documentation | Doc Writer | 19K | $0.01 |
| **Total** | | **463K** | **~$23.34** |

## Key Learnings

- **Backward compatibility doubles the work.** Maintaining v1 while building v2 required a compatibility layer that was its own mini-project. Factor this into estimates.
- **Cursor pagination edge cases are subtle.** The deleted-record cursor issue would have caused production incidents. The Code Reviewer caught it because the checklist includes "What happens when referenced data changes between requests?"
- **Shared middleware reduces duplication.** The envelope and error handler middleware, built once by Specialist A, were consumed by both Specialists. Good interface design in Phase 1 paid off.
- **Parallel decomposition by domain works well.** Users and projects were fully independent domains, making parallel implementation clean with no file conflicts.
