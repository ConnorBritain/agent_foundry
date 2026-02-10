# Security — Compressed AGENTS.md Knowledge

## Quick Reference
| Area | Key Concepts |
|---|---|
| OWASP Top 10 | Injection, broken auth, XSS, SSRF, misconfiguration |
| Authentication | Password hashing, MFA, session management, JWT security |
| Input Validation | Server-side validation, sanitization, parameterized queries |
| CORS | Origin allowlists, preflight, credentials, methods |
| CSP | Content-Security-Policy headers, nonces, report-uri |
| Headers | Security headers, HSTS, X-Frame-Options, referrer policy |

## OWASP Top 10 (2021) — Web Application Security
| # | Risk | Prevention |
|---|---|---|
| A01 | Broken Access Control | Deny by default, validate server-side, RBAC, RLS |
| A02 | Cryptographic Failures | TLS everywhere, strong hashing, no secrets in code |
| A03 | Injection | Parameterized queries, ORM, input validation, no eval() |
| A04 | Insecure Design | Threat modeling, secure defaults, principle of least privilege |
| A05 | Security Misconfiguration | Hardened defaults, no default creds, error handling |
| A06 | Vulnerable Components | Dependency scanning, npm audit, auto-updates |
| A07 | Auth & Identity Failures | MFA, strong passwords, rate limiting, secure sessions |
| A08 | Software & Data Integrity | Verify dependencies, CI/CD security, signed artifacts |
| A09 | Security Logging Failures | Log auth events, detect anomalies, don't log secrets |
| A10 | SSRF | Allowlist URLs, validate redirects, block internal IPs |

## Authentication Security
### Password Handling
```
NEVER: store plaintext, MD5, SHA-1/256 alone
ALWAYS: bcrypt (cost 12+), scrypt, or Argon2id

// bcrypt example
import bcrypt from 'bcryptjs';
const hash = await bcrypt.hash(password, 12);
const valid = await bcrypt.compare(password, hash);
```

| Rule | Implementation |
|---|---|
| Min password length | 8+ characters (NIST recommends 8-64) |
| Breach check | Check against HaveIBeenPwned API |
| No complexity rules | NIST 800-63b: length > complexity rules |
| Rate limit login | 5 attempts per 15 min, then lockout/CAPTCHA |
| Timing-safe compare | Use crypto.timingSafeEqual for token comparison |

### Session Management
```
HttpOnly cookies: prevent JS access (XSS protection)
Secure flag: HTTPS only
SameSite=Lax: CSRF protection (Strict for high-security)
Max-Age: set reasonable expiry (1hr access, 7d refresh)
Rotate session ID on login: prevent session fixation
Invalidate on logout: destroy server-side session
```

### JWT Security
| Rule | Detail |
|---|---|
| Short expiry | Access tokens: 15min-1hr |
| Refresh tokens | Longer-lived, stored HttpOnly, single-use rotation |
| Signing | RS256 (asymmetric) for distributed systems, HS256 for single server |
| Validation | Always verify signature, exp, iss, aud claims |
| Never in localStorage | XSS can steal tokens — use HttpOnly cookies |
| Never in URL | Tokens in URLs leak via referrer headers and logs |

## Input Validation
### Server-Side Validation (Zod)
```typescript
import { z } from 'zod';

const createUserSchema = z.object({
  email: z.string().email().max(255).toLowerCase().trim(),
  name: z.string().min(1).max(100).trim(),
  age: z.number().int().min(13).max(150),
  role: z.enum(['user', 'admin']).default('user'),
  bio: z.string().max(1000).optional(),
});

// In API route
const result = createUserSchema.safeParse(await request.json());
if (!result.success) {
  return Response.json({ errors: result.error.flatten() }, { status: 400 });
}
const validData = result.data; // fully typed and sanitized
```

### Validation Rules
```
1. ALWAYS validate on server (client validation is UX, not security)
2. Validate type, length, range, format, allowed values
3. Reject unexpected fields (strict schemas)
4. Sanitize for output context (HTML encoding, SQL parameterization)
5. Use allowlists over denylists when possible
6. Validate file uploads: type, size, extension, content-type
```

### SQL Injection Prevention
```
NEVER: string concatenation in queries
ALWAYS: parameterized queries or ORM

// Parameterized (safe)
db.query('SELECT * FROM users WHERE id = $1', [userId]);

// ORM (safe)
db.user.findUnique({ where: { id: userId } });

// DANGEROUS — never do this
db.query(`SELECT * FROM users WHERE id = '${userId}'`);
```

## XSS (Cross-Site Scripting) Prevention
| Type | Attack | Prevention |
|---|---|---|
| Stored XSS | Malicious script saved in DB, rendered to others | Sanitize input, encode output |
| Reflected XSS | Script in URL/params reflected in page | Encode URL params in output |
| DOM XSS | Client-side JS inserts untrusted data into DOM | Avoid innerHTML, use textContent |

