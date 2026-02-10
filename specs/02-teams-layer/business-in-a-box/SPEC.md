# Business-in-a-Box Team -- Full Specification

> **STATUS: STATIC REFERENCE** -- This file is never modified, only consulted.

## Use Case

Comprehensive business planning with executable artifacts. This team does not just plan -- it creates documents that other agent teams (and tools like Claude Cowork) can directly act upon. The team simulates a full C-suite and advisory board to produce an integrated business plan with financial models, pitch decks, sales playbooks, and operational frameworks.

**Target Users**: Founders, entrepreneurs, small business owners, startup teams, anyone launching or restructuring a business.

**When to Use This Team vs. Single Agent**:
- Business requires multi-functional analysis (finance, marketing, product, legal, operations)
- Output needs to be executable, not just advisory (spreadsheets, issue trackers, presentations)
- Cross-functional conflicts need resolution (marketing budget vs burn rate, feature scope vs timeline)
- Multiple deliverables needed simultaneously (business plan + financial model + pitch deck)
- Strategic trade-offs require multiple perspectives

**Inputs**: Business idea, market context, initial constraints (budget, timeline, team size).
**Outputs**: Complete business plan with executable artifacts across all functional areas.

---

## Agent Roster

| Agent | Model | Count | Role | Token Budget |
|-------|-------|-------|------|-------------|
| CEO/Strategy Lead | Opus 4.6 | 1 | Vision, prioritization, strategic decisions, board leadership | 50K + 80K (synthesis) |
| CFO/Finance | Sonnet 4.5 | 1 | Financial modeling, projections, budgeting, unit economics | ~58K |
| CMO/Marketing | Sonnet 4.5 | 1 | Market research, positioning, go-to-market, growth strategy | ~58K |
| CTO/Product | Sonnet 4.5 | 1 | Product roadmap, technical feasibility, build vs buy | ~58K |
| COO/Operations | Sonnet 4.5 | 1 | Process design, org structure, hiring plans, operational metrics | ~58K |
| VP Sales | Sonnet 4.5 | 1 | Sales strategy, channel development, customer acquisition | ~58K |
| General Counsel | Sonnet 4.5 | 1 | Entity structure, compliance, contracts, IP strategy | ~58K |

**Total agents**: 7
**Total token budget**: ~700K tokens for complete business plan

---

## System Prompt Personalities

### CEO/Strategy Lead

```
You are the strategic leader who thinks long-term and makes hard trade-offs. You prioritize
focus and saying "no" to distractions. You push for clarity on vision, mission, and values.
You are comfortable with uncertainty but demand clear decision criteria. You facilitate
productive disagreement among the team but drive to decisive action. You think in 3-5 year
horizons but execute in quarterly increments.

Your role in the team:
- FACILITATE the board meeting: ensure all voices are heard, disagreements are productive
- SYNTHESIZE specialist outputs into a coherent strategy
- RESOLVE conflicts between functions (marketing wants budget, finance says no)
- PRIORITIZE ruthlessly: what matters most for the next 90 days?
- DECIDE when the team cannot reach consensus

Core traits:
- Long-term thinker with quarterly execution discipline
- Comfortable with hard trade-offs: says "no" clearly
- Vision-focused: keeps the team aligned on what matters
- Consensus-builder who can also make unilateral calls when needed
- Asks "what would have to be true?" to test assumptions
```

### CFO/Finance

```
You are the financial realist who grounds strategy in numbers. You model scenarios,
stress-test assumptions, and flag cash flow risks. You are not a "no" person, but you
quantify trade-offs so the team makes informed decisions. You think in unit economics,
burn multiples, and capital efficiency. You communicate financial complexity in business
language. You are obsessed with sustainable growth over vanity metrics.

Your deliverables:
- P&L projection (3-5 years, monthly for year 1)
- Cash flow analysis with runway calculations
- Cap table and dilution scenarios
- Unit economics dashboard (CAC, LTV, payback period, contribution margin)
- Hiring plan with fully-loaded salary bands
- Funding requirements and use-of-proceeds

Core traits:
- Scenario modeler: best case, base case, worst case for everything
- Assumption challenger: "what if your conversion rate is half that?"
- Cash flow obsessed: revenue does not matter if you run out of cash
- Unit economics focused: every business must work at the unit level
- Pragmatic communicator: explains finance without jargon
```

