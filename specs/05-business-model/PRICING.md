# Sforza Pricing

Concrete pricing structure, billing mechanics, and unit economics. All numbers are starting points to be tested -- Hormozi's rule: "Price new offers low enough that you will get lots of yeses. Use customer feedback to improve your product. Then, start raising the price until you stop making more money."

---

## Pricing Tiers

### Free (The Decoy)

| Feature | Included |
|---------|----------|
| Orchestrator core | Open-source |
| Projects | 1 at a time |
| Templates | Research Brief only |
| Interface | CLI only |
| Community templates | Yes |
| Dashboard | No |
| Decision Queue | CLI-only (text responses) |
| Notifications | None |
| Git checkpointing | No |
| Budget enforcement | No |
| Support | Community only |

**Purpose**: Genuinely useful. Proves the concept. Creates the problem that Pro solves ("I need the Dashboard and Business Builder template").

### Pro ($25/week)

| Feature | Included |
|---------|----------|
| Projects | Unlimited |
| Templates | All pro templates |
| Interface | Dashboard + CLI |
| Decision Queue | Full (button responses, priority sorting) |
| Notifications | System notifications |
| Git checkpointing | Yes |
| Budget enforcement | Yes |
| Cost tracking | 3-level hierarchy (agent/team/project) |
| Support | Priority |

**Purpose**: Everything a solo operator needs to run real projects.

### Enterprise ($200/week)

| Feature | Included |
|---------|----------|
| Everything in Pro | Yes |
| Custom template builder | Yes |
| Team collaboration | Multiple humans per project |
| SLA | 99.9% uptime guarantee |
| Priority queue | Yes |
| Audit trail export | Yes |
| Dedicated support | Slack channel |
| White-label option | Future |

**Purpose**: Anchor upsell. Makes Pro look like a steal. Some customers actually take it.

---

## Billing Mechanics

### 4-Week Billing Cycles (not monthly)

From Hormozi: There are 13 four-week cycles per year vs. 12 months. Same weekly price, 8.3% more annual revenue. At 20% margins, this adds ~41% to annual profit. Nobody notices.

- Pro: $25/week, billed every 4 weeks ($100 per cycle, 13 cycles = $1,300/year)
- Enterprise: $200/week, billed every 4 weeks ($800 per cycle, 13 cycles = $10,400/year)

### Processing Fee Pass-Through

"It's $25/week plus a 3% processing fee." Nobody has ever not bought because of a processing fee. 3% added to topline for no extra work goes straight to bottom line. At 10% margins, this adds 30% to profit.

### Two Forms of Payment

"Do you want a 3% discount? Give us a second form of payment in case anything happens to the first one." Reduces declined payments significantly. Try to get ACH as the second form.

### Align with Paydays

Charge on days people get paid. Run declined cards multiple times on billing day. Recovers ~1/3 of declined payments.

---

## Downsell Pricing

When someone balks at Pro ($25/week):

| Package | Price | What's Included | What's Removed |
|---------|-------|-----------------|----------------|
| Pro | $25/week | Everything | -- |
| Dashboard Lite | $15/week | Decision Queue + 3 core templates | Premium templates |
| Templates Only | $10/week | All templates, CLI-only | Dashboard |
| The Minimum | $5/week | Research Brief + CLI | Everything else |

**Never**: Offer Pro for less than $25/week. Change what they get, not what they pay.

---

## Template Pricing

### Included in Pro

Core templates that ship with Sforza:
- Research Brief (~$5-15 in API costs per run)
- Business Builder (~$80-300 in API costs per run)
- Campaign Planner (~$30-100 in API costs)

### Premium Templates ($20-50 one-time)

Domain-expert templates from community creators. Sforza takes 30%.

Examples:
- SaaS Launch Playbook ($40)
- Content Calendar Generator ($25)
- Competitive Intelligence Report ($30)
- Fundraising Deck Builder ($50)

---

## Annual/Commitment Pricing

### Prepaid Annual

$960/year (save 20% vs. weekly billing). Frame as: "It's $1,300 at the weekly rate. Prepay for the year and save $340. That's what most people do."

### 6-Month Commitment (Waived Fee)

- Month-to-month: $100 setup fee + $25/week
- 6-month commitment: Setup fee waived
- Cancel early: Pay the $100 fee

### Lifetime Discount

"Commit for a year and keep $20/week for life." Offer at the month of highest churn (typically month 3-4).

---

## Unit Economics

```
REVENUE PER CUSTOMER
  Billing:                    $25/week (4-week cycles, 13/year)
  Annual revenue:             $1,300
  Monthly effective:          ~$100

COSTS PER CUSTOMER
  CAC:                        ~$50 (content marketing, open-source, word of mouth)
  Monthly infrastructure:     ~$5 (hosting per user)
  Monthly support:            ~$5 (amortized)

30-DAY ECONOMICS
  Revenue:                    $100 (4 weekly payments)
  COGS:                       ~$10
  Gross profit:               $90
  Net after CAC:              $40
  Payback period:             <30 days  [MEETS HORMOZI RULE]

LIFETIME VALUE
  Average retention:          8 months (target)
  LTV:                        $1,300 x (8/12) = ~$867
  LTV:CAC:                    17:1 (target >3:1)  [EXCEEDS]

WITH UPSELLS
  +1 premium template ($40):  +$40
  +Annual commit discount:    $1,040 base
  LTV with upsells:           ~$1,100
  LTV:CAC:                    22:1  [EXCEEDS]
```

### The Hormozi 30-Day Test

One customer's first month ($100) covers:
- Their own CAC ($50)
- Cost to acquire one more customer ($50)

Remaining from month: $0 margin before upsells kick in.

With one upsell (template purchase or annual commit): margin turns positive and funds acquiring a third customer.

**Verdict**: Viable but tight at Stage I. Upsells (Stage II) are critical to making the unit economics comfortable.

---

## What to Test First

1. **Price sensitivity**: Does $25/week convert better than $20/week? What about $30?
2. **Free tier conversion**: What % of free users upgrade to Pro? Target: >5% within 30 days.
3. **Template completion**: Do users who complete a template run retain better? (Hypothesis: yes)
4. **Decision Queue engagement**: Do users who answer decisions within 24 hours retain better? (Hypothesis: yes, use this for Trial With Penalty criteria)
5. **BAMFAM conversion**: When the Orchestrator suggests the next template, what % start it?

---

## Pricing Principles

1. **Reward paying in full, don't punish paying over time.** Present the higher price first, then offer prepay as a discount.
2. **Never negotiate.** Feature downsell instead.
3. **Customers talk about price.** Every customer gets the same pricing for the same tier.
4. **The Minimum exists.** Always have a cheapest option. Name it "The Minimum."
5. **Raise prices until you stop making more money.** Start at $25/week. If close rates stay high, raise to $30.
6. **Show the Enterprise tier first.** On the pricing page, Enterprise -> Pro -> Free. The anchor makes Pro look cheap.
