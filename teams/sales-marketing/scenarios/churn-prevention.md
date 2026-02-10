# Scenario: Churn Prevention

## Overview

This scenario covers the detection, assessment, and intervention workflow for at-risk customer accounts. It models a customer base where annual churn is running at 8% (target: 5%) and demonstrates how the Customer Success, Growth Analyst, and Coordinator agents collaborate to build and execute a churn prevention system that identifies at-risk accounts early, diagnoses root causes, intervenes effectively, and tracks outcomes.

The goal is to reduce churn from 8% to 5% annually and achieve a save rate of >60% for flagged accounts.

---

## Starting State

### Customer Base Profile

| Metric | Value |
|--------|-------|
| Total customers | 250 |
| Annual churn rate | 8% (20 customers/year) |
| Monthly churn rate | ~0.67% (~1.7 customers/month) |
| Average ACV | $36,000 |
| Annual revenue at risk from churn | $720,000 |
| Target churn rate | 5% (12.5 customers/year) |
| Revenue saved if target achieved | $270,000/year |

### Why 8% Is a Problem

At 8% annual churn with a $3,000 CAC and $36,000 ACV:
- Each lost customer represents $36,000 in recurring revenue
- Replacing a churned customer costs $3,000 in acquisition + lost expansion revenue
- At 20 churns/year, that is $720K in lost recurring revenue plus $60K in replacement cost
- Reducing churn by 3 percentage points (8% to 5%) saves $270K/year in revenue -- equivalent to acquiring 7.5 new customers without spending a dollar on marketing

---

## Detection: Churn Signal Framework

**Agents involved**: Customer Success (signal definition), Growth Analyst (scoring model), Pipeline Manager (CRM integration)

### Signal Categories

The churn prediction system monitors five categories of signals, each contributing to an overall risk score.

**Category 1: Product Usage Decline**

| Signal | Detection Method | Weight | Threshold |
|--------|-----------------|--------|-----------|
| Login frequency declining | Week-over-week active users trending down for 3+ weeks | High | >20% decline from 90-day average |
| Core feature abandonment | Key workflow completions dropping | High | >30% decline from 90-day average |
| Session duration shrinking | Average time-in-product decreasing | Medium | >25% decline from 90-day average |
| API call volume dropping | API request count trending down (for technical products) | Medium | >30% decline from 90-day average |
| New feature non-adoption | New features released but not used within 30 days | Low | 0 usage of last 2 feature releases |

**Category 2: Support Patterns**

| Signal | Detection Method | Weight | Threshold |
|--------|-----------------|--------|-----------|
| Ticket volume spike | Support tickets increasing month-over-month | Medium | >2x normal monthly volume |
| Severity escalation | Proportion of high-severity tickets increasing | High | >50% of tickets are P1/P2 |
| Repeated issues | Same issue reported 3+ times without resolution | High | 3+ tickets on same topic |
| Negative CSAT | Post-ticket satisfaction score below threshold | Medium | CSAT <3/5 on last 2+ tickets |
| "Cancel" or "alternative" language | NLP detection of churn-related language in tickets | High | Any mention of cancellation, competitor names, or "looking for alternatives" |

**Category 3: Engagement Decline**

| Signal | Detection Method | Weight | Threshold |
|--------|-----------------|--------|-----------|
| Meeting cancellations | CSM meetings cancelled or no-showed | High | 2+ consecutive cancellations |
| Email non-response | CSM emails unanswered | Medium | No response to last 3 outreach attempts |
| QBR declined | Customer declines or reschedules QBR | High | QBR postponed 2+ times |
| Community disengagement | Stopped participating in user community or events | Low | No community activity in 60+ days |
| Training non-attendance | Invited to training sessions but does not attend | Medium | Declined/missed 3+ sessions |

**Category 4: Competitive & Market Signals**

