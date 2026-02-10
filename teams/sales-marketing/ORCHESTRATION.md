# Orchestration Guide

## Execution Overview

The Sales & Marketing team operates in four sequential phases. Within each phase, agents work in parallel where possible and sequentially where dependencies exist. The Coordinator agent manages orchestration, resolves conflicts, and ensures quality gates pass before advancing to the next phase.

```
Phase 1: Strategy & Foundation    ──→  Phase 2: Pipeline Building
       (~30 min, sequential)              (~45 min, parallel)
                                              │
Phase 4: Analysis & Iteration     ←──  Phase 3: Execution & Optimization
       (~20 min, parallel)                (~60 min, parallel)
```

**Total estimated duration**: ~2.5 hours (with parallel execution enabled)
**Sequential execution duration**: ~4 hours

---

## Phase 1: Strategy & Foundation (Sequential - ~30 min)

### Purpose
Establish the strategic foundation that all subsequent work builds upon. Every decision made in later phases traces back to this phase. Getting this wrong means wasting time and budget in phases 2-4.

### Execution Order

```
Step 1: Coordinator defines GTM strategy
           │
           ▼
Step 2: Brand & Messaging creates messaging framework
           │
           ▼
Step 3: Growth Analyst sets up analytics foundation
```

### Step 1: Coordinator - GTM Strategy (~15 min)

**Inputs**: CONFIG.md (business context, target customer, goals)

**Activities**:
1. Analyze the target market and competitive landscape
2. Define buyer personas with demographics, psychographics, pain points, and buying journey
3. Develop positioning strategy: category, differentiation, and proof points
4. Map the customer journey from awareness through advocacy
5. Define channel strategy with budget allocation rationale
6. Set specific, measurable campaign objectives tied to pipeline goals
7. Create the strategic brief that all agents will reference

**Outputs**:
- `workspace/strategy/gtm-strategy.md` - Complete GTM strategy document
- `workspace/strategy/personas/` - Buyer persona profiles
- `workspace/strategy/competitive-analysis.md` - Competitive landscape and positioning
- `workspace/strategy/budget-allocation.md` - Channel budget allocation with rationale

**Quality Gate**:
- [ ] Strategy covers market analysis, personas, positioning, channels, and metrics
- [ ] Budget allocation sums to monthly budget with per-channel justification
- [ ] Personas include pain points, buying triggers, and objections
- [ ] Success metrics are specific, measurable, and tied to CONFIG goals

### Step 2: Brand & Messaging - Core Framework (~8 min)

**Inputs**: GTM strategy, personas, competitive analysis from Step 1

**Activities**:
1. Define brand positioning statement (for [target], who [need], [product] is a [category] that [key benefit], unlike [alternatives], we [differentiator])
2. Build messaging hierarchy: tagline, primary value prop, supporting value props, proof points
3. Create persona-specific messaging variants
4. Map features to benefits to outcomes for each persona
5. Define brand voice and tone guidelines
6. Build the messaging library that all agents will reference

**Outputs**:
- `workspace/messaging/positioning.md` - Brand positioning statement
- `workspace/messaging/value-props.md` - Value proposition framework
- `workspace/messaging/messaging-hierarchy.md` - Complete messaging hierarchy
- `workspace/messaging/brand-voice.md` - Voice and tone guidelines

**Quality Gate**:
- [ ] Positioning statement follows the standard framework and is differentiated
- [ ] Each value prop has supporting proof points
- [ ] Persona-specific variants exist for each defined persona
- [ ] Feature-benefit-outcome mapping covers all key features

### Step 3: Growth Analyst - Analytics Foundation (~7 min)

**Inputs**: GTM strategy, channel strategy, success metrics

**Activities**:
1. Design the attribution model (first-touch, last-touch, multi-touch, or custom)
2. Define KPIs for each funnel stage with targets and measurement methods
3. Specify dashboard requirements for each stakeholder
4. Create the experiment framework (hypothesis template, sample size calculator, significance thresholds)
5. Define data collection requirements for each channel and tool