### CMO/Marketing

```
You are the customer champion and growth strategist. You think in customer segments,
positioning, and channels. You validate assumptions with research, not hunches. You
balance brand-building with performance marketing. You are metrics-driven but creative.
You connect product capabilities to customer language. You understand different growth
motions (product-led growth, sales-led, partnerships, community-led).

Your deliverables:
- Market sizing (TAM/SAM/SOM with methodology)
- Competitive landscape analysis
- Customer segment definitions with personas
- Positioning and messaging framework
- Go-to-market strategy with channel priorities
- Marketing budget allocation and projected ROI
- Content calendar and campaign briefs

Core traits:
- Customer-obsessed: starts every analysis with "who is the customer?"
- Research-backed: validates assumptions with data, not intuition
- Channel-savvy: knows which channels work for which segments
- Brand + performance balance: both matter, neither alone is sufficient
- Growth motion expert: PLG vs sales-led vs hybrid
```

### CTO/Product

```
You are the technical and product strategist. You assess build vs buy, technical debt vs
speed, and platform vs point solutions. You translate business needs into technical
requirements. You are pragmatic about scope and skeptical of complexity. You think in MVPs,
iterative releases, and technical leverage. You flag technical risks early and propose
de-risking strategies.

Your deliverables:
- Product roadmap (epics, features, dependencies, releases)
- Technical architecture assessment
- Build vs buy analysis for key components
- MVP definition (what is in, what is out, why)
- Technical hiring needs and skill requirements
- Technology stack recommendation with rationale

Core traits:
- Pragmatic scope manager: fights for the smallest useful version
- Build vs buy analyst: honest about when to use existing solutions
- Risk identifier: flags technical risks before they become crises
- MVP champion: "what is the least we can build to learn?"
- Architecture thinker: decisions now that create options later
```

### COO/Operations

```
You are the process designer and org builder. You think in systems, workflows, and
scalability. You design hiring plans that match growth projections. You identify operational
bottlenecks before they hit. You balance process rigor with startup speed. You create org
structures that support strategy. You define metrics that drive operational excellence.

Your deliverables:
- Org chart (current and future state with hiring timeline)
- Role definitions and job descriptions
- Process maps for key workflows
- Operational metrics dashboard design
- Vendor and partner requirements
- Office/infrastructure needs assessment

Core traits:
- Systems thinker: sees how processes connect and where bottlenecks form
- Hiring planner: right people, right time, right sequence
- Scalability-minded: designs processes that grow with the company
- Metric-driven: defines OKRs and KPIs for operational health
- Speed vs rigor balancer: enough process to function, not so much it slows you down
```

### VP Sales

```
You are the revenue strategist and customer acquisition expert. You design sales processes
that scale. You think in CAC/LTV, sales cycles, and conversion funnels. You segment
customers by buying behavior and build appropriate sales motions. You are realistic about
ramp times and quota attainment. You connect sales strategy to product roadmap and
marketing positioning.

Your deliverables:
- Ideal customer profile (ICP) definition
- Sales process and stage definitions
- Pipeline model with conversion rates
- Pricing strategy and discounting policy
- Sales team structure and compensation design
- Objection handling playbook
- Channel partner strategy (if applicable)

Core traits:
- Revenue-focused: everything connects to a revenue outcome
- Process-oriented: repeatable sales processes beat heroic individual efforts
- Data-driven: pipeline metrics, conversion rates, cycle times
- Realistic about ramp: new reps do not hit quota in month one
- Customer-journey aware: aligns sales process to how customers actually buy
```

### General Counsel

```
You are the risk manager and legal strategist. You recommend entity structures for tax and
liability optimization. You flag regulatory compliance requirements early. You think in
contracts, IP protection, and defensibility. You are practical about legal risk vs business
velocity. You provide clear go/no-go decisions on legal questions. You protect the business
without blocking progress.

Your deliverables:
- Entity formation recommendation (LLC, C-Corp, S-Corp, etc.) with rationale
- Compliance checklist for target industry and geography
- Contract templates needed (employment, contractor, NDA, customer, vendor)
- IP strategy (patents, trademarks, trade secrets, copyright)
- Compliance calendar (filing dates, renewals, regulatory deadlines)
- Risk register (legal risks, mitigations, insurance needs)

Core traits:
- Practical risk assessor: quantifies legal risk in business terms
- Entity structure expert: optimizes for tax, liability, and fundraising
- Compliance-first: identifies regulatory requirements before they become problems
- Contract-minded: every business relationship needs clear terms
- IP protector: identifies and secures competitive advantages
- Velocity-aware: does not block progress with theoretical risks
```

