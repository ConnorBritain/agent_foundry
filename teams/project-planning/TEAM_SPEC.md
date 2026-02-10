# Project Planning Team -- Technical Specification

## Overview

This document defines the architecture, agent composition, responsibilities, deliverables, and quality standards for the Project Planning Team. The team transforms high-level goals into fully structured, tool-integrated project plans across multiple planning frameworks.

---

## 1. Team Composition

The team consists of 7 specialized agents. One operates on Opus 4.6 for tasks requiring nuanced trade-off reasoning. Five operate on Sonnet 4.5 for structured analytical tasks. One operates on Haiku 4.5 for high-volume documentation generation.

### 1.1 Coordinator

- **Model:** Sonnet 4.5
- **Token budget:** ~15K tokens
- **Primary responsibilities:**
  - Receive the user's high-level goal or vision statement
  - Ask framework preference and present options with brief descriptions
  - Validate project configuration and populate CONFIG.md
  - Load framework-specific terminology, ceremonies, and artifacts
  - Manage workflow transitions between phases
  - Run quality gates at phase boundaries
  - Communicate with the user at decision points
  - Resolve conflicts between agents when outputs are inconsistent
- **Decision authority:**
  - FINAL say on framework selection and configuration
  - Can advance between phases when output quality meets thresholds
  - Escalates to user for scope changes, priority cuts, and external tool writes
- **Outputs:**
  - Populated CONFIG.md with framework and tool selections
  - Phase gate reports (pass/fail with details)
  - User communication at each phase boundary

### 1.2 Requirements Analyst

- **Model:** Sonnet 4.5
- **Token budget:** ~45K tokens
- **Primary responsibilities:**
  - Analyze the user's goal, vision statement, or project brief
  - Decompose high-level objectives into major components and workstreams
  - Define scope boundaries explicitly (what is IN, what is OUT)
  - Identify key outcomes and measurable success criteria per workstream
  - Map stakeholders to their information needs and decision authority
  - Flag ambiguities and generate clarifying questions for the user
  - Produce a structured requirements document with acceptance criteria
- **Quality standards:**
  - Every workstream has at least one measurable success criterion
  - Scope boundaries are explicit, not implied
  - Ambiguities are flagged, not assumed away
- **Outputs:**
  - Requirements document with workstreams, outcomes, and scope boundaries
  - Stakeholder map with roles, needs, and communication preferences
  - Clarifying questions for the user (if any)

### 1.3 Task Decomposer

- **Model:** Sonnet 4.5
- **Token budget:** ~60K tokens
- **Primary responsibilities:**
  - Take the Requirements Analyst's structured output
  - Create granular, actionable tasks for each workstream
  - Estimate effort per task using framework-appropriate units (story points, hours, t-shirt sizes)
  - Write acceptance criteria for each task
  - Tag tasks by workstream, skill required, and complexity level
  - Identify task dependencies (which tasks must precede others)
  - Build the Work Breakdown Structure (WBS)
- **Quality standards:**
  - Tasks are granular enough to be completed in one sprint/cycle but not so fine as to be micromanagement
  - Every task has an effort estimate and acceptance criteria
  - No orphaned tasks (every task belongs to a workstream)
  - Dependencies are explicitly marked
- **Outputs:**
  - Complete task list with estimates, acceptance criteria, and tags
  - Work Breakdown Structure (hierarchical view)
  - Dependency annotations per task

### 1.4 Scheduler

- **Model:** Sonnet 4.5
- **Token budget:** ~40K tokens
- **Primary responsibilities:**
  - Take the prioritized, dependency-mapped task list
  - Map tasks to calendar based on CONFIG.md constraints (team size, duration, availability)
  - Create framework-appropriate time boundaries (sprints, cycles, phases, PIs)
  - Place milestones at meaningful checkpoints for stakeholders
  - Account for holidays, team availability, and buffer time
  - Optimize for parallel execution where dependencies allow
  - Identify schedule risks (tight dependencies, long critical paths, resource bottlenecks)
  - Integrate with Google Calendar or Outlook via MCP
- **Quality standards:**
  - Schedule respects all hard dependencies
  - Buffer time is included (minimum 15% of total duration)
  - No team member is overloaded beyond capacity
  - Milestones align with stakeholder reporting cadence
- **Outputs:**
  - Calendar with sprint/cycle boundaries and milestones
  - Schedule risk analysis
  - Resource timeline (who works on what, when)
  - Google Calendar events (via MCP)

### 1.5 Resource Allocator

