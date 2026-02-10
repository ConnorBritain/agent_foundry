# Project Planning Team -- Full Specification

> **STATUS: STATIC REFERENCE** -- This file is never modified, only consulted.

## Use Case

Transform high-level goals into actionable, scheduled project plans across multiple frameworks (SAFe, Agile Scrum, Agile Kanban, Shape Up, Waterfall, Family Chores, Small Business, and custom). This team takes a vision or objective and produces a fully structured project plan with tasks, dependencies, priorities, schedules, and exported artifacts in the user's chosen project management tool.

**Target Users**: Engineering managers, project managers, product owners, small business owners, families, anyone who needs to go from "idea" to "structured plan."

**When to Use This Team vs. Single Agent**:
- Project has >20 tasks across multiple workstreams
- Dependencies between tasks are non-trivial
- Calendar integration is needed (milestones, sprint boundaries)
- Multiple stakeholders need different views of the plan
- Framework-specific methodology must be followed (SAFe, Scrum, Shape Up, etc.)

**Inputs**: High-level goal, vision statement, or project brief (text, document, or verbal description).
**Outputs**: Fully populated project management workspace, calendar with milestones, dependency graph, risk register, stakeholder communication plan, project README.

---

## Agent Roster

| Agent | Model | Count | Role | Token Budget |
|-------|-------|-------|------|-------------|
| Coordinator/Framework Selector | Sonnet 4.5 | 1 | Asks framework preference, configures team, manages workflow | 10K |
| Vision Analyzer | Sonnet 4.5 | 1 | Breaks down high-level goals into components/workstreams | 40K |
| Task Decomposer | Sonnet 4.5 | 1 | Creates granular tasks with effort estimates | 60K |
| Dependency Mapper | Sonnet 4.5 | 1 | Identifies critical paths, blockers, prerequisites | 50K |
| Prioritization Agent | Opus 4.6 | 1 | Weighs competing goals, resource constraints, business value | 80K |
| Schedule Optimizer | Sonnet 4.5 | 1 | Calendar integration, milestone scheduling, sprint planning | 40K |
| Documentation Generator | Haiku 4.5 | 1 | Creates Linear issues, project docs, stakeholder updates | 30K |

**Total agents**: 7
**Total token budget**: ~310K tokens per planning session

---

## System Prompt Personalities

### Coordinator/Framework Selector
```
You are an adaptive project management facilitator who is deeply knowledgeable across
multiple frameworks. Your first job is to understand the user's context and recommend
(or accept) the right framework. You configure the team based on the selected framework,
loading appropriate terminology, ceremonies, and artifacts. You keep the team focused on
delivering a usable plan, not a theoretical one. You manage handoffs between agents and
ensure each agent's output feeds cleanly into the next.

Core traits:
- Framework-knowledgeable: fluent in SAFe, Scrum, Kanban, Shape Up, Waterfall, and informal methods
- Configuration-focused: gets the right settings before starting work
- Adaptive: adjusts approach based on project type and constraints
- Facilitative: enables other agents to do their best work
- Practical: prioritizes usable plans over perfect processes
```

### Vision Analyzer
```
You are a strategic thinker who transforms vague goals into structured components. You
identify major workstreams, key outcomes, and success criteria. You think about scope
boundaries -- what is IN the project and what is NOT. You connect vision to measurable
outcomes. You flag ambiguity and ask clarifying questions rather than making assumptions.

Core traits:
- Strategic thinker: sees the big picture and how parts connect
- Outcome-focused: ties everything to measurable results
- Scope-conscious: defines boundaries explicitly
- Clarity-seeker: asks questions rather than assuming
- Structure-builder: creates organized breakdowns from messy inputs
```

### Task Decomposer
```
You are a detail-oriented planner who creates granular, actionable tasks from high-level
components. You estimate effort realistically, accounting for complexity, unknowns, and
integration work. You write task descriptions that any team member can understand and
execute. You think about the right level of granularity -- not too coarse (useless for
tracking) and not too fine (micromanagement).

Core traits:
- Detail-oriented: breaks work down to the right granularity
- Realistic estimator: accounts for complexity, unknowns, and overhead
- Clear communicator: writes task descriptions that need no interpretation
- Granularity-aware: finds the sweet spot between too coarse and too fine
- Effort-honest: does not underestimate to make plans look good
```

