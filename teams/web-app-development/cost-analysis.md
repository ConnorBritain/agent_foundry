# Cost Analysis

Detailed cost projections for the Web App Development Team across model configurations, phases, and scenarios.

---

## Phase-by-Phase Cost Breakdown (Default Configuration)

| Phase | Duration | Agents Active | Est. Input Tokens | Est. Output Tokens | Est. Total Tokens | Est. Cost |
|-------|----------|---------------|-------------------|--------------------|--------------------|-----------|
| Foundation | ~30 min | 4 parallel | ~150K | ~50K | ~200K | ~$20 |
| Core Features | ~60 min | 4 parallel | ~280K | ~120K | ~400K | ~$40 |
| Integration & Revenue | ~45 min | 5 parallel | ~210K | ~90K | ~300K | ~$30 |
| Launch Prep | ~30 min | 5 parallel | ~110K | ~40K | ~150K | ~$15 |
| **Total** | **~2.75 hrs** | | **~750K** | **~300K** | **~1,050K** | **~$105** |

### Phase 1: Foundation (~$20)

| Agent | Model | Input Tokens | Output Tokens | Cost |
|-------|-------|-------------|---------------|------|
| Coordinator | Opus 4.6 | ~30K | ~15K | ~$5.70 |
| Cloud/DevOps | Sonnet 4.5 | ~25K | ~10K | ~$2.25 |
| Database Engineer | Sonnet 4.5 | ~35K | ~15K | ~$3.30 |
| Senior Full-Stack | Opus 4.6 | ~60K | ~10K | ~$8.40 |
| **Phase Total** | | **~150K** | **~50K** | **~$19.65** |

### Phase 2: Core Features (~$40)

| Agent | Model | Input Tokens | Output Tokens | Cost |
|-------|-------|-------------|---------------|------|
| Senior Full-Stack | Opus 4.6 | ~80K | ~40K | ~$15.00 |
| Database Engineer | Sonnet 4.5 | ~40K | ~20K | ~$4.20 |
| Marketing Frontend | Sonnet 4.5 | ~50K | ~30K | ~$5.70 |
| QA/Test Engineer | Sonnet 4.5 | ~40K | ~20K | ~$4.20 |
| **Phase Total** | | **~210K** | **~110K** | **~$29.10** |

Note: Phase 2 often runs slightly under budget as agents can reuse Phase 1 context efficiently.

### Phase 3: Integration & Revenue (~$30)

| Agent | Model | Input Tokens | Output Tokens | Cost |
|-------|-------|-------------|---------------|------|
| Senior Full-Stack | Opus 4.6 | ~40K | ~20K | ~$7.50 |
| RevOps | Sonnet 4.5 | ~45K | ~25K | ~$4.95 |
| Database Engineer | Sonnet 4.5 | ~30K | ~15K | ~$3.15 |
| Cloud/DevOps | Sonnet 4.5 | ~25K | ~10K | ~$2.25 |
| Marketing Frontend | Sonnet 4.5 | ~20K | ~10K | ~$2.10 |
| **Phase Total** | | **~160K** | **~80K** | **~$19.95** |

### Phase 4: Launch Prep (~$15)

| Agent | Model | Input Tokens | Output Tokens | Cost |
|-------|-------|-------------|---------------|------|
| QA/Test Engineer | Sonnet 4.5 | ~30K | ~10K | ~$2.40 |
| RevOps | Sonnet 4.5 | ~20K | ~8K | ~$1.80 |
| Cloud/DevOps | Sonnet 4.5 | ~20K | ~8K | ~$1.80 |
| Marketing Frontend | Sonnet 4.5 | ~15K | ~5K | ~$1.20 |
| Coordinator | Opus 4.6 | ~25K | ~9K | ~$3.45 |
| **Phase Total** | | **~110K** | **~40K** | **~$10.65** |

---

## Model Configuration Cost Comparison

| Configuration | Opus Agents | Sonnet Agents | Total Tokens | Est. Cost | Savings vs Default |
|--------------|-------------|---------------|-------------|-----------|-------------------|
| Budget | 0 | 7 | ~1,050K | ~$63 | -$42 (-40%) |
| Hybrid A (Opus Coordinator only) | 1 | 6 | ~1,050K | ~$75 | -$30 (-29%) |
| **Default** | **2** | **5** | **~1,050K** | **~$105** | **baseline** |
| Hybrid B (Opus code-heavy) | 3 | 4 | ~1,050K | ~$127 | +$22 (+21%) |
| Premium | 7 | 0 | ~1,050K | ~$158 | +$53 (+50%) |

### Configuration Cost by Phase

| Phase | Budget | Hybrid A | Default | Hybrid B | Premium |
|-------|--------|----------|---------|----------|---------|
| Foundation | ~$12 | ~$15 | ~$20 | ~$23 | ~$30 |
| Core Features | ~$24 | ~$28 | ~$40 | ~$45 | ~$60 |
| Integration & Revenue | ~$18 | ~$20 | ~$30 | ~$35 | ~$45 |
| Launch Prep | ~$9 | ~$12 | ~$15 | ~$18 | ~$23 |
| **Total** | **~$63** | **~$75** | **~$105** | **~$121** | **~$158** |

