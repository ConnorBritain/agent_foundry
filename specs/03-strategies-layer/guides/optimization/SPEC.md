# Optimization Playbook Specification

> **STATUS**: STATIC REFERENCE -- Extracted from master prompt. Never modified, only consulted.

## Purpose

Provide concrete, actionable techniques for reducing token consumption and costs in agent workflows. Include before/after examples, measurement methodology, and tooling guidance. Focus on practical optimizations that maintain or improve output quality while reducing spend.

## Output File

`strategies/optimization.md`

## Content Structure

### 1. Context Compression Techniques

#### Pipe-Delimited Documentation Index (Vercel Pattern)

**Before** (uncompressed, ~2500 tokens):
```markdown
# Next.js Routing

## Pages and Layouts
The App Router uses a file-system based router where folders define routes.
Each folder in the route hierarchy represents a route segment...

### page.js
A page is UI that is unique to a route. You can define pages by exporting
a component from a page.js file...

### layout.js
A layout is UI that is shared between multiple pages. On navigation,
layouts preserve state, remain interactive, and do not re-render...
```

**After** (compressed, ~400 tokens):
```
[Next.js Docs Index]|root: ./.nextjs-docs
|IMPORTANT: Prefer retrieval-led reasoning over pre-training
|01-routing:{pages.md,layouts.md,loading.md,error.md,not-found.md}
|02-data:{server-components.md,server-actions.md,fetching-patterns.md}
|03-rendering:{client-vs-server.md,streaming.md,static-dynamic.md}
|04-caching:{full-route.md,data-cache.md,revalidation.md}
```

**Compression ratio**: ~84% reduction
**Quality impact**: Vercel eval shows 100% pass rate with compressed format

#### Compression Strategies by Content Type

| Content Type | Best Compression | Expected Ratio | Notes |
|-------------|-----------------|----------------|-------|
| API references | Pipe-delimited index | 80-85% | Function signatures + file paths |
| Prose documentation | Summary + references | 60-70% | Key concepts + file pointers |
| Code examples | Skeleton + file paths | 70-80% | Pattern outline + full code in files |
| Configuration docs | YAML summary | 75-85% | Key-value pairs, option lists |
| Error messages | Error code index | 85-90% | Code + one-line description |

#### Step-by-Step Compression Process
1. Identify the full documentation corpus
2. Categorize content (API ref, prose, examples, config)
3. Extract key identifiers and structure
4. Create compressed index with file references
5. Validate with token-calculator.py
6. Test with agent to verify retrieval quality
7. Iterate until target compression ratio achieved

### 2. Lazy Loading Patterns

#### Progressive Disclosure Architecture

```
Layer 0: Always loaded (AGENTS.md)
├── System prompt, personality, core constraints
├── Compressed documentation indices
└── Budget: 5-15K tokens

Layer 1: Loaded on skill trigger (SKILL.md body)
├── Workflow instructions
├── Step-by-step process
└── Budget: <5K tokens per skill

Layer 2: Loaded on-demand (references/)
├── Detailed documentation
├── Code examples
├── Data files
└── Budget: Variable, loaded only when needed

Layer 3: Never loaded (external)
├── Full documentation sites
├── Large codebases
├── Historical data
└── Budget: Zero (accessed via MCP or web tools)
```

#### When to Lazy Load vs Eagerly Load

| Content | Load Strategy | Rationale |
|---------|--------------|-----------|
| System prompt | Eager (Layer 0) | Always needed |
| Framework docs index | Eager (Layer 0) | Frequently referenced |
| Skill metadata | Eager (Layer 0) | Needed for trigger matching |
| Skill instructions | Lazy (Layer 1) | Only when triggered |
| Reference docs | Lazy (Layer 2) | Only when skill needs detail |
| External data | On-demand (Layer 3) | Too large to pre-load |

#### Implementation Patterns

**File Reference Pattern**:
```markdown
For detailed API documentation, read: ./references/api-reference.md
For code examples, read: ./references/examples/
```

**Conditional Loading Pattern**:
```markdown
## If task involves authentication:
Read: ./references/auth-patterns.md

## If task involves database:
Read: ./references/database-patterns.md
```

