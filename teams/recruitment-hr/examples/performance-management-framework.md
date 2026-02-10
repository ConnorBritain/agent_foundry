# Example: Performance Management Framework — 50-Person Company

## Project Overview

"BuildRight" is a 50-person construction tech startup transitioning from informal ("the founders know everyone") to structured performance management. They need OKRs, career ladders, review processes, and compensation bands — without becoming bureaucratic.

## Configuration

```yaml
company_stage: series_b
current_headcount: 50
target_headcount: 75  # Growing, but perf system needed now
culture:
  values: [build_together, straight_talk, move_fast, get_better]
  work_model: hybrid
  meeting_culture: balanced
tools:
  engagement: lattice
  hris: rippling
```

## Phase 1: Foundation

### Coordinator/Head of People assesses current state:

**Diagnosis:**
- No written expectations for any role
- Promotions happen ad-hoc ("founders feel someone is ready")
- Compensation is inconsistent (early employees underpaid vs market, recent hires above)
- Feedback is informal and inconsistent across managers
- Top performers feel unrecognized; underperformers aren't addressed
- Managers have never been trained on people management

**Design Principles:**
1. Light process, high impact — no 20-page review forms
2. Continuous feedback > annual review
3. Transparent criteria — everyone knows what "great" looks like
4. Manager enablement — train managers before launching

### Performance Management designs the system:

**Goal-Setting Framework: OKRs (Quarterly)**

Company OKRs → Department OKRs → Team OKRs → Individual OKRs

