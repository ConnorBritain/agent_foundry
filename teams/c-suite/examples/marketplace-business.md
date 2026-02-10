# Example: C-Suite Team Planning a Two-Sided Marketplace

## Scenario

**Company:** DesignBridge
**Product:** A two-sided marketplace connecting businesses with vetted freelance designers for on-demand design work (brand identity, UI/UX, marketing assets, packaging).
**Stage:** Early idea, founder has domain expertise
**Founders:** 1 founder (former design agency owner) + 1 technical advisor (part-time)
**Funding:** $30K personal savings, exploring bootstrapping vs pre-seed
**Target Market:** SMBs and startups that need design work but cannot afford a full-time designer or agency
**Planning Horizon:** 3 years

## Project Charter Inputs

```yaml
company_name: DesignBridge
business_type: Two-sided marketplace
stage: idea
industry: Creative Services / Freelance Marketplace
target_market:
  supply_side: Freelance designers (graphic, UI/UX, brand)
  demand_side: SMBs and startups (10-100 employees)
founders:
  - name: Priya Sharma
    role: CEO
    background: "12 years running a design agency, network of 200+ freelance designers"
    equity: 85%
  - name: Jake Morrison
    role: Technical Advisor (part-time)
    background: "Senior engineer at Upwork, built marketplace matching systems"
    equity: 15%
funding:
  current_cash: 30000
  seeking: undecided
  bootstrap_viable: true
  target_round: pre-seed
  target_amount: 750000
planning_horizon: 3
outputs:
  financial_model: true
  pitch_deck: true
  sales_playbook: true
  marketing_plan: true
  product_roadmap: true
  org_chart: true
  legal_checklist: true
```

## Team Execution

### Phase 1: Vision Alignment
**CEO Agent** defines:
- **Mission:** Connect businesses with exceptional freelance designers through a curated, quality-first marketplace
- **Vision:** Become the default destination for design talent, replacing the agency model for 80% of design needs
- **Strategic priorities:** (1) Solve the chicken-and-egg problem by starting supply-side with Priya's network, (2) Prove demand with 50 completed projects in first 3 months, (3) Achieve 40%+ repeat rate from demand side
- **Core hypothesis:** "We believe SMBs and startups will prefer a curated design marketplace over agencies (too expensive) and general freelance platforms (too noisy) because they want agency-quality work at freelance prices without the vetting headache"

### Phase 2: Specialist Deep-Dives

