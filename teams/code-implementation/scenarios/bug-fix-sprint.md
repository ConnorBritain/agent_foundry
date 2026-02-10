# Scenario: Bug Fix Sprint -- Triaging and Fixing a Backlog of 20+ Bugs

## Context

A mature application has accumulated a backlog of 23 bug reports across GitHub Issues. Bugs range from UI glitches to data corruption edge cases. The team must triage, prioritize, and fix as many bugs as possible in a single sprint, producing a clean PR per bug or per logical group of related bugs.

This scenario repurposes the team for high-throughput bug fixing rather than feature development. The Coordinator acts as triage lead, and the Specialists work through bugs in priority order.

## Trigger

The Coordinator is given:
- A GitHub Issues label filter (e.g., `label:bug status:open`)
- A priority framework: P0 (data loss, security), P1 (broken feature), P2 (degraded experience), P3 (cosmetic)
- A time budget of 2 hours and cost budget of $60

## Team Configuration

| Agent | Model | Role in This Scenario |
|-------|-------|-----------------------|
| Coordinator | Sonnet 4.5 | Triage bugs, prioritize, assign to Specialists, track progress |
| Specialist A | Opus 4.6 | Fix P0 and P1 bugs (highest severity, complex root causes) |
| Specialist B | Opus 4.6 | Fix P2 bugs (moderate severity, parallel with Specialist A) |
| Code Reviewer | Sonnet 4.5 | Review each fix for correctness, regression risk, and side effects |
| Test Engineer | Sonnet 4.5 | Write regression tests for each fix, verify no regressions |
| DevOps Specialist | Sonnet 4.5 | Monitor CI pipeline health, assist with environment-specific bugs |

## Workflow

### Phase 1: Triage and Prioritization (~10 min)
- Coordinator fetches all open bug issues via GitHub MCP
- Reads each issue description, reproduction steps, and labels
- Classifies each bug by severity: P0 (3 bugs), P1 (5 bugs), P2 (8 bugs), P3 (7 bugs)
- Groups related bugs (e.g., three bugs all caused by the same missing null check)
- Assigns P0 and P1 bugs to Specialist A (critical path)
- Assigns P2 bugs to Specialist B (parallel)
- Defers P3 bugs unless time permits
- Estimates fix complexity for each bug (quick fix, medium, investigation needed)

### Phase 2: Parallel Bug Fixing (~60-80 min)
- **Specialist A:** Works through P0 and P1 bugs in priority order. Each fix is a separate commit referencing the issue number. For bugs requiring investigation, reads related code, identifies root cause, implements targeted fix.
- **Specialist B:** Works through P2 bugs in priority order. Groups related bugs into single fixes where appropriate. Focuses on clean, minimal changes that address the reported issue without introducing new risks.
- **Test Engineer:** Writes a regression test for each bug as it is fixed. Each test reproduces the original bug condition and verifies the fix resolves it.

### Phase 3: Review Cycle (~20-30 min)
- Code Reviewer reviews fixes in priority order (P0 first)
- For each fix, checks: Does it address the root cause (not just the symptom)? Does it introduce side effects? Is the change minimal and safe?
- Flags any fix that has regression risk or changes shared utilities
- Specialists address blockers on reviewed fixes before moving to next bug
- Reviewer approves fixes in batches

### Phase 4: Regression Testing and Closure (~15-20 min)
- Test Engineer runs full regression suite to verify no existing tests break
- Runs new regression tests to confirm all fixes hold
- Coordinator creates PRs grouped by severity (one PR for P0 fixes, one for P1, one for P2)
- Each PR description includes: bugs fixed (with issue links), root cause analysis, regression tests added
- Coordinator comments on each GitHub Issue with fix status and PR link

## Expected Outputs

- 12-18 bugs fixed (P0 through P2, P3 if time permits)
- One commit per bug or per related bug group, referencing issue numbers
- Regression test for each fix
- 2-3 pull requests grouped by severity
- Issue comments with fix status and PR links
- Triage report for unfixed P3 bugs with estimated effort

## Estimated Cost

| Configuration | Est. Tokens | Est. Cost | Est. Time |
|--------------|-------------|-----------|-----------|
| Budget (all Sonnet) | ~700K | ~$15 | ~2.5 hr |
| Default (mixed) | ~700K | ~$40 | ~2 hr |
| Premium (all Opus) | ~700K | ~$65 | ~1.5 hr |

Note: Bug fix sprints use approximately 1.4x the standard token budget due to the high number of context switches between bugs. Each bug requires reading the issue, understanding the relevant code, implementing the fix, and writing a regression test. The Default configuration is recommended -- Opus for Specialists is valuable because root cause analysis on complex bugs benefits from deep reasoning.