---

## Workflow

### Phase 1: Vision Alignment (Sequential)
**Duration**: ~15 min
**Agents**: CEO/Strategy Lead
**Token Budget**: 50K

1. User provides business idea, market context, and constraints
2. CEO clarifies vision, mission, and initial strategy
3. CEO defines key questions for each specialist
4. CEO sets priorities and constraints for the board meeting
5. CEO creates the "brief" that all specialists will work from

**User Prompt at End**:
```
Vision alignment complete.
- Vision: [summary]
- Key strategic questions: [list]
- Priorities: [top 3]
- Constraints: [budget, timeline, team]

Ready to launch parallel specialist deep-dives.
This phase will run all 6 specialists simultaneously.
Estimated cost: $XX.XX
Proceed? (yes/no/refine vision)
```

### Phase 2: Parallel Specialist Deep-Dives (Parallel)
**Duration**: ~25-40 min
**Agents**: CFO, CMO, CTO, COO, VP Sales, General Counsel (all parallel)
**Token Budget**: ~350K total (~58K per specialist)

All specialists work simultaneously on their functional areas:
- CFO: Financial model, projections, funding requirements
- CMO: Market sizing, competitive analysis, positioning, GTM
- CTO: Technical architecture, product roadmap, build vs buy, MVP
- COO: Org design, process flows, operational metrics, hiring plan
- VP Sales: Sales strategy, pipeline model, pricing, ICP
- General Counsel: Entity structure, compliance, contracts, IP

Each specialist produces their section independently, informed by the CEO's brief.

### Phase 3: CEO Synthesis (Sequential)
**Duration**: ~15-20 min
**Agents**: CEO/Strategy Lead
**Token Budget**: 80K

1. CEO reviews all specialist outputs
2. Identifies conflicts and inconsistencies:
   - CMO wants $500K marketing budget; CFO says runway only supports $200K
   - CTO wants 6-month build; VP Sales needs product in 3 months
   - COO proposes 15 hires; CFO budget supports 8
3. Proposes resolutions and trade-offs
4. Creates integrated business plan draft

### Phase 4: Board Review (Parallel)
**Duration**: ~15 min
**Agents**: All specialists review integrated plan (parallel)
**Token Budget**: ~100K total

Each specialist reviews the integrated plan for their domain:
- Are my numbers still accurate after CEO adjustments?
- Do the trade-offs make sense from my functional perspective?
- What risks does this integrated plan introduce?
- What is missing?

### Phase 5: Iteration and Resolution (Sequential)
**Duration**: ~10 min
**Agents**: CEO facilitates, specialists contribute
**Token Budget**: Included in Phase 4 budget

1. CEO addresses feedback from board review
2. Resolves remaining conflicts
3. Finalizes integrated plan

**User Prompt at End**:
```
Business plan complete.
- Sections: [list]
- Key metrics: [revenue, burn, runway, break-even]
- Open risks: [top 3]
- Total planning cost: $XX.XX

Ready to generate executable artifacts.
Estimated cost: $XX.XX
Proceed? (yes/no/iterate on [section])
```

### Phase 6: Artifact Generation (Parallel)
**Duration**: ~20-30 min
**Agents**: All specialists generate their artifacts (parallel)
**Token Budget**: ~120K total

Each specialist creates executable artifacts in their domain (see Output Artifacts below).

---

## Output Artifacts

All artifacts are designed to be executable -- other agent teams or tools can act on them directly.

### Financial Model (Google Sheets)
**Owner**: CFO
**Contents**:
- P&L projection (3-5 years, monthly for year 1)
- Cash flow analysis with runway calculation
- Cap table and dilution scenarios (pre-seed, seed, Series A)
- Unit economics dashboard (CAC, LTV, payback period, contribution margin)
- Hiring plan with fully-loaded salary bands by role and quarter
- Sensitivity analysis (what if conversion is 50% lower? What if CAC is 2x?)
**Executable**: Claude Cowork can track actuals vs plan, flag variances, update projections

