# Model Selection Guide

> How to choose the right Claude model for each agent role in your Agent Foundry teams.

## Overview

Every agent in an Agent Foundry team runs on a Claude model. The model you assign to each agent determines its reasoning depth, speed, cost, and output quality. Choosing well means your team runs faster, costs less, and produces better results. Choosing poorly means you either overpay for simple tasks or get poor results on complex ones.

Claude currently offers three model tiers: Opus, Sonnet, and Haiku. Each tier exists for a reason — Opus for deep reasoning on hard problems, Sonnet for balanced performance on most tasks, and Haiku for high-volume work where speed and cost matter more than nuance. The right model for an agent depends entirely on what that agent does.

This guide provides concrete guidance for mapping agent roles to models, including cost analysis, latency expectations, and a decision matrix you can apply to any team configuration.

## Model Tiers at a Glance

| Property | Opus 4.6 | Sonnet 4.5 | Haiku 4.5 |
|---|---|---|---|
| **Model ID** | `claude-opus-4-6` | `claude-sonnet-4-5-20250929` | `claude-haiku-4-5-20251001` |
| **Context Window** | 200K tokens | 200K tokens | 200K tokens |
| **Max Output** | 32K tokens | 16K tokens | 8K tokens |
| **Input Cost** | $15 / 1M tokens | $3 / 1M tokens | $0.80 / 1M tokens |
| **Output Cost** | $75 / 1M tokens | $15 / 1M tokens | $4 / 1M tokens |
| **Prompt Caching (Write)** | $18.75 / 1M tokens | $3.75 / 1M tokens | $1.00 / 1M tokens |
| **Prompt Caching (Read)** | $1.50 / 1M tokens | $0.30 / 1M tokens | $0.08 / 1M tokens |
| **Relative Speed** | Slowest | Medium | Fastest |
| **Reasoning Depth** | Deepest | Strong | Adequate |
| **Best For** | Architecture, coordination, complex analysis | Feature implementation, code generation, review | Testing, formatting, high-volume simple tasks |

## Opus 4.6 — The Strategic Thinker

### When to Use

Opus is your most capable and most expensive model. Reserve it for roles where reasoning quality directly determines project success.

**Ideal agent roles:**
- **Orchestrator / Coordinator**: The agent that breaks down complex projects into tasks, assigns work to other agents, resolves conflicts, and makes architectural decisions. This role requires understanding the full project context and making nuanced judgments.
- **Lead Architect**: Designing system architecture, choosing patterns, making technology decisions that cascade through the entire project.
- **Code Reviewer (critical paths)**: Reviewing security-sensitive code, performance-critical algorithms, or complex business logic where subtle bugs have high impact.
- **Debugging Agent (hard bugs)**: When an agent needs to reason across multiple files, trace execution paths, and form hypotheses about non-obvious failures.
- **Specification Writer**: Translating ambiguous requirements into precise technical specifications that other agents will implement.

### When NOT to Use

Do not use Opus for:
- Writing boilerplate code or CRUD endpoints.
- Running tests and reporting results.
- Formatting, linting, or documentation generation.
- Any task where a Sonnet agent produces equivalent results.

### Cost Example

A typical orchestrator session might consume 50K input tokens and 10K output tokens:
- **Opus cost**: (50K x $15/1M) + (10K x $75/1M) = $0.75 + $0.75 = **$1.50 per session**
- **With prompt caching**: If 40K tokens are cached reads: (40K x $1.50/1M) + (10K x $15/1M) + (10K x $75/1M) = $0.06 + $0.15 + $0.75 = **$0.96 per session**

### Configuration

```yaml
agents:
  orchestrator:
    model: claude-opus-4-6
    max_tokens: 16384
    temperature: 0.3  # Lower temperature for more deterministic coordination
    budget:
      max_cost_per_session: 5.00
      warning_threshold: 3.00
```

## Sonnet 4.5 — The Reliable Workhorse

### When to Use

Sonnet is the default choice for most agent roles. It offers strong reasoning at a fraction of Opus cost, with faster response times. When in doubt, start with Sonnet.

**Ideal agent roles:**
- **Feature Developer**: Implementing new features, writing business logic, building API endpoints. Sonnet handles multi-file changes and understands architectural patterns well.
- **Frontend Developer**: Building UI components, implementing designs, writing CSS/JS/TS. Sonnet produces clean, idiomatic frontend code.
- **Backend Developer**: API development, database queries, service integration. The balance of speed and quality fits iterative development cycles.
- **Code Reviewer (standard)**: Reviewing typical pull requests for correctness, style, and best practices.
- **Refactoring Agent**: Restructuring code, extracting functions, improving modularity. Sonnet follows instructions precisely and handles multi-file refactors well.
- **Documentation Writer**: Writing technical documentation, API docs, code comments. Strong writing quality without Opus pricing.
- **Integration Agent**: Connecting services, setting up configurations, writing glue code.

