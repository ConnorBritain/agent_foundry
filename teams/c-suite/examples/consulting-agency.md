# Example: C-Suite Team Setting Up a Consulting Agency

## Scenario

**Company:** Meridian AI Consulting
**Product:** An AI consulting firm helping mid-market companies (100-1000 employees) implement AI solutions -- from strategy and use case identification through proof-of-concept development and production deployment.
**Stage:** Pre-launch, founder leaving corporate role
**Founders:** 1 founder (former AI/ML director at a Fortune 500) + 1 co-founder (former management consultant at McKinsey)
**Funding:** Not seeking external funding, bootstrapping from day one
**Target Market:** Mid-market companies in financial services, healthcare, and manufacturing that know they need AI but do not have in-house expertise
**Planning Horizon:** 3 years

## Project Charter Inputs

```yaml
company_name: Meridian AI Consulting
business_type: Professional services / Consulting
stage: pre-launch
industry: AI / Machine Learning Consulting
target_market: Mid-market companies (100-1000 employees) in financial services, healthcare, manufacturing
founders:
  - name: David Kim
    role: CEO / Practice Lead
    background: "15 years in AI/ML, Director of AI at JPMorgan, PhD in Machine Learning"
    equity: 60%
  - name: Laura Chen
    role: COO / Client Lead
    background: "10 years at McKinsey, engagement manager, MBA from Wharton"
    equity: 40%
funding:
  current_cash: 120000
  seeking: false
  bootstrap: true
  revenue_target_year1: 800000
planning_horizon: 3
outputs:
  financial_model: true
  pitch_deck: false
  sales_playbook: true
  marketing_plan: true
  product_roadmap: true
  org_chart: true
  legal_checklist: true
```

## Team Execution

### Phase 1: Vision Alignment
**CEO Agent** defines:
- **Mission:** Help mid-market companies capture the value of AI by providing end-to-end consulting from strategy through production deployment
- **Vision:** Become the trusted AI transformation partner for mid-market enterprises, bridging the gap between AI hype and business value
- **Strategic priorities:** (1) Land 3 anchor clients in first 90 days through founder networks, (2) Develop a repeatable engagement model that junior consultants can deliver, (3) Reach $65K MRR by Month 12
- **Core hypothesis:** "We believe mid-market companies in regulated industries will pay $200-400/hour for AI consulting because they cannot attract full-time AI talent, the big consultancies are too expensive ($500-800/hour), and the stakes of getting AI wrong in regulated industries are too high for DIY"

### Phase 2: Specialist Deep-Dives

**CFO** produces:
- Revenue model: time-and-materials billing + fixed-price projects + retainer agreements
- Blended billing rate: $275/hour (partners at $400, senior consultants at $250, junior at $175)
- Utilization target: 70% billable (30% for sales, admin, professional development)
- Year 1 revenue: $780K (2 founders x 1,400 billable hours x $275 avg)
- Year 3 revenue: $3.2M (8 consultants, 65% utilization, $280 blended rate)
- Key metric: revenue per consultant per month ($10K minimum to sustain)
- Cash flow: positive from Month 1 if first client lands in Week 4 (no inventory, low overhead)
- No external funding needed: $120K covers 6 months of personal runway and startup costs
- Hiring plan: first junior consultant at $800K ARR, second at $1.2M ARR
- Profit margins: 25-35% operating margin at scale (consulting industry benchmark: 20-30%)

**CMO** produces:
- TAM: $35B (US AI consulting and implementation market)
- SAM: $4B (mid-market AI consulting, non-big-4)
- SOM: $8M (Year 5, ~30 consultants serving 50-70 clients)
- Competitors: Big 4 (Deloitte, Accenture -- too expensive for mid-market), boutique AI firms (few focused on mid-market), freelance ML engineers (no strategic layer)
- Positioning: "Big-firm AI expertise, boutique-firm attention, mid-market pricing"
- Primary channels: thought leadership (LinkedIn, conference speaking), referral network, industry-specific events
- Content strategy: weekly LinkedIn posts on AI implementation lessons, monthly case study, quarterly whitepaper
- Personas: "CTO Carlos" (100-person fintech, needs AI roadmap), "VP Operations Olivia" (300-person manufacturer, needs process automation)