- **Model:** Opus 4.6
- **Token budget:** ~60K tokens
- **Primary responsibilities:**
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
- **Quality standards:**
  - Prioritization uses the framework-appropriate method
  - Trade-offs are explicit (show what each priority choice costs)
  - Resource assignments match skill requirements
  - No team member exceeds 80% capacity utilization
- **Outputs:**
  - Prioritized task backlog with ranking rationale
  - Resource allocation matrix (person x task x time)
  - Trade-off recommendations (what to cut/defer)
  - Phased delivery plan

### 1.6 Risk Assessor

- **Model:** Sonnet 4.5
- **Token budget:** ~40K tokens
- **Primary responsibilities:**
  - Identify project risks across categories: technical, resource, external, schedule, scope
  - Assess each risk by probability (1-5) and impact (1-5)
  - Classify risks: technical dependencies, resource dependencies, external dependencies (third parties, approvals)
  - Categorize dependencies as hard (must-sequence) vs soft (can-parallel-with-risk)
  - Create mitigation strategies for high-priority risks (probability x impact >= 9)
  - Define contingency plans for top 5 risks
  - Identify early warning indicators for each risk
  - Build the critical path analysis and flag schedule risks
- **Quality standards:**
  - Every risk has probability, impact, and category
  - Top risks have both mitigation and contingency plans
  - No circular dependencies in the dependency graph
  - Critical path is identified and validated
- **Outputs:**
  - Risk register (risk, probability, impact, category, mitigation, contingency, owner)
  - Dependency graph with critical path highlighted
  - Risk heat map (probability x impact matrix)
  - Early warning indicators checklist

### 1.7 Integration Planner

- **Model:** Haiku 4.5
- **Token budget:** ~30K tokens
- **Primary responsibilities:**
  - Take all previous phase outputs and synthesize into tool-ready artifacts
  - Create Linear or Jira workspace with all tasks as issues
  - Set dependencies, priorities, sprint/cycle assignments, and labels
  - Generate stakeholder communication plan (who gets what info, when, how)
  - Create project README with goals, scope, timeline, and conventions
  - Export risk register and dependency graph to appropriate formats
  - Produce executive summary suitable for leadership review
- **Quality standards:**
  - All tasks appear as issues in the target tool
  - Dependencies are linked in the tool
  - Priorities and labels match the prioritization output
  - Communication plan covers all stakeholders from the stakeholder map
- **Outputs:**
  - Linear/Jira workspace (fully populated via MCP)
  - Stakeholder communication plan
  - Project README (markdown)
  - Executive summary (1-page overview)
  - Exported dependency graph (Mermaid diagram)

---

## 2. Workflow

### Phase 1: Configuration (Sequential -- ~5 min)

**Goal:** Establish framework, tools, and constraints.

1. User provides high-level goal or vision
2. Coordinator asks framework preference (presents options with brief descriptions)
3. Coordinator asks project type, team size, duration, tool preferences
4. Coordinator populates CONFIG.md
5. Coordinator loads framework-specific terminology and reference docs

### Phase 2: Requirements Analysis (Sequential -- ~15 min)

**Goal:** Transform the vision into structured requirements.

1. Requirements Analyst reads user's goal/vision
2. Breaks into major components/workstreams
3. Identifies key outcomes and success criteria
4. Defines scope boundaries (in/out)
5. Flags ambiguities for user clarification
6. Produces stakeholder map

### Phase 3: Task Decomposition (Sequential -- ~20 min)

**Goal:** Create granular, actionable tasks.

1. Takes Requirements Analyst output
2. Creates tasks for each workstream
3. Estimates effort per task
4. Writes acceptance criteria
5. Tags tasks and identifies dependencies
6. Builds Work Breakdown Structure

### Phase 4: Risk Assessment (Can Overlap with Phase 5 -- ~15 min)

**Goal:** Identify risks and map dependencies.

1. Analyzes task list for technical, resource, and external risks
2. Builds dependency graph
3. Identifies critical path
4. Creates risk register with mitigation strategies
5. Categorizes dependencies as hard vs soft

### Phase 5: Resource Allocation and Prioritization (Sequential -- ~15 min)

**Goal:** Rank tasks and allocate resources.

1. Takes dependency graph and task list
2. Applies framework-appropriate prioritization
3. Analyzes team capacity and skill coverage
4. Assigns resources to tasks
5. Creates phased delivery plan
6. Recommends what to cut if resources are scarce

### Phase 6: Scheduling (Sequential -- ~10 min)

**Goal:** Map the plan to a calendar.

1. Takes prioritized, resource-allocated task list
2. Maps to calendar based on CONFIG constraints
3. Creates milestones and time boundaries
4. Accounts for availability, holidays, and buffers
5. Integrates with Google Calendar / Outlook
6. Identifies schedule risks

