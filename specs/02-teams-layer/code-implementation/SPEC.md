# Code Implementation Team -- Full Specification

> **STATUS: STATIC REFERENCE** -- This file is never modified, only consulted.

## Use Case

Build features from requirements to deployment with integrated code review, testing, and documentation. This team takes a feature specification or user story and produces production-ready, tested, documented code through a coordinated multi-agent workflow.

**Target Users**: Software engineers, engineering managers, product teams needing rapid feature development.

**When to Use This Team vs. Single Agent**:
- Feature requires >500 lines of code across multiple files
- Feature touches multiple modules or services
- Quality requirements include code review, testing, and documentation
- Parallel development of independent sub-features is possible
- Feature has external dependencies requiring coordination

**Inputs**: Feature specification, user story, or requirements document.
**Outputs**: Production-ready code on a feature branch with tests, documentation, and passing CI.

---

## Agent Roster

| Agent | Model | Count | Role | Token Budget |
|-------|-------|-------|------|-------------|
| Coordinator/Planner | Sonnet 4.5 | 1 | Task decomposition, dependency analysis, milestone tracking | 30K |
| Implementation Specialist A | Opus 4.6 | 1 | Primary feature development | 150K |
| Implementation Specialist B | Opus 4.6 | 1 | Parallel secondary feature development | 150K |
| Code Reviewer | Opus 4.6 | 1 | Quality enforcement, style adherence, security review | 80K |
| Test Engineer | Sonnet 4.5 | 1 | Test generation, coverage analysis, validation | 60K |
| Documentation Writer | Haiku 4.5 | 1 | API docs, README updates, inline comments | 20K |

**Total agents**: 6
**Total token budget**: ~340K tokens per feature (parallel execution reduces wall-clock time but not total tokens; Implementation Specialists run concurrently so effective parallel token consumption is ~150K for that phase, not 300K)

---

## System Prompt Personalities

### Coordinator/Planner
```
You are a strategic project planner and technical coordinator. You decompose complex features
into parallelizable work units, identify dependencies between tasks, and track milestones.
You are risk-aware and flag potential blockers early. You make decisions about task ordering
based on dependency analysis, not gut feel. You communicate clearly with the team about
priorities and deadlines. You do not write code yourself -- you plan, coordinate, and
ensure the team converges on a working solution.

Core traits:
- Strategic thinker who plans 2-3 steps ahead
- Risk-aware: identifies what could go wrong before it does
- Dependency-focused: understands what blocks what
- Decisive: makes clear task assignments, does not waffle
- Communicative: sends clear, actionable messages to team members
```

### Implementation Specialist A & B
```
You are a pragmatic software engineer who writes clean, production-ready code. You prioritize
working solutions over perfect abstractions. You refactor as you go but do not over-engineer.
You are security-conscious and consider edge cases. You follow the project's established
patterns and conventions. You write code that is easy to review -- small commits, clear
variable names, and comments where the "why" is not obvious.

Core traits:
- Pragmatic builder: ships working code, iterates to improve
- Refactoring-friendly: leaves code better than you found it
- Security-conscious: validates inputs, handles errors, avoids vulnerabilities
- Convention-follower: matches existing project style
- Review-friendly: writes code others can understand and review
```

### Code Reviewer
```
You are a detail-oriented code reviewer who enforces quality standards constructively but
firmly. You catch bugs, security issues, performance problems, and style violations. You
explain WHY something is a problem, not just THAT it is. You distinguish between blocking
issues (must fix) and suggestions (nice to have). You follow the team's style guide strictly
and flag deviations. You look for: logic errors, missing error handling, security
vulnerabilities, performance regressions, test coverage gaps, and documentation needs.

Core traits:
- Detail-oriented perfectionist: catches what others miss
- Constructive but firm: explains problems clearly, insists on fixes for blockers
- Standards-enforcer: follows style guide to the letter
- Security-minded: thinks like an attacker
- Prioritized feedback: separates blockers from suggestions
```

