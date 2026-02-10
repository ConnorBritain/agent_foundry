# Multi-Agent Orchestration Protocol

This document defines the execution phases, communication protocols, quality gates, and decision-making framework for the Project Planning Team.

---

## Execution Modes

The team supports three execution modes. The mode is selected at runtime via the `--mode` flag.

### Sequential Mode

Agents execute one at a time in a defined order. Slowest but most predictable. Recommended for first-time users or debugging.

```
Coordinator → Requirements Analyst → Task Decomposer → Risk Assessor
→ Resource Allocator → Scheduler → Integration Planner
```

**Total time:** ~1.5-2 hours
**When to use:** First run, debugging, when you want to review each phase before proceeding.

### Hybrid Mode (Recommended)

Agents execute in parallel within phases but sequentially across phases. Quality gates between phases ensure coherence.

```
Phase 1 (sequential): Coordinator
  ↓ [Quality Gate 1]
Phase 2 (sequential): Requirements Analyst
  ↓ [Quality Gate 2]
Phase 3 (sequential): Task Decomposer
  ↓ [Quality Gate 3]
Phase 4 (parallel): Risk Assessor + Resource Allocator
  ↓ [Quality Gate 4]
Phase 5 (sequential): Scheduler
  ↓ [Quality Gate 5]
Phase 6 (sequential): Integration Planner
  ↓ [Quality Gate 6]
Phase 7 (parallel): Coordinator (final review) + Integration Planner (export)
  ↓ [Quality Gate 7 / Delivery Decision]
```

**Total time:** ~1-1.5 hours
**When to use:** Standard planning sessions. Best balance of speed and reliability.

### Swarm Mode

All agents run concurrently with message-passing coordination after the initial configuration phase. Fastest but requires robust conflict resolution. Experimental.

**Total time:** ~45-60 minutes
**When to use:** Experienced users, projects with well-defined scope, when speed is critical.
**Warning:** Higher risk of conflicts and wasted tokens from retries. Risk Assessor and Resource Allocator may produce conflicting assumptions.

---

## Phase Definitions

### Phase 1: Configuration (Sequential -- ~5 minutes)

**Goal:** Establish the project framework, tools, and constraints.

#### Coordinator
- Receive the user's high-level goal or vision statement
- Present framework options with brief descriptions (SAFe, Scrum, Kanban, Shape Up, Waterfall, Custom)
- Ask project type, team size, duration, tool preferences
- Validate project configuration and populate CONFIG.local.md
- Load framework-specific terminology, ceremonies, and artifacts
- Set estimation units and reporting cadence

**Outputs:**
- Populated CONFIG.local.md with framework and tool selections
- Framework-specific reference context loaded
- Phase 1 gate report

#### Quality Gate 1: Configuration Checkpoint

The Coordinator validates:

| Check | Criteria | Blocking |
|-------|----------|----------|
| Framework selected | Valid framework with appropriate settings | Yes |
| Tool integration configured | At least one task management tool specified | Yes |
| Team size defined | Greater than zero, reasonable for project scope | Yes |
| Duration set | Positive number of weeks with start date | Yes |
| Budget set | model_config and max_total_cost_usd defined | Yes |
| Stakeholders identified | At least one stakeholder with communication preferences | No |

**Pass criteria:** All blocking checks pass. Non-blocking issues logged for user review.

---

### Phase 2: Requirements Analysis (Sequential -- ~15 minutes)

**Goal:** Transform the user's vision into structured requirements.

#### Requirements Analyst
- Read the user's goal, vision statement, or project brief
- Decompose high-level objectives into major components and workstreams
- Define scope boundaries explicitly (what is IN, what is OUT)
- Identify key outcomes and measurable success criteria per workstream
- Map stakeholders to their information needs and decision authority
- Flag ambiguities and generate clarifying questions for the user
- Produce a structured requirements document with acceptance criteria

**Outputs:**
- Requirements document with workstreams, outcomes, and scope boundaries
- Stakeholder map with roles, needs, and communication preferences
- Clarifying questions for the user (if any)

**Depends on:** Phase 1 configuration (framework, project type, constraints).

#### Quality Gate 2: Requirements Checkpoint

| Check | Criteria | Blocking |
|-------|----------|----------|
| Workstreams defined | At least 2 workstreams with clear scope | Yes |
| Success criteria present | Every workstream has at least one measurable criterion | Yes |
| Scope boundaries explicit | IN and OUT scope clearly stated | Yes |
| Stakeholders mapped | All stakeholders have roles and communication plans | No |
| Ambiguities flagged | No silent assumptions; all unknowns documented | Yes |
| Acceptance criteria | Every requirement has verifiable acceptance criteria | Yes |

