# Example: Planning Migration from Monolith to Microservices

## Scenario

A mid-stage startup is migrating its core product from a Django monolith to a microservices architecture. The monolith serves 50K daily active users and handles payments, user management, notifications, and the core product logic. The migration must happen without downtime and while the team continues shipping features.

## Project Charter Inputs

- **Vision:** "Migrate our Django monolith to microservices over 16 weeks. Extract payments, notifications, and user management into independent services. Maintain zero downtime and continue feature development during migration."
- **Framework:** Scrum (2-week sprints)
- **Team:** 8 engineers (3 backend, 2 full-stack, 1 DevOps, 1 frontend, 1 QA)
- **Duration:** 16 weeks (8 sprints)
- **Tools:** Jira for task management, Google Calendar for scheduling
- **Constraints:** Zero downtime; must maintain feature velocity at 60% of normal; payments migration requires PCI compliance review

## Team Execution

### Phase 1: Configuration
- Coordinator sets: Scrum, 2-week sprints, 8 engineers, 16 weeks
- Estimation unit: story points
- Velocity estimate: 55 points/sprint (reduced from normal 70 due to migration overhead)
- Total capacity: ~440 story points

### Phase 2: Requirements Analysis
Requirements Analyst identifies 5 workstreams:

| Workstream | Scope | Success Criteria |
|-----------|-------|-----------------|
| WS1: Service Infrastructure | API gateway, service mesh, CI/CD per service, observability | All services deploy independently; <5min deploy time per service |
| WS2: User Management Service | Extract auth, profiles, permissions from monolith | Service handles 100% of auth traffic; <100ms p99 latency |
| WS3: Payments Service | Extract billing, subscriptions, invoicing | PCI compliant; processes payments with <500ms latency; zero failed transactions during cutover |
| WS4: Notifications Service | Extract email, push, in-app notifications | Delivers notifications within 30s; supports 10K msgs/min |
| WS5: Strangler Pattern Orchestration | Route traffic incrementally from monolith to services | Gradual cutover with rollback capability per service |

**Out of scope:** Core product logic migration (stays in monolith for now), database sharding, new feature development within extracted services.

### Phase 3: Task Decomposition
Task Decomposer creates 58 tasks across 5 workstreams:

| Workstream | Tasks | Total Points | Dependencies |
|-----------|-------|-------------|-------------|
| WS1: Service Infrastructure | 12 | 75 | None (start immediately) |
| WS2: User Management Service | 13 | 95 | WS1 (needs infra) |
| WS3: Payments Service | 14 | 110 | WS1 (needs infra), WS2 (needs auth) |
| WS4: Notifications Service | 10 | 65 | WS1 (needs infra) |
| WS5: Strangler Pattern | 9 | 60 | WS2, WS3, WS4 (needs services ready) |
| **Total** | **58** | **405** | |

Sample tasks from WS3 (Payments):
- WS3-001: Design payments service API contract (5 pts)
- WS3-002: Set up payments service repo with CI/CD (3 pts)
- WS3-003: Implement Stripe integration in new service (8 pts)
- WS3-004: Build subscription lifecycle management (8 pts)
- WS3-005: Implement invoice generation (5 pts)
- WS3-006: Create data migration scripts for billing history (8 pts)
- WS3-007: PCI compliance review and remediation (13 pts)
- WS3-008: Build parallel-run validation (comparing monolith vs service output) (8 pts)
- WS3-009: Load test payments service at 2x current traffic (5 pts)
- WS3-010: Implement circuit breaker and fallback to monolith (5 pts)

### Phase 4: Risk Assessment and Resource Allocation

**Top 5 Risks:**

| Risk | P | I | Score | Mitigation |
|------|---|---|-------|-----------|
| Data inconsistency during parallel run (monolith + service) | 4 | 5 | 20 | Event sourcing for state sync; automated consistency checker runs every 5 min |
| PCI compliance review delays payments migration | 3 | 5 | 15 | Start PCI review in Sprint 1; engage compliance consultant early |
| Service-to-service latency exceeds budget under load | 3 | 4 | 12 | Load test each service at 2x traffic before cutover; circuit breakers on all calls |
| Team context-switching between feature work and migration | 4 | 3 | 12 | Dedicate 3 backend engineers to migration full-time; other 5 handle features |
| Monolith database schema changes during migration break service assumptions | 3 | 4 | 12 | Freeze monolith schema for extracted domains; use database views as contracts |

**Resource Allocation:**

