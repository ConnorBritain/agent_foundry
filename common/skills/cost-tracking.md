---
skill_name: "cost-tracking"
version: "1.0.0"
description: "Monitor and report token usage, API costs, and budget consumption"
author: "Sforza"
triggers:
  - "at the end of each phase"
  - "when budget threshold is approaching"
  - "when user requests cost report"
---

# Cost Tracking Skill

## Purpose

Track token consumption, estimate costs, and enforce budget guardrails across all agent activity within a team session.

## Token Counting

### Per-Message Tracking

After each API interaction, record:

| Field | Source |
|-------|--------|
| Input tokens | response.usage.input_tokens |
| Output tokens | response.usage.output_tokens |
| Cache read tokens | response.usage.cache_read_input_tokens |
| Cache write tokens | response.usage.cache_creation_input_tokens |

### Pricing Table (as of 2026)

| Model | Input (per 1M) | Output (per 1M) | Cache Read | Cache Write |
|-------|----------------|------------------|------------|-------------|
| Opus 4.6 | $15.00 | $75.00 | $1.50 | $18.75 |
| Sonnet 4.5 | $3.00 | $15.00 | $0.30 | $3.75 |
| Haiku 4.5 | $0.80 | $4.00 | $0.08 | $1.00 |

## Budget Monitoring

### Alert Thresholds

- **50%**: Informational log — "Halfway through budget"
- **80%**: Warning — Post to cross-team-communication.md, notify user
- **95%**: Critical — Pause non-essential work, request user approval to continue
- **100%**: Hard stop — Do not proceed without explicit budget increase

### Per-Phase Reporting

At each phase transition, report:

```markdown
## Cost Report: [Team Name] — Phase [N] Complete

| Metric | Value |
|--------|-------|
| Phase duration | X hours |
| Total tokens (input) | XXX,XXX |
| Total tokens (output) | XXX,XXX |
| Phase cost | $XX.XX |
| Cumulative cost | $XX.XX |
| Budget remaining | $XX.XX (XX%) |
| Projected total | $XXX.XX |
```

### Budget Projection

Estimate remaining cost based on:
- Tokens consumed so far vs percentage of work complete
- Historical cost per phase for this team type
- Number of remaining phases

```
projected_total = (cost_so_far / progress_pct) * 100
remaining = budget - cost_so_far
on_track = projected_total <= budget
```

## Cost Optimization Tips

1. **Use Haiku for drafts** — Switch to Sonnet/Opus only for final review
2. **Cache aggressively** — Reuse system prompts across turns (cache read is 10x cheaper)
3. **Minimize context** — Only include relevant conversation history, not entire thread
4. **Batch operations** — Combine multiple small requests into one larger request
5. **Early termination** — If a phase produces low-quality output, stop and reassess before spending more

## Updating Project Status

Write cost data to `shared-workspace/project-status.json`:

```json
{
  "team": "team-name",
  "cost": {
    "phase_cost": 42.50,
    "total_cost": 128.75,
    "budget": 200.00,
    "budget_pct": 64,
    "projected_total": 185.00,
    "on_track": true
  }
}
```
