# Example: User Research Study

This example demonstrates a product discovery research study for a B2B SaaS product, combining user behavior analysis, usability evaluation, and feature prioritization.

---

## Research Brief

| Property | Value |
|----------|-------|
| **Research Type** | Product/UX |
| **Research Question** | "Why has our onboarding completion rate dropped from 68% to 41% over the past quarter, and what improvements would have the highest impact on activation?" |
| **Domain** | Technology / B2B SaaS |
| **Mode** | Product |
| **Configuration** | Default |
| **Actual Cost** | ~$24 |
| **Duration** | ~75 minutes (hybrid mode) |

---

## Configuration Used

```yaml
research_type: product_ux
domain: technology
research_question: "Why has our onboarding completion rate dropped from 68% to 41% over the past quarter, and what improvements would have the highest impact on activation?"
product_mode:
  enabled: true
  product_stage: growth
  research_focus: optimization
  analytics_access: yes
  product_url: "https://app.example.com"
  analytics_data_path: "./data/analytics-export-q4.csv"
  interview_transcripts_path: "./data/user-interviews/"
sources:
  depth: standard
  max_sources: 15
  source_recency_years: 2
agent_budget:
  model_config: default
  max_total_cost_usd: 35
```

---

## Phase 1: Study Design (Coordinator Output)

**Refined Research Question:** What caused the 27-point drop in onboarding completion rate, which onboarding steps have the highest drop-off, and which improvements would most efficiently recover the activation rate?

**Sub-questions:**
1. At which specific onboarding step(s) did the drop-off increase?
2. Did the drop affect all user segments equally or specific cohorts?
3. Were there product changes during the period that correlate with the decline?
4. What do current industry benchmarks say about B2B SaaS onboarding rates?
5. What usability friction exists in the current onboarding flow?
6. Which improvements would have the highest RICE score?

**Active Agents:** Coordinator, Primary Researcher, Analyst, Synthesizer, User Behavior Analyst, Usability Evaluator, Feature Prioritizer (7 agents).

---

## Phase 2: Data Collection Summary

### Analytics Data (User Behavior Analyst)

The User Behavior Analyst processed the analytics export and identified:

**Funnel Analysis -- Onboarding Steps:**

| Step | Completion (Q3) | Completion (Q4) | Change | Significance |
|------|-----------------|-----------------|--------|-------------|
| 1. Account creation | 100% | 100% | -- | Baseline |
| 2. Profile setup | 92% | 89% | -3pp | Minor |
| 3. Connect data source | 78% | 52% | **-26pp** | **Critical** |
| 4. First dashboard | 72% | 46% | -26pp | Downstream |
| 5. Invite team member | 68% | 41% | -27pp | Downstream |

**Key Finding:** Step 3 ("Connect data source") is the breakpoint. The 26-point drop cascades through all subsequent steps.

**Cohort Analysis:**

| Segment | Q3 Completion | Q4 Completion | Change |
|---------|--------------|---------------|--------|
| Self-serve signups | 65% | 38% | -27pp |
| Sales-assisted signups | 82% | 76% | -6pp |
| Enterprise signups | 90% | 88% | -2pp |

**Key Finding:** Self-serve users are disproportionately affected. Sales-assisted and enterprise users (who get human onboarding help) show minimal decline.

### External Research (Primary Researcher)

Found 14 relevant sources on B2B SaaS onboarding:
- Industry benchmark: median onboarding completion for B2B SaaS is 45-55%
- Best-in-class onboarding completion: 70-80%
- Common onboarding friction points: integration setup, data import, value demonstration
- Pendo/Appcues research on progressive onboarding patterns

### User Interviews (Analyst)

Coded 8 interview transcripts from recent churned users:

| Theme | Frequency | Example Quote |
|-------|-----------|---------------|
| Integration confusion | 6/8 | "I didn't know which connector to pick. There were 47 options and no guidance." |
| Error messages unhelpful | 5/8 | "It just said 'connection failed' with no way to debug." |
| Expected faster setup | 4/8 | "The marketing said '5-minute setup' but I spent 45 minutes." |
| No sample data option | 3/8 | "I just wanted to see what the product does before connecting my real data." |

---

## Phase 3: Analysis Summary

### Root Cause Analysis (Analyst)

The Analyst cross-referenced the data and identified:

**Primary Root Cause:** A product update in early Q4 added 12 new data source connectors (from 35 to 47), expanding the connector selection screen without updating the guidance flow. Self-serve users face a paradox-of-choice problem that did not exist when there were fewer options.

**Contributing Factors:**
1. No search or filtering on the connector selection screen
2. No "recommended for you" logic based on signup data
3. Error messages for failed connections lack diagnostic steps
4. No sandbox/demo mode to try the product without connecting real data

