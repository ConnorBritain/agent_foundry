# Scenario: Lead-to-Customer Journey

## Overview

This scenario traces the complete lifecycle of a single prospect from anonymous website visitor through becoming a paying customer and expanding their account. It demonstrates how all seven agents coordinate across the full funnel, with specific handoffs, content touchpoints, and data flows at each transition.

The journey follows four phases: Awareness & Lead Capture, Nurture & Qualification, Sales Process, and Onboarding & Expansion. Each phase maps to specific agent responsibilities and measurable outcomes.

---

## The Prospect

For this scenario, we follow **Sarah Chen, VP of Engineering** at a 200-person B2B SaaS company. Her team of 35 engineers is growing fast, and deployment velocity has stalled. She is a strong match for the "VP of Engineering" persona defined in the GTM strategy.

---

## Phase 1: Awareness & Lead Capture

**Goal**: Move Sarah from anonymous stranger to known Marketing Qualified Lead (MQL).

**Agents involved**: Demand Generation, Brand & Messaging, Growth Analyst

### Step-by-Step Journey

**Day 0 -- Google Search**

Sarah searches "how to speed up deployment pipeline" after a frustrating sprint retrospective where the team identified slow deployments as the number one blocker. Google returns a mix of organic results and paid ads.

- **Demand Generation** has set up a Google Ads search campaign targeting high-intent keywords like "speed up deployment pipeline", "deployment automation tool", and "CI/CD platform comparison". The campaign uses exact match for core terms and phrase match for long-tail variations. Bid strategy is target CPA, calibrated against 45 days of historical conversion data.
- **Growth Analyst** has defined the tracking plan: UTM parameters on every paid link (source=google, medium=cpc, campaign=deployment-speed, content=search-ad-v2), Google Ads conversion tracking on form submissions, and Google Analytics events for page engagement.

**Day 0 -- Paid Ad Click**

Sarah clicks the ad. The headline reads: "Ship 10x Faster Without Hiring -- See How 500 Engineering Teams Eliminated Deployment Bottlenecks." The ad speaks to her specific pain (deployment speed) and includes social proof (500 teams).

- **Brand & Messaging** wrote the ad copy following the messaging hierarchy: the headline addresses the primary pain point with a quantified outcome, the description elaborates with a differentiator. Copy was A/B tested against two variants; this variant won with a 23% higher CTR at statistical significance after 2,400 impressions per variant.

**Day 0 -- Landing Page**

The ad links to a dedicated landing page. Message match is exact: the page headline mirrors the ad promise. The page structure follows the Demand Generation landing page template:

1. **Headline**: "Ship 10x Faster Without Hiring" (matches ad)
2. **Subheadline**: "Engineering teams waste 30% of their time fighting deployment infrastructure instead of building product. We fix that."
3. **Benefit bullets**: Three benefits, each addressing a pain point from the VP Engineering persona profile
4. **Social proof**: Logos of 5 customers in the 100-500 employee range, plus a testimonial from a VP of Engineering at a similar company
5. **Lead magnet CTA**: "Download: The Engineering Leader's Guide to 10x Deployment Speed" -- a gated PDF that provides genuine tactical value
6. **Form**: Name, work email, company name, team size (4 fields; appropriate for top-of-funnel)

**Day 0 -- Lead Magnet Download**

Sarah fills out the form and downloads the guide. At this moment:

- **Demand Generation** captures the lead in HubSpot with source attribution (Google Ads, search campaign, deployment-speed keyword cluster)
- **Growth Analyst** records the first touch in the attribution model: Google Ads (search) gets first-touch credit
- **Pipeline Manager** receives the lead data; the lead scoring model assigns an initial score based on form data: VP of Engineering (+20 for title match), 200-person company (+25 for company size match), work email domain confirmed (+10)

**Day 0 -- MQL Threshold**

Sarah's lead score crosses the MQL threshold of 55 points (title match + company size + content download + form completion). She is now a Marketing Qualified Lead.

- **Demand Generation** triggers the MQL nurture sequence: a 5-email series over 14 days designed to educate, build trust, and move her toward a sales conversation
- **Growth Analyst** logs the MQL event with timestamp and attribution data

