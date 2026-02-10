# Decision Framework

> A structured framework for deciding team composition, execution strategy, and resource allocation in Sforza.

## Overview

Sforza gives you the building blocks — agent roles, model tiers, harnesses, and orchestration patterns. But the blocks can be assembled in many ways, and the right assembly depends on your project. A solo developer automating tests needs a different configuration than an enterprise team building a product from a specification.

This framework provides decision trees, evaluation criteria, and allocation models so you can make these choices systematically rather than by intuition. Each decision point includes concrete criteria and recommended configurations.

The framework covers four key decisions: which teams to use, how many agents to run, whether to execute serially or in parallel, and how to allocate your budget across agents and tasks.

## Decision 1: Which Teams to Use

### Team Selection Decision Tree

```
START: What is your project goal?
  |
  |-- Building a new feature or product from scratch?
  |     |
  |     |-- Is there a written specification?
  |     |     YES --> "spec-to-product" team
  |     |     NO  --> "product-discovery" team (writes spec first, then builds)
  |     |
  |     |-- Is it full-stack (frontend + backend)?
  |           YES --> "full-stack" team (5-7 agents)
  |           NO  --> "focused" team (3-4 agents, backend-only or frontend-only)
  |
  |-- Modifying or improving an existing codebase?
  |     |
  |     |-- Is it a refactoring / migration?
  |     |     YES --> "refactoring" team (architect + implementers + test agents)
  |     |     NO  --> Continue
  |     |
  |     |-- Is it bug fixes or maintenance?
  |     |     YES --> "maintenance" team (debugger + fixer + test agent)
  |     |     NO  --> "enhancement" team (developer + reviewer + test agent)
  |
  |-- Research, analysis, or documentation?
  |     YES --> "research" team (analyst + writer + reviewer)
  |     NO  --> Continue
  |
  |-- Code review or quality audit?
        YES --> "review" team (security reviewer + quality reviewer + reporter)
        NO  --> Use a single agent with the appropriate role
```

### Team Templates Quick Reference

| Team Type | Agents | Typical Models | Duration | Est. Cost Range |
|---|---|---|---|---|
| spec-to-product | 5-7 | 1 Opus + 3-4 Sonnet + 1-2 Haiku | 2-6 hours | $15-60 |
| full-stack | 5-7 | 1 Opus + 3-4 Sonnet + 1-2 Haiku | 2-6 hours | $15-60 |
| focused (backend/frontend) | 3-4 | 1 Sonnet (lead) + 2-3 Sonnet/Haiku | 1-3 hours | $5-25 |
| refactoring | 4-5 | 1 Opus + 2-3 Sonnet + 1 Haiku | 1-4 hours | $10-40 |
| maintenance | 2-3 | 1 Sonnet + 1-2 Haiku | 30min-2hr | $2-10 |
| enhancement | 3-4 | 1 Sonnet + 1-2 Sonnet + 1 Haiku | 1-3 hours | $5-20 |
| research | 2-3 | 1 Opus + 1 Sonnet + 1 Haiku | 1-2 hours | $5-15 |
| review | 2-3 | 1 Opus + 1-2 Sonnet | 30min-1hr | $3-10 |

### Single Agent vs. Team Decision

Not every task needs a team. Use this to decide:

```
Should I use a team or a single agent?

SINGLE AGENT when:
  - Task is well-defined and scoped to < 5 files
  - No review or validation is needed beyond running tests
  - Task can complete in one context window
  - Budget is tight and the task is straightforward

TEAM when:
  - Task spans multiple concerns (frontend + backend + tests)
  - Task requires review (security, architecture, quality)
  - Task is large enough to benefit from parallel execution
  - Output quality must be high (multi-agent review improves quality)
  - Task requires different expertise (security + performance + UX)
```

## Decision 2: How Many Agents to Run

### Agent Count Guidelines

