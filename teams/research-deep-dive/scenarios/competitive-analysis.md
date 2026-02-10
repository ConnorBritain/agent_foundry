# Scenario: Deep Competitive Analysis of 5+ Competitors

This scenario defines the end-to-end flow for conducting a thorough competitive analysis covering product capabilities, pricing, market positioning, strengths, weaknesses, and strategic trajectories for five or more competitors.

---

## Scenario Overview

| Property | Value |
|----------|-------|
| **Priority** | High |
| **Research Mode** | Competitive |
| **Validated After** | Phase 4 |
| **Primary Agents** | Lead Researcher, Source Analyst, Data Synthesizer, Fact Checker, Report Writer |
| **Estimated Duration** | ~60-90 minutes (hybrid mode) |
| **Estimated Cost** | ~$20-35 (default config) |

---

## Context

A product or strategy team needs a comprehensive understanding of the competitive landscape. This is not a surface-level feature comparison -- it is a deep analysis of each competitor's strategy, capabilities, market positioning, customer sentiment, and likely future moves. The output must be actionable: it should reveal strategic gaps the company can exploit and threats it must defend against.

## Trigger

User provides a competitive analysis brief specifying:
- The company's own product and positioning
- A list of 5+ known competitors (or a request to identify them)
- Specific dimensions to compare (features, pricing, market share, funding, team)
- The strategic decision this analysis will inform
- Any competitors that are particularly important to analyze deeply

---

## Team Configuration

| Agent | Role in This Scenario |
|-------|----------------------|
| Lead Researcher | Defines the competitive analysis framework, assigns per-competitor research streams, synthesizes cross-competitor patterns |
| Source Analyst | Researches each competitor: product pages, pricing, G2/Capterra reviews, Crunchbase funding, LinkedIn team data, press coverage, financial filings |
| Data Synthesizer | Builds comparison matrices, identifies competitive clusters, maps positioning, detects strategic patterns |
| Fact Checker | Verifies pricing claims, funding amounts, feature availability, and market share figures |
| Report Writer | Produces competitor profiles, comparison tables, positioning analysis, and strategic recommendations |

---

## Workflow

### Phase 1: Research Design (~10 min)
- Lead Researcher defines the evaluation framework: dimensions, scoring criteria, data requirements
- Establishes consistent criteria applied to every competitor (avoid comparing apples to oranges)
- Defines data sources per dimension: product pages for features, Crunchbase for funding, G2 for sentiment
- Prioritizes which competitors get the deepest analysis based on strategic relevance

### Phase 2: Data Collection (~25-35 min)
- Source Analyst researches each competitor systematically using the evaluation framework
- Collects data across consistent dimensions: product features, pricing tiers, target segments, funding history, team size, recent announcements
- Gathers customer sentiment: G2 reviews, Capterra ratings, Reddit discussions, Twitter sentiment
- Documents what could not be found (pricing hidden behind sales calls, private company financials)
- Traces all claims to primary sources (product pages, SEC filings, official announcements)

### Phase 3: Analysis and Synthesis (~20-25 min)
- Lead Researcher integrates per-competitor findings into cross-competitor analysis
- Data Synthesizer builds multi-dimensional comparison matrices
- Data Synthesizer identifies competitive clusters (who competes with whom most directly)
- Data Synthesizer maps positioning: price vs feature richness, enterprise vs SMB focus, horizontal vs vertical
- Data Synthesizer identifies strategic gaps: underserved segments, missing features, pricing opportunities
- Fact Checker verifies all comparative claims and quantitative figures

### Phase 4: Deliverable Production (~15-20 min)
- Report Writer produces individual competitor profiles (1-2 pages each)
- Report Writer creates comparison matrices across all evaluation dimensions
- Report Writer writes positioning analysis with strategic implications
- Report Writer produces executive briefing with top competitive threats and opportunities
- Lead Researcher reviews for analytical rigor and actionability

---

## Expected Outputs

| Deliverable | Format | Description |
|------------|--------|-------------|
| Competitor profiles | Markdown (1-2 pages per competitor) | Individual deep-dives: product, pricing, positioning, strengths, weaknesses, strategy |
| Comparison matrix | Markdown tables | Feature-by-feature, pricing, and capability comparison across all competitors |
| Positioning analysis | Markdown with diagrams | Market positioning map, competitive clusters, strategic gap analysis |
| Executive briefing | Markdown (2-3 pages) | Top threats, opportunities, and recommended strategic responses |
| Source database | Markdown table | All sources per competitor with credibility tiers and access dates |

---

## Estimated Cost

| Phase | Agent(s) | Est. Tokens | Est. Cost |
|-------|----------|------------|-----------|
| Research Design | Lead Researcher | ~20K | ~$3.00 |
| Data Collection | Source Analyst | ~100K | ~$6.00 |
| Analysis & Synthesis | Lead Researcher + Data Synthesizer + Fact Checker | ~80K | ~$5.00 |
| Deliverable Production | Report Writer | ~60K | ~$3.60 |
| **Total** | | **~260K** | **~$18-30** |

Note: Cost scales with the number of competitors. Each additional competitor beyond 5 adds approximately $2-3 to the total cost.

---

## Edge Case: Private Companies with Limited Data

When key competitors are private companies with limited public financial data:
- Source Analyst searches for proxy indicators: employee count (LinkedIn), web traffic estimates, funding rounds, customer testimonials
- Data Synthesizer estimates revenue using proxies: employee count x revenue-per-employee benchmarks
- Fact Checker validates estimates by cross-referencing multiple proxy methods
- Report Writer clearly labels estimates as proxy-based, not verified financial data, and includes confidence intervals

## Edge Case: Rapidly Changing Competitive Landscape

When competitors are launching new products or making acquisitions during the research:
- Source Analyst flags recent competitive developments found during collection
- Lead Researcher decides whether to update analysis or note changes as caveats
- Report Writer includes "as of [date]" timestamps on all competitive data
- All deliverables acknowledge the dynamic nature of the landscape

---

## Validation Criteria

- [ ] Every competitor is evaluated against the same framework and dimensions
- [ ] Pricing data cites specific sources (product pages, published pricing, analyst reports)
- [ ] Feature comparisons reflect current product state, not roadmap promises
- [ ] Customer sentiment is based on actual reviews, not marketing claims
- [ ] Strategic gaps are supported by evidence, not assumptions
- [ ] Limitations are documented (hidden pricing, private companies, outdated data)
- [ ] Recommendations are specific and tied to identified competitive gaps
