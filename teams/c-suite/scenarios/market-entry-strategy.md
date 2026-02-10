# Scenario: Planning Market Entry for a New Geography or Segment

## Context

An existing business wants to expand into a new market -- either a new geographic region (e.g., US company entering Europe) or a new customer segment (e.g., SMB product moving to enterprise). This scenario requires evaluating market attractiveness, adapting the existing business model, identifying regulatory and operational requirements, and building a phased entry plan with clear go/no-go decision points.

## Trigger

The user has an existing business and wants to evaluate or plan expansion. Typical triggers:
- Board or investors asking for a growth plan beyond the current market
- Inbound demand from a new geography or customer segment
- Current market approaching saturation or facing competitive pressure
- Strategic opportunity (partnership, acquisition target, regulatory change)

CONFIG.local.md specifies `scenario: market_entry` with current market details and target market.

## Team Configuration

| Agent | Role in Scenario | Priority |
|-------|-----------------|----------|
| CEO / Strategy Lead | Evaluates strategic fit, makes go/no-go recommendation, defines entry mode | Primary |
| CMO / Marketing | Analyzes target market size, competitive landscape, customer differences | Primary |
| CFO / Finance | Models entry economics, investment required, payback timeline | Primary |
| VP Sales | Adapts sales process, pricing, and ICP for new market | Primary |
| General Counsel | Identifies regulatory requirements, compliance gaps, legal entity needs | Primary |
| COO / Operations | Plans operational requirements, hiring, infrastructure, partnerships | Supporting |
| CTO / Product | Assesses product adaptation needs, localization, technical requirements | Supporting |

## Workflow

### Phase 1: Market Attractiveness Assessment (~15 min)
- CEO defines the strategic rationale for market entry
- CEO identifies success criteria and go/no-go decision points
- CMO evaluates target market size (TAM/SAM/SOM for the new market)
- CMO maps the competitive landscape in the target market
- CEO assigns each specialist their market entry analysis scope

### Phase 2: Entry Analysis (~30-40 min, parallel)
- CMO produces target market analysis:
  - Market sizing specific to the new geography or segment
  - Competitive landscape differences from current market
  - Customer persona adaptations (different pain points, buying behavior, objections)
  - Positioning adjustments needed for the new market
  - Channel strategy for the target market
- CFO models entry economics:
  - Investment required for market entry (one-time and ongoing)
  - Revenue ramp assumptions for the new market (slower than current market)
  - Break-even timeline for the new market
  - Impact on overall company financials (cash flow, runway)
  - Scenario analysis: best, base, worst case for market entry
- VP Sales adapts the sales approach:
  - ICP differences in the new market
  - Pricing adjustments (purchasing power, competitor pricing, willingness to pay)
  - Sales process modifications (longer cycles, different decision-makers, RFP processes)
  - Channel partner requirements in the target market
  - Sales team needs (local hires, language, cultural considerations)
- General Counsel identifies legal requirements:
  - Entity formation needs in the target jurisdiction
  - Regulatory compliance requirements (data privacy, industry-specific)
  - Employment law differences (hiring in new jurisdiction)
  - Contract template adaptations (governing law, dispute resolution, local requirements)
  - Tax implications of operating in the new market
  - IP protection in the target jurisdiction
- CTO assesses product needs:
  - Localization requirements (language, currency, date formats, units)
  - Data residency and sovereignty requirements
  - Integration requirements specific to the target market
  - Performance and infrastructure needs (local hosting, CDN)
- COO plans operational setup:
  - Local team needs (roles, hiring timeline, remote vs office)
  - Operational infrastructure (banking, payroll, communication)
  - Partnership requirements (local resellers, service partners, consultants)
  - Support model adaptation (time zones, language, SLAs)

### Phase 3: Entry Strategy Synthesis (~15 min)
- CEO evaluates all specialist analyses against strategic criteria
- CEO selects entry mode:
  - Direct entry (own team, own operations)
  - Partnership (local partner handles distribution and/or operations)
  - Acquisition (buy a local player)
  - Hybrid (partner initially, transition to direct)
- CEO defines the phased entry plan with milestones and decision points
- CEO produces go/no-go recommendation with supporting rationale

### Phase 4: Cross-Functional Validation (~10 min)
- All specialists validate the entry plan against their domain analysis
- CFO confirms the financial model supports the chosen entry mode
- General Counsel confirms legal feasibility and timeline
- VP Sales confirms revenue assumptions for the new market
- Team identifies the 3 biggest risks and mitigation strategies

### Phase 5: Final Plan (~5 min)
- CEO locks the market entry plan
- CEO defines Phase 1 execution steps (first 90 days)
- CEO documents go/no-go decision criteria for expansion commitment

### Phase 6: Artifact Generation (~15 min)
- CEO produces market entry strategy document
- CFO produces entry financial model (standalone or extension of main model)
- CMO produces target market analysis with competitive map
- General Counsel produces compliance requirements for the target jurisdiction

## Expected Outputs

- Market entry strategy document (entry mode, phased plan, decision points)
- Target market analysis (size, competition, customer differences)
- Entry financial model (investment, revenue ramp, break-even, scenarios)
- Regulatory and compliance requirements for target jurisdiction
- Adapted ICP and sales process for the new market
- Pricing strategy for the new market with competitive positioning
- Operational setup plan (team, infrastructure, partnerships)
- Product adaptation requirements (localization, compliance, integrations)
- Risk register specific to market entry
- 90-day execution plan with milestones and go/no-go gates

## Estimated Cost

| Phase | Agents | Est. Tokens | Est. Cost |
|-------|--------|-------------|-----------|
| Market Attractiveness | 2-3 | ~40K | ~$5.00 |
| Entry Analysis | 6 parallel | ~300K | ~$20.00 |
| Entry Strategy Synthesis | 1 (CEO) | ~60K | ~$9.00 |
| Cross-Functional Validation | 5-6 | ~50K | ~$4.50 |
| Final Plan | 1 (CEO) | ~15K | ~$2.25 |
| Artifact Generation | 4-5 | ~60K | ~$5.50 |
| **Total** | | **~525K** | **~$46.25** |

Add 20% buffer: **~$56 effective total**. Costs are higher for regulated markets or complex geographies (add 30-50%).

## Go/No-Go Framework

The CEO evaluates market entry against these criteria:

| Criterion | Go Signal | No-Go Signal |
|-----------|-----------|-------------|
| Market size | SOM exceeds 2x entry investment within 3 years | SOM does not justify the investment |
| Competition | Clear positioning gap or underserved segment | Market dominated with high switching costs |
| Regulatory | Compliance achievable within 6 months and budget | Regulatory barriers require 12+ months or $100K+ |
| Product fit | Minor adaptations needed (localization, integrations) | Fundamental product changes required |
| Unit economics | CAC payback under 18 months in the new market | CAC payback exceeds 24 months |
| Team | Can hire or partner for local expertise within 3 months | No viable local talent or partners |
