# Cost Analysis -- Recruitment & HR Team

## Default Configuration Cost Breakdown

### Phase-by-Phase Summary

| Phase | Duration | Active Agents | Est. Tokens | Est. Cost |
|-------|----------|---------------|-------------|-----------|
| Phase 1: Foundation | ~30 min | 3 | ~150K | ~$15 |
| Phase 2: Infrastructure | ~45 min | 3 | ~250K | ~$25 |
| Phase 3: Execution | ~45 min | 4 | ~300K | ~$30 |
| Phase 4: Optimization | ~20 min | 2 | ~80K | ~$8 |
| **Total** | **~2 hrs 20 min** | | **~780K** | **~$78** |

### Phase 1: Foundation (Detailed)

Sequential execution -- agents run one at a time.

| Step | Agent | Model | Input Tokens | Output Tokens | Cost |
|------|-------|-------|-------------|---------------|------|
| 1.1 People Strategy | Coordinator | Opus 4.6 | ~15K | ~25K | ~$6.00 |
| 1.2 Values & Culture | Culture & Engagement | Sonnet 4.5 | ~20K | ~20K | ~$3.60 |
| 1.3 Role Frameworks | Performance Mgmt | Sonnet 4.5 | ~25K | ~30K | ~$5.40 |
| **Phase 1 Total** | | | **~60K** | **~75K** | **~$15.00** |

**Notes:**
- Coordinator uses Opus 4.6 for strategy synthesis -- higher per-token cost but fewer tokens needed
- Culture and Performance agents receive previous outputs as input context, increasing their input token counts
- Output is heavy in Phase 1 because it produces the foundational documents that all subsequent phases reference

### Phase 2: Infrastructure (Detailed)

Parallel execution -- three agents run simultaneously.

| Stream | Agent | Model | Input Tokens | Output Tokens | Cost |
|--------|-------|-------|-------------|---------------|------|
| 2A Hiring Playbook | Talent Acquisition | Sonnet 4.5 | ~30K | ~60K | ~$9.00 |
| 2B Onboarding Program | Onboarding & Enablement | Sonnet 4.5 | ~25K | ~45K | ~$7.20 |
| 2C Compensation | Comp & Benefits | Haiku 4.5 | ~25K | ~40K | ~$5.20 |
| **Phase 2 Total** | | | **~80K** | **~145K** | **~$21.40** |

**Actual cost may reach ~$25 with:**
- Re-prompting for job descriptions that need iteration
- Salary band calculations requiring multiple passes
- Cross-referencing between hiring playbook and compensation outputs

**Notes:**
- Talent Acquisition produces the most output (multiple job descriptions, interview guides, scorecards)
- Compensation analysis is efficient on Haiku -- structured data work with predictable patterns
- Wall-clock time is ~45 min despite parallel execution because Stream 2A has the most deliverables

### Phase 3: Execution (Detailed)

Parallel execution -- four agents run simultaneously.

| Stream | Agent | Model | Input Tokens | Output Tokens | Cost |
|--------|-------|-------|-------------|---------------|------|
| 3A Active Recruiting | Talent Acquisition | Sonnet 4.5 | ~40K | ~50K | ~$9.00 |
| 3B Onboarding Execution | Onboarding & Enablement | Sonnet 4.5 | ~30K | ~35K | ~$6.30 |
| 3C Culture Launch | Culture & Engagement | Sonnet 4.5 | ~30K | ~40K | ~$7.20 |
| 3D Performance Activation | Performance Mgmt | Sonnet 4.5 | ~35K | ~45K | ~$7.50 |
| **Phase 3 Total** | | | **~135K** | **~170K** | **~$30.00** |

**Notes:**
- Input tokens are higher in Phase 3 because agents consume Phase 1 and 2 outputs as context
- All four Sonnet agents run in parallel, so wall-clock time equals the slowest agent (~45 min)
- Recruiting and Performance produce the most output due to templates and guides

### Phase 4: Optimization (Detailed)

Parallel execution -- Coordinator leads, specialists support.

| Stream | Agent | Model | Input Tokens | Output Tokens | Cost |
|--------|-------|-------|-------------|---------------|------|
| 4A System Analysis | Coordinator | Opus 4.6 | ~40K | ~20K | ~$6.00 |
| 4B Agent Refinements | All Specialists | Mixed | ~15K | ~10K | ~$2.00 |
| **Phase 4 Total** | | | **~55K** | **~30K** | **~$8.00** |

**Notes:**
- Coordinator processes outputs from all Phase 3 streams, hence higher input token count
- Specialist refinements are lightweight -- mostly annotations and version updates
- This is the cheapest phase but provides critical strategic value

---

## Configuration Comparisons

### Budget Configuration

| Phase | Duration | Tokens | Cost |
|-------|----------|--------|------|
| Foundation | ~25 min | ~100K | ~$8 |
| Infrastructure | ~40 min | ~180K | ~$14 |
| Execution | ~40 min | ~180K | ~$14 |
| Optimization | ~15 min | ~60K | ~$4 |
| **Total** | **~2 hrs** | **~520K** | **~$40** |