```
Minimum viable team: 2 agents
  - 1 implementer + 1 reviewer
  - Use when: simple features, tight budget, clear requirements

Standard team: 3-4 agents
  - 1 coordinator + 1-2 implementers + 1 tester/reviewer
  - Use when: moderate features, balanced cost/quality needs

Full team: 5-7 agents
  - 1 orchestrator + 2-3 implementers + 1 reviewer + 1-2 testers
  - Use when: complex features, quality matters, budget allows

Large team: 8+ agents
  - Multiple sub-teams with a master orchestrator
  - Use when: large-scale projects, multiple workstreams, enterprise use
  - Warning: coordination overhead increases with agent count
```

### Diminishing Returns Curve

```
Quality
  ^
  |         .............................
  |       ..
  |     ..
  |   ..
  |  .
  | .
  |.
  +---+---+---+---+---+---+---+---+--> Agent Count
      1   2   3   4   5   6   7   8

Key inflection points:
- 1 -> 2 agents: Major quality jump (review catches errors)
- 2 -> 4 agents: Significant improvement (specialization + parallel work)
- 4 -> 6 agents: Moderate improvement (more specialization)
- 6 -> 8 agents: Minimal improvement (coordination overhead grows)
- 8+  agents: Returns diminish, coordination cost dominates
```

### The Coordination Tax

Every additional agent adds coordination overhead:

| Team Size | Coordination Overhead | Net Productivity per Agent |
|---|---|---|
| 1 agent | 0% | 100% |
| 2 agents | ~5% | ~95% |
| 3 agents | ~10% | ~90% |
| 4 agents | ~15% | ~85% |
| 5 agents | ~20% | ~80% |
| 6 agents | ~25% | ~75% |
| 8 agents | ~35% | ~65% |
| 10 agents | ~45% | ~55% |

**Rule of thumb**: If the coordination cost exceeds 30%, you have too many agents. Split into sub-teams with separate orchestrators instead of running one large team.

## Decision 3: Serial vs. Parallel Execution

### Execution Strategy Decision Tree

```
START: Can agents work on independent tasks simultaneously?
  |
  |-- YES (tasks have no shared file dependencies)
  |     |
  |     |-- Are you budget-constrained?
  |     |     YES --> Run 2-3 in parallel (cost-controlled parallelism)
  |     |     NO  --> Run all eligible agents in parallel (max throughput)
  |     |
  |     |-- Do tasks share any files?
  |           YES --> Group by file dependency, parallelize groups
  |           NO  --> Full parallel execution
  |
  |-- NO (tasks have sequential dependencies)
  |     |
  |     |-- Is there a critical path?
  |     |     YES --> Serialize the critical path, parallelize everything else
  |     |     NO  --> Full serial execution (pipeline pattern)
  |     |
  |     |-- Can the dependency be broken by defining interfaces first?
  |           YES --> Interface-first pattern (define contracts, then parallelize)
  |           NO  --> Serial execution is required
  |
  |-- MIXED (some parallel, some serial)
        --> Use phased execution (see below)
```

### Execution Patterns

**Pattern 1: Full Parallel**
```
Time -->
Agent A: [==========]
Agent B: [==========]
Agent C: [==========]
Agent D: [==========]

Best when: Tasks are fully independent (e.g., writing tests for different modules)
Speedup: ~Nx (where N = number of agents)
Risk: Merge conflicts if agents touch shared files
```

**Pattern 2: Pipeline (Serial)**
```
Time -->
Agent A: [=====]
Agent B:       [=====]
Agent C:             [=====]

Best when: Each step depends on the previous (spec -> implement -> test)
Speedup: None (sequential)
Benefit: Each agent builds on verified output from the previous
```

**Pattern 3: Phased Parallel**
```
Time -->
Phase 1:  Agent A: [=====]  (architecture/planning)
Phase 2:  Agent B: [=====]  Agent C: [=====]  (parallel implementation)
Phase 3:  Agent D: [=====]  (integration/testing)

Best when: Some tasks can parallelize after initial setup
Speedup: Moderate (parallel in the middle)
Benefit: Combines the safety of serial with the speed of parallel
```

**Pattern 4: Fan-Out / Fan-In**
```
Time -->
              Agent B: [====]
Agent A: [==]  Agent C: [====]  Agent E: [===]
              Agent D: [====]

Best when: One agent creates work items, many execute, one integrates
Example: Orchestrator assigns tasks, developers implement, reviewer integrates
```