### Phase 1 Metrics

| Metric | Target | Actual (This Journey) |
|--------|--------|-----------------------|
| Ad CTR | >2.5% | 3.1% |
| Landing page conversion rate | >25% | Form submitted (converted) |
| Cost per MQL | <$150 | $127 (campaign average) |
| Time to MQL | <1 day | Same day |

---

## Phase 2: Nurture & Qualification

**Goal**: Move Sarah from MQL to Sales Qualified Lead (SQL) through education, engagement, and intent signals.

**Agents involved**: Demand Generation, Brand & Messaging, Pipeline Manager, Growth Analyst

### Step-by-Step Journey

**Days 1-3 -- Email Nurture: Education**

The nurture sequence, designed by Demand Generation and written using Brand & Messaging's messaging library:

- **Email 1 (Day 1)**: "Here's your guide + 3 things most teams get wrong about deployment speed." Delivers the lead magnet with added value. Open rate target: >40%.
- **Email 2 (Day 3)**: "How [Customer Name] cut deployment time from 4 hours to 12 minutes." Case study email. Specific, quantified results from a company similar to Sarah's. Links to full case study on the website.

Sarah opens both emails and clicks through to the case study. Each interaction adds to her lead score and attribution record.

**Days 5-8 -- Content Engagement**

- **Email 3 (Day 5)**: "The hidden cost of slow deployments: a calculator." Links to an interactive ROI calculator (built by Sales Enablement, promoted by Demand Generation). Sarah enters her team size (35 engineers) and estimated deployment frequency. The calculator shows she is losing approximately $420K/year in engineering productivity.
- Sarah visits the blog post "CI/CD Platform Comparison: 2026 Edition" via organic search (new touchpoint in the attribution model)
- Sarah visits the pricing page for the first time

**Day 8 -- Intent Signal: Pricing Page Visit**

The pricing page visit is a high-intent signal. Pipeline Manager's lead scoring model adds +15 points. Combined with her engagement history:

| Signal | Points |
|--------|--------|
| Title match (VP Engineering) | +20 |
| Company size match | +25 |
| Lead magnet download | +10 |
| Email opens (2) | +5 |
| Email clicks (2) | +10 |
| Case study visit | +5 |
| ROI calculator usage | +10 |
| Pricing page visit | +15 |
| **Total** | **100** |

**Day 10 -- Demo Request**

- **Email 4 (Day 10)**: "See it in action: book a 20-minute demo tailored to your stack." The CTA drives to a demo booking page with calendar integration.
- Sarah books a demo. This is the highest-intent action available.

**Day 10 -- SQL Threshold**

Sarah's lead score is now 115 (100 + 15 for demo request). She crosses the SQL threshold of 80. The system:

1. **Pipeline Manager** creates a deal in HubSpot at the "SQL Accepted" stage with all engagement history attached
2. **Demand Generation** exits Sarah from the nurture sequence to avoid marketing/sales conflict
3. **Growth Analyst** logs the MQL-to-SQL conversion: 10 days (under the 14-day target)
4. **Pipeline Manager** assigns the deal to a sales rep and creates a task: "Prepare for discovery call using engagement history"

### Phase 2 Metrics

| Metric | Target | Actual (This Journey) |
|--------|--------|-----------------------|
| MQL-to-SQL conversion | >20% | Converted |
| MQL-to-SQL time | <14 days | 10 days |
| Email open rate (sequence avg) | >35% | 42% |
| Email click rate (sequence avg) | >5% | 7.3% |
| Pricing page visit before SQL | Yes | Yes (Day 8) |

---

## Phase 3: Sales Process

**Goal**: Move Sarah from SQL through Discovery, Demo, Proposal, and Close.

**Agents involved**: Pipeline Manager, Sales Enablement, Brand & Messaging, Growth Analyst

### Step-by-Step Journey

**Day 12 -- Discovery Call**

