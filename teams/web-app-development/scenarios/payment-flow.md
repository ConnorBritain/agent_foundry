# Scenario: Payment Flow

This scenario defines the complete subscription payment flow, including checkout, webhook processing, database updates, and feature unlocking. It is validated after Phase 3 and again in Phase 4.

---

## Scenario Overview

| Property | Value |
|----------|-------|
| **Priority** | Critical |
| **Validated After** | Phase 3, Phase 4 |
| **Primary Agents** | RevOps, Senior Full-Stack, Database Engineer, QA/Test |
| **Estimated Test Time** | ~10 minutes (E2E with webhook verification) |

---

## Success Path: New Customer Upgrades to Pro (Monthly)

### Preconditions

- User is authenticated and on the Free plan (no active subscription)
- Stripe products and prices are created in test mode
- Webhook endpoint is configured and receiving events
- Stripe test card numbers are available

### Steps

| Step | User Action / System Event | Expected Outcome |
|------|---------------------------|------------------|
| 1 | User navigates to `/pricing` | Pricing page loads with Free, Pro, and Enterprise plan cards. Monthly/annual toggle visible. Pro card shows "$29/month" |
| 2 | User clicks "Upgrade to Pro" on the Pro plan card | Application calls `/api/checkout` with the Pro monthly price ID |
| 3 | (Server) Checkout handler creates or retrieves Stripe Customer | Customer record linked to user ID. If new customer, record created in `customers` table |
| 4 | (Server) Checkout handler creates Stripe Checkout Session | Session created with correct price, success URL (`/dashboard?checkout=success`), cancel URL (`/pricing?checkout=cancelled`) |
| 5 | User is redirected to Stripe Checkout | Stripe Checkout page loads with Pro plan details and price |
| 6 | User enters test card `4242 4242 4242 4242`, exp `12/34`, CVC `123` | Card is accepted |
| 7 | User clicks "Subscribe" | Stripe processes the payment |
| 8 | (Stripe) `checkout.session.completed` webhook fires | Webhook received at `/api/webhooks/stripe` |
| 9 | (Server) Webhook handler verifies signature | Signature valid, event processed |
| 10 | (Server) Webhook handler checks idempotency | Event ID not previously processed, continue |
| 11 | (Server) Webhook handler syncs subscription to database | `subscriptions` record created with `status: 'active'`, correct `price_id`, `current_period_start`, `current_period_end` |
| 12 | (Stripe) `customer.subscription.created` webhook fires | Subscription record confirmed in database |
| 13 | (Stripe) `invoice.payment_succeeded` webhook fires | Invoice record created in database |
| 14 | User is redirected to `/dashboard?checkout=success` | Dashboard loads with success toast: "Welcome to Pro!" |
| 15 | User's subscription status updates on dashboard | Dashboard shows "Pro Plan" badge, next billing date, usage limits updated |
| 16 | User can access Pro-only features | Feature gates check subscription status and allow access |

### Validation Criteria

- [ ] `customers` table has a record linking user ID to Stripe customer ID
- [ ] `subscriptions` table has a record with `status: 'active'` and correct `price_id`
- [ ] `invoices` table has a payment record with correct amount (2900 cents)
- [ ] Dashboard displays correct plan name ("Pro")
- [ ] Dashboard displays correct next billing date (1 month from now)
- [ ] Pro-only features are accessible
- [ ] Free plan limits are lifted (e.g., project limit increased to unlimited)

---

## Success Path: Upgrade from Monthly to Annual

### Preconditions

- User has an active Pro monthly subscription

### Steps

| Step | User Action / System Event | Expected Outcome |
|------|---------------------------|------------------|
| 1 | User navigates to `/settings` and clicks "Manage Billing" | Redirect to Stripe Billing Portal |
| 2 | User clicks "Update plan" in the Billing Portal | Plan options displayed |
| 3 | User selects "Annual" billing | Portal shows prorated amount |
| 4 | User confirms the plan change | Stripe processes the proration and updates the subscription |
| 5 | (Stripe) `customer.subscription.updated` webhook fires | Webhook handler updates `subscriptions` record with new `price_id` (annual price) |
| 6 | User returns to the application | Dashboard shows updated plan: "Pro (Annual)", new billing date |

