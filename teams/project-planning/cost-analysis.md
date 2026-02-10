# Cost Analysis

Detailed cost projections for the Project Planning Team across model configurations, phases, and scenarios.

---

## Phase-by-Phase Cost Breakdown (Default Configuration)

| Phase | Duration | Agents Active | Est. Input Tokens | Est. Output Tokens | Est. Total Tokens | Est. Cost |
|-------|----------|---------------|-------------------|--------------------|--------------------|-----------|
| Configuration | ~5 min | 1 | ~10K | ~5K | ~15K | ~$0.90 |
| Requirements Analysis | ~15 min | 1 | ~30K | ~15K | ~45K | ~$2.70 |
| Task Decomposition | ~20 min | 1 | ~40K | ~20K | ~60K | ~$3.60 |
| Risk + Resource (parallel) | ~15 min | 2 parallel | ~65K | ~35K | ~100K | ~$11.40 |
| Scheduling | ~10 min | 1 | ~25K | ~15K | ~40K | ~$2.40 |
| Integration | ~10 min | 1 | ~20K | ~10K | ~30K | ~$0.75 |
| Final Review + Export | ~5 min | 2 parallel | ~15K | ~5K | ~20K | ~$1.00 |
| **Total** | **~1.5 hrs** | | **~205K** | **~105K** | **~290K** | **~$22.75** |

Note: The parallel phases (4 and 7) run two agents simultaneously but do not increase total tokens because both agents consume from the same task list.

### Phase 1: Configuration (~$0.90)

| Agent | Model | Input Tokens | Output Tokens | Cost |
|-------|-------|-------------|---------------|------|
| Coordinator | Sonnet 4.5 | ~10K | ~5K | ~$0.90 |

### Phase 2: Requirements Analysis (~$2.70)

| Agent | Model | Input Tokens | Output Tokens | Cost |
|-------|-------|-------------|---------------|------|
| Requirements Analyst | Sonnet 4.5 | ~30K | ~15K | ~$2.70 |

### Phase 3: Task Decomposition (~$3.60)

| Agent | Model | Input Tokens | Output Tokens | Cost |
|-------|-------|-------------|---------------|------|
| Task Decomposer | Sonnet 4.5 | ~40K | ~20K | ~$3.60 |

### Phase 4: Risk Assessment + Resource Allocation (~$11.40)

| Agent | Model | Input Tokens | Output Tokens | Cost |
|-------|-------|-------------|---------------|------|
| Risk Assessor | Sonnet 4.5 | ~25K | ~15K | ~$2.40 |
| Resource Allocator | Opus 4.6 | ~40K | ~20K | ~$9.00 |
| **Phase Total** | | **~65K** | **~35K** | **~$11.40** |

Note: This is the most expensive phase because the Resource Allocator runs on Opus 4.6 for nuanced trade-off reasoning. The Risk Assessor and Resource Allocator execute in parallel, so wall-clock time is ~15 minutes (the longer of the two).

### Phase 5: Scheduling (~$2.40)

| Agent | Model | Input Tokens | Output Tokens | Cost |
|-------|-------|-------------|---------------|------|
| Scheduler | Sonnet 4.5 | ~25K | ~15K | ~$2.40 |

### Phase 6: Integration and Documentation (~$0.75)

| Agent | Model | Input Tokens | Output Tokens | Cost |
|-------|-------|-------------|---------------|------|
| Integration Planner | Haiku 4.5 | ~20K | ~10K | ~$0.75 |

### Phase 7: Final Review + Export (~$1.00)

| Agent | Model | Input Tokens | Output Tokens | Cost |
|-------|-------|-------------|---------------|------|
| Coordinator | Sonnet 4.5 | ~8K | ~2K | ~$0.48 |
| Integration Planner | Haiku 4.5 | ~7K | ~3K | ~$0.25 |
| **Phase Total** | | **~15K** | **~5K** | **~$0.73** |

---

## Model Configuration Cost Comparison

| Configuration | Opus Agents | Sonnet Agents | Haiku Agents | Total Tokens | Est. Cost | Savings vs Default |
|--------------|-------------|---------------|-------------|-------------|-----------|-------------------|
| Budget | 0 | 6 | 1 | ~290K | ~$16 | -$7 (-30%) |
| **Default** | **1** | **5** | **1** | **~290K** | **~$23** | **baseline** |
| Premium | 6 | 0 | 1 | ~290K | ~$55 | +$32 (+140%) |

### Per-Phase Cost by Configuration

| Phase | Budget | Default | Premium |
|-------|--------|---------|---------|
| Configuration | ~$0.90 | ~$0.90 | ~$2.25 |
| Requirements Analysis | ~$2.70 | ~$2.70 | ~$6.75 |
| Task Decomposition | ~$3.60 | ~$3.60 | ~$9.00 |
| Risk + Resource | ~$6.00 | ~$11.40 | ~$15.00 |
| Scheduling | ~$2.40 | ~$2.40 | ~$6.00 |
| Integration | ~$0.75 | ~$0.75 | ~$1.80 |
| Final Review | ~$0.50 | ~$1.00 | ~$2.50 |
| **Total** | **~$16** | **~$23** | **~$55** |

