# Scenario: Quarterly Product Roadmap Creation

## Context

A product team needs to create a quarterly roadmap (13 weeks) for Q3. Multiple workstreams are in flight: new feature development, technical debt reduction, and infrastructure scaling. The roadmap must align engineering capacity with business priorities and provide milestone visibility to leadership.

## Trigger

The user provides business objectives and constraints for the quarter. Example:

> "Plan our Q3 roadmap. Objectives: (1) Launch self-serve onboarding, (2) Reduce API p99 latency below 200ms, (3) Migrate billing to Stripe. Team: 12 engineers across 3 squads. Quarter runs July 1 - September 30. We use Scrum with 2-week sprints."

## Team Configuration

| Agent | Role in This Scenario | Active |
|-------|----------------------|--------|
| Coordinator | Validate quarterly config, manage multi-workstream planning | Yes |
| Requirements Analyst | Decompose quarterly objectives into workstreams with success criteria | Yes |
| Task Decomposer | Create epic-level and story-level tasks across all workstreams | Yes |
| Scheduler | Plan 6-7 sprints across the quarter with milestones | Yes |
| Resource Allocator | Distribute 3 squads across workstreams, handle trade-offs | Yes (Opus) |
| Risk Assessor | Identify cross-workstream risks and quarterly dependencies | Yes |
| Integration Planner | Export full roadmap to tools, create leadership communication plan | Yes |

## Workflow

### Phase 1: Quarterly Configuration (~5 min)
- Coordinator sets up: Scrum framework, 13-week duration, 6-7 sprints
- Configures 3 squads with skill profiles
- Sets reporting cadence: biweekly for leadership, weekly for squad leads

### Phase 2: Objective Decomposition (~15 min)
- Requirements Analyst decomposes each objective into workstreams:
  - WS1: Self-serve onboarding (frontend, backend, integrations)
  - WS2: API performance optimization (profiling, caching, query optimization)
  - WS3: Stripe billing migration (data migration, API integration, testing)
- Defines success criteria per workstream (e.g., "onboarding completion rate >80%")
- Maps dependencies between workstreams (billing migration blocks onboarding pricing page)

### Phase 3: Task Decomposition (~25 min)
- Task Decomposer creates epics and stories for each workstream
- Estimates at story level (story points) and epic level (t-shirt sizes)
- Total estimated work: ~240 story points across all squads
- Maps cross-workstream dependencies

### Phase 4: Risk and Resource Assessment (~15 min, parallel)
- Risk Assessor flags: Stripe migration has external dependency on Stripe support team; API optimization may require infrastructure changes that affect other workstreams
- Resource Allocator distributes squads: Squad A on onboarding, Squad B on API performance, Squad C on billing migration
- Identifies that billing migration needs database expertise from Squad B in Sprint 3

### Phase 5: Quarter Scheduling (~12 min)
- Scheduler maps work across 6 sprints plus a buffer sprint
- Places quarterly milestones: mid-quarter review (Aug 12), feature freeze (Sep 15), launch (Sep 29)
- Ensures billing migration completes before onboarding pricing page starts
- Includes 2 weeks of buffer distributed across the quarter

### Phase 6: Roadmap Export (~8 min)
- Integration Planner creates full roadmap in Linear/Jira
- Generates leadership roadmap summary with milestone dates and confidence levels
- Creates cross-squad dependency diagram
- Sets up biweekly leadership review calendar events

## Expected Outputs

- Quarterly roadmap with 3 workstreams, 6-7 sprints, and key milestones
- 50-80 stories organized under 8-12 epics
- Resource allocation across 3 squads for the full quarter
- Cross-workstream dependency map
- Risk register with quarterly risks and mitigations
- Leadership summary with milestone dates and confidence levels
- Linear/Jira project with full sprint assignments
- Google Calendar with sprint boundaries, milestones, and review meetings

## Estimated Cost

| Phase | Tokens | Cost |
|-------|--------|------|
| Quarterly Configuration | ~15K | ~$0.90 |
| Objective Decomposition | ~45K | ~$2.70 |
| Task Decomposition | ~70K | ~$4.20 |
| Risk + Resource | ~100K | ~$11.40 |
| Quarter Scheduling | ~45K | ~$2.70 |
| Roadmap Export | ~30K | ~$0.75 |
| **Total** | **~305K** | **~$22.65** |

Note: Quarterly roadmapping is a full-complexity run. The Resource Allocator on Opus is essential here because it must reason about multi-squad allocation trade-offs across a 13-week horizon.
