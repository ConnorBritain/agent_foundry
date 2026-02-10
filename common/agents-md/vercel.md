# Vercel — Compressed AGENTS.md Knowledge

## Quick Reference
| Area | Key Concepts |
|---|---|
| Deployment | Git-based, preview/production, build settings, monorepo support |
| Edge Functions | Edge Runtime, middleware, geolocation, streaming |
| Serverless | Node.js functions, cold starts, timeouts, memory limits |
| Environment | Variables, secrets, per-branch overrides, system env vars |
| Domains | Custom domains, DNS, SSL, redirects, rewrites |
| Analytics | Web Vitals, speed insights, audience, real-time logs |

## Project Structure & Deployment
```
Git push → Vercel auto-deploys:
  main/master → Production deployment (production URL)
  other branches → Preview deployment (unique URL per commit)
  PR → Preview + comment with deploy URL
```

| Setting | Location |
|---|---|
| Framework preset | Auto-detected (Next.js, Vite, etc.) or manual in vercel.json |
| Build command | Override: vercel.json > buildCommand or dashboard settings |
| Output directory | Auto-detected or override: outputDirectory |
| Root directory | For monorepos: set project root in dashboard or vercel.json |
| Install command | Default: npm install / yarn / pnpm install (auto-detected) |

### vercel.json Configuration
```json
{
  "framework": "nextjs",
  "buildCommand": "pnpm build",
  "regions": ["iad1"],
  "headers": [
    { "source": "/api/(.*)", "headers": [{ "key": "Cache-Control", "value": "no-store" }] }
  ],
  "redirects": [
    { "source": "/old-path", "destination": "/new-path", "permanent": true }
  ],
  "rewrites": [
    { "source": "/api/:path*", "destination": "https://backend.example.com/:path*" }
  ]
}
```

## Environment Variables
| Scope | Visibility |
|---|---|
| Production | Only production deployments |
| Preview | Only preview deployments (PR/branch) |
| Development | Only vercel dev local |
| NEXT_PUBLIC_* | Exposed to client bundle (inlined at build time) |
| Non-prefixed | Server-only (API routes, server components, middleware) |

### System Environment Variables
```
VERCEL=1 — running on Vercel
VERCEL_ENV=production|preview|development
VERCEL_URL=deployment-url.vercel.app (no protocol)
VERCEL_GIT_COMMIT_SHA — current commit hash
VERCEL_GIT_COMMIT_REF — branch name
VERCEL_REGION — function execution region
```

### CLI Management
```bash
vercel env pull .env.local          # Pull all dev env vars
vercel env add VARIABLE_NAME        # Add new variable (interactive)
vercel env rm VARIABLE_NAME         # Remove variable
vercel env ls                       # List all variables
```

## Edge Functions & Middleware
### Middleware (Next.js)
```typescript
// middleware.ts at project root
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  // Geolocation
  const country = request.geo?.country;
  const city = request.geo?.city;
  // IP
  const ip = request.ip;
  // Rewrite/redirect
  if (country === 'CN') return NextResponse.redirect('/cn');
  // Add headers
  const response = NextResponse.next();
  response.headers.set('x-region', country ?? 'unknown');
  return response;
}

export const config = { matcher: ['/((?!_next/static|favicon.ico).*)'] };
```

### Edge Runtime for API Routes
```typescript
export const runtime = 'edge'; // opt into edge runtime
export async function GET(request: Request) {
  return new Response(JSON.stringify({ region: process.env.VERCEL_REGION }));
}
```

| Feature | Edge Runtime | Node.js Runtime |
|---|---|---|
| Cold start | ~0ms | 250ms+ |
| Max duration | 30s (hobby) / 5min (pro) | 10s (hobby) / 60s (pro) / 300s (enterprise) |
| Max size | 1MB (after compression) | 50MB |
| APIs | Web standard (fetch, Response) | Full Node.js |
| Use when | Low latency, geolocation, auth checks | Heavy computation, native modules |

