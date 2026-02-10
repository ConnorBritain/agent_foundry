# Model Configuration Guide

This document describes the model assignment options for the Project Planning Team. The choice of model per agent affects cost, speed, and output quality.

---

## Pricing Reference

| Model | Input (per 1M tokens) | Output (per 1M tokens) | Effective Blended Rate |
|-------|----------------------|------------------------|----------------------|
| Claude Opus 4.6 | $15.00 | $75.00 | ~$15.00 per 100K tokens |
| Claude Sonnet 4.5 | $3.00 | $15.00 | ~$6.00 per 100K tokens |
| Claude Haiku 4.5 | $0.25 | $1.25 | ~$0.50 per 100K tokens |

Blended rate assumes a typical 3:1 input-to-output ratio for planning tasks.

---

## Configuration Profiles

### Default Configuration (Recommended)

Best balance of quality and cost. Opus 4.6 is assigned to the Resource Allocator role that requires nuanced trade-off reasoning across competing priorities. Sonnet 4.5 handles analytical and structured planning tasks. Haiku 4.5 handles high-volume documentation generation.

| Agent | Model | Rationale |
|-------|-------|-----------|
| Coordinator | Sonnet 4.5 | Configuration and workflow management are procedural tasks. Sonnet handles structured decision-making effectively. |
| Requirements Analyst | Sonnet 4.5 | Vision analysis requires structured thinking but follows established decomposition patterns. |
| Task Decomposer | Sonnet 4.5 | Task creation and estimation are pattern-heavy. Sonnet produces well-structured WBS reliably. |
| Scheduler | Sonnet 4.5 | Calendar math and timeline optimization follow clear rules. Sonnet handles constraint-based scheduling well. |
| Resource Allocator | **Opus 4.6** | Prioritization requires weighing competing business goals, stakeholder politics, and resource constraints. This is the most judgment-intensive role. |
| Risk Assessor | Sonnet 4.5 | Risk identification follows established frameworks (probability x impact). Sonnet handles structured risk analysis well. |
| Integration Planner | Haiku 4.5 | Documentation generation and tool export are high-volume, pattern-based tasks. Haiku is cost-effective here. |

**Estimated total cost: ~$25**

```yaml
model_config: default
agents:
  coordinator:
    model: claude-sonnet-4-5
    max_tokens: 15000
  requirements_analyst:
    model: claude-sonnet-4-5
    max_tokens: 45000
  task_decomposer:
    model: claude-sonnet-4-5
    max_tokens: 60000
  scheduler:
    model: claude-sonnet-4-5
    max_tokens: 40000
  resource_allocator:
    model: claude-opus-4-6
    max_tokens: 60000
  risk_assessor:
    model: claude-sonnet-4-5
    max_tokens: 40000
  integration_planner:
    model: claude-haiku-4-5
    max_tokens: 30000
```

---

### Budget Configuration

All agents on Sonnet 4.5 (with Haiku for Integration). Use this when cost is the primary constraint or for straightforward projects with clear priorities.

| Agent | Model | Trade-off |
|-------|-------|-----------|
| Coordinator | Sonnet 4.5 | No change from default. |
| Requirements Analyst | Sonnet 4.5 | No change from default. |
| Task Decomposer | Sonnet 4.5 | No change from default. |
| Scheduler | Sonnet 4.5 | No change from default. |
| Resource Allocator | **Sonnet 4.5** | May produce less nuanced prioritization. Trade-off recommendations may be less sophisticated. Review priority decisions more carefully. |
| Risk Assessor | Sonnet 4.5 | No change from default. |
| Integration Planner | Haiku 4.5 | No change from default. |

**Estimated total cost: ~$16**

```yaml
model_config: budget
agents:
  coordinator:
    model: claude-sonnet-4-5
    max_tokens: 15000
  requirements_analyst:
    model: claude-sonnet-4-5
    max_tokens: 45000
  task_decomposer:
    model: claude-sonnet-4-5
    max_tokens: 60000
  scheduler:
    model: claude-sonnet-4-5
    max_tokens: 40000
  resource_allocator:
    model: claude-sonnet-4-5
    max_tokens: 60000
  risk_assessor:
    model: claude-sonnet-4-5
    max_tokens: 40000
  integration_planner:
    model: claude-haiku-4-5
    max_tokens: 30000
```

**When to use budget config:**
- Small projects with fewer than 30 tasks
- Clear, unambiguous priority order
- Single-team projects without cross-team dependencies
- Planning sessions where the user will manually review prioritization
- Tight budget constraints

---

### Premium Configuration

Opus 4.6 for all analytical roles. Use this for complex enterprise planning where nuanced reasoning across every phase justifies the cost.