### When NOT to Use

Consider Opus instead when:
- The task requires reasoning across 10+ interconnected files with complex dependencies.
- Architectural decisions have long-term consequences that are expensive to reverse.
- The agent is coordinating other agents and needs to understand the full project state.

Consider Haiku instead when:
- The task is highly repetitive with predictable patterns.
- Speed matters more than nuance (e.g., running the same transformation across 50 files).
- The output will be validated by another agent or automated test anyway.

### Cost Example

A feature development session might consume 80K input tokens and 15K output tokens:
- **Sonnet cost**: (80K x $3/1M) + (15K x $15/1M) = $0.24 + $0.225 = **$0.465 per session**
- **With prompt caching**: If 60K tokens are cached: (60K x $0.30/1M) + (20K x $3/1M) + (15K x $15/1M) = $0.018 + $0.06 + $0.225 = **$0.303 per session**

### Configuration

```yaml
agents:
  feature-developer:
    model: claude-sonnet-4-5-20250929
    max_tokens: 12288
    temperature: 0.5  # Moderate temperature for creative but consistent code
    budget:
      max_cost_per_session: 2.00
      warning_threshold: 1.50
```

## Haiku 4.5 — The Speed Runner

### When to Use

Haiku is fast and cheap. Use it for high-volume tasks where throughput matters more than reasoning depth, and where outputs are validated by other systems.

**Ideal agent roles:**
- **Test Writer**: Generating unit tests, integration tests, and test fixtures. Test correctness is validated by running the tests, so imperfect reasoning is caught automatically.
- **Test Runner / Reporter**: Executing test suites, parsing results, generating reports. Minimal reasoning needed.
- **Formatter / Linter Agent**: Running code formatters, applying style fixes, fixing lint warnings. Pattern-matching work that Haiku handles well.
- **File Transformer**: Applying the same transformation across many files (e.g., updating imports, renaming variables, migrating syntax).
- **Log Analyzer**: Parsing build logs, test output, and error messages to extract structured information.
- **Triage Agent**: Initial classification of issues, routing tasks to appropriate agents, simple status checks.
- **Boilerplate Generator**: Creating CRUD endpoints, model definitions, configuration files from templates.

### When NOT to Use

Do not use Haiku for:
- Any coordination or orchestration role.
- Complex architectural decisions or design work.
- Security-sensitive code review.
- Tasks requiring nuanced understanding of business logic.
- Writing user-facing documentation that requires strong prose.

### Cost Example

A test-writing session might consume 40K input tokens and 8K output tokens:
- **Haiku cost**: (40K x $0.80/1M) + (8K x $4/1M) = $0.032 + $0.032 = **$0.064 per session**
- **With prompt caching**: If 30K tokens are cached: (30K x $0.08/1M) + (10K x $0.80/1M) + (8K x $4/1M) = $0.0024 + $0.008 + $0.032 = **$0.042 per session**

### Configuration

```yaml
agents:
  test-writer:
    model: claude-haiku-4-5-20251001
    max_tokens: 4096
    temperature: 0.2  # Low temperature for predictable test output
    budget:
      max_cost_per_session: 0.50
      warning_threshold: 0.30
```

## Cost Comparison by Team Configuration

### Scenario: Building a Full-Stack Feature

A team of 5 agents builds a new feature over approximately 3 hours of agent time.

| Agent Role | Model | Sessions | Est. Cost/Session | Total Cost |
|---|---|---|---|---|
| Orchestrator | Opus 4.6 | 5 | $1.50 | $7.50 |
| Backend Dev | Sonnet 4.5 | 8 | $0.47 | $3.76 |
| Frontend Dev | Sonnet 4.5 | 8 | $0.47 | $3.76 |
| Test Engineer | Haiku 4.5 | 12 | $0.06 | $0.72 |
| Code Reviewer | Sonnet 4.5 | 6 | $0.35 | $2.10 |
| **Total** | | **39** | | **$17.84** |

### Anti-pattern: All Opus

The same team using Opus for every role:

| Agent Role | Model | Sessions | Est. Cost/Session | Total Cost |
|---|---|---|---|---|
| All 5 agents | Opus 4.6 | 39 | $1.50 avg | **$58.50** |

**Opus-everywhere costs 3.3x more** with negligible quality improvement for test writing and formatting tasks.

### Anti-pattern: All Haiku

| Agent Role | Model | Sessions | Est. Cost/Session | Total Cost |
|---|---|---|---|---|
| All 5 agents | Haiku 4.5 | 39 | $0.06 avg | **$2.34** |

Cheap, but the orchestrator will make poor coordination decisions, the developers will produce architecturally inconsistent code, and you will spend more time on rework than you saved.

## Decision Matrix

Use this matrix to assign models to agent roles:

```
START: What does this agent do?
  |
  |-- Coordinates other agents or makes architectural decisions?
  |     YES --> Opus 4.6
  |     NO  --> Continue
  |
  |-- Writes production code or reviews code for correctness?
  |     YES --> Is the code security-critical or architecturally complex?
  |               YES --> Opus 4.6
  |               NO  --> Sonnet 4.5
  |     NO  --> Continue
  |
  |-- Writes documentation or specifications?
  |     YES --> Is it user-facing or requires nuanced writing?
  |               YES --> Sonnet 4.5
  |               NO  --> Haiku 4.5
  |     NO  --> Continue
  |
  |-- Runs tests, formats code, or processes structured data?
  |     YES --> Haiku 4.5
  |     NO  --> Continue
  |
  |-- Is the output validated by automated systems (tests, CI)?
  |     YES --> Haiku 4.5 (cheapest, validated by automation)
  |     NO  --> Sonnet 4.5 (safe default)
```

## Latency Considerations

Response latency affects the overall team execution time, especially for agents on the critical path.

| Model | Time to First Token | Typical Full Response | Impact |
|---|---|---|---|
| Opus 4.6 | 2-5 seconds | 30-120 seconds | Acceptable for orchestration (runs infrequently) |
| Sonnet 4.5 | 1-3 seconds | 10-45 seconds | Good for iterative development loops |
| Haiku 4.5 | <1 second | 3-15 seconds | Ideal for high-frequency, short-task agents |

**Critical path optimization**: If your orchestrator (Opus) is blocking other agents while it reasons, consider breaking orchestration into two phases — a quick Sonnet-based task router for simple assignments and an Opus-based strategic planner for complex decisions.

## Model Routing Patterns

### Tiered Routing

Start with a cheaper model and escalate to a more capable one if the task proves difficult.

```yaml
routing:
  strategy: tiered
  tiers:
    - model: claude-haiku-4-5-20251001
      condition: "task.complexity == 'low'"
    - model: claude-sonnet-4-5-20250929
      condition: "task.complexity == 'medium' OR haiku.failed"
    - model: claude-opus-4-6
      condition: "task.complexity == 'high' OR sonnet.failed"
```

### Confidence-Based Routing

Let the initial model assess its own confidence. If confidence is low, escalate.

```yaml
routing:
  strategy: confidence
  initial_model: claude-sonnet-4-5-20250929
  escalation_model: claude-opus-4-6
  confidence_threshold: 0.7
  escalation_prompt: "Rate your confidence in this solution from 0 to 1."
```

## Recommendations

### For most teams
Use Opus for the orchestrator, Sonnet for developers and reviewers, and Haiku for testers and formatters. This balances cost and quality.

### For budget-constrained projects
Use Sonnet for the orchestrator (it handles coordination well for straightforward projects), Sonnet for primary developers, and Haiku for everything else. Reserve Opus for manual escalation when Sonnet struggles.

### For quality-critical projects
Use Opus for the orchestrator, architect, and code reviewer. Use Sonnet for all development roles. Use Haiku only for fully automated tasks with test validation.

### For high-throughput projects
Use aggressive prompt caching across all tiers. Route repetitive tasks to Haiku. Run Sonnet agents in parallel rather than running fewer Opus agents serially.

### For experimentation
Start every agent on Sonnet. Run your workflow. Identify which agents are bottlenecks (promote to Opus) and which produce simple outputs (demote to Haiku). Iterate.

## Related Resources

- [Harness Comparison](./harness-comparison.md) — Choose the right coding harness for each agent
- [Optimization Guide](./optimization-guide.md) — Prompt caching, token budgeting, and cost reduction
- [Decision Framework](./decision-framework.md) — Team composition and parallel execution strategies
- [Long-Running Agents](./long-running-agents.md) — Managing agents that exceed context windows