| Signal | Detection Method | Weight | Threshold |
|--------|-----------------|--------|-----------|
| Competitor mentioned | Customer mentions competitor in any interaction | High | Any mention |
| RFP or evaluation process | Customer starts formal evaluation or RFP | Critical | Any indication |
| Competitor content engagement | Customer engaging with competitor content (if trackable) | Medium | 3+ competitor content interactions |
| Industry analyst inquiry | Customer asks analyst firms about alternatives | Medium | Any indication from relationship intel |

**Category 5: Contract & Financial Signals**

| Signal | Detection Method | Weight | Threshold |
|--------|-----------------|--------|-----------|
| Renewal approaching without engagement | Contract within 90 days of renewal with no recent CSM interaction | High | <90 days to renewal + no meeting in 30 days |
| Budget review requested | Customer asks about downgrade options or cost reduction | High | Any inquiry |
| Payment failure | Invoice unpaid or payment method declined | Medium | Payment >15 days overdue |
| Champion departure | Primary champion leaves company or changes role | Critical | Any confirmed departure |
| New decision-maker | New executive asking "what does this product do for us?" | High | Any re-evaluation inquiry |

---

## Risk Scoring Model

**Agent involved**: Growth Analyst

### Scoring Methodology

Each account receives a composite risk score calculated weekly. The score ranges from 0 (no risk) to 100 (maximum risk), mapped to three risk tiers.

**Score Calculation**:

```
Risk Score = (Usage Score * 0.30) + (Support Score * 0.15) + (Engagement Score * 0.25)
           + (Competitive Score * 0.15) + (Contract Score * 0.15)
```

Each component score is 0-100, where 0 = healthy and 100 = critical risk.

**Component Scoring**:

Usage Score:
- 0-20: Usage at or above 90-day average
- 21-40: Usage 10-20% below average (normal fluctuation)
- 41-60: Usage 20-35% below average (concerning trend)
- 61-80: Usage 35-50% below average (significant decline)
- 81-100: Usage >50% below average or approaching zero

Engagement Score:
- 0-20: Regular meetings, responsive to emails, attending events
- 21-40: Slightly less responsive than normal
- 41-60: Missed 1 meeting, delayed email responses
- 61-80: Missed 2+ meetings, multiple unanswered emails
- 81-100: Unresponsive to all outreach for 30+ days

Support Score:
- 0-20: Low ticket volume, high satisfaction
- 21-40: Normal ticket volume, average satisfaction
- 41-60: Elevated ticket volume or declining satisfaction
- 61-80: High ticket volume with severity escalation
- 81-100: Critical escalations, repeated unresolved issues, churn language

Competitive Score:
- 0-20: No competitive signals detected
- 21-40: Indirect signals (competitor content engagement)
- 41-60: Direct mention of competitor in conversation
- 61-80: Active evaluation of competitors confirmed
- 81-100: RFP issued or formal evaluation in progress

Contract Score:
- 0-20: Renewal >180 days away, or recent renewal completed
- 21-40: Renewal 90-180 days away with healthy engagement
- 41-60: Renewal <90 days with no renewal discussion started
- 61-80: Renewal <60 days with declining engagement or budget concerns
- 81-100: Champion departed, new decision-maker questioning value, or downgrade requested

### Risk Tiers

| Tier | Score Range | Color | Accounts (est.) | Action Level |
|------|-------------|-------|-----------------|--------------|
| **Green** | 0-29 | Green | ~200 (80%) | Monitor. Standard CSM cadence. |
| **Yellow** | 30-59 | Yellow | ~35 (14%) | Attention. CSM proactive outreach within 1 week. |
| **Red** | 60-100 | Red | ~15 (6%) | Critical. Immediate intervention. CS leadership involved. |

### Score Transitions

The system also monitors score transitions, which are more actionable than absolute scores:

| Transition | Action |
|------------|--------|
| Green to Yellow | CSM notified. Proactive outreach within 5 business days. |
| Yellow to Red | CS leadership notified. Intervention plan required within 48 hours. |
| Red to Yellow | Intervention showing progress. Continue plan. Weekly monitoring. |
| Yellow to Green | Risk mitigated. Resume standard cadence. Document learnings. |
| Any to Red (jump) | Immediate escalation. Usually triggered by champion departure or competitor RFP. |

