# Sforza Money Model

Hormozi's framework applied to Sforza. A Money Model is a deliberate sequence of offers designed to increase how many customers you get, how much they pay, and how fast they pay it.

**Cardinal rule**: Make enough profit from one customer to get and service at least two more in 30 days.

**Build rule**: Perfect one offer at a time. Don't launch all four stages simultaneously.

---

## The Sequence

```
Stage I:  ATTRACTION  -- Get customers and cash
Stage II: UPSELLS     -- Get more cash from them faster
          DOWNSELLS   -- Turn nos into yeses
Stage III: CONTINUITY -- Maximize total spend over time
```

Each stage pays for the next. Each stage must work reliably before advancing.

---

## Stage I: Attraction Offer (The Decoy)

**Pattern**: Hormozi's Decoy Offer. Advertise a free/cheap thing. When leads engage, present a premium version side-by-side. The free version is the decoy that makes the premium look obvious.

### Free Tier (The Decoy)

- Open-source orchestrator core
- One project at a time
- One template: Research Brief (low stakes, immediately useful)
- CLI-only interface -- no dashboard
- Community templates only

### Pro Tier ($25/week)

- Unlimited projects, all pro templates
- Dashboard with Decision Queue
- Multi-channel notifications
- Git checkpointing, budget enforcement
- Priority support

**Why this works**: The free tier is genuinely useful -- not crippled. But the moment you want the Dashboard or Business Builder template, you upgrade. The free tier creates the problem; Pro solves it.

