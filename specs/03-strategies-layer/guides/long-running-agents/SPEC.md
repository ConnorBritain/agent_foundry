# Long-Running Agent Strategies Specification

> **STATUS**: STATIC REFERENCE -- Extracted from master prompt. Never modified, only consulted.

## Purpose

Provide a comprehensive guide for managing extended agent sessions that run for hours or across multiple days. Cover session persistence, context window management, cost optimization over time, error recovery patterns, and real-time monitoring.

## Output File

`strategies/long-running-agents.md`

## Content Structure

### 1. Session Management

#### When to Persist State

Define clear triggers for state persistence based on:

| Trigger | Threshold | Action |
|---------|-----------|--------|
| Session duration | >30 minutes | Enable checkpointing |
| Token usage | >50K tokens consumed | Create state snapshot |
| Multi-day workflow | Any cross-day boundary | Mandatory checkpoint |
| Phase transition | Between workflow phases | Save phase outputs |
| Error occurrence | Any recoverable error | Checkpoint before retry |
| Cost milestone | Every $10 spent | Financial checkpoint |

#### Checkpoint Strategies

**File-Based Checkpointing** (Recommended for most workflows):
- Store checkpoint files in `shared-state/checkpoints/`
- Use timestamped JSON files with structured state
- Include: current phase, completed work, pending tasks, accumulated context summary
- Example file structure and naming convention

**Database-Backed Checkpointing** (For production/enterprise):
- SQLite for local development
- PostgreSQL for team workflows
- Schema design for agent state
- Query patterns for state recovery

**Git-Based Checkpointing**:
- Commit at each checkpoint
- Branch-per-checkpoint for rollback
- Tag significant milestones
- When to use: version-controlled workflows

#### Example Checkpoint Code

Provide working Python code for:

```python
# Checkpoint structure
{
    "checkpoint_id": "uuid",
    "timestamp": "ISO8601",
    "agent_name": "string",
    "workflow_phase": "string",
    "completed_tasks": ["list"],
    "pending_tasks": ["list"],
    "context_summary": "compressed summary of work so far",
    "token_usage": {
        "total": 0,
        "by_phase": {},
        "by_model": {}
    },
    "cost_accumulated": 0.00,
    "artifacts_produced": ["file paths"],
    "resumption_instructions": "what to do next"
}
```

Include save/load/resume functions with error handling.

### 2. Context Window Management

#### Summarization Strategy

**Trigger**: Every 100K tokens of accumulated context.

**Process**:
1. Identify high-value context (decisions, artifacts, current state)
2. Compress low-value context (exploration, failed attempts, verbose output)
3. Generate structured summary maintaining critical information
4. Replace full context with summary + references to full logs
5. Validate that summary preserves actionable information

**Summary Template**:
```markdown
## Context Summary (Generated at [TOKEN_COUNT] tokens)

### Decisions Made
- [Decision 1]: [Rationale] (Phase X)
- [Decision 2]: [Rationale] (Phase Y)

### Artifacts Produced
- [File path]: [Description] (Phase X)

### Current State
- Phase: [Current phase]
- Pending: [Remaining tasks]
- Blockers: [Any blockers]

### Key Findings
- [Finding 1]: [Impact]

### References
- Full log: [path to log file]
- Previous summaries: [paths]
```

#### Segmentation Approach

Break long workflows into segments:
- Each segment has its own context budget
- Segments communicate through structured handoff documents
- Previous segment summaries loaded as reference context
- Segment boundaries align with workflow phases

**Segment Design**:
- Maximum segment length: 100K tokens
- Handoff document: <5K tokens
- Reference context from previous segments: <10K tokens
- Working context for current segment: Remaining budget

#### Reference-Based Patterns

Instead of carrying full context:
- Write intermediate results to files
- Reference files by path in context
- Load file contents on-demand when needed
- Maintain an index of produced artifacts

### 3. Cost Optimization

#### Token Budget Crossover Points

Table showing when model switching becomes cost-effective:

| Workflow Duration | Tokens Used | All-Opus Cost | Mixed-Model Cost | Savings | Recommendation |
|------------------|-------------|---------------|-------------------|---------|----------------|
| 15 minutes | ~25K | $X.XX | $X.XX | X% | All-Opus acceptable |
| 30 minutes | ~50K | $X.XX | $X.XX | X% | Consider mixed |
| 1 hour | ~100K | $X.XX | $X.XX | X% | Mixed recommended |
| 2 hours | ~200K | $X.XX | $X.XX | X% | Mixed strongly recommended |
| 4 hours | ~400K | $X.XX | $X.XX | X% | Phased model switching |
| 8 hours | ~800K | $X.XX | $X.XX | X% | Aggressive optimization |
| 24 hours | ~2.4M | $X.XX | $X.XX | X% | Software Factory mode |

#### Calculation Methodology

Provide formulas for:
- Cost per phase = (input_tokens * input_price) + (output_tokens * output_price)
- Total workflow cost = sum of phase costs + overhead factor (1.15x for retries)
- Model switching savings = baseline_cost - optimized_cost
- Break-even point for checkpoint overhead vs restart cost

#### Model Switching Over Time Strategy

**Phase-Based Model Selection**:
- **Planning phases**: Opus (highest reasoning needed, lowest token volume)
- **Implementation phases**: Opus or Sonnet (depends on complexity)
- **Review phases**: Opus for quality-critical, Sonnet for standard
- **Documentation phases**: Haiku (high volume, lower complexity)
- **Maintenance/monitoring phases**: Haiku (simple status checks)

