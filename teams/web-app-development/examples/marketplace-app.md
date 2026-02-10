# Example: Marketplace App — Freelancer Platform

## Project Overview

Build "SkillBridge" — a two-sided marketplace connecting freelance designers with small businesses. Features: freelancer profiles, project posting, proposal system, escrow payments, reviews.

## Configuration

```yaml
project_type: marketplace
target_audience: b2b2c
auth_strategy: email_magic_link
payment_model: usage_based  # 10% platform fee per transaction
deployment_region: us_east
stack:
  frontend_framework: nextjs
  backend: supabase
  hosting: vercel
  database: supabase_postgres
  auth_provider: supabase_auth
  payment_provider: stripe  # Stripe Connect for marketplace
```

## Key Differences from SaaS Starter

### Two-Sided Data Model
- **Clients**: Post projects, review proposals, release payments
- **Freelancers**: Create profiles, submit proposals, deliver work
- Both roles use the same auth but see different dashboards

### Stripe Connect (not standard Stripe)
- RevOps configures Stripe Connect for marketplace payments
- Freelancers onboard via Stripe Connect Express accounts
- Platform collects 10% fee on each transaction
- Escrow: funds held until client approves deliverable

### Search & Discovery
- Senior Full-Stack builds freelancer search with filters (skill, rate, availability)
- Database Engineer implements full-text search with `tsvector` in Postgres
- Marketing Frontend builds SEO-optimized freelancer profile pages (public)

### Trust & Safety
- QA/Test focuses on payment escrow edge cases
- Database Engineer implements review/rating system with RLS
- Cloud/DevOps adds rate limiting and abuse detection

## Phase Highlights

### RevOps Handles Complex Payment Flow
1. Client posts project with budget ($500-$5,000)
2. Freelancer submits proposal
3. Client accepts → Stripe creates PaymentIntent (held, not captured)
4. Freelancer delivers → Client approves → Payment captured
5. Platform takes 10% fee, freelancer receives 90% to their Connect account
6. Dispute flow: 7-day window for client to raise issues

### Database Engineer Designs for Scale
- Partitioned `proposals` table (by status: active, accepted, completed)
- Materialized views for freelancer search rankings
- Connection pooling configured for concurrent marketplace activity

## Cost Summary

| Phase | Notes | Cost |
|-------|-------|------|
| Foundation | Stripe Connect adds complexity | $25 |
| Core Features | Two dashboards, search, profiles | $50 |
| Integration & Revenue | Escrow payments, Connect onboarding | $40 |
| Launch Prep | Extensive payment edge case testing | $20 |
| **Total** | | **~$135** |

Higher than SaaS starter due to Stripe Connect complexity and two-sided UX.
