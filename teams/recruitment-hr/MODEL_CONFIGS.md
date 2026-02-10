# Model Configurations -- Recruitment & HR Team

## Model Selection Rationale

People operations spans a wide spectrum of cognitive demands. Strategy and org design require deep reasoning about human systems. Hiring and culture work demands creativity and contextual judgment. Compensation analysis is data-intensive but structurally predictable. The model assignments reflect these differences.

---

## Default Configuration

The recommended configuration for most teams. Balances output quality with cost efficiency.

```yaml
default:
  coordinator:
    model: claude-opus-4-6
    max_tokens: 16384
    temperature: 0.6
    rationale: >
      People strategy requires synthesizing competing priorities, reading
      organizational dynamics, and making judgment calls that ripple through
      every function. The Coordinator must reason about second and third-order
      effects of people decisions. Opus provides the depth of reasoning needed
      for this systems-level thinking.

  talent_acquisition:
    model: claude-sonnet-4-5
    max_tokens: 12288
    temperature: 0.7
    rationale: >
      Job design and sourcing require creativity -- compelling descriptions,
      novel sourcing channels, interview questions that reveal true capability.
      Sonnet handles this well. The slightly higher temperature encourages
      creative sourcing approaches.

  onboarding_enablement:
    model: claude-sonnet-4-5
    max_tokens: 12288
    temperature: 0.5
    rationale: >
      Onboarding plans need to be thorough and well-structured. Lower
      temperature keeps the output focused and systematic. Sonnet provides
      enough capability for designing multi-stage learning experiences.

  culture_engagement:
    model: claude-sonnet-4-5
    max_tokens: 12288
    temperature: 0.7
    rationale: >
      Culture work requires creativity in ritual design and empathy in
      feedback system construction. Higher temperature supports the
      generative nature of this work. Sonnet balances creative output
      with structured thinking.

  performance_management:
    model: claude-sonnet-4-5
    max_tokens: 12288
    temperature: 0.4
    rationale: >
      Performance frameworks must be precise, fair, and internally consistent.
      Lower temperature ensures criteria are clear and unambiguous. Career
      ladders require careful differentiation between levels.

  compensation_benefits:
    model: claude-haiku-4-5
    max_tokens: 8192
    temperature: 0.3
    rationale: >
      Compensation analysis is data-driven and structurally predictable --
      benchmarking, band construction, equity calculations. Haiku handles
      these patterns efficiently. Low temperature ensures numerical precision
      and consistent formatting.
```

### Default Cost Estimate

| Agent | Model | Tokens/Run | Cost/Run |
|-------|-------|-----------|----------|
| Coordinator | Opus 4.6 | ~80K | ~$16.00 |
| Talent Acquisition | Sonnet 4.5 | ~160K | ~$14.40 |
| Onboarding & Enablement | Sonnet 4.5 | ~140K | ~$12.60 |
| Culture & Engagement | Sonnet 4.5 | ~150K | ~$13.50 |
| Performance Management | Sonnet 4.5 | ~150K | ~$13.50 |
| Compensation & Benefits | Haiku 4.5 | ~100K | ~$8.00 |
| **Total** | | **~780K** | **~$78.00** |

---

## Budget Configuration

For cost-sensitive deployments. Shifts more work to Haiku where feasible. Reduces token limits to focus on essentials.

```yaml
budget:
  coordinator:
    model: claude-sonnet-4-5
    max_tokens: 8192
    temperature: 0.5
    rationale: >
      Sonnet can handle people strategy for straightforward scenarios
      (small team, single location, clear business model). Loses some
      nuance on complex org design but delivers solid fundamentals.

  talent_acquisition:
    model: claude-sonnet-4-5
    max_tokens: 8192
    temperature: 0.6
    rationale: >
      Hiring quality is not the place to cut corners. Sonnet stays here
      because a mis-hire costs 1.5-2x annual salary. Reduced token limit
      focuses output on essentials.

  onboarding_enablement:
    model: claude-haiku-4-5
    max_tokens: 8192
    temperature: 0.4
    rationale: >
      Onboarding plans are highly templatable. Haiku can produce solid
      checklists and schedules. Loses some creativity in learning path
      design but covers the fundamentals well.

  culture_engagement:
    model: claude-haiku-4-5
    max_tokens: 8192
    temperature: 0.5
    rationale: >
      Budget configuration sacrifices some depth in culture work.
      Haiku can produce values documentation and basic ritual designs
      but may need human review for nuance and tone.

  performance_management:
    model: claude-haiku-4-5
    max_tokens: 8192
    temperature: 0.3
    rationale: >
      OKR templates, review forms, and career ladder structures are
      pattern-based. Haiku handles these efficiently. May need human
      review on the judgment calls in calibration guidance.

  compensation_benefits:
    model: claude-haiku-4-5
    max_tokens: 4096
    temperature: 0.2
    rationale: >
      Already the budget-friendly choice in the default config. Further
      reduced token limit focuses on core deliverables only.
```

### Budget Cost Estimate

| Agent | Model | Tokens/Run | Cost/Run |
|-------|-------|-----------|----------|
| Coordinator | Sonnet 4.5 | ~60K | ~$5.40 |
| Talent Acquisition | Sonnet 4.5 | ~120K | ~$10.80 |
| Onboarding & Enablement | Haiku 4.5 | ~100K | ~$8.00 |
| Culture & Engagement | Haiku 4.5 | ~80K | ~$6.40 |
| Performance Management | Haiku 4.5 | ~80K | ~$6.40 |
| Compensation & Benefits | Haiku 4.5 | ~80K | ~$3.20 |
| **Total** | | **~520K** | **~$40.20** |

