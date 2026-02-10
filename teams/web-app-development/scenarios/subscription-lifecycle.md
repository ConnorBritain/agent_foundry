# Scenario: Subscription Lifecycle

This scenario defines the complete lifecycle of a subscription from free signup through trial, paid conversion, payment failure, cancellation, and reactivation. It is validated after Phase 3 and fully in Phase 4.

---

## Scenario Overview

| Property | Value |
|----------|-------|
| **Priority** | Critical |
| **Validated After** | Phase 3 (partial), Phase 4 (complete) |
| **Primary Agents** | RevOps, Database Engineer, Senior Full-Stack, QA/Test |
| **Estimated Test Time** | ~15 minutes (full lifecycle E2E) |

---

## Lifecycle State Diagram

```
                            ┌──────────────────────────────────────────┐
                            │                                          │
  ┌──────┐    Start Trial   │  ┌──────────┐   Trial Expires    ┌──────┴──────┐
  │ Free ├──────────────────┼──► Trialing ├──────────────────► │   Active    │
  └──┬───┘                  │  └────┬─────┘                    └──┬───┬──────┘
     │                      │       │                              │   │
     │   Direct Purchase    │       │ User cancels trial           │   │ Payment fails
     │                      │       │                              │   │
     │                      │       ▼                              │   ▼
     │                      │  ┌──────────┐                    ┌──┴────────┐
     └──────────────────────┼──►Canceled  │◄───────────────────┤ Past Due  │
                            │  └────┬─────┘   Grace period     └──┬────────┘
                            │       │          expires             │
                            │       │                              │ Payment succeeds
                            │       │ Reactivation                 │ (retry)
                            │       │                              │
                            │       ▼                              ▼
                            │  ┌──────────┐                    ┌──────────┐
                            │  │Reactivated├───────────────────► Active   │
                            │  └──────────┘   New payment      └──────────┘
                            │                                          │
                            └──────────────────────────────────────────┘
```

---

## Phase 1: Free Tier

### State: Free

The user has signed up but has no paid subscription.

| Property | Value |
|----------|-------|
| Subscription Status | None (no record in `subscriptions` table) |
| Feature Access | Free tier limits (per CONFIG) |
| Billing | No payment method on file |
| Dashboard Display | "Free Plan" badge, "Upgrade to Pro" CTA |

### User Experience

- User has full access to free-tier features
- Usage limits are enforced (e.g., 3 projects, 1GB storage, 1000 API calls/month)
- Upgrade prompts appear when approaching limits
- Pricing page is accessible with plan comparison

### Validation Criteria

- [ ] No subscription record exists for the user
- [ ] `canAccessFeature(userId, 'unlimited_projects')` returns `false`
- [ ] `getUsageLimits(userId)` returns free tier limits
- [ ] Dashboard shows free plan badge
- [ ] Upgrade CTA is visible and functional

---

## Phase 2: Trial (14 Days)

### Trigger

User clicks "Start Free Trial" on the pricing page or during onboarding.

### State: Trialing

| Property | Value |
|----------|-------|
| Subscription Status | `trialing` |
| Duration | 14 days (per CONFIG `trial.duration_days`) |
| Payment Method | Collected upfront if `trial.require_payment_method: true`; otherwise collected at conversion |
| Feature Access | Full Pro plan features |
| Dashboard Display | "Pro Plan (Trial)" badge, "X days remaining" counter |

### Steps

| Step | Event | Database Update | User Experience |
|------|-------|-----------------|-----------------|
| 1 | User starts trial | Stripe creates subscription with `status: trialing`, `trial_end` set to 14 days from now. Webhook syncs to `subscriptions` table | Dashboard updates to show "Pro Plan (Trial)" badge with "14 days remaining" |
| 2 | Day 1-10 | No changes | User has full Pro access. Trial countdown visible in dashboard |
| 3 | Day 11 (3 days before expiry) | `customer.subscription.trial_will_end` webhook fires | Notification: "Your trial ends in 3 days. Add a payment method to continue." |
| 4 | Day 14 | Trial period ends. Stripe attempts to charge | See conversion outcomes below |

