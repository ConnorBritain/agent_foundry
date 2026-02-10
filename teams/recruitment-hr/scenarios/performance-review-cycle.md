# Scenario: Performance Review Cycle

## Overview

A complete performance management cycle from goal setting through calibration and outcomes, covering a 50-person engineering organization across two quarters.

## Phase 1: Goal Setting (Quarter Start)

### Company OKR Cascade

**Company Objective**: "Become the market leader in SMB payments"
- KR1: Reach $2M ARR by Q4
- KR2: Achieve NPS > 50
- KR3: Launch enterprise tier

**Engineering Team Objective**: "Deliver enterprise-ready platform"
- KR1: Ship multi-tenant architecture (by week 8)
- KR2: Reduce p95 latency to <200ms (by week 10)
- KR3: Achieve 99.9% uptime (continuous)

### Individual Goal Setting Process

**Performance Management Specialist designs the framework:**

1. Manager sets team-level goals aligned to engineering OKRs
2. Each IC drafts 3-5 individual OKRs (mix of delivery + growth)
3. Manager reviews for alignment, ambition, measurability
4. Mutual agreement documented in performance tool

**Example Individual OKRs (Senior Engineer):**
```
Objective: Lead multi-tenant architecture migration

KR1: Design and get approval for multi-tenant schema (Week 2)
KR2: Implement tenant isolation with zero downtime (Week 6)
KR3: Load test proves 10x current capacity (Week 8)

Growth Goal: Develop technical leadership skills
KR1: Lead 3 architecture review sessions
KR2: Mentor 1 junior engineer through their first major feature
KR3: Write and publish 1 internal tech blog post
```

**SMART Criteria Checklist:**
- [ ] Specific: Clear deliverable or measurable outcome
- [ ] Measurable: Quantified or binary (done/not done)
- [ ] Achievable: Stretch but realistic given time and resources
- [ ] Relevant: Aligned to team and company objectives
- [ ] Time-bound: Clear deadline within the quarter

### Coordinator approves the process and timeline:
- Week 1: Company OKRs shared
- Week 2: Team OKRs finalized
- Week 3: Individual OKRs drafted and reviewed
- Week 4: All OKRs locked and visible to organization

## Phase 2: Mid-Cycle Check (Mid-Quarter)

### Purpose
Course correction, not evaluation. No ratings assigned.

### Manager 1:1 Template (Performance Management Specialist provides):

```markdown
## Mid-Cycle Check-in: [Employee Name]
Date: [Date]

### OKR Progress
| OKR | Status | Confidence | Notes |
|-----|--------|------------|-------|
| KR1 | On track | High | Schema approved week 2 |
| KR2 | At risk | Medium | Dependency on DevOps migration |
| KR3 | Not started | Low | Blocked until KR2 complete |
| Growth KR1 | On track | High | Led 2 of 3 sessions |

### Discussion Points
1. What's going well?
2. What's blocking progress?
3. Do any goals need to be adjusted?
4. What support do you need?

### Adjustments Made
- [Document any goal changes and rationale]

### Action Items
- Manager: [actions]
- Employee: [actions]
```

### Common Mid-Cycle Outcomes:
- **60% of OKRs**: On track, no changes
- **25% of OKRs**: Adjusted scope or timeline (documented with rationale)
- **10% of OKRs**: Replaced due to priority shift (approved by skip-level)
- **5% of OKRs**: Identified as at-risk, intervention plan created

## Phase 3: Formal Review (Quarter End)

### Self-Assessment (Employee writes)

```markdown
## Self-Assessment: [Name], Q3 2026

### OKR Results
| OKR | Target | Actual | Rating |
|-----|--------|--------|--------|
| Multi-tenant schema | Approved by W2 | Approved W2 | Met |
| Tenant isolation | Zero downtime by W6 | Completed W7 (1 week late) | Mostly Met |
| Load test 10x | By W8 | 12x capacity achieved W9 | Exceeded |
| Led arch reviews | 3 sessions | 4 sessions | Exceeded |
| Mentored junior | 1 engineer | 1 engineer, shipped feature | Met |
| Tech blog post | 1 post | 1 post, 2K internal views | Met |

### Key Accomplishments
- Led the largest infrastructure change in company history
- Zero customer-facing incidents during migration
- Mentee shipped their first production feature independently

### Areas for Growth
- Delegation: Took on too much myself instead of distributing work
- Communication: Could improve status updates to stakeholders
- Timeline estimation: KR2 was late due to underestimating DevOps dependency

### Career Aspirations
- Targeting Staff Engineer within 12 months
- Want to own architecture decisions for payments domain
- Interested in presenting at external conferences
```

### Manager Assessment

Manager writes independent assessment, then shares with employee:

```markdown
## Manager Assessment: [Employee Name]

### Performance Rating: Exceeds Expectations

### Strengths
- Technical execution on multi-tenant migration was exceptional
- Growing leadership capabilities (architecture reviews, mentoring)
- Proactive problem-solving when blocked

### Development Areas
- Cross-team communication could be more proactive
- Needs to delegate more as scope increases
- Should build relationships with product team

### Recommended Rating: Exceeds Expectations (4/5)
### Promotion Recommendation: Ready for Staff Engineer discussion in Q1
```

### Peer Feedback (360 Input)

Performance Management Specialist collects structured peer feedback:

```
From: [Peer Name] | Relationship: [Cross-team collaborator]

What does this person do well?
"Jane's architecture designs are thorough and well-communicated.
She proactively identifies risks and proposes mitigations."

What could this person improve?
"Sometimes she moves too fast for the team to follow. More context-sharing
in Slack about why decisions were made would help."

Would you want to work with this person again? Yes / Mostly / No
"Yes, absolutely."
```

## Phase 4: Calibration

### Purpose
Ensure rating consistency across teams and managers. Prevent grade inflation and bias.

### Calibration Session (Coordinator facilitates)

**Participants**: All engineering managers + VP Engineering

**Process**:
1. Each manager presents their team's ratings distribution
2. Group discusses outliers (top and bottom)
3. Compare similar roles across teams for consistency
4. Adjust ratings where evidence supports change
5. Finalize ratings

**Rating Distribution Guidelines:**
| Rating | Description | Target % | Actual % |
|--------|-------------|----------|----------|
| 5 - Exceptional | Top 5%, transformative impact | 5-10% | 8% |
| 4 - Exceeds | Consistently above bar | 20-30% | 25% |
| 3 - Meets | Solid, reliable delivery | 50-60% | 55% |
| 2 - Developing | Gaps identified, support needed | 10-15% | 10% |
| 1 - Below | Significant concerns, PIP likely | 0-5% | 2% |

### Bias Checks (Performance Management Specialist monitors):
- [ ] Gender distribution across ratings is proportional
- [ ] Tenure does not correlate with rating (recent hires not penalized)
- [ ] Recency bias flagged (decisions based on full quarter, not last 2 weeks)
- [ ] No team has >40% "Exceeds" without justification
- [ ] Managers with all 3s challenged to differentiate

## Phase 5: Outcomes

### Exceeds Expectations (Rating 4-5)

**Actions:**
- Merit increase: 5-10% (based on current position in band)
- Equity refresh: Additional grant based on level
- Promotion discussion: If criteria met, promote in next cycle
- Development: Stretch assignment, conference budget, leadership opportunities

**Example — Jane Doe (Rating 4, Exceeds):**
- Merit increase: 7% ($182K → $195K)
- Equity refresh: 3,000 shares
- Promotion: Staff Engineer criteria review scheduled for Q1
- Assignment: Architecture owner for payments domain

### Meets Expectations (Rating 3)

**Actions:**
- Merit increase: 3-5% (standard cost-of-living + performance)
- Development plan: 1-2 growth areas with specific actions
- Continue current trajectory with expanded scope

### Developing (Rating 2)

**Actions:**
- Merit increase: 0-2%
- Formal development plan with 90-day milestones
- Weekly check-ins with manager
- Buddy/mentor assigned for specific skill gaps
- Re-evaluate at 90 days

**Development Plan Template:**
```markdown
## Development Plan: [Employee Name]
Created: [Date] | Review Date: [Date + 90 days]

### Gap Identified
[Specific skill or behavior gap with examples]

### Success Criteria (90 days)
1. [Measurable outcome 1]
2. [Measurable outcome 2]
3. [Measurable outcome 3]

### Support Provided
- Weekly 1:1 with manager (30 min)
- Mentor: [Name] for [skill area]
- Training: [Specific course or resource]

### Check-in Schedule
- Day 30: Progress review
- Day 60: Midpoint assessment
- Day 90: Final evaluation

### Possible Outcomes at Day 90
- Improved to Meets: Continue with normal management
- Some improvement: Extend plan 60 days
- No improvement: Transition to PIP
```

### Below Expectations (Rating 1)

**Actions:**
- No merit increase
- Performance Improvement Plan (PIP) initiated
- 60-day structured plan with weekly milestones
- Clear exit criteria (what "success" looks like)
- HR documentation throughout

**PIP is a last resort, not a first response.** Coordinator ensures:
- [ ] Employee received clear feedback throughout the quarter
- [ ] Development resources were offered
- [ ] Manager documented concerns in real-time (not retroactively)
- [ ] No surprises — employee should not be blindsided by a PIP

## Success Criteria

| Metric | Target | Notes |
|--------|--------|-------|
| On-time completion | >95% of reviews done by deadline | |
| Manager satisfaction | >4/5 with process | Survey managers |
| Employee perception of fairness | >4/5 | Anonymous survey |
| Calibration sessions held | 100% of departments | |
| Bias checks passed | All checks green | |
| Development plans created | 100% for rating 2 | |
| PIPs initiated with proper documentation | 100% | |
| Promotion decisions documented with criteria | 100% | |