The sales rep prepares using:
- **Sales Enablement** discovery question guide: 8 questions tailored to the VP Engineering persona, covering current deployment process, team pain points, decision-making process, budget, and timeline
- **Pipeline Manager** engagement history: the rep knows Sarah downloaded the deployment guide, used the ROI calculator (35 engineers, $420K loss estimate), read the case study, and visited pricing

Key discovery findings:
- Pain: Deployments take 3-4 hours, happen only twice per week, blocking feature velocity
- Urgency: Board mandated faster delivery speed in Q1 planning
- Budget: Has budget authority for tools under $50K/year
- Timeline: Wants to decide within 30 days
- Decision process: Sarah decides, CTO signs off, procurement handles contract
- Competition: Also evaluating one competitor

The rep logs these findings in HubSpot. Pipeline Manager validates the stage criteria and moves the deal to "Discovery Complete."

**Day 15 -- Needs Analysis & Custom Demo Prep**

The sales rep works with materials from Sales Enablement:
- **Demo script** for the VP Engineering persona: focuses on deployment speed, team productivity, and visibility
- **Competitive battle card** for the identified competitor: honest strengths/weaknesses, landmine questions, and win themes
- **ROI calculator** pre-filled with Sarah's data from the earlier calculator interaction

**Day 18 -- Custom Demo**

The demo follows Sales Enablement's branching demo script:
1. **Setup (3 min)**: "Based on our discovery call, your top priorities are deployment speed and team visibility. Let me show you exactly how we address those."
2. **Core flow (12 min)**: Live demonstration of the deployment pipeline, showing a code change going from commit to production in under 4 minutes. Directly addresses the "3-4 hour deployment" pain point.
3. **Differentiator moment (5 min)**: Shows the feature that competitors cannot match -- zero-config setup that auto-detects the existing CI/CD pipeline. This is a landmine question from the battle card: "Ask them to show you their onboarding process."
4. **ROI review (5 min)**: Shows the pre-filled ROI calculator: 35 engineers x 6 hours/week saved = $420K/year. At $36K/year contract, payback period is 1 month.
5. **Close (3 min)**: "Based on what we've discussed, I'd like to put together a proposal. Can I schedule 20 minutes next Tuesday to walk through it with you and your CTO?"

Sarah agrees and provides the CTO's email for the proposal meeting. Deal moves to "Demo/Evaluation" stage.

**Day 22 -- Proposal with ROI**

Sales Enablement materials used:
- **Proposal template**: Executive summary, problem statement, solution overview, implementation plan, pricing, ROI analysis, customer references
- **ROI calculator output**: Formatted one-pager showing annual savings, payback period, and 3-year return
- **Case study**: One-page summary of a similar company's results (matched on team size and industry)

The proposal includes:
- Annual contract: $36,000 (30 seats at $100/month)
- Implementation: 2-week guided onboarding included
- ROI: $420K annual savings, <1 month payback, 11.7x ROI in year 1

Deal moves to "Proposal/Negotiation" stage.

**Day 25 -- Objection Handling**

Sarah returns with two objections:

1. **"The competitor is 20% cheaper"**
   - Sales Enablement objection playbook response: Acknowledge the price difference. Reframe to total cost of ownership. "Their base price is lower, but they charge for implementation ($15K), require dedicated DevOps support (0.5 FTE), and their average deployment time is 3x ours based on G2 reviews. When you factor those in, the total cost over 3 years is actually 40% higher."

2. **"My CTO wants to see a proof of concept first"**
   - Objection playbook response: "Absolutely. We offer a 14-day production trial. Unlike a sandbox POC, you'll test with your actual codebase. Here's the POC success criteria template so we can agree on what 'success' looks like before we start."

Both objections are resolved. Sarah and the CTO agree to the proposal terms. Deal moves to "Contract/Legal" stage.

**Day 30 -- Contract & Close**

- Procurement requests minor contract modifications (standard liability cap adjustment)
- Sales rep uses the legal FAQ from Sales Enablement to address procurement questions without involving legal, saving 3-5 days
- Contract signed on Day 32

Deal moves to "Closed Won." Pipeline Manager:
- Marks the deal as closed-won with final value ($36,000 ACV)
- Logs close date, win reasons, and competitive outcome
- Triggers the sales-to-CS handoff workflow