**CFO** produces:
- Revenue model: 20% platform commission on project value (15% from client, 5% from designer)
- Average project value: $2,500 (range $500-$15,000)
- Revenue per transaction: $500 (20% of $2,500)
- Year 1 revenue: $240K (40 projects/month x $500 avg commission x 12 months)
- Year 3 revenue: $3.6M (300 projects/month x $1,000 avg commission)
- Marketplace economics: GMV $18M by Year 3, 20% take rate = $3.6M revenue
- Funding analysis: bootstrappable to $15K MRR, raise $750K pre-seed to accelerate to $50K MRR
- Unit economics: $150 CAC (demand side), $50 CAC (supply side, leveraging Priya's network), LTV $2,500 (demand side, 5 projects over 18 months)

**CMO** produces:
- TAM: $45B (global graphic design services market)
- SAM: $6B (freelance design for SMBs in US/UK/EU)
- SOM: $18M (0.3% of SAM in 5 years, ~7,200 projects/month)
- Competitors: 99designs (contest model, race to bottom), Fiverr (volume, low quality), Toptal (premium, enterprise-focused), direct agency hiring
- Positioning: "Agency quality, freelance speed, fair pricing for both sides"
- Supply-side strategy: Priya's network (first 50 designers), referral program, design community outreach
- Demand-side strategy: content marketing (design tips for startups), Product Hunt launch, startup community partnerships
- Key insight: most marketplaces fail by focusing on demand first -- DesignBridge starts supply-side (Priya's unfair advantage)

**CTO** produces:
- MVP scope: project brief submission, designer matching (manual initially), project workspace, payment escrow, review system
- MVP timeline: 10 weeks (4 weeks core platform, 3 weeks payment + escrow, 3 weeks matching + communication)
- Tech stack: Next.js + Supabase + Stripe Connect (for marketplace payments) + Vercel
- Build vs buy: buy payments (Stripe Connect), buy messaging (built on Supabase realtime), build matching algorithm (start manual, automate with AI later)
- Key risk: payment escrow complexity -- Stripe Connect handles 90% but dispute resolution is custom
- Product-market fit signal: 40%+ of demand-side clients post a second project within 60 days

**VP Sales** produces:
- Demand-side ICP: startups and SMBs, 10-50 employees, recently funded or growing, no in-house design team, spending $2K-10K/month on ad hoc design
- Supply-side ICP: freelance designers with 3+ years experience, portfolio quality score 7+/10, reliable availability, strong communication skills
- Pricing model: fixed-price projects (not hourly), designer sets price, platform adds 15% client fee
- No traditional sales team needed initially -- marketplace is self-serve
- Growth lever: account management for high-volume clients ($5K+/month in projects)
- Activation metrics: demand side posts first brief within 24 hours of signup, supply side completes profile within 48 hours

**COO** produces:
- Current org: 1 founder full-time + 1 technical advisor part-time
- Critical role: "marketplace operations manager" -- handles onboarding, quality disputes, designer vetting
- 6-month org: +1 full-stack engineer (full-time), +1 ops/community manager, +1 part-time design curator
- 12-month org: +1 engineer, +1 demand-side marketing, +1 supply-side community, Jake goes full-time
- Key process: designer vetting (portfolio review, test project, quality score assignment)
- Key process: dispute resolution (clear escalation path, 48-hour resolution SLA)
- Metric dashboard: GMV, take rate, supply/demand ratio, project completion rate, repeat rate, NPS

**General Counsel** produces:
- Entity: Delaware C-Corp if raising, Wyoming LLC if bootstrapping initially (convert later)
- Marketplace-specific legal:
  - Designers are independent contractors, NOT employees (critical classification issue)
  - Terms of Service must include: platform is facilitator not employer, IP transfers on payment, dispute resolution process
  - Payment processing compliance: Stripe Connect handles PCI DSS and money transmission
  - Need a 1099-K reporting process for designers earning $600+
- IP: trademark "DesignBridge," platform code is proprietary, designer work IP transfers to client on payment
- Key risk: designer misclassification as employees (Dynamex/ABC test in California)
- Insurance: general liability + E&O for marketplace disputes
- Compliance: FTC endorsement guidelines for reviews, DMCA process for IP disputes

### Phase 3: CEO Synthesis
**Conflicts resolved:**
1. CFO recommended bootstrapping vs CMO wanting $750K for demand generation → CEO decided: bootstrap to 50 completed projects (proof of concept), then raise $750K to accelerate
2. CTO wanted 10-week MVP vs VP Sales wanting more matching features → CEO decided: MVP ships in 10 weeks with manual matching, AI matching in v2
3. COO wanted to hire full-time engineer immediately vs CFO's cash constraints → CEO decided: contract developer for MVP ($15K), full-time hire after funding

### Phase 4-5: Board Review and Iteration
- CFO challenged 40 projects/month by Month 6 -- marketplace liquidity takes longer → adjusted to 20 projects/month, ramping to 40 by Month 9
- General Counsel flagged California AB5 risk for designers → CEO decided to consult employment attorney ($3K) before launch
- CMO challenged supply-side: 200-designer network is an advantage, but retention matters more than acquisition → added designer NPS and retention tracking

## Deliverables

```
output/
  designbridge/
    01-executive-summary.md
    02-business-plan.md
    03-financial-model.gsheet
      - Summary Dashboard
      - Marketplace Economics (GMV, take rate, revenue)
      - P&L (Monthly Y1, Quarterly Y2-3)
      - Cash Flow (bootstrap scenario + funded scenario)
      - Unit Economics (demand-side + supply-side)
      - Hiring Plan
      - Sensitivity Analysis
    04-pitch-deck.gslides
      - 11 slides with marketplace-specific metrics
    05-go-to-market/
      - market-analysis.md
      - competitive-landscape.md
      - supply-side-strategy.md
      - demand-side-strategy.md
      - customer-personas.md (demand + supply)
      - positioning-framework.md
    06-product/
      - mvp-specification.md
      - product-roadmap.md
      - matching-algorithm-plan.md
      - tech-stack.md
    07-sales/
      - marketplace-growth-playbook.md
      - pricing-strategy.md
      - activation-metrics.md
      - high-value-account-playbook.md
    08-operations/
      - org-chart-current.md
      - org-chart-12month.md
      - designer-vetting-process.md
      - dispute-resolution-process.md
      - vendor-assessment.md
    09-legal/
      - entity-recommendation.md
      - contractor-classification-analysis.md
      - compliance-checklist.md
      - marketplace-terms-of-service-framework.md
      - ip-transfer-policy.md
      - risk-register.md
    10-strategic-recommendations.md
```

## Cost Estimate

| Phase | Agents | Tokens | Cost |
|-------|--------|--------|------|
| Vision Alignment | 1 (CEO/Opus) | ~55K | ~$8.25 |
| Specialist Deep-Dives | 6 (Sonnet) | ~400K | ~$24.00 |
| CEO Synthesis | 1 (CEO/Opus) | ~90K | ~$13.50 |
| Board Review | 7 (all) | ~110K | ~$11.00 |
| Iteration | 2-3 | ~35K | ~$4.00 |
| Artifact Generation | 7 (all) | ~130K | ~$13.00 |
| **Total** | | **~820K** | **~$73.75** |

Effective total with 20% buffer: **~$88**. Higher than the SaaS example due to two-sided marketplace complexity (dual personas, dual acquisition strategies, marketplace economics).

## Expected Outcomes

After running this example, the founder would have:
- A clear strategy for solving the chicken-and-egg problem (supply-first, leveraging Priya's network)
- Two financial scenarios: bootstrap path (slower, capital-efficient) and funded path (faster, requires $750K)
- Marketplace-specific metrics framework: GMV, take rate, liquidity ratio, repeat rate
- A legal analysis addressing the critical contractor classification risk
- A phased product roadmap: manual matching (MVP) to AI matching (v2) to full automation (v3)
- A 90-day plan: onboard 50 designers from network (weeks 1-4), launch MVP (weeks 5-10), complete 50 projects (weeks 11-16)
- Clarity on the 3 things that must be true: (1) designers stay on platform (not go direct), (2) 40%+ of clients reorder within 60 days, (3) platform take rate is sustainable at 20%
