# Scenario: Campaign Optimization

## Overview

This scenario walks through optimizing a multi-channel paid acquisition program that is over budget on CAC and under target on MQL volume. Starting with three channels spending $10K/month total, a blended CAC of $450 (target: $300), and 65 MQLs/month (target: 100), the team runs a structured optimization cycle to improve performance through data analysis, hypothesis generation, experimentation, and budget reallocation.

**Starting state**: Underperforming. **Target end state**: On track.

---

## Starting State

### Channel Performance Baseline

| Channel | Monthly Spend | MQLs | Cost per MQL | SQLs | Cost per SQL | CAC | Observations |
|---------|--------------|------|-------------|------|-------------|-----|-------------|
| **LinkedIn Ads** | $4,000 | 15 | $267 | 8 | $500 | $520 | High quality leads, strong SQL conversion (53%), but low volume and high CAC |
| **Meta Ads** | $3,500 | 35 | $100 | 5 | $700 | $780 | High volume, cheap MQLs, but very poor SQL conversion (14%) -- leads are unqualified |
| **Google Ads** | $2,500 | 15 | $167 | 7 | $357 | $390 | Middle of the pack on both volume and quality. Decent SQL conversion (47%) |
| **Total** | **$10,000** | **65** | **$154** | **20** | **$500** | **$450** | Blended CAC $450 vs $300 target. MQLs 65 vs 100 target |

### Key Problems

1. **Blended CAC ($450) is 50% above target ($300)**: Cannot scale profitably at current efficiency
2. **MQL volume (65) is 35% below target (100)**: Insufficient pipeline feeding to hit revenue goals
3. **Meta channel is a trap**: Cheap MQLs that do not convert waste sales team time and inflate CAC
4. **LinkedIn works but does not scale**: Quality is excellent but volume is constrained at current budget
5. **Google Ads is underleveraged**: Decent performance but receiving the smallest budget allocation

---

## Phase 1: Baseline Analysis

**Agents involved**: Growth Analyst (primary), Coordinator (review), Demand Generation (input)

### Growth Analyst Deep Dive

The Growth Analyst performs a structured analysis of each channel, going beyond surface metrics to understand the underlying dynamics.

**LinkedIn Ads Analysis**:
- 53% MQL-to-SQL conversion is exceptional (benchmark: 20-30% for B2B LinkedIn)
- Average deal size from LinkedIn leads is $42K (17% above overall average of $36K)
- LTV of LinkedIn-acquired customers is 2.3x higher than Meta-acquired customers
- Current targeting: VP/Director Engineering at 200-2000 employee SaaS companies
- Budget utilization: spending $4K of estimated $8K addressable daily budget -- room to scale
- CPM has been stable at $45 over the past 90 days -- no saturation signals
- **Verdict**: Underinvested. Scale budget before CPM increases.

**Meta Ads Analysis**:
- 14% MQL-to-SQL conversion is significantly below benchmark (25-35%)
- Root cause investigation: 62% of Meta leads are from companies with <20 employees (below ICP minimum of 50)
- Landing page for Meta campaigns is the same generic page used for all channels -- no persona-specific messaging
- Ad creative is product-focused ("See our platform") rather than pain-focused ("Deployments taking too long?")
- Audience: broad lookalike of website visitors (1% similarity) -- too broad
- **Verdict**: Volume is misleading. Quality is poor because targeting is too broad and messaging is too generic. Fix targeting and landing page before considering budget changes.

**Google Ads Analysis**:
- 47% MQL-to-SQL conversion is strong (benchmark: 30-40% for B2B search)
- Keywords performing best: "deployment automation tool" (CPA $140), "CI/CD platform comparison" (CPA $155)
- Keywords underperforming: "DevOps tools" (CPA $380, too broad), "CI/CD" (CPA $290, informational intent)
- Landing page conversion rate: 18% (below benchmark of 25% for search intent traffic)
- Ad copy relevance: moderate. Current headlines do not include the specific search terms.
- **Verdict**: Strong channel with optimization headroom. Improve landing page, tighten keywords, increase budget on proven terms.