| Engineer | Primary Focus | Sprint Assignments |
|----------|-------------|-------------------|
| Backend 1 | WS1 + WS2: Infra and User Management | Sprints 1-2 infra, Sprints 3-5 user service, Sprints 6-8 cutover |
| Backend 2 | WS3: Payments Service | Sprints 1-8 payments (full time, critical path) |
| Backend 3 | WS4 + WS5: Notifications and Strangler | Sprints 1-2 infra, Sprints 3-5 notifications, Sprints 6-8 strangler |
| Full-stack 1 | Feature development + WS2 support | 60% features, 40% migration support |
| Full-stack 2 | Feature development + WS4 support | 60% features, 40% migration support |
| DevOps | WS1: Infrastructure | Sprints 1-3 infra, Sprints 4-8 deployment pipelines and observability |
| Frontend | Feature development + API migration | Sprints 1-6 features, Sprints 7-8 API endpoint migration |
| QA | Integration testing across all workstreams | Sprints 1-2 test strategy, Sprints 3-8 continuous testing |

### Phase 5: Sprint Schedule

| Sprint | Dates | Focus | Milestone |
|--------|-------|-------|-----------|
| Sprint 1 | Weeks 1-2 | API gateway, service mesh, CI/CD pipeline templates | Infrastructure foundation ready |
| Sprint 2 | Weeks 3-4 | Observability stack, user service API design, PCI review start | Service template validated end-to-end |
| Sprint 3 | Weeks 5-6 | User management service v1, payments service starts | User service in parallel-run mode |
| Sprint 4 | Weeks 7-8 | User service cutover, notifications service v1, payments continued | **User management migrated** |
| Sprint 5 | Weeks 9-10 | Notifications cutover, payments service v1 complete | **Notifications migrated** |
| Sprint 6 | Weeks 11-12 | Payments parallel run, load testing, PCI compliance sign-off | Payments validated in parallel mode |
| Sprint 7 | Weeks 13-14 | Payments cutover, strangler pattern finalization | **Payments migrated** |
| Sprint 8 | Weeks 15-16 | Monolith cleanup, monitoring hardening, documentation | **Migration complete** |

**Critical Path:** WS1 infra (Sprints 1-2) -> WS3 payments (Sprints 3-7) -> WS5 strangler (Sprint 7-8)

**Buffer:** 1.5 weeks of buffer distributed across Sprints 6-8 for the payments critical path.

### Phase 6: Integration and Documentation

Integration Planner produces:
- Jira project with 58 issues across 5 epics
- Sprint assignments matching the schedule above
- Dependency links between all workstream handoffs
- Migration runbook for each service cutover
- Rollback procedures per service
- Cross-team dependency register (PCI consultant, DevOps on-call)
- Stakeholder communication plan (weekly engineering sync, biweekly leadership update)

## Deliverables

```
migration-plan/
├── requirements.md              # 5 workstreams with success criteria
├── task-list.md                 # 58 tasks with estimates and acceptance criteria
├── wbs.md                       # Work Breakdown Structure
├── dependency-graph.md          # Mermaid diagram with critical path through payments
├── risk-register.md             # 15 risks, top 5 with full mitigation plans
├── resource-allocation.md       # Engineer assignments across 8 sprints
├── sprint-schedule.md           # 8 sprints with milestones and cutover dates
├── migration-runbooks/
│   ├── user-management-cutover.md
│   ├── payments-cutover.md
│   └── notifications-cutover.md
├── rollback-procedures.md       # Per-service rollback steps
├── stakeholder-comms-plan.md    # Weekly eng sync, biweekly leadership
└── executive-summary.md         # 1-page overview for leadership
```

## Cost Estimate

| Phase | Tokens | Cost |
|-------|--------|------|
| Configuration | ~15K | ~$0.90 |
| Requirements Analysis | ~45K | ~$2.70 |
| Task Decomposition | ~65K | ~$3.90 |
| Risk + Resource | ~100K | ~$11.40 |
| Scheduling | ~45K | ~$2.70 |
| Integration | ~35K | ~$0.88 |
| **Total** | **~305K** | **~$22.48** |

Note: This is a high-complexity scenario (1.5x multiplier) due to cross-workstream dependencies and the payments critical path. Budget $27 including retry buffer.

## Key Planning Decisions

1. **Strangler Fig pattern, not big-bang rewrite.** Each service is extracted and cuts over independently, reducing blast radius per migration step.
2. **Payments engineer is full-time dedicated.** The payments critical path cannot afford context-switching. One backend engineer works exclusively on WS3 for all 8 sprints.
3. **Feature velocity reduced to 60%, not paused.** Complete feature freeze would risk losing customers; 60% velocity keeps the product moving while freeing capacity for migration.
4. **PCI review starts Sprint 1.** Compliance reviews are slow and cannot be parallelized. Starting early prevents it from blocking the payments cutover in Sprint 7.
5. **Parallel-run validation before every cutover.** Each service runs alongside the monolith with automated output comparison before traffic is switched. This catches discrepancies before users are affected.
6. **Schema freeze for extracted domains.** The monolith database schema for users, payments, and notifications is frozen during migration. New features in those areas use the new service APIs.