| Agent | Model | Benefit |
|-------|-------|---------|
| Coordinator | **Opus 4.6** | More sophisticated framework configuration, better conflict resolution between agents. |
| Requirements Analyst | **Opus 4.6** | Deeper vision analysis, catches more ambiguities, better stakeholder insight. |
| Task Decomposer | **Opus 4.6** | More realistic effort estimates, better acceptance criteria, finer-grained decomposition. |
| Scheduler | **Opus 4.6** | More creative schedule optimization, better risk identification in timelines. |
| Resource Allocator | Opus 4.6 | No change from default. |
| Risk Assessor | **Opus 4.6** | More comprehensive risk identification, better mitigation strategies, subtler dependency analysis. |
| Integration Planner | **Sonnet 4.5** | Higher quality documentation, better executive summaries, more polished stakeholder comms. |

**Estimated total cost: ~$55**

```yaml
model_config: premium
agents:
  coordinator:
    model: claude-opus-4-6
    max_tokens: 15000
  requirements_analyst:
    model: claude-opus-4-6
    max_tokens: 45000
  task_decomposer:
    model: claude-opus-4-6
    max_tokens: 60000
  scheduler:
    model: claude-opus-4-6
    max_tokens: 40000
  resource_allocator:
    model: claude-opus-4-6
    max_tokens: 60000
  risk_assessor:
    model: claude-opus-4-6
    max_tokens: 40000
  integration_planner:
    model: claude-sonnet-4-5
    max_tokens: 30000
```

**When to use premium config:**
- Enterprise programs with 100+ tasks and multiple teams
- SAFe PI Planning sessions with complex dependencies
- Projects with significant financial risk (>$1M budget)
- Regulated industries requiring thorough risk analysis
- Cross-organization planning with political stakeholder dynamics

---

## Cost Comparison Table

| Configuration | Opus Agents | Sonnet Agents | Haiku Agents | Total Tokens | Est. Cost | Cost vs Default |
|--------------|-------------|---------------|-------------|-------------|-----------|-----------------|
| **Budget** | 0 | 6 | 1 | ~290K | ~$16 | -36% |
| **Default** | 1 | 5 | 1 | ~290K | ~$25 | baseline |
| **Premium** | 6 | 1 | 0 | ~290K | ~$55 | +120% |

### Per-Phase Cost Breakdown by Configuration

| Phase | Budget | Default | Premium |
|-------|--------|---------|---------|
| Configuration | ~$0.90 | ~$0.90 | ~$2.25 |
| Requirements Analysis | ~$2.70 | ~$2.70 | ~$6.75 |
| Task Decomposition | ~$3.60 | ~$3.60 | ~$9.00 |
| Risk Assessment | ~$2.40 | ~$2.40 | ~$6.00 |
| Resource Allocation | ~$3.60 | ~$9.00 | ~$9.00 |
| Scheduling | ~$2.40 | ~$2.40 | ~$6.00 |
| Integration | ~$0.75 | ~$0.75 | ~$1.80 |
| **Total** | **~$16** | **~$25** | **~$55** |

---

## Framework-Specific Model Recommendations

### SAFe (Complex Multi-Team)
- Recommend: **Premium** configuration
- Rationale: PI Planning involves 50-100+ features across multiple teams. Nuanced prioritization (WSJF) and cross-team dependency mapping benefit from Opus-level reasoning.
- Upgrade trigger: More than 3 Agile Release Trains

### Agile Scrum (Standard Team)
- Recommend: **Default** configuration
- Rationale: Sprint planning is well-structured. Opus for prioritization is sufficient.
- Downgrade trigger: Backlog is already well-groomed (use Budget)

### Shape Up (Product Team)
- Recommend: **Default** configuration
- Rationale: Appetite-setting and bet evaluation require judgment but not enterprise complexity.
- Upgrade trigger: Multiple betting tables running simultaneously

### Waterfall (Regulated/Fixed-Scope)
- Recommend: **Default** or **Premium** configuration
- Rationale: Requirements traceability and change control benefit from thorough analysis.
- Upgrade trigger: Regulatory compliance requirements

### Kanban (Continuous Flow)
- Recommend: **Budget** configuration
- Rationale: Kanban planning is lighter-weight; focus is on WIP limits and flow metrics.
- Upgrade trigger: Complex service class definitions or cost-of-delay calculations

---

## Recommendations

1. **Start with Default.** It provides the best quality-to-cost ratio for most projects.
2. **Use Budget for simple sprints.** When the backlog is already groomed and priorities are clear.
3. **Use Premium for PI Planning.** SAFe PI Planning justifies the additional cost with better cross-team coordination.
4. **Monitor Resource Allocator output.** This agent's prioritization quality is most affected by model choice. If priorities seem shallow, upgrade to Opus.
5. **Iterate on model selection.** Run the team once with Default, review the output quality per agent, then adjust models for subsequent runs.