### Coordinator Strategic Review

The Coordinator reviews the Growth Analyst's findings and establishes optimization priorities:

1. **Priority 1**: Increase LinkedIn budget from $4K to $6K (highest quality channel with room to scale)
2. **Priority 2**: Fix Meta targeting and landing page before making budget decisions (diagnose before cutting)
3. **Priority 3**: Optimize Google Ads landing page and keyword mix (quick wins available)
4. **Constraint**: Total budget remains $10K/month during the optimization cycle. Rebalance, do not increase.

---

## Phase 2: Hypotheses

**Agents involved**: Growth Analyst (experiment design), Demand Generation (execution plan), Brand & Messaging (creative)

### Hypothesis 1: LinkedIn Budget Increase

**Statement**: If we increase LinkedIn Ads budget from $4K to $6K/month (+50%) while maintaining current targeting and creative, MQL volume will increase from 15 to 22 (+47%) with no more than a 15% increase in cost per MQL.

**Rationale**: Current spend is 50% of estimated addressable daily budget. CPM is stable, indicating no audience saturation. Linear scaling is expected up to approximately 70% of addressable budget before diminishing returns.

**Risk**: CPM could increase as we bid on more competitive auction inventory, raising cost per MQL beyond the 15% threshold.

**Measurement**: Track CPM, CTR, conversion rate, cost per MQL, and MQL-to-SQL conversion weekly.

### Hypothesis 2: Meta Landing Page + Targeting Fix

**Statement**: If we (a) narrow Meta targeting to companies with 50-2000 employees and exclude non-ICP industries, and (b) create a persona-specific landing page with pain-focused messaging, MQL-to-SQL conversion will increase from 14% to at least 25%.

**Rationale**: The current 14% conversion rate is driven by poor lead quality (wrong company size) and generic messaging (no pain-point focus). Fixing both simultaneously should bring conversion in line with channel benchmarks.

**Test components**:
- **Targeting change**: Replace 1% broad lookalike with 1% lookalike filtered by company size (50-2000 employees using LinkedIn data overlay) + exclude non-ICP industries
- **Landing page change**: Brand & Messaging produces a pain-focused landing page for the VP Engineering persona. Headline addresses deployment speed (not product features). Social proof from similar-sized companies. Form adds company size field for qualification.

**Risk**: Volume will decrease as targeting narrows. This is expected and acceptable -- we are trading volume for quality.

**Measurement**: Track MQL volume, MQL-to-SQL conversion rate, and cost per SQL. Success = SQL conversion >25% even if MQL volume drops by up to 30%.

### Hypothesis 3: Google Ads Copy + Landing Page Optimization

**Statement**: If we (a) rewrite ad copy to include exact search terms in headlines, and (b) optimize the landing page for search intent (faster load, above-fold CTA, message match), landing page conversion rate will increase from 18% to at least 25%.

**Sub-hypotheses**:
- **3a (Ad copy)**: Rewriting headlines to include the search keyword ("Deployment Automation Tool" as headline for the deployment-automation ad group) will increase CTR by 15%+ and improve Quality Score.
- **3b (Landing page)**: Reducing page load time from 3.2s to <2s, adding message-matched headlines per ad group, and moving the CTA above the fold will increase conversion rate from 18% to 25%+.
- **3c (Keyword pruning)**: Pausing broad terms ("DevOps tools", "CI/CD") and reallocating budget to proven high-intent terms will reduce cost per MQL by 20%+.

**Measurement**: A/B test new landing page vs. current landing page with 50/50 traffic split. Track CTR, Quality Score, conversion rate, and cost per MQL.

---

## Phase 3: Experiment Design

**Agents involved**: Growth Analyst (statistical design), Demand Generation (implementation)

### Experiment 1: LinkedIn Budget Scale

