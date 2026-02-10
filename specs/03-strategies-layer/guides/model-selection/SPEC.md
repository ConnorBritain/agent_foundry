# Model Selection Strategy Specification

> **STATUS**: STATIC REFERENCE -- Extracted from master prompt. Never modified, only consulted.

## Purpose

Provide a universal guide for choosing models across all team templates. Help users make data-driven model selection decisions based on task type, programming language, framework, cost constraints, and quality requirements.

## Output File

`strategies/model-selection.md`

## Content Structure

### 1. General Principles

#### Task-to-Model Mapping

| Task Category | Recommended Model | Rationale |
|--------------|-------------------|-----------|
| Strategic planning, creative synthesis | Opus 4.6 | Highest reasoning capability |
| Standard coding, coordination | Sonnet 4.5 | Best cost/performance balance |
| High-volume, repetitive tasks | Haiku 4.5 | Cost-effective for simple work |
| Swift/Kotlin development | minimax2.5 | Benchmark leader for these languages |
| Chinese language workflows | Alibaba models | Native language optimization |

#### Cost Optimization Strategies
- Right-sizing: Match model capability to task complexity
- Phased approach: Start with cheaper models, upgrade only when quality insufficient
- Batch processing: Use cheaper models for bulk operations
- Caching: Avoid re-processing with expensive models
- Model switching: Different models for different workflow phases

### 2. Language-Specific Recommendations

#### Swift
- **Primary recommendation**: minimax2.5
- **Evidence**: Current benchmark leader for Swift and SwiftUI code generation
- **When to use Opus instead**: Complex architectural decisions, multi-framework integration, security-critical code
- **Cost impact**: ~15% reduction vs Opus 4.6
- **Trade-offs**: Slightly less sophisticated architectural reasoning, potentially less awareness of Swift ecosystem nuances

#### Kotlin
- **Primary recommendation**: minimax2.5
- **Evidence**: Benchmark leader for Kotlin and Jetpack Compose
- **When to use Opus instead**: Complex state management patterns, architectural patterns requiring deep reasoning
- **Cost impact**: ~15% reduction vs Opus 4.6
- **Trade-offs**: May miss subtle Kotlin coroutine edge cases

#### Python
- **Primary recommendation**: Opus 4.6
- **Evidence**: Benchmark leader for Python code generation and comprehension
- **Alternatives**: Sonnet 4.5 for simple CRUD and scripting (40% cost savings), Haiku 4.5 for boilerplate generation
- **Framework-specific**:
  - FastAPI complex endpoints: Opus 4.6
  - Django admin/CRUD: Sonnet 4.5
  - Simple scripts: Haiku 4.5

#### JavaScript/TypeScript
- **Primary recommendation**: Opus 4.6
- **Evidence**: Benchmark leader for JS/TS code generation
- **When to downgrade to Sonnet 4.5**: Standard React components, simple API routes, configuration files, test boilerplate
- **When to stay on Opus**: Complex state management, real-time systems, WebSocket implementations, performance-critical code

#### Rust
- **Primary recommendation**: Opus 4.6
- **Evidence**: Complexity of ownership/borrowing system requires strongest reasoning
- **Rationale**: Rust's type system and memory safety guarantees demand deep reasoning
- **Alternative**: Sonnet 4.5 for straightforward implementations with clear patterns
- **Never use Haiku for**: Unsafe code blocks, lifetime annotations, complex trait implementations

#### Go
- **Primary recommendation**: Opus 4.6 for concurrency patterns, Sonnet 4.5 for standard code
- **Rationale**: Go concurrency (goroutines, channels, select) benefits from stronger reasoning
- **Cost optimization**: Use Sonnet 4.5 for HTTP handlers, struct definitions, interface implementations
- **Use Opus for**: Complex concurrent systems, race condition analysis, performance optimization

### 3. Framework-Specific Guidance

#### Next.js Patterns by Complexity

