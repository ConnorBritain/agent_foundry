# API Design — Compressed AGENTS.md Knowledge

## Quick Reference
| Area | Key Concepts |
|---|---|
| REST | Resources, HTTP methods, status codes, HATEOAS |
| Errors | Consistent format, error codes, problem details (RFC 9457) |
| Pagination | Cursor-based, offset-based, page-based, link headers |
| Versioning | URL path, headers, query params — strategies and tradeoffs |
| OpenAPI | Specification, code generation, documentation, validation |
| Auth | Bearer tokens, API keys, OAuth2, rate limiting |

## REST Resource Design
### URL Structure
```
/{resource}              — collection (plural nouns)
/{resource}/{id}         — single resource
/{resource}/{id}/{sub}   — nested resource
```

| Pattern | Example | Anti-Pattern |
|---|---|---|
| Plural nouns | /users, /posts | /user, /getUsers |
| Hierarchical | /users/123/posts | /getUserPosts?userId=123 |
| Kebab-case | /user-profiles | /userProfiles, /user_profiles |
| No verbs in URL | POST /users | POST /createUser |
| Filter via query | /users?role=admin | /users/admins |
| Action sub-resource | /orders/123/cancel | /cancelOrder/123 |

### HTTP Methods
| Method | Purpose | Idempotent | Request Body | Success Code |
|---|---|---|---|---|
| GET | Read resource(s) | Yes | No | 200 |
| POST | Create resource | No | Yes | 201 |
| PUT | Full replace | Yes | Yes | 200 |
| PATCH | Partial update | Yes* | Yes | 200 |
| DELETE | Remove resource | Yes | No | 204 |

## HTTP Status Codes
### Success (2xx)
| Code | Meaning | When |
|---|---|---|
| 200 | OK | GET, PUT, PATCH success |
| 201 | Created | POST success, include Location header |
| 204 | No Content | DELETE success, no body returned |

### Client Error (4xx)
| Code | Meaning | When |
|---|---|---|
| 400 | Bad Request | Validation failed, malformed body |
| 401 | Unauthorized | Missing or invalid authentication |
| 403 | Forbidden | Authenticated but insufficient permissions |
| 404 | Not Found | Resource doesn't exist |
| 405 | Method Not Allowed | Wrong HTTP method for endpoint |
| 409 | Conflict | Duplicate resource, version conflict |
| 422 | Unprocessable Entity | Valid syntax but semantic errors |
| 429 | Too Many Requests | Rate limit exceeded |

### Server Error (5xx)
| Code | Meaning | When |
|---|---|---|
| 500 | Internal Server Error | Unexpected server failure |
| 502 | Bad Gateway | Upstream service failure |
| 503 | Service Unavailable | Maintenance, overload |
| 504 | Gateway Timeout | Upstream service timeout |

## Error Response Format (RFC 9457 — Problem Details)
```json
{
  "type": "https://api.example.com/errors/validation",
  "title": "Validation Error",
  "status": 400,
  "detail": "The request body contains invalid fields.",
  "instance": "/users/123",
  "errors": [
    { "field": "email", "message": "Must be a valid email address", "code": "INVALID_FORMAT" },
    { "field": "age", "message": "Must be at least 18", "code": "MIN_VALUE" }
  ]
}
```

### Error Design Rules
```
1. Always return consistent error shape (same fields in every error)
2. Include machine-readable error code (INVALID_FORMAT, NOT_FOUND, etc.)
3. Include human-readable message for debugging
4. Never leak stack traces or internal details in production
5. Use appropriate HTTP status code
6. Log full error details server-side with request ID
7. Include request ID in response for support correlation
```

## Pagination
### Cursor-Based (Recommended)
```json
// GET /posts?limit=20&cursor=eyJpZCI6MTAwfQ
{
  "data": [...],
  "pagination": {
    "next_cursor": "eyJpZCI6MTIwfQ",
    "has_more": true
  }
}
```
| Pros | Cons |
|---|---|
| Stable with real-time data | Can't jump to arbitrary page |
| Performant (no OFFSET) | Opaque cursor (by design) |
| No duplicates/skips | Requires sorted field |

