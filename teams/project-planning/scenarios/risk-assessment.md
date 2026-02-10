# Scenario: Comprehensive Risk Assessment for a Product Launch

## Context

A product team is 4 weeks from launching a new product to production. The launch involves new infrastructure, third-party integrations, data migration, and public-facing changes. A comprehensive risk assessment is needed to identify what could go wrong, quantify the impact, and create mitigation and contingency plans for the top risks.

## Trigger

The user requests a risk assessment for an upcoming launch. Example:

> "We're launching our new real-time collaboration feature in 4 weeks. It involves: WebSocket infrastructure, a new Redis cluster, integration with our notification service, and a database migration for the collaboration data model. 200K active users will be affected. Do a full risk assessment."

## Team Configuration

| Agent | Role in This Scenario | Active |
|-------|----------------------|--------|
| Coordinator | Frame the risk assessment scope, validate completeness | Yes |
| Requirements Analyst | Document launch requirements and success criteria | Yes |
| Task Decomposer | Break remaining work into tasks to assess completeness | Yes |
| Scheduler | Validate schedule feasibility given identified risks | Yes |
| Resource Allocator | Assess resource risks and capacity for contingency work | Yes (Opus) |
| Risk Assessor | Primary agent: full risk identification, scoring, and mitigation planning | Yes |
| Integration Planner | Document risk register, create monitoring plan, export action items | Yes |

## Workflow

### Phase 1: Risk Scope Configuration (~3 min)
- Coordinator frames the assessment: product launch, 4-week horizon, 200K affected users
- Identifies risk categories to assess: technical, operational, external, schedule, business

### Phase 2: Launch Requirements Review (~10 min)
- Requirements Analyst documents what "successful launch" means:
  - WebSocket connections handle 50K concurrent users
  - Redis cluster supports <10ms read latency
  - Notification delivery within 5 seconds
  - Zero data loss during migration
  - Rollback possible within 30 minutes
- Identifies critical success metrics and failure thresholds

### Phase 3: Completeness Assessment (~15 min)
- Task Decomposer lists remaining tasks and estimates effort
- Identifies tasks not yet started that are on the critical path
- Flags any tasks that cannot realistically complete in 4 weeks

### Phase 4: Risk Identification and Scoring (~15 min, parallel)
- Risk Assessor performs systematic risk identification:
  - **Technical:** WebSocket scaling under load, Redis failover behavior, migration data integrity
  - **Operational:** On-call readiness, runbook completeness, monitoring gaps
  - **External:** Notification service SLA, CDN capacity, third-party rate limits
  - **Schedule:** Remaining work vs available time, testing coverage gaps
  - **Business:** User communication plan, support team readiness, rollback impact on users
- Scores each risk (probability 1-5, impact 1-5)
- Creates mitigation plans for all risks scoring 9 or above
- Resource Allocator assesses capacity for contingency work alongside remaining feature work

### Phase 5: Schedule Risk Analysis (~10 min)
- Scheduler validates: can remaining work complete in 4 weeks with risk mitigations included?
- Identifies schedule pressure points (e.g., migration must happen in Week 3 to allow Week 4 for monitoring)
- Recommends go/no-go decision timeline

### Phase 6: Risk Documentation and Action Items (~8 min)
- Integration Planner produces:
  - Full risk register with scores, owners, mitigations, and contingencies
  - Risk heat map visualization
  - Action item list with owners and deadlines
  - Launch go/no-go checklist
  - Monitoring plan for launch week (what to watch, thresholds, who responds)

## Expected Outputs

- Risk register with 15-25 identified risks across all categories
- Risk heat map (probability x impact matrix)
- Mitigation plans for all high-priority risks (score >= 9)
- Contingency plans for top 5 risks with trigger conditions
- Launch go/no-go checklist (5-10 items, each with pass/fail criteria)
- Monitoring plan for launch week
- Early warning indicators checklist with owners and check dates
- Action items exported to Linear/Jira with deadlines
- Critical path analysis showing remaining work vs timeline

## Estimated Cost

| Phase | Tokens | Cost |
|-------|--------|------|
| Risk Scope Configuration | ~8K | ~$0.48 |
| Launch Requirements Review | ~25K | ~$1.50 |
| Completeness Assessment | ~35K | ~$2.10 |
| Risk + Resource | ~100K | ~$11.40 |
| Schedule Risk Analysis | ~30K | ~$1.80 |
| Risk Documentation | ~25K | ~$0.63 |
| **Total** | **~223K** | **~$17.91** |

Note: Risk assessment scenarios are weighted toward Phase 4, where the Risk Assessor does the bulk of the analytical work. The Resource Allocator on Opus helps reason about whether the team has capacity for both remaining work and contingency execution.
