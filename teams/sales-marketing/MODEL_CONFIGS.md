# Model Configurations

## Configuration Profiles

### Default Configuration (Recommended)

Balanced performance and cost. Suitable for most go-to-market execution scenarios.

| Agent | Model | Context Window | Rationale |
|-------|-------|---------------|-----------|
| Coordinator / VP Marketing | claude-opus-4-6 | 200K | Complex strategic reasoning, cross-functional synthesis, budget optimization decisions |
| Demand Generation Specialist | claude-sonnet-4-5 | 200K | Campaign design requires creativity + analytical rigor; high volume of ad copy and landing page variants |
| Sales Enablement Manager | claude-sonnet-4-5 | 200K | Pitch decks and battle cards require understanding competitive dynamics and translating features to value |
| Pipeline Manager | claude-sonnet-4-5 | 200K | CRM configuration and pipeline analysis need structured reasoning with data interpretation |
| Customer Success Manager | claude-sonnet-4-5 | 200K | Onboarding design and health scoring require understanding customer journeys and behavioral patterns |
| Growth Analyst | claude-sonnet-4-5 | 200K | Statistical analysis, attribution modeling, and cohort analysis require quantitative precision |
| Brand & Messaging Specialist | claude-haiku-4-5 | 200K | Well-scoped pattern tasks (feature-to-benefit, consistency checks) where Haiku excels at lower cost |

**Estimated cost per full run**: ~$93
**Estimated duration**: ~2.5 hours

---

### Budget Configuration

For teams with cost constraints, early exploration, or lower-stakes planning exercises. Trades some strategic depth for significant cost savings.

| Agent | Model | Context Window | Tradeoffs |
|-------|-------|---------------|-----------|
| Coordinator / VP Marketing | claude-sonnet-4-5 | 200K | Less nuanced strategic tradeoffs; still strong on planning and coordination |
| Demand Generation Specialist | claude-sonnet-4-5 | 200K | No change from default |
| Sales Enablement Manager | claude-haiku-4-5 | 200K | Battle cards may be less competitively nuanced; pitch decks more formulaic |
| Pipeline Manager | claude-haiku-4-5 | 200K | Stage definitions solid; forecasting methodology less sophisticated |
| Customer Success Manager | claude-haiku-4-5 | 200K | Onboarding sequences functional; health scoring model less nuanced |
| Growth Analyst | claude-sonnet-4-5 | 200K | No change from default; statistical rigor is non-negotiable |
| Brand & Messaging Specialist | claude-haiku-4-5 | 200K | No change from default |

**Estimated cost per full run**: ~$45
**Estimated duration**: ~2 hours

**When to use**:
- Initial GTM exploration before committing to a full plan
- Small deal sizes where elaborate playbooks have diminishing returns
- Rapid iteration where you will run multiple cycles quickly
- Early-stage companies with limited marketing budgets

---

### Premium Configuration

Maximum quality for high-stakes launches, enterprise GTM motions, or complex multi-product strategies. Every agent gets the strongest available model.

| Agent | Model | Context Window | Upgrade Benefit |
|-------|-------|---------------|----------------|
| Coordinator / VP Marketing | claude-opus-4-6 | 200K | No change from default; already at maximum |
| Demand Generation Specialist | claude-opus-4-6 | 200K | More sophisticated campaign strategies; better multi-channel coordination |
| Sales Enablement Manager | claude-opus-4-6 | 200K | Deeper competitive analysis; more persuasive narrative construction |
| Pipeline Manager | claude-sonnet-4-5 | 200K | No change; structured CRM work doesn't benefit significantly from Opus |
| Customer Success Manager | claude-opus-4-6 | 200K | More nuanced customer journey design; better churn prediction logic |
| Growth Analyst | claude-opus-4-6 | 200K | More sophisticated attribution models; better experimental design |
| Brand & Messaging Specialist | claude-sonnet-4-5 | 200K | Richer, more differentiated messaging; better persona-specific variants |

**Estimated cost per full run**: ~$160
**Estimated duration**: ~3 hours

**When to use**:
- Major product launches with significant revenue targets
- Enterprise GTM where deal sizes justify the investment
- Competitive markets where differentiation in messaging and strategy is critical
- Annual planning exercises that will guide quarters of execution