### Phase 3 Metrics

| Metric | Target | Actual (This Journey) |
|--------|--------|-----------------------|
| SQL-to-Opportunity conversion | >30% | Converted |
| Opportunity-to-Customer conversion | >25% | Converted |
| Sales cycle (SQL to Close) | <45 days | 22 days |
| Average deal size | $36,000 | $36,000 |
| Competitive win | -- | Won against 1 competitor |
| Discount given | <10% | 0% |

---

## Phase 4: Onboarding & Expansion

**Goal**: Get Sarah's team to first value within 7 days, full adoption within 30 days, and expansion within 12 months.

**Agents involved**: Customer Success, Pipeline Manager, Growth Analyst

### Step-by-Step Journey

**Day 32 -- Handoff & Welcome**

Pipeline Manager's handoff workflow triggers:
1. Customer Success receives the deal package: discovery notes, demo recording link, proposal, contract, champion profile (Sarah), decision-maker profile (CTO), technical requirements, and success criteria agreed during sales
2. CS assigns the account to a CSM based on the mid-market segment (ACV $36K)

Customer Success sends the Day 0 welcome:
- Welcome email with CS team introduction, onboarding timeline, and first meeting invite
- Access provisioning instructions
- Link to the quick-start guide

**Day 33 -- Kickoff Call (Day 1)**

CSM conducts the onboarding kickoff using the Customer Success onboarding playbook:
- Reviews Sarah's goals (cut deployment time from 3-4 hours to under 15 minutes)
- Defines success criteria: 10+ deployments per week within 30 days
- Agrees on timeline: first deployment by Day 5, team rollout by Day 14
- Identifies onboarding champion: Sarah's senior DevOps engineer
- Creates the success plan in HubSpot

**Days 34-36 -- Setup (Days 2-4)**

- Technical integration completed by Day 3 (connected to existing CI/CD pipeline)
- Configuration completed by Day 4 (deployment rules, notification channels, team permissions)
- Onboarding risk check: on track (login confirmed, integration active)

**Day 37 -- First Value (Day 5)**

Sarah's team completes their first deployment through the platform. Time: 7 minutes (down from 3-4 hours). This is the "first value" milestone.

- Customer Success logs the time-to-first-value: 5 days (under the 7-day target)
- Health score initialized: Green (product usage active, engagement strong, first value achieved)
- CSM sends congratulations message with tips for the next milestone

**Days 38-45 -- Adoption (Days 6-13)**

- Team rollout: 12 of 35 engineers actively using the platform by Day 10
- Second use case explored: automated rollback configuration
- CSM conducts Week 1 check-in call: reviews initial results, troubleshoots adoption blockers, plans team-wide rollout

**Day 62 -- Month 1 Review**

CSM conducts the 30-day review using the Customer Success QBR template (abbreviated version for Month 1):
- Deployment frequency: increased from 2/week to 8/week
- Deployment time: reduced from 3-4 hours to average 8 minutes
- Active users: 28 of 35 engineers (80% adoption)
- First-month ROI: $35K in engineering time recovered
- Health score: Green (87/100)

Satisfaction data collected: NPS score of 9 (promoter).

**Day 120 -- Quarter 1 QBR & Expansion**

Customer Success conducts the full QBR:

1. **Success review**: Deployments up 4x, time reduced 95%, zero deployment-related incidents in Q1
2. **Usage analysis**: Team hitting 85% of seat allocation. Three additional teams (QA, data engineering, platform) have expressed interest.
3. **Expansion signals detected**:
   - Usage at 85% of tier capacity
   - Additional teams requesting access
   - Sarah promoted to SVP (expanded responsibilities)
   - Company raised Series C (growth mode)

Expansion conversation follows the Customer Success expansion framework:
1. Review success: "Your team deployed 340 times last quarter with zero incidents. How does that compare to your expectations?"
2. Identify growth: "I've noticed the data engineering team has been asking about access. What's driving that?"
3. Quantify potential: "Companies that expand to cross-team usage typically see an additional 40% productivity gain from standardized deployment practices."
4. Propose naturally: "Would it be helpful if I put together a proposal for expanding to those three teams?"