```
Type: Budget scaling test (not A/B)
Duration: 4 weeks
Approach: Increase daily budget from $133/day to $200/day
Monitoring: Weekly CPM, CTR, conversion rate, MQL count, cost per MQL
Success criteria:
  - MQLs increase to >20/month
  - Cost per MQL stays below $310 (15% above current $267)
  - MQL-to-SQL conversion stays above 45%
Kill criteria:
  - CPM increases by >25% (indicates auction saturation)
  - MQL-to-SQL conversion drops below 35% (quality degradation)
  - Cost per MQL exceeds $350 for 2 consecutive weeks
```

### Experiment 2: Meta Targeting + Landing Page

```
Type: Multi-variable change (targeting + landing page simultaneously)
Duration: 3 weeks
Approach:
  - Week 1: Launch new targeting with existing landing page (isolate targeting effect)
  - Week 2-3: A/B test new landing page vs existing with new targeting
Statistical plan:
  - Baseline conversion rate: 14%
  - Minimum detectable effect: 11 percentage points (to reach 25%)
  - Significance level: 95%
  - Power: 80%
  - Required sample: ~180 MQLs per variant (estimated 3 weeks at new targeting volume)
Success criteria:
  - MQL-to-SQL conversion >25%
  - Cost per SQL <$500
Kill criteria:
  - MQL volume drops below 10/month (targeting too narrow)
  - Cost per MQL exceeds $250 (2.5x current)
```

### Experiment 3: Google Ads Copy + Landing Page

```
Type: A/B test (landing page) + sequential optimization (ad copy + keywords)
Duration: 3 weeks
Approach:
  - Week 1: Pause underperforming keywords, reallocate budget to top performers
  - Week 1-3: A/B test new landing page vs current (50/50 split)
  - Week 2: Launch new ad copy variants for top-performing keywords
Statistical plan:
  - Baseline conversion rate: 18%
  - Minimum detectable effect: 7 percentage points (to reach 25%)
  - Significance level: 95%
  - Power: 80%
  - Required sample: ~450 landing page visitors per variant (estimated 3 weeks)
Success criteria:
  - Landing page conversion rate >25%
  - Cost per MQL <$140
  - Quality Score improvement on primary keywords
Kill criteria:
  - Conversion rate drops below 15% (worse than current)
  - Click volume drops by >30% (ad copy not resonating)
```

---

## Phase 4: Execution -- Weeks 1-2

**Agents involved**: Demand Generation (execution), Growth Analyst (monitoring), Brand & Messaging (creative), Coordinator (decisions)

### Week 1 Actions

**LinkedIn**: Budget increased from $133/day to $200/day. Same targeting and creative.

**Meta**: New targeting launched (company size 50-2000, ICP industries only). Existing landing page retained for Week 1 to isolate the targeting effect.

**Google Ads**: Paused "DevOps tools" and "CI/CD" broad keywords. Reallocated $800/month to "deployment automation tool" and "CI/CD platform comparison" keywords. New landing page A/B test launched. Brand & Messaging delivered the pain-focused landing page variant.

### Week 1 Results

| Channel | Spend | MQLs | Cost/MQL | SQLs | Cost/SQL | Notes |
|---------|-------|------|----------|------|----------|-------|
| LinkedIn | $1,500 | 6 | $250 | 3 | $500 | On track. CPM stable. Volume scaling linearly. |
| Meta | $875 | 5 | $175 | 2 | $438 | Volume dropped 43% (expected). SQL conversion jumped to 40%. Cost/MQL up but cost/SQL improved. |
| Google Ads | $625 | 5 | $125 | 2 | $313 | Keyword pruning working. Landing page test collecting data. |

**Week 1 Assessment (Coordinator)**:
- LinkedIn scaling as predicted. Continue.
- Meta targeting change showing dramatic quality improvement. SQL conversion 40% vs 14% baseline. Ready to launch landing page test in Week 2.
- Google Ads keyword pruning showing immediate cost improvement. Landing page test needs more data.

### Week 2 Actions