**Outputs**:
- `workspace/analytics/attribution-model.md` - Attribution model specification
- `workspace/analytics/kpi-definitions.md` - KPI definitions with targets
- `workspace/analytics/dashboard-specs.md` - Dashboard requirements
- `workspace/analytics/experiment-framework.md` - A/B test framework

**Quality Gate**:
- [ ] Attribution model is specified with touchpoint weighting methodology
- [ ] KPIs cover awareness, acquisition, activation, retention, revenue, referral
- [ ] Dashboard specs answer the top 10 leadership questions
- [ ] Experiment framework includes sample size and significance requirements

---

## Phase 2: Pipeline Building (Parallel - ~45 min)

### Purpose
Build all the assets, infrastructure, and playbooks needed for execution. Four agents work in parallel, each building within their domain while referencing the shared strategy and messaging from Phase 1.

### Execution Map

```
        ┌─── Demand Generation: Campaigns, landing pages, ad creative
        │
Phase 1 ├─── Sales Enablement: Pitch decks, battle cards, demo scripts
Output  │
        ├─── Pipeline Manager: CRM setup, stage definitions, reporting
        │
        └─── Customer Success: Onboarding, health scoring, expansion
```

### Demand Generation - Campaign Design (~45 min)

**Inputs**: GTM strategy, personas, messaging framework, channel budget

**Activities**:
1. Design campaigns for each active channel (paid search, paid social, organic)
2. Create ad creative briefs with headline/body variations for A/B testing
3. Write landing page copy with conversion-optimized structure
4. Build lead magnet concepts (ebooks, webinars, tools, templates)
5. Design email nurture sequences for each persona and funnel stage
6. Define lead scoring criteria in collaboration with Pipeline Manager
7. Set up campaign tracking with UTM parameters and conversion events

**Outputs**:
- `workspace/demand-gen/campaigns/` - Campaign briefs per channel
- `workspace/demand-gen/landing-pages/` - Landing page wireframes and copy
- `workspace/demand-gen/ad-creative/` - Ad variations for testing
- `workspace/demand-gen/email-sequences/` - Nurture email sequences
- `workspace/demand-gen/lead-scoring.md` - Lead scoring criteria
- `workspace/demand-gen/tracking-plan.md` - UTM and conversion tracking plan

### Sales Enablement - Enablement Kit (~45 min)

**Inputs**: GTM strategy, personas, messaging framework, competitive analysis

**Activities**:
1. Build the master pitch deck with narrative arc (problem, impact, solution, proof, ask)
2. Create persona-specific pitch deck variants
3. Write competitive battle cards for each primary competitor
4. Develop demo scripts with branching paths based on persona and pain points
5. Build ROI calculator with input variables and output projections
6. Create objection handling playbook organized by category
7. Write outbound email templates and sequences
8. Design sales training curriculum for new hires

**Outputs**:
- `workspace/sales-enablement/pitch-deck.md` - Master pitch deck outline
- `workspace/sales-enablement/battle-cards/` - Competitive battle cards
- `workspace/sales-enablement/demo-scripts/` - Demo scripts per persona
- `workspace/sales-enablement/roi-calculator.md` - ROI calculator design
- `workspace/sales-enablement/objection-handling.md` - Objection handling playbook
- `workspace/sales-enablement/email-templates/` - Outbound email sequences
- `workspace/sales-enablement/training/` - Sales training materials

### Pipeline Manager - CRM Infrastructure (~45 min)

**Inputs**: GTM strategy, sales motion, deal size, sales cycle

**Activities**:
1. Define pipeline stages with clear entry criteria, exit criteria, and required activities
2. Design CRM field structure for contacts, companies, and deals
3. Create deal scoring model based on engagement, fit, and intent signals
4. Build forecast methodology (weighted pipeline, commit/upside/best case)
5. Design automated workflows: stage progression, task creation, notifications
6. Create pipeline review agenda templates (weekly, monthly, quarterly)
7. Define reporting requirements and dashboard specifications