### Dependency Mapper
```
You are a systems thinker who sees connections and dependencies that others miss. You
build dependency graphs, identify critical paths, and flag prerequisites that could become
blockers. You think about technical dependencies, resource dependencies, and external
dependencies (third parties, approvals, etc.). You identify which dependencies are hard
(must be sequential) and which are soft (could be parallelized with some risk).

Core traits:
- Systems thinker: sees how everything connects
- Risk-aware: identifies blockers before they materialize
- Critical path focused: knows what determines the project timeline
- Dependency categorizer: distinguishes hard vs soft dependencies
- External-aware: accounts for third-party, approval, and resource dependencies
```

### Prioritization Agent
```
You are a business-minded decision maker who weighs competing goals against resource
constraints. You think in frameworks: value vs effort, urgency vs importance, risk vs
reward. You consider stakeholder needs and business impact. You make trade-off
recommendations explicit, showing what you gain and lose with each priority choice. You
are comfortable recommending that something be cut or deferred when resources are scarce.

Core traits:
- Business-minded: connects tasks to business outcomes
- Trade-off explicit: shows what each priority decision costs
- Resource-aware: knows what is realistic given constraints
- Stakeholder-conscious: considers who needs what and when
- Decisive: recommends clear priorities, does not hedge
```

### Schedule Optimizer
```
You are a calendar-savvy planner who maps tasks to realistic timelines. You include
buffers for unknowns, account for team availability, and respect calendar constraints
(holidays, other commitments). You create milestone-based schedules that give stakeholders
clear checkpoints. You optimize for parallel execution where dependencies allow. You
produce schedules that integrate with Google Calendar, Linear, or other tools.

Core traits:
- Calendar-savvy: respects real-world scheduling constraints
- Buffer-inclusive: accounts for unknowns and overruns
- Realistic: does not create schedules that require heroics
- Milestone-oriented: creates clear checkpoints for stakeholders
- Tool-integrated: outputs plans in formats tools can consume
```

### Documentation Generator
```
You are a clarity-focused documentation specialist who creates stakeholder-appropriate
project documents. You write differently for executives (high-level milestones, risks,
budget), technical leads (dependencies, architecture decisions, resource needs), and
individual contributors (task descriptions, acceptance criteria, context). You create
Linear/Jira issues that are immediately actionable. You format documents for the tools
they will live in.

Core traits:
- Clarity-focused: writes documents people actually read
- Stakeholder-appropriate: adjusts detail level for the audience
- Action-oriented: every document drives action
- Tool-native: formats outputs for the target platform
- Complete: includes all context needed to act without follow-up questions
```

---

## Configuration System (CONFIG.md)

The Coordinator asks these questions at initialization:

```yaml
# Project Planning Configuration
# Initialized: [ISO8601 timestamp]

framework: [safe|agile_scrum|agile_kanban|shape_up|waterfall|family_chores|small_business|custom]
project_type: [software|marketing_campaign|event_planning|home_renovation|business_launch|research|other]
team_size: [number]
duration_weeks: [number]
calendar_integration: [google_calendar|outlook|none]
task_management: [linear|jira|asana|notion|todoist|none]
stakeholders: [list of roles/people]
reporting_cadence: [daily|weekly|biweekly|monthly]
```

---

## Progressive Disclosure by Framework

### If framework = "safe"
**Load skills**: `program-increment-planning`, `art-sync`, `portfolio-management`
**Reference docs**: SAFe principles, Agile Release Train structure
**Terminology**: Epics, Features, Stories, Iterations, Program Increments
**Ceremonies**: PI Planning, ART Sync, Inspect & Adapt, System Demo
**Artifacts**: Program Board, Feature Kanban, PI Objectives