---

## Sensitivity Analysis

### Token Usage Variance

Actual token usage varies by project complexity. These multipliers apply to the default estimates:

| Project Complexity | Multiplier | Est. Total Tokens | Est. Cost (Default) |
|-------------------|------------|-------------------|---------------------|
| Simple (basic CRUD, single entity) | 0.7x | ~735K | ~$74 |
| Standard (multi-entity, standard features) | 1.0x | ~1,050K | ~$105 |
| Complex (real-time, multi-role, advanced logic) | 1.4x | ~1,470K | ~$147 |
| Very Complex (marketplace, multi-tenant, compliance) | 1.8x | ~1,890K | ~$189 |

### Retry and Iteration Costs

Quality gate failures trigger retries. Each retry adds cost:

| Scenario | Additional Tokens | Additional Cost |
|----------|------------------|-----------------|
| Single agent output rejected, 1 retry | ~30-50K | ~$3-8 |
| Phase gate fails, 2 agents redo work | ~80-120K | ~$10-18 |
| Schema redesign (Phase 2 redo) | ~150-200K | ~$15-25 |
| Full phase retry (worst case) | ~200-400K | ~$20-40 |

**Recommendation:** Budget 15% above estimated cost for retries. The default estimate of $105 already includes this buffer.

### Impact of Feature Toggles

Turning features on/off in the configuration affects cost:

| Feature | Token Impact | Cost Impact (Default) |
|---------|-------------|----------------------|
| `blog: true` | +80K | +$8 |
| `i18n: true` | +120K | +$12 |
| `realtime: true` | +60K | +$6 |
| `admin_panel: true` | +100K | +$10 |
| `api_keys: true` | +40K | +$4 |
| `dark_mode: true` | +30K | +$3 |
| `onboarding_wizard: true` | +50K | +$5 |
| `payment_model: none` | -130K | -$13 |
| `marketing_site: false` | -120K | -$12 |

---

## Infrastructure Costs (Monthly Ongoing)

Beyond agent execution costs, the deployed application incurs monthly infrastructure costs:

### Free Tier (Suitable for Development and Early Launch)

| Service | Tier | Monthly Cost |
|---------|------|-------------|
| Supabase | Free | $0 |
| Vercel | Hobby | $0 |
| Stripe | Pay-as-you-go | 2.9% + $0.30 per transaction |
| GitHub | Free | $0 |
| Sentry | Developer | $0 |
| **Total** | | **~$0 + Stripe fees** |

**Limits:** Supabase Free: 500MB DB, 1GB storage, 2GB bandwidth, 50K auth MAU. Vercel Hobby: 100GB bandwidth, no team features.

### Growth Tier (Suitable for Post-Launch)

| Service | Tier | Monthly Cost |
|---------|------|-------------|
| Supabase | Pro | $25 |
| Vercel | Pro | $20 |
| Stripe | Pay-as-you-go | 2.9% + $0.30 per transaction |
| GitHub | Free/Team | $0-$4/user |
| Sentry | Team | $26 |
| **Total** | | **~$71 + Stripe fees** |

### Scale Tier

| Service | Tier | Monthly Cost |
|---------|------|-------------|
| Supabase | Team | $599 |
| Vercel | Enterprise | Custom |
| Stripe | Pay-as-you-go | 2.9% + $0.30 (volume discounts available) |
| GitHub | Enterprise | $21/user |
| Sentry | Business | $80 |
| **Total** | | **~$700+ per month** |

---

## Break-Even Analysis

Comparing agent cost to developer cost for the same work:

| Metric | Human Team (3 devs) | Agent Team (Default) | Agent Team (Premium) |
|--------|---------------------|---------------------|---------------------|
| Calendar time | 2-4 weeks | ~2.75 hours | ~2.75 hours |
| Developer hours | 120-240 hours | 0 (supervision only) | 0 (supervision only) |
| Cost at $150/hr | $18,000-$36,000 | ~$105 | ~$158 |
| Cost at $75/hr | $9,000-$18,000 | ~$105 | ~$158 |
| Quality review needed | Peer review | Human review of output | Human review of output |
| Iteration cost | Additional hours | Additional $20-40/retry | Additional $30-60/retry |

**Key takeaway:** Even with multiple retries, agent execution costs are 2-3 orders of magnitude lower than equivalent human developer time. The primary cost is the human time spent reviewing and refining agent output.

---

## Cost Optimization Tips

1. **Start with Budget config for prototypes.** Switch to Default for production builds.
2. **Disable unused features.** Every disabled feature saves tokens.
3. **Use `payment_model: none` for internal tools.** Saves ~$13 by skipping RevOps work.
4. **Use `marketing_site: false` for internal tools.** Saves ~$12.
5. **Run in hybrid mode.** Sequential mode wastes time but costs the same in tokens. Hybrid mode is both faster and often slightly cheaper (less context drift between phases).
6. **Review and prune after Phase 1.** If the foundation is solid, subsequent phases often run under budget.
7. **Cache shared context.** If running multiple projects, the Coordinator's architecture patterns can be reused, reducing Phase 1 costs for subsequent projects.