### File Conflict Prevention

When agents run in parallel, file conflicts are the primary risk.

**Strategies:**
1. **File ownership**: Assign specific files or directories to specific agents. No agent writes to another agent's files.
2. **Interface contracts**: Define shared interfaces first (types, API contracts), then let agents implement independently.
3. **Branch-per-agent**: Each agent works on a git branch, with a merge agent handling integration.
4. **Lock files**: Use a shared state lock to prevent simultaneous writes to the same file.

```yaml
# File ownership configuration
parallel_execution:
  file_ownership:
    backend-dev:
      owns: ["src/api/**", "src/services/**", "src/db/**"]
    frontend-dev:
      owns: ["src/components/**", "src/pages/**", "src/styles/**"]
    test-engineer:
      owns: ["tests/**", "fixtures/**"]
    shared_files:
      # These files require coordination — only one agent writes at a time
      locked: ["src/types/index.ts", "package.json", "tsconfig.json"]
```

## Decision 4: Budget Allocation

### Budget Allocation Models

**Model 1: Role-Based Allocation (Recommended for most teams)**

Allocate based on the importance and cost profile of each role:

| Role | Budget Share | Rationale |
|---|---|---|
| Orchestrator | 15-25% | High model cost (Opus) but fewer sessions |
| Primary Developer(s) | 35-45% | Most sessions, medium model cost (Sonnet) |
| Reviewer | 10-15% | Fewer sessions, medium-high model cost |
| Tester(s) | 10-15% | Many sessions but cheapest model (Haiku) |
| Buffer | 10-15% | For retries, escalations, and unexpected work |

**Example**: $50 budget for a full-stack feature:
- Orchestrator (Opus): $10
- Backend Dev (Sonnet): $12
- Frontend Dev (Sonnet): $12
- Reviewer (Sonnet): $5
- Test Writer (Haiku): $4
- Buffer: $7

**Model 2: Phase-Based Allocation**

Allocate by project phase rather than role:

| Phase | Budget Share | Activities |
|---|---|---|
| Planning | 15-20% | Architecture, specification, task breakdown |
| Implementation | 45-55% | Coding, building, integrating |
| Review & Testing | 20-25% | Code review, testing, QA |
| Buffer | 10-15% | Rework, escalation, unexpected issues |

**Model 3: Fixed-Cost-Per-Agent**

Set a hard cost cap per agent. Simple but less flexible.

```yaml
budget:
  strategy: per_agent_cap
  default_cap: 5.00
  overrides:
    orchestrator: 10.00
    test-writer: 2.00
  total_cap: 50.00
  alert_at: 40.00
```

### Budget Monitoring

```yaml
budget_monitoring:
  track_by: ["agent", "model", "phase"]
  alerts:
    - threshold: 50%
      action: "log_warning"
    - threshold: 75%
      action: "notify_user"
    - threshold: 90%
      action: "restrict_to_haiku_only"
    - threshold: 100%
      action: "halt_all_agents"
  reporting:
    interval: "per_session"
    format: "cost_breakdown_by_agent"
```

## Putting It All Together: Example Decisions

### Scenario: "Build a REST API for user management"

```
1. Team Selection:
   - Goal: Build a new feature --> focused team (backend-only)
   - No frontend needed
   - Specification exists
   --> "focused-backend" team

2. Agent Count:
   - Moderate complexity (5-10 files)
   - Quality matters (user-facing API)
   --> 4 agents: coordinator + developer + tester + reviewer

3. Execution Strategy:
   - Coordinator plans first (serial)
   - Developer implements (serial after planning)
   - Tester writes tests in parallel with late development
   - Reviewer reviews after implementation
   --> Phased execution

4. Budget:
   - Total: $15
   - Coordinator (Sonnet, not Opus — straightforward project): $3
   - Developer (Sonnet): $5
   - Tester (Haiku): $2
   - Reviewer (Sonnet): $3
   - Buffer: $2
```