---

## Intervention Workflow

**Agents involved**: Customer Success (primary), Coordinator (escalation), Sales Enablement (re-engagement materials), Growth Analyst (impact analysis)

### Step 1: Identify At-Risk Account

The risk scoring model flags an account. For this scenario, we follow **Acme Corp**:

- **Account**: Acme Corp, 80 seats, $96K ACV, 8 months into annual contract
- **Risk score**: 67 (Red) -- jumped from Green (22) to Red in one week
- **Trigger**: Champion (VP of Engineering, Maria Lopez) left the company. New VP asking "what does this product do for us?"
- **Secondary signals**: Login frequency down 15% over past 3 weeks (team uncertain without champion), 2 support tickets from new VP's team asking basic "how to" questions (suggests new stakeholders unfamiliar with the product)

### Step 2: Root Cause Analysis

The CSM conducts a structured root cause analysis within 48 hours of the Red flag:

**Information Gathering**:
- Review all engagement history for the past 90 days
- Check product usage data for the account (Growth Analyst provides usage analytics)
- Review support ticket history for the past 60 days
- Check if renewal date is approaching (4 months away)
- Identify all contacts at the account and their engagement status

**Root Cause Assessment**:

| Factor | Finding | Severity |
|--------|---------|----------|
| Champion loss | Maria Lopez (VP Eng) left. She was the executive sponsor and internal advocate. | Critical |
| New decision-maker | James Park (new VP Eng) has no context on the product's value or the original buying decision. | High |
| Knowledge gap | New team members do not understand the product's full capabilities. Basic "how to" tickets suggest underutilization. | Medium |
| Usage decline | 15% login decline is modest but directionally concerning. Likely reflects uncertainty, not dissatisfaction. | Medium |
| Product value | Product is actually delivering well. Deployment metrics are strong. The value exists but is not visible to the new VP. | Positive signal |

**Root Cause Summary**: This is a classic champion-loss churn risk. The product is delivering value, but the new decision-maker does not know it. Without intervention, James Park will evaluate the renewal based on incomplete information, potentially deciding to cut a tool he does not understand to make budget room for tools he does understand.

### Step 3: Intervention Plan

The CSM creates a tailored intervention plan based on the root cause analysis:

**Objective**: Establish a relationship with James Park, demonstrate the product's current value to his team, and secure his buy-in as the new champion within 4 weeks (well before the renewal conversation in 4 months).

**Week 1 -- Executive Introduction**:
- CSM sends a personalized email to James Park introducing the CS team and offering a "transition briefing" (not a sales pitch -- positioned as helping him get up to speed on tools his team uses)
- Prepare a 1-page value summary: what the product does for Acme, key metrics (deployment time reduction, deployment frequency increase, team time saved), and ROI data from the last QBR
- Coordinator provides executive air cover: CS leadership sends a brief welcome note to James from a VP-to-VP level

**Week 2 -- Transition Briefing Meeting**:
- Conduct the transition briefing with James (30 minutes, not 60 -- respect his time as a new VP with many priorities)
- Agenda: (1) What the product does for Acme today (5 min, with metrics), (2) How his team uses it (10 min, with usage data), (3) What his team says about it (5 min, with internal NPS/feedback), (4) What's coming that's relevant to his priorities (5 min), (5) How we support the team going forward (5 min)
- Sales Enablement provides a streamlined "executive re-engagement deck" -- not the original sales deck, but a concise value demonstration for an existing customer's new stakeholder
- Bring one of James's senior engineers (who actively uses the product) to the meeting as an internal advocate

**Week 3 -- Team Re-Training**:
- Offer a 45-minute "power user session" for James's team, positioned as training on recent features (not remedial training)
- Identify 2-3 features the team is not using that directly address pain points James mentioned in the transition briefing
- Customer Success creates a custom adoption roadmap for new features