| Pattern Complexity | Recommended Model | Examples |
|-------------------|-------------------|---------|
| Simple | Haiku 4.5 | Static pages, basic layouts |
| Standard | Sonnet 4.5 | Server components, data fetching, routing |
| Complex | Opus 4.6 | Server actions, streaming, caching strategies, middleware |
| Architecture | Opus 4.6 | App Router migration, ISR strategies, multi-tenant |

#### FastAPI Patterns by Complexity

| Pattern Complexity | Recommended Model | Examples |
|-------------------|-------------------|---------|
| Simple | Haiku 4.5 | Basic CRUD endpoints, Pydantic models |
| Standard | Sonnet 4.5 | Dependency injection, middleware, auth |
| Complex | Opus 4.6 | Async patterns, WebSocket, background tasks |
| Architecture | Opus 4.6 | Microservice design, event-driven systems |

### 4. When to Upgrade Models

#### Haiku to Sonnet
- **Triggers**:
  - Output quality consistently below acceptable threshold
  - Task requires multi-step reasoning (>3 steps)
  - Code review finds logic errors in Haiku output
  - Documentation needs technical depth beyond surface level
- **Cost impact**: ~3-4x increase per token
- **ROI threshold**: Upgrade when time spent fixing Haiku output exceeds cost difference
- **Decision rule**: If >20% of Haiku outputs require manual correction, upgrade to Sonnet

#### Sonnet to Opus
- **Triggers**:
  - Complex architectural decisions being made
  - Security-critical code generation
  - Multi-system integration requiring deep reasoning
  - Creative synthesis or strategic planning tasks
  - Sonnet producing architecturally unsound solutions
- **Cost impact**: ~5x increase per token
- **ROI threshold**: Upgrade when the cost of incorrect architecture exceeds model cost difference
- **Decision rule**: If task failure cost >$100, use Opus regardless of token cost

#### Opus to Specialized Models
- **Triggers**:
  - Language-specific benchmarks strongly favor alternatives (Swift/Kotlin → minimax2.5)
  - Domain-specific models available (Chinese language → Alibaba)
  - Cost optimization needed without quality loss
- **Verification**: Always A/B test before switching from Opus to specialized
- **Fallback plan**: Keep Opus available for tasks where specialized model underperforms

### 5. A/B Testing Process for Model Choices

