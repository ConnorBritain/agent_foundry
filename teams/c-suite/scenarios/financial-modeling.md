# Scenario: Building Financial Models and Projections for Fundraising

## Context

A startup is preparing to raise capital (pre-seed, seed, or Series A) and needs a rigorous financial model to support investor conversations. The model must demonstrate clear unit economics, realistic growth projections, defensible assumptions, and a credible path to profitability or next milestone. This scenario focuses heavily on the CFO agent with support from VP Sales (revenue assumptions) and CEO (strategic framing).

## Trigger

The user needs fundraising-ready financial projections. Typical triggers:
- Preparing for investor meetings or pitch competitions
- Need to determine how much capital to raise and at what valuation
- Existing business plan needs financial rigor for due diligence
- Board or advisors requesting detailed financial projections

CONFIG.local.md specifies `fundraising: true` with target round details.

## Team Configuration

| Agent | Role in Scenario | Priority |
|-------|-----------------|----------|
| CEO / Strategy Lead | Frames strategic context, validates milestone-funding alignment | Primary |
| CFO / Finance | Builds complete financial model, runs scenarios, sizes the round | Primary |
| VP Sales | Provides revenue assumptions, pipeline math, pricing validation | Supporting |
| CMO / Marketing | Provides CAC assumptions by channel, marketing budget needs | Supporting |
| CTO / Product | Provides build costs, technical hiring needs, infrastructure costs | Supporting |
| COO / Operations | Provides hiring plan timing and fully-loaded costs | Supporting |
| General Counsel | Provides entity and compliance cost estimates | Minimal |

## Workflow

### Phase 1: Strategic Framing (~10 min)
- CEO defines the fundraising narrative: what milestone will this round achieve?
- CEO sets constraints: target raise amount, acceptable dilution range, timeline
- CEO briefs CFO with strategic priorities for the financial model
- CEO asks VP Sales and CMO for revenue and CAC assumptions

### Phase 2: Model Construction (~30-40 min)
- CFO builds the core financial model:
  - Revenue model anchored to VP Sales' pipeline math and pricing
  - Expense model anchored to COO's hiring plan and CTO's build costs
  - P&L projection (monthly Year 1, quarterly Years 2-3 or 2-5)
  - Cash flow analysis with runway under each scenario
  - Cap table with pre-money valuation scenarios and dilution
  - Unit economics (CAC, LTV, LTV:CAC, payback period)
  - Sensitivity analysis on 5 key variables
- VP Sales validates revenue ramp assumptions and conversion rates
- CMO validates CAC projections by channel
- CTO validates engineering costs and infrastructure scaling costs

### Phase 3: Synthesis and Stress Testing (~15 min)
- CEO reviews the complete model for strategic coherence
- CFO presents three scenarios (best, base, worst case) to CEO
- CEO stress-tests: "What if conversion is 50% lower? What if churn doubles?"
- CEO validates that the funding ask covers the base case to next milestone
- CEO identifies the 3 numbers investors will challenge most

### Phase 4: Cross-Functional Validation (~10 min)
- VP Sales confirms revenue assumptions are achievable, not aspirational
- CMO confirms marketing budget supports the projected lead volume
- CTO confirms product can be delivered within the modeled timeline and budget
- COO confirms hiring can happen at the projected pace
- General Counsel confirms entity structure supports the proposed round

### Phase 5: Final Calibration (~5 min)
- CEO locks the base case as the primary fundraising model
- CFO documents every assumption with source or rationale
- CEO prepares the funding narrative: amount, use of proceeds, milestones

### Phase 6: Artifact Generation (~20 min)
- CFO produces the final Google Sheets model with formatted sheets, formulas, and charts
- CEO produces the financial summary section for the pitch deck
- CFO produces a standalone funding requirements one-pager

## Expected Outputs

- Complete financial model (Google Sheets):
  - P&L projection (3-5 years)
  - Cash flow analysis with runway
  - Cap table with dilution scenarios
  - Unit economics dashboard
  - Hiring plan with fully-loaded costs
  - Sensitivity analysis
  - Summary dashboard with key charts
- Funding requirements one-pager (amount, use of proceeds, milestones, valuation range)
- Financial narrative for pitch deck (3 key metrics, growth story, path to profitability)
- Assumption documentation (every number traced to source or rationale)

## Estimated Cost

| Phase | Agents | Est. Tokens | Est. Cost |
|-------|--------|-------------|-----------|
| Strategic Framing | 1 (CEO) | ~30K | ~$4.50 |
| Model Construction | 4-6 | ~250K | ~$18.00 |
| Synthesis / Stress Test | 2 (CEO + CFO) | ~60K | ~$9.00 |
| Cross-Functional Validation | 5-6 | ~60K | ~$5.00 |
| Final Calibration | 2 (CEO + CFO) | ~20K | ~$3.00 |
| Artifact Generation | 2 (CEO + CFO) | ~50K | ~$5.00 |
| **Total** | | **~470K** | **~$44.50** |

Add 20% buffer: **~$54 effective total**. Lower than full business plan because General Counsel and COO have reduced scope.

## Key Success Criteria

- Every revenue number traces back to pipeline math (leads x conversion x deal size)
- Every expense traces to a specific line item (role, tool, or service)
- Three scenarios are presented for all projections
- Runway is calculated on base-case revenue and worst-case expenses
- CAC payback period is under 18 months in the base case
- The funding ask covers at least 18 months of runway at base-case burn
- Assumptions are labeled, sourced, and easy to update with actuals
