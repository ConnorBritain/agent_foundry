# Cost Analysis

Detailed cost projections for the Research Deep Dive Team across modes, model configurations, and research complexity levels.

---

## Cost by Mode (Default Configuration)

### Literature Review Mode (~250K tokens, $12-20)

| Phase | Agent(s) | Input Tokens | Output Tokens | Total | Cost |
|-------|----------|-------------|---------------|-------|------|
| Study Design | Coordinator | ~20K | ~10K | ~30K | ~$4.50 |
| Source Discovery (Round 1) | Primary Researcher | ~60K | ~20K | ~80K | ~$4.80 |
| Source Discovery (Round 2) | Primary Researcher | ~30K | ~10K | ~40K | ~$2.40 |
| Analysis | Analyst | ~30K | ~10K | ~40K | ~$2.40 |
| Synthesis | Synthesizer + Coordinator | ~40K | ~20K | ~60K | ~$5.10 |
| **Total** | | **~180K** | **~70K** | **~250K** | **~$19.20** |

### Academic Mode (~440K tokens, $35-60)

| Phase | Agent(s) | Input Tokens | Output Tokens | Total | Cost |
|-------|----------|-------------|---------------|-------|------|
| Study Design | Coordinator + Methodology Designer | ~50K | ~30K | ~80K | ~$12.00 |
| Literature Review | Primary Researcher | ~70K | ~30K | ~100K | ~$6.00 |
| Data Analysis | Analyst | ~60K | ~20K | ~80K | ~$4.80 |
| Peer Review | Peer Reviewer | ~40K | ~20K | ~60K | ~$3.60 |
| Writing | Synthesizer | ~70K | ~30K | ~100K | ~$6.00 |
| Citations | Citation Manager | ~15K | ~5K | ~20K | ~$0.50 |
| **Total** | | **~305K** | **~135K** | **~440K** | **~$32.90** |

### Market/Competitive Mode (~340K tokens, $25-45)

| Phase | Agent(s) | Input Tokens | Output Tokens | Total | Cost |
|-------|----------|-------------|---------------|-------|------|
| Study Design | Coordinator | ~25K | ~15K | ~40K | ~$6.00 |
| Data Collection | Researcher + Market + Competitive + Interview | ~80K | ~40K | ~120K | ~$7.20 |
| Analysis | Analyst + Trend Forecaster | ~70K | ~30K | ~100K | ~$6.00 |
| Synthesis | Synthesizer + Coordinator | ~55K | ~25K | ~80K | ~$5.25 |
| **Total** | | **~230K** | **~110K** | **~340K** | **~$24.45** |

### Product/UX Mode (~280K tokens, $18-30)

| Phase | Agent(s) | Input Tokens | Output Tokens | Total | Cost |
|-------|----------|-------------|---------------|-------|------|
| Study Design | Coordinator | ~20K | ~10K | ~30K | ~$4.50 |
| Data Analysis | Analyst + User Behavior | ~55K | ~25K | ~80K | ~$4.80 |
| Usability | Usability Evaluator | ~40K | ~20K | ~60K | ~$3.60 |
| Prioritization | Feature Prioritizer | ~35K | ~15K | ~50K | ~$3.00 |
| Synthesis | Synthesizer + Coordinator | ~40K | ~20K | ~60K | ~$5.10 |
| **Total** | | **~190K** | **~90K** | **~280K** | **~$21.00** |

---

## Model Configuration Cost Comparison

| Configuration | Opus Agents | Sonnet Agents | Haiku Agents | Market Mode | Academic Mode | vs Default |
|--------------|-------------|---------------|--------------|-------------|---------------|------------|
| Budget | 0 | 7 | 1 | ~$18 | ~$25 | -30% |
| **Default** | **1** | **6** | **1** | **~$25** | **~$35** | **baseline** |
| Premium | 3 | 4 | 1 | ~$45 | ~$60 | +70% |
| Maximum | 4 | 3 | 1 | ~$65 | ~$90 | +150% |

### Configuration Cost by Phase (Market Mode)

| Phase | Budget | Default | Premium | Maximum |
|-------|--------|---------|---------|---------|
| Study Design | ~$2.40 | ~$6.00 | ~$6.00 | ~$6.00 |
| Data Collection | ~$7.20 | ~$7.20 | ~$7.20 | ~$12.00 |
| Analysis | ~$6.00 | ~$6.00 | ~$12.00 | ~$15.00 |
| Synthesis | ~$2.40 | ~$5.25 | ~$10.50 | ~$15.00 |
| **Total** | **~$18** | **~$25** | **~$36** | **~$48** |