**Evidence Strength:** High. The timing of the connector expansion matches the drop-off increase exactly. Cohort data shows the impact is isolated to self-serve users who do not receive human guidance.

### Usability Evaluation (Usability Evaluator)

Heuristic evaluation of the current onboarding flow:

| Issue | Heuristic Violated | Severity | Impact |
|-------|-------------------|----------|--------|
| 47 connectors with no search, filtering, or categorization | Recognition over recall | Critical | Users cannot find their connector |
| "Connection failed" with no actionable next step | Help users recognize, diagnose, and recover from errors | Critical | Users abandon after first failure |
| "5-minute setup" claim in marketing vs 20-45 min reality | Match between system and real world | Major | Trust violation, frustration |
| No way to skip integration and use sample data | User control and freedom | Major | Blocks exploration-first users |
| Progress bar shows 5 steps but step 3 takes 80% of time | Visibility of system status | Minor | Misleading progress expectations |

---

## Phase 4: Synthesis and Recommendations

### Feature Prioritization (RICE Scoring)

| Improvement | Reach | Impact | Confidence | Effort | RICE Score | Priority |
|------------|-------|--------|------------|--------|-----------|----------|
| Add search + category filters to connector screen | 100% of self-serve | High (3) | 95% | 1 week | **285** | **P0** |
| Implement "sandbox mode" with sample data | 100% of self-serve | High (3) | 80% | 3 weeks | 80 | **P1** |
| Add diagnostic error messages with fix suggestions | 60% of self-serve | High (3) | 90% | 2 weeks | 81 | **P1** |
| "Recommended connectors" based on signup industry | 100% of self-serve | Medium (2) | 70% | 2 weeks | 70 | **P2** |
| Update marketing to set accurate time expectations | 100% of visitors | Low (1) | 60% | 1 day | 60 | **P2** |
| Redesign progress bar to reflect actual time per step | 100% of self-serve | Low (1) | 80% | 3 days | 27 | **P3** |

### Experiment Proposals

**Experiment 1: Connector Search and Categories**
- **Hypothesis:** Adding search and category filtering to the connector selection screen will increase Step 3 completion by at least 15 percentage points for self-serve users.
- **Primary metric:** Step 3 completion rate (self-serve cohort)
- **Secondary metrics:** Time to complete Step 3, support tickets about connector selection
- **Minimum sample size:** 1,200 self-serve signups per variant (80% power, 5% significance)
- **Duration:** 2-3 weeks depending on signup volume

**Experiment 2: Sandbox Mode**
- **Hypothesis:** Offering a "try with sample data" option will increase onboarding completion by at least 10 percentage points by allowing users to experience value before committing to integration.
- **Primary metric:** Onboarding completion rate (self-serve cohort)
- **Secondary metrics:** Conversion from sandbox to real integration within 14 days
- **Minimum sample size:** 800 self-serve signups per variant
- **Duration:** 3-4 weeks

---

## Deliverables Produced

1. **Product Research Report** (2,800 words) -- Root cause analysis, usability findings, prioritized recommendations
2. **Executive Summary** (350 words) -- Key finding and top 3 recommended actions
3. **Prioritized Feature Backlog** -- 6 improvements scored by RICE with effort estimates
4. **Experiment Proposals** -- 2 A/B test designs with hypotheses, metrics, and sample sizes
5. **Usability Issue Tracker** -- 5 issues ranked by severity with remediation guidance
6. **Analytics Dashboard Recommendations** -- Metrics to track onboarding health going forward

---

## Cost Breakdown

| Phase | Tokens Used | Cost |
|-------|-----------|------|
| Study Design | 28K | $4.20 |
| Data Analysis (behavior + interviews) | 82K | $4.92 |
| Usability Evaluation | 52K | $3.12 |
| Feature Prioritization | 38K | $2.28 |
| Synthesis | 65K | $5.10 |
| Deliverables | 30K | $2.55 |
| **Total** | **295K** | **~$24** |

---

## Lessons Learned

1. **Quantitative and qualitative data told the same story.** The analytics pinpointed Step 3 as the problem. The interviews explained why. Neither alone would have been sufficient for actionable recommendations.
2. **The root cause was a product change, not a market change.** Without the timing correlation between the connector expansion and the drop-off, the team might have pursued external explanations (market saturation, competitor activity).
3. **RICE scoring changed the conversation.** The team initially wanted to build sandbox mode first (the most ambitious solution). RICE scoring showed that adding search to the connector screen was 3.5x higher priority due to effort efficiency.
4. **Experiment proposals made the research immediately actionable.** The product team could start implementing the P0 fix and designing the experiment within the same sprint.
5. **The self-serve vs assisted cohort split was the critical insight.** Without segmentation, the 41% completion rate looked like a product-wide problem. Segmented, it was clearly a self-serve guidance problem.