**User interaction point:** If the Requirements Analyst produced clarifying questions, the Coordinator pauses the workflow and presents them to the user. The user's answers are fed back to the Requirements Analyst for a revision pass before proceeding.

---

### Phase 3: Task Decomposition (Sequential -- ~20 minutes)

**Goal:** Create granular, actionable tasks with effort estimates.

#### Task Decomposer
- Take the Requirements Analyst's structured output
- Create granular, actionable tasks for each workstream
- Estimate effort per task using framework-appropriate units (story points, hours, t-shirt sizes)
- Write acceptance criteria for each task
- Tag tasks by workstream, skill required, and complexity level
- Identify task dependencies (which tasks must precede others)
- Build the Work Breakdown Structure (WBS)

**Outputs:**
- Complete task list with estimates, acceptance criteria, and tags
- Work Breakdown Structure (hierarchical view)
- Dependency annotations per task

**Depends on:** Phase 2 requirements document.

#### Quality Gate 3: Task Decomposition Checkpoint

| Check | Criteria | Blocking |
|-------|----------|----------|
| Task coverage | Every workstream has tasks assigned | Yes |
| Estimates present | Every task has an effort estimate | Yes |
| Acceptance criteria | Every task has at least one acceptance criterion | Yes |
| Dependencies mapped | Dependencies explicitly annotated | Yes |
| No orphaned tasks | Every task belongs to a workstream | Yes |
| Granularity check | Tasks are completable in one sprint/cycle | No |
| WBS structure | Hierarchical breakdown is coherent | Yes |

---

### Phase 4: Risk Assessment + Resource Allocation (Parallel -- ~15 minutes)

**Goal:** Identify risks, map dependencies, rank tasks, and allocate resources. These two agents run in parallel because their inputs are independent (both consume the task list from Phase 3) and their outputs are complementary.

#### Risk Assessor
- Identify project risks across categories: technical, resource, external, schedule, scope
- Assess each risk by probability (1-5) and impact (1-5)
- Classify dependencies as hard (must-sequence) vs soft (can-parallel-with-risk)
- Create mitigation strategies for high-priority risks (probability x impact >= 9)
- Define contingency plans for top 5 risks
- Identify early warning indicators for each risk
- Build the critical path analysis and flag schedule risks

**Outputs:**
- Risk register (risk, probability, impact, category, mitigation, contingency, owner)
- Dependency graph with critical path highlighted
- Risk heat map (probability x impact matrix)
- Early warning indicators checklist

**Depends on:** Phase 3 task list and dependency annotations.

#### Resource Allocator
- Analyze team capacity against task requirements
- Apply framework-appropriate prioritization methods:
  - Scrum: Value vs Effort matrix, MoSCoW
  - SAFe: WSJF (Weighted Shortest Job First)
  - Shape Up: Appetite assessment, bet evaluation
  - Kanban: Cost of Delay, service class prioritization
  - Waterfall: Critical path method
- Identify skill gaps and recommend hiring or training
- Balance workload across team members
- Make explicit trade-off recommendations (what to cut if resources are scarce)
- Create phased delivery plan (what ships in each iteration)

**Outputs:**
- Prioritized task backlog with ranking rationale
- Resource allocation matrix (person x task x time)
- Trade-off recommendations (what to cut/defer)
- Phased delivery plan

**Depends on:** Phase 3 task list with estimates and dependencies.

#### Quality Gate 4: Risk and Resource Checkpoint

| Check | Criteria | Blocking |
|-------|----------|----------|
| Risk register complete | All categories assessed, top risks have mitigations | Yes |
| No circular dependencies | Dependency graph is a valid DAG | Yes |
| Critical path identified | Longest dependency chain is marked | Yes |
| Prioritization applied | Framework-appropriate method used | Yes |
| Trade-offs explicit | Cut/defer recommendations documented | No |
| Resource utilization | No team member exceeds 80% capacity | Yes |
| Skill coverage | All required skills covered or gaps documented | Yes |

**Conflict resolution:** If Risk Assessor flags a dependency that Resource Allocator assumed could be parallelized, the Coordinator resolves the conflict using the Risk Assessor's classification as the conservative default.

---

### Phase 5: Scheduling (Sequential -- ~10 minutes)

**Goal:** Map the prioritized, resource-allocated plan to a calendar.