### Validation Criteria

- [ ] `subscriptions` record updated with annual `price_id`
- [ ] Proration calculated correctly (credit for remaining monthly period)
- [ ] No duplicate subscription created (same subscription ID, updated price)
- [ ] Dashboard reflects the plan change immediately after webhook processing

---

## Success Path: Trial Conversion to Paid

### Preconditions

- User signed up with a trial (14-day Pro trial per CONFIG)
- Trial is about to expire (within 3 days)
- User has a payment method on file

### Steps

| Step | User Action / System Event | Expected Outcome |
|------|---------------------------|------------------|
| 1 | (Stripe) `customer.subscription.trial_will_end` webhook fires (3 days before expiry) | Notification queued: "Your trial ends in 3 days" |
| 2 | Trial period expires | Stripe attempts to charge the payment method |
| 3 | (Stripe) Payment succeeds | `invoice.payment_succeeded` webhook fires |
| 4 | (Stripe) `customer.subscription.updated` webhook fires | Subscription status changes from `trialing` to `active` |
| 5 | (Server) Webhook handler updates subscription record | `subscriptions.status` updated to `active` |
| 6 | User continues using the application | No interruption in service. Pro features remain available |

### Validation Criteria

- [ ] Subscription status transitions from `trialing` to `active`
- [ ] First payment recorded in `invoices` table
- [ ] No service interruption during trial-to-paid conversion
- [ ] Trial-ending notification was sent/queued

---

## Failure Path: Declined Card

### Preconditions

- User is on the Stripe Checkout page attempting to subscribe

### Steps

| Step | User Action / System Event | Expected Outcome |
|------|---------------------------|------------------|
| 1 | User enters declined test card `4000 0000 0000 0002` | Card is declined |
| 2 | Stripe Checkout shows decline error | Message: "Your card was declined. Please try a different card." |
| 3 | User enters a valid card `4242 4242 4242 4242` | Card is accepted, subscription created successfully |

### Validation Criteria

- [ ] No subscription or customer record created for the declined attempt
- [ ] No charge to the user
- [ ] User can retry with a different card without starting over
- [ ] Decline is not logged as an application error (Stripe handles this UI)

---

## Failure Path: Fraud Detection

### Preconditions

- User attempts checkout with a card flagged for fraud

### Steps

| Step | User Action / System Event | Expected Outcome |
|------|---------------------------|------------------|
| 1 | User enters fraud test card `4000 0000 0000 9235` | Stripe Radar flags the transaction |
| 2 | Stripe blocks the payment | Checkout shows error: "Payment could not be processed" |
| 3 | No subscription is created | Database remains unchanged |

### Validation Criteria

- [ ] Fraudulent transaction is blocked
- [ ] No subscription created
- [ ] Event logged for review (Stripe Dashboard, not application logs)
- [ ] User can retry with a legitimate card

---

## Failure Path: User Closes Checkout Modal

### Preconditions

- User has been redirected to Stripe Checkout
- User decides not to complete the purchase

### Steps

| Step | User Action / System Event | Expected Outcome |
|------|---------------------------|------------------|
| 1 | User clicks the back arrow or closes the Stripe Checkout tab | Stripe redirects to cancel URL (`/pricing?checkout=cancelled`) |
| 2 | User returns to pricing page | Pricing page loads with cancel message: "Checkout was not completed." |
| 3 | No webhook events are fired | No database changes |

### Validation Criteria

- [ ] No subscription or payment record created
- [ ] No charge to the user
- [ ] User can attempt checkout again immediately
- [ ] Cancel URL displays appropriate messaging (not an error)

---

## Failure Path: Webhook Delivery Failure

### Preconditions

- User completes checkout successfully
- Webhook endpoint is temporarily unavailable (deployment in progress, network issue)

### Steps

| Step | User Action / System Event | Expected Outcome |
|------|---------------------------|------------------|
| 1 | User completes Stripe Checkout | Stripe fires `checkout.session.completed` webhook |
| 2 | Webhook endpoint returns 500 or times out | Stripe marks the webhook delivery as failed |
| 3 | (Stripe) Automatic retry after ~1 minute | Stripe retries the webhook |
| 4 | Webhook endpoint is back online | Webhook processes successfully |
| 5 | Subscription record created in database | Data is consistent with Stripe |

