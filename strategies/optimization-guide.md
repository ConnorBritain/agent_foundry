# Optimization Guide

> Optimizing Sforza for cost, speed, and quality through prompt caching, model routing, token budgeting, and execution tuning.

## Overview

Running an Sforza team involves three competing concerns: cost (how much you spend on API calls), speed (how fast the team completes work), and quality (how good the output is). You can rarely maximize all three simultaneously, but you can optimize the balance for your specific situation.

This guide covers five optimization levers: prompt caching to reduce cost, model routing to match capability to need, token budgeting to control spending, parallel execution optimization to improve speed, and output quality tuning to improve results. Each lever includes concrete configurations and measurable impact estimates.

The biggest gains come from the first two optimizations — prompt caching and model routing. Start there before fine-tuning the others.

## Optimization 1: Prompt Caching

Prompt caching is the single highest-impact cost optimization available. When multiple agents share the same system prompt, codebase context, or specification documents, caching avoids re-processing those tokens on every request.

### How Prompt Caching Works

```
Without caching:
  Request 1: [system_prompt + context + query] --> Full price for all tokens
  Request 2: [system_prompt + context + query] --> Full price again
  Request 3: [system_prompt + context + query] --> Full price again
  Total: 3x full price

With caching:
  Request 1: [system_prompt + context + query] --> Full price (cache write)
  Request 2: [cached_prefix + query] --> 90% discount on cached portion
  Request 3: [cached_prefix + query] --> 90% discount on cached portion
  Total: ~1.2x full price (vs. 3x without caching)
```

### Cost Savings by Model

| Model | Standard Input | Cache Write | Cache Read | Savings on Cache Read |
|---|---|---|---|---|
| Opus 4.6 | $15/1M | $18.75/1M | $1.50/1M | **90%** |
| Sonnet 4.5 | $3/1M | $3.75/1M | $0.30/1M | **90%** |
| Haiku 4.5 | $0.80/1M | $1.00/1M | $0.08/1M | **90%** |

The cache write costs 25% more than standard input, but cache reads cost 90% less. The break-even point is just **2 reads** — after that, every additional read is pure savings.

### What to Cache

**High-impact caching targets** (cache these first):

| Target | Typical Size | Reuse Frequency | Impact |
|---|---|---|---|
| System prompts | 500-2,000 tokens | Every request | High |
| Specification documents | 2,000-10,000 tokens | Every agent session | Very high |
| Codebase structure / file tree | 1,000-5,000 tokens | Every request | High |
| Shared type definitions | 1,000-3,000 tokens | Most requests | Medium-high |
| Architectural decision records | 500-2,000 tokens | Frequent | Medium |