---

## Model Selection Rationale

### Why Opus 4.6 for the Coordinator

The Coordinator role requires capabilities that only the strongest model delivers reliably:

1. **Multi-dimensional tradeoff analysis**: Allocating budget across 5+ channels while optimizing for CAC, considering payback period constraints, and accounting for channel saturation requires holding many variables simultaneously.

2. **Cross-functional synthesis**: The Coordinator must read and integrate outputs from 6 specialist agents, identify conflicts, and resolve them with a coherent strategy. This synthesis task benefits enormously from stronger reasoning.

3. **Long-horizon planning**: GTM strategy requires thinking about second and third-order effects (e.g., "if we invest heavily in content now, organic will reduce CAC in 6 months but we need paid to bridge the gap").

### Why Sonnet 4.5 for Most Specialists

Sonnet 4.5 provides the ideal balance for specialist roles:

1. **Domain-depth tasks**: Each specialist works within a well-defined domain. Sonnet handles domain-specific reasoning (campaign optimization, pipeline analysis, cohort analysis) with strong quality.

2. **Structured output**: Specialists produce structured deliverables (battle cards, stage definitions, scoring models) where Sonnet excels.

3. **Volume of output**: Specialists produce high volumes of content (multiple campaigns, email sequences, playbook sections). Sonnet's cost efficiency matters at volume.

### Why Haiku 4.5 for Brand & Messaging

The Brand & Messaging Specialist's tasks are particularly well-suited to Haiku:

1. **Pattern-based transformation**: Converting features to benefits to outcomes follows a consistent pattern that Haiku handles well.

2. **Consistency checking**: Reviewing content for brand voice compliance is a pattern-matching task.

3. **High volume, smaller scope**: Messaging tasks tend to be shorter, more numerous, and more formulaic than strategy or analysis tasks.

---

## Temperature Settings

| Agent | Temperature | Rationale |
|-------|------------|-----------|
| Coordinator | 0.3 | Strategic decisions should be consistent and well-reasoned |
| Demand Generation | 0.6 | Creative tasks (ad copy, landing pages) benefit from some variety |
| Sales Enablement | 0.4 | Balance between creativity (storytelling) and precision (competitive data) |
| Pipeline Manager | 0.2 | CRM configuration and forecasting need maximum consistency |
| Customer Success | 0.4 | Onboarding needs creativity; health scoring needs precision |
| Growth Analyst | 0.1 | Statistical analysis and attribution must be precise and reproducible |
| Brand & Messaging | 0.5 | Messaging benefits from creative exploration within brand constraints |

## Context Window Usage Guidance

| Agent | Typical Usage | Peak Usage | Notes |
|-------|--------------|------------|-------|
| Coordinator | 40-60K | 100K | Peaks when synthesizing all agent outputs |
| Demand Generation | 30-50K | 80K | High when managing multiple campaigns simultaneously |
| Sales Enablement | 30-50K | 70K | Peaks when building comprehensive competitive analysis |
| Pipeline Manager | 20-40K | 60K | Moderate; CRM configs are structured and compact |
| Customer Success | 30-50K | 70K | High during customer journey mapping |
| Growth Analyst | 40-60K | 90K | Peaks during multi-dimensional cohort analysis |
| Brand & Messaging | 15-30K | 50K | Lower; tasks are focused and well-scoped |

## Switching Between Configurations

To switch configurations, update the `model_config` field in your CONFIG.md:

```yaml
model_config: default  # Options: default, budget, premium

# Or override individual agents:
model_overrides:
  coordinator: claude-opus-4-6
  demand_generation: claude-opus-4-6  # Upgrade just this agent
  growth_analyst: claude-opus-4-6     # And this one
```

When upgrading individual agents, prioritize in this order:
1. **Coordinator** (if on budget config) - Biggest impact on overall strategy quality
2. **Growth Analyst** - Better analysis drives better decisions across all agents
3. **Demand Generation** - More sophisticated campaigns with better targeting
4. **Sales Enablement** - Stronger competitive positioning and deal narratives
5. **Customer Success** - More nuanced retention and expansion strategies