**Dynamic Switching Rules**:
- If current task complexity < threshold: downgrade model
- If error rate increases after downgrade: upgrade back
- If budget remaining < 20%: switch to cheapest viable model
- If quality metrics drop: switch to more capable model

### 4. Error Recovery

#### Graceful Failure Patterns

**Agent-Level Recovery**:
1. Detect error type (transient vs permanent)
2. For transient errors (API timeout, rate limit):
   - Exponential backoff with jitter
   - Maximum 3 retries
   - Log each attempt
3. For permanent errors (invalid input, impossible task):
   - Save current state to checkpoint
   - Log error with full context
   - Notify coordinator (if in team) or user (if standalone)
   - Provide clear error description and recovery options

**Team-Level Recovery**:
1. Coordinator detects agent failure
2. Assess impact on workflow:
   - Is the failed agent on the critical path?
   - Can other agents continue independently?
   - Is the failure recoverable without the failed agent?
3. Recovery actions:
   - Reassign task to backup agent
   - Skip non-critical task and continue
   - Pause workflow and notify user
   - Roll back to last good checkpoint

#### Resumption Checklist

When resuming from a checkpoint:

```markdown
## Pre-Resumption Checklist
- [ ] Load latest checkpoint file
- [ ] Verify checkpoint integrity (all required fields present)
- [ ] Check artifact files still exist and are valid
- [ ] Review context summary for accuracy
- [ ] Confirm pending tasks are still relevant
- [ ] Check if external state changed (git status, API availability)
- [ ] Verify token budget remaining
- [ ] Confirm model availability
- [ ] Load any new instructions since checkpoint
- [ ] Set up monitoring for new session
```

#### When to Stop and Restart

Situations where restarting is better than continuing:

- Context pollution: accumulated errors or contradictions in context
- Scope drift: agent has drifted far from original task
- Token budget exhaustion: >90% of budget consumed with <50% of work done
- Quality degradation: output quality declining over time
- State corruption: checkpoint data is inconsistent
- External changes: requirements changed significantly since session start

**Decision formula**: Restart if (estimated_remaining_cost > restart_cost * 0.7) AND (quality_trend is declining)

### 5. Monitoring

#### Real-Time Metrics to Track

| Metric | Collection Method | Frequency | Purpose |
|--------|------------------|-----------|---------|
| Token usage (cumulative) | API response headers | Every request | Budget tracking |
| Token usage (per phase) | Phase boundary logging | Per phase | Efficiency analysis |
| Cost (cumulative) | Calculated from tokens | Every request | Budget alerts |
| Error rate | Error counter / total requests | Every 10 requests | Quality monitoring |
| Task completion rate | Completed / total tasks | Per task | Progress tracking |
| Context window utilization | Context tokens / max window | Every request | Capacity planning |
| Latency per request | Timestamp differencing | Every request | Performance monitoring |
| Time per task | Task start/end timestamps | Per task | Velocity tracking |
| Quality score | Domain-specific metric | Per deliverable | Output quality |
| Agent health | Heartbeat mechanism | Every 5 minutes | Availability |

#### Alert Thresholds

| Alert | Threshold | Severity | Action |
|-------|-----------|----------|--------|
| Budget warning | 70% consumed | Warning | Notify user, review remaining work |
| Budget critical | 90% consumed | Critical | Pause non-essential work, get user approval |
| Error spike | >3 errors in 10 minutes | Warning | Check API status, review recent changes |
| Error sustained | >20% error rate over 30 min | Critical | Checkpoint and pause |
| Stall detected | No progress for 15 minutes | Warning | Check for blocking issues |
| Quality drop | Score below threshold for 3 tasks | Warning | Consider model upgrade |
| Context near limit | >80% context window used | Warning | Trigger summarization |
| Context at limit | >95% context window used | Critical | Force summarization or segmentation |

#### Monitoring Dashboard Template

Provide a template for real-time monitoring output:

```
=== Agent Session Monitor ===
Session: [ID] | Duration: [HH:MM] | Phase: [X/Y]
Model: [current] | Context: [used/max] ([%])

Tokens: [consumed] / [budget] ([%])
Cost:   $[spent] / $[budget] ([%])
Tasks:  [done] / [total] ([%])

Last 5 min: [tokens/min] tokens/min | [errors] errors
Quality:    [score] (target: [threshold])

Alerts: [none | list active alerts]
Next checkpoint: [time or token count]
=============================
```

## Writing Guidelines

- Include working code examples for all checkpoint and monitoring patterns
- Provide concrete token counts and dollar amounts (with calculation methodology)
- Include real-world scenarios showing when each pattern applies
- Present error recovery as decision trees, not just lists
- Reference StrongDM Software Factory pattern for 24/7 operation scenarios

## Dependencies

- Token pricing data for cost calculations
- Context window sizes for current models
- Common API error codes and their meanings

## Cross-References

- **Strategies Layer**: `specs/03-strategies-layer/SPEC.md`
- **Optimization Guide**: `specs/03-strategies-layer/guides/optimization/SPEC.md` (cost optimization techniques)
- **Model Selection**: `specs/03-strategies-layer/guides/model-selection/SPEC.md` (model switching strategies)
- **Quality Guide**: `specs/03-strategies-layer/guides/quality/SPEC.md` (quality monitoring)
- **Common Utilities**: `specs/01-common-layer/utilities/SPEC.md` (status-updater.py, cost-estimator.py)
