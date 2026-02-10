# Supabase — Compressed AGENTS.md Knowledge

## Quick Reference
| Area | Key Concepts |
|---|---|
| Auth | email/pw, OAuth, magic link, phone OTP, PKCE flow, session management |
| Database | Postgres 15+, schemas, migrations, triggers, functions, extensions |
| RLS | Row Level Security policies, auth.uid(), service_role bypass |
| Storage | Buckets, policies, signed URLs, transformations, resumable uploads |
| Edge Functions | Deno runtime, JWT verification, secrets, CORS, invocation |
| Realtime | Postgres changes, broadcast, presence, channels |

## Authentication Patterns
```
Client setup: createBrowserClient() for CSR | createServerClient() for SSR
PKCE flow: default for SSR — uses code exchange instead of implicit tokens
Session: access_token (JWT, 1hr) + refresh_token — auto-refresh via onAuthStateChange
```

| Pattern | Implementation |
|---|---|
| Email/Password | supabase.auth.signUp({ email, password }) → confirm via email link |
| OAuth | supabase.auth.signInWithOAuth({ provider: 'github' }) → redirect flow |
| Magic Link | supabase.auth.signInWithOtp({ email }) → link sent, no password |
| Phone OTP | supabase.auth.signInWithOtp({ phone }) → verify with token |
| Sign Out | supabase.auth.signOut() → clears session, triggers onAuthStateChange |
| Get User | supabase.auth.getUser() — server-verified | getSession() — client cached |

### Auth Middleware (Next.js)
```
middleware.ts: createServerClient → getUser() → redirect if !user
Must pass cookies via { get, set, remove } adapter for request/response
Always use getUser() not getSession() for server-side auth checks (JWT verified)
```

## Database & Migrations
| Command | Purpose |
|---|---|
| supabase db diff -f migration_name | Generate migration from schema changes |
| supabase migration new name | Create empty migration file |
| supabase db push | Apply migrations to remote |
| supabase db reset | Reset local DB, rerun all migrations |

### Schema Conventions
```
Tables: snake_case plural (user_profiles, team_members)
Columns: snake_case (created_at, updated_at, deleted_at for soft delete)
PKs: id uuid DEFAULT gen_random_uuid()
Timestamps: created_at timestamptz DEFAULT now(), updated_at via trigger
Foreign keys: reference_table_id (e.g., user_id, team_id)
```

### Common Trigger Pattern
```sql
CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$ BEGIN
  NEW.updated_at = now(); RETURN NEW;
END; $$ LANGUAGE plpgsql;

CREATE TRIGGER set_updated_at BEFORE UPDATE ON table_name
  FOR EACH ROW EXECUTE FUNCTION update_updated_at();
```

## Row Level Security (RLS)
```
CRITICAL: Enable RLS on ALL tables exposed to client
ALTER TABLE table_name ENABLE ROW LEVEL SECURITY;
Without policies: RLS enabled = zero access (deny all by default)
service_role key bypasses RLS — NEVER expose to client
```

| Policy Pattern | SQL Template |
|---|---|
| Users own rows | USING (auth.uid() = user_id) |
| Team access | USING (team_id IN (SELECT team_id FROM team_members WHERE user_id = auth.uid())) |
| Public read | FOR SELECT USING (true) |
| Insert own | FOR INSERT WITH CHECK (auth.uid() = user_id) |
| Admin full | USING (auth.uid() IN (SELECT user_id FROM admins)) |

### RLS Debugging
```
Check: SELECT * FROM pg_policies WHERE tablename = 'your_table';
Test as user: SET request.jwt.claims = '{"sub":"user-uuid"}';
Common mistake: forgetting WITH CHECK on INSERT/UPDATE (separate from USING)
```

## Storage
| Operation | Method |
|---|---|
| Upload | supabase.storage.from('bucket').upload(path, file, { upsert: true }) |
| Download | supabase.storage.from('bucket').download(path) |
| Public URL | supabase.storage.from('bucket').getPublicUrl(path) |
| Signed URL | supabase.storage.from('bucket').createSignedUrl(path, expiresIn) |
| Delete | supabase.storage.from('bucket').remove([path1, path2]) |
| List | supabase.storage.from('bucket').list(folder, { limit, offset, sortBy }) |

### Storage Policies
```
Bucket: public (no auth for reads) vs private (auth required for all)
Policies: same RLS syntax — storage.objects table, bucket_id + name columns
Path convention: user_id/folder/filename for per-user isolation
Size limits: set per bucket, enforce via policy or client validation
```

## Edge Functions
```
Location: supabase/functions/function-name/index.ts
Runtime: Deno — use npm: prefix for Node packages (import x from "npm:package")
Deploy: supabase functions deploy function-name
Secrets: supabase secrets set KEY=value → Deno.env.get("KEY")
```

### Edge Function Template
```typescript
import { createClient } from "npm:@supabase/supabase-js@2";
Deno.serve(async (req) => {
  // CORS headers for browser calls
  if (req.method === "OPTIONS") return new Response(null, { headers: corsHeaders });
  // Verify JWT from Authorization header
  const supabase = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_ANON_KEY")!, {
    global: { headers: { Authorization: req.headers.get("Authorization")! } }
  });
  const { data: { user } } = await supabase.auth.getUser();
  if (!user) return new Response("Unauthorized", { status: 401 });
  // Business logic here
  return new Response(JSON.stringify({ ok: true }), {
    headers: { ...corsHeaders, "Content-Type": "application/json" }
  });
});
```

## Realtime
| Channel Type | Use Case |
|---|---|
| postgres_changes | Listen to INSERT/UPDATE/DELETE on tables (requires RLS) |
| broadcast | Pub/sub between clients (low latency, ephemeral) |
| presence | Track online users, shared cursors, typing indicators |

```
Subscribe: supabase.channel('room').on('postgres_changes', { event: '*', schema: 'public', table: 'messages' }, handler).subscribe()
Unsubscribe: supabase.removeChannel(channel)
Filter: filter: 'room_id=eq.123' for targeted subscriptions
```

## Performance & Gotchas
| Issue | Solution |
|---|---|
| N+1 queries | Use select('*, relation(*)') for joins via PostgREST |
| Missing indexes | Add indexes on FK columns and frequently filtered columns |
| RLS perf | Avoid subqueries in policies — use security definer functions |
| Type safety | Generate types: supabase gen types typescript --project-id X > types/supabase.ts |
| Local dev | supabase start → local Postgres + Auth + Storage + Edge Runtime |
| Env vars | NEXT_PUBLIC_SUPABASE_URL + NEXT_PUBLIC_SUPABASE_ANON_KEY (safe for client) |
| Service role | SUPABASE_SERVICE_ROLE_KEY — server only, bypasses RLS |