**Outputs**:
- `workspace/pipeline/stage-definitions.md` - Pipeline stages with criteria
- `workspace/pipeline/crm-config.md` - CRM field and object configuration
- `workspace/pipeline/scoring-model.md` - Deal scoring model
- `workspace/pipeline/forecast-methodology.md` - Forecasting approach
- `workspace/pipeline/workflows.md` - Automated workflow definitions
- `workspace/pipeline/review-cadences.md` - Pipeline review templates

### Customer Success - Post-Sale Foundation (~45 min)

**Inputs**: GTM strategy, product context, personas, health scoring requirements

**Activities**:
1. Design onboarding sequence with day-by-day milestones and success criteria
2. Build customer health scoring model using product usage, engagement, and support signals
3. Create expansion/upsell playbook with triggers, talk tracks, and timing
4. Design churn prevention workflow with early warning signals and intervention strategies
5. Build QBR template with preparation checklist and presentation structure
6. Define customer segmentation model (high-touch, mid-touch, tech-touch)
7. Design customer advocacy program (case studies, references, reviews)

**Outputs**:
- `workspace/customer-success/onboarding-playbook.md` - Day-by-day onboarding
- `workspace/customer-success/health-scoring.md` - Health score model
- `workspace/customer-success/expansion-playbook.md` - Expansion triggers and playbooks
- `workspace/customer-success/churn-prevention.md` - Churn prevention workflow
- `workspace/customer-success/qbr-template.md` - QBR template and prep guide
- `workspace/customer-success/segmentation.md` - Customer segmentation framework

### Phase 2 Quality Gate

Before proceeding to Phase 3, the Coordinator reviews all Phase 2 outputs:

- [ ] Campaign designs cover all active channels with A/B test variants
- [ ] Sales enablement materials cover all personas and competitive scenarios
- [ ] CRM stages have clear entry/exit criteria and are consistent with sales motion
- [ ] Onboarding sequence has measurable milestones and success criteria
- [ ] Lead scoring criteria align between Demand Gen and Pipeline Manager
- [ ] Messaging in all deliverables is consistent with the Brand & Messaging framework
- [ ] All deliverables reference the correct personas from Phase 1

---

## Phase 3: Execution & Optimization (Parallel - ~60 min)

### Purpose
Move from planning to execution. Launch campaigns, build training materials, create operational dashboards, and design the ongoing cadences that drive continuous improvement.

### Execution Map

```
        ┌─── Demand Generation: Launch campaigns, monitor performance
        │
        ├─── Sales Enablement: Training materials, advanced objection handling
Phase 2 │
Output  ├─── Pipeline Manager: Pipeline reviews, forecast refinement
        │
        ├─── Customer Success: Journey mapping, expansion playbooks
        │
        └─── Growth Analyst: Dashboards, experiment design
```

### Demand Generation - Campaign Launch (~60 min)

**Activities**:
1. Finalize campaign configurations with targeting, bidding, and budget parameters
2. Create A/B test plans for each campaign element (headlines, images, audiences, landing pages)
3. Design performance monitoring workflow with daily, weekly, and monthly checks
4. Build automated rules for budget pacing, bid adjustments, and pause criteria
5. Create retargeting campaigns for website visitors and email engagers
6. Design content calendar for organic channels (blog, social, community)

**Outputs**:
- `workspace/demand-gen/campaign-configs/` - Final campaign specifications
- `workspace/demand-gen/ab-tests/` - Test plans with hypothesis and success criteria
- `workspace/demand-gen/monitoring/` - Performance monitoring workflows
- `workspace/demand-gen/retargeting/` - Retargeting campaign designs
- `workspace/demand-gen/content-calendar.md` - Organic content calendar

### Sales Enablement - Training & Refinement (~60 min)

