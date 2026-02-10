# Example: B2B SaaS Go-to-Market — HR Analytics Tool

## Project Overview

Launch GTM for "PeopleMetrics" — a B2B SaaS HR analytics platform targeting mid-market companies (100-1,000 employees). $299/mo base, $999/mo enterprise.

## Configuration

```yaml
business_model: b2b_saas
sales_motion: hybrid  # Self-serve for base, sales-led for enterprise
deal_size: mid_market
sales_cycle_days: 45
target_customer:
  industry: horizontal (all industries with 100+ employees)
  company_size: 100-1000 employees
  job_titles: [VP People, Head of HR, CHRO, People Analytics Manager]
channels:
  paid: [linkedin_ads, google_ads]
  organic: [seo, content_marketing]
  direct: [outbound]
goals:
  mqls_per_month: 150
  sqls_per_month: 45
  cac_target: 800
  ltv_target: 12000
  payback_period_months: 8
```

## Phase 1: Strategy & Foundation

### Coordinator/VP Marketing outputs:
- **ICP document**: VP People at companies with 100-1,000 employees, currently using spreadsheets or basic HRIS for people analytics, pain points are attrition prediction and engagement measurement
- **Positioning**: "The people analytics platform that predicts attrition before it happens"
- **Channel strategy**: 60% LinkedIn (buyer personas active), 25% Google (high intent), 15% content/SEO (long-term)
- **Budget allocation**: $15K/month — $9K LinkedIn, $3.75K Google, $2.25K content

### Brand & Messaging outputs:
- **Messaging hierarchy**:
  - Company: "Make people decisions with confidence"
  - Product: "Predict attrition, measure engagement, retain top talent"
  - Feature: "AI-powered flight risk scoring" / "Real-time engagement pulse"
- **Value propositions by persona**:
  - VP People: "Reduce regrettable attrition by 30% with predictive analytics"
  - CHRO: "Board-ready people metrics in one dashboard"
  - People Analytics Manager: "Replace 20 spreadsheets with one platform"

## Phase 2: Pipeline Building

### Demand Generation outputs:
- **LinkedIn campaign**: Targeting VP People + Head of HR at 100-1K companies
  - Ad creative: "Your best people are about to leave. Here's how to know before they do."
  - Lead magnet: "2026 People Analytics Benchmark Report" (gated PDF)
  - Budget: $9K/month, target CPL: $45
- **Google Ads**: High-intent keywords ("people analytics software", "employee attrition prediction")
  - Budget: $3.75K/month, target CPL: $60
- **Landing pages**: 3 variants — feature-led, pain-led, social-proof-led

### Sales Enablement outputs:
- **Pitch deck** (12 slides): Problem → Solution → Demo → ROI → Social proof → Pricing → Next steps
- **Battle cards**: vs. Lattice, vs. Culture Amp, vs. spreadsheets
- **ROI calculator**: Input headcount + attrition rate → output: savings from reduced attrition
- **Demo script**: 15-min flow showing flight risk dashboard with sample data

### Pipeline Manager outputs:
- **CRM stages**: Lead → MQL → SQL → Discovery → Demo → Proposal → Negotiation → Closed Won/Lost
- **Required fields per stage**: Budget confirmed (Proposal), decision maker identified (Discovery)
- **Automation**: MQL scoring (downloads + pricing page + company size), auto-assign to AE

## Phase 3: Execution

### Growth Analyst outputs:
- **Attribution dashboard**: First-touch and multi-touch models
- **Weekly metrics report**:
  - LinkedIn: 3,200 impressions, 45 clicks, 12 leads, CPL $42
  - Google: 800 clicks, 8 leads, CPL $55
  - Content: 2,100 organic visits, 4 leads, CPL $0
- **A/B test results**: Pain-led landing page converts 2.1x vs feature-led

### Customer Success outputs:
- **Onboarding sequence**: Day 1 (welcome + data integration), Day 3 (first dashboard), Day 7 (team training), Day 14 (check-in), Day 30 (QBR)
- **Health score model**: Login frequency (30%) + features used (30%) + support tickets (20%) + NPS response (20%)
- **Expansion trigger**: Company crosses 500 employees → propose enterprise tier

## Results (Month 3 Projection)

| Metric | Target | Projected |
|--------|--------|-----------|
| MQLs/month | 150 | 135 |
| SQLs/month | 45 | 38 |
| Pipeline value | $200K | $175K |
| Deals closed | 8 | 6 |
| New ARR | $28K | $22K |
| Blended CAC | $800 | $920 |
| LTV:CAC ratio | 15:1 | 13:1 |

### Growth Analyst recommendations:
1. Increase LinkedIn budget 30% (best channel)
2. Kill feature-led landing page (worst performer)
3. Launch referral program (customers willing to recommend)
4. Test webinar as lead magnet (higher intent than PDF)

## Cost: ~$93
