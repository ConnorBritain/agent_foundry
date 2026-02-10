---
skill_name: "code-review"
version: "1.0.0"
description: "Performs structured code reviews with severity levels, categorized feedback, and actionable suggestions"
author: "Sforza"
triggers:
  - "when asked to review code or a pull request"
  - "when asked to check code quality"
  - "when a diff or changeset is presented for feedback"
  - "when asked to find bugs or issues in code"
---

# Code Review Skill

## Purpose
Provide thorough, constructive code reviews that identify issues, suggest improvements, and maintain team standards. Reviews should be actionable, specific, and prioritized by severity.

## Review Process

### Step 1: Understand Context
Before reviewing, establish:
- What is the purpose of this change? (feature, bugfix, refactor)
- What files are modified and what is their role in the system?
- Are there related tests, documentation, or migration changes?

### Step 2: Review Checklist
Evaluate the code against these categories:

#### Correctness
- [ ] Does the code do what it claims to do?
- [ ] Are edge cases handled (null, empty, boundary values)?
- [ ] Are error paths handled gracefully?
- [ ] Are race conditions possible in async code?
- [ ] Are return types correct and exhaustive?

#### Security
- [ ] Is user input validated and sanitized?
- [ ] Are SQL queries parameterized?
- [ ] Are secrets kept out of source code?
- [ ] Are authentication/authorization checks present?
- [ ] Is sensitive data excluded from logs?

#### Performance
- [ ] Are there unnecessary re-renders (React)?
- [ ] Are database queries efficient (N+1, missing indexes)?
- [ ] Are large datasets paginated?
- [ ] Is memoization used where appropriate?
- [ ] Are expensive operations cached?

#### Maintainability
- [ ] Is the code readable without excessive comments?
- [ ] Are functions small and single-purpose?
- [ ] Are naming conventions consistent and descriptive?
- [ ] Is there unnecessary duplication?
- [ ] Are abstractions at the right level?

#### Testing
- [ ] Are new features covered by tests?
- [ ] Are edge cases and error paths tested?
- [ ] Do tests follow the AAA pattern (Arrange, Act, Assert)?
- [ ] Are mocks minimal and focused?

### Step 3: Classify Findings

#### Severity Levels
| Level | Label | Meaning | Action Required |
|---|---|---|---|
| P0 | CRITICAL | Security vulnerability, data loss risk, crash | Must fix before merge |
| P1 | ERROR | Bug, incorrect behavior, broken feature | Must fix before merge |
| P2 | WARNING | Performance issue, missing edge case, tech debt | Should fix before merge |
| P3 | SUGGESTION | Style improvement, better approach, minor refactor | Consider for this or future PR |
| P4 | NIT | Formatting, naming preference, minor style | Optional, low priority |

### Step 4: Format Feedback

#### Individual Finding Format
```
**[SEVERITY] Category: Brief title**
File: `path/to/file.ts` line X-Y

Description of the issue and why it matters.

Suggested fix:
\`\`\`typescript
// proposed code change
\`\`\`
```

#### Review Summary Format
```
## Code Review Summary

### Overview
Brief description of what was reviewed and overall assessment.

### Statistics
- Files reviewed: N
- Findings: X critical, Y warnings, Z suggestions

### Critical Issues (must fix)
1. [finding]

### Warnings (should fix)
1. [finding]

### Suggestions (consider)
1. [finding]

### Positive Observations
- Note good patterns, clean code, thorough tests

### Verdict
- [ ] APPROVE — ready to merge
- [ ] REQUEST CHANGES — critical/error issues must be addressed
- [ ] COMMENT — suggestions only, author decides
```

## Feedback Tone Guidelines
- Be specific: reference exact lines and provide concrete alternatives
- Be constructive: explain WHY something is an issue, not just WHAT
- Be respectful: "Consider using X because Y" not "This is wrong"
- Acknowledge good work: call out well-written code and good decisions
- Ask questions: "Is there a reason for X?" before assuming it's wrong
- Separate style from substance: don't block PRs over formatting preferences

## Common Patterns to Flag
| Pattern | Issue | Suggestion |
|---|---|---|
| any type in TypeScript | Type safety loss | Use proper type or unknown |
| Catching and swallowing errors | Silent failures | Log or rethrow with context |
| Magic numbers/strings | Unclear intent | Extract to named constants |
| Deeply nested callbacks | Readability | Refactor to async/await or extract |
| God functions (>50 lines) | Maintainability | Break into smaller functions |
| Missing error boundaries | UI crashes | Add React ErrorBoundary |
| Unsanitized user input | XSS/injection risk | Validate with schema (Zod) |
| Direct DOM manipulation in React | Framework bypass | Use refs or state |
| Console.log in production | Information leak | Use proper logger, strip in build |
| Commented-out code | Dead code | Remove, use git history |

## Auto-Detect Review Scope
When reviewing, automatically adjust depth based on change type:
- **New feature**: Full review — correctness, security, tests, design
- **Bug fix**: Focus on root cause, regression tests, related code paths
- **Refactor**: Focus on behavior preservation, test coverage, simplification
- **Dependency update**: Check changelog, breaking changes, security advisories
- **Config change**: Validate values, check environment-specific overrides
