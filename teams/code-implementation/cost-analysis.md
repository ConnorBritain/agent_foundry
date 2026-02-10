# Cost Analysis

Detailed cost projections for the Code Implementation Team across model configurations, phases, and feature complexity levels.

---

## Phase-by-Phase Cost Breakdown (Default Configuration)

| Phase | Duration | Agents Active | Est. Input Tokens | Est. Output Tokens | Est. Total Tokens | Est. Cost |
|-------|----------|---------------|-------------------|--------------------|--------------------|-----------|
| Planning | ~10 min | 1 (sequential) | ~20K | ~10K | ~30K | ~$0.24 |
| Implementation | ~20-40 min | 3 parallel | ~200K | ~100K | ~300K | ~$19.50 |
| Code Review | ~15-25 min | 1 (sequential) | ~55K | ~25K | ~80K | ~$5.20 |
| Testing + Docs | ~15-20 min | 2 parallel | ~55K | ~25K | ~80K | ~$0.50 |
| **Total** | **~60-90 min** | | **~330K** | **~160K** | **~490K** | **~$25.44** |

### Phase 1: Planning (~$0.24)

| Agent | Model | Input Tokens | Output Tokens | Cost |
|-------|-------|-------------|---------------|------|
| Coordinator | Sonnet 4.5 | ~20K | ~10K | ~$0.24 |

### Phase 2: Implementation (~$19.50)

| Agent | Model | Input Tokens | Output Tokens | Cost |
|-------|-------|-------------|---------------|------|
| Specialist A | Opus 4.6 | ~100K | ~50K | ~$9.75 |
| Specialist B | Opus 4.6 | ~100K | ~50K | ~$9.75 |
| Test Engineer (scenarios) | Sonnet 4.5 | ~10K | ~5K | ~$0.11 |
| **Phase Total** | | **~210K** | **~105K** | **~$19.61** |

Note: Specialists A and B run concurrently. Wall-clock time is ~20-40 minutes, not 40-80 minutes.

### Phase 3: Code Review (~$5.20)

| Agent | Model | Input Tokens | Output Tokens | Cost |
|-------|-------|-------------|---------------|------|
| Code Reviewer | Opus 4.6 | ~55K | ~25K | ~$5.20 |

Includes up to 2 re-review cycles for blocker resolution.

### Phase 4: Testing + Documentation (~$0.50)

| Agent | Model | Input Tokens | Output Tokens | Cost |
|-------|-------|-------------|---------------|------|
| Test Engineer | Sonnet 4.5 | ~40K | ~20K | ~$0.48 |
| Doc Writer | Haiku 4.5 | ~15K | ~5K | ~$0.02 |
| **Phase Total** | | **~55K** | **~25K** | **~$0.50** |

---

## Model Configuration Cost Comparison

| Configuration | Opus Agents | Sonnet Agents | Haiku Agents | Est. Cost/Feature | vs Default |
|--------------|-------------|---------------|--------------|-------------------|------------|
| **Budget** | 0 | 5 | 1 | ~$10 | -60% |
| **Default** | 3 | 2 | 1 | ~$25 | baseline |
| **Premium** | 5 | 0 | 1 | ~$45 | +80% |

---

## Sensitivity Analysis

### Feature Complexity Variance

Actual token usage varies by feature complexity. These multipliers apply to the default estimates:

| Feature Complexity | Multiplier | Est. Tokens | Est. Cost (Default) |
|-------------------|------------|-------------|---------------------|
| Simple (single module, CRUD, <300 LOC) | 0.6x | ~295K | ~$15 |
| Standard (multi-module, business logic, 300-800 LOC) | 1.0x | ~490K | ~$25 |
| Complex (cross-service, state mgmt, 800-1500 LOC) | 1.5x | ~735K | ~$38 |
| Very Complex (distributed, concurrency, >1500 LOC) | 2.0x | ~980K | ~$50 |

### Retry and Iteration Costs

Review cycles and test failures trigger retries. Each retry adds cost:

| Scenario | Additional Tokens | Additional Cost |
|----------|------------------|-----------------|
| Single blocker fix, 1 re-review | ~20-30K | ~$2-4 |
| Multiple blockers, 2 re-reviews | ~40-60K | ~$5-8 |
| Test failure, 1 fix-retest cycle | ~30-50K | ~$3-6 |
| Full re-implementation of one Specialist's work | ~150K | ~$10-15 |

**Recommendation:** Budget 15-20% above estimated cost for retries. A $30 ceiling covers most standard features.

---

## Hourly Burn Rate by Configuration

| Configuration | Tokens/Hour | Est. Cost/Hour |
|--------------|-------------|----------------|
| All Opus 4.6 | ~200K | $30-50 |
| Mixed (default) | ~200K | $15-30 |
| All Sonnet 4.5 | ~200K | $5-12 |
| All Haiku 4.5 | ~200K | $0.50-1.50 |

---

## Break-Even Analysis

Comparing agent cost to developer cost for the same feature:

| Metric | Human Developer | Agent Team (Default) | Agent Team (Premium) |
|--------|----------------|---------------------|---------------------|
| Calendar time | 1-3 days | ~60-90 minutes | ~60-90 minutes |
| Developer hours | 4-16 hours | 0 (supervision only) | 0 (supervision only) |
| Cost at $150/hr | $600-$2,400 | ~$25 | ~$45 |
| Cost at $75/hr | $300-$1,200 | ~$25 | ~$45 |
| Review included | Separate PR review | Built-in code review | Built-in code review |
| Tests included | Often deferred | Built-in test generation | Built-in test generation |

**Key takeaway:** Even with multiple retries, agent execution costs are 1-2 orders of magnitude lower than equivalent human developer time. The primary cost is the human time spent reviewing agent output and validating the merge.

---

## Cost Optimization Tips

1. **Start with Budget config for prototypes.** Switch to Default for production features.
2. **Scope features tightly.** Smaller, well-defined features cost less and produce better results than large, vague ones.
3. **Provide clear specs.** Ambiguous requirements cause retries. A detailed spec saves tokens.
4. **Use hybrid mode.** Sequential mode wastes wall-clock time. Swarm mode wastes tokens on conflicts.
5. **Set a cost ceiling.** Use `max_total_cost_usd` in CONFIG to prevent runaway costs.
6. **Review the plan before implementation.** Catching scope issues in Phase 1 costs $0.24. Catching them in Phase 3 costs $20+.
7. **Reuse test scenarios.** If running similar features, the Test Engineer's scenarios can be adapted rather than written from scratch.
