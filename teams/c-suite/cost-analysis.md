# Cost Analysis

Detailed cost projections for the C-Suite Team across model configurations, phases, and scenarios.

---

## Phase-by-Phase Cost Breakdown (Default Configuration)

| Phase | Duration | Agents Active | Est. Input Tokens | Est. Output Tokens | Est. Total Tokens | Est. Cost |
|-------|----------|---------------|-------------------|--------------------|--------------------|-----------|
| Vision Alignment | ~15 min | 1 (CEO) | ~35K | ~15K | ~50K | ~$7.50 |
| Specialist Deep-Dives | ~25-40 min | 6 parallel | ~210K | ~140K | ~350K | ~$21.00 |
| CEO Synthesis | ~15-20 min | 1 (CEO) | ~55K | ~25K | ~80K | ~$12.00 |
| Board Review | ~15 min | 7 parallel | ~70K | ~30K | ~100K | ~$10.00 |
| Iteration & Resolution | ~10 min | 1-3 | ~included | ~included | ~included | ~included |
| Artifact Generation | ~20-30 min | 6 parallel | ~80K | ~40K | ~120K | ~$12.00 |
| **Total** | **~1.5-2 hrs** | | **~450K** | **~250K** | **~700K** | **~$62.50** |

### Phase 1: Vision Alignment (~$7.50)

| Agent | Model | Input Tokens | Output Tokens | Cost |
|-------|-------|-------------|---------------|------|
| CEO / Strategy Lead | Opus 4.6 | ~35K | ~15K | ~$7.50 |
| **Phase Total** | | **~35K** | **~15K** | **~$7.50** |

### Phase 2: Specialist Deep-Dives (~$21.00)

| Agent | Model | Input Tokens | Output Tokens | Cost |
|-------|-------|-------------|---------------|------|
| CFO / Finance | Sonnet 4.5 | ~38K | ~20K | ~$3.48 |
| CMO / Marketing | Sonnet 4.5 | ~38K | ~20K | ~$3.48 |
| CTO / Product | Sonnet 4.5 | ~38K | ~20K | ~$3.48 |
| COO / Operations | Sonnet 4.5 | ~38K | ~20K | ~$3.48 |
| VP Sales | Sonnet 4.5 | ~38K | ~20K | ~$3.48 |
| General Counsel | Sonnet 4.5 | ~38K | ~20K | ~$3.48 |
| **Phase Total** | | **~228K** | **~120K** | **~$20.88** |

### Phase 3: CEO Synthesis (~$12.00)

| Agent | Model | Input Tokens | Output Tokens | Cost |
|-------|-------|-------------|---------------|------|
| CEO / Strategy Lead | Opus 4.6 | ~55K | ~25K | ~$12.00 |
| **Phase Total** | | **~55K** | **~25K** | **~$12.00** |

Note: Phase 3 is token-intensive because the CEO must read all 6 specialist outputs (~6 x 20K output tokens = ~120K input) plus the board brief, then produce the integrated plan.

### Phase 4: Board Review (~$10.00)

| Agent | Model | Input Tokens | Output Tokens | Cost |
|-------|-------|-------------|---------------|------|
| CEO / Strategy Lead | Opus 4.6 | ~15K | ~5K | ~$3.00 |
| CFO / Finance | Sonnet 4.5 | ~10K | ~4K | ~$0.90 |
| CMO / Marketing | Sonnet 4.5 | ~10K | ~4K | ~$0.90 |
| CTO / Product | Sonnet 4.5 | ~10K | ~4K | ~$0.90 |
| COO / Operations | Sonnet 4.5 | ~10K | ~4K | ~$0.90 |
| VP Sales | Sonnet 4.5 | ~10K | ~4K | ~$0.90 |
| General Counsel | Sonnet 4.5 | ~10K | ~4K | ~$0.90 |
| **Phase Total** | | **~75K** | **~29K** | **~$8.40** |

### Phase 6: Artifact Generation (~$12.00)

| Agent | Model | Input Tokens | Output Tokens | Cost |
|-------|-------|-------------|---------------|------|
| CEO / Strategy Lead | Opus 4.6 | ~10K | ~8K | ~$2.10 |
| CFO / Finance | Sonnet 4.5 | ~12K | ~8K | ~$1.56 |
| CMO / Marketing | Sonnet 4.5 | ~12K | ~8K | ~$1.56 |
| CTO / Product | Sonnet 4.5 | ~12K | ~8K | ~$1.56 |
| COO / Operations | Sonnet 4.5 | ~12K | ~8K | ~$1.56 |
| VP Sales | Sonnet 4.5 | ~12K | ~8K | ~$1.56 |
| General Counsel | Sonnet 4.5 | ~12K | ~8K | ~$1.56 |
| **Phase Total** | | **~82K** | **~56K** | **~$11.46** |

---

## Model Configuration Cost Comparison

| Configuration | Opus Agents | Sonnet Agents | Total Tokens | Est. Cost | Savings vs Default |
|--------------|-------------|---------------|-------------|-----------|-------------------|
| Budget | 0 | 7 | ~700K | ~$45-80 | -$35 (-40%) |
| **Default** | **1** | **6** | **~700K** | **~$80-150** | **baseline** |
| Hybrid Finance | 2 | 5 | ~700K | ~$95-170 | +$20 (+15%) |
| Premium | 7 | 0 | ~700K | ~$150-350 | +$100 (+80%) |