### Trial Conversion Outcomes

**Outcome A: Payment method on file, payment succeeds**

| Step | Event | Result |
|------|-------|--------|
| 1 | Trial expires | Stripe charges the payment method |
| 2 | `invoice.payment_succeeded` webhook | Invoice recorded in database |
| 3 | `customer.subscription.updated` webhook | Subscription status: `trialing` -> `active` |
| 4 | User experience | Seamless transition. No service interruption. Dashboard updates to "Pro Plan" (no trial badge) |

**Outcome B: No payment method on file**

| Step | Event | Result |
|------|-------|--------|
| 1 | Trial expires | Stripe cannot charge (no payment method) |
| 2 | `customer.subscription.updated` webhook | Subscription status: `trialing` -> `past_due` or `canceled` (depending on Stripe config) |
| 3 | User experience | Downgrade to free tier. Notification: "Your trial has ended. Upgrade to continue using Pro features." |

**Outcome C: Payment method on file, payment fails**

| Step | Event | Result |
|------|-------|--------|
| 1 | Trial expires | Stripe attempts to charge but card is declined |
| 2 | `invoice.payment_failed` webhook | Dunning flow begins (see Phase 4: Payment Failure) |
| 3 | User experience | Notification: "We could not process your payment. Please update your payment method." |

### Validation Criteria

- [ ] Trial duration is exactly 14 days (configurable via CONFIG)
- [ ] Pro features are accessible during trial
- [ ] Trial countdown is accurate (days remaining calculation)
- [ ] Trial-ending notification fires 3 days before expiry
- [ ] Conversion is seamless when payment method is valid
- [ ] Downgrade is handled gracefully when payment fails

---

## Phase 3: Paid Subscription (Active)

### State: Active

| Property | Value |
|----------|-------|
| Subscription Status | `active` |
| Billing | Auto-charged monthly or annually per plan |
| Feature Access | Full plan features |
| Dashboard Display | "Pro Plan" badge, next billing date, manage billing link |

### Recurring Billing

| Step | Event | Database Update | User Experience |
|------|-------|-----------------|-----------------|
| 1 | Billing period ends | Stripe creates invoice and attempts charge | No user action required |
| 2 | Payment succeeds | `invoice.payment_succeeded` webhook. Invoice recorded | No notification (silent renewal). User retains access |
| 3 | Payment fails | `invoice.payment_failed` webhook. Dunning starts | See Phase 4: Payment Failure |

### Plan Changes

**Upgrade (Pro to Enterprise):**

| Step | Event | Result |
|------|-------|--------|
| 1 | User clicks "Upgrade" in billing portal or settings | Redirect to Stripe Billing Portal |
| 2 | User selects Enterprise plan | Stripe calculates proration (credit for unused Pro time, charge for Enterprise) |
| 3 | User confirms | Subscription updated. `customer.subscription.updated` webhook fires |
| 4 | Database update | `subscriptions.price_id` updated to Enterprise price ID |
| 5 | User experience | Dashboard updates to "Enterprise Plan." Enterprise features unlocked immediately |

**Downgrade (Enterprise to Pro):**

| Step | Event | Result |
|------|-------|--------|
| 1 | User selects Pro in billing portal | Stripe schedules downgrade for end of current period |
| 2 | `customer.subscription.updated` webhook | `subscriptions.cancel_at_period_end` may be set, or price change scheduled |
| 3 | At period end | Subscription changes to Pro pricing. `customer.subscription.updated` webhook fires |
| 4 | User experience | Dashboard shows "Downgrade to Pro scheduled for [date]." Enterprise features available until period end |

### Validation Criteria

- [ ] Subscription auto-renews without user action
- [ ] Proration is calculated correctly for mid-cycle plan changes
- [ ] Upgrades take effect immediately
- [ ] Downgrades take effect at end of billing period (no immediate loss of features)
- [ ] Invoice history is available in billing portal