**Summary + Drill-Down Pattern**:
```markdown
## Available Patterns (summaries)
- Auth: JWT + session-based, see references/auth.md for implementation
- Caching: Multi-layer cache strategy, see references/caching.md for config
- Error handling: Structured error types, see references/errors.md for catalog
```

### 3. Caching Strategies for Repeated Operations

#### Response Caching
- Cache model responses for identical or near-identical prompts
- Hash-based cache keys (prompt hash + model + temperature)
- Cache invalidation on configuration changes
- Storage: local file cache, Redis for multi-agent teams

#### Context Caching
- Reuse computed context summaries across sessions
- Cache AGENTS.md token counts (avoid re-computing)
- Cache skill validation results (until skill file changes)
- Cache cost estimates (until pricing changes)

#### Artifact Caching
- Cache intermediate artifacts (analysis results, research findings)
- Fingerprint-based invalidation (re-cache when inputs change)
- Shared artifact cache for multi-agent teams
- Example: Research team caches literature review results for synthesis phase

#### Cache Hit Rate Optimization
- Measure cache hit rate per operation type
- Target: >50% hit rate for repeated operations
- Strategies: Normalize prompts before hashing, use semantic similarity for near-misses
- Monitor cache size and implement eviction policies

### 4. Batching and Parallelization

#### Task Batching
- Group similar tasks for same-model processing
- Batch documentation generation (all docs in one Haiku session)
- Batch code reviews (all files in one Opus session)
- Batch test generation (all test files in one Sonnet session)

**Batching Savings Formula**:
```
unbatched_cost = N * (context_load_cost + task_cost)
batched_cost = context_load_cost + N * task_cost
savings = N * context_load_cost - context_load_cost
savings_percentage = (N - 1) / N * (context_load_cost / total_cost)
```

#### Parallel Execution Optimization
- Identify independent tasks for parallel execution
- Calculate optimal parallelism level:
  - Too few: wasted time
  - Too many: coordination overhead exceeds benefit
- Optimal team size formula: `sqrt(total_tasks)` as starting point, adjust based on dependency density

#### Pipeline Optimization
- Identify bottleneck phases (longest duration)
- Apply parallelism to bottleneck phases
- Stream results to next phase when possible
- Measure pipeline throughput, not just individual step speed

### 5. Measuring Token Efficiency

#### Efficiency Metrics

| Metric | Formula | Target |
|--------|---------|--------|
| Token efficiency ratio | useful_output_tokens / total_tokens | >30% |
| Cost per deliverable | total_cost / deliverables_produced | Varies by type |
| Context utilization | context_tokens_referenced / context_tokens_loaded | >60% |
| Retry overhead | retry_tokens / total_tokens | <10% |
| Coordination overhead | coordination_tokens / total_tokens | <20% |

#### Measurement Process
1. Instrument agent workflows to log token usage per operation
2. Categorize tokens: productive (task work) vs overhead (coordination, retries, context loading)
3. Calculate efficiency metrics
4. Identify lowest-efficiency operations
5. Apply optimization techniques
6. Re-measure and compare

#### Token Audit Template
```markdown
## Token Audit: [Workflow Name]
Date: [date]

### Total Usage
- Input tokens: [count]
- Output tokens: [count]
- Total tokens: [count]
- Total cost: $[amount]

### Breakdown by Phase
| Phase | Input | Output | Total | % of Total | Model |
|-------|-------|--------|-------|-----------|-------|
| [Phase 1] | | | | | |
| [Phase 2] | | | | | |

### Efficiency Analysis
- Token efficiency ratio: [%]
- Context utilization: [%]
- Retry overhead: [%]
- Coordination overhead: [%]

### Optimization Opportunities
1. [Opportunity]: Estimated savings [X]%
2. [Opportunity]: Estimated savings [Y]%

### Recommendations
- [Recommendation 1]
- [Recommendation 2]
```

### 6. Before/After Case Studies