**Low-impact targets** (don't bother caching):

| Target | Why Low Impact |
|---|---|
| Individual file contents | Change frequently, cache invalidates |
| Command outputs | Unique per execution |
| Error messages | Unique per occurrence |
| Short queries | Too small to matter |

### Implementation

Structure your prompts to maximize cache hit rates:

```yaml
# Good: Static content at the beginning (cacheable prefix)
prompt_structure:
  - section: system_prompt       # Static -- cache this
    cache: true
  - section: specification       # Static per project -- cache this
    cache: true
  - section: codebase_context    # Semi-static -- cache this
    cache: true
  - section: task_history        # Changes per session -- don't cache
    cache: false
  - section: current_task        # Changes per request -- don't cache
    cache: false
```

```yaml
# Agent configuration with caching
agents:
  developer:
    model: claude-sonnet-4-5-20250929
    prompt_caching:
      enabled: true
      cache_prefix:
        - source: "file:specs/project-spec.md"     # 5K tokens, cached
        - source: "file:specs/api-contract.md"      # 3K tokens, cached
        - source: "file:shared-state/architecture-decisions.md"  # 2K tokens, cached
      # Total cached prefix: ~10K tokens
      # Savings per request: ~$0.027 (Sonnet) vs. ~$0.03 without cache
      # Over 50 requests: $1.35 saved vs. $0.0375 extra cache write cost
```

### Cache Lifetime and Invalidation

- Anthropic's prompt cache has a 5-minute TTL that resets on each cache hit.
- For active agent sessions (multiple requests per minute), the cache stays warm automatically.
- For CI/CD runs with gaps between requests, consider pre-warming the cache with a dummy request.
- If your specification changes, the cache invalidates automatically (content-addressed).

## Optimization 2: Model Routing

Model routing assigns the cheapest model that can handle each task, rather than using a single model for everything.

### Static Routing

Assign models at team configuration time based on role:

```yaml
# Static routing: model assigned per agent role
agents:
  orchestrator:
    model: claude-opus-4-6           # Complex coordination
  developer:
    model: claude-sonnet-4-5-20250929  # Feature implementation
  test-writer:
    model: claude-haiku-4-5-20251001   # High-volume test generation
  formatter:
    model: claude-haiku-4-5-20251001   # Mechanical transformation
```

**Cost impact**: A team using Opus for everything costs 5-10x more than a team with proper static routing. See the [Model Selection Guide](./model-selection-guide.md) for detailed cost comparisons.

### Dynamic Routing

Adjust the model based on task complexity at runtime:

```yaml
# Dynamic routing configuration
routing:
  strategy: dynamic
  classifier:
    model: claude-haiku-4-5-20251001  # Cheap model classifies task complexity
    prompt: |
      Classify this task as LOW, MEDIUM, or HIGH complexity:
      - LOW: Mechanical changes, formatting, simple tests, boilerplate
      - MEDIUM: Feature implementation, standard code review, documentation
      - HIGH: Architecture decisions, security review, complex debugging
      Task: {task_description}
      Classification:

  model_map:
    LOW: claude-haiku-4-5-20251001
    MEDIUM: claude-sonnet-4-5-20250929
    HIGH: claude-opus-4-6

  # Fallback: If a lower model fails or returns low confidence, escalate
  escalation:
    enabled: true
    trigger: "confidence < 0.6 OR task_failed"
    max_escalations: 1
```

**Cost impact of dynamic routing:**

| Scenario | All-Opus Cost | Static Routing | Dynamic Routing |
|---|---|---|---|
| 100 tasks (mixed complexity) | $150 | $45 | $35 |
| Savings vs. All-Opus | -- | 70% | 77% |

### Hybrid Routing

Use static routing for known roles and dynamic routing for ad-hoc tasks:

```yaml
routing:
  strategy: hybrid
  static:
    orchestrator: claude-opus-4-6
    code-reviewer: claude-sonnet-4-5-20250929
  dynamic:
    all_other_agents: true
    classifier_model: claude-haiku-4-5-20251001
```

## Optimization 3: Token Budgeting

Token budgeting sets hard limits on how many tokens each agent can consume, preventing runaway costs.

### Per-Agent Budgets

```yaml
budget:
  global:
    max_total: 100.00          # Hard cap for entire team run
    warning_at: 75.00          # Alert at 75%

  per_agent:
    orchestrator:
      max_input_tokens: 500000   # 500K input tokens
      max_output_tokens: 100000  # 100K output tokens
      max_cost: 25.00
    developer:
      max_input_tokens: 1000000
      max_output_tokens: 200000
      max_cost: 15.00
    test-writer:
      max_input_tokens: 500000
      max_output_tokens: 100000
      max_cost: 3.00

  on_budget_exceeded:
    action: "checkpoint_and_halt"  # Options: warn, throttle, halt
    notification: "slack:#sforza-alerts"
```

### Token-Efficient Prompting

Reduce token consumption through prompt design:

**1. Concise system prompts**

```markdown
# Bad: Verbose system prompt (800 tokens)
You are an expert software developer with decades of experience in building
robust, scalable applications. You follow best practices including clean code
principles, SOLID design patterns, comprehensive testing, and thorough
documentation. When writing code, you should consider performance implications,
security vulnerabilities, maintainability concerns, and user experience...

# Good: Focused system prompt (200 tokens)
You are a backend developer. Write clean, tested TypeScript code.
Follow the project's existing patterns. Use Drizzle ORM for database access.
Validate all inputs. Handle errors with the project's AppError class.
```

**2. Targeted file reads**

```yaml
# Bad: Read everything
file_reading:
  strategy: "read_all_src"  # Reads every file in src/
  typical_tokens: 50,000

# Good: Read what's needed
file_reading:
  strategy: "targeted"
  rules:
    - "Read only files directly related to the current task"
    - "Read type definition files for interfaces"
    - "Do NOT read test files unless writing tests"
  typical_tokens: 10,000
```

**3. Structured output format**

```yaml
# Instruct agents to use compact output
output_format:
  code_changes: "unified_diff"    # Diffs, not full file contents
  explanations: "bullet_points"   # Not prose paragraphs
  status_updates: "structured"    # YAML/JSON, not narrative
  max_explanation_length: 200     # Tokens, not words
```

### Token Consumption Tracking

```yaml
tracking:
  granularity: "per_request"
  metrics:
    - "input_tokens"
    - "output_tokens"
    - "cache_read_tokens"
    - "cache_write_tokens"
    - "cost_usd"
  aggregation:
    - "per_agent"
    - "per_session"
    - "per_team_run"
  export:
    format: "csv"
    path: "logs/token_usage_{date}.csv"
```

## Optimization 4: Parallel Execution

Running agents in parallel reduces wall-clock time. But parallelism has costs: coordination overhead, potential merge conflicts, and higher peak API usage.

### Parallelism Strategies

**Strategy 1: Task-Level Parallelism**

Run independent tasks simultaneously:

```yaml
execution:
  strategy: task_parallel
  max_concurrent_agents: 4
  task_dependencies:
    implement_api:
      depends_on: ["plan_architecture"]
    implement_ui:
      depends_on: ["plan_architecture"]
    write_api_tests:
      depends_on: ["implement_api"]
    write_ui_tests:
      depends_on: ["implement_ui"]
    integration_test:
      depends_on: ["write_api_tests", "write_ui_tests"]

  # implement_api and implement_ui run in parallel
  # write_api_tests and write_ui_tests run in parallel
  # integration_test waits for both test suites
```

**Strategy 2: Agent-Level Parallelism**

Multiple agents work on different aspects of the same codebase:

```yaml
execution:
  strategy: agent_parallel
  agents:
    backend-dev:
      workspace: "src/api/"
      parallel_group: "implementation"
    frontend-dev:
      workspace: "src/ui/"
      parallel_group: "implementation"
    test-writer:
      workspace: "tests/"
      parallel_group: "validation"

  # "implementation" group runs in parallel
  # "validation" group runs after "implementation" completes
```

**Strategy 3: Pipeline Parallelism**

Overlap pipeline stages so that stage N+1 starts as soon as stage N produces partial output:

```yaml
execution:
  strategy: pipeline
  stages:
    - name: "plan"
      agent: "orchestrator"
      outputs: ["task_list"]
    - name: "implement"
      agents: ["dev-1", "dev-2", "dev-3"]
      trigger: "on_each_task_from_plan"  # Start as tasks become available
    - name: "review"
      agent: "reviewer"
      trigger: "on_each_implementation"  # Review each piece as it's done
```

### Speed Impact

| Configuration | Wall-Clock Time | API Cost | Notes |
|---|---|---|---|
| Fully serial (1 agent) | 60 min | $10 | Slowest, cheapest |
| 2 parallel agents | 35 min | $11 | Good balance |
| 4 parallel agents | 20 min | $13 | Near-optimal for most projects |
| 8 parallel agents | 15 min | $18 | Diminishing returns, higher coordination cost |

### Rate Limit Awareness

Parallel agents share your API rate limit. Monitor and throttle accordingly:

```yaml
rate_limit_management:
  strategy: "fair_share"
  total_rpm: 4000       # Your rate limit (requests per minute)
  per_agent_rpm: 500    # Reserve per agent
  burst_allowance: 1.5  # Allow 50% burst for short periods
  on_throttle:
    action: "queue_and_retry"
    max_queue_depth: 10
    queue_timeout: 120  # seconds
```

## Optimization 5: Output Quality Tuning

Quality optimization ensures agent outputs are correct, consistent, and aligned with project standards.

### Temperature Settings

```yaml
# Temperature recommendations by task type
temperature_guide:
  coordination:     0.2   # Deterministic task assignment and planning
  code_generation:  0.4   # Consistent but not rigid code output
  code_review:      0.3   # Thorough but focused review
  test_writing:     0.3   # Systematic test generation
  creative_writing: 0.7   # Documentation, comments, naming
  debugging:        0.2   # Analytical, methodical investigation
  refactoring:      0.3   # Consistent pattern application
```

### Quality-Enhancing Prompt Patterns

**Pattern 1: Specification Anchoring**

Give agents explicit specifications to code against, reducing interpretation errors:

```yaml
quality:
  specification_anchoring:
    enabled: true
    spec_files:
      - "specs/api-contract.yaml"    # OpenAPI spec
      - "specs/data-models.md"       # Data model definitions
      - "specs/business-rules.md"    # Business logic rules
    instruction: |
      Always reference the specification files before writing code.
      If the spec is ambiguous, flag it rather than guessing.
      Never deviate from the spec without explicit instruction.
```

**Pattern 2: Self-Validation**

Have agents validate their own output before submitting:

```yaml
quality:
  self_validation:
    enabled: true
    steps:
      - "After writing code, run the linter and fix any issues"
      - "After writing tests, run them and fix any failures"
      - "Before marking a task complete, re-read the specification and verify alignment"
      - "If any test fails, debug and fix before proceeding"
```

**Pattern 3: Iterative Refinement**

Allow agents multiple passes on important outputs:

```yaml
quality:
  iterative_refinement:
    enabled: true
    max_iterations: 3
    refinement_trigger: "tests_failing OR review_comments_exist"
    refinement_prompt: |
      Your previous output had issues: {issues}
      Revise your implementation to address these issues.
      Focus specifically on: {focus_areas}
```

**Pattern 4: Exemplar-Driven Output**

Provide examples of good output in the agent's context:

```yaml
quality:
  exemplars:
    enabled: true
    examples:
      - file: "examples/good-api-endpoint.ts"
        label: "Follow this pattern for new API endpoints"
      - file: "examples/good-test-file.ts"
        label: "Follow this pattern for test files"
      - file: "examples/good-error-handling.ts"
        label: "Follow this pattern for error handling"
```

### Quality Metrics

Track quality over time to identify degradation:

```yaml
quality_metrics:
  automated:
    - metric: "test_pass_rate"
      target: ">= 95%"
      measurement: "tests_passed / tests_total"
    - metric: "lint_clean"
      target: "0 errors"
      measurement: "lint_error_count"
    - metric: "type_check_clean"
      target: "0 errors"
      measurement: "tsc_error_count"
    - metric: "build_success"
      target: "true"
      measurement: "build_exit_code == 0"

  review_based:
    - metric: "reviewer_approval_rate"
      target: ">= 80% first-pass approval"
    - metric: "rework_rate"
      target: "<= 20% of tasks require rework"
```

## Optimization Priority Matrix

Apply optimizations in this order for maximum impact:

| Priority | Optimization | Effort | Impact | Savings |
|---|---|---|---|---|
| 1 | Prompt caching | Low | Very High | 40-60% cost reduction |
| 2 | Static model routing | Low | High | 50-70% cost reduction |
| 3 | Token-efficient prompts | Medium | High | 20-40% cost reduction |
| 4 | Parallel execution | Medium | High | 40-60% time reduction |
| 5 | Dynamic model routing | Medium | Medium | 10-20% additional cost reduction |
| 6 | Temperature tuning | Low | Medium | Quality improvement |
| 7 | Self-validation | Low | Medium | Quality improvement |
| 8 | Iterative refinement | Medium | Medium | Quality improvement |
| 9 | Token budgeting | Low | Low-Medium | Cost control (not reduction) |
| 10 | Exemplar-driven output | Medium | Medium | Quality improvement |

## Recommendations

### For cost optimization (primary goal)
Apply prompt caching first (biggest single win). Then implement static model routing — this alone cuts costs 50-70% compared to all-Opus. Add token-efficient prompts to reduce per-request consumption. Set token budgets as guardrails.

### For speed optimization (primary goal)
Maximize parallel execution with file ownership to prevent conflicts. Use pipeline parallelism so downstream agents start as soon as upstream agents produce output. Use Sonnet over Opus where possible — faster responses mean faster cycle times.

### For quality optimization (primary goal)
Use Opus for all reasoning-heavy roles. Add self-validation to every agent. Implement multi-agent review (see Quality Assurance guide). Use specification anchoring to reduce interpretation errors. Accept the higher cost.

### For balanced optimization
Start with prompt caching and static model routing (cost). Add parallel execution (speed). Implement self-validation and specification anchoring (quality). This covers the highest-impact optimizations across all three dimensions.

## Related Resources

- [Model Selection Guide](./model-selection-guide.md) — Detailed model cost and capability comparisons
- [Decision Framework](./decision-framework.md) — Budget allocation strategies
- [Long-Running Agents](./long-running-agents.md) — Context management and token efficiency
- [Quality Assurance](./quality-assurance.md) — Multi-agent review and validation patterns
- [Deployment Guide](./deployment-guide.md) — Infrastructure-level optimization