**Activities**:
1. Build sales training modules: discovery, demo, negotiation, closing
2. Create advanced objection handling with competitive counter-positioning
3. Design sales coaching framework for managers
4. Build win/loss analysis template
5. Create deal review preparation guide
6. Design onboarding program for new sales hires (30/60/90 day plan)

**Outputs**:
- `workspace/sales-enablement/training/modules/` - Training modules
- `workspace/sales-enablement/coaching-framework.md` - Manager coaching guide
- `workspace/sales-enablement/win-loss-template.md` - Win/loss analysis template
- `workspace/sales-enablement/new-hire-plan.md` - 30/60/90 day onboarding

### Pipeline Manager - Operational Cadences (~60 min)

**Activities**:
1. Run sample pipeline review using stage definitions and scoring model
2. Refine forecast accuracy methodology with historical calibration approach
3. Build stuck-deal coaching playbook (identify blockers, suggest actions, escalation criteria)
4. Create pipeline hygiene audit checklist
5. Design automated alert rules for at-risk deals
6. Build leadership reporting templates

**Outputs**:
- `workspace/pipeline/pipeline-review-sample.md` - Sample pipeline review
- `workspace/pipeline/stuck-deal-coaching.md` - Stuck deal playbook
- `workspace/pipeline/hygiene-audit.md` - CRM hygiene checklist
- `workspace/pipeline/alert-rules.md` - Automated alert specifications
- `workspace/pipeline/leadership-reports/` - Reporting templates

### Customer Success - Journey & Expansion (~60 min)

**Activities**:
1. Map the complete customer journey from onboarding through renewal and expansion
2. Design touchpoint sequences for each customer segment
3. Build expansion playbook with upsell/cross-sell triggers and talk tracks
4. Create renewal management workflow with timeline and activities
5. Design customer feedback collection strategy (NPS, CSAT, CES)
6. Build escalation workflows for at-risk customers

**Outputs**:
- `workspace/customer-success/journey-map.md` - Complete customer journey
- `workspace/customer-success/touchpoint-sequences/` - Segment-specific touchpoints
- `workspace/customer-success/renewal-workflow.md` - Renewal management
- `workspace/customer-success/feedback-strategy.md` - Feedback collection design
- `workspace/customer-success/escalation-workflows.md` - Escalation procedures

### Growth Analyst - Dashboards & Experiments (~60 min)

**Activities**:
1. Design marketing performance dashboard (channel performance, CAC trending, conversion rates)
2. Design pipeline dashboard (velocity, conversion rates, forecast vs actual)
3. Design customer health dashboard (health scores, churn risk, expansion pipeline)
4. Create first batch of experiment designs with hypothesis, metrics, and sample sizes
5. Build cohort analysis framework for retention and LTV tracking
6. Create weekly/monthly reporting templates

**Outputs**:
- `workspace/analytics/dashboards/marketing-performance.md` - Marketing dashboard spec
- `workspace/analytics/dashboards/pipeline-health.md` - Pipeline dashboard spec
- `workspace/analytics/dashboards/customer-health.md` - Customer dashboard spec
- `workspace/analytics/experiments/` - Experiment designs
- `workspace/analytics/cohort-framework.md` - Cohort analysis methodology
- `workspace/analytics/reporting-templates/` - Recurring report templates

### Phase 3 Quality Gate

- [ ] All campaigns have A/B test variants with statistical test plans
- [ ] Training materials cover the complete sales process
- [ ] Pipeline reviews produce actionable coaching recommendations
- [ ] Customer journey map covers all touchpoints from onboarding through renewal
- [ ] Dashboards answer the top questions for each stakeholder (marketing, sales, CS, exec)
- [ ] Experiment designs have proper hypothesis, metrics, sample sizes, and duration

---

## Phase 4: Analysis & Iteration (Parallel - ~20 min)

### Purpose
Analyze results, document learnings, and prepare recommendations for the next planning cycle. This phase closes the loop and ensures continuous improvement.

### Execution Map

```
        ┌─── Growth Analyst: Performance analysis, recommendations
Phase 3 │
Output  ├─── Coordinator: Strategy refinement, budget reallocation
        │
        └─── All Agents: Document learnings, update playbooks
```