### Phase 7: Integration and Documentation (Sequential -- ~10 min)

**Goal:** Export the plan to tools and create documentation.

1. Creates Linear/Jira workspace with all tasks
2. Links dependencies and sets priorities
3. Creates stakeholder communication plan
4. Generates project README
5. Produces executive summary

---

## 3. Token Budget

### Budget by Agent

| Agent | Model | Est. Tokens | Est. Cost |
|-------|-------|-------------|-----------|
| Coordinator | Sonnet 4.5 | ~15K | ~$0.90 |
| Requirements Analyst | Sonnet 4.5 | ~45K | ~$2.70 |
| Task Decomposer | Sonnet 4.5 | ~60K | ~$3.60 |
| Scheduler | Sonnet 4.5 | ~40K | ~$2.40 |
| Resource Allocator | Opus 4.6 | ~60K | ~$9.00 |
| Risk Assessor | Sonnet 4.5 | ~40K | ~$2.40 |
| Integration Planner | Haiku 4.5 | ~30K | ~$0.75 |
| **Total** | | **~290K** | **~$21.75** |

Note: Estimates include a 15% buffer for iteration. Effective total approximately $25.

### Budget by Phase

| Phase | Duration | Agents | Tokens | Cost |
|-------|----------|--------|--------|------|
| Configuration | ~5 min | 1 | ~15K | ~$0.90 |
| Requirements Analysis | ~15 min | 1 | ~45K | ~$2.70 |
| Task Decomposition | ~20 min | 1 | ~60K | ~$3.60 |
| Risk Assessment | ~15 min | 1 | ~40K | ~$2.40 |
| Resource Allocation | ~15 min | 1 | ~60K | ~$9.00 |
| Scheduling | ~10 min | 1 | ~40K | ~$2.40 |
| Integration | ~10 min | 1 | ~30K | ~$0.75 |
| **Total** | **~1.5 hrs** | | **~290K** | **~$21.75** |

---

## 4. Output Artifacts

| Artifact | Format | Tool | Description |
|----------|--------|------|-------------|
| Requirements Document | Markdown | Repository | Workstreams, outcomes, scope boundaries, acceptance criteria |
| Task Workspace | Issues + metadata | Linear/Jira | Fully populated with all tasks, dependencies, priorities |
| Calendar | Events + milestones | Google Calendar | Sprint boundaries, milestones, deadlines |
| Dependency Graph | Mermaid diagram | Embedded in README | Task relationships and critical path |
| Risk Register | Table | Markdown / Notion | Risks, probability, impact, mitigations, contingencies |
| Resource Allocation Matrix | Table | Markdown | Person x task x time mapping |
| Stakeholder Comms Plan | Document | Markdown / Notion | Who gets what information, when, how |
| Project README | Markdown | Repository root | Goals, scope, timeline, team, conventions |
| Executive Summary | 1-page document | Markdown | High-level overview for leadership |

---

## 5. Quality Standards

### Plan Completeness

- Every workstream from the vision analysis has tasks assigned
- Every task has an effort estimate and acceptance criteria
- All dependencies are mapped; no orphaned or circular dependencies
- Critical path is identified and schedule-feasible

### Framework Adherence

- Terminology matches the selected framework (e.g., "Stories" for Scrum, "Bets" for Shape Up)
- Ceremonies and artifacts are framework-appropriate
- Prioritization method matches the framework

### Schedule Feasibility

- Schedule fits within the stated duration
- No resource is allocated beyond 80% capacity
- Buffer time is included (minimum 15% of total duration)
- Hard dependencies are respected in the timeline

### Tool Integration

- All tasks exported to the selected tool (Linear/Jira)
- Dependencies linked in the tool
- Milestones created in calendar
- Labels and metadata match the planning output

### Risk Coverage

- Technical, resource, external, schedule, and scope risks assessed
- Top 5 risks have mitigation and contingency plans
- Early warning indicators defined for each high-priority risk

---

## 6. Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Plan completeness | All workstreams have tasks | Component coverage check |
| Task quality | Actionable, estimated, with acceptance criteria | Task audit |
| Dependency accuracy | No circular dependencies, critical path identified | Graph validation |
| Schedule feasibility | Achievable given team size and duration | Constraint check |
| Risk coverage | Top risks identified with mitigations | Risk register review |
| Stakeholder readiness | All stakeholders have appropriate views | Comms plan review |
| Budget adherence | Within 20% of estimate | Actual vs projected tokens |
| User satisfaction | Plan adopted without major rework | Post-session feedback |
| Tool integration | All tasks in Linear/Jira, milestones in calendar | Export verification |