---

## Phase 4: Payment Failure (Dunning)

### Trigger

Stripe's automatic charge fails (declined card, expired card, insufficient funds).

### State: Past Due

| Property | Value |
|----------|-------|
| Subscription Status | `past_due` |
| Feature Access | Full access maintained during grace period |
| Dashboard Display | Warning banner: "Payment failed. Please update your payment method." |

### Dunning Schedule

The dunning schedule follows CONFIG `dunning` settings. Default:

| Day | Event | Action | Notification |
|-----|-------|--------|-------------|
| 0 | Initial payment failure | Status set to `past_due`. Dunning counter initialized | Email: "Your payment failed. Please update your payment method." + link to billing portal |
| 3 | First retry | Stripe retries the charge | If fails: Email: "Second payment attempt failed. Update your card to avoid service interruption." |
| 7 | Second retry | Stripe retries the charge | If fails: Email: "We have been unable to process your payment. You have 14 days to resolve this." |
| 14 | Final retry | Stripe retries the charge | If fails: Email: "Final notice: Your subscription will be downgraded in 7 days unless payment is resolved." |
| 21 | Grace period expires | Automatic downgrade to Free plan | Email: "Your subscription has been downgraded to the Free plan. Upgrade anytime to restore access." |

### Dunning State Tracking

```sql
-- Tracked in subscriptions or a dedicated dunning_state table
dunning_started_at    TIMESTAMPTZ   -- When the first failure occurred
retry_count           INTEGER       -- Number of retries attempted (0, 1, 2, 3)
last_retry_at         TIMESTAMPTZ   -- Timestamp of most recent retry
grace_period_ends_at  TIMESTAMPTZ   -- When access will be revoked
```

### Recovery During Dunning

If the user updates their payment method and the next retry succeeds:

| Step | Event | Result |
|------|-------|--------|
| 1 | User clicks "Update payment method" in email or dashboard | Redirect to Stripe Billing Portal |
| 2 | User adds a new card | Stripe updates the default payment method |
| 3 | Next retry attempt succeeds | `invoice.payment_succeeded` webhook fires |
| 4 | Subscription status updates | `past_due` -> `active`. Dunning counters reset |
| 5 | User experience | Warning banner removed. Normal service restored |

### Validation Criteria

- [ ] Subscription status is set to `past_due` on first failure (not immediately canceled)
- [ ] User retains access to Pro features during the entire dunning period (21 days)
- [ ] Retry attempts follow the configured schedule (Day 3, 7, 14)
- [ ] Each retry sends an appropriate notification
- [ ] Grace period expires after configured days (7 days after final retry)
- [ ] Automatic downgrade occurs at grace period end
- [ ] Recovery is seamless: update card -> retry succeeds -> status restored
- [ ] Dunning state is tracked and queryable for analytics

---

## Phase 5: Cancellation

### Trigger

User voluntarily cancels their subscription via billing portal or settings.

### State: Canceled

| Property | Value |
|----------|-------|
| Subscription Status | `canceled` (or `active` with `cancel_at_period_end: true`) |
| Feature Access | Pro features retained until end of current billing period |
| Dashboard Display | "Pro Plan (Cancels on [date])" badge, "Reactivate" button |

### Cancellation Flow

| Step | Event | Database Update | User Experience |
|------|-------|-----------------|-----------------|
| 1 | User clicks "Cancel subscription" in billing portal | Stripe sets `cancel_at_period_end: true`. `customer.subscription.updated` webhook fires | Confirmation: "Your subscription will remain active until [period end date]." |
| 2 | `subscriptions` record updated | `cancel_at_period_end: true` | Dashboard shows "Cancels on [date]" with "Reactivate" button |
| 3 | User retains Pro access until period end | No changes | All Pro features continue to work |
| 4 | Period end date arrives | `customer.subscription.deleted` webhook fires. `subscriptions.status` set to `canceled`. `ended_at` set | Dashboard updates to "Free Plan." Pro features restricted |

