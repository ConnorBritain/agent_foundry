# Multi-Agent Orchestration Protocol

This document defines the execution phases, communication protocols, quality gates, and decision-making framework for the Code Implementation Team.

---

## Execution Modes

The team supports three execution modes. The mode is selected at runtime via the `--mode` flag.

### Sequential Mode

Agents execute one at a time in a defined order. Slowest but most predictable. Recommended for first-time users or debugging.

```
Coordinator → Specialist A → Specialist B → Code Reviewer → Test Engineer → Doc Writer
```

**Total time:** ~1.5-3 hours
**When to use:** First run, debugging, small features, tight budgets.

### Hybrid Mode (Recommended)

Agents execute in parallel within phases but sequentially across phases. Quality gates between phases ensure coherence.

```
Phase 1 (sequential):  Coordinator
  ↓ [User Prompt]
Phase 2 (parallel):    Specialist A + Specialist B + Test Engineer (scenario writing)
  ↓ [User Prompt]
Phase 3 (sequential):  Code Reviewer
  ↓ [User Prompt]
Phase 4 (parallel):    Test Engineer (execution) + Documentation Writer
  ↓ [User Prompt / Merge Decision]
```

**Total time:** ~45-90 minutes
**When to use:** Most features. Best balance of speed and reliability.

### Swarm Mode

All agents active from the start. Fastest but highest risk of conflicts and wasted tokens from retries.

```
All agents run concurrently:
- Coordinator plans while Test Engineer designs scenarios
- Specialists begin implementation as soon as tasks are assigned
- Code Reviewer does incremental reviews on each push
- Doc Writer starts structure while implementation is in progress
```

**Total time:** ~20-40 minutes
**When to use:** Time-critical features, experienced users, well-defined scope.
**Warning:** Higher token waste from context drift and conflict resolution.

---

## Phase Definitions

### Phase 1: Planning (Sequential -- ~10 minutes)

**Goal:** Decompose the feature into parallelizable work units and assign tasks.

#### Coordinator / Planner
- Read and parse the feature specification from CONFIG
- Analyze the existing codebase structure and conventions
- Decompose the feature into tasks with dependency graph
- Assign tasks to Specialists (A gets primary/critical path, B gets secondary/independent)
- Identify shared interfaces and contracts between parallel tasks
- Define file ownership to prevent merge conflicts
- Estimate implementation time and cost

**Outputs:**
- Task list with dependencies
- Specialist assignments with acceptance criteria
- Shared interface definitions
- File ownership map

#### Quality Gate 1: Planning Checkpoint

**User Prompt at End:**
```
Planning complete.
- Tasks: [N] total, [X] for Specialist A, [Y] for Specialist B
- Dependencies: [list critical dependencies]
- Shared interfaces: [list contracts between Specialists]
- Estimated implementation time: [range]
- Estimated cost: $XX.XX

Parallel implementation will run Specialists A & B simultaneously.
Proceed? (yes/no/review)
```

---

### Phase 2: Implementation (Parallel -- ~20-40 minutes)

**Goal:** Build the feature code on parallel branches.

#### Implementation Specialist A
- Create branch `agent/impl-a/[feature-name]`
- Implement primary feature tasks per Coordinator's assignment
- Follow project conventions and style guide
- Push commits every 10-15 minutes
- Send status updates every 5 minutes

#### Implementation Specialist B
- Create branch `agent/impl-b/[feature-name]`
- Implement secondary feature tasks per Coordinator's assignment
- Coordinate with Specialist A through shared interfaces
- Push commits every 10-15 minutes
- Send status updates every 5 minutes

#### Test Engineer (Parallel -- Scenario Writing)
- Write holdout test scenarios in `scenarios/` directory
- Design test cases covering happy paths, error paths, and edge cases
- Do NOT share scenarios with Implementation Specialists (holdout principle)
- Prepare test harness and fixtures

**File Lock Manager:** Prevents conflicts on shared files. Each Specialist writes only to their assigned directories. Shared files (e.g., route definitions, type exports) are owned by one Specialist as assigned by the Coordinator.

#### Quality Gate 2: Implementation Checkpoint

**User Prompt at End:**
```
Implementation complete.
- Specialist A: [summary of changes, files modified, lines added]
- Specialist B: [summary of changes, files modified, lines added]
- Branches ready for review
- Cost so far: $XX.XX

Next: Code review (sequential).
Proceed? (yes/no/review branches)
```

---

### Phase 3: Code Review (Sequential -- ~15-25 minutes)

**Goal:** Enforce quality standards and resolve issues before testing.

#### Code Reviewer
1. Check out both implementation branches
2. Review against: style guide, security checklist, project conventions
3. Categorize findings as BLOCKER or SUGGESTION
4. Send review to Specialists with specific file and line references
5. Specialists address BLOCKER issues and push fixes
6. Re-review until all blockers resolved (max 3 cycles per CONFIG)
7. Approve merge: both branches merge into `feature/[name]`

**Review Checklist:**
- Logic errors and correctness
- Missing error handling
- Security vulnerabilities (injection, auth bypass, data leaks)
- Performance regressions (N+1 queries, unbounded loops, large allocations)
- Style guide compliance
- Test coverage gaps
- Documentation needs

