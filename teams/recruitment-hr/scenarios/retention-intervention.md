# Scenario: Retention Intervention

## Overview

The system detects flight risk signals for a high-performing employee and orchestrates a multi-agent intervention to retain them.

## Phase 1: Detection

### Flight Risk Signals Monitored by Culture & Engagement Specialist

| Signal | Threshold | Jane's Data |
|--------|-----------|-------------|
| 1:1 frequency | Declining over 4 weeks | Canceled 2 of last 4 |
| Slack activity | 30%+ decrease | Down 40% from baseline |
| Engagement survey (eNPS) | Score < 7 | Scored 5 (was 9 six months ago) |
| Goal updates | None in 30+ days | Last update 45 days ago |
| Opportunity participation | Declined 2+ | Declined tech lead role on new project |
| Meeting participation | Passive in 3+ meetings | Camera off, minimal input lately |

### Alert Generated
```
FLIGHT RISK ALERT
Employee: Jane Doe, Senior Engineer
Risk Score: 75% (High)
Tenure: 2.5 years
Performance: Top 15% (last 3 reviews)
Trigger: Combination of declining engagement + declined opportunity
```

## Phase 2: Investigation (Week 1)

### Coordinator/Head of People reviews Jane's profile:

**Performance History**:
- Consistent "Exceeds Expectations" ratings
- Led successful migration to microservices (6 months ago)
- Mentors 2 junior engineers
- No performance concerns

**Compensation Analysis** (Compensation & Benefits):
- Current salary: $165,000 (50th percentile for role/level/location)
- Market rate: $180,000 (75th percentile)
- Last raise: 12 months ago (3% cost-of-living)
- Equity: Initial grant, no refresh

**Engagement Data** (Culture & Engagement):
- Recent survey comments: "Feeling stuck", "Want more leadership"
- Skip-level meeting notes: "Interested in architecture decisions"
- Peer feedback: "Jane seems disengaged lately"

**Career Goals** (Performance Management):
- Expressed interest in Staff Engineer track
- Wants to own architecture decisions, not just implement
- Previous 1:1 notes mention desire for conference speaking

## Phase 3: Intervention Plan (Week 1)

Coordinator assembles cross-agent response:

### Performance Management Specialist recommends:
- Assign Jane as tech lead on upcoming payments platform rebuild
- Create clear Staff Engineer promotion criteria (6-month timeline)
- Pair with VP Engineering for monthly architecture mentorship
- Sponsor conference talk submission (QCon, StrangeLoop)

### Compensation & Benefits Analyst recommends:
- Market adjustment: $165K → $182K (75th percentile)
- Equity refresh: 5,000 shares vesting over 4 years
- Total comp increase: ~15%
- Budget impact: Justified by replacement cost ($50K+ recruiting + 6 months ramp)

### Culture & Engagement Specialist recommends:
- Manager conducts stay interview (structured, not ad-hoc)
- Increase 1:1 cadence to weekly for next 2 months
- Include Jane in architecture review committee
- Recognize her mentorship contributions publicly

### Onboarding & Enablement Manager recommends:
- Enroll in leadership development program
- Budget for external coaching ($5K/year)

## Phase 4: Execution (Weeks 2-4)

### Stay Interview (Manager, guided by Culture & Engagement)

**Questions asked:**
1. "What gets you most excited about coming to work?"
   - Jane: "Solving hard problems, but I haven't had one in months"
2. "What would make you consider leaving?"
   - Jane: "Lack of growth. I feel like I'm doing the same thing I did a year ago"
3. "If you could change one thing about your role, what would it be?"
   - Jane: "More ownership over architecture. I want to design systems, not just build features"
4. "What would it take for you to be excited about the next 2 years here?"
   - Jane: "A clear path to Staff Engineer with real scope increase"

### Actions Taken
1. **Week 2**: Manager presents retention package
   - Payments platform tech lead role (starts immediately)
   - Salary adjustment to $182K (effective next pay cycle)
   - Equity refresh grant
   - Staff Engineer promotion criteria document (co-authored with Jane)
2. **Week 3**: VP Engineering mentorship begins
   - Monthly 1:1 focused on architecture thinking
   - Added to architecture review committee
3. **Week 4**: Conference talk submitted
   - Jane submits talk proposal to QCon on microservices migration
   - Company sponsors travel and registration

### Jane's Response
- Accepts retention package with enthusiasm
- Re-engages in team meetings immediately
- Starts payments platform design document within first week
- eNPS self-reported: "I feel heard and valued"

## Phase 5: Follow-Up (Months 2-6)

### Monthly Check-ins (Culture & Engagement)
| Month | eNPS | Slack Activity | 1:1 Quality | Notes |
|-------|------|---------------|-------------|-------|
| Month 1 | 7 | +20% | Engaged | Settling into new role |
| Month 2 | 8 | +35% | Highly engaged | Leading design reviews |
| Month 3 | 9 | +50% | Driving agenda | QCon talk accepted |
| Month 6 | 9 | Baseline+40% | Self-directed | Staff Engineer promotion discussion |

### Performance Management tracks:
- Payments platform: On track, Jane leading architecture decisions
- Mentoring: Expanded to 3 junior engineers
- Conference: Talk delivered to positive reception
- Promotion: Meets 5/6 Staff Engineer criteria at month 5

### Coordinator ensures commitments are kept:
- [ ] Salary adjustment processed (Week 2) - DONE
- [ ] Equity refresh granted (Week 3) - DONE
- [ ] VP mentorship cadence maintained (Monthly) - ON TRACK
- [ ] Promotion review scheduled (Month 6) - SCHEDULED

## Success Criteria

| Metric | Target | Actual |
|--------|--------|--------|
| Employee retained | Yes | Yes |
| Engagement score recovery | eNPS > 8 | eNPS = 9 |
| Time to intervention | < 2 weeks from alert | 5 days |
| Commitment delivery | 100% of promises kept | 100% |
| Promotion timeline | < 12 months | 7 months |
| Manager capability growth | Improved retention skills | Stay interview conducted |
| Cost of retention | < replacement cost ($50K+) | ~$22K (raise + equity) |
| ROI | Positive | 2.3x (retained top performer at 44% of replacement cost) |

## Lessons Learned

1. **Early detection works**: Flight risk score flagged Jane 6-8 weeks before she would have started interviewing
2. **Compensation alone isn't enough**: The salary increase mattered, but scope and growth mattered more
3. **Stay interviews > exit interviews**: Catching disengagement early allows intervention; exit interviews are too late
4. **Follow-through is critical**: Broken promises accelerate departure — every commitment must be tracked and delivered