---

## Sensitivity Analysis

### Retry and Iteration Costs

Quality gate failures or research pivots add cost:

| Scenario | Additional Tokens | Additional Cost |
|----------|------------------|-----------------|
| Expand search to additional database | ~40-60K | ~$3-5 |
| Deeper analysis on emerging theme | ~30-50K | ~$2-4 |
| Methodology redesign (academic) | ~40-80K | ~$6-12 |
| Additional source discovery round | ~40-60K | ~$3-5 |
| Full re-analysis after new data | ~60-100K | ~$4-8 |
| Complete pipeline restart (rare) | ~250-440K | ~$20-45 |

**Recommendation:** Budget 20% above estimated cost for iterations and discoveries. Research frequently uncovers sub-questions.

### Impact of Configuration Options

| Option | Token Impact | Cost Impact (Default) |
|--------|-------------|----------------------|
| `sources.depth: deep` | +60K | +$4-5 |
| `sources.depth: light` | -40K | -$3-4 |
| `analysis.sensitivity_analysis: true` | +20K | +$1-2 |
| `academic_mode.include_grant_proposal: true` | +60K | +$4-5 |
| `market_mode.include_tam_sam_som: false` | -40K | -$3 |
| Additional mode-specific agent activated | +50-60K | +$3-5 |

---

## Per-Study Cost Estimates

| Study Type | Configuration | Est. Cost | Duration |
|-----------|--------------|-----------|----------|
| Academic (full) | Default | $35-60 | 2-3 hours |
| Academic (lit review only) | Budget | $12-20 | 1-2 hours |
| Market research (comprehensive) | Default | $25-45 | 1-2 hours |
| Competitive intelligence (focused) | Default | $20-35 | 45-90 min |
| Product/UX research | Default | $18-30 | 45-90 min |
| Quick literature scan | Budget | $8-15 | 30-60 min |

---

## Ongoing Research Costs

| Activity | Frequency | Est. Cost |
|----------|-----------|-----------|
| Monthly market update | Monthly | $15-25 |
| Quarterly competitive review | Quarterly | $25-40 |
| Product research sprint | Per sprint | $15-25 |
| Academic paper revision | Per revision | $20-35 |
| Annual market landscape | Annual | $50-80 |

### Annual Cost Scenarios

| Research Cadence | Budget Config | Default Config | Premium Config |
|-----------------|--------------|----------------|----------------|
| 2 studies/month | ~$480/yr | ~$720/yr | ~$1,200/yr |
| 4 studies/month | ~$960/yr | ~$1,440/yr | ~$2,400/yr |
| 8 studies/month | ~$1,920/yr | ~$2,880/yr | ~$4,800/yr |

---

## Break-Even Analysis

Comparing agent cost to human researcher cost for equivalent work:

| Metric | Human Researcher | Agent Team (Default) | Agent Team (Premium) |
|--------|-----------------|---------------------|---------------------|
| Calendar time | 2-6 weeks | 1-3 hours | 1-3 hours |
| Cost per market study | $5,000-$25,000 | ~$25-45 | ~$45-70 |
| Cost per literature review | $2,000-$10,000 | ~$12-20 | ~$20-35 |
| Source verification | Variable | Systematic | Systematic |
| Methodology documentation | Often incomplete | Always included | Always included |
| Reproducibility | Low | High (documented protocol) | High (documented protocol) |

**Key takeaway:** Agent cost is 2-3 orders of magnitude lower than equivalent human research. The primary cost is human time reviewing methodology design and validating findings.

---

## Cost Optimization Tips

1. **Use Literature Review mode for preliminary research.** Core team only, $12-20 per study. Upgrade to full mode after validating the research direction.
2. **Set source depth to "light" for familiar domains.** Deep search is unnecessary when you already know the key sources and landscape.
3. **Disable unused mode features.** If you do not need TAM/SAM/SOM, set `include_tam_sam_som: false` to skip the Market Sizing Analyst.
4. **Review after Phase 1.** Catching methodology or scope issues early avoids expensive downstream rework.
5. **Reuse source databases.** Prior research outputs can be fed into new studies, reducing Phase 2 costs.
6. **Use Budget config for recurring updates.** Monthly market updates on a well-established domain do not need Opus-level study design.
7. **Batch related research questions.** The Coordinator can design a multi-question study that shares data collection, reducing total cost vs running separate studies.