### Validation Criteria

- [ ] Cancellation does not immediately revoke access
- [ ] User has Pro features until the end of their paid period
- [ ] Dashboard clearly shows when access will end
- [ ] "Reactivate" button is available before the period ends
- [ ] After period end, user is on Free plan with free tier limits
- [ ] Canceled subscription is excluded from MRR calculations

---

## Phase 6: Reactivation

### Trigger

User reactivates a canceled or expired subscription.

### Scenario A: Reactivate Before Period End

| Step | Event | Result |
|------|-------|--------|
| 1 | User clicks "Reactivate" on dashboard | Application calls Stripe API to remove `cancel_at_period_end` |
| 2 | `customer.subscription.updated` webhook fires | `cancel_at_period_end` set to `false` |
| 3 | User experience | Dashboard returns to "Pro Plan" (no cancellation notice). Billing continues as normal |

### Scenario B: Reactivate After Period End (Re-subscribe)

| Step | Event | Result |
|------|-------|--------|
| 1 | User clicks "Upgrade to Pro" on dashboard or pricing page | New checkout flow initiated |
| 2 | User completes Stripe Checkout | New subscription created. Previous subscription remains `canceled` |
| 3 | `checkout.session.completed` webhook fires | New `subscriptions` record created with `status: 'active'` |
| 4 | User experience | Dashboard shows "Pro Plan." Full access restored |

### Validation Criteria

- [ ] Reactivation before period end cancels the cancellation (no new subscription needed)
- [ ] Reactivation after period end requires a new checkout (new subscription)
- [ ] Previous subscription data is preserved for analytics (churn tracking)
- [ ] Re-subscribed user gets full Pro access immediately
- [ ] No duplicate active subscriptions for the same user

---

## Complete Lifecycle Timeline Example

```
Day  0: User signs up (Free plan)
Day  5: User starts Pro trial
Day  5-18: User has Pro features (14-day trial)
Day 16: Trial-ending notification sent (3 days before expiry)
Day 19: Trial expires, payment method charged successfully -> Active
Day 19-49: User is Active on Pro monthly
Day 49: Monthly renewal, payment succeeds -> Active
Day 79: Monthly renewal, payment FAILS -> Past Due
Day 82: First retry (Day 3), payment fails
Day 86: Second retry (Day 7), payment fails
Day 93: Final retry (Day 14), payment fails
Day 100: Grace period expires (Day 21), auto-downgrade -> Free
Day 110: User returns, clicks "Upgrade to Pro"
Day 110: User completes checkout -> Active (re-subscribed)
Day 140: User cancels subscription -> Active (cancel_at_period_end)
Day 140-170: User has Pro access until period end
Day 170: Period ends -> Canceled, downgrade to Free
Day 200: User clicks "Reactivate" -> New checkout -> Active
```

---

## Database State at Each Phase

| Phase | `subscriptions.status` | `cancel_at_period_end` | Feature Access | MRR Impact |
|-------|----------------------|----------------------|----------------|------------|
| Free | (no record) | N/A | Free tier | $0 |
| Trialing | `trialing` | `false` | Pro features | $0 (trial) |
| Active | `active` | `false` | Pro features | +$29 |
| Past Due | `past_due` | `false` | Pro features (grace) | +$29 (at risk) |
| Canceling | `active` | `true` | Pro features (until period end) | +$29 (churning) |
| Canceled | `canceled` | N/A | Free tier | $0 |
| Reactivated | `active` | `false` | Pro features | +$29 |

---

## Agents Responsible

| Agent | Responsibility |
|-------|---------------|
| **RevOps Specialist** | Subscription logic, dunning flow, webhook handlers, Stripe configuration |
| **Database Engineer** | Subscription tables, status tracking, dunning state, revenue views |
| **Senior Full-Stack Developer** | Dashboard subscription display, upgrade/downgrade UI, reactivation button |
| **QA / Test Engineer** | Full lifecycle E2E tests, dunning simulation, edge case coverage |
