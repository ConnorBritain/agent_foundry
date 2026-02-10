# Scenario: Cross-Team Coordination Across Sforza Teams

## Context

A project requires coordinated work across multiple Sforza teams. The project planning team must identify cross-team dependencies, establish integration contracts, schedule handoff points, and create a communication plan that keeps all teams aligned. This scenario exercises the Integration Planner's cross-team dependency mapping capabilities.

## Trigger

The user describes a project that spans multiple teams. Example:

> "We're launching a new AI-powered search feature. It requires: the Backend Engineering team to build the search API, the AI/ML team to train and deploy the ranking model, the Frontend team to build the search UI, and the DevOps team to provision the infrastructure. Plan the cross-team coordination for a 10-week timeline."

## Team Configuration

| Agent | Role in This Scenario | Active |
|-------|----------------------|--------|
| Coordinator | Manage cross-team planning complexity, resolve inter-team conflicts | Yes |
| Requirements Analyst | Identify cross-team requirements and interface contracts | Yes |
| Task Decomposer | Create tasks with explicit cross-team dependency annotations | Yes |
| Scheduler | Schedule handoff points and integration windows across teams | Yes |
| Resource Allocator | Identify shared resource constraints across teams | Yes (Opus) |
| Risk Assessor | Assess cross-team dependency risks, identify critical integration paths | Yes |
| Integration Planner | Map all cross-team dependencies, design integration sequence, create shared communication plan | Yes |

## Workflow

### Phase 1: Multi-Team Configuration (~5 min)
- Coordinator identifies 4 participating teams and their capacities
- Sets up shared timeline (10 weeks) and integration milestones
- Establishes communication protocol between teams

### Phase 2: Cross-Team Requirements (~15 min)
- Requirements Analyst identifies interface contracts between teams:
  - Backend <-> AI/ML: Model serving API contract (input schema, output schema, latency SLA)
  - Backend <-> Frontend: Search API contract (endpoints, request/response format, pagination)
  - Backend <-> DevOps: Infrastructure requirements (compute, storage, networking)
  - AI/ML <-> DevOps: GPU provisioning and model deployment pipeline
- Flags ambiguities in cross-team interfaces
- Documents who owns each interface contract

### Phase 3: Task Decomposition with Cross-Team Tags (~20 min)
- Task Decomposer creates tasks per team with cross-team dependency annotations
- Marks tasks that block other teams (e.g., "Backend: Deploy search API v1" blocks "Frontend: Integrate search UI")
- Identifies shared tasks that need joint effort (e.g., integration testing)
- Creates integration tasks at team boundaries

### Phase 4: Risk and Resource Assessment (~15 min, parallel)
- Risk Assessor identifies cross-team risks:
  - AI/ML model training may take longer than estimated, blocking backend integration
  - DevOps GPU provisioning has 2-week lead time
  - No shared staging environment exists for end-to-end testing
- Resource Allocator identifies shared resource constraints:
  - One senior engineer is needed by both Backend and AI/ML teams
  - Shared staging environment needs DevOps allocation in Week 5

### Phase 5: Cross-Team Scheduling (~12 min)
- Scheduler creates a unified timeline across all 4 teams
- Places integration milestones at handoff points:
  - Week 3: API contracts finalized (all teams)
  - Week 5: Model serving API available (AI/ML -> Backend)
  - Week 6: Search API v1 available (Backend -> Frontend)
  - Week 7: Infrastructure ready (DevOps -> all teams)
  - Week 8: End-to-end integration testing (all teams)
  - Week 9: Bug fixes and hardening
  - Week 10: Launch
- Schedules cross-team sync meetings (weekly)

### Phase 6: Coordination Artifacts (~10 min)
- Integration Planner produces:
  - Cross-team dependency diagram showing all inter-team handoffs
  - Interface contract register with owners, SLAs, and status
  - Shared milestone calendar visible to all teams
  - Escalation protocol for cross-team blockers
  - Communication plan: weekly cross-team sync, daily per-team standups, Slack channels per interface

## Expected Outputs

- Cross-team dependency map (Mermaid diagram) showing all inter-team handoffs
- Interface contract register with 4-6 contracts, each with owner, schema, and SLA
- Unified timeline with integration milestones visible to all teams
- Per-team task lists with cross-team dependency annotations
- Cross-team risk register (5-8 risks focused on integration points)
- Communication plan covering all 4 teams
- Linear/Jira project with cross-team issue links
- Shared Google Calendar with integration milestones and sync meetings

## Estimated Cost

| Phase | Tokens | Cost |
|-------|--------|------|
| Multi-Team Configuration | ~15K | ~$0.90 |
| Cross-Team Requirements | ~50K | ~$3.00 |
| Task Decomposition | ~65K | ~$3.90 |
| Risk + Resource | ~100K | ~$11.40 |
| Cross-Team Scheduling | ~45K | ~$2.70 |
| Coordination Artifacts | ~35K | ~$0.88 |
| **Total** | **~310K** | **~$22.88** |

Note: Cross-team coordination is among the most complex scenarios. The Resource Allocator on Opus is critical for reasoning about shared resource constraints across teams. Budget an additional 20% for cross-team conflict resolution.
