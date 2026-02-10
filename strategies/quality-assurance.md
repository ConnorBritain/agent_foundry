# Quality Assurance Strategies

> Multi-agent review patterns, validation workflows, and human-in-the-loop checkpoints for AI-generated outputs.

## Overview

AI agents produce output faster than humans can review it. Without quality assurance strategies, this speed becomes a liability — agents generate plausible-looking code that contains subtle bugs, inconsistencies, or architectural drift. The solution is not to slow agents down but to build quality checks into the workflow itself.

Agent Foundry supports multiple QA patterns: agent-to-agent review (one agent checks another's work), automated validation (tests, linters, type checkers), human-in-the-loop checkpoints (pausing for human approval at critical points), and output validation pipelines (structured verification of deliverables against specifications).

This guide covers each pattern with implementation details so you can build QA into your teams from the start rather than bolting it on after quality problems emerge.

## QA Pattern 1: Multi-Agent Review

The most effective quality improvement in Agent Foundry is having one agent review another's output. A dedicated reviewer agent catches errors that the implementing agent missed — different "perspectives" from different system prompts surface different issues.

### Basic Review Pattern

```
Developer Agent --> writes code --> Reviewer Agent --> approves or requests changes
                                         |
                                         |--> Approved: merge to main
                                         |--> Changes requested: Developer revises
```

### Implementation

```yaml
team:
  name: reviewed-development
  agents:
    developer:
      model: claude-sonnet-4-5-20250929
      role: "Implement features per specification"
      output_to: "shared-workspace/changes/"

    reviewer:
      model: claude-sonnet-4-5-20250929
      role: "Review code changes for correctness, security, and quality"
      input_from: "shared-workspace/changes/"
      review_criteria:
        - "Correctness: Does the code do what the spec says?"
        - "Security: Are inputs validated? Are there injection risks?"
        - "Error handling: Are errors caught and handled appropriately?"
        - "Testing: Are edge cases covered?"
        - "Style: Does it follow project conventions?"
      output_format:
        approved: "APPROVED: {summary}"
        changes_requested: |
          CHANGES REQUESTED:
          {list of specific issues with file paths and line numbers}
```

### Specialized Reviewers

For higher-quality reviews, use specialized reviewer agents:

```yaml
review_pipeline:
  reviewers:
    security-reviewer:
      model: claude-opus-4-6
      focus: |
        Review ONLY for security issues:
        - SQL injection, XSS, CSRF vulnerabilities
        - Authentication and authorization flaws
        - Sensitive data exposure
        - Input validation gaps
        - Dependency vulnerabilities

    performance-reviewer:
      model: claude-sonnet-4-5-20250929
      focus: |
        Review ONLY for performance issues:
        - N+1 query patterns
        - Missing database indexes
        - Unnecessary memory allocation
        - Blocking operations in async contexts
        - Missing caching opportunities

    architecture-reviewer:
      model: claude-opus-4-6
      focus: |
        Review ONLY for architectural alignment:
        - Does this follow the established patterns?
        - Are concerns properly separated?
        - Are dependencies flowing in the right direction?
        - Is the interface clean and consistent?

  approval_requirement: "all"  # Options: all, majority, any
```

### Review Effectiveness Data

Based on typical Agent Foundry team runs:

| Configuration | Bug Detection Rate | Cost Overhead | Recommended For |
|---|---|---|---|
| No review | ~60% (self-caught) | 0% | Prototypes, throwaway code |
| Single reviewer (Sonnet) | ~82% | +15-20% | Most development work |
| Single reviewer (Opus) | ~88% | +25-35% | Important features |
| Specialized reviewers (2) | ~93% | +30-40% | Production code |
| Specialized reviewers (3) | ~96% | +45-60% | Security-critical code |

The jump from no review to a single reviewer is the highest-impact quality investment. Specialized reviewers provide diminishing but still meaningful returns.

## QA Pattern 2: Automated Validation Pipeline

Automated checks catch mechanical errors (syntax, types, test failures) without consuming API tokens on review.

### Validation Pipeline

```yaml
validation:
  pipeline:
    # Stage 1: Syntax and formatting
    - name: "lint"
      command: "npm run lint"
      on_failure: "return_to_agent"  # Agent fixes lint errors
      max_retries: 3

    # Stage 2: Type checking
    - name: "typecheck"
      command: "npx tsc --noEmit"
      on_failure: "return_to_agent"
      max_retries: 3

    # Stage 3: Unit tests
    - name: "unit_tests"
      command: "npm test -- --coverage"
      on_failure: "return_to_agent"
      max_retries: 2
      coverage_threshold: 80

    # Stage 4: Integration tests
    - name: "integration_tests"
      command: "npm run test:integration"
      on_failure: "escalate_to_reviewer"  # Agent might need help
      max_retries: 1

    # Stage 5: Build
    - name: "build"
      command: "npm run build"
      on_failure: "escalate_to_reviewer"
      max_retries: 1
```

### Self-Healing Pattern

Agents should fix their own validation failures before escalating:

```
Developer writes code
  --> Lint fails
    --> Developer reads lint errors, fixes them
      --> Lint passes
        --> Type check fails
          --> Developer reads type errors, fixes them
            --> Type check passes
              --> Tests fail
                --> Developer reads test output, debugs, fixes
                  --> Tests pass
                    --> Send to reviewer
```

Implementation in the agent's system prompt:

```markdown
After writing or modifying code, ALWAYS run the validation pipeline:
1. Run `npm run lint` — fix ALL lint errors before proceeding
2. Run `npx tsc --noEmit` — fix ALL type errors before proceeding
3. Run `npm test` — fix ALL test failures before proceeding
4. Run `npm run build` — fix ALL build errors before proceeding

Do NOT mark your task as complete until all four checks pass.
If you cannot fix an issue after 3 attempts, document the problem
and escalate to the reviewer.
```

### Pre-Commit Hooks

Configure git hooks to enforce validation:

```bash
#!/bin/bash
# .git/hooks/pre-commit (installed by Agent Foundry)

echo "Running pre-commit validation..."

# Lint
npm run lint --quiet
if [ $? -ne 0 ]; then
    echo "BLOCKED: Lint errors found. Fix before committing."
    exit 1
fi

# Type check
npx tsc --noEmit --quiet
if [ $? -ne 0 ]; then
    echo "BLOCKED: Type errors found. Fix before committing."
    exit 1
fi

# Tests (fast subset)
npm test -- --bail --quiet
if [ $? -ne 0 ]; then
    echo "BLOCKED: Tests failing. Fix before committing."
    exit 1
fi

echo "Pre-commit validation passed."
```

## QA Pattern 3: Human-in-the-Loop Checkpoints

Some decisions should not be made by agents alone. Human-in-the-loop (HITL) checkpoints pause the workflow for human review at critical points.

### When to Use HITL Checkpoints

```
ALWAYS use HITL for:
  - Security-critical changes (authentication, authorization, encryption)
  - Database schema migrations (data loss risk)
  - Public API changes (breaking change risk)
  - Infrastructure changes (cost and availability risk)
  - Deletion of files or data
  - Changes to deployment configurations
  - Any change the team has flagged as requiring approval

CONSIDER HITL for:
  - Architectural decisions that are expensive to reverse
  - Large refactoring operations (> 20 files)
  - Third-party service integrations
  - Performance-critical code paths

SKIP HITL for:
  - Internal implementation details with test coverage
  - Documentation updates
  - Test additions
  - Style/formatting changes
  - Bug fixes with clear reproduction and test
```

### Checkpoint Implementation

```yaml
checkpoints:
  - name: "architecture_approval"
    trigger: "phase == 'planning' AND task == 'architecture_design'"
    action: "pause_and_notify"
    notification:
      channel: "slack:#architecture-review"
      message: |
        Agent Foundry requires human approval:
        Team: {team_name}
        Agent: {agent_name}
        Task: Architecture design for {project_name}
        Artifacts: {list_of_design_documents}

        Reply with APPROVE or REJECT (with feedback).
    timeout: "4h"
    on_timeout: "halt_team"

  - name: "schema_migration_approval"
    trigger: "file_modified MATCHES '*/migrations/*.sql'"
    action: "pause_and_notify"
    notification:
      channel: "slack:#database-team"
      message: |
        Database migration requires approval:
        Migration file: {file_path}
        Changes: {migration_summary}
    timeout: "2h"
    on_timeout: "halt_agent"

  - name: "pre_deploy_approval"
    trigger: "phase == 'deployment'"
    action: "pause_and_notify"
    notification:
      channel: "slack:#deploys"
    timeout: "1h"
    on_timeout: "halt_team"
```

### HITL Workflow

```
Agent reaches checkpoint
  |
  +--> Agent writes checkpoint summary
  |    (what was done, what needs approval, relevant files)
  |
  +--> System sends notification to human
  |
  +--> Agent pauses (saves state, releases resources)
  |
  +--> Human reviews artifacts
  |      |
  |      +--> APPROVE: Agent resumes from checkpoint
  |      |
  |      +--> REJECT with feedback:
  |      |    Agent receives feedback, revises, re-submits
  |      |
  |      +--> TIMEOUT: Team halts, human notified
  |
  +--> (Checkpoint logged for audit trail)
```

### Minimizing HITL Latency

Human checkpoints are the biggest bottleneck in agent workflows. Minimize their impact:

1. **Batch checkpoints**: Group related decisions into a single checkpoint rather than interrupting for each one.
2. **Provide context**: Give the reviewer everything they need in the notification — don't make them dig through files.
3. **Set tight timeouts**: A 30-minute timeout with escalation is better than a 4-hour timeout that blocks the team.
4. **Async design**: Let non-blocked agents continue working while the checkpoint is pending.
5. **Pre-approve patterns**: Define patterns that are pre-approved (e.g., "migrations that only add columns and indexes are auto-approved").

## QA Pattern 4: Output Validation

Validate agent outputs against specifications and expected formats before accepting them.

### Specification Compliance Checking

```yaml
validation:
  spec_compliance:
    enabled: true
    specs:
      api_contract:
        file: "specs/openapi.yaml"
        check: "All new endpoints match the OpenAPI spec"
        tool: "openapi-diff"

      data_models:
        file: "specs/data-models.md"
        check: "All database schemas match the data model spec"
        validator_agent:
          model: claude-haiku-4-5-20251001
          prompt: |
            Compare the implemented database schema against the specification.
            List any discrepancies. Output PASS if compliant, FAIL with details if not.

      naming_conventions:
        rules:
          - "API endpoints use kebab-case: /api/user-profiles"
          - "Database tables use snake_case: user_profiles"
          - "TypeScript interfaces use PascalCase: UserProfile"
          - "TypeScript variables use camelCase: userProfile"
        validator_agent:
          model: claude-haiku-4-5-20251001
```

### Structural Validation

Check that outputs have the expected structure:

```yaml
validation:
  structural:
    - type: "api_endpoint"
      required:
        - "Input validation middleware"
        - "Error handling with appropriate status codes"
        - "Response type matching OpenAPI spec"
        - "Authentication middleware (unless explicitly public)"
      validator: "structural-check-agent"

    - type: "database_migration"
      required:
        - "Up migration"
        - "Down migration (rollback)"
        - "Idempotency (IF NOT EXISTS / IF EXISTS)"
      validator: "migration-check-agent"

    - type: "test_file"
      required:
        - "At least one happy-path test"
        - "At least one error-case test"
        - "At least one edge-case test"
        - "Descriptive test names"
      validator: "test-quality-agent"
```

### Fact-Checking Workflow

For documentation and content-generating agents, verify factual claims:

```yaml
fact_checking:
  enabled: true
  agent:
    model: claude-sonnet-4-5-20250929
    prompt: |
      Review the following documentation for factual accuracy:
      1. Are code examples syntactically correct?
      2. Do file paths reference files that actually exist?
      3. Are API descriptions consistent with the actual implementation?
      4. Are version numbers and dependency names correct?

      For each claim, mark as VERIFIED, UNVERIFIED, or INCORRECT.
      Provide evidence for INCORRECT claims.

  scope:
    - "*.md"           # All markdown files
    - "docs/**"        # All documentation
    - "README*"        # README files
```

## QA Pattern 5: Regression Testing for Prompts

When you change agent prompts or configurations, regression test to ensure quality doesn't degrade.

### Prompt Regression Testing

```yaml
prompt_regression:
  test_suite:
    - name: "api_endpoint_generation"
      prompt_file: "prompts/developer.md"
      test_cases:
        - input: "Create a GET endpoint for /api/users that returns paginated results"
          expected:
            - "Includes pagination parameters (page, limit)"
            - "Returns total count in response"
            - "Validates pagination inputs"
            - "Handles empty results"
          model: claude-sonnet-4-5-20250929

        - input: "Create a POST endpoint for /api/users with email and password"
          expected:
            - "Validates email format"
            - "Hashes password before storage"
            - "Returns 201 on success"
            - "Returns 409 on duplicate email"
          model: claude-sonnet-4-5-20250929

    - name: "code_review_quality"
      prompt_file: "prompts/reviewer.md"
      test_cases:
        - input: "code_with_sql_injection.ts"  # Known-bad code
          expected:
            - "Identifies SQL injection vulnerability"
            - "Suggests parameterized queries"
          model: claude-sonnet-4-5-20250929

  execution:
    trigger: "prompt_file_changed"
    runner: "regression-test-agent"
    pass_threshold: 0.9   # 90% of test cases must pass
    on_failure: "block_prompt_change"
```

### A/B Testing Prompts

When optimizing prompts, test new versions against the current version:

```yaml
ab_testing:
  enabled: true
  experiment:
    name: "developer_prompt_v2"
    control:
      prompt_file: "prompts/developer_v1.md"
      model: claude-sonnet-4-5-20250929
    treatment:
      prompt_file: "prompts/developer_v2.md"
      model: claude-sonnet-4-5-20250929
    tasks:
      - "Implement user registration endpoint"
      - "Add pagination to list endpoint"
      - "Implement file upload handler"
    evaluation:
      metrics:
        - "test_pass_rate"
        - "lint_error_count"
        - "reviewer_approval_rate"
        - "token_consumption"
      evaluator_model: claude-opus-4-6
      min_sample_size: 10
```

## QA Workflow: Putting It All Together

A comprehensive QA workflow combines all patterns:

```
Phase 1: Development
  Developer Agent writes code
    --> Self-validation (lint, typecheck, tests)
    --> Fix own errors (up to 3 retries)
    --> Checkpoint: code ready for review

Phase 2: Automated Review
  Validation Pipeline runs
    --> Lint check
    --> Type check
    --> Unit tests with coverage
    --> Integration tests
    --> Build verification
    --> Spec compliance check
  If any fail --> return to Developer Agent

Phase 3: Agent Review
  Reviewer Agent(s) examine the code
    --> Security review (Opus)
    --> Architecture review (Opus or Sonnet)
    --> Code quality review (Sonnet)
  If changes requested --> return to Developer Agent

Phase 4: Human Checkpoint (conditional)
  If security-critical OR schema change OR public API change:
    --> Pause for human review
    --> Human approves, rejects, or requests changes

Phase 5: Integration
  Merge Agent integrates approved changes
    --> Final integration test suite
    --> Final build verification
    --> Tag and package
```

### Cost of QA

| QA Level | Cost Overhead | Bug Detection | Best For |
|---|---|---|---|
| Minimal (self-validation only) | +5% | ~65% | Prototypes, experiments |
| Standard (validation + single reviewer) | +20% | ~85% | Most development |
| Thorough (validation + specialized reviewers) | +40% | ~94% | Production features |
| Comprehensive (all patterns + HITL) | +60% | ~98% | Critical systems |

The cost of QA is almost always less than the cost of fixing bugs in production. A 40% cost overhead that catches 94% of bugs is excellent ROI.

## Recommendations

### For all projects
Implement self-validation (lint, typecheck, tests) as a minimum. This is free (no API cost) and catches the most common errors. Make it mandatory — agents should never submit code that doesn't pass basic checks.

### For projects with multiple developers (human or agent)
Add a single reviewer agent (Sonnet). This is the highest-impact QA investment. The 20% cost overhead pays for itself in reduced rework and fewer bugs reaching production.

### For production-bound code
Add specialized reviewers for security and architecture. Implement HITL checkpoints for schema changes, public API changes, and security-sensitive code. Add spec compliance checking.

### For regulated environments
Implement the comprehensive QA workflow with full audit logging. Every agent action, review decision, and human approval is logged. Use the regression testing framework to validate prompt changes before deployment.

### For prompt engineering iteration
Use regression testing and A/B testing when modifying agent prompts. A small change to a prompt can significantly affect output quality. Measure before and after.

## Related Resources

- [Decision Framework](./decision-framework.md) — Team composition including reviewer roles
- [Model Selection Guide](./model-selection-guide.md) — Choosing models for reviewer agents
- [Optimization Guide](./optimization-guide.md) — Balancing quality optimization with cost
- [Long-Running Agents](./long-running-agents.md) — QA across multi-session workflows
- [Deployment Guide](./deployment-guide.md) — CI/CD integration for automated QA
