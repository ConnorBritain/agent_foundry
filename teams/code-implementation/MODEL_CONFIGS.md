# Model Configuration Guide

This document describes the model assignment options for the Code Implementation Team. The choice of model per agent affects cost, output quality, and review thoroughness.

---

## Pricing Reference

| Model | Input (per 1M tokens) | Output (per 1M tokens) | Effective Blended Rate |
|-------|----------------------|------------------------|----------------------|
| Claude Opus 4.6 | $15.00 | $75.00 | ~$15.00 per 100K tokens |
| Claude Sonnet 4.5 | $3.00 | $15.00 | ~$6.00 per 100K tokens |
| Claude Haiku 4.5 | $0.25 | $1.25 | ~$0.50 per 100K tokens |

Blended rate assumes a typical 3:1 input-to-output ratio for code generation tasks.

---

## Configuration Profiles

### Default Configuration (Recommended)

Best balance of quality and cost. Opus 4.6 for agents that write and review production code. Sonnet 4.5 for planning and testing. Haiku 4.5 for documentation.

| Agent | Model | Rationale |
|-------|-------|-----------|
| Coordinator / Planner | Sonnet 4.5 | Planning and coordination is well-structured. Does not need Opus reasoning depth. |
| Implementation Specialist A | **Opus 4.6** | Complex logic, architecture decisions, production-quality code require deep reasoning. |
| Implementation Specialist B | **Opus 4.6** | Same requirements as Specialist A. Parallel execution demands equal capability. |
| Code Reviewer | **Opus 4.6** | Catches subtle bugs, security issues, and architectural problems that lighter models miss. |
| Test Engineer | Sonnet 4.5 | Test generation is systematic. Sonnet handles test patterns effectively. |
| Documentation Writer | Haiku 4.5 | Documentation is mechanical formatting. Haiku is efficient and cost-effective. |

**Estimated total cost per feature: ~$25 (with 20% buffer: ~$30)**

```yaml
model_config: default
agents:
  coordinator:
    model: claude-sonnet-4-5
    max_tokens: 30000
  impl_specialist_a:
    model: claude-opus-4-6
    max_tokens: 150000
  impl_specialist_b:
    model: claude-opus-4-6
    max_tokens: 150000
  code_reviewer:
    model: claude-opus-4-6
    max_tokens: 80000
  test_engineer:
    model: claude-sonnet-4-5
    max_tokens: 60000
  doc_writer:
    model: claude-haiku-4-5
    max_tokens: 20000
```

---

### Budget Configuration

All agents on Sonnet 4.5 or Haiku 4.5. Use when cost is the primary constraint or for prototypes and MVPs.

| Agent | Model | Trade-off |
|-------|-------|-----------|
| Coordinator / Planner | Sonnet 4.5 | No change from default. |
| Implementation Specialist A | Sonnet 4.5 | Less sophisticated architectural decisions. May miss edge cases in complex logic. |
| Implementation Specialist B | Sonnet 4.5 | Same trade-off as Specialist A. |
| Code Reviewer | Sonnet 4.5 | May miss subtle bugs and security issues. Good for style enforcement. |
| Test Engineer | Sonnet 4.5 | No change from default. |
| Documentation Writer | Haiku 4.5 | No change from default. |

**Estimated total cost per feature: ~$10**

```yaml
model_config: budget
agents:
  coordinator:
    model: claude-sonnet-4-5
    max_tokens: 30000
  impl_specialist_a:
    model: claude-sonnet-4-5
    max_tokens: 150000
  impl_specialist_b:
    model: claude-sonnet-4-5
    max_tokens: 150000
  code_reviewer:
    model: claude-sonnet-4-5
    max_tokens: 80000
  test_engineer:
    model: claude-sonnet-4-5
    max_tokens: 60000
  doc_writer:
    model: claude-haiku-4-5
    max_tokens: 20000
```

**When to use budget config:**
- Prototypes and MVPs where speed matters more than polish
- Simple CRUD features with well-established patterns
- Features that will receive additional human review
- High-volume feature development where cost compounds

---

### Premium Configuration

All code-touching agents on Opus 4.6. Use for high-stakes features, security-critical code, or complex business logic.

| Agent | Model | Benefit |
|-------|-------|---------|
| Coordinator / Planner | **Opus 4.6** | Better decomposition of highly complex features, superior dependency analysis. |
| Implementation Specialist A | Opus 4.6 | No change from default. |
| Implementation Specialist B | Opus 4.6 | No change from default. |
| Code Reviewer | Opus 4.6 | No change from default. |
| Test Engineer | **Opus 4.6** | More creative edge-case discovery, better concurrency and race condition tests. |
| Documentation Writer | Sonnet 4.5 | Richer technical documentation with better explanations. |

**Estimated total cost per feature: ~$45**

```yaml
model_config: premium
agents:
  coordinator:
    model: claude-opus-4-6
    max_tokens: 30000
  impl_specialist_a:
    model: claude-opus-4-6
    max_tokens: 150000
  impl_specialist_b:
    model: claude-opus-4-6
    max_tokens: 150000
  code_reviewer:
    model: claude-opus-4-6
    max_tokens: 80000
  test_engineer:
    model: claude-opus-4-6
    max_tokens: 60000
  doc_writer:
    model: claude-sonnet-4-5
    max_tokens: 20000
```

**When to use premium config:**
- Security-critical features (authentication, authorization, payments)
- Complex concurrency or state management logic
- Features with high regression risk
- Code that must pass rigorous external audit

---

## Language-Specific Optimizations

### Swift / Kotlin Development

- Consider replacing Implementation Specialists with minimax2.5
- Benchmarks show minimax2.5 outperforms on Swift/SwiftUI and Kotlin/Jetpack Compose generation
- Cost impact: ~15% reduction vs Opus 4.6
- Keep Opus for Code Reviewer (architectural quality still matters)

### Python / JavaScript / TypeScript

- Stick with default (Opus 4.6 for Implementation)
- Opus 4.6 benchmarks highest for these languages
- Alternative: Sonnet 4.5 for simpler CRUD operations (40% cost savings)

### Rust / Go

- Opus 4.6 recommended for memory safety (Rust) and concurrency patterns (Go)
- Do NOT use Haiku for Rust: borrow checker complexity requires strong reasoning

---

## Cost Comparison Table

| Configuration | Opus Agents | Sonnet Agents | Haiku Agents | Est. Cost/Feature | vs Default |
|--------------|-------------|---------------|--------------|-------------------|------------|
| **Budget** | 0 | 5 | 1 | ~$10 | -60% |
| **Default** | 3 | 2 | 1 | ~$25 | baseline |
| **Premium** | 5 | 0 | 1 | ~$45 | +80% |

---

## Recommendations

1. **Start with Default.** It provides the best quality-to-cost ratio for most features.
2. **Use Budget for prototypes.** When shipping speed matters more than code quality.
3. **Use Premium for security-critical code.** The Opus Test Engineer catches edge cases that Sonnet misses.
4. **Monitor review cycles.** If the Code Reviewer consistently requires 3+ passes, consider upgrading the Implementation Specialists or simplifying the feature decomposition.
5. **Match language to model.** Use language-specific optimizations for Swift and Kotlin projects.