### Configuration Cost by Phase

| Phase | Budget | Default | Hybrid Finance | Premium |
|-------|--------|---------|----------------|---------|
| Vision Alignment | ~$3.50 | ~$7.50 | ~$7.50 | ~$7.50 |
| Specialist Deep-Dives | ~$21.00 | ~$21.00 | ~$24.50 | ~$52.50 |
| CEO Synthesis | ~$4.80 | ~$12.00 | ~$12.00 | ~$12.00 |
| Board Review | ~$4.20 | ~$10.00 | ~$10.90 | ~$15.00 |
| Artifact Generation | ~$7.20 | ~$12.00 | ~$13.50 | ~$18.00 |
| **Total** | **~$40.70** | **~$62.50** | **~$68.40** | **~$105.00** |
| + 20% buffer | ~$8.14 | ~$12.50 | ~$13.68 | ~$21.00 |
| **Effective Total** | **~$49** | **~$75** | **~$82** | **~$126** |

---

## Sensitivity Analysis

### Token Usage Variance

Actual token usage varies by business complexity. These multipliers apply to the default estimates:

| Business Complexity | Multiplier | Est. Total Tokens | Est. Cost (Default) |
|-------------------|------------|-------------------|---------------------|
| Simple (single product, clear market) | 0.7x | ~490K | ~$55 |
| Standard (SaaS, defined competitors) | 1.0x | ~700K | ~$75 |
| Complex (marketplace, multiple segments) | 1.4x | ~980K | ~$105 |
| Very Complex (regulated, multi-geography) | 1.8x | ~1,260K | ~$135 |

### Iteration Costs

Board review disagreements and conflict resolution trigger additional tokens:

| Scenario | Additional Tokens | Additional Cost |
|----------|------------------|-----------------|
| Single specialist revision, 1 cycle | ~20-30K | ~$2-4 |
| CEO re-synthesis after major feedback | ~40-60K | ~$6-9 |
| Full board review redo (rare) | ~80-120K | ~$10-18 |
| Financial model restructure | ~50-80K | ~$5-10 |

**Recommendation:** Budget 20% above estimated cost for iteration cycles. Business planning often requires multiple rounds of cross-functional alignment.

### Impact of Output Toggles

Disabling outputs in CONFIG reduces cost:

| Output Toggle | Token Impact | Cost Impact (Default) |
|---------|-------------|----------------------|
| `financial_model: false` | -80K | -$5 |
| `pitch_deck: false` | -40K | -$4 |
| `sales_playbook: false` | -50K | -$3 |
| `marketing_plan: false` | -50K | -$3 |
| `product_roadmap: false` | -40K | -$3 |
| `org_chart: false` | -30K | -$2 |
| `legal_checklist: false` | -30K | -$2 |
| `projection_years: 3` (vs 5) | -30K | -$2 |

---

## External Service Costs

Beyond agent execution costs, the MCP server integrations have their own pricing:

### Free Tier (Suitable for Most Startups)

| Service | Tier | Monthly Cost |
|---------|------|-------------|
| Google Sheets | Free (Google Workspace) | $0 |
| Notion | Free (for personal use) | $0 |
| Linear | Free (up to 250 issues) | $0 |
| **Total** | | **$0** |

### Professional Tier

| Service | Tier | Monthly Cost |
|---------|------|-------------|
| Google Workspace | Business Starter | $7/user/month |
| Notion | Plus | $10/user/month |
| Linear | Standard | $8/user/month |
| **Total** | | **~$25/user/month** |

---

## Break-Even Analysis

Comparing agent cost to consultant cost for the same work:

| Metric | Human Team (MBA Consultants) | Agent Team (Default) | Agent Team (Premium) |
|--------|------------------------------|---------------------|---------------------|
| Calendar time | 2-4 weeks | ~1.5-2 hours | ~1.5-2 hours |
| Consultant hours | 80-160 hours | 0 (review only) | 0 (review only) |
| Cost at $200/hr | $16,000-$32,000 | ~$75-150 | ~$150-350 |
| Cost at $100/hr | $8,000-$16,000 | ~$75-150 | ~$150-350 |
| Quality review needed | Partner review | Founder review | Founder review |
| Iteration cost | Additional hours billed | Additional $10-40/cycle | Additional $20-60/cycle |

**Key takeaway:** Agent execution costs are 2-3 orders of magnitude lower than equivalent consulting engagement. The primary investment is the founder's time reviewing and refining agent output.

---

## Cost Optimization Tips

1. **Start with Budget config for idea exploration.** Switch to Default when preparing investor materials.
2. **Disable unused outputs.** If you do not need a pitch deck yet, set `pitch_deck: false` and save ~$4.
3. **Use 3-year projections instead of 5.** Most early-stage investors focus on the first 3 years anyway.
4. **Run in hybrid mode.** Sequential mode takes longer and costs similarly in tokens due to context drift.
5. **Front-load CONFIG detail.** The more context you provide in CONFIG, the fewer clarification cycles the CEO needs, reducing Phase 1 costs.
6. **Review after Phase 3.** If the CEO synthesis reveals strategic issues, address them before Phase 6 artifact generation to avoid rework.
7. **Reuse across iterations.** If iterating on the same business, Phase 2 specialist outputs can be cached and only delta-updated, reducing costs by 30-40%.
