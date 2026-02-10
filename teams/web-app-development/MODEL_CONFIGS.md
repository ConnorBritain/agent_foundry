# Model Configuration Guide

This document describes the model assignment options for the Web App Development Team. The choice of model per agent affects cost, speed, and output quality.

---

## Pricing Reference

| Model | Input (per 1M tokens) | Output (per 1M tokens) | Effective Blended Rate |
|-------|----------------------|------------------------|----------------------|
| Claude Opus 4.6 | $15.00 | $75.00 | ~$15.00 per 100K tokens |
| Claude Sonnet 4.5 | $3.00 | $15.00 | ~$6.00 per 100K tokens |

Blended rate assumes a typical 3:1 input-to-output ratio for code generation tasks.

---

## Configuration Profiles

### Default Configuration (Recommended)

Best balance of quality and cost. Opus 4.6 is assigned to roles that require deep architectural reasoning and complex code generation. Sonnet 4.5 handles high-throughput execution tasks.

| Agent | Model | Rationale |
|-------|-------|-----------|
| Coordinator / Tech Lead | **Opus 4.6** | Architecture decisions require deep reasoning across the entire system. Mistakes here cascade to every other agent. |
| Senior Full-Stack Developer | **Opus 4.6** | Complex Next.js patterns, React Server Components, and integration code benefit from Opus's superior code quality. |
| Cloud / DevOps Engineer | Sonnet 4.5 | Infrastructure tasks are well-defined and procedural. Sonnet handles YAML generation and CLI commands effectively. |
| Marketing Frontend Developer | Sonnet 4.5 | Landing pages and SEO follow established patterns. Sonnet produces high-quality Tailwind CSS and semantic HTML. |
| Database Engineer | Sonnet 4.5 | SQL schema design and RLS policies are well-structured tasks. Sonnet excels at generating correct SQL. |
| RevOps Specialist | Sonnet 4.5 | Stripe integration follows documented API patterns. Webhook handlers are procedural. |
| QA / Test Engineer | Sonnet 4.5 | Test writing is pattern-heavy. Sonnet generates correct Playwright and Vitest code reliably. |

**Estimated total cost: ~$105**

```yaml
model_config: default
agents:
  coordinator:
    model: claude-opus-4-6
    max_tokens: 150000
  senior_fullstack:
    model: claude-opus-4-6
    max_tokens: 200000
  cloud_devops:
    model: claude-sonnet-4-5
    max_tokens: 120000
  marketing_frontend:
    model: claude-sonnet-4-5
    max_tokens: 120000
  database_engineer:
    model: claude-sonnet-4-5
    max_tokens: 150000
  revops:
    model: claude-sonnet-4-5
    max_tokens: 130000
  qa_test:
    model: claude-sonnet-4-5
    max_tokens: 130000
```

---

### Budget Configuration

All agents on Sonnet 4.5. Use this when cost is the primary constraint, or for simpler projects where deep architectural reasoning is less critical.

| Agent | Model | Trade-off |
|-------|-------|-----------|
| Coordinator / Tech Lead | Sonnet 4.5 | May produce less nuanced architecture decisions. Review recommendations more carefully. |
| Senior Full-Stack Developer | Sonnet 4.5 | Code quality is still high but may need more iteration on complex patterns like streaming, suspense boundaries, and parallel routes. |
| Cloud / DevOps Engineer | Sonnet 4.5 | No change from default. |
| Marketing Frontend Developer | Sonnet 4.5 | No change from default. |
| Database Engineer | Sonnet 4.5 | No change from default. |
| RevOps Specialist | Sonnet 4.5 | No change from default. |
| QA / Test Engineer | Sonnet 4.5 | No change from default. |

**Estimated total cost: ~$63**

```yaml
model_config: budget
agents:
  coordinator:
    model: claude-sonnet-4-5
    max_tokens: 150000
  senior_fullstack:
    model: claude-sonnet-4-5
    max_tokens: 200000
  cloud_devops:
    model: claude-sonnet-4-5
    max_tokens: 120000
  marketing_frontend:
    model: claude-sonnet-4-5
    max_tokens: 120000
  database_engineer:
    model: claude-sonnet-4-5
    max_tokens: 150000
  revops:
    model: claude-sonnet-4-5
    max_tokens: 130000
  qa_test:
    model: claude-sonnet-4-5
    max_tokens: 130000
```

**When to use budget config:**
- Prototyping or proof-of-concept projects
- Simple CRUD applications with minimal business logic
- Projects where you will manually review and adjust architecture decisions
- Cost-sensitive engagements
- Internal tools with relaxed quality requirements

---

### Premium Configuration

All agents on Opus 4.6. Use this for mission-critical projects where output quality is paramount and cost is not a constraint.