**CTO** produces:
- Service offerings (the "product" for a consulting firm):
  - AI Readiness Assessment (2-week engagement, $25K fixed price)
  - AI Strategy Workshop (1-day, $8K, lead generation tool)
  - Proof of Concept Development (6-8 weeks, $60-100K)
  - Production Implementation (3-6 months, $150-400K)
  - AI Operations Retainer ($10-20K/month ongoing)
- Technology stack for internal operations: Notion (knowledge base), Linear (project tracking), Slack, Google Workspace
- Delivery methodology: assessment, design, build, deploy, optimize -- each phase has defined deliverables and quality gates
- IP development: build reusable frameworks and accelerators that reduce delivery time by 30-40% (key to scaling margins)
- Key risk: over-reliance on founder delivery -- must systematize methodology for junior consultants

**VP Sales** produces:
- ICP: mid-market companies (100-1000 employees), regulated industries (financial services, healthcare, manufacturing), IT budget $1M+, no in-house ML team, C-level AI mandate
- Sales process:
  - Lead source: founder network (primary), speaking engagements, referrals, LinkedIn thought leadership
  - Entry point: AI Strategy Workshop ($8K, low-commitment way to start)
  - Expansion: workshop leads to readiness assessment, then PoC, then implementation
  - Land-and-expand: average client relationship grows from $8K initial to $200K+ Year 1
- Pricing strategy:
  - Workshops: $8K fixed (entry point, break-even, designed to convert)
  - Assessments: $25K fixed (high margin, standardized delivery)
  - PoC: $60-100K fixed (moderate margin, customized)
  - Implementation: $200-400/hour T&M or $150-400K fixed (highest margin at scale)
  - Retainer: $10-20K/month (predictable revenue, 70%+ margin)
- Pipeline model: 3 workshops/month by Month 6, 40% convert to assessment, 60% of assessments convert to PoC, 70% of PoCs convert to implementation
- No dedicated sales hire needed Year 1 -- founders sell, Laura leads business development

**COO** produces:
- Current org: David (CEO/Practice Lead -- delivers technical work), Laura (COO/Client Lead -- manages clients, runs BD)
- 6-month org: +1 senior AI consultant (contract-to-hire, $180K salary), +1 part-time admin/bookkeeper
- 12-month org: +1 senior consultant, +1 junior consultant, +1 project manager (7 people total)
- 24-month org: +2 consultants, +1 BD/sales, +1 operations (11 people total)
- Key processes:
  - Client engagement lifecycle (proposal to invoice)
  - Knowledge management (reusable frameworks, templates, case studies)
  - Quality assurance (peer review of all deliverables)
  - Time tracking and billing (critical for T&M engagements)
- Vendor stack: QuickBooks (accounting), Gusto (payroll), Harvest (time tracking), HubSpot CRM (free tier)
- Hiring strategy: hire from AI/ML roles at large companies (they want consulting variety and autonomy)

**General Counsel** produces:
- Entity: LLC initially (pass-through taxation, simpler, no VC funding needed). Convert to S-Corp when revenue exceeds $150K for payroll tax optimization
- Key contracts (blocking):
  - Master Services Agreement (MSA) template for client engagements
  - Statement of Work (SOW) template for each project
  - Independent Contractor Agreement (for contract consultants)
  - Mutual NDA (clients require before sharing proprietary data)
  - IP Assignment Agreement (work product belongs to client, methodology belongs to firm)
- Professional liability: E&O insurance required ($1M minimum, ~$3-5K/year)
- Data handling: clients in financial services and healthcare require specific data handling provisions (BAA for HIPAA, encryption requirements, data retention policies)
- Non-compete: founders should have clean departures from current employers, no non-compete violations
- Regulatory: AI consulting has no specific licensing requirements, but deliverables in regulated industries must comply with industry regulations (HIPAA, SOX, etc.)
- Key risk: client data exposure during AI model training -- need clear data governance provisions in every MSA

