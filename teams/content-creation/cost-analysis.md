# Cost Analysis

Detailed cost projections for the Content Creation Team across model configurations, phases, and content types.

---

## Phase-by-Phase Cost Breakdown (Default Configuration)

| Phase | Duration | Agents Active | Est. Input Tokens | Est. Output Tokens | Est. Total Tokens | Est. Cost |
|-------|----------|---------------|-------------------|--------------------|--------------------|-----------|
| Vision + Research | ~10 min | 2 parallel | ~50K | ~20K | ~70K | ~$7.00 |
| Drafting | ~15 min | 1 | ~40K | ~20K | ~60K | ~$3.60 |
| Humanize + Critique | ~15 min | 2 parallel | ~70K | ~30K | ~100K | ~$6.00 |
| Fact-Check | ~5-10 min | 1 | ~15K | ~5K | ~20K | ~$0.50 |
| Incorporate + Format | ~10 min | 2 parallel | ~30K | ~10K | ~40K | ~$4.75 |
| **Total** | **~55-60 min** | | **~205K** | **~85K** | **~290K** | **~$21.85** |

### Phase 1: Vision + Research (~$7.00)

| Agent | Model | Input Tokens | Output Tokens | Cost |
|-------|-------|-------------|---------------|------|
| Coordinator / Editor | Opus 4.6 | ~20K | ~10K | ~$4.50 |
| Research Specialist | Sonnet 4.5 | ~30K | ~10K | ~$2.40 |
| **Phase Total** | | **~50K** | **~20K** | **~$6.90** |

### Phase 2: Drafting (~$3.60)

| Agent | Model | Input Tokens | Output Tokens | Cost |
|-------|-------|-------------|---------------|------|
| Content Drafter | Sonnet 4.5 | ~40K | ~20K | ~$3.60 |
| **Phase Total** | | **~40K** | **~20K** | **~$3.60** |

### Phase 3: Humanize + Critique (~$6.00)

| Agent | Model | Input Tokens | Output Tokens | Cost |
|-------|-------|-------------|---------------|------|
| Humanizer | Sonnet 4.5 | ~35K | ~15K | ~$3.00 |
| Content Critic | Sonnet 4.5 | ~35K | ~15K | ~$3.00 |
| **Phase Total** | | **~70K** | **~30K** | **~$6.00** |

### Phase 4: Fact-Check (~$0.50)

| Agent | Model | Input Tokens | Output Tokens | Cost |
|-------|-------|-------------|---------------|------|
| Fact Checker | Haiku 4.5 | ~15K | ~5K | ~$0.50 |
| **Phase Total** | | **~15K** | **~5K** | **~$0.50** |

### Phase 5: Incorporate + Format (~$4.75)

| Agent | Model | Input Tokens | Output Tokens | Cost |
|-------|-------|-------------|---------------|------|
| Coordinator / Editor | Opus 4.6 | ~25K | ~5K | ~$4.50 |
| Format Specialist | Haiku 4.5 | ~8K | ~2K | ~$0.25 |
| **Phase Total** | | **~33K** | **~7K** | **~$4.75** |

---

## Model Configuration Cost Comparison

| Configuration | Opus Agents | Sonnet Agents | Haiku Agents | Est. Cost/Article | vs Default |
|--------------|-------------|---------------|--------------|-------------------|------------|
| Budget | 0 | 5 | 2 | ~$17 | -19% |
| **Default** | **1** | **4** | **2** | **~$21** | **baseline** |
| Premium | 3 | 2 | 2 | ~$38 | +81% |
| Maximum | 5 | 1 | 1 | ~$52 | +148% |

### Configuration Cost by Phase

| Phase | Budget | Default | Premium | Maximum |
|-------|--------|---------|---------|---------|
| Vision + Research | ~$4.50 | ~$7.00 | ~$7.00 | ~$11.50 |
| Drafting | ~$3.60 | ~$3.60 | ~$9.00 | ~$9.00 |
| Humanize + Critique | ~$6.00 | ~$6.00 | ~$10.50 | ~$16.50 |
| Fact-Check | ~$0.50 | ~$0.50 | ~$0.50 | ~$3.00 |
| Incorporate + Format | ~$2.40 | ~$4.75 | ~$4.75 | ~$4.75 |
| **Total** | **~$17** | **~$21** | **~$38** | **~$52** |

---

## Cost by Content Type

Different content types consume different token budgets based on length and complexity.

