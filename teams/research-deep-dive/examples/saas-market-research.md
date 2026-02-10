# Example: SaaS Market Research

This example demonstrates a market sizing and competitive analysis for a B2B SaaS product entering the customer data platform (CDP) market.

---

## Research Brief

| Property | Value |
|----------|-------|
| **Research Type** | Market/Competitive |
| **Research Question** | "What is the total addressable market for a mid-market CDP, and who are the primary competitors serving the $10M-$500M ARR segment?" |
| **Domain** | Technology / SaaS |
| **Mode** | Market |
| **Configuration** | Default |
| **Actual Cost** | ~$34 |
| **Duration** | ~85 minutes (hybrid mode) |

---

## Configuration Used

```yaml
research_type: market
domain: technology
research_question: "What is the total addressable market for a mid-market customer data platform (CDP), and who are the primary competitors serving companies with $10M-$500M ARR?"
market_mode:
  enabled: true
  market_definition: "Customer data platforms (CDPs) for mid-market B2B and B2C companies"
  geographic_scope: global
  customer_segments:
    - "B2B SaaS companies ($10M-$500M ARR)"
    - "B2C e-commerce brands ($10M-$500M revenue)"
    - "Fintech companies ($10M-$500M ARR)"
  include_tam_sam_som: true
  include_competitive_landscape: true
  include_trend_analysis: true
sources:
  depth: standard
  max_sources: 25
  source_recency_years: 2
agent_budget:
  model_config: default
  max_total_cost_usd: 50
```

---

## Phase 1: Study Design (Coordinator Output)

The Coordinator produced the following study protocol:

**Refined Research Question:** What is the TAM/SAM/SOM for a mid-market CDP targeting companies with $10M-$500M ARR, who are the top 10 competitors in this segment, and what are the key competitive dynamics?

**Sub-questions:**
1. What is the overall CDP market size and growth rate?
2. What percentage of the CDP market is mid-market ($10M-$500M ARR customers)?
3. Who are the primary competitors and what are their estimated revenues?
4. What pricing models and ranges dominate the mid-market segment?
5. What are the key buying criteria for mid-market CDP buyers?
6. What trends will shape the CDP market over the next 3-5 years?

**Methodology:** Top-down sizing from industry analyst reports, bottom-up sizing from competitor revenue and customer count estimates. Competitive analysis from public data, job postings, and customer reviews.

**Active Agents:** Coordinator, Primary Researcher, Analyst, Synthesizer, Market Sizing Analyst, Competitive Intelligence, Trend Forecaster (7 agents).

**Estimated Cost:** $30-40.

---

## Phase 2: Data Collection Summary

The Primary Researcher found 23 sources:

| Category | Count | Examples |
|----------|-------|---------|
| Industry analyst reports | 4 | Gartner Magic Quadrant for CDPs, IDC MarketScape, Forrester Wave |
| Company financial data | 5 | Segment (Twilio earnings), mParticle funding round, Rudderstack series B |
| Market research reports | 3 | Grand View Research CDP report, Markets and Markets CDP forecast |
| Customer review platforms | 3 | G2 CDP category, TrustRadius CDP reviews |
| Industry publications | 5 | MarTech Today, CDP Institute reports, TechCrunch funding coverage |
| Expert analysis | 3 | Industry blog posts from recognized CDP analysts |

**Research Gaps Identified:**
- No reliable public data on mid-market segment breakout (most reports cover total market)
- Private company revenue estimates vary by 30-50% across sources
- Limited data on Southeast Asian and Latin American CDP adoption

---

## Phase 3: Analysis Summary

### Market Sizing (Top-Down)

| Metric | Value | Source | Confidence |
|--------|-------|--------|------------|
| Global CDP market (2025) | $5.2B | Gartner, IDC average | High |
| Growth rate (CAGR 2025-2030) | 24.3% | Analyst consensus | Medium-High |
| Mid-market segment share | 28-35% | Estimated from vendor revenue mix | Medium |
| **TAM (mid-market CDP)** | **$1.5-1.8B** | Calculated | Medium |

### Market Sizing (Bottom-Up)

| Metric | Value | Methodology |
|--------|-------|-------------|
| Addressable companies ($10M-$500M ARR) | ~180,000 globally | Company database cross-reference |
| CDP adoption rate in segment | 12-18% | Customer review platform data |
| Average contract value | $45K-$85K/year | Pricing page and review data |
| **TAM (bottom-up)** | **$1.2-2.0B** | Calculated |

**Reconciled estimate:** $1.4-1.8B TAM, $400-550M SAM (addressable with mid-market product), $40-80M realistic SOM (year 3).

### Competitive Landscape (Top 8)

| Competitor | Est. Revenue | Mid-Market Focus | Key Strength |
|-----------|-------------|------------------|-------------|
| Segment (Twilio) | ~$400M | Medium (moving upmarket) | Data infrastructure depth |
| mParticle | ~$80M | High | Mobile-first, real-time |
| Rudderstack | ~$40M | High | Open-source, developer-friendly |
| Lytics | ~$25M | High | ML-driven personalization |
| Bloomreach | ~$150M | Medium | Commerce-specific |
| Tealium | ~$120M | Medium | Tag management heritage |
| Treasure Data | ~$100M | Low (enterprise) | Data lake integration |
| ActionIQ | ~$50M | Low (enterprise) | Enterprise analytics |

---

## Phase 4: Synthesis (Deliverables Produced)

The Synthesizer produced:

1. **Executive Summary** (400 words) -- Key market opportunity, competitive dynamics, and entry recommendation
2. **Market Analysis Report** (3,200 words) -- Full market sizing, competitive profiles, trend analysis
3. **TAM/SAM/SOM Model** -- Dual-approach with reconciliation and sensitivity tables
4. **Competitive Landscape Map** -- Positioning matrix (mid-market focus vs product breadth)
5. **Trend Scenarios** -- 3 scenarios for CDP market evolution (consolidation, fragmentation, platform absorption)

### Key Recommendations (Evidence-Mapped)

1. **Target the open-source-friendly mid-market segment** -- Rudderstack's growth validates developer-led adoption, and the mid-market segment is underserved by enterprise vendors moving upmarket (findings 3, 4, 6).
2. **Price at $40-60K/year for the core product** -- Competitive pricing data shows mid-market sweet spot, with expansion revenue from usage-based components (finding 5).
3. **Differentiate on data governance and privacy** -- Trend analysis shows GDPR/CCPA compliance becoming a primary buying criterion, and no current mid-market CDP leads on this dimension (finding 6).

---

## Cost Breakdown

| Phase | Tokens Used | Cost |
|-------|-----------|------|
| Study Design | 35K | $5.25 |
| Data Collection | 105K | $6.30 |
| Analysis | 88K | $5.28 |
| Synthesis | 72K | $5.55 |
| Deliverables | 45K | $3.50 |
| **Total** | **345K** | **~$34** |

---

## Lessons Learned

1. **Mid-market segment data is scarce.** Most industry reports cover total market. The bottom-up approach was essential for mid-market-specific sizing.
2. **Private company revenue estimates need multiple sources.** Single-source estimates varied by 30-50%. Cross-referencing reduced uncertainty.
3. **Job postings are valuable competitive intelligence.** Hiring patterns revealed product direction better than press releases.
4. **The Trend Forecaster added significant value.** Platform absorption scenario (CDPs being absorbed into cloud platform suites) was a critical strategic consideration.