Sarah agrees. The expansion deal:
- 45 additional seats at $100/month = $54,000 additional ACV
- Total ACV: $90,000 (2.5x original deal)
- Pipeline Manager creates expansion opportunity in HubSpot

**Day 135 -- Expansion Close**

Expansion deal closes. Year 1 totals:
- Original ACV: $36,000
- Expansion ACV: $54,000
- Total Year 1 revenue: $90,000
- Expansion rate: 150% (well above the 20% target)

### Phase 4 Metrics

| Metric | Target | Actual (This Journey) |
|--------|--------|-----------------------|
| Time to first value | <7 days | 5 days |
| 30-day adoption | >60% of seats | 80% (28/35) |
| Month 1 health score | Green | Green (87/100) |
| NPS | >8 | 9 |
| Year 1 retention | >85% | Retained |
| Year 1 expansion | >20% | 150% |
| Year 1 total revenue | >$36,000 | $90,000 |

---

## Full Journey Summary

```
Day 0:   Google search → paid ad → landing page → lead magnet → MQL
Day 1-10: Email nurture → content engagement → pricing page → demo request → SQL
Day 12:  Discovery call
Day 18:  Custom demo
Day 22:  Proposal with ROI
Day 25:  Objection handling
Day 32:  Contract signed → Closed Won
Day 33:  Onboarding kickoff
Day 37:  First value (7-minute deployment)
Day 62:  Month 1 review (80% adoption)
Day 120: Quarter 1 QBR → expansion proposal
Day 135: Expansion close (2.5x original deal)
```

**Total journey: 135 days from stranger to expanded customer.**

---

## Success Criteria Summary

| Metric | Target | Result | Status |
|--------|--------|--------|--------|
| MQL to SQL conversion time | <14 days | 10 days | Pass |
| SQL to Opportunity conversion | >30% | 100% | Pass |
| Opportunity to Customer conversion | >25% | 100% | Pass |
| Sales cycle (SQL to Close) | <45 days | 22 days | Pass |
| Time to first value | <7 days | 5 days | Pass |
| Year 1 retention | >85% | Retained | Pass |
| Year 1 expansion | >20% | 150% | Pass |

---

## Agent Contribution Map

| Agent | Phase 1 | Phase 2 | Phase 3 | Phase 4 |
|-------|---------|---------|---------|---------|
| **Coordinator** | Strategy brief, persona definition | -- | -- | -- |
| **Brand & Messaging** | Ad copy, landing page messaging | Email copy, CTA language | -- | -- |
| **Demand Generation** | Google Ads campaign, landing page, lead magnet | Email nurture sequence, retargeting | -- | -- |
| **Pipeline Manager** | Lead scoring | SQL creation, deal staging | Stage management, handoff | Expansion deal tracking |
| **Sales Enablement** | -- | ROI calculator | Discovery guide, demo script, battle card, proposal, objection playbook | -- |
| **Customer Success** | -- | -- | -- | Onboarding, health scoring, QBR, expansion |
| **Growth Analyst** | Attribution tracking, UTM plan | Conversion tracking | Win/loss logging | Cohort analysis, LTV calculation |

---

## Key Takeaways

1. **The handoffs matter as much as the work within each phase.** Sarah's experience was seamless because the MQL-to-SQL, SQL-to-demo, sales-to-CS, and CS-to-expansion handoffs were all explicitly defined with data passing between agents.

2. **Personalization compounds.** The sales rep knew about the ROI calculator interaction. The CSM knew about the discovery call findings. Each agent built on the context gathered by previous agents.

3. **Timing drives conversion.** The nurture sequence was calibrated to Sarah's engagement signals, not an arbitrary calendar. The demo was scheduled when intent was highest (pricing page visit + demo request).

4. **Expansion is a natural outcome of success.** The CSM did not "sell" the expansion. The expansion was a logical consequence of demonstrable value, usage growth, and a well-timed QBR conversation.
