# Scenario: Creating a Complete Business Plan for a New Startup

## Context

A founder or founding team has an idea for a new business and needs a comprehensive, investor-ready business plan. The business may be at the idea stage, have a prototype, or have early traction. The founder wants a plan that covers strategy, finance, marketing, product, operations, sales, and legal -- produced as an integrated, internally consistent set of documents and artifacts.

This is the primary scenario for the C-Suite Team and exercises all 7 agents across all 6 phases.

## Trigger

The user provides a completed `CONFIG.local.md` with:
- Business idea description and target market
- Founder backgrounds and equity splits
- Stage (idea, prototype, early revenue)
- Funding status and goals
- Planning horizon (typically 3-5 years)
- Output preferences (which artifacts to generate)

## Team Configuration

| Agent | Role in Scenario | Priority |
|-------|-----------------|----------|
| CEO / Strategy Lead | Defines vision, synthesizes plan, resolves conflicts | Primary |
| CFO / Finance | Builds financial model, unit economics, funding requirements | Primary |
| CMO / Marketing | Market analysis, positioning, go-to-market strategy | Primary |
| CTO / Product | MVP definition, product roadmap, technical architecture | Primary |
| COO / Operations | Org design, process maps, hiring sequence | Primary |
| VP Sales | ICP, sales process, pricing strategy, pipeline model | Primary |
| General Counsel | Entity formation, compliance, IP, contracts | Primary |

## Workflow

### Phase 1: Vision Alignment (~15 min)
- CEO reads and validates CONFIG.local.md
- CEO defines mission, vision, and 3 strategic priorities
- CEO writes board brief with context, constraints, and success criteria
- CEO assigns 2-4 targeted questions to each specialist
- Quality Gate 1: Config valid, vision defined, brief distributed

### Phase 2: Specialist Deep-Dives (~25-40 min, parallel)
- CFO builds P&L, cash flow, cap table, unit economics, hiring budget
- CMO calculates TAM/SAM/SOM, maps competitors, defines personas, designs GTM
- CTO defines MVP scope, builds roadmap, recommends tech stack, assesses risks
- COO designs org charts, role definitions, process maps, metrics dashboard
- VP Sales defines ICP, designs sales process, creates pricing strategy, builds pipeline model
- General Counsel recommends entity, builds compliance checklist, develops IP strategy
- Quality Gate 2: All specialists delivered, internal consistency verified

### Phase 3: CEO Synthesis (~15-20 min)
- CEO reads all 6 specialist outputs
- CEO identifies cross-functional conflicts (budget, timeline, scope, pricing)
- CEO resolves each conflict with binding decision and documented rationale
- CEO produces integrated business plan narrative
- Quality Gate 3: All conflicts resolved, plan internally consistent

### Phase 4: Board Review (~15 min, parallel)
- All 7 agents review the integrated plan from their domain perspective
- Each specialist challenges assumptions, flags errors, proposes improvements
- Quality Gate 4: No factual errors, assumptions realistic, risks captured

### Phase 5: Iteration and Resolution (~10 min)
- CEO accepts or rejects proposed amendments
- CEO locks the final plan version
- Quality Gate 5: Plan locked, all amendments addressed

### Phase 6: Artifact Generation (~20-30 min, parallel)
- CFO produces financial model in Google Sheets
- CMO produces go-to-market plan in Notion
- CTO produces product roadmap in Linear or Notion
- COO produces org charts and process maps
- VP Sales produces sales playbook in Notion
- General Counsel produces compliance checklist and calendar in Notion
- CEO produces executive summary and pitch deck content
- Quality Gate 6: All artifacts produced, no placeholder text, numbers match

## Expected Outputs

- Executive summary (1-page)
- Integrated business plan narrative
- Financial model (Google Sheets: P&L, cash flow, cap table, unit economics, hiring plan, sensitivity)
- Go-to-market plan with channel strategy and content calendar
- Product roadmap with MVP specification
- Sales playbook with ICP, pipeline model, pricing, objection handling
- Org charts (current, 6-month, 12-month, 24-month)
- Compliance checklist and calendar
- IP strategy and risk register
- Pitch deck content (if enabled)
- Strategic recommendations and 90-day execution plan

## Estimated Cost

| Phase | Agents | Est. Tokens | Est. Cost |
|-------|--------|-------------|-----------|
| Vision Alignment | 1 (CEO) | ~50K | ~$7.50 |
| Specialist Deep-Dives | 6 parallel | ~350K | ~$21.00 |
| CEO Synthesis | 1 (CEO) | ~80K | ~$12.00 |
| Board Review | 7 parallel | ~100K | ~$10.00 |
| Iteration | 1-3 | ~included | ~included |
| Artifact Generation | 7 parallel | ~120K | ~$12.00 |
| **Total** | | **~700K** | **~$62.50** |

Add 20% buffer for iteration cycles: **~$75 effective total**.

## Variations

| Variation | Impact |
|-----------|--------|
| Idea stage (no traction) | More emphasis on market validation, less on scaling |
| Early revenue | CFO anchors projections to actual data, VP Sales uses real conversion rates |
| Regulated industry | General Counsel scope expands significantly, add 30% to cost |
| Hardware product | CTO scope includes supply chain, COO adds manufacturing processes |
| Non-profit | CFO models grants and donations, General Counsel addresses 501(c)(3) |
