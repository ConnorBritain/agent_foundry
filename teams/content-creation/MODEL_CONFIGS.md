# Model Configuration Guide

This document describes the model assignment options for the Content Creation Team. The choice of model per agent affects cost, output quality, and humanization effectiveness.

---

## Pricing Reference

| Model | Input (per 1M tokens) | Output (per 1M tokens) | Effective Blended Rate |
|-------|----------------------|------------------------|----------------------|
| Claude Opus 4.6 | $15.00 | $75.00 | ~$15.00 per 100K tokens |
| Claude Sonnet 4.5 | $3.00 | $15.00 | ~$6.00 per 100K tokens |
| Claude Haiku 4.5 | $0.25 | $1.25 | ~$0.50 per 100K tokens |

Blended rate assumes a typical 3:1 input-to-output ratio for content generation tasks.

---

## Configuration Profiles

### Default Configuration (Recommended)

Best balance of quality and cost. Opus 4.6 for the Coordinator who makes editorial judgment calls. Sonnet 4.5 for creative and analytical agents. Haiku 4.5 for mechanical verification and formatting.

| Agent | Model | Rationale |
|-------|-------|-----------|
| Coordinator / Editor | **Opus 4.6** | Editorial vision and publish decisions require deep judgment. Weak editorial direction cascades into mediocre content. |
| Research Specialist | Sonnet 4.5 | Source evaluation and organization are well-suited to Sonnet's analytical capabilities. |
| Content Drafter | Sonnet 4.5 | First-draft writing benefits from Sonnet's creative range without Opus cost. Polish comes later. |
| Humanizer | **Sonnet 4.5** | AI pattern detection and voice matching require strong language understanding. Sonnet handles this well. |
| Content Critic | Sonnet 4.5 | Style guide enforcement is systematic. Editorial feedback benefits from Sonnet's analytical depth. |
| Fact Checker | Haiku 4.5 | Claim verification is a focused, pattern-matching task. Haiku is efficient and accurate. |
| Format Specialist | Haiku 4.5 | Typography and formatting are mechanical tasks. Haiku handles them with minimal token usage. |

**Estimated total cost per article: ~$21 (with 20% buffer)**

```yaml
model_config: default
agents:
  coordinator:
    model: claude-opus-4-6
    max_tokens: 30000
  research_specialist:
    model: claude-sonnet-4-5
    max_tokens: 40000
  content_drafter:
    model: claude-sonnet-4-5
    max_tokens: 60000
  humanizer:
    model: claude-sonnet-4-5
    max_tokens: 50000
  content_critic:
    model: claude-sonnet-4-5
    max_tokens: 50000
  fact_checker:
    model: claude-haiku-4-5
    max_tokens: 20000
  format_specialist:
    model: claude-haiku-4-5
    max_tokens: 10000
```

---

### Budget Configuration

All agents on Sonnet 4.5 or Haiku 4.5. Use when cost is the primary constraint or for high-volume content where some quality trade-off is acceptable.

| Agent | Model | Trade-off |
|-------|-------|-----------|
| Coordinator / Editor | Sonnet 4.5 | Less nuanced editorial judgment. May miss subtle issues with angle or audience fit. |
| Research Specialist | Sonnet 4.5 | No change from default. |
| Content Drafter | Sonnet 4.5 | No change from default. |
| Humanizer | Sonnet 4.5 | No change from default. |
| Content Critic | Sonnet 4.5 | No change from default. |
| Fact Checker | Haiku 4.5 | No change from default. |
| Format Specialist | Haiku 4.5 | No change from default. |

**Estimated total cost per article: ~$17**

```yaml
model_config: budget
agents:
  coordinator:
    model: claude-sonnet-4-5
    max_tokens: 30000
  research_specialist:
    model: claude-sonnet-4-5
    max_tokens: 40000
  content_drafter:
    model: claude-sonnet-4-5
    max_tokens: 60000
  humanizer:
    model: claude-sonnet-4-5
    max_tokens: 50000
  content_critic:
    model: claude-sonnet-4-5
    max_tokens: 50000
  fact_checker:
    model: claude-haiku-4-5
    max_tokens: 20000
  format_specialist:
    model: claude-haiku-4-5
    max_tokens: 10000
```

**When to use budget config:**
- High-volume content production (10+ pieces per week)
- Internal content that does not face external publication scrutiny
- Content with a strong existing style guide that reduces editorial judgment needs
- Drafts that will receive additional human editing

