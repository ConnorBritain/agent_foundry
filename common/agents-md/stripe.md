# Stripe — Compressed AGENTS.md Knowledge

## Quick Reference
| Area | Key Concepts |
|---|---|
| Payments | PaymentIntents, SetupIntents, payment methods, idempotency |
| Subscriptions | Products, prices, subscription lifecycle, trials, metered billing |
| Checkout | Hosted checkout, embedded, custom flows, line items |
| Webhooks | Event handling, signature verification, idempotency, retry logic |
| Billing Portal | Customer self-service, plan changes, cancellation, invoice history |
| Connect | Platform payments, direct/destination charges, transfers |

## Core Objects & Relationships
```
Customer → PaymentMethod (many)
Customer → Subscription (many) → Price → Product
Subscription → Invoice (periodic) → PaymentIntent (per invoice)
Checkout Session → creates Customer + Subscription or one-time PaymentIntent
```

## API Keys & Environment
| Key | Usage |
|---|---|
| pk_test_* / pk_live_* | Public key — client-side (Stripe.js, Elements) |
| sk_test_* / sk_live_* | Secret key — server-side only, NEVER expose |
| whsec_* | Webhook signing secret — per endpoint |

```
STRIPE_SECRET_KEY=sk_test_... (server env)
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_test_... (client env)
STRIPE_WEBHOOK_SECRET=whsec_... (server env)
```

## Checkout Integration
### Hosted Checkout (Recommended for most cases)
```typescript
// Server: create checkout session
const session = await stripe.checkout.sessions.create({
  mode: 'subscription', // or 'payment' for one-time
  customer: customerId, // optional — creates new if omitted
  line_items: [{ price: 'price_xxx', quantity: 1 }],
  success_url: 'https://app.com/success?session_id={CHECKOUT_SESSION_ID}',
  cancel_url: 'https://app.com/pricing',
  metadata: { userId: 'user_123' }, // pass-through data
});
// Client: redirect
redirect(session.url);
```

### Embedded Checkout
```
Use @stripe/react-stripe-js EmbeddedCheckoutProvider
Pass clientSecret from session.client_secret (requires ui_mode: 'embedded')
```

## Subscription Lifecycle
| Event | Action |
|---|---|
| customer.subscription.created | Provision access, store subscription ID |
| customer.subscription.updated | Handle plan changes, status transitions |
| customer.subscription.deleted | Revoke access, cleanup |
| invoice.payment_succeeded | Confirm payment, extend access |
| invoice.payment_failed | Notify user, retry logic, grace period |
| customer.subscription.trial_will_end | Send reminder 3 days before trial ends |

### Subscription Statuses
```
active → paying, full access
trialing → trial period, full access
past_due → payment failed, grace period (configurable)
canceled → explicitly canceled, access until period end (if cancel_at_period_end)
unpaid → all retries exhausted, revoke access
incomplete → first payment failed during creation
incomplete_expired → incomplete for 23hrs, abandoned
```

### Creating Subscriptions
```typescript
// Via Checkout (recommended)
stripe.checkout.sessions.create({ mode: 'subscription', ... })

// Via API (custom UI)
stripe.subscriptions.create({
  customer: 'cus_xxx',
  items: [{ price: 'price_xxx' }],
  trial_period_days: 14,
  payment_behavior: 'default_incomplete', // requires client confirmation
  expand: ['latest_invoice.payment_intent'],
});
```

## Webhook Handling
### Critical Pattern
```typescript
// Route handler (Next.js App Router)
export async function POST(req: Request) {
  const body = await req.text(); // raw body required
  const sig = req.headers.get('stripe-signature')!;
  let event: Stripe.Event;
  try {
    event = stripe.webhooks.constructEvent(body, sig, process.env.STRIPE_WEBHOOK_SECRET!);
  } catch (err) {
    return new Response('Webhook signature verification failed', { status: 400 });
  }
  // Handle events
  switch (event.type) {
    case 'checkout.session.completed':
      const session = event.data.object as Stripe.Checkout.Session;
      await provisionAccess(session.metadata.userId, session.subscription);
      break;
    case 'invoice.payment_failed':
      await handleFailedPayment(event.data.object);
      break;
  }
  return new Response('ok', { status: 200 }); // always 200 to acknowledge
}
```

### Webhook Best Practices
| Rule | Rationale |
|---|---|
| Always return 200 quickly | Stripe retries on non-2xx (up to 3 days) |
| Verify signature ALWAYS | Prevents spoofed events |
| Handle idempotently | Same event may arrive multiple times |
| Use event.data.object | Don't re-fetch unless stale data concern |
| Process async for heavy work | Queue jobs, respond 200 immediately |
| Store event ID | Track processed events to skip duplicates |

## Billing Portal
```typescript
const portalSession = await stripe.billingPortal.sessions.create({
  customer: customerId,
  return_url: 'https://app.com/settings',
});
redirect(portalSession.url);
```
Configure in Stripe Dashboard: allowed actions, plan switching, cancellation, invoice history.

## Products & Prices
| Concept | Details |
|---|---|
| Product | What you sell (name, description, metadata) |
| Price | How much (amount, currency, interval, billing_scheme) |
| Recurring | interval: month/year, interval_count, trial_period_days |
| Metered | usage_type: 'metered', report usage via API |
| Tiered | tiers_mode: 'graduated' or 'volume', define tier brackets |

### Price Lookup Keys
```
Use lookup_key on prices for stable references across environments
stripe.prices.list({ lookup_keys: ['pro_monthly'] }) → same code, different price IDs per env
```

## Customer Management
```typescript
// Create or retrieve customer
const customer = await stripe.customers.create({
  email: user.email,
  metadata: { userId: user.id },
});
// Store customer.id in your database linked to user

// List payment methods
const methods = await stripe.paymentMethods.list({
  customer: customerId, type: 'card',
});
```

## Error Handling
| Error Type | Meaning | Action |
|---|---|---|
| card_error | Card declined, expired, etc. | Show user-friendly message |
| invalid_request_error | Bad parameters | Fix code, log for debugging |
| authentication_error | Invalid API key | Check env configuration |
| rate_limit_error | Too many requests | Implement backoff |
| idempotency_error | Conflicting idempotency key | Use unique keys per operation |

## Testing & Development
| Tool | Purpose |
|---|---|
| stripe listen --forward-to localhost:3000/api/webhooks | Forward webhook events locally |
| stripe trigger checkout.session.completed | Fire test events |
| Test cards: 4242424242424242 | Successful payment |
| Test cards: 4000000000000002 | Declined card |
| Test cards: 4000002500003155 | Requires 3D Secure |
| Test clocks | Simulate subscription lifecycle time progression |

## Security Checklist
```
[ ] Secret key only on server, never in client bundle
[ ] Webhook signature verified on every event
[ ] Idempotency keys on all mutating API calls
[ ] Amount validation server-side (never trust client-sent amounts)
[ ] Metadata for linking Stripe objects to your domain objects
[ ] PCI compliance: use Stripe.js/Elements, never handle raw card numbers
```
