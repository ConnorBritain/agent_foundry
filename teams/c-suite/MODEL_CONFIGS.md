# Model Configuration Guide

This document describes the model assignment options for the C-Suite Team. The choice of model per agent affects cost, speed, and output quality.

---

## Pricing Reference

| Model | Input (per 1M tokens) | Output (per 1M tokens) | Effective Blended Rate |
|-------|----------------------|------------------------|----------------------|
| Claude Opus 4.6 | $15.00 | $75.00 | ~$15.00 per 100K tokens |
| Claude Sonnet 4.5 | $3.00 | $15.00 | ~$6.00 per 100K tokens |
| Claude Haiku 4.5 | $0.25 | $1.25 | ~$0.50 per 100K tokens |

Blended rate assumes a typical 3:1 input-to-output ratio for business planning tasks.

---

## Configuration Profiles

### Default Configuration (Recommended)

Best balance of quality and cost. Opus 4.6 is assigned to the CEO role where strategic synthesis, conflict resolution, and cross-functional reasoning are critical. Sonnet 4.5 handles specialist deep-dives where domain expertise follows well-structured patterns.

| Agent | Model | Rationale |
|-------|-------|-----------|
| CEO / Strategy Lead | **Opus 4.6** | Strategic synthesis requires reasoning across all functional areas simultaneously. Conflict resolution between specialists demands nuanced trade-off analysis. Mistakes in strategic direction cascade to every artifact. |
| CFO / Finance | Sonnet 4.5 | Financial modeling follows structured patterns (P&L, cash flow, unit economics). Sonnet handles spreadsheet-style calculations and scenario modeling effectively. |
| CMO / Marketing | Sonnet 4.5 | Market research and positioning follow established frameworks (TAM/SAM/SOM, Porter's Five Forces). Sonnet produces high-quality competitive analysis. |
| CTO / Product | Sonnet 4.5 | Product roadmaps and build-vs-buy analysis follow structured decision frameworks. Sonnet handles technical assessment well for planning-level detail. |
| COO / Operations | Sonnet 4.5 | Org design and process mapping are pattern-heavy tasks. Sonnet produces clear, actionable operational plans. |
| VP Sales | Sonnet 4.5 | Sales process design and pipeline modeling follow established methodologies (BANT, MEDDIC). Sonnet generates comprehensive playbooks. |
| General Counsel | Sonnet 4.5 | Legal checklists and entity recommendations follow jurisdiction-specific rules. Sonnet handles compliance frameworks systematically. |

**Estimated total cost: ~$80-150** (including iteration cycles)

```yaml
model_config: default
agents:
  ceo:
    model: claude-opus-4-6
    max_tokens: 130000
  cfo:
    model: claude-sonnet-4-5
    max_tokens: 58000
  cmo:
    model: claude-sonnet-4-5
    max_tokens: 58000
  cto:
    model: claude-sonnet-4-5
    max_tokens: 58000
  coo:
    model: claude-sonnet-4-5
    max_tokens: 58000
  vp_sales:
    model: claude-sonnet-4-5
    max_tokens: 58000
  general_counsel:
    model: claude-sonnet-4-5
    max_tokens: 58000
```

---

### Budget Configuration

All agents on Sonnet 4.5. Use this for initial exploration, when the user will be heavily involved in strategic synthesis, or when cost is the primary constraint.

| Agent | Model | Trade-off |
|-------|-------|-----------|
| CEO / Strategy Lead | Sonnet 4.5 | Strategic synthesis may miss subtle cross-functional trade-offs. User should review the integrated plan more carefully for consistency. |
| CFO / Finance | Sonnet 4.5 | No change from default. |
| CMO / Marketing | Sonnet 4.5 | No change from default. |
| CTO / Product | Sonnet 4.5 | No change from default. |
| COO / Operations | Sonnet 4.5 | No change from default. |
| VP Sales | Sonnet 4.5 | No change from default. |
| General Counsel | Sonnet 4.5 | No change from default. |

**Estimated total cost: ~$45-80**

```yaml
model_config: budget
agents:
  ceo:
    model: claude-sonnet-4-5
    max_tokens: 130000
  cfo:
    model: claude-sonnet-4-5
    max_tokens: 58000
  cmo:
    model: claude-sonnet-4-5
    max_tokens: 58000
  cto:
    model: claude-sonnet-4-5
    max_tokens: 58000
  coo:
    model: claude-sonnet-4-5
    max_tokens: 58000
  vp_sales:
    model: claude-sonnet-4-5
    max_tokens: 58000
  general_counsel:
    model: claude-sonnet-4-5
    max_tokens: 58000
```

**When to use budget config:**
- Early-stage idea exploration (not yet ready for investor materials)
- Founder will do the strategic synthesis personally
- Simple business models with few cross-functional dependencies
- Cost-sensitive planning for bootstrapped ventures

---

### Premium Configuration

All agents on Opus 4.6. Use this for mission-critical business plans where nuance, depth, and cross-functional reasoning quality are paramount.

| Agent | Model | Benefit |
|-------|-------|---------|
| CEO / Strategy Lead | Opus 4.6 | No change from default. |
| CFO / Finance | **Opus 4.6** | More sophisticated financial modeling, better stress testing, more nuanced sensitivity analysis. Catches edge cases in unit economics. |
| CMO / Marketing | **Opus 4.6** | Deeper competitive analysis, more creative positioning, better identification of non-obvious market segments. |
| CTO / Product | **Opus 4.6** | More thorough build-vs-buy analysis, better risk identification, more nuanced architecture assessment. |
| COO / Operations | **Opus 4.6** | More sophisticated org design, better bottleneck identification, more realistic process maps. |
| VP Sales | **Opus 4.6** | More nuanced ICP definition, better objection handling, more realistic pipeline modeling. |
| General Counsel | **Opus 4.6** | More thorough compliance analysis, better risk quantification, more nuanced entity structure reasoning. |

**Estimated total cost: ~$150-350**

```yaml
model_config: premium
agents:
  ceo:
    model: claude-opus-4-6
    max_tokens: 130000
  cfo:
    model: claude-opus-4-6
    max_tokens: 58000
  cmo:
    model: claude-opus-4-6
    max_tokens: 58000
  cto:
    model: claude-opus-4-6
    max_tokens: 58000
  coo:
    model: claude-opus-4-6
    max_tokens: 58000
  vp_sales:
    model: claude-opus-4-6
    max_tokens: 58000
  general_counsel:
    model: claude-opus-4-6
    max_tokens: 58000
```

**When to use premium config:**
- Preparing for Series A or later fundraising rounds
- Complex multi-sided marketplaces or regulated industries
- Plans that will be presented to institutional investors or boards
- Business models with significant cross-functional complexity
- When the cost of a bad strategic decision far exceeds the marginal model cost

---

## Cost Comparison Table

| Configuration | Opus 4.6 Agents | Sonnet 4.5 Agents | Total Tokens | Est. Cost | Cost vs Default |
|--------------|----------------|-------------------|-------------|-----------|-----------------|
| **Budget** | 0 | 7 | ~700K | ~$45-80 | -40% |
| **Default** | 1 | 6 | ~700K | ~$80-150 | baseline |
| **Premium** | 7 | 0 | ~700K | ~$150-350 | +80% |

### Per-Phase Cost Breakdown by Configuration

| Phase | Budget | Default | Premium |
|-------|--------|---------|---------|
| Vision Alignment | ~$3.50 | ~$7.50 | ~$7.50 |
| Specialist Deep-Dives | ~$21.00 | ~$21.00 | ~$52.50 |
| CEO Synthesis | ~$4.80 | ~$12.00 | ~$12.00 |
| Board Review | ~$4.20 | ~$10.00 | ~$15.00 |
| Artifact Generation | ~$7.20 | ~$12.00 | ~$18.00 |
| **Subtotal** | **~$40.70** | **~$62.50** | **~$105.00** |
| + 20% buffer | ~$8.14 | ~$12.50 | ~$21.00 |
| **Effective Total** | **~$49** | **~$75** | **~$126** |

---

## Hybrid Configuration

### Hybrid: Opus CEO + Opus CFO

Add Opus to the CFO for higher-quality financial modeling alongside strategic synthesis. Recommended when financial projections need to withstand investor scrutiny.

```yaml
model_config: hybrid_finance
agents:
  ceo:
    model: claude-opus-4-6
  cfo:
    model: claude-opus-4-6
  cmo:
    model: claude-sonnet-4-5
  cto:
    model: claude-sonnet-4-5
  coo:
    model: claude-sonnet-4-5
  vp_sales:
    model: claude-sonnet-4-5
  general_counsel:
    model: claude-sonnet-4-5
```

**Estimated cost: ~$95-170**

---

## Recommendations

1. **Start with Default.** The CEO on Opus 4.6 provides the strategic synthesis quality that makes the integrated plan coherent. Specialists on Sonnet 4.5 produce strong functional outputs.
2. **Use Budget for ideation.** When you are exploring business ideas and need quick directional plans, not investor-ready materials.
3. **Use Premium for fundraising.** The marginal cost is negligible compared to the value of a compelling, consistent business plan presented to investors.
4. **Consider Hybrid for finance-heavy plans.** If the financial model is the primary deliverable (e.g., for a board meeting), upgrade the CFO to Opus.
5. **Monitor conflict resolution quality.** If the CEO synthesis (Phase 3) produces inconsistencies, consider upgrading to Premium for the next run.