```
React: auto-escapes JSX output (safe by default)
DANGER: dangerouslySetInnerHTML — sanitize with DOMPurify first
DANGER: href={userInput} — validate URL scheme (no javascript:)
```

### Content-Security-Policy (CSP)
```
Content-Security-Policy:
  default-src 'self';
  script-src 'self' 'nonce-{random}';
  style-src 'self' 'unsafe-inline';
  img-src 'self' data: https:;
  font-src 'self';
  connect-src 'self' https://api.example.com;
  frame-ancestors 'none';
  base-uri 'self';
  form-action 'self';
```

| Directive | Controls |
|---|---|
| default-src | Fallback for all resource types |
| script-src | JavaScript sources (use nonce for inline) |
| style-src | CSS sources |
| img-src | Image sources |
| connect-src | fetch/XHR/WebSocket destinations |
| frame-ancestors | Who can embed this page (replaces X-Frame-Options) |
| report-uri | Where to send CSP violation reports |

### Nonce-Based CSP (Next.js)
```typescript
// middleware.ts
const nonce = crypto.randomUUID();
const csp = `script-src 'self' 'nonce-${nonce}'; ...`;
// Pass nonce to components for inline scripts
<Script nonce={nonce} src="..." />
```

## CORS (Cross-Origin Resource Sharing)
```typescript
// Strict CORS configuration
const allowedOrigins = ['https://app.example.com', 'https://admin.example.com'];

function corsHeaders(origin: string | null) {
  if (origin && allowedOrigins.includes(origin)) {
    return {
      'Access-Control-Allow-Origin': origin, // specific origin, not *
      'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type, Authorization',
      'Access-Control-Allow-Credentials': 'true', // if using cookies
      'Access-Control-Max-Age': '86400', // cache preflight for 24hr
    };
  }
  return {}; // no CORS headers = browser blocks request
}
```

| Rule | Detail |
|---|---|
| Never use origin: * with credentials | Browsers reject this combination |
| Allowlist origins | Don't reflect Origin header blindly |
| Limit methods | Only allow methods your API uses |
| Limit headers | Only allow headers your API expects |
| Preflight caching | Max-Age reduces OPTIONS requests |

## Security Headers
```
// Recommended headers for all responses
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: camera=(), microphone=(), geolocation=()
X-XSS-Protection: 0  (deprecated, but set to 0 to avoid quirks)
```

### Next.js Security Headers
```javascript
// next.config.js
const securityHeaders = [
  { key: 'Strict-Transport-Security', value: 'max-age=63072000; includeSubDomains; preload' },
  { key: 'X-Content-Type-Options', value: 'nosniff' },
  { key: 'X-Frame-Options', value: 'DENY' },
  { key: 'Referrer-Policy', value: 'strict-origin-when-cross-origin' },
];
module.exports = {
  async headers() {
    return [{ source: '/(.*)', headers: securityHeaders }];
  },
};
```

## Secrets Management
```
NEVER: commit secrets to git, hardcode in source, log secrets
ALWAYS: use environment variables, secret managers, .env in .gitignore
```

| Tool | Use Case |
|---|---|
| .env.local | Local development (in .gitignore) |
| Vercel env vars | Production deployment |
| GitHub Secrets | CI/CD workflows |
| AWS Secrets Manager / Vault | Enterprise secret rotation |

## Dependency Security
```bash
npm audit                          # Check for known vulnerabilities
npm audit fix                      # Auto-fix compatible updates
npx npm-check-updates -u           # Update to latest versions
```

| Practice | Detail |
|---|---|
| Lock files | Commit package-lock.json / pnpm-lock.yaml |
| Dependabot | Auto-create PRs for vulnerable dependencies |
| Minimal deps | Fewer dependencies = smaller attack surface |
| Review new deps | Check maintenance, popularity, security history |
| Pin versions | Exact versions in production, ranges in libraries |

## Security Checklist
```
[ ] HTTPS everywhere (HSTS enabled)
[ ] Authentication: bcrypt/argon2, rate limiting, MFA option
[ ] Authorization: deny by default, validate on every request
[ ] Input validation: server-side with strict schemas
[ ] SQL injection: parameterized queries only
[ ] XSS: CSP headers, output encoding, no dangerouslySetInnerHTML
[ ] CORS: allowlisted origins, no wildcard with credentials
[ ] CSRF: SameSite cookies, CSRF tokens for forms
[ ] Secrets: env vars, not in code, rotated regularly
[ ] Dependencies: audited, updated, minimal
[ ] Security headers: full set configured
[ ] Logging: auth events logged, secrets never logged
[ ] Error handling: generic messages to client, details server-side
```