| Agent | Model | Benefit |
|-------|-------|---------|
| Coordinator / Tech Lead | Opus 4.6 | No change from default. |
| Senior Full-Stack Developer | Opus 4.6 | No change from default. |
| Cloud / DevOps Engineer | **Opus 4.6** | More sophisticated IaC, better edge case handling in CI/CD, more thorough security configuration. |
| Marketing Frontend Developer | **Opus 4.6** | Better conversion copy, more creative landing page layouts, deeper accessibility compliance. |
| Database Engineer | **Opus 4.6** | More optimized query plans, better index strategy, more thorough RLS policy coverage. |
| RevOps Specialist | **Opus 4.6** | More robust dunning flows, better edge case handling in webhook processing, more sophisticated revenue analytics. |
| QA / Test Engineer | **Opus 4.6** | More comprehensive test coverage, better edge case identification, more realistic load test scenarios. |

**Estimated total cost: ~$158**

```yaml
model_config: premium
agents:
  coordinator:
    model: claude-opus-4-6
    max_tokens: 150000
  senior_fullstack:
    model: claude-opus-4-6
    max_tokens: 200000
  cloud_devops:
    model: claude-opus-4-6
    max_tokens: 120000
  marketing_frontend:
    model: claude-opus-4-6
    max_tokens: 120000
  database_engineer:
    model: claude-opus-4-6
    max_tokens: 150000
  revops:
    model: claude-opus-4-6
    max_tokens: 130000
  qa_test:
    model: claude-opus-4-6
    max_tokens: 130000
```

**When to use premium config:**
- Production SaaS applications with paying customers
- Projects with complex business logic or compliance requirements
- Applications handling sensitive data (financial, health, PII)
- When the cost of bugs in production exceeds the marginal model cost
- High-revenue applications where quality directly impacts revenue

---

## Cost Comparison Table

| Configuration | Opus 4.6 Agents | Sonnet 4.5 Agents | Total Tokens | Est. Cost | Cost vs Default |
|--------------|----------------|-------------------|-------------|-----------|-----------------|
| **Budget** | 0 | 7 | ~1,000K | ~$63 | -40% |
| **Default** | 2 | 5 | ~1,000K | ~$105 | baseline |
| **Premium** | 7 | 0 | ~1,000K | ~$158 | +50% |

### Per-Phase Cost Breakdown by Configuration

| Phase | Budget | Default | Premium |
|-------|--------|---------|---------|
| Foundation (~30 min) | ~$12 | ~$20 | ~$30 |
| Core Features (~60 min) | ~$24 | ~$40 | ~$60 |
| Integration & Revenue (~45 min) | ~$18 | ~$30 | ~$45 |
| Launch Prep (~30 min) | ~$9 | ~$15 | ~$23 |
| **Total** | **~$63** | **~$105** | **~$158** |

---

## Hybrid Configurations

You can mix and match models per agent for custom cost/quality trade-offs. Common hybrid configurations:

### Hybrid A: Opus Coordinator Only

Only the Coordinator uses Opus. All execution agents use Sonnet. Good when you want high-quality architecture decisions but are comfortable with Sonnet-quality code.

```yaml
model_config: hybrid_a
agents:
  coordinator:
    model: claude-opus-4-6
  senior_fullstack:
    model: claude-sonnet-4-5
  cloud_devops:
    model: claude-sonnet-4-5
  marketing_frontend:
    model: claude-sonnet-4-5
  database_engineer:
    model: claude-sonnet-4-5
  revops:
    model: claude-sonnet-4-5
  qa_test:
    model: claude-sonnet-4-5
```

**Estimated cost: ~$75**

### Hybrid B: Opus for Code-Heavy Agents

Opus for Coordinator, Full-Stack, and Database. Sonnet for the rest. Good for data-intensive applications.

```yaml
model_config: hybrid_b
agents:
  coordinator:
    model: claude-opus-4-6
  senior_fullstack:
    model: claude-opus-4-6
  cloud_devops:
    model: claude-sonnet-4-5
  marketing_frontend:
    model: claude-sonnet-4-5
  database_engineer:
    model: claude-opus-4-6
  revops:
    model: claude-sonnet-4-5
  qa_test:
    model: claude-sonnet-4-5
```

**Estimated cost: ~$127**

---

## Recommendations

1. **Start with Default.** It provides the best quality-to-cost ratio for most projects.
2. **Use Budget for prototypes.** Switch to Default or Premium when moving to production.
3. **Use Premium for revenue-critical apps.** The marginal cost ($53 over Default) is negligible compared to the cost of production bugs.
4. **Monitor token usage.** If an agent consistently uses fewer tokens than budgeted, consider reducing its allocation. If it hits limits, consider upgrading its model.
5. **Iterate on model selection.** Run the team once with Default, review the output quality per agent, then adjust models for subsequent runs.