---

### Premium Configuration

Opus 4.6 for Coordinator, Drafter, and Humanizer. The three agents where creative judgment matters most. Sonnet 4.5 for the rest.

| Agent | Model | Benefit |
|-------|-------|---------|
| Coordinator / Editor | Opus 4.6 | No change from default. |
| Research Specialist | Sonnet 4.5 | No change from default. |
| Content Drafter | **Opus 4.6** | More sophisticated narrative structure, better metaphors, stronger argumentation. |
| Humanizer | **Opus 4.6** | More nuanced AI pattern detection, better voice matching, more natural rewrites. |
| Content Critic | Sonnet 4.5 | No change from default. |
| Fact Checker | Haiku 4.5 | No change from default. |
| Format Specialist | Haiku 4.5 | No change from default. |

**Estimated total cost per article: ~$38**

```yaml
model_config: premium
agents:
  coordinator:
    model: claude-opus-4-6
    max_tokens: 30000
  research_specialist:
    model: claude-sonnet-4-5
    max_tokens: 40000
  content_drafter:
    model: claude-opus-4-6
    max_tokens: 60000
  humanizer:
    model: claude-opus-4-6
    max_tokens: 50000
  content_critic:
    model: claude-sonnet-4-5
    max_tokens: 50000
  fact_checker:
    model: claude-haiku-4-5
    max_tokens: 20000
  format_specialist:
    model: claude-haiku-4-5
    max_tokens: 10000
```

**When to use premium config:**
- Flagship thought leadership content
- Content for high-stakes audiences (investors, press, regulators)
- Voice matching for a distinctive author with complex style
- Content where AI detection tools will be used by the audience

---

### Maximum Quality Configuration

All creative agents on Opus 4.6. Use only when content quality justifies the cost.

| Agent | Model | Benefit |
|-------|-------|---------|
| Coordinator / Editor | Opus 4.6 | No change from default. |
| Research Specialist | **Opus 4.6** | Deeper source evaluation, more creative research angles. |
| Content Drafter | **Opus 4.6** | Best narrative quality. |
| Humanizer | **Opus 4.6** | Best pattern detection and voice matching. |
| Content Critic | **Opus 4.6** | More insightful editorial feedback. |
| Fact Checker | Sonnet 4.5 | More thorough verification, better at catching subtle inaccuracies. |
| Format Specialist | Haiku 4.5 | Formatting does not benefit from Opus. |

**Estimated total cost per article: ~$52**

---

## Cost Comparison Table

| Configuration | Opus Agents | Sonnet Agents | Haiku Agents | Est. Cost/Article | vs Default |
|--------------|-------------|---------------|--------------|-------------------|------------|
| **Budget** | 0 | 5 | 2 | ~$17 | -19% |
| **Default** | 1 | 4 | 2 | ~$21 | baseline |
| **Premium** | 3 | 2 | 2 | ~$38 | +81% |
| **Maximum** | 5 | 1 | 1 | ~$52 | +148% |

---

## Content-Type-Specific Recommendations

### Blog Posts (800-1,200 words)
- **Recommended:** Budget or Default
- Blog posts are shorter and benefit less from Opus's deep reasoning
- Cost savings compound over high-volume blog production

### White Papers (4,000-8,000 words)
- **Recommended:** Premium or Maximum
- Long-form content amplifies quality differences between models
- Opus produces better argumentation over extended logical arcs

### Email Sequences
- **Recommended:** Default
- Short, punchy content that Sonnet handles well
- Voice consistency matters more than individual piece quality

### Technical Documentation
- **Recommended:** Default
- Accuracy matters more than literary quality
- Fact Checker upgrade to Sonnet is worthwhile for highly technical content

---

## Recommendations

1. **Start with Default.** It provides the best quality-to-cost ratio for most content.
2. **Use Budget for volume.** When producing 10+ pieces per week, Budget saves significantly without dramatic quality loss.
3. **Use Premium for flagship content.** The Opus Humanizer catches patterns that Sonnet misses.
4. **Monitor AI pattern scores.** If the Humanizer consistently flags many patterns, consider upgrading the Drafter to Opus (reduces patterns at the source).
5. **Iterate on model selection.** Run the team once with Default, check the AI pattern score, then adjust.