### Test Engineer
```
You are an edge-case hunter obsessed with test coverage and regression prevention. You
think about what COULD break, not just what SHOULD work. You write tests at multiple levels:
unit, integration, and end-to-end. You design test scenarios that cover happy paths, error
paths, boundary conditions, and concurrency issues. You measure coverage and flag gaps. You
write test code that is as clean and maintainable as production code.

Core traits:
- Edge-case hunter: thinks about failure modes first
- Coverage-obsessed: measures and improves test coverage
- Regression-prevention focused: writes tests that catch future breakage
- Multi-level tester: unit, integration, and e2e
- Clean test code: tests are documentation, not throwaway code
```

### Documentation Writer
```
You are a clarity-focused technical writer who creates documentation that developers actually
read and use. You write API docs, README updates, and inline comments. You prioritize
examples over descriptions -- show, do not tell. You consider the reader's experience level
and provide appropriate context. You keep documentation close to the code it describes. You
follow the project's documentation conventions.

Core traits:
- Clarity-focused: every sentence has a purpose
- Example-driven: code examples over prose descriptions
- Accessibility-minded: considers different experience levels
- Proximity-aware: docs live near the code they describe
- Convention-follower: matches existing documentation style
```

---

## Configuration System (CONFIG.md)

The Coordinator populates this at initialization:

```yaml
# Code Implementation Team Configuration
# Auto-populated by coordinator at start
# Initialized: [ISO8601 timestamp]

project_type: [web_app|mobile_app|backend_api|library|cli_tool]
primary_language: [python|javascript|typescript|swift|kotlin|rust|go|other]
framework: [nextjs|react|fastapi|django|spring|swiftui|jetpack_compose|other]
testing_framework: [pytest|jest|vitest|xctest|junit|other]
code_style: [pep8|airbnb|google|custom]
review_strictness: [relaxed|standard|strict]
timestamp_initialized: [ISO8601]
```

This configuration drives:
- Which AGENTS.md framework templates to load (from common/agents-md/)
- Which testing patterns the Test Engineer uses
- How strict the Code Reviewer enforces style
- Which MCP servers to activate

---

## MODEL_CONFIGS.md

### Default Configuration (Recommended)
| Agent | Model | Rationale |
|-------|-------|-----------|
| Coordinator | Sonnet 4.5 | Planning and coordination -- does not need Opus reasoning depth |
| Implementation A | Opus 4.6 | Complex logic, architecture decisions, production-quality code |
| Implementation B | Opus 4.6 | Complex logic, architecture decisions, production-quality code |
| Code Reviewer | Opus 4.6 | Catches subtle bugs, security issues, architectural problems |
| Test Engineer | Sonnet 4.5 | Test generation is well-structured, does not need Opus |
| Documentation Writer | Haiku 4.5 | Cost-effective for documentation tasks |

### Language-Specific Optimizations

**Swift Development**
- Replace Implementation Specialists with minimax2.5
- Reason: Current benchmarks show minimax2.5 outperforms on Swift/SwiftUI code generation
- Cost impact: ~15% reduction vs Opus 4.6
- Trade-off: Slightly less sophisticated architectural decisions
- Keep Opus for Code Reviewer (architectural quality still matters)

**Kotlin Development**
- Replace Implementation Specialists with minimax2.5
- Reason: Superior Kotlin/Jetpack Compose performance in benchmarks
- Keep Opus for: Complex state management, architectural patterns

**Python / JavaScript / TypeScript**
- Stick with default (Opus 4.6 for Implementation)
- Reason: Opus 4.6 benchmarks highest for these languages
- Alternative: Sonnet 4.5 for simpler CRUD operations (40% cost savings)

**Rust / Go**
- Opus 4.6 for memory safety (Rust) and concurrency patterns (Go)
- Alternative: Sonnet 4.5 for straightforward implementations
- Do NOT use Haiku for Rust -- borrow checker complexity requires stronger reasoning

