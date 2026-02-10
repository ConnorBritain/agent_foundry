# Scenario: Code Refactoring

This scenario validates the team's ability to restructure existing code without changing its external behavior, improving maintainability, readability, or performance.

---

## Scenario Overview

| Property | Value |
|----------|-------|
| **Priority** | Medium |
| **Validated After** | Phase 4 |
| **Primary Agents** | Coordinator, Specialists A and B, Code Reviewer, Test Engineer |
| **Estimated Duration** | ~45-75 minutes (hybrid mode) |

---

## Success Path: Module Extraction Refactor

### Preconditions

- Existing codebase has a large module that should be split into smaller, focused modules
- Existing tests cover the current behavior (refactoring safety net)
- No new features are being added -- behavior must remain identical

### Steps

| Step | Action | Expected Outcome |
|------|--------|------------------|
| 1 | Coordinator analyzes the module and identifies extraction boundaries | Task decomposition: which functions move where, dependency map |
| 2 | Coordinator assigns parallel extraction tasks | Specialist A extracts module X, Specialist B extracts module Y |
| 3 | Coordinator defines interface contracts for extracted modules | Clear boundaries between new modules |
| 4 | Specialists implement extractions on parallel branches | Code moved, imports updated, no behavior changes |
| 5 | Code Reviewer verifies behavior preservation | Diff shows moves and renames, not logic changes |
| 6 | Test Engineer runs existing tests against refactored code | All existing tests pass without modification |
| 7 | Test Engineer adds tests for new module boundaries | Integration tests for extracted module interfaces |

### Validation Criteria

- [ ] All existing tests pass without modification (behavior preserved)
- [ ] No new functionality added (pure refactoring)
- [ ] Module boundaries are clean (no circular dependencies)
- [ ] Import paths updated throughout the codebase
- [ ] New modules have clear, focused responsibilities
- [ ] Code Reviewer confirms no logic changes in the diff

---

## Success Path: Performance Refactor

### Preconditions

- Performance bottleneck identified (slow query, N+1 problem, large payload)
- Existing tests cover the affected code paths
- Performance target is defined (e.g., response time < 200ms)

### Steps

| Step | Action | Expected Outcome |
|------|--------|------------------|
| 1 | Coordinator identifies bottleneck and defines performance target | Clear metric for success (e.g., query time < 50ms) |
| 2 | Specialist A implements the optimization | Query optimized, caching added, or algorithm improved |
| 3 | Code Reviewer verifies correctness preserved | Same results, faster execution |
| 4 | Test Engineer validates existing tests pass | No behavioral regressions |
| 5 | Test Engineer adds performance benchmark test | Test asserts the optimization meets the target |

### Validation Criteria

- [ ] Performance target met (measurable improvement)
- [ ] All existing tests pass (behavior preserved)
- [ ] No new functionality added
- [ ] Optimization is maintainable (not a hack)

---

## Edge Case: Refactoring Reveals a Bug

### Preconditions

- During refactoring, a Specialist discovers a latent bug in the existing code

### Steps

| Step | Action | Expected Outcome |
|------|--------|------------------|
| 1 | Specialist reports discovered bug to Coordinator | Bug documented with location and impact |
| 2 | Coordinator decides: fix now or defer | If fix is small, include it. If large, create separate task. |
| 3 | If fixing: Specialist adds fix in a separate commit | Bug fix commit is distinct from refactoring commits |
| 4 | Test Engineer adds regression test for the bug | Bug will not recur |

### Validation Criteria

- [ ] Bug fix is in a separate commit from refactoring
- [ ] Bug fix has its own regression test
- [ ] Refactoring and bug fix can be reviewed independently

---

## Edge Case: Refactoring Breaks an Existing Test

### Preconditions

- An existing test fails after refactoring
- The failure is due to the test depending on implementation details, not behavior

### Steps

| Step | Action | Expected Outcome |
|------|--------|------------------|
| 1 | Test Engineer identifies why the test fails | Test was coupled to implementation (e.g., mocking internals) |
| 2 | Test Engineer updates the test to test behavior, not implementation | Test verifies the same behavior through the new interface |
| 3 | Code Reviewer verifies the test update is correct | Test still validates the original requirement |

### Validation Criteria

- [ ] Updated test verifies behavior, not implementation details
- [ ] No test coverage lost
- [ ] Test passes against the refactored code

---

## Agents Responsible

| Agent | Responsibility |
|-------|---------------|
| **Coordinator** | Identify refactoring boundaries, assign parallel tasks, manage scope |
| **Specialist A** | Primary module extraction or optimization |
| **Specialist B** | Secondary module extraction or import updates |
| **Code Reviewer** | Verify behavior preservation, no logic changes in diff |
| **Test Engineer** | Run existing tests, add boundary tests, handle test updates |
| **Doc Writer** | Update API docs if module paths changed, changelog entry |