---

## Sensitivity Analysis

### Token Usage Variance

Actual token usage varies by project complexity. These multipliers apply to the default estimates:

| Project Complexity | Multiplier | Est. Total Tokens | Est. Cost (Default) |
|-------------------|------------|-------------------|---------------------|
| Simple (single team, <20 tasks) | 0.6x | ~175K | ~$14 |
| Standard (multi-workstream, 20-50 tasks) | 1.0x | ~290K | ~$23 |
| Complex (cross-team, 50-100 tasks) | 1.5x | ~435K | ~$35 |
| Enterprise (SAFe PI, 100+ features) | 2.5x | ~725K | ~$58 |

### Retry and Iteration Costs

Quality gate failures trigger retries. Each retry adds cost:

| Scenario | Additional Tokens | Additional Cost |
|----------|------------------|-----------------|
| Requirements revision (user clarification) | ~10-15K | ~$1-2 |
| Single agent output rejected, 1 retry | ~15-25K | ~$2-5 |
| Phase gate fails, 1 agent redoes work | ~30-60K | ~$3-9 |
| Full Risk+Resource redo (worst case) | ~80-100K | ~$10-14 |

**Recommendation:** Budget 15% above estimated cost for retries. A $23 default run should budget $27.

### Impact of Framework Choice

The selected framework affects token consumption:

| Framework | Token Impact | Rationale |
|-----------|-------------|-----------|
| Scrum | Baseline | Standard complexity |
| Kanban | -15% | Lighter planning overhead |
| Shape Up | -10% | Fewer ceremonies, simpler structure |
| Waterfall | +10% | More detailed phase gates and traceability |
| SAFe | +40-60% | Multiple teams, program-level planning, PI objectives |

### Impact of Project Duration

Longer projects require more tasks and scheduling work:

| Duration | Token Multiplier | Est. Cost (Default) |
|----------|-----------------|---------------------|
| 4 weeks | 0.7x | ~$16 |
| 8 weeks | 0.85x | ~$20 |
| 12 weeks (default) | 1.0x | ~$23 |
| 26 weeks | 1.4x | ~$32 |
| 52 weeks | 1.8x | ~$41 |

---

## Tool Integration Costs

### MCP Server Token Overhead

MCP server calls add minimal token overhead:

| Tool | Calls per Session | Tokens per Call | Total Overhead |
|------|------------------|-----------------|----------------|
| Linear | ~20-50 issue creates | ~200 | ~4K-10K |
| Jira | ~20-50 issue creates | ~300 | ~6K-15K |
| Google Calendar | ~5-15 events | ~150 | ~750-2.25K |

MCP overhead is included in the Integration Planner's token budget and typically accounts for less than 5% of total cost.

---

## Break-Even Analysis

Comparing agent cost to human planning cost:

| Metric | Human Planner | Agent Team (Default) | Agent Team (Premium) |
|--------|---------------|---------------------|---------------------|
| Calendar time | 1-3 days | ~1.5 hours | ~1.5 hours |
| Planner hours | 8-24 hours | 0 (supervision only) | 0 (supervision only) |
| Cost at $150/hr | $1,200-$3,600 | ~$23 | ~$55 |
| Cost at $75/hr | $600-$1,800 | ~$23 | ~$55 |
| Output consistency | Variable | Consistent structure | Highest quality |
| Framework adherence | Depends on experience | Strict adherence | Strict adherence |
| Tool integration | Manual (hours) | Automatic (minutes) | Automatic (minutes) |

**Key takeaway:** Even with Premium configuration and multiple retries, agent execution is 1-2 orders of magnitude cheaper than equivalent human planning time. The primary cost is the human time reviewing and refining the agent's output.

---

## Cost Optimization Tips

1. **Start with Budget config for simple sprints.** Switch to Default when prioritization quality matters.
2. **Use Kanban or Shape Up for lighter projects.** These frameworks require fewer tokens than Scrum or SAFe.
3. **Pre-groom your vision statement.** A well-defined vision reduces Requirements Analyst tokens by 20-30% and eliminates clarification loops.
4. **Skip calendar integration for draft plans.** Set `calendar_integration: none` to save Integration Planner tokens.
5. **Run in hybrid mode.** Parallel phases save wall-clock time without increasing token cost.
6. **Review and prune after Phase 3.** If the task decomposition is solid, subsequent phases run efficiently.
7. **Reuse configurations across sprints.** For recurring sprint planning, the Coordinator's configuration phase is nearly free after the first run.
8. **Monitor the Resource Allocator closely.** As the only Opus agent in Default config, it consumes ~40% of the total cost. If its output is acceptable with Sonnet, switch to Budget config and save ~$7 per session.