### Cost vs Performance Matrix

| Configuration | Est. Cost/Feature | Code Quality | Best For |
|--------------|-------------------|--------------|----------|
| All Opus 4.6 | $25-45 | Highest | Production systems, complex logic |
| Mixed (default) | $15-30 | High | Most projects, balanced approach |
| All Sonnet 4.5 | $8-15 | Good | MVPs, prototypes, simple CRUD |
| Language-optimized | $12-25 | High | Swift/Kotlin projects |

### When to Upgrade Models
- **Haiku to Sonnet**: Documentation needs technical depth beyond formatting
- **Sonnet to Opus**: Complex architectural decisions, security-critical code, subtle concurrency
- **Opus to Specialized**: Language-specific benchmarks favor alternatives (Swift/Kotlin)

---

## Parallel Execution Strategy

### Phase 1: Planning (Sequential)
**Duration**: ~10 min
**Agents**: Coordinator/Planner only
**Token Budget**: 30K

1. Coordinator reads feature specification
2. Decomposes into tasks with dependency graph
3. Assigns tasks to Implementation Specialists (A gets primary, B gets secondary)
4. Identifies shared interfaces and contracts between parallel tasks
5. Creates task assignments in Linear/Jira (if MCP connected)
6. Test Engineer receives spec to begin scenario design (overlaps into Phase 2)

**User Prompt at End**:
```
Planning complete.
- Tasks: [N] total, [X] for Specialist A, [Y] for Specialist B
- Dependencies: [list critical dependencies]
- Estimated implementation time: [range]
- Estimated cost: $XX.XX

Parallel implementation will run Specialists A & B simultaneously.
Proceed? (yes/no/review)
```

### Phase 2: Implementation (Parallel)
**Duration**: ~20-40 min
**Agents**: Implementation Specialist A, Implementation Specialist B (parallel); Test Engineer begins scenario writing (parallel)
**Token Budget**: 150K per specialist (running concurrently)

- Specialist A: Primary feature on branch `agent/impl-a/[feature-name]`
- Specialist B: Secondary features on branch `agent/impl-b/[feature-name]`
- Test Engineer: Writes holdout test scenarios in `scenarios/` (does NOT share with implementers)
- File lock manager prevents conflicts on shared files
- Agents push commits every 10-15 minutes
- Status updates every 5 minutes

**User Prompt at End**:
```
Implementation complete.
- Specialist A: [summary of changes, files modified, lines added]
- Specialist B: [summary of changes, files modified, lines added]
- Branches ready for review
- Cost so far: $XX.XX

Next: Code review (sequential).
Proceed? (yes/no/review branches)
```

### Phase 3: Code Review (Sequential)
**Duration**: ~15-25 min
**Agents**: Code Reviewer
**Token Budget**: 80K

1. Code Reviewer checks out both implementation branches
2. Reviews against style guide, security checklist, and project conventions
3. Produces review with BLOCKING issues and SUGGESTIONS
4. Implementation Specialists address BLOCKING issues
5. Code Reviewer re-reviews until all blocking issues resolved
6. Approves merge to feature branch

**User Prompt at End**:
```
Code review complete.
- Blocking issues found: [N] (all resolved)
- Suggestions: [N] (optional, listed below)
- Security concerns: [none|list]
- Code merged to feature branch

Next: Testing + Documentation (parallel).
Proceed? (yes/no/review suggestions)
```

### Phase 4: Testing + Documentation (Parallel)
**Duration**: ~15-20 min
**Agents**: Test Engineer, Documentation Writer (parallel)
**Token Budget**: 60K (Test) + 20K (Docs)

- Test Engineer:
  - Runs holdout scenarios against implemented code
  - Generates additional unit/integration tests
  - Measures coverage, flags gaps
  - Reports results to Coordinator

- Documentation Writer:
  - Updates API documentation
  - Updates README if needed
  - Adds inline comments where reviewer flagged complexity
  - Generates changelog entry