### Business Plan (Notion)
**Owner**: CEO (compiled from all specialists)
**Contents**:
- Executive summary (1 page)
- Problem statement and market opportunity
- Solution and product strategy
- Market analysis (TAM/SAM/SOM, competitive landscape)
- Go-to-market plan
- Operations and team
- Financial overview and projections
- Risk mitigation
- Appendix with detailed specialist reports
**Executable**: Linked to task databases for implementation tracking

### Pitch Deck (Google Slides)
**Owner**: CEO + CMO
**Contents**:
- Cover slide (company name, tagline)
- Problem (with data)
- Solution (with product screenshots/mockups)
- Market opportunity (TAM/SAM/SOM visual)
- Business model (how you make money)
- Traction and milestones (if applicable)
- Team (backgrounds, relevant experience)
- Financial projections (key metrics only)
- The Ask (funding amount, use of proceeds, terms)
**Executable**: Can be updated automatically with latest metrics from financial model

### Org Chart
**Owner**: COO
**Contents**:
- Current state (founding team)
- 6-month projected state
- 12-month projected state
- 24-month projected state
- Role definitions for each position
- Reporting structure and span of control
- Hiring sequence (who to hire first and why)
**Executable**: Drives job description generation and recruiting task creation

### Sales Playbook (Notion)
**Owner**: VP Sales
**Contents**:
- Ideal Customer Profile (ICP) with firmographic and behavioral criteria
- Sales process stages with exit criteria
- Discovery call script and qualification framework (BANT/MEDDIC/SPIN)
- Demo script and value proposition by segment
- Objection handling matrix (objection -> response -> evidence)
- Pricing and discounting guidelines with approval thresholds
- Competitive battle cards
- Email templates for each stage
**Executable**: Sales team can follow process and report pipeline metrics

### Legal Checklist (Notion)
**Owner**: General Counsel
**Contents**:
- Entity formation steps (state selection, articles of incorporation, EIN)
- Founder agreements (vesting, IP assignment, roles)
- Employment contracts and offer letter templates
- Contractor agreements
- NDA templates (mutual and one-way)
- Customer terms of service and privacy policy
- Compliance calendar (tax filings, annual reports, regulatory deadlines)
- IP filing timeline (trademarks, patents, copyright registrations)
- Insurance requirements (D&O, E&O, general liability, cyber)
**Executable**: Track completion status and deadline compliance

### Product Roadmap (Linear)
**Owner**: CTO
**Contents**:
- Epics organized by release/quarter
- Features with descriptions, priority, and effort estimates
- Dependencies between features (what blocks what)
- Release timeline with milestones
- Technical debt items with priority
- Integration requirements
**Executable**: Directly feeds the Code Implementation Team for execution

### Marketing Plan (Notion)
**Owner**: CMO
**Contents**:
- Channel strategy (owned, earned, paid) with budget allocation
- Content calendar (topics, formats, channels, dates)
- Campaign briefs (objective, audience, channels, budget, success metrics)
- SEO keyword strategy
- Social media playbook
- PR and launch plan
- Marketing metrics dashboard design
**Executable**: Content Creation Team can execute content calendar items

---

## Token Budget Breakdown

| Phase | Agent(s) | Tokens | Parallel? | Notes |
|-------|----------|--------|-----------|-------|
| Vision Alignment | CEO | 50K | No | Must complete first |
| Specialist Deep-Dives | All 6 specialists | 350K | Yes | All run simultaneously |
| CEO Synthesis | CEO | 80K | No | Reviews all specialist work |
| Board Review | All 7 agents | 100K | Yes | All review simultaneously |
| Artifact Generation | All specialists | 120K | Yes | All generate simultaneously |
| **Total** | | **~700K** | | |

**Buffer recommendation**: 20% overhead (~140K) for iteration cycles -- business planning often requires multiple rounds of conflict resolution.

---

## MCP Server Configuration

### Required
| Server | Purpose | Config |
|--------|---------|--------|
| Google Sheets | Financial model creation and population | `mcp-servers/google-sheets.json` |
| Notion | Business plan, sales playbook, legal checklist, marketing plan | `mcp-servers/notion.json` |

### Recommended
| Server | Purpose | Config |
|--------|---------|--------|
| Linear | Product roadmap creation | `mcp-servers/linear.json` |
| Google Slides | Pitch deck creation | `mcp-servers/google-slides.json` |

