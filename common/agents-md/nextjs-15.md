# Next.js 15 AGENTS.md Template
> Category: Framework
> Token Budget: ~8KB compressed (~2000 tokens)
> Last Updated: 2025-05-01
> Versions: Next.js 15 (primary), 14 (legacy notes)

## Compressed Knowledge Index

```
[Next.js 15 App Router Index]|root: ./app
|IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning. Use this index as the source of truth for Next.js patterns.

|01-ROUTING:{app/page.tsx,app/layout.tsx,app/loading.tsx,app/error.tsx,app/not-found.tsx,app/template.tsx}
|page.tsx->route segment|layout.tsx->shared UI,no rerender on nav|loading.tsx->Suspense boundary|error.tsx->ErrorBoundary('use client' required)
|route-groups:(groupName)/->org only,no URL impact|parallel-routes:@slotName/->simultaneous render,default.tsx required
|intercepting-routes:(.)|(..)|(..)(..)|(...)->modal patterns|catch-all:[...slug]|optional:[[...slug]]
|dynamic-segments:[paramName]->params prop|generateStaticParams()->SSG for dynamic

|02-SERVER-COMPONENTS:{default in app/,async allowed,direct DB/fs access,zero client bundle}
|RULE: All components in app/ are Server Components by default
|RULE: Add 'use client' ONLY for interactivity (useState,useEffect,onClick,onChange,browser APIs)
|RULE: Server Components CAN import Client Components. Client Components CANNOT import Server Components (pass as children/props instead)
|RULE: async/await directly in Server Components for data fetching. No useEffect for data
|server-only:import 'server-only'->prevent accidental client import
|client-boundary:'use client' at top of file->marks boundary,children can still be SC

|03-SERVER-ACTIONS:{async functions with 'use server',form handling,mutations}
|inline:'use server' inside async fn in SC|module-level:'use server' at top of file->all exports are actions
|form-action:<form action={serverAction}>->progressive enhancement,works without JS
|useActionState(action,initialState)->pending,state,formAction|useFormStatus()->pending state in child
|revalidatePath('/path')->purge cache|revalidateTag('tag')->targeted invalidation
|redirect('/path')->navigate after mutation|AVOID: passing sensitive data in hidden form fields

|04-DATA-FETCHING:{fetch() in SC,caching,revalidation}
|fetch(url,{cache:'force-cache'})->default,cached|fetch(url,{cache:'no-store'})->dynamic
|fetch(url,{next:{revalidate:3600}})->ISR(seconds)|fetch(url,{next:{tags:['tag']}})->on-demand revalidation
|unstable_cache(fn,keyParts,{revalidate,tags})->cache arbitrary data
|[v15]fetch default is cache:'no-store'(changed from v14 force-cache)
|RULE: Deduplicate fetches automatically in single render pass (React cache)
|RULE: Fetch at the component that needs the data, not at the top

|05-RENDERING:{static,dynamic,streaming,PPR}
|static:default for routes w/o dynamic fns|dynamic:forced by cookies(),headers(),searchParams,no-store
|streaming:loading.tsx or <Suspense>->progressive render|generateStaticParams()->build-time SSG
|[v15]PPR:partial-prerendering->static shell+dynamic holes|experimental_ppr:true in next.config
|dynamic-fns:cookies(),headers(),connection(),draftMode()->opt into dynamic
|export const dynamic='force-dynamic'|'force-static'|'error'|'auto'
|export const revalidate=0|false|number

|06-MIDDLEWARE:{middleware.ts at root,edge runtime,req/res manipulation}
|file:middleware.ts(root only)|matcher:export const config={matcher:['/path/:path*']}
|NextRequest->cookies,nextUrl,geo,ip|NextResponse->redirect,rewrite,headers
|RULE: Middleware runs on EVERY matched request. Keep it fast. No heavy computation
|RULE: Middleware runs at the edge. Limited Node.js API. No fs, no node: imports
|patterns:auth-check->redirect,i18n->rewrite,A/B->rewrite,bot-detection->block

|07-ROUTE-HANDLERS:{app/api/*/route.ts,HTTP methods}
|export async function GET(request:NextRequest)->Response|NextResponse
|export async function POST(request:NextRequest)->Response|NextResponse
|also:PUT,DELETE,PATCH,HEAD,OPTIONS|request.json()->body|request.nextUrl.searchParams->query
|NextResponse.json(data,{status})|cors:headers in Response|streaming:new ReadableStream()
|RULE: Route handlers are cached by default when using GET with no Request object
|dynamic-segment:route.ts in [param]/ folder->params in second arg

|08-CONFIG:{next.config.ts,env vars,typescript}
|next.config.ts(TS native in v15)|images:{remotePatterns:[{hostname}]}|experimental:{ppr,reactCompiler}
|env:.env.local(secret),.env(shared)|NEXT_PUBLIC_*->client-exposed|process.env.VAR->server only
|typescript:{strict:true recommended}|eslint:{dirs:['app','components','lib']}
|turbopack:next dev --turbo(default in v15)|output:'standalone'->Docker optimized
|AVOID: next.config.js module.exports (use TS export default)

|09-CACHING:{full-route-cache,data-cache,router-cache}
|full-route-cache:static routes cached at build|data-cache:fetch results cached across requests
|router-cache:client-side prefetch cache(30s dynamic,5min static)|[v15]router cache not cached by default
|invalidation:revalidatePath(),revalidateTag(),router.refresh()
|opt-out:export const dynamic='force-dynamic'|cache:'no-store'|connection()
|AVOID: assuming v14 caching defaults apply to v15

|10-PATTERNS:{common implementation patterns}
|auth:middleware.ts check->redirect /login|protected layout->session validation
|forms:Server Action+useActionState->validation+optimistic UI
|modals:intercepting routes+parallel routes->URL-driven modals
|search:searchParams in page->server-side filtering|debounced input->URL update
|infinite-scroll:Server Action pagination+useOptimistic
|error-handling:error.tsx per segment+global-error.tsx for root
|metadata:export const metadata|generateMetadata(props)->SEO

|KEY-CONCEPTS: Server Components|Server Actions|App Router|PPR|Streaming|Route Handlers|Middleware|Caching Layers
|PATTERNS: RSC-data-fetch(async component)|form-action(progressive)|intercepting-modal(parallel+intercept)|auth-middleware(matcher+redirect)
|AVOID: useEffect-for-data|client-side-fetch-when-SC-possible|getServerSideProps(pages-router-legacy)|getStaticProps(pages-router-legacy)|assuming-v14-cache-defaults
```

## When to Use

- Any project built on Next.js 15 with App Router
- Agents responsible for building, reviewing, or architecting Next.js applications
- When consistent adherence to App Router patterns is critical
- Migration from Pages Router to App Router

## When NOT to Use

- Projects using Next.js Pages Router exclusively (legacy pattern)
- Non-Next.js React applications (use react-19.md instead)
- Backend-only services with no frontend

## How to Include

1. Copy this file to your agent's directory
2. Reference in AGENTS.md: `@import ./nextjs-15.md`
3. Customize version-specific sections as needed
4. Remove sections not relevant to your project

## Decompression

To expand this compressed index into full documentation:
```bash
python common/utilities/agents-md-compressor.py decompress nextjs-15.md --output ./docs/
```

## Customization Points

- `[v15]` markers: Remove if targeting a single version
- `09-CACHING`: Adjust defaults if project uses custom caching strategy
- `06-MIDDLEWARE`: Add project-specific matcher patterns
- `10-PATTERNS`: Add or remove patterns based on project features