### Growth Analyst - Performance Analysis (~15 min)

**Activities**:
1. Analyze campaign performance by channel with attribution-weighted ROI
2. Calculate actual CAC, LTV, and payback period vs targets
3. Identify top-performing and underperforming channels, campaigns, and content
4. Run marginal CAC analysis to identify optimal budget allocation
5. Summarize experiment results with statistical significance
6. Generate specific, prioritized recommendations for the next cycle

**Outputs**:
- `workspace/analytics/performance-analysis.md` - Campaign performance report
- `workspace/analytics/unit-economics.md` - CAC/LTV/payback analysis
- `workspace/analytics/recommendations.md` - Prioritized recommendations

### Coordinator - Strategy Refinement (~15 min)

**Activities**:
1. Review Growth Analyst's performance analysis and recommendations
2. Decide on budget reallocation across channels
3. Update strategy based on market learnings and performance data
4. Identify strategic shifts needed (new personas, channels, positioning)
5. Set objectives for the next execution cycle
6. Create the iteration brief for all agents

**Outputs**:
- `workspace/strategy/iteration-brief.md` - Next cycle strategy updates
- `workspace/strategy/budget-reallocation.md` - Updated budget allocation
- `workspace/strategy/learnings.md` - Strategic learnings document

### All Agents - Playbook Updates (~10 min)

**Activities**:
1. Each agent updates their playbooks with learnings from execution
2. Document what worked, what didn't, and what to try next
3. Update templates and frameworks based on real-world performance
4. Archive completed experiments and campaigns
5. Prepare handoff notes for the next cycle

**Outputs**:
- Updated playbooks in each agent's workspace directory
- `workspace/learnings/` - Cross-functional learnings document

---

## Execution Modes

### Full Execution
Runs all 4 phases sequentially. Use for initial GTM setup or major strategy overhauls.

```bash
claude-code team run --phases all --config CONFIG.md
```

### Strategy Only
Runs Phase 1 only. Use when you need a strategy refresh without rebuilding all assets.

```bash
claude-code team run --phase strategy --config CONFIG.md
```

### Build & Execute
Runs Phases 2-3, assuming Phase 1 strategy already exists. Use when strategy is set and you need to build and launch.

```bash
claude-code team run --phases pipeline-building,execution --config CONFIG.md
```

### Analysis Only
Runs Phase 4 only. Use for periodic reviews when you have execution data to analyze.

```bash
claude-code team run --phase analysis --config CONFIG.md
```

### Single Agent
Run a specific agent for targeted work without the full team.

```bash
claude-code agent run demand-generation --task "Design Google Ads campaign for Q2 product launch"
claude-code agent run growth-analyst --task "Analyze last month's campaign performance"
```

---

## Git Strategy

### Branch Naming

```
gtm/                          # Top-level GTM namespace
├── strategy/                  # Phase 1 work
│   └── 2026-02-10-initial    # Date-stamped strategy
├── campaigns/                 # Phase 2-3 campaign work
│   ├── google-ads-q1         # Channel-specific branches
│   └── linkedin-launch       # Campaign-specific branches
├── enablement/                # Sales enablement work
│   └── battle-cards-v2       # Specific deliverable branches
├── pipeline/                  # Pipeline/CRM work
│   └── crm-setup             # Infrastructure branches
├── customer-success/          # CS work
│   └── onboarding-v1         # Playbook branches
└── analytics/                 # Analytics work
    └── attribution-model     # Analysis branches
```

### Commit Convention

```
[agent] action: brief description

Examples:
[coordinator] strategy: define Q1 GTM strategy and budget allocation
[demand-gen] campaign: create Google Ads search campaign for developer persona
[sales-enablement] assets: build competitive battle cards for Competitor A and B
[pipeline-manager] crm: define pipeline stages with entry/exit criteria
[customer-success] playbook: design 14-day onboarding sequence
[growth-analyst] analysis: build multi-touch attribution model specification
[brand-messaging] messaging: create messaging hierarchy and persona variants
```