#### Setup
1. Define the task set (minimum 20 representative tasks)
2. Establish quality metrics (correctness, completeness, style adherence)
3. Run identical tasks through both models
4. Blind evaluation (evaluator doesn't know which model produced which output)

#### Execution
1. **Baseline**: Run task set through current model, record quality scores and costs
2. **Challenger**: Run same task set through candidate model, record quality scores and costs
3. **Compare**: Statistical comparison of quality scores
4. **Cost analysis**: Calculate cost difference and quality-adjusted cost

#### Decision Criteria
- Switch models if: Quality difference <5% AND cost reduction >20%
- Stay with current if: Quality difference >10% regardless of cost
- Further testing if: Quality difference 5-10% (expand task set)

#### Monitoring After Switch
- Run quality checks on first 50 tasks
- Compare to baseline metrics
- Maintain rollback capability for 2 weeks

### 6. Monitoring Metrics and Red Flags

#### Metrics to Track
- **Task completion rate**: Percentage of tasks completed without human intervention
- **Error rate**: Frequency of incorrect outputs requiring correction
- **Token efficiency**: Tokens consumed per successful task completion
- **Latency**: Time from task submission to completion
- **Cost per task**: Total cost including retries and corrections
- **Quality score**: Domain-specific quality metric (code review scores, factual accuracy, etc.)

#### Red Flags (Immediate Action Required)
- Task completion rate drops below 80%
- Error rate exceeds 15% for Opus, 25% for Sonnet, 35% for Haiku
- Token usage per task increases >30% without task complexity change
- Quality scores decline for 3 consecutive measurement periods
- Cost per task exceeds budget allocation by >50%

#### Red Flag Response Protocol
1. Check if model API behavior changed (version updates)
2. Review task distribution for complexity drift
3. A/B test current model against alternatives
4. Consider model upgrade if quality is root cause
5. Consider prompt/context optimization if efficiency is root cause

### 7. Team Template Model Recommendations

Quick reference for model assignments across team templates:

#### Code Implementation Team
| Role | Default Model | Alternative | When to Switch |
|------|--------------|-------------|----------------|
| Coordinator | Sonnet 4.5 | Opus 4.6 | Complex project architecture |
| Implementation | Opus 4.6 | minimax2.5 | Swift/Kotlin projects |
| Code Reviewer | Opus 4.6 | Sonnet 4.5 | Simple CRUD reviews |
| Test Engineer | Sonnet 4.5 | Haiku 4.5 | Boilerplate test generation |
| Doc Writer | Haiku 4.5 | Sonnet 4.5 | Technical depth needed |

#### Project Planning Team
| Role | Default Model | Alternative | When to Switch |
|------|--------------|-------------|----------------|
| Coordinator | Sonnet 4.5 | Opus 4.6 | Complex multi-team coordination |
| Vision Analyzer | Sonnet 4.5 | Opus 4.6 | Ambiguous or broad goals |
| Task Decomposer | Sonnet 4.5 | Haiku 4.5 | Well-defined task lists |
| Prioritization | Opus 4.6 | Sonnet 4.5 | Clear priority criteria |
| Doc Generator | Haiku 4.5 | Sonnet 4.5 | Stakeholder-facing docs |

#### Content Creation Team
| Role | Default Model | Alternative | When to Switch |
|------|--------------|-------------|----------------|
| Coordinator/Editor | Opus 4.6 | Sonnet 4.5 | Straightforward content |
| Researcher | Sonnet 4.5 | Opus 4.6 | Complex/academic research |
| Drafter | Sonnet 4.5 | Haiku 4.5 | Template-based content |
| Humanizer | Sonnet 4.5 | Opus 4.6 | Nuanced voice matching |
| Fact-Checker | Haiku 4.5 | Sonnet 4.5 | Technical claims |

#### C-Suite Team
| Role | Default Model | Alternative | When to Switch |
|------|--------------|-------------|----------------|
| CEO/Strategy | Opus 4.6 | - | Always use strongest model |
| CFO/Finance | Sonnet 4.5 | Opus 4.6 | Complex financial modeling |
| CMO/Marketing | Sonnet 4.5 | Opus 4.6 | Competitive strategy |
| CTO/Product | Sonnet 4.5 | Opus 4.6 | Technical architecture |
| COO/Operations | Sonnet 4.5 | Haiku 4.5 | Standard process docs |

#### Research Deep-Dive Team
| Role | Default Model | Alternative | When to Switch |
|------|--------------|-------------|----------------|
| Coordinator | Opus 4.6 | - | Always use strongest model |
| Literature Review | Sonnet 4.5 | Haiku 4.5 | Source cataloging only |
| Data Analyst | Sonnet 4.5 | Opus 4.6 | Complex statistical analysis |
| Synthesis Writer | Sonnet 4.5 | Opus 4.6 | Academic publication |

## Writing Guidelines

- Include specific benchmark references with dates and sources
- Provide dollar-amount cost comparisons, not just relative percentages
- Include concrete code examples showing quality differences between models
- Present trade-offs honestly; no model is universally best
- Update cadence recommendation: monthly review of benchmark data

## Dependencies

- Current model pricing data from Anthropic, minimax, and Alibaba
- Latest benchmark results for language-specific comparisons
- Team template specifications for role-model mapping

## Cross-References

- **Strategies Layer**: `specs/03-strategies-layer/SPEC.md`
- **Harness Comparison**: `specs/03-strategies-layer/guides/harness-comparison/SPEC.md` (harness-specific model support)
- **Optimization Guide**: `specs/03-strategies-layer/guides/optimization/SPEC.md` (cost optimization techniques)
- **Team Templates**: `specs/02-teams-layer/SPEC.md` (MODEL_CONFIGS.md per team)