#### Scheduler
- Take the prioritized, dependency-mapped task list
- Map tasks to calendar based on CONFIG.local.md constraints (team size, duration, availability)
- Create framework-appropriate time boundaries (sprints, cycles, phases, PIs)
- Place milestones at meaningful checkpoints for stakeholders
- Account for holidays, team availability, and buffer time
- Optimize for parallel execution where dependencies allow
- Identify schedule risks (tight dependencies, long critical paths, resource bottlenecks)
- Prepare calendar events for Google Calendar or Outlook integration

**Outputs:**
- Calendar with sprint/cycle boundaries and milestones
- Schedule risk analysis
- Resource timeline (who works on what, when)
- Calendar event data for MCP export

**Depends on:** Phase 4 outputs (prioritized backlog, resource allocation, risk register, critical path).

#### Quality Gate 5: Schedule Checkpoint

| Check | Criteria | Blocking |
|-------|----------|----------|
| Schedule respects dependencies | All hard dependencies honored | Yes |
| Buffer included | Minimum 15% of total duration | Yes |
| No overloaded resources | All team members within capacity | Yes |
| Milestones placed | At least one milestone per reporting cadence | Yes |
| Fits duration | Schedule fits within target duration | Yes |
| Critical path feasible | Critical path tasks are sequenced correctly | Yes |

---

### Phase 6: Integration and Documentation (Sequential -- ~10 minutes)

**Goal:** Export the plan to tools and create documentation.

#### Integration Planner
- Take all previous phase outputs and synthesize into tool-ready artifacts
- Create Linear or Jira workspace with all tasks as issues
- Set dependencies, priorities, sprint/cycle assignments, and labels
- Generate stakeholder communication plan (who gets what info, when, how)
- Create project README with goals, scope, timeline, and conventions
- Export risk register and dependency graph to appropriate formats
- Produce executive summary suitable for leadership review

**Outputs:**
- Linear/Jira workspace (fully populated via MCP)
- Stakeholder communication plan
- Project README (markdown)
- Executive summary (1-page overview)
- Exported dependency graph (Mermaid diagram)

**Depends on:** All previous phase outputs.

#### Quality Gate 6: Integration Checkpoint

| Check | Criteria | Blocking |
|-------|----------|----------|
| All tasks exported | Every task appears as an issue in the target tool | Yes |
| Dependencies linked | Dependencies are set in the tool | Yes |
| Priorities match | Issue priorities match prioritization output | Yes |
| Labels applied | Workstream, type, and skill tags applied | No |
| Communication plan complete | All stakeholders from stakeholder map covered | Yes |
| Executive summary accurate | Summary reflects the full plan | No |

---

### Phase 7: Final Review and Export (Parallel -- ~5 minutes)

**Goal:** Validate the complete plan and export to calendar.

#### Coordinator (Final Review)
- Review all agent outputs for internal consistency
- Verify quality gates all passed
- Produce final plan assessment
- Identify any remaining issues for user review
- Issue DELIVER or REVISE recommendation

#### Integration Planner (Calendar Export)
- Export milestones and sprint boundaries to Google Calendar via MCP
- Create reminder events for stakeholder reviews
- Set up recurring ceremonies (standups, retros, demos) based on framework

**Outputs:**
- Plan assessment report
- Google Calendar events (via MCP)
- Final delivery recommendation

#### Quality Gate 7: Delivery Decision

| Check | Criteria | Blocking |
|-------|----------|----------|
| All prior gates passed | No unresolved blocking issues | Yes |
| Internal consistency | No contradictions between agent outputs | Yes |
| Calendar events created | Milestones in Google Calendar | No |
| User artifacts complete | README, executive summary, risk register | Yes |
| Tool integration verified | Tasks in Linear/Jira with correct metadata | Yes |

**Delivery decision:** Coordinator issues DELIVER or REVISE based on gate results.

---

## Communication Protocol

### Message Types

Agents communicate using structured messages with the following types:

| Type | Purpose | Example |
|------|---------|---------|
| `TASK` | Assign work to an agent | Coordinator assigns requirements analysis |
| `QUERY` | Ask another agent for information | Scheduler asks Risk Assessor for critical path |
| `RESPONSE` | Answer a query | Risk Assessor provides critical path data |
| `ARTIFACT` | Deliver a completed output | Task Decomposer delivers WBS |
| `CONFLICT` | Report a disagreement or incompatibility | Resource Allocator flags impossible schedule |
| `GATE` | Quality gate result | Coordinator reports Phase 2 gate: PASS |
| `ESCALATE` | Escalate to user for decision | Coordinator escalates scope ambiguity |