## Serverless Functions
```
Location: app/api/*/route.ts (App Router) or pages/api/*.ts (Pages Router)
Regions: defaults to iad1 (US East), configurable per-function or project-wide
Memory: 1024MB default, up to 3008MB
```

| Config | How |
|---|---|
| Timeout | export const maxDuration = 30; (in seconds, per function) |
| Region | export const preferredRegion = 'sfo1'; |
| Runtime | export const runtime = 'nodejs'; // or 'edge' |
| Dynamic | export const dynamic = 'force-dynamic'; // skip cache |

## Caching & Performance
| Layer | Control |
|---|---|
| CDN / Edge Cache | Cache-Control headers, s-maxage for shared cache |
| ISR | revalidate: 60 in fetch or page config — revalidate every 60s |
| On-demand ISR | revalidatePath('/path') or revalidateTag('tag') from server action |
| Static | export const dynamic = 'force-static' or generateStaticParams |
| No cache | export const dynamic = 'force-dynamic' or no-store in fetch |

### Cache Headers Pattern
```
Static assets: public, max-age=31536000, immutable (_next/static)
API responses: s-maxage=60, stale-while-revalidate=300
HTML pages: s-maxage=3600 with on-demand revalidation
Private data: private, no-store, no-cache
```

## Domains & DNS
```bash
vercel domains add example.com       # Add custom domain
vercel domains ls                    # List domains
vercel certs ls                      # List SSL certificates
```

| Record | Value |
|---|---|
| A record | 76.76.21.21 (for apex domain) |
| CNAME | cname.vercel-dns.com (for subdomains) |
| Nameservers | ns1.vercel-dns.com, ns2.vercel-dns.com (for Vercel DNS) |

## Monorepo Support
```
Turborepo (recommended): turbo.json defines pipeline
Root vercel.json with project-level overrides
Each project: set root directory in Vercel dashboard
Ignored Build Step: vercel.json > ignoreCommand or git diff detection
```

### Turborepo Integration
```json
// turbo.json
{
  "pipeline": {
    "build": { "dependsOn": ["^build"], "outputs": [".next/**", "dist/**"] },
    "lint": {},
    "test": { "dependsOn": ["build"] }
  }
}
```

## Analytics & Monitoring
| Tool | Purpose |
|---|---|
| Speed Insights | Core Web Vitals (LCP, FID, CLS, TTFB, INP) per route |
| Web Analytics | Page views, visitors, referrers, country (privacy-focused) |
| Logs | Real-time function logs, build logs, access logs |
| Checks | Custom deployment checks via API (integration point) |

```typescript
// Enable Speed Insights
import { SpeedInsights } from '@vercel/speed-insights/next';
// In layout: <SpeedInsights />

// Enable Analytics
import { Analytics } from '@vercel/analytics/react';
// In layout: <Analytics />
```

## CLI Commands
| Command | Purpose |
|---|---|
| vercel | Deploy current directory (interactive) |
| vercel --prod | Deploy to production |
| vercel dev | Run local dev with Vercel env vars |
| vercel build | Test build locally |
| vercel logs <url> | Stream deployment logs |
| vercel inspect <url> | Show deployment details |
| vercel promote <deployment> | Promote preview to production |
| vercel rollback | Rollback production to previous |

## Gotchas & Best Practices
| Issue | Solution |
|---|---|
| Build env vars missing | Env vars must exist at build time for NEXT_PUBLIC_* |
| Function timeout | Increase maxDuration, move heavy work to background (queue) |
| Cold starts | Use edge runtime or keep functions warm with cron |
| 4MB response limit | Stream large responses, use external storage for files |
| Preview env leaks | Use separate Stripe test keys, DB branches for preview |
| CORS on API routes | Set headers manually; Vercel doesn't add CORS by default |
| Monorepo builds | Use ignoreCommand to skip unchanged projects |
