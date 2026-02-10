# Example: Internal Tool — Team Dashboard

## Project Overview

Build "PulseBoard" — an internal dashboard for a 30-person startup to track KPIs, team OKRs, and operational metrics. No public users, no payments, no marketing site.

## Configuration

```yaml
project_type: internal_tool
target_audience: b2b  # Internal use only
auth_strategy: oauth_only  # Google Workspace SSO only
payment_model: none  # No payment processing needed
deployment_region: us_east
stack:
  frontend_framework: nextjs
  backend: supabase
  hosting: vercel
  database: supabase_postgres
  auth_provider: supabase_auth  # Google OAuth restricted to company domain
  payment_provider: none
```

## Simplified Team Allocation

Since there's no marketing site, payments, or revenue operations:
- **Marketing Frontend**: Not needed (skip or reassign to dashboards)
- **RevOps**: Not needed (skip entirely)
- **QA/Test**: Lighter scope (no payment flows to test)

Effective team: **4 agents** (Coordinator, Senior Full-Stack, Cloud/DevOps, Database Engineer)

## What Changes

### Auth is Domain-Restricted
```typescript
// Only allow @company.com Google accounts
const { data, error } = await supabase.auth.signInWithOAuth({
  provider: 'google',
  options: {
    queryParams: { hd: 'company.com' }  // Restrict to domain
  }
})
```

### No Marketing Site
- Skip landing page, pricing, SEO, conversion tracking
- Single app at `pulse.company.com`
- Internal documentation only

### No Payments
- No Stripe integration
- No subscription tiers or feature gating
- All authenticated users get full access
- Role-based access: Admin, Manager, Viewer (via RLS)

### Dashboard-Focused Features
- **KPI widgets**: Revenue (from external API), active users, NPS score
- **OKR tracker**: Company → Team → Individual goal progress
- **Team directory**: Who's working on what, availability
- **Incident log**: Current issues and status
- **Data sources**: Pull from Google Sheets, Stripe API, Linear API via Edge Functions

## Phase Highlights

### Phase 1: Foundation (~20 min)
- Coordinator: Define data sources, widget types, role permissions
- Cloud/DevOps: Supabase + Vercel setup, domain-restricted auth
- Database Engineer: Schema for KPIs, OKRs, team data
- Senior Full-Stack: Next.js scaffold with dashboard layout

### Phase 2: Core Features (~40 min)
- Senior Full-Stack: Dashboard grid with draggable widgets, OKR tree view
- Database Engineer: Edge Functions to sync external data (hourly cron)
- Cloud/DevOps: Scheduled Edge Function triggers, env config

### Phase 3: Polish (~20 min)
- Senior Full-Stack: Real-time updates via Supabase Realtime
- Database Engineer: Role-based RLS (Admins can edit, Viewers read-only)
- Cloud/DevOps: Production deploy, basic monitoring

## Cost Summary

| Phase | Notes | Cost |
|-------|-------|------|
| Foundation | Simpler (no marketing, no payments) | $12 |
| Core Features | Dashboard widgets, data sync | $30 |
| Polish | Real-time, roles, deploy | $10 |
| **Total** | | **~$52** |

~50% cheaper than the SaaS starter since 3 agents are not needed and scope is smaller.
