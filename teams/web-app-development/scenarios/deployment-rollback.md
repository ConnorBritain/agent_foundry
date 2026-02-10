# Scenario: Deployment Rollback

## Overview

A production deployment introduces a critical bug. The team must detect, respond, rollback, verify recovery, and conduct a post-mortem.

## Trigger

Cloud/DevOps Engineer merges PR to `main`, triggering production deployment via GitHub Actions.

## Phase 1: Deployment

1. GitHub Actions pipeline runs: lint, test, build
2. All checks pass
3. Vercel deploys new version to production
4. Cloud/DevOps posts to cross-team communication: "v1.4.2 deployed to production"

## Phase 2: Detection (~5 minutes post-deploy)

### Automated Signals
- Sentry: Error rate spikes from 0.1% to 12%
- Vercel Analytics: p95 response time jumps from 200ms to 3,200ms
- Stripe webhook handler: 504 Gateway Timeout errors logged
- QA/Test: Synthetic monitoring (Playwright health check) fails

### Alert Chain
1. Sentry fires alert → Slack notification
2. Vercel deployment status shows degraded performance
3. QA/Test automated health check returns HTTP 500 on `/api/webhooks/stripe`

## Phase 3: Assessment (~2 minutes)

Coordinator triages:

1. **Scope**: Stripe webhook endpoint is crashing — payment processing is down
2. **Impact**: New subscriptions and payment updates are failing
3. **Root cause**: New middleware introduced in v1.4.2 breaks JSON body parsing for webhook signature verification
4. **Decision**: Rollback immediately (do NOT attempt hotfix in production)

## Phase 4: Rollback (~1 minute)

### Vercel Instant Rollback
```bash
# Vercel supports instant rollback to previous deployment
vercel rollback --yes
```

1. Cloud/DevOps initiates Vercel instant rollback to v1.4.1
2. Previous deployment is promoted to production
3. DNS/edge propagation: <30 seconds
4. No database rollback needed (schema unchanged in v1.4.2)

### Verification Checklist
- [ ] Health endpoint returns 200
- [ ] Stripe webhook test event succeeds
- [ ] Sentry error rate returns to baseline
- [ ] Vercel response times normalize
- [ ] QA/Test synthetic monitoring passes
- [ ] Manual test: complete a test subscription flow

## Phase 5: Recovery Verification (~10 minutes)

1. QA/Test runs full Playwright E2E suite against production
2. RevOps sends Stripe test webhook, confirms processing
3. Cloud/DevOps monitors error rates for 10 minutes
4. Coordinator confirms: "Production stable on v1.4.1"

### Stripe Webhook Replay
```
# Replay any webhooks that failed during the outage window
# Stripe automatically retries failed webhooks, but verify:
1. Check Stripe Dashboard → Webhooks → Recent deliveries
2. Identify events with 504 status during outage window
3. Stripe will auto-retry these (up to 3 days)
4. Monitor for successful delivery of retried events
5. Verify database records match Stripe state
```

## Phase 6: Post-Mortem (~30 minutes)

### Incident Timeline
| Time | Event |
|------|-------|
| 14:00 | PR merged to main |
| 14:03 | Deployment complete |
| 14:08 | Sentry alert fires |
| 14:10 | Coordinator assesses impact |
| 14:11 | Rollback initiated |
| 14:12 | Rollback complete |
| 14:22 | All checks passing, production stable |

### Root Cause
New authentication middleware was applied globally instead of selectively. It consumed the raw request body before the Stripe webhook handler could read it for signature verification.

### What Went Wrong
1. Middleware was not tested with Stripe webhook payloads
2. E2E tests did not include webhook signature verification
3. No canary deployment to catch the issue before full rollout

### Action Items
- [ ] Add Playwright test for Stripe webhook with valid signature
- [ ] Implement canary deployments (10% traffic for 5 minutes before full rollout)
- [ ] Exclude `/api/webhooks/*` routes from body-parsing middleware
- [ ] Add specific monitoring alert for webhook endpoint error rates
- [ ] Update deployment checklist to include webhook verification

### Prevention Measures
- [ ] Configure Vercel deployment protection (require approval for production)
- [ ] Add pre-deployment webhook smoke test to GitHub Actions
- [ ] Implement feature flags for middleware changes

## Success Criteria

- **Detection time**: <10 minutes from deployment
- **Rollback time**: <2 minutes from decision
- **Total downtime**: <15 minutes
- **Data loss**: Zero (Stripe retries failed webhooks)
- **Customer impact**: Minimal (subscriptions delayed, not lost)
- **Post-mortem completed**: Within 24 hours
- **Action items assigned**: Within 48 hours
