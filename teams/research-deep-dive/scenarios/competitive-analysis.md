# Scenario: Competitive Analysis

This scenario defines the end-to-end flow for conducting a comprehensive competitive landscape analysis, including competitor profiling, feature comparison, positioning assessment, and strategic recommendations.

---

## Scenario Overview

| Property | Value |
|----------|-------|
| **Priority** | High |
| **Research Mode** | Market/Competitive |
| **Validated After** | Phase 5 |
| **Primary Agents** | Core team + Competitive Intelligence, Market Sizing Analyst, Trend Forecaster |
| **Estimated Duration** | ~60-90 minutes (hybrid mode) |
| **Estimated Cost** | ~$25-40 (default config) |

---

## Success Path: Competitive Landscape for Market Entry Decision

### Preconditions

- Research question specifies the competitive space to analyze
- Market mode is enabled with `include_competitive_landscape: true`
- At least 3-5 known competitors are identified in the brief (or discovery is requested)
- Web search API key is set and has available quota

### Steps

| Step | Agent | Action | Expected Outcome |
|------|-------|--------|------------------|
| 1 | Coordinator | Design competitive analysis protocol: define dimensions (features, pricing, positioning, strategy, strengths, weaknesses), comparison framework | Study protocol with analysis dimensions and competitor shortlist |
| 2 | Primary Researcher | Gather public intelligence: company pages, press releases, reviews, job postings, tech stack signals | Source database with multi-angle data on each competitor |
| 3 | Competitive Intelligence | Build competitor profiles: company overview, product capabilities, pricing, target market, funding, team size | Structured profiles for each competitor |
| 4 | Competitive Intelligence | Create feature comparison matrix across all competitors | Quantitative and qualitative feature comparison |
| 5 | Analyst | Analyze competitive positioning: market share estimates, growth trajectories, strategic patterns | Positioning analysis with data-backed assessments |
| 6 | Trend Forecaster | Predict competitive moves: likely expansions, pivots, vulnerabilities | Scenario analysis of competitive dynamics |
| 7 | Synthesizer | Draft competitive landscape report with positioning map and strategic recommendations | Complete report with executive briefing |
| 8 | Coordinator | Review for completeness: all competitors covered, analysis dimensions addressed, recommendations actionable | GO decision with quality metrics |

### Validation Criteria

- [ ] All identified competitors are profiled with consistent data dimensions
- [ ] Feature comparison uses consistent scoring or rating methodology
- [ ] Pricing data is current (within 6 months) or dated explicitly
- [ ] Competitive moats and vulnerabilities are identified for each competitor
- [ ] Strategic recommendations map to specific competitive insights
- [ ] Positioning map shows clear differentiation or overlap
- [ ] Data sources include multiple independent sources per competitor
- [ ] Job postings and hiring patterns are analyzed as strategy signals
- [ ] Customer sentiment is captured from review sites and social channels

---

## Edge Case: Competitor Information Is Limited (Private Companies)

### Preconditions

- Key competitors are private companies with limited public financial data
- Revenue estimates and market share cannot be directly verified

### Steps

| Step | Agent | Action | Expected Outcome |
|------|-------|--------|------------------|
| 1 | Primary Researcher | Searches for proxy indicators: employee count (LinkedIn), web traffic (SimilarWeb), funding rounds, customer testimonials | Proxy data with confidence ratings |
| 2 | Competitive Intelligence | Estimates revenue using proxies: employee count x revenue-per-employee benchmarks, funding round valuations | Revenue estimates with methodology and uncertainty range |
| 3 | Analyst | Validates estimates by cross-referencing multiple proxy methods | Reconciled estimate with confidence interval |
| 4 | Synthesizer | Clearly labels estimates as proxy-based, not verified financial data | Report distinguishes verified vs estimated data points |

### Validation Criteria

- [ ] Proxy methodology is documented and defensible
- [ ] Multiple proxy methods are used and reconciled
- [ ] Estimates include confidence intervals
- [ ] Report clearly labels which data is verified vs estimated

---

## Edge Case: Rapidly Changing Competitive Landscape

### Preconditions

- Competitors are launching new products or making acquisitions during the research period
- Data collected early in the study may be outdated by synthesis phase

### Steps

| Step | Agent | Action | Expected Outcome |
|------|-------|--------|------------------|
| 1 | Primary Researcher | Flags recent competitive developments found during source discovery | List of recent changes with dates |
| 2 | Coordinator | Decides whether to update analysis or note changes as caveats | Updated protocol or documented caveats |
| 3 | Trend Forecaster | Incorporates recent moves into scenario analysis | Updated scenarios reflecting new competitive dynamics |
| 4 | Synthesizer | Includes "as of [date]" timestamps on competitive data | Report with clear temporal context |

### Validation Criteria

- [ ] Report includes "as of" date for all competitive data
- [ ] Recent competitive moves are noted even if analysis could not be updated
- [ ] Trend scenarios account for the most recent developments
- [ ] Recommendations acknowledge the dynamic nature of the landscape

---

## Agents Responsible

| Agent | Responsibility |
|-------|---------------|
| **Coordinator** | Analysis protocol design, dimension definition, quality review |
| **Primary Researcher** | Multi-source data gathering for each competitor |
| **Competitive Intelligence** | Competitor profiling, feature comparison, strategy assessment |
| **Market Sizing Analyst** | Market share estimation and competitive positioning quantification |
| **Analyst** | Cross-competitor statistical analysis and proxy validation |
| **Trend Forecaster** | Competitive dynamics prediction and scenario modeling |
| **Synthesizer** | Landscape report, positioning map, executive briefing |