**LinkedIn**: Continue at $200/day. Test one new ad creative variant (case study format vs current benefit-focused format).

**Meta**: Launch new landing page A/B test with the improved targeting active. Brand & Messaging delivered the VP Engineering pain-focused landing page.

**Google Ads**: Launch new ad copy with keyword-specific headlines. Continue landing page A/B test.

### Week 2 Results

| Channel | Spend | MQLs | Cost/MQL | SQLs | Cost/SQL | Notes |
|---------|-------|------|----------|------|----------|-------|
| LinkedIn | $1,500 | 7 | $214 | 4 | $375 | Volume increasing. Case study creative variant outperforming control (+18% CTR). |
| Meta | $875 | 6 | $146 | 3 | $292 | New landing page variant showing 35% conversion rate vs 22% for control. Not yet significant. |
| Google Ads | $625 | 6 | $104 | 3 | $208 | New ad copy driving +22% CTR. Landing page test: treatment at 27% vs control 19%. Approaching significance. |

### Kill / Continue Decisions (End of Week 2)

**Growth Analyst Assessment**:

1. **LinkedIn**: Continue and consider further budget increase. CPM stable at $47 (only +4% from baseline). No saturation signals. Quality maintained (57% SQL conversion this period).

2. **Meta -- kill the control landing page early**: While not yet at formal statistical significance (p=0.08), the new landing page is showing a 35% vs 22% conversion rate with directional confidence. Given the magnitude of improvement and the downside risk (keeping a clearly inferior page running), recommend switching 100% traffic to the new page and monitoring for 2 more weeks. This is a pragmatic decision, not a statistical one.

3. **Google Ads -- landing page approaching significance**: Treatment at 27% vs control 19% (p=0.06). Continue test for one more week to reach significance. Meanwhile, the new ad copy is a clear winner (+22% CTR). Scale new copy across all ad groups.

**Coordinator Decision**: Approve all recommendations. Additionally, begin planning budget reallocation for Week 4 based on trends.

---

## Phase 5: Results & Budget Reallocation

**Agents involved**: Growth Analyst (analysis), Coordinator (decisions), Demand Generation (execution)

### Week 3-4 Consolidated Results

| Channel | Monthly Spend | MQLs | Cost/MQL | SQLs | Cost/SQL | MQL→SQL % | CAC |
|---------|--------------|------|----------|------|----------|-----------|-----|
| **LinkedIn** | $6,000 | 26 | $231 | 14 | $429 | 54% | $380 |
| **Meta** | $2,000 | 18 | $111 | 6 | $333 | 33% | $350 |
| **Google Ads** | $2,000 | 20 | $100 | 9 | $222 | 45% | $260 |
| **Total** | **$10,000** | **64** | **$156** | **29** | **$345** | **45%** | **$320** |

### Before vs After Comparison

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Blended CAC | $450 | $320 | -29% |
| Monthly MQLs | 65 | 64 | -2% (but quality dramatically higher) |
| Monthly SQLs | 20 | 29 | +45% |
| MQL-to-SQL conversion | 31% | 45% | +14pp |
| Cost per SQL | $500 | $345 | -31% |

### Key Insights

1. **MQL count stayed roughly flat, but SQL count increased 45%.** This is the critical lesson: optimizing for MQL volume was the wrong goal. The team was generating 65 MQLs but only 20 SQLs. By optimizing for quality, they generate 64 MQLs and 29 SQLs with the same budget.

2. **Meta is no longer a volume trap.** Narrowing targeting and improving the landing page transformed Meta from a channel that wasted sales time (14% SQL conversion) to a legitimate contributor (33% SQL conversion). Volume dropped from 35 to 18 MQLs, but SQLs actually increased from 5 to 6.

3. **Google Ads is the efficiency winner.** At $260 CAC, Google Ads is the most efficient channel by far. The combination of keyword pruning and landing page optimization doubled its output.

4. **LinkedIn is the quality winner.** At 54% SQL conversion and the highest deal sizes, LinkedIn produces the most valuable pipeline per dollar. The higher CAC ($380) is justified by higher LTV.

