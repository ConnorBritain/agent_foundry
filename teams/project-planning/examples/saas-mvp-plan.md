# Example: Planning an MVP for an AI-Powered Customer Support Tool

## Scenario

A startup is building an AI-powered customer support SaaS product. The MVP must demonstrate core value -- AI-assisted ticket resolution -- to secure Series A funding. The team has 12 weeks, 5 engineers, and needs to go from zero to a working product with paying design partners.

## Project Charter Inputs

- **Vision:** "Build an AI customer support tool that automatically drafts responses to support tickets, learns from agent corrections, and reduces average resolution time by 40%."
- **Framework:** Scrum (2-week sprints)
- **Team:** 5 engineers (2 backend, 1 frontend, 1 ML engineer, 1 full-stack)
- **Duration:** 12 weeks (6 sprints)
- **Tools:** Linear for task management, Google Calendar for scheduling
- **Constraints:** Must have 3 paying design partners by Week 10; demo-ready by Week 8

## Team Execution

### Phase 1: Configuration
- Coordinator sets: Scrum, 2-week sprints, 5 engineers, 12 weeks
- Estimation unit: story points
- Velocity estimate: 35 points/sprint (conservative for new team)
- Total capacity: ~210 story points

### Phase 2: Requirements Analysis
Requirements Analyst identifies 4 workstreams:

| Workstream | Scope | Success Criteria |
|-----------|-------|-----------------|
| WS1: Ticket Ingestion | Email/API integration for importing tickets | Supports 3 ticket sources; <30s ingestion latency |
| WS2: AI Response Engine | LLM-powered draft response generation | 70% of drafts accepted with minor edits; <10s generation time |
| WS3: Agent Dashboard | Web UI for support agents to review and send responses | Agent can review, edit, and send AI draft in <2 minutes |
| WS4: Learning Loop | Feedback mechanism to improve AI responses from corrections | Model quality improves measurably after 100 corrections |

**Out of scope:** Multi-language support, voice/phone integration, custom model training, analytics dashboard.

### Phase 3: Task Decomposition
Task Decomposer creates 42 tasks across 4 workstreams:

| Workstream | Tasks | Total Points | Key Dependencies |
|-----------|-------|-------------|-----------------|
| WS1: Ticket Ingestion | 10 | 45 | None (can start immediately) |
| WS2: AI Response Engine | 12 | 65 | WS1 (needs tickets to process) |
| WS3: Agent Dashboard | 11 | 50 | WS2 (needs AI responses to display) |
| WS4: Learning Loop | 9 | 40 | WS2 + WS3 (needs agent corrections) |
| **Total** | **42** | **200** | |

Sample tasks from WS2:
- WS2-001: Set up LLM integration with prompt management (8 pts)
- WS2-002: Build ticket context extraction pipeline (5 pts)
- WS2-003: Implement response generation with template support (8 pts)
- WS2-004: Add response confidence scoring (5 pts)
- WS2-005: Build A/B testing framework for prompt variants (3 pts)

### Phase 4: Risk Assessment and Resource Allocation

**Top 5 Risks:**

| Risk | P | I | Score | Mitigation |
|------|---|---|-------|-----------|
| LLM response quality insufficient for demo | 3 | 5 | 15 | Build prompt engineering toolkit early; have 3 prompt variants ready |
| Design partner onboarding takes longer than expected | 4 | 4 | 16 | Start partner outreach in Week 1; have onboarding guide by Week 4 |
| ML engineer is single point of failure for WS2 + WS4 | 4 | 4 | 16 | Full-stack engineer pairs on ML tasks from Sprint 2 |
| Email integration complexity varies across providers | 3 | 3 | 9 | Start with Gmail API only; add others post-MVP |
| Data privacy requirements from design partners | 3 | 3 | 9 | Build tenant isolation from Day 1; prepare DPA template |

**Resource Allocation:**

| Engineer | Primary Workstream | Sprint Assignments |
|----------|-------------------|-------------------|
| Backend 1 | WS1: Ticket Ingestion | Sprints 1-3 WS1, Sprints 4-6 WS2 support |
| Backend 2 | WS2: AI Response Engine | Sprints 1-6 WS2 |
| Frontend | WS3: Agent Dashboard | Sprints 1-2 design, Sprints 3-6 WS3 |
| ML Engineer | WS2 + WS4 | Sprints 1-4 WS2, Sprints 5-6 WS4 |
| Full-stack | WS1 + WS3 | Sprints 1-2 WS1, Sprints 3-4 WS3, Sprints 5-6 integration |

### Phase 5: Sprint Schedule

| Sprint | Dates | Focus | Milestone |
|--------|-------|-------|-----------|
| Sprint 1 | Weeks 1-2 | Ticket ingestion foundation, LLM integration setup | Dev environment ready |
| Sprint 2 | Weeks 3-4 | Email import working, first AI responses generating | Internal demo: AI responds to test tickets |
| Sprint 3 | Weeks 5-6 | Agent dashboard v1, response quality tuning | Agent dashboard usable end-to-end |
| Sprint 4 | Weeks 7-8 | Integration testing, design partner onboarding prep | **Demo-ready (hard deadline)** |
| Sprint 5 | Weeks 9-10 | Design partner onboarding, feedback loop v1 | **3 design partners live (hard deadline)** |
| Sprint 6 | Weeks 11-12 | Learning loop, bug fixes, metrics collection | MVP complete; Series A prep data |

**Buffer:** Sprint 6 includes 1 week of buffer for carryover work.

### Phase 6: Integration and Documentation

Integration Planner exports to Linear:
- 1 project: "AI Support Tool MVP"
- 4 workstream labels
- 42 issues with story points, acceptance criteria, and dependencies
- 6 sprints with capacity targets
- 5 milestones linked to sprint boundaries

## Deliverables

```
project-plan/
├── requirements.md              # 4 workstreams with success criteria
├── task-list.md                 # 42 tasks with estimates and acceptance criteria
├── wbs.md                       # Work Breakdown Structure
├── dependency-graph.md          # Mermaid diagram with critical path
├── risk-register.md             # 12 risks, top 5 with full mitigation plans
├── resource-allocation.md       # Engineer x sprint assignments
├── sprint-schedule.md           # 6 sprints with milestones
├── stakeholder-comms-plan.md    # Weekly investor updates, daily standups
├── executive-summary.md         # 1-page overview for investors
└── project-readme.md            # Goals, scope, timeline, conventions
```

## Cost Estimate

| Phase | Tokens | Cost |
|-------|--------|------|
| Configuration | ~12K | ~$0.72 |
| Requirements Analysis | ~40K | ~$2.40 |
| Task Decomposition | ~55K | ~$3.30 |
| Risk + Resource | ~95K | ~$10.80 |
| Scheduling | ~35K | ~$2.10 |
| Integration | ~25K | ~$0.63 |
| **Total** | **~262K** | **~$19.95** |

## Key Planning Decisions

1. **Gmail-only for MVP.** Reduces WS1 complexity by 40%. Other email providers are post-MVP.
2. **ML engineer pairs with full-stack.** Eliminates single-point-of-failure risk on the AI engine.
3. **Demo-ready by Week 8, not Week 12.** Forces prioritization of core flow over nice-to-haves.
4. **Tenant isolation from Day 1.** More expensive upfront but avoids rearchitecting for design partners.
5. **Sprint 6 as buffer sprint.** Protects the Week 10 partner deadline with overflow capacity.