### Offset-Based
```json
// GET /posts?limit=20&offset=40
{
  "data": [...],
  "pagination": {
    "total": 500,
    "limit": 20,
    "offset": 40
  }
}
```
| Pros | Cons |
|---|---|
| Simple to implement | Slow at high offsets (DB performance) |
| Jump to any page | Duplicates/skips with concurrent writes |
| Familiar to clients | Requires total count query |

### Link Headers (HATEOAS)
```
Link: <https://api.example.com/posts?cursor=abc123>; rel="next",
      <https://api.example.com/posts?cursor=xyz789>; rel="prev"
```

## Versioning
| Strategy | Format | Pros | Cons |
|---|---|---|---|
| URL path | /api/v1/users | Explicit, easy routing | URL changes, cache issues |
| Header | Accept: application/vnd.api.v2+json | Clean URLs | Hidden, harder to test |
| Query param | /api/users?version=2 | Simple to add | Clutters query string |

### Recommended: URL Path Versioning
```
/api/v1/users — current stable
/api/v2/users — new version (breaking changes only)
Deprecation: X-API-Deprecated: true header + sunset date
```

### Breaking vs Non-Breaking Changes
| Breaking (new version) | Non-Breaking (same version) |
|---|---|
| Remove field | Add optional field |
| Rename field | Add new endpoint |
| Change field type | Add query parameter |
| Change error format | Deprecate (but keep) field |
| Change auth mechanism | Add response header |

## Request/Response Design
### Standard Response Envelope
```json
{
  "data": { ... },
  "meta": { "request_id": "req_abc123", "timestamp": "2024-01-15T10:30:00Z" }
}

// Collection response
{
  "data": [...],
  "pagination": { "next_cursor": "...", "has_more": true },
  "meta": { "request_id": "req_abc123", "total": 150 }
}
```

### Request Conventions
| Convention | Example |
|---|---|
| Query filtering | ?status=active&role=admin |
| Sorting | ?sort=created_at&order=desc or ?sort=-created_at |
| Field selection | ?fields=id,name,email |
| Search | ?q=search+term |
| Include relations | ?include=author,comments |
| Date filtering | ?created_after=2024-01-01&created_before=2024-02-01 |

## Rate Limiting
```
Headers to include in every response:
X-RateLimit-Limit: 100        — max requests per window
X-RateLimit-Remaining: 95     — remaining in current window
X-RateLimit-Reset: 1640995200 — window reset timestamp (Unix)
Retry-After: 60               — seconds to wait (on 429 response)
```

| Strategy | Best For |
|---|---|
| Fixed window | Simple, most APIs |
| Sliding window | More accurate rate control |
| Token bucket | Burst-friendly, API gateways |
| Per-user + per-IP | Prevent abuse from both authenticated and anonymous |

## Authentication Patterns
| Pattern | Use Case | Implementation |
|---|---|---|
| API Key | Server-to-server, simple apps | X-API-Key header or query param |
| Bearer Token (JWT) | User-facing APIs | Authorization: Bearer <token> |
| OAuth2 | Third-party integrations | Authorization code + PKCE |
| Session Cookie | Web apps, same-domain | HttpOnly, Secure, SameSite |

## OpenAPI / Swagger
```yaml
openapi: 3.1.0
info:
  title: My API
  version: 1.0.0
paths:
  /users:
    get:
      summary: List users
      parameters:
        - name: limit
          in: query
          schema: { type: integer, default: 20, maximum: 100 }
        - name: cursor
          in: query
          schema: { type: string }
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
                    items: { $ref: '#/components/schemas/User' }
                  pagination:
                    $ref: '#/components/schemas/CursorPagination'
```

### Code Generation
```
openapi-typescript: Generate TS types from spec
orval: Generate typed API client (fetch, axios, react-query)
zodios: Runtime validation from OpenAPI
Prism: Mock server from OpenAPI spec
```

## API Design Checklist
```
[ ] Resources are plural nouns, no verbs in URLs
[ ] Correct HTTP methods and status codes
[ ] Consistent error format with error codes
[ ] Pagination on all collection endpoints
[ ] Rate limiting with proper headers
[ ] Authentication on all non-public endpoints
[ ] Input validation with clear error messages
[ ] CORS configured for expected origins
[ ] Request/response logging with correlation IDs
[ ] OpenAPI spec maintained and up to date
[ ] Versioning strategy defined
[ ] Idempotency keys for non-idempotent operations
```