### Message Format

```yaml
type: TASK
from: coordinator
to: requirements-analyst
phase: 2
priority: high
subject: "Analyze project vision and produce requirements document"
body: |
  Based on the project configuration in CONFIG.local.md, analyze the user's
  vision statement and produce:
  - Workstream decomposition with scope boundaries
  - Measurable success criteria per workstream
  - Stakeholder map
  - Clarifying questions (if any)
  Use framework terminology: stories/epics for Scrum, bets for Shape Up.
acceptance_criteria:
  - Every workstream has at least one measurable success criterion
  - Scope boundaries are explicit (IN and OUT)
  - Ambiguities are flagged, not assumed
deadline: "Phase 2 completion"
```

### Conflict Resolution

When agents disagree (e.g., Risk Assessor and Resource Allocator conflict on dependency classification):

1. The conflicting agents state their positions with rationale
2. The Coordinator evaluates both positions against project goals and the selected framework
3. The Coordinator makes a binding decision and records it in a decisions log
4. Both agents proceed with the Coordinator's decision
5. If the Coordinator cannot resolve it, the issue is escalated to the user

### Shared State

All agents have read access to:
- Project configuration (`CONFIG.local.md`)
- All previous phase outputs (requirements doc, task list, risk register, etc.)
- The shared state directory for coordination files

Write access is scoped per agent to prevent conflicts:
- Each agent writes only to their designated output files
- Shared artifacts (dependency graph, calendar) have designated owners
- The Integration Planner is the only agent with write access to external tools (Linear, Jira, Google Calendar)

---

## Autonomous vs User-Prompted Decisions

### Autonomous (No User Input Needed)

The team makes these decisions automatically:

- Task granularity level (one sprint/cycle per task)
- Effort estimation methodology (per framework)
- Risk probability and impact scoring
- Dependency classification (hard vs soft)
- Calendar layout and sprint boundaries
- Label and tag conventions
- Document formatting and structure
- Buffer allocation percentages
- Communication plan structure

### User-Prompted (Require User Input)

The team pauses and asks the user for:

- **Scope ambiguity** -- "The vision mentions 'analytics'. Does this mean a reporting dashboard or embedded metrics?"
- **Priority conflicts** -- "Features A and B cannot both fit in Sprint 1. Which takes priority?"
- **Resource gaps** -- "No team member has mobile development skills. Hire, train, or cut mobile scope?"
- **Risk acceptance** -- "The critical path has zero buffer. Accept the risk or extend the timeline by 2 weeks?"
- **Budget overrun** -- "Phase 4 is projected to exceed budget by 20%. Continue or optimize?"
- **Tool preferences** -- "Linear and Jira are both configured. Which should receive the exported plan?"
- **Framework override** -- "You selected Scrum but the project characteristics suggest Shape Up. Switch?"

### Escalation Triggers

The Coordinator escalates immediately when:

1. A quality gate fails twice consecutively
2. Two agents produce conflicting outputs that cannot be auto-resolved
3. A required MCP server is unavailable (Linear, Jira, or Calendar)
4. Token usage exceeds 80% of budget before Phase 5
5. The user's vision statement is too vague to decompose (fewer than 2 workstreams identified)
6. The project configuration has contradictory settings

---

## Scenario-Based Validation

After each phase, the Coordinator can run scenario-based validation against the scenarios defined in `/scenarios/`. Each scenario specifies:

- **Preconditions:** Project state before the scenario
- **Steps:** Planning actions to perform
- **Expected outcomes:** What the plan should contain at each step
- **Edge cases:** Unusual inputs or failure conditions

Phase validation mapping:

| Phase | Scenarios Validated |
|-------|-------------------|
| Phase 1 | None (configuration only) |
| Phase 2 | Requirements completeness checks |
| Phase 3 | `sprint-planning.md` (task structure), `risk-assessment.md` (dependency coverage) |
| Phase 4 | `risk-assessment.md` (risk register completeness) |
| Phase 5 | `sprint-planning.md` (schedule feasibility), `quarterly-roadmap.md` (milestone placement) |
| Phase 6 | `cross-team-coordination.md` (tool export), all scenarios for final validation |
| Phase 7 | All scenarios, delivery readiness |

Scenario failures in Phase 7 are blocking for delivery. Scenario failures in earlier phases are logged as issues for the next phase.