#### Case Study 1: AGENTS.md Compression
- **Before**: 12K token uncompressed Next.js documentation
- **After**: 1.8K token compressed index with file references
- **Savings**: 85% context reduction
- **Quality impact**: No degradation (Vercel eval validated)
- **Method**: Pipe-delimited indexing with retrieval-led instructions

#### Case Study 2: Skill Trigger Optimization
- **Before**: Single trigger phrase, 44% trigger rate
- **After**: Multiple trigger patterns + examples + boundaries, 92% trigger rate
- **Savings**: 52% fewer failed skill invocations (which waste tokens on retries)
- **Method**: Added 5 trigger patterns, 3 "when to use" examples, 3 "when NOT to use" examples

#### Case Study 3: Team Coordination Optimization
- **Before**: Every agent loads full team context (500K total tokens across team)
- **After**: Agents load only role-specific context + shared minimal base (280K total)
- **Savings**: 44% token reduction
- **Method**: Partitioned context by role, shared only coordination protocol

#### Case Study 4: Model Right-Sizing
- **Before**: All-Opus team (Code Implementation), $XX per feature
- **After**: Mixed models (Opus for complex, Sonnet for standard, Haiku for docs), $XX per feature
- **Savings**: 35-45% cost reduction
- **Quality impact**: <5% quality degradation (within acceptable threshold)
- **Method**: Model selection guide applied per role

#### Case Study 5: Caching Implementation
- **Before**: Re-analyzing same codebase structure every session
- **After**: Cached codebase analysis, refreshed only on git changes
- **Savings**: 15-20K tokens per session
- **Method**: File fingerprint-based cache with git hash invalidation

### 7. Tooling for Measuring Improvements

#### Common Utilities Integration

**token-calculator.py**:
- Measure token count for any file or directory
- Compare compressed vs uncompressed formats
- Project costs based on model pricing
- Usage: `python token-calculator.py path/to/agents.md --model opus`

**cost-estimator.py**:
- Estimate workflow costs before execution
- Compare model configurations
- Sensitivity analysis (what if tokens are 20% higher?)
- Usage: `python cost-estimator.py --team code-implementation --workflow feature`

**agents-md-compressor.py**:
- Compress documentation into optimized format
- Measure compression ratio
- Validate compressed format preserves essential information
- Usage: `python agents-md-compressor.py --input docs/ --output agents.md --target-tokens 2000`

#### Custom Measurement Scripts

Provide templates for:
- Token usage logger (wraps API calls, logs usage)
- Efficiency dashboard generator (reads logs, produces report)
- A/B test analyzer (compares two configurations statistically)
- Budget alert system (monitors usage against limits)

#### Optimization Workflow
1. **Baseline**: Measure current token usage and costs
2. **Identify**: Find highest-cost operations and lowest-efficiency areas
3. **Hypothesize**: Select optimization technique likely to help
4. **Implement**: Apply optimization to test configuration
5. **Measure**: Run same workflow with optimized configuration
6. **Compare**: Statistical comparison of before/after
7. **Deploy**: Roll out optimization if improvement confirmed
8. **Monitor**: Track metrics post-deployment for regression

## Writing Guidelines

- Every technique must include a concrete before/after example
- Include actual token counts and cost figures (with calculation methodology)
- Provide copy-paste code for measurement scripts
- Show diminishing returns (when is further optimization not worth it)
- Include "quick wins" section for immediate impact optimizations
- Order techniques by effort-to-impact ratio (easy wins first)

## Dependencies

- Common utility scripts (token-calculator.py, cost-estimator.py, agents-md-compressor.py)
- Token pricing data for cost calculations
- Benchmark data from Vercel eval study

## Cross-References

- **Strategies Layer**: `specs/03-strategies-layer/SPEC.md`
- **Long-Running Agents**: `specs/03-strategies-layer/guides/long-running-agents/SPEC.md` (cost optimization over time)
- **Model Selection**: `specs/03-strategies-layer/guides/model-selection/SPEC.md` (model right-sizing)
- **Common Utilities**: `specs/01-common-layer/utilities/SPEC.md` (measurement tools)
- **Common AGENTS.md**: `specs/01-common-layer/agents-md-templates/SPEC.md` (compression format)