#### Quality Gate 3: Review Checkpoint

**User Prompt at End:**
```
Code review complete.
- Blocking issues found: [N] (all resolved)
- Suggestions: [N] (optional, listed below)
- Security concerns: [none|list]
- Code merged to feature branch

Next: Testing + Documentation (parallel).
Proceed? (yes/no/review suggestions)
```

---

### Phase 4: Testing + Documentation (Parallel -- ~15-20 minutes)

**Goal:** Validate the implementation and produce documentation.

#### Test Engineer
- Run holdout scenarios against the implemented feature branch
- Generate additional unit and integration tests for uncovered paths
- Measure test coverage and flag gaps below threshold
- Run the project's CI commands (lint, typecheck, test, build)
- Report results to Coordinator

#### Documentation Writer
- Update API documentation for new or modified endpoints
- Update README if setup, usage, or configuration changed
- Add inline comments where the Code Reviewer flagged complexity
- Generate a changelog entry following project conventions

#### Quality Gate 4: Merge Decision

**User Prompt at End:**
```
Testing and documentation complete.
- Test results: [pass/fail count]
- Coverage: [percentage]
- Holdout scenario satisfaction: [percentage]
- CI status: [pass/fail]
- Documentation updated: [list of files]
- Total cost: $XX.XX

Feature ready for merge to [default_branch].
Merge? (yes/no/review)
```

---

## Communication Protocol

### Message Types

| Type | Purpose | Example |
|------|---------|---------|
| `TASK` | Assign work to an agent | Coordinator assigns auth module to Specialist A |
| `STATUS` | Progress update | Specialist A reports 3/5 tasks complete |
| `BLOCKED` | Report a blocker | Specialist B needs interface definition |
| `QUERY` | Ask another agent for information | Reviewer asks Specialist A about design choice |
| `RESPONSE` | Answer a query | Specialist A explains design rationale |
| `REVIEW` | Code review findings | Reviewer sends categorized findings |
| `FIX` | Address a review finding | Specialist A pushes fix for blocker |
| `GATE` | Quality gate result | Coordinator reports Phase 2: PASS |
| `ESCALATE` | Escalate to user | Coordinator flags ambiguous requirement |

### Message Format

```yaml
type: TASK
from: coordinator
to: impl-specialist-a
phase: 2
priority: high
subject: "Implement user authentication module"
body: |
  Implement the authentication module per the spec in specs/auth-module.md.
  Files to create/modify:
  - src/auth/login.ts (new)
  - src/auth/middleware.ts (new)
  - src/routes/auth.ts (modify)
  Shared interface: Use AuthResult type from types/shared.ts
acceptance_criteria:
  - Login endpoint returns JWT on valid credentials
  - Middleware rejects expired tokens with 401
  - Rate limiting on login attempts (5 per minute)
deadline: "Phase 2 completion"
```

### Conflict Resolution

When Specialists need to modify the same file:
1. The Coordinator assigns file ownership in Phase 1
2. If a conflict arises, the owning Specialist makes the change
3. The non-owning Specialist requests the change via a `QUERY` message
4. If unresolved, the Coordinator decides and records the decision

---

## Git Branch Strategy

```
main (or default_branch from CONFIG)
├── agent/impl-a/[feature]-primary
├── agent/impl-b/[feature]-secondary
└── feature/[feature-name]           ← merge target for both impl branches
```

Merge order:
1. `agent/impl-a/*` and `agent/impl-b/*` merge into `feature/[name]`
2. Code Reviewer approves `feature/[name]`
3. Test and doc changes commit to `feature/[name]`
4. `feature/[name]` is ready for PR to `main`

### Commit Convention

```
<type>(<scope>): <subject>

<body>

Agent: <agent-name>
Phase: <phase-number>
```

Types: `feat`, `fix`, `refactor`, `test`, `docs`, `chore`

---

## Autonomous vs User-Prompted Decisions

### Autonomous (No User Input Needed)

- Reassign tasks between Specialists if one is blocked
- Retry failed test runs (up to 3 attempts)
- Merge branches when all tests pass and reviewer approves
- Request focused fixes from Specialists for reviewer-flagged issues
- Cost limit: <$20 per autonomous action

### User-Prompted (Require User Input)

- **Scope change:** Feature is larger than estimated, requires re-planning
- **Ambiguous requirements:** Spec is unclear, multiple valid interpretations
- **Budget overrun:** Projected cost exceeds `max_total_cost_usd`
- **Review strictness relaxation:** Reviewer cannot approve after max cycles
- **Third Specialist needed:** Feature complexity warrants a third implementer
- **Any single action costing >$50**

---

## Scenario-Based Validation

The Test Engineer writes holdout scenarios before implementation. These scenarios are NOT shared with Implementation Specialists. After implementation, the Test Engineer runs these scenarios to validate the feature independently.

```yaml
scenario: "User Authentication Flow"
preconditions:
  - Database seeded with test users
  - OAuth provider mock configured
test_cases:
  - name: "Successful login"
    input: valid credentials
    expected: JWT token returned, session created
  - name: "Invalid password"
    input: wrong password
    expected: 401 error, no session, rate limit incremented
convergence_threshold: 0.90
```

Scenario satisfaction >= 90% is required for the merge decision.