| Content Type | Word Count | Research Tokens | Drafting Tokens | Review Tokens | Total Tokens | Est. Cost (Default) |
|-------------|------------|-----------------|-----------------|---------------|-------------|---------------------|
| Short blog post | 800-1,200 | ~30K | ~30K | ~50K | ~160K | ~$12-18 |
| Long-form article | 2,500-4,000 | ~70K | ~60K | ~100K | ~290K | ~$18-30 |
| Technical doc | 1,500-3,000 | ~50K | ~50K | ~80K | ~230K | ~$15-25 |
| White paper | 4,000-8,000 | ~100K | ~100K | ~150K | ~430K | ~$25-45 |
| Email newsletter | 500-800 | ~20K | ~20K | ~40K | ~120K | ~$8-15 |
| Social campaign (10 posts) | 2,000-3,000 | ~40K | ~40K | ~80K | ~220K | ~$15-25 |

### Scaling Multipliers

| Content Length | Multiplier | Rationale |
|---------------|------------|-----------|
| Under 1,000 words | 0.6x | Less research, shorter review cycles |
| 1,000-2,500 words | 0.85x | Standard blog post range |
| 2,500-4,000 words | 1.0x | Baseline (long-form article) |
| 4,000-6,000 words | 1.4x | More research depth, longer review |
| 6,000-10,000 words | 1.8x | White paper territory, extensive citations |

---

## Sensitivity Analysis

### Retry and Iteration Costs

Quality gate failures trigger retries. Each retry adds cost:

| Scenario | Additional Tokens | Additional Cost |
|----------|------------------|-----------------|
| Humanizer re-pass (AI patterns above threshold) | ~30-40K | ~$2-3 |
| Drafter revision (structural issues) | ~40-60K | ~$3-5 |
| Fact Checker flags FALSE claim, Coordinator revises | ~15-20K | ~$2-4 |
| Full Phase 3 redo (Humanize + Critique) | ~80-100K | ~$6-8 |
| Complete pipeline restart (rare) | ~250K | ~$20 |

**Recommendation:** Budget 20% above estimated cost for retries. The default estimate of ~$21 becomes ~$25 with buffer.

### Impact of Configuration Options

| Option | Token Impact | Cost Impact (Default) |
|--------|-------------|----------------------|
| `research.depth: deep` | +40K | +$3 |
| `research.depth: light` | -20K | -$2 |
| `seo.enabled: true` | +15K | +$1 |
| `humanization.aggressiveness: aggressive` | +25K | +$2 |
| `humanization.aggressiveness: light` | -15K | -$1 |
| `user_writing_samples` provided | +10K | +$1 |
| `iteration_budget: 3` (from default 2) | +50K potential | +$4 potential |

---

## Volume Pricing Scenarios

### Content Calendar: 4 Articles per Month

| Configuration | Per Article | Monthly (4 articles) | Annual |
|--------------|-------------|---------------------|--------|
| Budget | ~$17 | ~$68 | ~$816 |
| Default | ~$21 | ~$84 | ~$1,008 |
| Premium | ~$38 | ~$152 | ~$1,824 |

### Content Calendar: 12 Articles per Month

| Configuration | Per Article | Monthly (12 articles) | Annual |
|--------------|-------------|----------------------|--------|
| Budget | ~$17 | ~$204 | ~$2,448 |
| Default | ~$21 | ~$252 | ~$3,024 |
| Premium | ~$38 | ~$456 | ~$5,472 |

---

## Break-Even Analysis

Comparing agent cost to freelance writer cost for equivalent work:

| Metric | Freelance Writer | Agent Team (Default) | Agent Team (Premium) |
|--------|-----------------|---------------------|---------------------|
| Calendar time | 3-7 days | ~1 hour | ~1 hour |
| Cost per article (2,500-4,000 words) | $500-$2,000 | ~$21 | ~$38 |
| Research quality | Varies | Systematic, sourced | Systematic, sourced |
| Fact-checking included | Rarely | Always | Always |
| Style guide enforcement | Manual review | Automated | Automated |
| AI pattern audit | Not applicable | Included | Included |
| Revision cost | $100-$500/round | ~$5-8/round | ~$8-12/round |

**Key takeaway:** Agent cost is 1-2 orders of magnitude lower than equivalent freelance work. The primary cost is human time reviewing output and providing editorial direction.

---

## Cost Optimization Tips

1. **Use Budget config for internal content.** Blog posts, newsletters, and internal docs rarely need Opus-level editorial judgment.
2. **Use Premium for external thought leadership.** Investor-facing, press-facing, or high-stakes content justifies the Opus Drafter and Humanizer.
3. **Batch similar content.** Research findings can be reused across related articles, reducing Phase 1 costs for subsequent pieces.
4. **Set research depth to "light" for familiar topics.** Deep research is wasteful when you already know the domain well.
5. **Provide writing samples.** Voice matching reduces Humanizer iterations, saving $2-4 per article.
6. **Review after Phase 1.** Catching angle or research issues early avoids expensive downstream rework.
7. **Keep iteration budget at 2.** A third Humanizer pass rarely yields significant improvement over the second.