**How to present** (Hormozi's framing): Don't ask "do you want Pro?" Ask: "Are you here to try an AI tool, or to actually ship something? ...Great. Most people who want results go with Pro because the Decision Queue is where the magic happens."

### Alternative: Win Your Money Back

- Pay $100 for the first month
- If you ship a working deliverable using a template within 30 days, get your next month free as credit
- Criteria (easy to track, gets results, advertises the business):
  1. Complete all Decision Queue items within 24 hours
  2. All template phases completed
  3. Post a public review/testimonial with your deliverables
- Apply the credit over time: $25/week off for 4 weeks (keeps them paying)
- **Make everyone a winner**: Halfway through, regardless of progress: "You started. That's the biggest victory. We'll credit your whole first month."

---

## Stage II: Upsell Offers

**Principle**: Your first offer doesn't always make the profit. You make it on the second, third, and fourth offers.

### The BAMFAM Upsell

When a template run completes, the Orchestrator immediately suggests the next one:

> "Your Research Brief is done. The next step for most people is the Business Builder template -- want me to set it up? Your research will carry over as input."

This is Sforza's "Do you want fries with that?" It costs nothing to ask.

### The Rollover Upsell

Credit previous template spend toward the next, more expensive template:

> "You spent $15 on the Research Brief. I'll credit that toward the Business Builder ($150 value). You're basically $15 ahead already."

For winback:
> "You ran a Research Brief 3 months ago. We'll credit that $15 toward any template you run this week."

Price the next offer at 4x the credit minimum so you still profit.

### The Menu Upsell (Unsell -> Prescribe -> A/B -> Card on File)

The Orchestrator uses this when recommending templates:

1. **Unsell**: "You don't need the full 8-team Business Builder. You've already got your strategy. You just need Web Dev and Marketing."
2. **Prescribe**: "Here's what I'd run: Web Dev first (2 hours, ~$60), then Marketing (1.5 hours, ~$40). The marketing team will pull from your web dev deliverables automatically."
3. **A/B**: "Would you rather start with Web Dev or Marketing first?"
4. **Card on file**: "Want to use the same API key and billing? ...Great."

This builds massive trust. You're telling them what NOT to buy.

### The Anchor Upsell

Show the expensive thing first:

- **Enterprise tier ($200/week)**: Dedicated support, custom template builder, SLA, team collaboration (multiple humans), priority queue, audit trail export
- **Pro tier ($25/week)**: Everything a solo operator needs

Present Enterprise first on the pricing page. Pro looks like a steal by comparison. And some people will actually take Enterprise.

### Premium Templates ($20-50 one-time)

Domain-expert templates. Community creates and sells. Sforza takes 30% (App Store model). Both an upsell and a retention engine -- new templates = new reasons to stay.

---

## Stage II: Downsell Offers

**Principle**: Never drop the price for the same thing. Change what they get, or how they pay.

### Feature Downsells (when someone balks at Pro)

Don't discount. Remove features:
1. Remove premium templates, keep dashboard: "$15/week -- you get the Decision Queue and 3 core templates"
2. Remove dashboard, keep all templates: "$10/week -- CLI-only with all templates"
3. The "Minimum Package": "$5/week -- just the Research Brief template with CLI"

Name the cheapest combination "The Minimum." When presenting: "So nothing more than the minimum package then?" -- they say yes because "minimum" feels like the floor.

### Payment Plan Downsell (for annual/large template purchases)

- "It's $960 if you prepay for the year -- you save 20%. That's what most people do."
- If no: "Want to just split it? $480 now, $480 in 30 days?"
- If no: "What's the most you can put down today?"
- Align billing with paydays (recovers 1/3 of declined payments)

### Trial With Penalty

"Try Pro for 14 days free. Complete at least one template run and answer all Decision Queue items within 24 hours. If you do, the trial is free. If you skip the decisions, you'll be billed $25 for the week."

Why this works:
- The "penalty" actions are exactly what makes great customers
- Completing a template run proves the value
- Card is already on file
- Always get a credit card: "That's just how we've always done it."

### Temperature Check (after two downsells)

"On a scale from 1-10, how bad do you want this?" If 8+, keep downselling payment structures. If 7 or below, ask "What would a 10 look like?" -- then recombine features to match.

---

## Stage III: Continuity Offers

The $25/week subscription IS the continuity. Strengthen retention with Hormozi's three continuity patterns:

### Continuity Bonus (get them to start)

"Sign up for Pro today and get the Business Builder template free ($50 value). Plus, VIP members get early access to new templates, priority support, and a member title in the community."

Focus the pitch on the bonus, not the subscription. "Join to get Business Builder free" > "Subscribe for $25/week."

More bonuses = more sign-ups. Stack them.

### Continuity Discount (get them to commit)

"Pay $25/week month-to-month. Or commit for a year and keep $20/week for life."

Apply the discount spread over time, not up front. Offer a "lifetime discount" at your highest-churn month. If average retention is 4 months, offer at month 3: "You're about to unlock your lifetime rate. One more month and you're locked in at $20/week forever."

### Waived Fee (get them to stay)

- $100 setup fee for month-to-month. Waived with a 6-month commitment.
- If they cancel early, they pay the fee.
- "It costs us money to onboard you. If you commit, we cover it. If you leave early, you cover it. Fair enough?"
- Fee should be 3-5x the weekly rate. $100 is 4x $25.

### Template Unlock Cadence (retention engine)

Each month you stay, unlock one premium template permanently. After 12 months, you own the full library even if you cancel. This is the title/status play -- "Month 6 member: you've unlocked Campaign Planner, Event Coordinator, and Content Engine."

---

## What NOT To Do

1. **Don't discount.** If someone wants Pro for less, downsell features -- never the same thing for less.
2. **Don't launch all four stages at once.** Start with the Decoy Offer. Get it working reliably. Then add upsells. Then downsells. Then continuity.
3. **Don't make the free tier too good.** It should be genuinely useful but create a clear problem: "I finished my Research Brief but now I need Business Builder, and that requires Pro."
4. **Don't hide pricing.** Transparency is the moat. Show exactly what agents cost (BYOLLM), what Sforza costs ($25/week), and what each template run costs (estimated in YAML).

---

## Implementation Priority

**Phase 1** (launch): Decoy Offer only. Free CLI + Research Brief vs. Pro with Dashboard.

**Phase 2** (month 2-3): Add BAMFAM upsell (Orchestrator suggests next template). Add Rollover Upsell for template-to-template progression.

**Phase 3** (month 4-6): Add Feature Downsells and Trial With Penalty. Add Premium Templates marketplace (30% rev share).

**Phase 4** (month 6+): Add Continuity Bonus, Continuity Discount, Waived Fee. Add template unlock cadence.
