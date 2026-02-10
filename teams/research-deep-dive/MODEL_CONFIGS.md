# Model Configuration Guide

This document describes the model assignment options for the Research Deep Dive Team. The choice of model per agent affects cost, output quality, and analytical depth.

---

## Pricing Reference

| Model | Input (per 1M tokens) | Output (per 1M tokens) | Effective Blended Rate |
|-------|----------------------|------------------------|----------------------|
| Claude Opus 4.6 | $15.00 | $75.00 | ~$15.00 per 100K tokens |
| Claude Sonnet 4.5 | $3.00 | $15.00 | ~$6.00 per 100K tokens |
| Claude Haiku 4.5 | $0.25 | $1.25 | ~$0.50 per 100K tokens |

Blended rate assumes a typical 3:1 input-to-output ratio for research tasks.

---

## Configuration Profiles

### Default Configuration (Recommended)

Best balance of rigor and cost. Opus 4.6 for the Coordinator who makes methodological judgment calls. Sonnet 4.5 for core research and analysis agents. Haiku 4.5 for mechanical tasks like citation formatting.

| Agent | Model | Rationale |
|-------|-------|-----------|
| Coordinator / Research Lead | **Opus 4.6** | Study design and methodological judgment require deep reasoning. Weak research design cascades into unreliable findings. |
| Primary Researcher | Sonnet 4.5 | Source evaluation and literature organization are well-suited to Sonnet's analytical capabilities. |
| Analyst | Sonnet 4.5 | Statistical analysis and visualization benefit from Sonnet's quantitative reasoning without Opus cost. |
| Synthesizer | Sonnet 4.5 | Narrative construction from research findings is strong in Sonnet. Audience adaptation is solid. |
| Citation Manager (academic) | Haiku 4.5 | Bibliography formatting is a mechanical, pattern-based task. Haiku handles it efficiently. |
| Mode-specific agents | Sonnet 4.5 | Analytical depth without Opus premium. Market sizing, competitive analysis, and usability evaluation are well-served. |

**Estimated total cost per study: $25-45 (market mode), $35-60 (academic mode)**

```yaml
model_config: default
agents:
  coordinator:
    model: claude-opus-4-6
    max_tokens: 80000
  primary_researcher:
    model: claude-sonnet-4-5
    max_tokens: 100000
  analyst:
    model: claude-sonnet-4-5
    max_tokens: 100000
  synthesizer:
    model: claude-sonnet-4-5
    max_tokens: 100000
  citation_manager:
    model: claude-haiku-4-5
    max_tokens: 20000
  mode_specific_agents:
    model: claude-sonnet-4-5
    max_tokens: 60000
```

---

### Budget Configuration

All agents on Sonnet 4.5 or Haiku 4.5. Use when cost is the primary constraint or for preliminary research that may be expanded later.

| Agent | Model | Trade-off |
|-------|-------|-----------|
| Coordinator / Research Lead | Sonnet 4.5 | Less nuanced methodological judgment. May miss subtle design flaws or scope issues. |
| Primary Researcher | Sonnet 4.5 | No change from default. |
| Analyst | Sonnet 4.5 | No change from default. |
| Synthesizer | Sonnet 4.5 | No change from default. |
| Citation Manager (academic) | Haiku 4.5 | No change from default. |
| Mode-specific agents | Sonnet 4.5 | No change from default. |

**Estimated total cost per study: $18-35 (market mode), $25-45 (academic mode)**

```yaml
model_config: budget
agents:
  coordinator:
    model: claude-sonnet-4-5
    max_tokens: 80000
  primary_researcher:
    model: claude-sonnet-4-5
    max_tokens: 100000
  analyst:
    model: claude-sonnet-4-5
    max_tokens: 100000
  synthesizer:
    model: claude-sonnet-4-5
    max_tokens: 100000
  citation_manager:
    model: claude-haiku-4-5
    max_tokens: 20000
  mode_specific_agents:
    model: claude-sonnet-4-5
    max_tokens: 60000
```

**When to use budget config:**
- Preliminary or exploratory research before committing to a full study
- Internal research that does not face external publication scrutiny
- Research on well-defined questions with established methodology
- When the user will provide significant methodological guidance themselves

---

### Premium Configuration

