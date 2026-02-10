# Scenario: API Endpoint Development

This scenario validates the team's ability to design, implement, test, and document a new API endpoint or set of related endpoints.

---

## Scenario Overview

| Property | Value |
|----------|-------|
| **Priority** | High |
| **Validated After** | Phase 4 |
| **Primary Agents** | All 6 agents |
| **Estimated Duration** | ~45-60 minutes (hybrid mode) |

---

## Success Path: RESTful CRUD Endpoint

### Preconditions

- Existing project with established API patterns (route structure, response format, auth middleware)
- Database schema exists or migration will be created
- Authentication and authorization middleware is in place

### Steps

| Step | Action | Expected Outcome |
|------|--------|------------------|
| 1 | Coordinator reads endpoint spec and analyzes existing API patterns | Identifies: route structure, middleware chain, response format, validation approach |
| 2 | Coordinator decomposes into parallel tasks | A: route handlers + validation, B: database migration + service layer |
| 3 | Specialist B creates database migration and service layer | New table, indexes, and data access functions |
| 4 | Specialist A creates route handlers with validation | CRUD endpoints following existing patterns |
| 5 | Code Reviewer validates security and correctness | Auth checks, input validation, error handling, SQL injection prevention |
| 6 | Test Engineer runs holdout scenarios | Happy paths, error paths, auth bypass attempts |
| 7 | Doc Writer creates API documentation | Endpoint docs with request/response examples |

### Validation Criteria

- [ ] Endpoints follow existing API patterns (route naming, response shape)
- [ ] All endpoints require authentication (unless explicitly public)
- [ ] Input validation on all request bodies and query parameters
- [ ] Proper HTTP status codes (200, 201, 204, 400, 401, 403, 404, 500)
- [ ] Error responses follow existing error format
- [ ] Database migration is reversible
- [ ] Indexes added for query patterns
- [ ] Rate limiting on public-facing endpoints
- [ ] API documentation with examples for each endpoint

---

## Success Path: Protected Endpoint with Authorization

### Preconditions

- Endpoint requires role-based access control (e.g., only admins can delete)
- Authorization middleware or utility exists in the project

### Steps

| Step | Action | Expected Outcome |
|------|--------|------------------|
| 1 | Coordinator identifies authorization requirements per endpoint | GET: any authenticated user, POST/PUT: owner only, DELETE: admin only |
| 2 | Specialist A implements authorization checks | Middleware or inline checks per endpoint |
| 3 | Code Reviewer verifies authorization cannot be bypassed | Tests for: missing token, wrong role, resource owned by another user |
| 4 | Test Engineer writes authorization test matrix | Every role x endpoint combination tested |

### Validation Criteria

- [ ] Unauthorized users receive 401 (not 500)
- [ ] Forbidden users receive 403 (not 404 or 500)
- [ ] Users cannot access other users' resources
- [ ] Admin-only actions reject non-admin users
- [ ] Authorization check cannot be bypassed via parameter manipulation

---

## Edge Case: Endpoint with File Upload

### Preconditions

- Endpoint accepts multipart/form-data with file uploads
- Storage service is configured (local, S3, or equivalent)

### Steps

| Step | Action | Expected Outcome |
|------|--------|------------------|
| 1 | Specialist A implements file upload handler | Validates file type, size, and content |
| 2 | Specialist A stores file and returns reference | File stored securely, reference saved to database |
| 3 | Code Reviewer checks for: path traversal, file type validation, size limits | No security vulnerabilities in file handling |
| 4 | Test Engineer tests with: oversized files, wrong types, malicious filenames | All invalid uploads rejected with clear errors |

### Validation Criteria

- [ ] File type validation (allowlist, not blocklist)
- [ ] File size limit enforced
- [ ] Filename sanitized (no path traversal)
- [ ] File content validated (not just extension)
- [ ] Storage path does not leak internal directory structure

---

## Edge Case: Paginated List Endpoint

### Preconditions

- Endpoint returns a list of resources that could be large
- Project has established pagination patterns (cursor or offset)

### Steps

| Step | Action | Expected Outcome |
|------|--------|------------------|
| 1 | Specialist A implements paginated list endpoint | Default page size, max page size, cursor or offset support |
| 2 | Test Engineer tests pagination edge cases | Empty results, single page, last page, invalid cursor |

### Validation Criteria

- [ ] Default page size applied when not specified
- [ ] Maximum page size enforced (prevents full table scan)
- [ ] Empty page returns empty array, not error
- [ ] Invalid page/cursor returns 400, not 500
- [ ] Response includes pagination metadata (total, next cursor, has_more)
- [ ] Results are consistently ordered (deterministic pagination)

---

## Agents Responsible

| Agent | Responsibility |
|-------|---------------|
| **Coordinator** | Analyze existing API patterns, decompose endpoint tasks |
| **Specialist A** | Route handlers, validation, middleware, request/response |
| **Specialist B** | Database migration, service layer, data access |
| **Code Reviewer** | Security review (auth, injection, validation), pattern compliance |
| **Test Engineer** | Endpoint tests (happy path, errors, auth, edge cases) |
| **Doc Writer** | API documentation with examples, changelog entry |