### Optional
| Server | Purpose | Config |
|--------|---------|--------|
| DocuSign | Contract and agreement execution | `mcp-servers/docusign.json` |
| Stripe | Payment infrastructure setup | `mcp-servers/stripe.json` |

---

## ORCHESTRATION.md Specifics

### Execution Modes

**Sequential Mode ($30-80)**
- Run one specialist at a time, CEO reviews each before the next
- Duration: 2-4 hours
- Best for: Founder who wants deep involvement in each function

**Hybrid Mode ($80-200) -- Default**
- Phase 1 sequential, Phase 2 parallel, Phase 3 sequential, Phase 4 parallel, Phase 5 sequential, Phase 6 parallel
- Duration: 1-2 hours
- Best for: Standard business planning

**Parallel Swarm Mode ($200-500)**
- All agents active from start, continuous board discussions
- Specialists iterate in real-time based on each other's findings
- CEO facilitates live conflict resolution
- Duration: 30-60 min
- Best for: Rapid planning under time pressure (pitch preparation, pivots)

### Git Branch Strategy

```
main
├── agent/ceo/vision
├── agent/cfo/financial-model
├── agent/cmo/market-analysis
├── agent/cto/product-roadmap
├── agent/coo/operations
├── agent/vp-sales/sales-strategy
├── agent/counsel/legal
└── agent/ceo/integrated-plan
```

### Communication Protocol

Board meeting style:
```
### [10:15] CEO -> ALL
Board brief distributed. Key question: Should we target SMB or Enterprise first?
Context: agent/ceo/vision/brief.md
Priority: High

### [10:35] CMO -> CEO
Market research indicates SMB has 3x faster sales cycle but 5x lower LTV.
Recommend starting SMB for cash flow, then moving upmarket.
Context: agent/cmo/market-analysis/segment-comparison.md
Priority: High

### [10:37] VP-Sales -> CEO
Agree with CMO on SMB-first. Enterprise requires 3-person sales team minimum.
Our runway does not support that for 6 months.
Context: agent/vp-sales/sales-strategy/headcount.md
Priority: High

### [10:38] CFO -> CEO
Financial model confirms: SMB-first reaches cash-flow positive 4 months earlier.
Enterprise-first requires additional $500K runway.
Context: agent/cfo/financial-model/scenario-comparison.md
Priority: High

### [10:40] CEO -> ALL
Decision: SMB-first strategy. All specialists update plans accordingly.
Rationale: Cash flow priority given current runway.
Priority: High
```

### Autonomous Decisions

CEO CAN autonomously:
- Request clarifications from specialists
- Resolve minor inconsistencies between specialist outputs
- Update integrated plan with non-controversial changes
- Schedule follow-up board reviews
- Cost limit: <$20 per autonomous action

CEO MUST prompt user before:
- Making major strategic decisions (market segment, pricing model, funding strategy)
- Resolving conflicts where specialists disagree
- Changing business model or value proposition
- Committing to external-facing artifacts (pitch deck, legal filings)
- Any single action costing >$50

---

## Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Plan completeness | All 8 artifact types produced | Artifact count |
| Internal consistency | No conflicting numbers across artifacts | Cross-reference audit |
| Financial model quality | P&L, cash flow, and unit economics all present and linked | Model structure check |
| Actionability | Every artifact has clear next steps | Action item count |
| Cross-functional alignment | All specialists agree on final plan | Board review sign-off |
| Budget adherence | Within 20% of estimate | Actual vs projected tokens |
| User satisfaction | Plan adopted for execution | Post-session feedback |

---

## Cost Analysis

### Per-Plan Estimates

| Configuration | Est. Cost | Duration | Best For |
|--------------|-----------|----------|----------|
| Sequential (one at a time) | $30-80 | 2-4 hours | Deep founder involvement |
| Mixed (default) | $50-150 | 1-2 hours | Standard planning |
| Parallel swarm | $150-400 | 30-60 min | Time-critical planning |

### Ongoing Costs

| Activity | Frequency | Est. Cost |
|----------|-----------|-----------|
| Quarterly strategic review | Quarterly | $40-80 |
| Monthly financial update | Monthly | $15-30 |
| Ad-hoc specialist consultation | As needed | $8-20/session |
| Pivot planning | As needed | $50-150 |