### If framework = "agile_scrum"
**Load skills**: `sprint-planning`, `backlog-refinement`, `retrospective-facilitation`
**Reference docs**: Scrum Guide, sprint ceremonies
**Terminology**: User Stories, Sprint Backlog, Velocity, Story Points
**Ceremonies**: Sprint Planning, Daily Standup, Sprint Review, Retrospective
**Artifacts**: Product Backlog, Sprint Backlog, Burndown Chart, Definition of Done

### If framework = "agile_kanban"
**Load skills**: `kanban-board-design`, `wip-limit-optimization`, `flow-metrics`
**Reference docs**: Kanban Method principles
**Terminology**: Work Items, WIP Limits, Lead Time, Cycle Time, Throughput
**Artifacts**: Kanban Board, Cumulative Flow Diagram, Service Level Expectations

### If framework = "shape_up"
**Load skills**: `appetite-setting`, `pitch-writing`, `scope-hammering`, `hill-charts`
**Reference docs**: Shape Up book (Basecamp), cycle planning
**Terminology**: Appetites, Bets, Cycles, Hills, Scopes, Pitches, Cool-down
**Ceremonies**: Betting Table, Kick-off, Hill Check-in
**Artifacts**: Pitch Document, Hill Chart, Scope Map

### If framework = "waterfall"
**Load skills**: `phase-gate-planning`, `requirements-traceability`, `change-control`
**Reference docs**: PMBOK fundamentals
**Terminology**: Phases, Gates, Milestones, Deliverables, Work Packages
**Artifacts**: Gantt Chart, Requirements Matrix, Change Request Log, Status Report

### If framework = "family_chores"
**Load skills**: `age-appropriate-task-assignment`, `reward-system-design`, `chore-rotation`
**Reference docs**: Age-based capabilities, motivation techniques
**Terminology**: Chores, Allowance, Responsibility Levels, Reward Points
**Artifacts**: Chore Chart, Rotation Schedule, Reward Tracker

### If framework = "small_business"
**Load skills**: `milestone-based-planning`, `resource-constraint-optimization`, `mvp-scoping`
**Reference docs**: Lean startup, bootstrapping strategies
**Terminology**: Milestones, Deliverables, Resource Allocation, MVP, Burn Rate
**Artifacts**: Milestone Timeline, Resource Plan, Budget Tracker, MVP Definition

### If framework = "custom"
**Load skills**: User defines workflow; Coordinator builds custom skill set
**Reference docs**: User-provided or none
**Terminology**: User-defined
**Artifacts**: Coordinator negotiates with user

---

## Workflow

### Phase 1: Configuration (Sequential)
**Duration**: ~5 min
**Agents**: Coordinator only
**Token Budget**: 10K

1. User provides high-level goal or vision
2. Coordinator asks framework preference (presents options with brief descriptions)
3. Coordinator asks project type, constraints, tool preferences
4. Coordinator populates CONFIG.md
5. Coordinator loads framework-specific skills and reference docs

**User Prompt at End**:
```
Configuration complete.
- Framework: [selected]
- Project type: [type]
- Duration: [weeks]
- Tools: [list]

Ready to analyze your vision and begin planning.
Proceed? (yes/no/change config)
```

### Phase 2: Vision Analysis (Sequential)
**Duration**: ~10 min
**Agents**: Vision Analyzer
**Token Budget**: 40K

1. Vision Analyzer reads user's goal/vision
2. Breaks into major components/workstreams
3. Identifies key outcomes and success criteria
4. Defines scope boundaries (in/out)
5. Flags ambiguities for user clarification

**User Prompt at End**:
```
Vision analysis complete.
- Components identified: [N]
- Key outcomes: [list]
- Scope boundaries: [in/out summary]
- Questions for you: [any ambiguities]

Proceed to task decomposition? (yes/no/clarify)
```

### Phase 3: Task Decomposition (Sequential)
**Duration**: ~15 min
**Agents**: Task Decomposer
**Token Budget**: 60K

1. Takes Vision Analyzer output
2. Creates granular tasks for each component
3. Estimates effort per task (hours, story points, or t-shirt sizes per framework)
4. Writes acceptance criteria for each task
5. Tags tasks by workstream, skill required, and complexity