**Week 4 -- Success Confirmation**:
- Send James a personalized follow-up with updated usage metrics showing his team's engagement since the re-training
- Propose scheduling a formal QBR in Month 2 of the intervention (2 months before renewal)
- If engagement is positive, introduce the idea of expanding to James's new initiatives (he may have priorities Maria did not)

### Step 4: Executive Sponsor Engagement

When a Red-tier account involves champion loss or new executive stakeholders, the Coordinator activates executive sponsor engagement:

- CS leadership (VP or Director level) sends a personal welcome note to James
- If James is unresponsive to CSM outreach after 1 week, escalate to an exec-to-exec call
- The Coordinator provides strategic context: Acme's account history, expansion potential, and competitive landscape in their industry

### Step 5: Resolution & Monitoring

**Tracking the intervention**:

| Week | Action | Expected Outcome | Actual Outcome |
|------|--------|-------------------|----------------|
| 1 | Executive introduction email + value summary | James responds and accepts meeting | Meeting booked for Week 2 |
| 2 | Transition briefing | James understands value; asks good questions | James engaged; asked about API capabilities for his new project |
| 3 | Team re-training session | 10+ attendees, positive feedback | 14 attendees, 4.5/5 satisfaction score |
| 4 | Follow-up with metrics + QBR proposal | James agrees to QBR; risk score declining | QBR booked, risk score dropped to Yellow (42) |
| 6 | Informal check-in | James mentions product positively in team meeting (internal advocate forming) | James's team submitted a feature request (positive engagement signal) |
| 8 | QBR | Formal success review; renewal discussion positive | Renewal confirmed. James interested in expanding to his new team (12 additional seats) |

**Risk score progression**:
- Week 0: 22 (Green)
- Week 1: 67 (Red) -- champion departure detected
- Week 2: 63 (Red) -- meeting booked but not yet held
- Week 3: 52 (Yellow) -- successful transition briefing, engagement improving
- Week 4: 42 (Yellow) -- re-training completed, usage recovering
- Week 6: 31 (Yellow) -- feature request submitted, regular engagement
- Week 8: 18 (Green) -- QBR completed, renewal confirmed, expansion pipeline

**Outcome**: Account saved. Renewal confirmed at $96K. Expansion pipeline of $14.4K (12 seats). Champion-loss risk converted to expansion opportunity.

---

## Churn Prevention at Scale

### Portfolio Risk Management

The system does not just manage individual accounts. The Growth Analyst monitors portfolio-level risk metrics:

**Weekly Risk Dashboard**:

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Accounts in Green | 200 (80%) | >80% | On target |
| Accounts in Yellow | 35 (14%) | <15% | On target |
| Accounts in Red | 15 (6%) | <5% | Above target |
| Average risk score | 24 | <25 | On target |
| Risk score trend (30-day) | -2 points | Declining | Positive |

**Monthly Churn Funnel**:

```
250 total accounts
     │
     ├── 200 Green (80%) ──→ Expected churn: <1% ──→ ~2 accounts/year
     │
     ├── 35 Yellow (14%) ──→ Expected churn: 8% ──→ ~3 accounts/year
     │                         (with intervention)
     │
     └── 15 Red (6%) ──→ Expected churn: 25% ──→ ~4 accounts/year
                           (with intervention)

Expected annual churn with intervention: ~9 accounts (3.6%)
Expected annual churn without intervention: ~20 accounts (8.0%)
Intervention value: ~11 saved accounts = ~$396K in retained revenue
```

### Intervention Playbooks by Root Cause

| Root Cause | Frequency | Save Rate | Primary Intervention |
|------------|-----------|-----------|---------------------|
| **Champion departure** | 30% of Red accounts | 65% | Executive re-engagement, transition briefing, new champion building |
| **Product value not realized** | 25% of Red accounts | 70% | Usage review, re-training, adoption roadmap, success plan reset |
| **Competitor threat** | 15% of Red accounts | 45% | Competitive response (feature roadmap, pricing review, executive engagement) |
| **Budget/cost pressure** | 15% of Red accounts | 55% | ROI demonstration, downtier option, deferred payment, multi-year discount |
| **Product quality issues** | 10% of Red accounts | 50% | Engineering escalation, dedicated support, SLA credits, product team engagement |
| **Strategic misalignment** | 5% of Red accounts | 30% | Honest assessment. If the product no longer fits, negotiate a graceful offboarding and request referral for ICP-fit contacts. |