### Scenario: "Migrate from REST to GraphQL across the full stack"

```
1. Team Selection:
   - Goal: Refactoring/migration of existing codebase
   - Full-stack (frontend + backend)
   --> "refactoring" team, full-stack variant

2. Agent Count:
   - High complexity (40+ files)
   - Multiple concerns (API, schema, client, tests)
   --> 6 agents: orchestrator + architect + 2 developers + tester + reviewer

3. Execution Strategy:
   - Phase 1: Architect designs schema + orchestrator plans (serial)
   - Phase 2: Backend dev + frontend dev implement in parallel
   - Phase 3: Tester validates + reviewer reviews (parallel)
   --> Phased parallel with 3 phases

4. Budget:
   - Total: $50
   - Orchestrator (Opus): $10
   - Architect (Opus, planning phase only): $8
   - Backend Dev (Sonnet): $10
   - Frontend Dev (Sonnet): $10
   - Tester (Haiku): $3
   - Reviewer (Sonnet): $5
   - Buffer: $4
```

### Scenario: "Fix a performance bug in the search endpoint"

```
1. Team Selection:
   - Goal: Bug fix on existing codebase
   --> "maintenance" team

2. Agent Count:
   - Narrow scope (1-3 files likely)
   - Needs investigation first
   --> 2 agents: debugger/fixer + test writer
     (or even 1 agent if budget is very tight)

3. Execution Strategy:
   - Debugger investigates and fixes (serial)
   - Test writer adds regression test after fix
   --> Pipeline (serial)

4. Budget:
   - Total: $5
   - Debugger (Sonnet): $3
   - Test Writer (Haiku): $1
   - Buffer: $1
```

## Quick Decision Checklist

Use this checklist before launching any Sforza team:

```
[ ] Have I identified the project goal clearly?
[ ] Have I selected the appropriate team template?
[ ] Have I determined the right number of agents?
    [ ] Not too few (missing roles like testing/review)?
    [ ] Not too many (coordination overhead > 30%)?
[ ] Have I chosen the execution strategy?
    [ ] Identified parallel vs. serial task dependencies?
    [ ] Set up file ownership for parallel agents?
[ ] Have I allocated the budget?
    [ ] Assigned models appropriate to each role?
    [ ] Set per-agent and total budget caps?
    [ ] Included a 10-15% buffer?
[ ] Have I configured monitoring?
    [ ] Budget alerts set?
    [ ] Quality checkpoints defined?
    [ ] Human review points identified?
```

## Recommendations

### For first-time Sforza users
Start with a 3-agent team: one Sonnet coordinator, one Sonnet developer, and one Haiku tester. Run in pipeline (serial) mode. This is simple, predictable, and teaches you how Sforza works before you scale up.

### For maximizing speed
Use phased parallel execution with file ownership. Run the orchestrator first (5 minutes), then fan out to 3-4 parallel developers, then fan in for review. This achieves near-linear speedup on parallelizable work.

### For maximizing quality
Add a dedicated reviewer agent (Opus or Sonnet) that reviews every piece of output before it merges. Use the multi-agent review pattern from the Quality Assurance guide. Quality is worth the extra 10-15% cost.

### For minimizing cost
Use the minimum viable team (2 agents). Run Sonnet for implementation and Haiku for testing. Skip the orchestrator — manage the workflow yourself. Use prompt caching aggressively.

### For enterprise projects
Use sub-teams with a master orchestrator. Each sub-team has 3-5 agents with its own coordinator. The master orchestrator (Opus) assigns work to sub-teams and integrates results. This scales to 15-20+ agents without overwhelming coordination overhead.

## Related Resources

- [Model Selection Guide](./model-selection-guide.md) — Detailed guidance on which model for each role
- [Harness Comparison](./harness-comparison.md) — Choosing the right harness for each agent
- [Optimization Guide](./optimization-guide.md) — Cost and performance optimization techniques
- [Long-Running Agents](./long-running-agents.md) — Managing agents across multiple sessions
- [Quality Assurance](./quality-assurance.md) — Multi-agent review and validation patterns
