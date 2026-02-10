# Scenario: Sprint Planning for a 2-Week Sprint

## Context

A software team of 5 engineers is midway through a 12-week project using Scrum. They need to plan the next 2-week sprint. The product backlog has been groomed but tasks need decomposition, estimation, assignment, and scheduling. The team has a velocity of approximately 40 story points per sprint.

## Trigger

The user provides a sprint goal and a set of prioritized backlog items to plan into the next sprint. Example:

> "Plan Sprint 4 for our e-commerce platform. Sprint goal: Complete checkout flow and begin payment integration. We have 5 engineers, 2-week sprint starting March 10. Velocity is 40 story points."

## Team Configuration

| Agent | Role in This Scenario | Active |
|-------|----------------------|--------|
| Coordinator | Validate sprint config, run quality gates | Yes |
| Requirements Analyst | Clarify acceptance criteria for sprint backlog items | Yes |
| Task Decomposer | Break backlog items into sprint-sized tasks with estimates | Yes |
| Scheduler | Map tasks to the 2-week sprint window with daily capacity | Yes |
| Resource Allocator | Assign tasks to engineers based on skills and capacity | Yes |
| Risk Assessor | Flag sprint-specific risks (dependencies, availability) | Yes |
| Integration Planner | Export sprint to Linear/Jira, create calendar events | Yes |

## Workflow

### Phase 1: Sprint Configuration (~3 min)
- Coordinator confirms framework: Scrum, 2-week sprint
- Validates team size (5), velocity (40 points), start date (March 10)
- Loads sprint-specific context (previous sprint outcomes, carryover items)

### Phase 2: Backlog Refinement (~8 min)
- Requirements Analyst reviews each backlog item for the sprint
- Clarifies acceptance criteria and flags ambiguities
- Confirms scope boundaries for the sprint goal

### Phase 3: Task Decomposition (~12 min)
- Task Decomposer breaks each backlog item into tasks (1-8 story points each)
- Writes acceptance criteria per task
- Maps task dependencies within the sprint
- Targets total of ~40 story points to match velocity

### Phase 4: Risk and Resource Assessment (~10 min, parallel)
- Risk Assessor identifies sprint risks: dependency on payment API team, engineer PTO on March 14-15
- Resource Allocator assigns tasks to engineers by skill match and availability
- Adjusts for reduced capacity (one engineer out 2 days)

### Phase 5: Sprint Scheduling (~8 min)
- Scheduler maps tasks to the 10 working days
- Places sprint ceremonies: planning (Mar 10), daily standups, review (Mar 21), retro (Mar 21)
- Accounts for the critical path through checkout flow tasks

### Phase 6: Export (~5 min)
- Integration Planner creates/updates issues in Linear or Jira
- Links dependencies, sets sprint assignment, applies labels
- Creates Google Calendar events for ceremonies

## Expected Outputs

- Sprint backlog with 8-15 tasks totaling ~40 story points
- Task assignments for all 5 engineers
- Sprint calendar with ceremonies and daily task plan
- Sprint risk register (3-5 risks with mitigations)
- Linear/Jira sprint populated with all issues
- Google Calendar events for sprint ceremonies

## Estimated Cost

| Phase | Tokens | Cost |
|-------|--------|------|
| Sprint Configuration | ~8K | ~$0.48 |
| Backlog Refinement | ~20K | ~$1.20 |
| Task Decomposition | ~30K | ~$1.80 |
| Risk + Resource | ~50K | ~$5.70 |
| Sprint Scheduling | ~20K | ~$1.20 |
| Export | ~15K | ~$0.38 |
| **Total** | **~143K** | **~$10.76** |

Note: Sprint planning is lighter than full project planning because scope is pre-defined and the project context already exists. Expect 50-60% of full project planning cost.