### Phase 3: CEO Synthesis
**Conflicts resolved:**
1. CFO's conservative Year 1 revenue ($780K) vs VP Sales' optimistic pipeline ($1.1M) → CEO decided: plan for $780K, celebrate if $1.1M. Hire against $780K.
2. CTO wanted to invest in building proprietary AI frameworks early vs CFO's cash preservation → CEO decided: build reusable templates during client work (no separate R&D budget), formalize into frameworks after 5+ engagements
3. COO wanted to hire senior consultant in Month 3 vs CFO's preference for Month 6 → CEO decided: contract senior consultant in Month 3, convert to full-time in Month 6 if pipeline supports it

### Phase 4-5: Board Review and Iteration
- CFO flagged that 70% utilization in Year 1 is optimistic for founders also doing sales → adjusted to 60% Year 1, 70% Year 2+
- General Counsel flagged: former employer IP -- David must confirm no non-compete and no IP overlap with JPMorgan work → action item: legal review before launch
- CMO challenged: "thought leadership" is slow -- supplement with direct outreach to David's network → added 50 personal outreach emails in Week 1-2 to announce the firm

## Deliverables

```
output/
  meridian-ai-consulting/
    01-executive-summary.md
    02-business-plan.md
    03-financial-model.gsheet
      - Summary Dashboard
      - P&L (Monthly Y1, Quarterly Y2-3)
      - Cash Flow (bootstrap model)
      - Utilization Model (billable hours tracking)
      - Engagement Pipeline (deal stages and revenue)
      - Hiring Plan (with utilization impact)
      - Sensitivity Analysis
    04-go-to-market/
      - market-analysis.md
      - competitive-landscape.md
      - customer-personas.md
      - positioning-framework.md
      - thought-leadership-plan.md
      - content-calendar.md
    05-service-offerings/
      - service-catalog.md
      - ai-strategy-workshop-brief.md
      - readiness-assessment-framework.md
      - delivery-methodology.md
      - quality-assurance-process.md
    06-sales/
      - consulting-sales-playbook.md
      - pricing-strategy.md
      - proposal-template-guide.md
      - land-and-expand-framework.md
      - objection-handling.md
    07-operations/
      - org-chart-current.md
      - org-chart-12month.md
      - hiring-plan.md
      - client-engagement-process.md
      - knowledge-management-plan.md
      - vendor-assessment.md
    08-legal/
      - entity-recommendation.md
      - msa-key-terms.md
      - contractor-agreement-requirements.md
      - data-governance-policy.md
      - compliance-checklist.md
      - risk-register.md
    09-strategic-recommendations.md
```

## Cost Estimate

| Phase | Agents | Tokens | Cost |
|-------|--------|--------|------|
| Vision Alignment | 1 (CEO/Opus) | ~45K | ~$6.75 |
| Specialist Deep-Dives | 6 (Sonnet) | ~330K | ~$19.80 |
| CEO Synthesis | 1 (CEO/Opus) | ~75K | ~$11.25 |
| Board Review | 7 (all) | ~95K | ~$9.00 |
| Iteration | 2-3 | ~25K | ~$3.00 |
| Artifact Generation | 6 (all, no pitch deck) | ~100K | ~$10.00 |
| **Total** | | **~670K** | **~$59.80** |

Effective total with 20% buffer: **~$72**. Slightly lower than SaaS example because pitch deck is disabled and consulting has simpler product architecture.

## Expected Outcomes

After running this example, the founders would have:
- A bootstrap-viable business plan with clear path to profitability from Month 1
- A service catalog with defined offerings, pricing, and delivery methodology
- A financial model that tracks utilization (the core metric for consulting firms)
- A sales playbook built around the land-and-expand model (workshop to assessment to implementation)
- Legal foundation with MSA and SOW templates designed for regulated industry clients
- A hiring plan tied to revenue milestones (hire only when revenue supports it)
- A 90-day plan: announce firm and do direct outreach (weeks 1-2), land 3 anchor clients (weeks 3-8), deliver first workshops (weeks 9-12), convert to assessments (weeks 13-16)
- Clarity on the 3 things that must be true: (1) founders can close 3 clients from their network in 90 days, (2) workshop-to-assessment conversion exceeds 40%, (3) 60%+ utilization is achievable while also selling