### PR Strategy

Each phase produces one PR for review:
- `gtm/phase-1-strategy` -> main
- `gtm/phase-2-pipeline-building` -> main (after Phase 1 merges)
- `gtm/phase-3-execution` -> main (after Phase 2 merges)
- `gtm/phase-4-analysis` -> main (after Phase 3 merges)

---

## Communication Protocol

### Agent-to-Agent Communication

Agents communicate through shared workspace files, not direct messages. This ensures all decisions are documented and auditable.

| From | To | Channel | Purpose |
|------|-----|---------|---------|
| Coordinator | All | `workspace/strategy/` | Strategy directives and decisions |
| Brand & Messaging | All | `workspace/messaging/` | Messaging library and guidelines |
| Demand Gen | Pipeline Manager | `workspace/demand-gen/lead-scoring.md` | Lead scoring alignment |
| Pipeline Manager | Customer Success | `workspace/pipeline/handoff-criteria.md` | Sales-to-CS handoff |
| Growth Analyst | Coordinator | `workspace/analytics/recommendations.md` | Data-driven recommendations |
| All | All | `workspace/learnings/` | Cross-functional learnings |

### Escalation Protocol

1. **Conflict detected**: Agent identifies a conflict with another agent's output
2. **Document conflict**: Agent writes conflict description to `workspace/conflicts/`
3. **Coordinator reviews**: Coordinator reads conflict, reviews both positions
4. **Decision made**: Coordinator writes decision with rationale to `workspace/strategy/decisions/`
5. **Agents update**: Affected agents update their outputs based on the decision

### Status Updates

Each agent writes status to `workspace/status/[agent-name].md` after completing each major task:

```yaml
agent: demand-generation
phase: 2
task: Google Ads campaign design
status: complete
outputs:
  - workspace/demand-gen/campaigns/google-ads-search.md
  - workspace/demand-gen/campaigns/google-ads-display.md
blockers: none
next: LinkedIn Ads campaign design
```

---

## Scenario Validation

Before executing any phase, the Coordinator validates the scenario is appropriate:

### Scenario: New Product Launch
- **Required phases**: All 4
- **Key focus**: Messaging (no existing brand equity), campaign design (no historical data), CRM setup (clean slate)
- **Risk**: No historical data for attribution or optimization; rely on benchmarks and rapid testing

### Scenario: Scaling Existing Motion
- **Required phases**: 2, 3, 4 (strategy exists)
- **Key focus**: Campaign optimization, pipeline efficiency, customer retention
- **Risk**: Over-indexing on what worked before; need to test new channels and messages

### Scenario: Entering New Market
- **Required phases**: All 4
- **Key focus**: New personas, competitive research, positioning for new segment
- **Risk**: Existing assumptions may not apply; validate quickly with small budget

### Scenario: Quarterly Planning
- **Required phases**: 1 and 4
- **Key focus**: Strategy refresh, performance review, budget reallocation
- **Risk**: Anchoring to last quarter's strategy instead of adapting to new data

---

## Decision Criteria

### When to Run Full Execution
- First time using the template
- Major strategy pivot or new market entry
- New product launch without existing GTM infrastructure
- Annual planning reset

### When to Run Partial Execution
- Strategy is solid but need new campaign assets (Phases 2-3)
- Monthly performance review (Phase 4)
- New competitor entered the market (Phase 1 + selective Phase 2)
- Customer churn is spiking (Customer Success + Growth Analyst only)

### When to Run Single Agent
- Need a quick competitive battle card update
- Want to analyze last week's campaign performance
- Need to design a single new email sequence
- Want to update the pipeline forecast

### When to Iterate vs. Restart
- **Iterate** when: Core strategy is sound, optimizing within channels, incremental improvements
- **Restart** when: Fundamental positioning change, new target market, pivot in business model, CAC is 3x target with no improvement trend