Rules:
- 1 Objective per person with 3-4 Key Results
- Key Results are measurable (number, date, yes/no)
- 70% achievement is the target (if you hit 100%, goals weren't ambitious enough)
- Growth goals are separate from delivery goals (both required)

**Example cascade:**
```
Company: "Become the #1 construction project management tool"
  └─ Engineering: "Ship the mobile app to 1,000 beta users"
      └─ Mobile Team: "Deliver core feature set with <2s load time"
          └─ Senior Dev: "Implement offline sync for field workers"
              KR1: Offline mode works for 5 core actions (by W4)
              KR2: Data sync resolves conflicts correctly (by W6)
              KR3: Field test with 10 real users, satisfaction >8/10 (by W8)
```

## Phase 2: Career Ladders

### Performance Management creates ladders for each function:

**Engineering Ladder:**

| Level | Title | Scope | Autonomy | Impact | Comp Band |
|-------|-------|-------|----------|--------|-----------|
| IC1 | Junior Engineer | Tasks within a feature | Guided | Individual | $90-120K |
| IC2 | Engineer | Features end-to-end | Moderate | Team feature | $120-155K |
| IC3 | Senior Engineer | System-level projects | High | Team outcomes | $155-190K |
| IC4 | Staff Engineer | Cross-team architecture | Self-directed | Org outcomes | $190-230K |
| IC5 | Principal Engineer | Company-wide technical strategy | Autonomous | Company outcomes | $230-280K |
| M1 | Engineering Manager | 4-8 direct reports | High | Team health + delivery | $170-210K |
| M2 | Director of Engineering | 2-4 teams | Self-directed | Department outcomes | $210-260K |

**Each level includes behavioral indicators:**

Example — Senior Engineer (IC3):
- **Technical**: Designs systems that others can build on. Makes pragmatic trade-offs.
- **Execution**: Breaks down ambiguous problems. Delivers consistently.
- **Communication**: Writes clear design docs. Explains complex topics simply.
- **Leadership**: Mentors IC1-IC2s. Improves team practices.
- **Business**: Understands user needs. Makes product-aware technical decisions.

### Compensation & Benefits aligns bands:

**Process:**
1. Benchmark every role against market data (Pave, Levels.fyi, Glassdoor)
2. Set bands at 25th-75th percentile with target at 50th (moving to 65th post-Series B)
3. Map every current employee to their level and band
4. Identify outliers: 8 employees below band (underpaid), 3 above band (overpaid)
5. Create correction plan: Bring underpaid employees to band minimum over 2 cycles

**Equity framework:**
| Level | Initial Grant | Refresh (annual) | Vesting |
|-------|--------------|-------------------|---------|
| IC1 | 0.02% | 0.005% | 4yr/1yr cliff |
| IC2 | 0.05% | 0.01% | 4yr/1yr cliff |
| IC3 | 0.10% | 0.025% | 4yr/1yr cliff |
| IC4 | 0.20% | 0.05% | 4yr/1yr cliff |
| M1 | 0.15% | 0.04% | 4yr/1yr cliff |
| M2 | 0.30% | 0.08% | 4yr/1yr cliff |

## Phase 3: Review Process

### Performance Management designs a lightweight quarterly review:

**Cycle (runs in last 2 weeks of quarter):**
1. **Week 1, Mon-Wed**: Self-assessment (30 min)
2. **Week 1, Thu-Fri**: Peer feedback collected (15 min per peer, 2-3 peers)
3. **Week 2, Mon-Wed**: Manager writes assessment
4. **Week 2, Thu**: Calibration session (managers + Head of People)
5. **Week 2, Fri**: Manager delivers feedback in 1:1

**Self-Assessment Template (kept deliberately short):**
```markdown
1. OKR Results (copy from OKR tracker with brief commentary)
2. What am I most proud of this quarter? (2-3 sentences)
3. Where did I fall short? (2-3 sentences)
4. What do I want to focus on next quarter? (2-3 sentences)
```

**Manager Assessment Template:**
```markdown
1. OKR achievement summary
2. Rating: Exceptional / Exceeds / Meets / Developing / Below
3. Top 2 strengths (with specific examples)
4. Top 1-2 growth areas (with specific examples)
5. Recommendation: Promotion / On track / Development plan needed
```

**Calibration ensures:**
- Consistent standards across teams
- High performers identified and rewarded
- Underperformance addressed (not hidden)
- No surprises — if someone is "Developing", they should already know

## Phase 4: Manager Training

### Onboarding & Enablement creates manager enablement program:

**Module 1: Setting Goals (60 min workshop)**
- How to write good OKRs (examples + anti-examples)
- Cascading from company → team → individual
- Exercise: Write OKRs for their team and get peer feedback

**Module 2: Giving Feedback (60 min workshop)**
- SBI framework: Situation → Behavior → Impact
- Practice: Role-play delivering positive, constructive, and difficult feedback
- Common mistakes: "You always...", vague praise, feedback sandwiches

**Module 3: Running 1:1s (45 min workshop)**
- Template: Career development, blockers, feedback, personal check-in
- Cadence: Weekly 30-min minimum, never cancel two in a row
- The 90/10 rule: Report talks 90% of the time

**Module 4: Conducting Reviews (45 min workshop)**
- Walk through the review template
- How to calibrate (what each rating means with examples)
- How to deliver tough messages with respect
- Legal awareness: Document performance issues in real-time

## Key Artifacts Produced

1. **OKR Framework** with templates, examples, and scoring guide
2. **Career Ladders** for Engineering, Product, Sales, Operations (4 ladders, 5-7 levels each)
3. **Compensation Bands** with market data and equity guidelines
4. **Review Process** with all templates and timeline
5. **Manager Training Program** (4 modules, slides + exercises)
6. **1:1 Template** for weekly manager-report conversations
7. **Promotion Criteria** document with clear requirements per level

## Results (After 2 Cycles / 6 Months)

| Metric | Before | After |
|--------|--------|-------|
| Employees who know their level | 20% | 100% |
| Employees with written goals | 15% | 95% |
| Managers trained on feedback | 0% | 100% |
| On-time review completion | N/A | 92% |
| Employee fairness perception | 5.2/10 | 7.8/10 |
| Voluntary attrition | 18% annual | 11% annual |
| Promotion decisions with documented criteria | 0% | 100% |
| Comp outliers (outside band) | 22% | 4% |

## Cost: ~$85
