# Example: Planning Team Scaling from 5 to 25 People Over 6 Months

## Scenario

A growing startup needs to scale its engineering team from 5 to 25 people over 6 months. This is not just a hiring plan -- it requires restructuring into squads, defining ownership boundaries, onboarding workflows, and maintaining delivery velocity during growth. The project planning team treats this as a multi-workstream project.

## Project Charter Inputs

- **Vision:** "Scale the engineering team from 5 to 25 people in 6 months while maintaining delivery velocity and code quality. Restructure from a single team into 4 squads with clear ownership."
- **Framework:** Kanban (continuous flow; hiring and onboarding do not fit sprint boundaries)
- **Team:** Current 5 engineers + hiring manager + VP Engineering
- **Duration:** 26 weeks
- **Tools:** Linear for task tracking, Google Calendar for interview scheduling and onboarding
- **Constraints:** Must not drop below 80% of current velocity during scaling; budget for 20 new hires

## Team Execution

### Phase 1: Configuration
- Coordinator sets: Kanban, 26-week duration, continuous flow
- Service classes: Expedite (critical hires), Standard (planned hires), Fixed Date (onboarding cohorts)
- WIP limits: 5 concurrent hiring pipelines, 3 concurrent onboarders

### Phase 2: Requirements Analysis
Requirements Analyst identifies 5 workstreams:

| Workstream | Scope | Success Criteria |
|-----------|-------|-----------------|
| WS1: Hiring Pipeline | Source, interview, close 20 engineers | 20 offers accepted; <45 day avg time-to-hire |
| WS2: Squad Formation | Define 4 squads with ownership areas | All code modules have a single owning squad |
| WS3: Onboarding Program | Structured onboarding for new hires | New hires ship first PR within 2 weeks |
| WS4: Knowledge Transfer | Document systems, transfer ownership | All critical systems have 2+ knowledgeable engineers |
| WS5: Process Scaling | Adapt engineering processes for 25 people | CI/CD, code review, and deployment processes support 4 squads |

**Out of scope:** Office space planning, HR systems, compensation benchmarking.

### Phase 3: Task Decomposition
Task Decomposer creates 38 tasks across 5 workstreams:

| Workstream | Tasks | Key Deliverables |
|-----------|-------|-----------------|
| WS1: Hiring Pipeline | 10 | Job descriptions, interview rubrics, sourcing channels, offer templates |
| WS2: Squad Formation | 7 | Squad charters, ownership map, team topology diagram |
| WS3: Onboarding Program | 8 | Onboarding checklist, buddy system, 30/60/90 day plans |
| WS4: Knowledge Transfer | 7 | System documentation, architecture decision records, runbooks |
| WS5: Process Scaling | 6 | CI/CD multi-team setup, code review guidelines, deployment runbooks |
| **Total** | **38** | |

### Phase 4: Risk Assessment and Resource Allocation

**Top 5 Risks:**

| Risk | P | I | Score | Mitigation |
|------|---|---|-------|-----------|
| Hiring market is competitive; cannot fill 20 roles in 6 months | 4 | 5 | 20 | Start 3 sourcing channels simultaneously; offer referral bonuses; engage 2 agencies |
| Current team velocity drops >20% due to interview load | 4 | 4 | 16 | Cap interview time at 5 hrs/week per engineer; rotate interviewers |
| New hires leave within 3 months (early attrition) | 3 | 4 | 12 | Structured onboarding, buddy system, 30-day check-ins |
| Squad boundaries create silos and ownership gaps | 3 | 4 | 12 | Define explicit shared ownership areas; cross-squad retros monthly |
| Knowledge transfer incomplete before team restructure | 3 | 4 | 12 | Start documentation in Month 1; pair programming for critical systems |

**Phased Hiring Plan:**

| Month | Hires | Cumulative Team Size | Focus |
|-------|-------|---------------------|-------|
| Month 1 | 3 | 8 | Senior hires to anchor squads; start documentation |
| Month 2 | 4 | 12 | Mid-level hires; form first 2 squads |
| Month 3 | 5 | 17 | Fill remaining senior gaps; form squads 3 and 4 |
| Month 4 | 4 | 21 | Mid-level and junior hires; all squads operational |
| Month 5 | 3 | 24 | Backfill and specialists |
| Month 6 | 1 | 25 | Final hire; focus on stabilization |

### Phase 5: Timeline and Milestones

| Week | Milestone | Description |
|------|-----------|-------------|
| Week 2 | Hiring infrastructure ready | Job posts live, interview rubrics complete, sourcing active |
| Week 4 | First 3 hires start | Senior engineers who will lead squads |
| Week 6 | Squad charters drafted | Ownership boundaries defined for 4 squads |
| Week 8 | Squads 1 and 2 operational | First two squads running independently |
| Week 10 | Onboarding v2 launched | Refined onboarding based on first cohort feedback |
| Week 13 | Mid-point review | 12+ hires onboarded; velocity assessment |
| Week 16 | All 4 squads operational | Full team topology in place |
| Week 20 | Knowledge transfer complete | All critical systems have 2+ knowledgeable engineers |
| Week 24 | Process scaling complete | CI/CD, code review, and deployment support 4 squads |
| Week 26 | Scaling complete | 25 engineers, 4 squads, stable velocity |

### Phase 6: Integration and Documentation

Integration Planner exports:
- 38 tasks to Linear with Kanban board
- Service class labels (expedite, standard, fixed date)
- Milestone events to Google Calendar
- Hiring pipeline tracking board
- Onboarding cohort schedule

## Deliverables

```
scaling-plan/
├── requirements.md              # 5 workstreams with success criteria
├── task-list.md                 # 38 tasks with owners and acceptance criteria
├── hiring-plan.md               # Month-by-month hiring targets and channels
├── squad-charters.md            # 4 squad charters with ownership maps
├── onboarding-program.md        # Onboarding checklist, buddy system, 30/60/90 plans
├── knowledge-transfer-plan.md   # System documentation schedule and pair assignments
├── risk-register.md             # 10 risks with mitigations
├── timeline.md                  # 26-week timeline with milestones
├── stakeholder-comms-plan.md    # Weekly VP update, monthly board update
└── executive-summary.md         # 1-page overview for leadership
```

## Cost Estimate

| Phase | Tokens | Cost |
|-------|--------|------|
| Configuration | ~12K | ~$0.72 |
| Requirements Analysis | ~40K | ~$2.40 |
| Task Decomposition | ~50K | ~$3.00 |
| Risk + Resource | ~95K | ~$10.80 |
| Scheduling | ~40K | ~$2.40 |
| Integration | ~25K | ~$0.63 |
| **Total** | **~262K** | **~$19.95** |

## Key Planning Decisions

1. **Kanban over Scrum.** Hiring and onboarding are continuous processes that do not fit 2-week sprints. Kanban's flow-based model with WIP limits is a better fit.
2. **Senior hires first.** Anchoring each squad with a senior engineer before adding junior members reduces onboarding load and establishes squad culture.
3. **Cap interview load at 5 hrs/week.** Prevents current team velocity from cratering during the hiring push.
4. **Onboarding in cohorts.** Grouping new hires into biweekly cohorts creates peer support and makes onboarding logistics manageable.
5. **Documentation before restructure.** Starting knowledge transfer in Month 1 ensures critical knowledge is captured before the original team disperses into squads.
