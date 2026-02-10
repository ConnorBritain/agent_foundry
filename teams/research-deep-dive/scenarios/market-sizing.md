# Scenario: Market Sizing Study

This scenario defines the end-to-end flow for conducting a TAM/SAM/SOM market sizing analysis with defensible assumptions, dual-approach methodology, and sensitivity analysis.

---

## Scenario Overview

| Property | Value |
|----------|-------|
| **Priority** | Critical |
| **Research Mode** | Market/Competitive |
| **Validated After** | Phase 5 |
| **Primary Agents** | Core team + Market Sizing Analyst, Competitive Intelligence, Trend Forecaster |
| **Estimated Duration** | ~90-120 minutes (hybrid mode) |
| **Estimated Cost** | ~$30-45 (default config) |

---

## Success Path: TAM/SAM/SOM for a New Market Entry

### Preconditions

- Research question specifies the market to size and the product/service category
- Market mode is enabled with `include_tam_sam_som: true`
- Geographic scope and customer segments are defined in CONFIG
- Web search API key is set and has available quota

### Steps

| Step | Agent | Action | Expected Outcome |
|------|-------|--------|------------------|
| 1 | Coordinator | Design market sizing protocol: define market boundaries, methodology (top-down + bottom-up), data sources | Study protocol with clear market definition and dual-approach plan |
| 2 | Primary Researcher | Gather market data: industry reports, financial filings, government data, analyst estimates | Source database with 15-25 market data sources, credibility-assessed |
| 3 | Competitive Intelligence | Research competitors: pricing, revenue estimates, market share, customer counts | Competitor database with quantitative metrics |
| 4 | Market Sizing Analyst | Build top-down model: total market value from macro data | Top-down TAM/SAM/SOM with documented assumptions |
| 5 | Market Sizing Analyst | Build bottom-up model: aggregate from customer segments and unit economics | Bottom-up TAM/SAM/SOM with documented assumptions |
| 6 | Analyst | Reconcile models, run sensitivity analysis | Reconciled estimate with confidence range and sensitivity tables |
| 7 | Trend Forecaster | Model growth scenarios: base, optimistic, pessimistic | 3-5 year projections with probability-weighted scenarios |
| 8 | Synthesizer | Draft market analysis report with executive summary | Complete report with all models, assumptions, and recommendations |
| 9 | Coordinator | Review for rigor: assumptions documented, models reconciled, sources credible | GO decision with quality metrics |

### Validation Criteria

- [ ] Market boundaries are clearly defined (what is in, what is out)
- [ ] Both top-down and bottom-up approaches are used and reconciled
- [ ] Every assumption is documented with source and rationale
- [ ] Sensitivity analysis shows impact of key assumption changes
- [ ] Growth projections include multiple scenarios with probability estimates
- [ ] All market data cites primary sources (industry reports, filings, government data)
- [ ] Competitive landscape is quantified (revenue, market share, pricing)
- [ ] TAM > SAM > SOM relationship is logical and defensible
- [ ] Executive summary communicates the key number with confidence range

---

## Edge Case: Top-Down and Bottom-Up Models Diverge Significantly

### Preconditions

- Top-down model estimates TAM at $12B, bottom-up model estimates $4.5B
- Divergence exceeds 50%

### Steps

| Step | Agent | Action | Expected Outcome |
|------|-------|--------|------------------|
| 1 | Analyst | Identifies divergence and diagnoses root cause | Report on which assumptions differ between models |
| 2 | Market Sizing Analyst | Tests whether adjusting specific assumptions brings models closer | Sensitivity analysis on divergence-causing assumptions |
| 3 | Coordinator | Escalates to user: "Models diverge by 63%. Key differences are [list]." | User provides domain input or accepts range |
| 4 | Synthesizer | Presents both models with honest assessment of which is more reliable | Report clearly states the range and why models differ |

### Validation Criteria

- [ ] Divergence is diagnosed (which assumptions differ)
- [ ] User is informed of the divergence before deliverables are finalized
- [ ] Final report presents a range rather than a false point estimate
- [ ] The more reliable model is identified with justification

---

## Edge Case: Limited Market Data Available

### Preconditions

- Market is nascent or niche with limited published data
- Fewer than 5 credible market data sources found

### Steps

| Step | Agent | Action | Expected Outcome |
|------|-------|--------|------------------|
| 1 | Primary Researcher | Documents data gaps explicitly in the source database | Gap analysis identifies what data is missing |
| 2 | Coordinator | Adjusts methodology: proxy markets, analogous industries, expert triangulation | Revised protocol using alternative estimation methods |
| 3 | Market Sizing Analyst | Builds model using proxies and analogies with wider confidence intervals | Market size estimate with clearly stated proxy assumptions |
| 4 | Synthesizer | Frames findings with appropriate uncertainty language | Report clearly distinguishes data-driven estimates from proxy-based estimates |

### Validation Criteria

- [ ] Data limitations are documented before analysis begins
- [ ] Proxy markets and analogies are justified (why they are comparable)
- [ ] Confidence intervals are wider to reflect data uncertainty
- [ ] Report explicitly states which estimates are data-driven vs proxy-based

---

## Agents Responsible

| Agent | Responsibility |
|-------|---------------|
| **Coordinator** | Market sizing protocol design, model reconciliation oversight, quality review |
| **Primary Researcher** | Market data collection from industry reports, filings, and government sources |
| **Competitive Intelligence** | Competitor research: revenue, pricing, market share |
| **Market Sizing Analyst** | TAM/SAM/SOM model construction (top-down and bottom-up) |
| **Analyst** | Model reconciliation, sensitivity analysis, statistical validation |
| **Trend Forecaster** | Growth projections and scenario modeling |
| **Synthesizer** | Market analysis report and executive summary |