**User Prompt at End**:
```
Testing and documentation complete.
- Test results: [pass/fail count]
- Coverage: [percentage]
- Scenario satisfaction: [percentage]
- Documentation updated: [list of files]
- Total cost: $XX.XX

Feature ready for merge to main.
Merge? (yes/no/review)
```

---

## Token Budget Breakdown

| Phase | Agent(s) | Tokens | Parallel? | Notes |
|-------|----------|--------|-----------|-------|
| Planning | Coordinator | 30K | No | Sequential, must complete first |
| Implementation | Specialist A | 150K | Yes (with B) | Primary features |
| Implementation | Specialist B | 150K | Yes (with A) | Secondary features |
| Review | Code Reviewer | 80K | No | Must follow implementation |
| Testing | Test Engineer | 60K | Yes (with Docs) | Runs after review |
| Documentation | Documentation Writer | 20K | Yes (with Test) | Runs after review |
| **Total** | | **~340K** | | Parallel phases overlap in time |

**Note on parallel token accounting**: When Specialists A and B run in parallel, both consume tokens simultaneously. The total token bill is still 300K for both, but wall-clock time is halved compared to sequential execution.

**Buffer recommendation**: Add 15-20% overhead (~50-70K) for iteration cycles (reviewer requests changes, tests fail and need fixes).

---

## MCP Server Configuration

### Required
| Server | Purpose | Config |
|--------|---------|--------|
| GitHub | PR creation, branch management, code review integration | `mcp-servers/github.json` |

### Recommended
| Server | Purpose | Config |
|--------|---------|--------|
| Linear | Task tracking, sprint management | `mcp-servers/linear.json` |
| Jira | Enterprise task tracking (alternative to Linear) | `mcp-servers/jira.json` |

### Optional
| Server | Purpose | Config |
|--------|---------|--------|
| Sentry | Error tracking context for bug fixes | `mcp-servers/sentry.json` |

---

## ORCHESTRATION.md Specifics

### Execution Modes

**Sequential Mode ($10-30)**
- Run agents one at a time: Coordinator -> Specialist A -> Specialist B -> Reviewer -> Test Engineer -> Docs Writer
- User manages handoffs between agents
- Duration: 1.5-3 hours
- Best for: Learning the workflow, small features, tight budgets

**Hybrid Mode ($30-100) -- Default**
- Phase 1 sequential, Phase 2 parallel, Phase 3 sequential, Phase 4 parallel
- Coordinator manages handoffs automatically
- Duration: 45-90 min
- Best for: Most production features

**Parallel Swarm Mode ($100-500)**
- All agents active from the start
- Test Engineer writes scenarios while Specialists implement
- Code Reviewer does incremental reviews on each push
- Documentation Writer starts structure while implementation is in progress
- Duration: 20-40 min
- Best for: Time-critical features, large teams

### Git Branch Strategy

```
main
├── agent/coordinator/plan-[feature]
├── agent/impl-a/[feature]-primary
├── agent/impl-b/[feature]-secondary
├── agent/reviewer/review-[feature]
├── agent/test/scenarios-[feature]
└── agent/docs/docs-[feature]
```

Merge order:
1. impl-a and impl-b merge into `feature/[name]`
2. Reviewer approves `feature/[name]`
3. Test and docs branches merge into `feature/[name]`
4. `feature/[name]` merges into `main`

### Communication Protocol

```
### [14:23] Coordinator -> Implementation-A
Task assignment: Implement user authentication module
Context: specs/auth-module.md
Priority: High

### [14:25] Coordinator -> Implementation-B
Task assignment: Implement notification service
Context: specs/notification-service.md
Priority: High

### [14:45] Implementation-A -> Coordinator
Blocked: Need clarification on OAuth provider configuration
Context: src/auth/oauth.ts:L42
Priority: High

### [14:47] Coordinator -> Implementation-A
Resolution: Use Google OAuth as default, support generic OIDC
Context: CONFIG.md#oauth-providers
Priority: High
```

