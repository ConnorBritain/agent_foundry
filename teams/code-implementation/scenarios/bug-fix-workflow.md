# Scenario: Bug Fix Workflow

This scenario validates the team's ability to diagnose, fix, test, and document a bug reported in production or during development.

---

## Scenario Overview

| Property | Value |
|----------|-------|
| **Priority** | High |
| **Validated After** | Phase 4 |
| **Primary Agents** | Coordinator, Specialist A, Code Reviewer, Test Engineer |
| **Estimated Duration** | ~30-45 minutes (hybrid mode) |

---

## Success Path: Reported Bug with Reproduction Steps

### Preconditions

- Bug report includes reproduction steps, expected behavior, and actual behavior
- The bug is in an existing module within the codebase
- The bug affects a single code path (not a systemic issue)

### Steps

| Step | Action | Expected Outcome |
|------|--------|------------------|
| 1 | Coordinator reads bug report from feature spec | Bug decomposed into: root cause analysis, fix implementation, regression test |
| 2 | Coordinator assigns root cause analysis to Specialist A | Specialist A traces the code path to identify the defect |
| 3 | Specialist A identifies root cause and proposes fix | Fix description sent to Coordinator with affected files |
| 4 | Specialist A implements the fix on branch | Targeted fix with minimal code changes |
| 5 | Code Reviewer reviews the fix | Verifies fix addresses root cause without side effects |
| 6 | Test Engineer writes regression test | Test reproduces the original bug and verifies the fix |
| 7 | Test Engineer runs existing test suite | No regressions introduced by the fix |
| 8 | Doc Writer updates changelog | Bug fix entry in changelog |

### Validation Criteria

- [ ] Root cause identified and documented in commit message
- [ ] Fix is minimal (no unrelated changes)
- [ ] Regression test reproduces the original bug scenario
- [ ] Regression test passes with the fix applied
- [ ] Existing test suite passes (no regressions)
- [ ] Changelog entry describes the fix

---

## Success Path: Bug with Sentry Context

### Preconditions

- Sentry MCP server is enabled in CONFIG
- Bug report includes a Sentry error ID or link
- Sentry contains stack trace and error context

### Steps

| Step | Action | Expected Outcome |
|------|--------|------------------|
| 1 | Coordinator retrieves error context from Sentry | Stack trace, affected users, frequency, first/last occurrence |
| 2 | Coordinator assigns fix to Specialist A with Sentry context | Specialist has full error context for diagnosis |
| 3 | Specialist A traces the stack trace to root cause | Fix addresses the exact failure point |
| 4 | Review and testing proceed as normal | Same quality gates apply |

### Validation Criteria

- [ ] Sentry context used to inform the fix (mentioned in commit)
- [ ] Fix addresses the specific error type and stack trace
- [ ] Error path now handles the failure gracefully

---

## Edge Case: Bug Spans Multiple Modules

### Preconditions

- The bug involves interaction between two or more modules
- Fix requires changes in multiple files across different domains

### Steps

| Step | Action | Expected Outcome |
|------|--------|------------------|
| 1 | Coordinator decomposes fix across Specialists A and B | A fixes the primary module, B fixes the secondary module |
| 2 | Both Specialists implement fixes in parallel | Parallel branches as in standard feature workflow |
| 3 | Code Reviewer verifies the interaction between fixes | Cross-module integration validated |

### Validation Criteria

- [ ] Both modules fixed consistently
- [ ] Integration between modules tested
- [ ] No new interaction bugs introduced

---

## Edge Case: Bug Cannot Be Reproduced

### Preconditions

- Bug report lacks clear reproduction steps
- The defect is intermittent or environment-specific

### Steps

| Step | Action | Expected Outcome |
|------|--------|------------------|
| 1 | Coordinator analyzes bug report and codebase | Identifies likely code paths that could cause the reported behavior |
| 2 | Specialist A adds defensive checks and logging | Hardens the suspected code path |
| 3 | Test Engineer writes tests for suspected scenarios | Edge cases and race conditions covered |
| 4 | Coordinator escalates if root cause remains unclear | User informed that fix is defensive, not definitive |

### Validation Criteria

- [ ] Defensive fix does not change correct behavior
- [ ] Additional logging aids future diagnosis
- [ ] User informed about uncertainty in the fix

---

## Agents Responsible

| Agent | Responsibility |
|-------|---------------|
| **Coordinator** | Bug analysis, task assignment, Sentry context retrieval |
| **Specialist A** | Root cause analysis, fix implementation |
| **Specialist B** | Secondary module fixes (if multi-module bug) |
| **Code Reviewer** | Fix review, regression risk assessment |
| **Test Engineer** | Regression test, existing suite validation |
| **Doc Writer** | Changelog entry |