**Trade-offs:**
- Culture and engagement outputs will be more generic and may lack nuance
- Onboarding plans will be functional but less creative
- Performance frameworks will be solid templates but may need human judgment for edge cases
- Coordinator loses some depth on complex organizational dynamics

---

## Premium Configuration

For critical People operations -- executive hiring, major org restructuring, culture transformation. Maximum output quality across all agents.

```yaml
premium:
  coordinator:
    model: claude-opus-4-6
    max_tokens: 32768
    temperature: 0.7
    rationale: >
      Extended token limit allows for deep-dive strategy documents,
      comprehensive org design, and thorough scenario planning.
      Higher temperature encourages exploration of non-obvious
      organizational structures.

  talent_acquisition:
    model: claude-opus-4-6
    max_tokens: 16384
    temperature: 0.7
    rationale: >
      Opus for executive and critical-path hiring. Better at reading
      between the lines of candidate signals, designing interviews
      for senior roles, and crafting compelling narratives for
      hard-to-fill positions.

  onboarding_enablement:
    model: claude-sonnet-4-5
    max_tokens: 16384
    temperature: 0.6
    rationale: >
      Extended limits allow for comprehensive, role-specific onboarding
      programs. Sonnet remains appropriate -- onboarding is important
      but does not require Opus-level reasoning.

  culture_engagement:
    model: claude-opus-4-6
    max_tokens: 16384
    temperature: 0.8
    rationale: >
      Culture transformation is one of the hardest problems in
      organizational design. Opus brings deeper understanding of
      human dynamics, organizational psychology, and systemic
      change. Higher temperature supports creative ritual design.

  performance_management:
    model: claude-sonnet-4-5
    max_tokens: 16384
    temperature: 0.5
    rationale: >
      Extended limits for comprehensive career ladders and detailed
      calibration guidance. Sonnet handles this well even in premium
      configuration -- the domain is more about thoroughness than
      depth of reasoning.

  compensation_benefits:
    model: claude-sonnet-4-5
    max_tokens: 12288
    temperature: 0.3
    rationale: >
      Upgraded from Haiku for complex equity modeling, multi-geography
      compensation, and sophisticated benefits analysis. Sonnet provides
      better handling of edge cases in compensation design.
```

### Premium Cost Estimate

| Agent | Model | Tokens/Run | Cost/Run |
|-------|-------|-----------|----------|
| Coordinator | Opus 4.6 | ~120K | ~$24.00 |
| Talent Acquisition | Opus 4.6 | ~100K | ~$20.00 |
| Onboarding & Enablement | Sonnet 4.5 | ~180K | ~$16.20 |
| Culture & Engagement | Opus 4.6 | ~100K | ~$20.00 |
| Performance Management | Sonnet 4.5 | ~180K | ~$16.20 |
| Compensation & Benefits | Sonnet 4.5 | ~160K | ~$14.40 |
| **Total** | | **~840K** | **~$110.80** |

---

## Configuration Selection Guide

| Scenario | Recommended Config | Why |
|----------|-------------------|-----|
| Startup (pre-seed to seed) building first processes | Budget | Processes will evolve rapidly; invest in iteration, not polish |
| Series A/B scaling from 15 to 50 people | Default | Needs quality systems but cost efficiency matters |
| Executive team hiring | Premium (Talent Acq only) | Bad exec hires are existential; invest in evaluation quality |
| Culture crisis / post-layoff rebuild | Premium (Culture & Coordinator) | Nuance matters enormously when trust is damaged |
| Annual comp review / equity refresh | Default (Comp only) | Structured analysis with standard methodology |
| Rapid growth (doubling in 6 months) | Default | Full team needed, quality matters but so does speed |
| IPO preparation / going public | Premium | Everything must withstand regulatory and public scrutiny |

---

## Model Switching Between Phases

Different phases may benefit from different configurations:

```yaml
phase_specific_overrides:
  phase_1_foundation:
    # Strategy phase benefits from deeper reasoning
    coordinator: claude-opus-4-6  # Always Opus for strategy
    culture_engagement: claude-sonnet-4-5  # At minimum Sonnet

  phase_2_infrastructure:
    # Template-heavy phase can use efficient models
    compensation_benefits: claude-haiku-4-5  # Efficient for data work
    onboarding_enablement: claude-haiku-4-5  # Templates are structured

  phase_3_execution:
    # Execution needs judgment
    talent_acquisition: claude-sonnet-4-5  # Candidate evaluation needs nuance
    performance_management: claude-sonnet-4-5  # Goal setting needs context

  phase_4_optimization:
    # Analysis and synthesis
    coordinator: claude-opus-4-6  # Synthesis of cross-functional data
    # Other agents: minimum viable model for metrics reporting
```

---

## Token Budget Allocation by Phase

```
Phase 1 (Foundation):     ~20% of total budget
Phase 2 (Infrastructure): ~30% of total budget
Phase 3 (Execution):      ~35% of total budget
Phase 4 (Optimization):   ~15% of total budget
```

This allocation reflects that infrastructure and execution phases produce the most content, while foundation and optimization phases are more about strategic thinking and analysis.