### Validation Criteria

- [ ] User sees "checkout success" page immediately (does not depend on webhook)
- [ ] Webhook retries are handled correctly
- [ ] Subscription record is eventually consistent (created when webhook succeeds)
- [ ] Dashboard may show a brief delay ("Activating your subscription...") until webhook processes
- [ ] No duplicate records when the webhook finally succeeds

---

## Failure Path: Duplicate Webhook

### Preconditions

- Stripe delivers the same webhook event twice (network retry, Stripe internal retry)

### Steps

| Step | User Action / System Event | Expected Outcome |
|------|---------------------------|------------------|
| 1 | First `checkout.session.completed` webhook arrives | Processed normally. Subscription record created. Event ID stored |
| 2 | Second `checkout.session.completed` webhook arrives (duplicate) | Webhook handler checks event ID against processed events |
| 3 | Duplicate detected | Handler returns 200 to Stripe without processing again |

### Validation Criteria

- [ ] Only one subscription record exists in database
- [ ] Only one invoice record exists for the initial payment
- [ ] Handler returns 200 (not an error) to prevent further Stripe retries
- [ ] Duplicate detection is logged for monitoring (not as an error, as an info event)

---

## Failure Path: Race Condition (Checkout + Webhook)

### Preconditions

- User completes checkout and is redirected to success page
- Success page attempts to fetch subscription status from database
- Webhook has not yet been processed

### Steps

| Step | User Action / System Event | Expected Outcome |
|------|---------------------------|------------------|
| 1 | User lands on `/dashboard?checkout=success` | Dashboard loads |
| 2 | Dashboard fetches subscription status from database | Subscription record may not exist yet (webhook in transit) |
| 3 | Dashboard shows loading/pending state | Message: "Activating your subscription..." with a spinner |
| 4 | Dashboard polls or uses realtime subscription for updates | After webhook processes (typically 1-3 seconds), status updates |
| 5 | Subscription status appears | Dashboard shows "Pro Plan" badge and updates features |

### Validation Criteria

- [ ] Dashboard does not show an error when subscription is not yet in database
- [ ] Dashboard handles the "pending" state gracefully
- [ ] Polling or realtime update triggers UI refresh when subscription appears
- [ ] Maximum wait time before showing "contact support" message: 30 seconds
- [ ] No race condition between polling and webhook creating the record

---

## Performance Targets

| Metric | Target |
|--------|--------|
| Checkout session creation | < 2 seconds |
| Stripe Checkout page load | < 3 seconds (Stripe-controlled) |
| Webhook processing time | < 5 seconds from receipt to database update |
| Dashboard subscription status update | < 10 seconds after checkout completion |
| Success rate (non-fraud, valid card) | > 98% |
| Idempotency | 100% (duplicate webhooks never create duplicate records) |

---

## Stripe Test Cards Reference

| Card Number | Scenario |
|-------------|----------|
| `4242 4242 4242 4242` | Successful payment |
| `4000 0000 0000 0002` | Card declined |
| `4000 0000 0000 9995` | Insufficient funds |
| `4000 0000 0000 0069` | Expired card |
| `4000 0000 0000 0119` | Processing error |
| `4000 0025 0000 3155` | Requires 3D Secure authentication |
| `4000 0000 0000 9235` | Fraud detection block |

All test cards use any future expiration date, any 3-digit CVC, and any billing postal code.

---

## Agents Responsible

| Agent | Responsibility |
|-------|---------------|
| **RevOps Specialist** | Stripe products/prices, checkout handler, webhook handler, billing portal, subscription library |
| **Senior Full-Stack Developer** | Payment UI components, checkout flow, subscription status display, success/cancel pages |
| **Database Engineer** | Subscription tables, webhook helper functions, RLS policies, revenue views |
| **Cloud / DevOps Engineer** | Webhook endpoint configuration, Stripe secrets management |
| **QA / Test Engineer** | E2E payment tests, idempotency tests, race condition tests |
