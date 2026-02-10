# Code Implementation Team -- Technical Specification

## Overview

This document defines the architecture, agent composition, responsibilities, deliverables, and quality standards for the Code Implementation Team. The team takes a feature specification or user story and produces production-ready, tested, documented code on a feature branch with passing CI.

---

## 1. Team Composition

The team consists of 6 specialized agents. Three operate on Opus 4.6 for tasks requiring deep code reasoning (implementation and review). Two operate on Sonnet 4.5 for planning and testing. One operates on Haiku 4.5 for documentation.

### 1.1 Coordinator / Planner

- **Model:** Sonnet 4.5
- **Token budget:** ~30K tokens
- **Primary responsibilities:**
  - Receive and parse the feature specification
  - Decompose the feature into parallelizable work units
  - Identify dependencies between tasks and establish execution order
  - Assign tasks to Implementation Specialists with clear acceptance criteria
  - Define shared interfaces and contracts between parallel tasks
  - Track milestones and flag potential blockers
  - Run quality gates between phases
  - Produce user-facing progress summaries at each gate
- **Decision authority:**
  - FINAL say on task assignment, ordering, and priority
  - Can reassign tasks between Specialists if one is blocked
  - Escalates to user for scope changes, ambiguous requirements, or budget overruns
- **Outputs:**
  - Task decomposition with dependency graph
  - Task assignments for each Specialist
  - Shared interface definitions
  - Phase gate reports with user prompts

### 1.2 Implementation Specialist A

- **Model:** Opus 4.6
- **Token budget:** ~150K tokens
- **Primary responsibilities:**
  - Implement primary feature tasks on branch `agent/impl-a/[feature-name]`
  - Write clean, production-ready code following project conventions
  - Handle complex logic, architecture decisions, and edge cases
  - Push commits every 10-15 minutes with clear commit messages
  - Address blocking issues flagged by the Code Reviewer
- **Technical standards:**
  - Follow the project's existing code style and patterns
  - Validate all inputs, handle all errors
  - Write code that is easy to review: small functions, clear names, comments for non-obvious logic
  - No new dependencies without Coordinator approval
- **Outputs:**
  - Implementation branch with commits
  - Status updates every 5 minutes

### 1.3 Implementation Specialist B

- **Model:** Opus 4.6
- **Token budget:** ~150K tokens
- **Primary responsibilities:**
  - Implement secondary feature tasks on branch `agent/impl-b/[feature-name]`
  - Work in parallel with Specialist A on independent sub-features
  - Follow the same technical standards as Specialist A
  - Coordinate with Specialist A through shared interfaces defined by the Coordinator
- **Outputs:**
  - Implementation branch with commits
  - Status updates every 5 minutes

### 1.4 Code Reviewer

- **Model:** Opus 4.6
- **Token budget:** ~80K tokens
- **Primary responsibilities:**
  - Review both implementation branches against quality standards
  - Identify blocking issues (must fix) and suggestions (nice to have)
  - Check for: logic errors, missing error handling, security vulnerabilities, performance regressions, test coverage gaps, style violations
  - Explain WHY something is a problem, not just THAT it is
  - Re-review after Specialists address blocking issues
  - Approve merge to feature branch when all blockers are resolved
- **Review categories:**
  - **BLOCKER:** Must fix before merge. Logic errors, security issues, missing error handling.
  - **SUGGESTION:** Optional improvement. Style preferences, alternative approaches, minor optimizations.
- **Outputs:**
  - Structured review with categorized findings
  - Approval or rejection with rationale

### 1.5 Test Engineer

- **Model:** Sonnet 4.5
- **Token budget:** ~60K tokens
- **Primary responsibilities:**
  - Write holdout test scenarios before seeing the implementation
  - Generate unit tests, integration tests, and end-to-end tests
  - Measure test coverage and flag gaps
  - Run holdout scenarios against the implemented code
  - Report test results and coverage to the Coordinator
- **Testing standards:**
  - Tests cover happy paths, error paths, boundary conditions, and edge cases
  - Test code is as clean and maintainable as production code
  - Tests are deterministic: no flaky tests, no cross-test dependencies
  - Coverage target: >= 80% of new code
- **Outputs:**
  - Holdout test scenarios (written before implementation)
  - Unit and integration test files
  - Test results and coverage report

### 1.6 Documentation Writer

- **Model:** Haiku 4.5
- **Token budget:** ~20K tokens
- **Primary responsibilities:**
  - Update API documentation for new or modified endpoints
  - Update README if the feature changes setup, usage, or configuration
  - Add inline comments where the Code Reviewer flagged complexity
  - Generate a changelog entry for the feature
  - Follow the project's existing documentation conventions
- **Documentation standards:**
  - Prioritize examples over descriptions: show, do not tell
  - Keep documentation close to the code it describes
  - Every public function or endpoint has a doc comment
  - Changelog entries follow Keep a Changelog format
- **Outputs:**
  - Updated API docs
  - Updated README (if needed)
  - Inline comments
  - Changelog entry

---

## 2. Token Budget Summary

| Agent | Model | Token Budget | Est. Cost |
|-------|-------|-------------|-----------|
| Coordinator / Planner | Sonnet 4.5 | ~30K | ~$0.24 |
| Implementation Specialist A | Opus 4.6 | ~150K | ~$9.75 |
| Implementation Specialist B | Opus 4.6 | ~150K | ~$9.75 |
| Code Reviewer | Opus 4.6 | ~80K | ~$5.20 |
| Test Engineer | Sonnet 4.5 | ~60K | ~$0.48 |
| Documentation Writer | Haiku 4.5 | ~20K | ~$0.02 |
| **Total** | | **~490K** | **~$25.44** |

Note: Estimates include a 15-20% buffer for iteration cycles (reviewer requests changes, tests fail). Effective cost with buffer: approximately $30.

---

## 3. Quality Standards

### 3.1 Code Quality

- Follow the project's established code style (configured via `code_style` in CONFIG.md)
- All inputs validated, all errors handled
- No unused imports, no dead code
- Functions are small, focused, and named clearly
- Comments explain "why," not "what"

### 3.2 Security

- All user inputs validated and sanitized
- No secrets or credentials in code
- Authentication and authorization checks on all protected paths
- SQL injection prevention (parameterized queries or ORM)
- XSS prevention (output encoding)

### 3.3 Testing

- Coverage >= 80% on new code
- Unit tests for all business logic
- Integration tests for API endpoints and database operations
- Edge cases and error paths tested
- Holdout scenarios pass at >= 90% satisfaction rate

### 3.4 Documentation

- All public APIs documented with request/response examples
- README updated if setup or usage changes
- Changelog entry for every feature
- Complex code sections have inline comments

---

## 4. Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Scenario satisfaction | >= 90% | Holdout test pass rate |
| Test coverage | >= 80% | Coverage tool output |
| Review approval | First-pass or second-pass | Number of review cycles |
| Documentation completeness | All public APIs documented | API doc coverage |
| Budget adherence | Within 20% of estimate | Actual vs projected tokens |
| Wall-clock time | < 90 min (hybrid mode) | Start to merge |