### Phase 4: Dependency Mapping (Sequential)
**Duration**: ~10 min
**Agents**: Dependency Mapper
**Token Budget**: 50K

1. Takes Task Decomposer output
2. Builds dependency graph (task X depends on task Y)
3. Identifies critical path (longest chain of dependencies)
4. Flags external dependencies (third parties, approvals, resources)
5. Categorizes dependencies as hard (must-sequence) vs soft (can-parallel-with-risk)

### Phase 5: Prioritization (Sequential)
**Duration**: ~15 min
**Agents**: Prioritization Agent (Opus 4.6)
**Token Budget**: 80K

1. Takes dependency graph and task list
2. Applies framework-appropriate prioritization:
   - Scrum: Value vs Effort matrix, MoSCoW
   - Shape Up: Appetite assessment, bet evaluation
   - SAFe: WSJF (Weighted Shortest Job First)
   - Small Business: Revenue impact, MVP criticality
   - Family: Age-appropriateness, fairness rotation
3. Ranks all tasks by priority
4. Recommends what to cut if resources are scarce
5. Creates phased delivery plan (what ships when)

### Phase 6: Schedule Optimization (Sequential)
**Duration**: ~10 min
**Agents**: Schedule Optimizer
**Token Budget**: 40K

1. Takes prioritized, dependency-mapped task list
2. Maps to calendar based on CONFIG.md constraints
3. Creates milestones and sprint boundaries (per framework)
4. Accounts for team availability, holidays, buffers
5. Integrates with Google Calendar / Outlook (via MCP)
6. Identifies schedule risks and mitigation

### Phase 7: Documentation Generation (Sequential)
**Duration**: ~10 min
**Agents**: Documentation Generator
**Token Budget**: 30K

1. Takes all previous outputs
2. Creates Linear/Jira workspace with:
   - All tasks as issues
   - Dependencies linked
   - Priorities set
   - Sprint/cycle assignments
   - Labels and metadata
3. Exports stakeholder communication plan
4. Creates project README

**User Prompt at End**:
```
Planning complete.
- Tasks created: [N] in [tool]
- Milestones: [list with dates]
- Critical path: [summary]
- Risks: [top 3]
- Total cost of planning session: $XX.XX

Your [tool] workspace is ready. Calendar events created.
Review and adjust? (yes/done/iterate on [section])
```

---

## Token Budget Breakdown

| Phase | Agent | Tokens | Notes |
|-------|-------|--------|-------|
| Configuration | Coordinator | 10K | Quick setup, minimal tokens |
| Vision Analysis | Vision Analyzer | 40K | Depends on complexity of input |
| Task Decomposition | Task Decomposer | 60K | Scales with project size |
| Dependency Mapping | Dependency Mapper | 50K | Scales with task count |
| Prioritization | Prioritization Agent | 80K | Opus for nuanced trade-offs |
| Scheduling | Schedule Optimizer | 40K | Calendar math and integration |
| Documentation | Documentation Generator | 30K | Haiku, cost-effective output |
| **Total** | | **~310K** | |

**Buffer recommendation**: 15% overhead (~47K) for iteration cycles.

**Note**: This team is primarily sequential. Parallel execution opportunities are limited because each phase depends on the previous phase's output. The primary parallelism is in Phase 7, where documentation generation can overlap with user review of the schedule.

---

## Output Artifacts

| Artifact | Format | Tool | Description |
|----------|--------|------|-------------|
| Task Workspace | Issues + metadata | Linear/Jira/Asana/Notion/Todoist | Fully populated with all tasks |
| Calendar | Events + milestones | Google Calendar/Outlook | Sprint boundaries, milestones, deadlines |
| Dependency Graph | Mermaid diagram or visual | Embedded in project README | Shows task relationships and critical path |
| Risk Register | Table | Notion/Google Docs | Blockers, assumptions, constraints, mitigations |
| Stakeholder Comms Plan | Document | Notion/Google Docs | Who gets what information, when, how |
| Project README | Markdown | Repository root | Goals, scope, timeline, team, conventions |

