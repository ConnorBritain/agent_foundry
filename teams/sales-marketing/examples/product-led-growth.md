# Example: Product-Led Growth — Developer Tool

## Project Overview

Launch PLG motion for "QueryLens" — a database query optimization tool for developers. Freemium model with self-serve upgrade. No sales team needed initially.

## Configuration

```yaml
business_model: b2b_saas
sales_motion: product_led
deal_size: smb
sales_cycle_days: 7  # Self-serve, credit card on website
target_customer:
  industry: technology
  company_size: 1-500 employees
  job_titles: [Software Engineer, DBA, Backend Developer, DevOps]
channels:
  paid: [google_ads]
  organic: [seo, content_marketing, community]
  direct: [partnerships]
goals:
  signups_per_month: 1000
  free_to_paid_rate: 0.05
  cac_target: 50
  ltv_target: 1200
  payback_period_months: 1
```

## How the Team Adapts for PLG

### Coordinator shifts strategy:
- No outbound sales — all self-serve
- Focus on activation metrics, not MQLs
- Community and content > paid ads
- Product is the primary sales tool

### Demand Generation focuses on:
- SEO content: "How to optimize slow Postgres queries" (targets developers searching for solutions)
- Developer community: DEV.to articles, Hacker News launches, Reddit presence
- Google Ads: Only high-intent ("database query optimizer", "slow SQL fix")
- No LinkedIn or Meta ads (wrong audience for dev tools)

### Sales Enablement pivots to:
- In-app onboarding flows (not pitch decks)
- Documentation and tutorials (not battle cards)
- Usage-based upgrade prompts (not sales calls)
- Self-serve comparison page on website

### Pipeline Manager tracks:
- Signup → Activation (first query analyzed) → Habit (3 queries/week) → Conversion (paid plan)
- No CRM stages — product analytics replaces CRM
- Cohort analysis by signup source and activation rate

### Customer Success automates:
- Automated email sequence triggered by behavior:
  - Day 0: Welcome + quick start guide
  - Day 1 (no activation): "Here's how to analyze your first query"
  - Day 3 (activated): "Pro tip: Set up automated monitoring"
  - Day 7 (power user): "You've optimized 15 queries — unlock unlimited with Pro"
  - Day 14 (inactive): "We miss you — here's what's new"
- Health score is purely product-usage based

### Growth Analyst focuses on:
- Activation funnel: Signup → Install → First query → Aha moment
- Conversion triggers: What behavior predicts upgrade?
- Viral coefficient: How many users invite teammates?
- Content attribution: Which blog posts drive signups?

## Key Metrics Dashboard

| Metric | Month 1 | Month 3 | Month 6 |
|--------|---------|---------|---------|
| Signups | 400 | 1,200 | 3,000 |
| Activation rate | 35% | 45% | 55% |
| Free → Paid | 3% | 5% | 7% |
| Paying customers | 12 | 60 | 210 |
| MRR | $600 | $3,000 | $10,500 |
| CAC (blended) | $30 | $25 | $18 |
| Viral coefficient | 0.2 | 0.4 | 0.6 |

## Cost: ~$75

Lower than typical because PLG reduces need for heavy sales enablement and pipeline management. Growth Analyst and Demand Generation (content-focused) do the heavy lifting.
