# Example: Deep Competitor Teardown of Project Management Tools

## Scenario

A mid-stage SaaS company building a project management tool for engineering teams needs a comprehensive competitive teardown. Their product is gaining traction with small teams but they are losing enterprise deals to established players. Leadership needs to understand exactly where they stand relative to competitors and where to invest next.

## Project Charter Inputs

- **Company:** BuildFlow (engineering project management tool, Series A, 500 paying customers)
- **Research Question:** How does BuildFlow compare to the top 7 competitors across features, pricing, market positioning, and customer satisfaction, and where should we invest to win enterprise deals?
- **Research Type:** Competitive
- **Domain:** Technology (SaaS / Project Management)
- **Competitors to Analyze:** Linear, Jira, Asana, Monday.com, Shortcut, ClickUp, Notion Projects
- **Target Audience:** CPO, CEO, and board of directors
- **Constraints:** Focus on engineering team use cases, $30 budget

## Team Execution

### Phase 1: Research Design (Lead Researcher, ~10 min)
- Defines evaluation framework with 8 dimensions:
  1. Core PM features (tasks, boards, sprints, roadmaps, timelines)
  2. Engineering-specific features (Git integration, CI/CD, incident management, code reviews)
  3. Enterprise features (SSO, SCIM, audit logs, custom roles, compliance)
  4. Pricing and packaging (per-seat cost, feature gating, enterprise pricing)
  5. Integrations ecosystem (number and quality of integrations)
  6. Customer sentiment (G2 score, Capterra rating, common complaints)
  7. Company metrics (funding, team size, revenue estimates, growth trajectory)
  8. Strategic direction (recent releases, roadmap signals, hiring patterns)
- Each competitor evaluated against all 8 dimensions for consistency
- Prioritizes enterprise features and engineering-specific features as most relevant to BuildFlow's competitive challenge

### Phase 2: Data Collection (Source Analyst, ~30 min)
- Researches each competitor systematically:
  - **Linear:** Product pages, changelog, G2 reviews (4.6/5, 1,200+ reviews), Crunchbase ($52M Series B), recent blog posts on enterprise features
  - **Jira:** Atlassian investor presentations, G2 reviews (4.3/5, 5,800+ reviews), pricing page, enterprise documentation
  - **Asana:** SEC filings (public company), G2 reviews (4.4/5, 9,500+ reviews), earnings call transcripts, feature comparison pages
  - **Monday.com:** SEC filings (public company), G2 reviews (4.6/5, 12,000+ reviews), pricing tiers, enterprise case studies
  - **Shortcut:** Product pages, G2 reviews (4.5/5, 400+ reviews), Crunchbase ($62M raised), API documentation
  - **ClickUp:** Product pages, G2 reviews (4.6/5, 9,000+ reviews), Crunchbase ($537M raised), pricing page
  - **Notion Projects:** Product pages, G2 reviews (4.7/5, 5,500+ reviews for Notion overall), recent PM feature announcements
- Collects 62 sources total across all competitors
- Gap: Linear and Shortcut do not publish enterprise pricing publicly (flagged as "contact sales")

### Phase 3: Analysis and Synthesis (Lead Researcher + Data Synthesizer + Fact Checker, ~25 min)
- Lead Researcher identifies competitive clusters:
  - **Engineering-first:** Linear, Shortcut (lean, developer-focused, opinionated workflows)
  - **Enterprise generalist:** Jira, Asana, Monday.com (broad feature set, deep enterprise capabilities)
  - **All-in-one:** ClickUp, Notion Projects (PM as part of broader workspace)
- Data Synthesizer builds comparison matrices:
  - Feature matrix: 45 features across 8 categories for all 7 competitors
  - Pricing comparison: normalized to per-seat/month at 50-seat and 200-seat team sizes
  - Enterprise readiness scorecard: SSO, SCIM, audit logs, SOC 2, custom roles, SLA
  - Customer sentiment analysis: top 3 praises and complaints per competitor from G2 reviews
- Data Synthesizer identifies BuildFlow's competitive gaps for enterprise:
  1. Missing SSO/SCIM (table stakes for enterprise, all 7 competitors have it)
  2. No audit logging (6/7 competitors offer this)
  3. Limited custom roles (only admin/member, competitors offer 4-8 role types)
  4. No SOC 2 certification (required for enterprise procurement)
- Data Synthesizer identifies BuildFlow's competitive advantages:
  1. Native Git integration depth (deeper than Asana, Monday, ClickUp, Notion)
  2. Developer experience and speed (comparable to Linear, ahead of Jira)
  3. Pricing 40% below enterprise generalists at 200-seat scale
- Fact Checker verifies: pricing figures (all current as of research date), G2 scores, funding amounts, feature availability

### Phase 4: Deliverable Production (Report Writer, ~20 min)
- Produces individual competitor profiles (1-2 pages each, 7 profiles)
- Creates comprehensive feature comparison matrix (45 features x 8 competitors including BuildFlow)
- Writes positioning analysis: BuildFlow sits between engineering-first and enterprise generalist clusters
- Produces executive briefing with the 4 enterprise gap priorities and investment recommendation
- Includes pricing comparison table normalized to common team sizes

## Deliverables

```
output/
  executive-briefing.md                 -- 3-page briefing with enterprise gap priorities
  competitive-teardown-report.md       -- 22-page comprehensive competitive analysis
  competitor-profiles/
    linear.md                          -- Linear profile (2 pages)
    jira.md                            -- Jira profile (2 pages)
    asana.md                           -- Asana profile (2 pages)
    monday.md                          -- Monday.com profile (2 pages)
    shortcut.md                        -- Shortcut profile (1.5 pages)
    clickup.md                         -- ClickUp profile (2 pages)
    notion-projects.md                 -- Notion Projects profile (1.5 pages)
  feature-comparison-matrix.md         -- 45-feature comparison across all 8 products
  pricing-comparison.md                -- Normalized pricing at 50 and 200-seat scales
  enterprise-readiness-scorecard.md    -- Enterprise feature gap analysis with priorities
  customer-sentiment-analysis.md       -- G2/Capterra sentiment summary per competitor
  source-database.md                   -- 62 sources with credibility tiers
```

## Cost Estimate

| Phase | Model Mix | Tokens | Cost |
|-------|-----------|--------|------|
| Research Design | Opus (Lead Researcher) | ~20K | $3.00 |
| Data Collection | Sonnet (Source Analyst) | ~110K | $6.60 |
| Analysis & Synthesis | Opus (Lead Researcher) + Sonnet (Data Synthesizer) + Haiku (Fact Checker) | ~90K | $6.50 |
| Deliverable Production | Sonnet (Report Writer) | ~80K | $4.80 |
| **Total** | | **~300K** | **~$21** |

## Expected Outcomes

- CPO has a prioritized enterprise feature roadmap: SSO/SCIM first, then audit logging, then custom roles, then SOC 2
- CEO can articulate BuildFlow's positioning in enterprise sales conversations: "engineering-first PM with enterprise capabilities"
- Board presentation includes defensible competitive data showing BuildFlow's price advantage and Git integration depth
- Sales team receives competitor battle cards derived from the feature comparison matrix
- Product team understands which competitors to watch most closely (Linear and Shortcut in the engineering-first cluster)
- Follow-up research identified: customer win/loss analysis to validate which enterprise gaps are actually causing deal losses