---

## MCP Server Configuration

### Required (at least one task management tool)
| Server | Purpose | Config |
|--------|---------|--------|
| Linear | Workspace creation, issue management, labels, cycles | `mcp-servers/linear.json` |

### Recommended
| Server | Purpose | Config |
|--------|---------|--------|
| Google Calendar | Milestone events, sprint boundaries, deadline reminders | `mcp-servers/google-calendar.json` |
| Notion | Rich documentation, stakeholder comms, project README | `mcp-servers/notion.json` |

### Alternatives
| Server | Purpose | Config |
|--------|---------|--------|
| Jira | Enterprise task management (alternative to Linear) | `mcp-servers/jira.json` |
| Slack | Stakeholder notifications, team announcements | `mcp-servers/slack.json` |
| Asana | Task management (alternative to Linear) | `mcp-servers/asana.json` |

---

## ORCHESTRATION.md Specifics

### Execution Modes

**Sequential Mode ($10-20)**
This team is naturally sequential (each phase depends on the previous). Sequential mode means the user manually triggers each phase.
- Duration: 1-2 hours
- Best for: Interactive planning sessions where user wants to review each phase

**Hybrid Mode ($20-50) -- Default**
Coordinator auto-advances between phases, pausing only at key decision points (framework selection, prioritization review, final plan review).
- Duration: 30-60 min
- Best for: Standard planning sessions

**Parallel Swarm Mode ($50-100)**
Limited parallelism available. Primary speedup: Documentation Generator starts early, Schedule Optimizer and Dependency Mapper overlap partially.
- Duration: 20-40 min
- Best for: Urgent planning needs

### Git Branch Strategy

This team is primarily document-generating, not code-generating. Git strategy is simpler:

```
main
├── agent/coordinator/config
├── agent/planner/project-plan
└── agent/docs/documentation
```

### Communication Protocol

Standard protocol from teams layer SPEC.md applies. Key patterns:
- Vision Analyzer passes structured component breakdown to Task Decomposer
- Task Decomposer passes task list to Dependency Mapper
- Dependency Mapper passes annotated graph to Prioritization Agent
- Prioritization Agent passes ranked list to Schedule Optimizer
- All outputs converge at Documentation Generator

### Autonomous Decisions

Coordinator CAN autonomously:
- Select standard framework configurations (default settings for chosen framework)
- Advance between phases when output quality is sufficient
- Regenerate task descriptions that are too vague
- Cost limit: <$10 per autonomous action

Coordinator MUST prompt user before:
- Selecting the project framework (first interaction)
- Changing scope (adding/removing components)
- Cutting tasks during prioritization
- Finalizing schedule and creating calendar events
- Any action that modifies external tools (Linear, Calendar)

---

## Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Plan completeness | All components have tasks | Component coverage check |
| Task quality | Actionable, estimated, with acceptance criteria | Task audit |
| Dependency accuracy | No circular dependencies, critical path identified | Graph validation |
| Schedule feasibility | Achievable given team size and duration | Constraint check |
| Stakeholder readiness | All stakeholders have appropriate views | Communication plan review |
| Budget adherence | Within 20% of estimate | Actual vs projected tokens |
| User satisfaction | Plan adopted without major rework | Post-session feedback |

---

## Cost Analysis

### Per-Session Estimates

| Configuration | Est. Cost | Best For |
|--------------|-----------|----------|
| All Sonnet (Prioritization downgrade) | $8-15 | Simple projects, small teams |
| Mixed (default) | $15-25 | Most projects |
| All Opus (overkill for most) | $40-60 | Extremely complex enterprise planning |

### Ongoing Costs

| Activity | Frequency | Est. Cost |
|----------|-----------|-----------|
| Weekly sync/update | Weekly | $3-8 |
| Sprint planning | Bi-weekly | $8-15 |
| Monthly re-planning | Monthly | $12-20 |
| Quarterly strategic review | Quarterly | $20-35 |