Opus 4.6 for the Coordinator, Analyst, and Synthesizer. The three agents where analytical judgment matters most. Sonnet 4.5 for data collection.

| Agent | Model | Benefit |
|-------|-------|---------|
| Coordinator / Research Lead | Opus 4.6 | No change from default. |
| Primary Researcher | Sonnet 4.5 | No change from default. |
| Analyst | **Opus 4.6** | Deeper statistical reasoning, better identification of confounders and biases. |
| Synthesizer | **Opus 4.6** | More nuanced narrative, better distinction between correlation and causation, stronger executive summaries. |
| Citation Manager (academic) | Haiku 4.5 | No change from default. |
| Mode-specific agents | Sonnet 4.5 | No change from default. |

**Estimated total cost per study: $40-70 (market mode), $55-90 (academic mode)**

```yaml
model_config: premium
agents:
  coordinator:
    model: claude-opus-4-6
    max_tokens: 80000
  primary_researcher:
    model: claude-sonnet-4-5
    max_tokens: 100000
  analyst:
    model: claude-opus-4-6
    max_tokens: 100000
  synthesizer:
    model: claude-opus-4-6
    max_tokens: 100000
  citation_manager:
    model: claude-haiku-4-5
    max_tokens: 20000
  mode_specific_agents:
    model: claude-sonnet-4-5
    max_tokens: 60000
```

**When to use premium config:**
- Research for publication in peer-reviewed journals
- Market research informing >$1M investment decisions
- Competitive intelligence for board-level strategic planning
- Research where analytical errors have high downstream cost

---

### Maximum Quality Configuration

Opus 4.6 for all core agents and the Methodology Designer. Sonnet 4.5 for remaining specialists.

| Agent | Model | Benefit |
|-------|-------|---------|
| Coordinator / Research Lead | Opus 4.6 | No change from default. |
| Primary Researcher | **Opus 4.6** | Deeper source evaluation, more creative search strategies, better gap identification. |
| Analyst | **Opus 4.6** | Best statistical reasoning. |
| Synthesizer | **Opus 4.6** | Best narrative quality and evidence interpretation. |
| Methodology Designer (academic) | **Opus 4.6** | No change from default (already Opus). |
| Citation Manager (academic) | Haiku 4.5 | Citation formatting does not benefit from Opus. |
| Other mode-specific agents | Sonnet 4.5 | Sonnet handles market sizing and competitive analysis well. |

**Estimated total cost per study: $60-100 (market mode), $80-130 (academic mode)**

---

## Cost Comparison Table

| Configuration | Opus Agents | Sonnet Agents | Haiku Agents | Est. Cost (Market) | vs Default |
|--------------|-------------|---------------|--------------|-------------------|------------|
| **Budget** | 0 | 7 | 1 | ~$25 | -38% |
| **Default** | 1 | 6 | 1 | ~$40 | baseline |
| **Premium** | 3 | 4 | 1 | ~$60 | +50% |
| **Maximum** | 4 | 3 | 1 | ~$85 | +113% |

---

## Research-Type-Specific Recommendations

### Literature Reviews
- **Recommended:** Budget or Default
- Straightforward methodology reduces the need for Opus-level design judgment
- Cost savings are meaningful when running multiple reviews

### Academic Research
- **Recommended:** Default or Premium
- Methodology design benefits significantly from Opus reasoning
- Premium justified when targeting top-tier journals

### Market/Competitive Research
- **Recommended:** Default
- Market sizing benefits from Sonnet's analytical capability
- Premium justified only for >$1M investment decisions

### Product/UX Research
- **Recommended:** Budget or Default
- Established frameworks (RICE, heuristic evaluation) reduce judgment requirements
- Budget config is appropriate when the user is an experienced product researcher

---

## Recommendations

1. **Start with Default.** It provides the best rigor-to-cost ratio for most research.
2. **Use Budget for exploration.** When you are scoping a research area before committing to a deep study, Budget saves significantly.
3. **Use Premium for high-stakes decisions.** When the research directly informs a major investment, publication, or strategic pivot, the Opus Analyst and Synthesizer provide meaningfully better output.
4. **Monitor source quality scores.** If the Primary Researcher consistently finds insufficient sources, the issue is likely search strategy, not model capability.
5. **Iterate on configuration.** Run the team once with Default, review the deliverable quality, then adjust for subsequent studies.