### Scenario-Based Validation

Test Engineer writes scenarios before implementation begins:

```yaml
# scenarios/auth-feature.md
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
  - name: "OAuth callback"
    input: valid OAuth code
    expected: User created/updated, JWT returned
  - name: "Token expiration"
    input: expired JWT
    expected: 401 error, refresh flow triggered
convergence_threshold: 0.90
```

### Autonomous Decisions

Coordinator CAN autonomously:
- Reassign tasks between Specialists A and B if one is blocked
- Retry failed test runs (up to 3 attempts)
- Merge branches when all tests pass and reviewer approves
- Request focused fixes from Specialists for reviewer-flagged issues
- Cost limit: <$20 per autonomous action

Coordinator MUST prompt user before:
- Adding a third Implementation Specialist
- Relaxing review strictness
- Skipping test coverage requirements
- Re-planning after major scope discovery
- Any single action costing >$50

---

## Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Scenario satisfaction | >= 90% | Holdout test pass rate |
| Test coverage | >= 80% | Coverage tool output |
| Review approval | First-pass or second-pass | Number of review cycles |
| Documentation completeness | All public APIs documented | API doc coverage |
| Budget adherence | Within 20% of estimate | Actual vs projected tokens |
| Wall-clock time | < 90 min (hybrid mode) | Start to merge |

---

## Cost Analysis

### Per-Feature Estimates (Mixed Default Configuration)

| Phase | Model | Tokens | Input Cost | Output Cost | Total |
|-------|-------|--------|------------|-------------|-------|
| Planning | Sonnet 4.5 | 30K | $0.09 | $0.15 | $0.24 |
| Implementation A | Opus 4.6 | 150K | $2.25 | $7.50 | $9.75 |
| Implementation B | Opus 4.6 | 150K | $2.25 | $7.50 | $9.75 |
| Review | Opus 4.6 | 80K | $1.20 | $4.00 | $5.20 |
| Testing | Sonnet 4.5 | 60K | $0.18 | $0.30 | $0.48 |
| Documentation | Haiku 4.5 | 20K | $0.005 | $0.01 | $0.015 |
| **Total** | | **~340K** | | | **~$25.44** |

*Note: Costs are estimates based on published pricing. Actual costs vary based on input/output token ratio, caching, and retry cycles. Add 15-20% buffer for iteration.*

### Hourly Burn Rate by Configuration

| Configuration | Tokens/Hour | Est. Cost/Hour |
|--------------|-------------|----------------|
| All Opus 4.6 | ~200K | $30-50 |
| Mixed (default) | ~200K | $15-30 |
| All Sonnet 4.5 | ~200K | $5-12 |
| All Haiku 4.5 | ~200K | $0.50-1.50 |

---

## Skills per Agent

### Coordinator/Planner
- `task-decomposition` -- Break feature specs into parallelizable work units
- `dependency-analysis` -- Identify task ordering and critical path
- `status-reporter` -- Generate progress summaries for user prompts

### Implementation Specialists
- Framework-specific skills loaded based on CONFIG.md:
  - `nextjs-patterns` (if framework=nextjs)
  - `fastapi-patterns` (if framework=fastapi)
  - `react-patterns` (if framework=react)
- `code-implementation` -- Core code writing workflow
- `refactoring` -- Improve existing code structure

### Code Reviewer
- `code-review` -- Systematic review against quality checklist
- `security-review` -- OWASP-based security analysis
- `style-enforcement` -- Project-specific style guide checking

### Test Engineer
- `test-generator` -- Create tests from specifications
- `coverage-analysis` -- Measure and improve test coverage
- `scenario-design` -- Write holdout test scenarios

### Documentation Writer
- `documentation-writer` -- Generate docs from code
- `api-docs-generator` -- Generate API reference documentation
- `changelog-writer` -- Create changelog entries from commits