### Proactive Prevention (Yellow Tier)

Not every intervention needs to be reactive. For Yellow-tier accounts, the system triggers proactive measures:

1. **Automated re-engagement**: In-app messages highlighting unused features relevant to the account's use case
2. **Content-driven nurture**: Email sequence sharing best practices, new features, and customer success stories
3. **CSM touchpoint**: Casual check-in call or email ("Noticed your team hasn't tried [feature] yet -- want a quick walkthrough?")
4. **Community invitation**: Invite to upcoming webinar, user group, or community event
5. **Feedback request**: "We want to make sure we're delivering value. Can you share 5 minutes of feedback?"

The goal of proactive prevention is to catch accounts before they reach Red, when intervention is easier, cheaper, and more likely to succeed.

---

## Success Criteria

### Program-Level Metrics

| Metric | Before | Target | Timeline |
|--------|--------|--------|----------|
| Annual churn rate | 8% | 5% | 6 months to reach run-rate |
| Monthly churn rate | 0.67% | 0.42% | 6 months |
| Red account save rate | N/A (no system) | >60% | 3 months to calibrate |
| Yellow account prevention rate | N/A | >80% | 3 months |
| Average time to intervention (Red) | N/A | <48 hours | Immediate |
| Average time to intervention (Yellow) | N/A | <5 business days | Immediate |
| Revenue retained (annual) | $0 incremental | $270K | 12 months |

### Risk Model Accuracy

The Growth Analyst validates the risk model quarterly:

| Validation Metric | Target |
|-------------------|--------|
| Red accounts that actually churn (true positive rate) | >25% should churn without intervention |
| Green accounts that churn (false negative rate) | <2% of churned accounts were Green 60 days before churn |
| Yellow accounts that progress to Red (true early warning) | >50% of Red accounts were Yellow before Red |
| Model calibration | Predicted churn rate within 2 percentage points of actual |

---

## Agent Contribution Map

| Agent | Contribution |
|-------|-------------|
| **Customer Success** | Signal definition, intervention playbooks, account management, QBR execution, champion building |
| **Growth Analyst** | Risk scoring model, portfolio analytics, cohort analysis, model validation, save rate tracking |
| **Coordinator** | Executive sponsor engagement, strategic escalation, resource allocation for high-value saves |
| **Sales Enablement** | Executive re-engagement materials, transition briefing deck, ROI summaries for stakeholder changes |
| **Pipeline Manager** | CRM integration for risk scores, renewal pipeline tracking, expansion opportunity creation |
| **Brand & Messaging** | Re-engagement email copy, customer communication tone/messaging for sensitive situations |

---

## Key Takeaways

1. **Churn prevention is a system, not a heroic effort.** Individual CSMs making ad hoc saves is not scalable. A scoring model with clear thresholds, intervention playbooks, and escalation protocols turns churn prevention into a repeatable process.

2. **Champion loss is the single biggest churn risk.** 30% of Red accounts are triggered by champion departure. Building multi-threaded relationships (multiple contacts, executive sponsors, user-level advocates) is the best insurance against this risk.

3. **The value exists -- it just needs to be visible.** In the Acme Corp example, the product was delivering strong results. The risk was that the new VP did not know it. Most churn is not caused by product failure; it is caused by value invisibility.

4. **Early detection dramatically improves save rates.** Catching an account at Yellow (8% expected churn with intervention) is far more effective than catching it at Red (25% expected churn with intervention). Investing in proactive Yellow-tier measures has the highest ROI.

5. **Not every account should be saved.** The 5% of Red accounts driven by strategic misalignment have a 30% save rate. Spending significant resources on accounts that no longer fit the ICP creates false retention that eventually churns anyway. Graceful offboarding with a referral request is sometimes the right answer.