**Cost savings:** ~$38 (49% reduction)
**Quality trade-offs:**
- Coordinator on Sonnet may miss nuance in complex organizational dynamics
- Onboarding and culture outputs will be more template-like, less tailored
- Performance frameworks will be functional but less sophisticated

### Premium Configuration

| Phase | Duration | Tokens | Cost |
|-------|----------|--------|------|
| Foundation | ~40 min | ~200K | ~$25 |
| Infrastructure | ~50 min | ~300K | ~$35 |
| Execution | ~50 min | ~350K | ~$40 |
| Optimization | ~25 min | ~100K | ~$12 |
| **Total** | **~2 hrs 45 min** | **~950K** | **~$112** |

**Additional cost:** ~$34 (44% increase)
**Quality improvements:**
- Opus-level reasoning for culture design and talent acquisition
- Deeper analysis in compensation modeling
- More sophisticated scenario planning and edge case handling

---

## Execution Mode Costs

| Mode | Phases Run | Duration | Tokens | Cost |
|------|-----------|----------|--------|------|
| Full Execution | All 4 | ~2 hr 20 min | ~780K | ~$78 |
| Foundation Only | Phase 1 | ~30 min | ~150K | ~$15 |
| Hiring Sprint | 1 + 2A + 2C | ~1 hr 15 min | ~350K | ~$45 |
| Culture Reset | 1 + 2B + 3C | ~1 hr 15 min | ~300K | ~$40 |
| Performance Overhaul | 1.3 + 3D | ~50 min | ~200K | ~$25 |

---

## Cost Optimization Strategies

### 1. Phase Gating
Run Phase 1 first and review outputs before committing to Phases 2-4. If the foundation is solid, proceed. If not, iterate on Phase 1 (cheaper than re-running everything).

**Potential savings:** Avoids wasted spend on infrastructure built on a flawed strategy.

### 2. Selective Agent Upgrades
Use budget configuration as baseline, then upgrade specific agents for high-stakes work:
- Upgrade Talent Acquisition to Sonnet for executive hiring only
- Upgrade Culture to Sonnet only during culture crises
- Keep Compensation on Haiku -- it performs well for structured analysis

**Potential savings:** $15-25 per run depending on which agents are upgraded.

### 3. Template Reuse
After the first full run, many outputs (career ladders, interview guides, onboarding plans) need only incremental updates. Subsequent runs can use the budget configuration with previous outputs as context.

**Potential savings:** 40-60% on subsequent runs.

### 4. Batch Hiring
Run the hiring playbook once for a batch of similar roles rather than individually. Five engineering job descriptions in one run cost less than five separate runs.

**Potential savings:** ~30% on multi-role hiring.

---

## Cost vs. Impact Analysis

| Investment | Cost | Impact | ROI Signal |
|-----------|------|--------|-----------|
| People strategy | ~$6 | Aligns all people decisions | High -- prevents expensive misalignment |
| Job descriptions | ~$5 each | Better candidate quality | High -- bad hires cost 1.5-2x salary |
| Interview scorecards | ~$3 each | Consistent evaluation | High -- reduces bias and mis-hires |
| Onboarding program | ~$12 | Faster time-to-productivity | High -- new hires contribute weeks earlier |
| Culture framework | ~$10 | Retention and engagement | Medium -- hard to measure directly |
| Career ladders | ~$8 | Reduced attrition | High -- top performers stay when they see a path |
| Salary bands | ~$5 | Pay equity, faster offers | High -- removes negotiation bias |
| Performance system | ~$12 | Fair evaluations | Medium -- improves over multiple cycles |

### Comparison: AI Team Cost vs. Consulting Cost

| Deliverable | AI Team Cost | HR Consultant Cost | Time (AI) | Time (Consultant) |
|------------|-------------|-------------------|-----------|-------------------|
| Full People operations suite | ~$78 | $15,000-$40,000 | ~2.5 hours | 4-8 weeks |
| Hiring infrastructure only | ~$45 | $5,000-$15,000 | ~1.25 hours | 1-3 weeks |
| Culture framework only | ~$40 | $8,000-$20,000 | ~1.25 hours | 2-4 weeks |
| Compensation analysis only | ~$15 | $5,000-$12,000 | ~30 minutes | 1-2 weeks |

**Important caveat:** AI-generated outputs are strong starting points but benefit from human review, especially for culture-sensitive decisions, legal compliance, and company-specific context that may not be captured in the configuration.

---

## Token Usage by Deliverable Type

| Deliverable Type | Avg. Tokens | Examples |
|-----------------|-------------|----------|
| Strategy documents | ~8K output | People strategy, culture framework |
| Job descriptions | ~2K output each | Individual role descriptions |
| Interview guides | ~4K output each | Phone screen, technical, team, final |
| Templates | ~1.5K output each | OKR template, 1:1 guide, review form |
| Playbooks | ~6K output each | Sourcing playbook, onboarding playbook |
| Analysis reports | ~5K output | Pay equity report, optimization report |
| Checklists | ~1K output each | Pre-boarding, Day 1, equipment provisioning |

These averages help estimate costs for partial runs or custom execution modes.