### Proposed Budget Reallocation for Next Month

Based on marginal CAC analysis, the Growth Analyst recommends:

| Channel | Current Spend | Proposed Spend | Change | Rationale |
|---------|--------------|---------------|--------|-----------|
| LinkedIn | $6,000 | $6,500 | +$500 | Marginal CAC still below target. Test $6.5K before expected diminishing returns. |
| Google Ads | $2,000 | $2,500 | +$500 | Most efficient channel. Expand to adjacent keyword groups. |
| Meta | $2,000 | $1,000 | -$1,000 | Quality improved but marginal Meta MQL is still least efficient. Reduce to focus budget on stronger channels. |
| **Total** | **$10,000** | **$10,000** | **$0** | Budget-neutral reallocation |

**Expected outcome with new allocation**:

| Metric | Current | Projected | Change |
|--------|---------|-----------|--------|
| Blended CAC | $320 | $295 | -8% (below $300 target) |
| Monthly MQLs | 64 | 68 | +6% |
| Monthly SQLs | 29 | 33 | +14% |

### Coordinator Decision

Approve the reallocation with one addition: allocate $500 of the Meta reduction to test a new channel (Reddit Ads targeting engineering subreddits) as a small-budget experiment. This maintains the 15-20% experimentation budget principle.

Final allocation: LinkedIn $6,500 / Google $2,500 / Meta $500 / Reddit $500 (experiment).

---

## Optimization Cycle Summary

```
Week 0:  Baseline: CAC $450, 65 MQLs, 20 SQLs
Week 1:  Diagnose root causes, form hypotheses
Week 2:  Design experiments, launch tests
Week 3:  Execute, monitor, make early kill/continue decisions
Week 4:  Consolidate results, calculate new baseline
Week 5:  Reallocate budget, plan next experiment cycle
Result:  CAC $320, 64 MQLs, 29 SQLs (projected: CAC $295 with reallocation)
```

**Total optimization cycle: 4 weeks to achieve a 29% CAC reduction and 45% SQL increase with zero budget increase.**

---

## Agent Contribution Map

| Agent | Contribution |
|-------|-------------|
| **Growth Analyst** | Baseline analysis, root cause diagnosis, experiment design, statistical monitoring, marginal CAC analysis, budget reallocation recommendation |
| **Demand Generation** | Campaign execution, keyword management, bid optimization, landing page A/B test implementation, new creative deployment |
| **Brand & Messaging** | Pain-focused landing page copy for Meta, message-matched headlines for Google Ads |
| **Coordinator** | Strategic prioritization, kill/continue decisions, budget reallocation approval, experiment budget allocation |
| **Pipeline Manager** | SQL validation, conversion tracking from MQL through pipeline stages |

---

## Lessons for Repeatability

1. **Diagnose before optimizing.** The instinct was to cut Meta budget (cheap but unqualified leads). The analysis showed the problem was targeting and messaging, not the channel itself. Cutting Meta would have lost 6 SQLs/month.

2. **Optimize for SQLs, not MQLs.** The team was benchmarking on MQLs ($154 average cost per MQL looked acceptable). Switching to SQL-based optimization revealed that the $100 Meta MQLs cost $700 per SQL -- the most expensive channel by the metric that matters.

3. **Run experiments sequentially within a channel, in parallel across channels.** Testing targeting and landing page simultaneously on Meta made it impossible to isolate which change drove the improvement. Sequential testing (targeting first, landing page second) produced cleaner learnings even though it took an extra week.

4. **Set kill criteria before starting.** Having predetermined kill criteria prevented the team from letting losing experiments run too long and wasting budget. The early kill on the Meta control landing page saved approximately $300 in wasted spend.

5. **Budget reallocation is the highest-leverage optimization.** Individual channel optimizations improved efficiency 10-20%. Budget reallocation toward the most efficient channels amplified those gains to 29% total CAC improvement.
