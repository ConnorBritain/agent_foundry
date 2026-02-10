# Scenario: Creating a Comprehensive Industry Report

This scenario defines the end-to-end flow for producing a comprehensive industry report suitable for internal strategy, investor communications, or publication. The report covers market dynamics, competitive structure, value chain analysis, regulatory environment, and future outlook.

---

## Scenario Overview

| Property | Value |
|----------|-------|
| **Priority** | High |
| **Research Mode** | Market |
| **Validated After** | Phase 4 |
| **Primary Agents** | Lead Researcher, Source Analyst, Data Synthesizer, Fact Checker, Report Writer |
| **Estimated Duration** | ~120-180 minutes (hybrid mode) |
| **Estimated Cost** | ~$35-60 (default config) |

---

## Context

A strategy team, investor relations group, or research division needs a comprehensive industry report that provides a 360-degree view of an industry. This is the most extensive research scenario -- it covers market sizing, competitive dynamics, value chain analysis, regulatory landscape, technology trends, and future scenarios. The output should be publication-quality and suitable for board presentations, investor decks, or thought leadership.

## Trigger

User provides an industry report brief specifying:
- The industry to analyze and its boundaries
- Geographic scope (global, regional, or country-specific)
- Target audience (internal strategy, investors, customers, public)
- Time horizon for forward-looking analysis (1-3 years, 3-5 years, 5-10 years)
- Specific themes or questions to emphasize
- Depth requirements (overview vs comprehensive)

---

## Team Configuration

| Agent | Role in This Scenario |
|-------|----------------------|
| Lead Researcher | Defines the report structure, decomposes into research streams, ensures comprehensive coverage across all industry dimensions |
| Source Analyst | Conducts deep source discovery across industry reports, government data, academic research, financial filings, and news |
| Data Synthesizer | Integrates market data, builds value chain models, constructs future scenarios, creates visualization specifications |
| Fact Checker | Verifies all market statistics, growth projections, regulatory citations, and company-specific claims |
| Report Writer | Produces the publication-quality industry report, executive summary, and presentation deck |

---

## Workflow

### Phase 1: Research Design (~20 min)
- Lead Researcher defines the industry boundaries and scope
- Decomposes the report into research streams:
  - Market size and growth dynamics (historical and projected)
  - Industry structure and competitive forces (Porter's Five Forces or equivalent)
  - Value chain analysis (from inputs to end customer)
  - Key players and competitive positioning
  - Regulatory and macro environment
  - Technology trends affecting the industry
  - Future outlook and scenario analysis
- Identifies required data sources per stream
- Establishes quality criteria: all market figures require 2+ independent sources

### Phase 2: Data Collection (~40-60 min)
- Source Analyst executes systematic search across all research streams
- Gathers historical market data from industry databases and government statistics
- Collects competitive data: market shares, revenue figures, strategic moves
- Identifies regulatory frameworks, recent policy changes, and pending legislation
- Discovers technology trends affecting the industry's future
- Documents all sources with credibility assessments
- Flags data gaps and areas where estimates must substitute for hard data

### Phase 3: Analysis and Synthesis (~30-40 min)
- Lead Researcher integrates findings across all research streams
- Data Synthesizer builds market sizing model with growth drivers and inhibitors
- Data Synthesizer maps the value chain with margin distribution and power dynamics
- Data Synthesizer constructs competitive positioning analysis
- Data Synthesizer develops 2-3 future scenarios (base case, optimistic, pessimistic) with probability estimates
- Data Synthesizer creates visualization specifications for key data points
- Fact Checker verifies all quantitative claims, especially growth projections and market share figures

### Phase 4: Deliverable Production (~30-40 min)
- Report Writer produces the comprehensive industry report (20-35 pages)
- Report Writer creates executive summary (3-5 pages) suitable for standalone distribution
- Report Writer develops presentation-format briefing for board or investor use
- Report Writer integrates all visualizations and data tables
- Lead Researcher reviews for comprehensiveness, analytical rigor, and narrative coherence
- Coordinator performs final quality gate

---

## Expected Outputs

| Deliverable | Format | Description |
|------------|--------|-------------|
| Industry report | Markdown (20-35 pages) | Comprehensive report: market overview, competitive structure, value chain, regulation, outlook |
| Executive summary | Markdown (3-5 pages) | Standalone summary with key metrics, trends, and strategic implications |
| Presentation briefing | Markdown (slide-style) | Board-ready presentation with one insight per section and speaker notes |
| Market sizing model | Markdown with tables | Historical and projected market size with documented methodology and assumptions |
| Scenario analysis | Markdown | 2-3 future scenarios with probability estimates and strategic implications |
| Competitive landscape | Markdown with tables | Market shares, positioning map, strategic group analysis |
| Source database | Markdown table | Complete source list with credibility assessments |
| Methodology notes | Markdown | Research methodology documentation for reproducibility |

---

## Estimated Cost

| Phase | Agent(s) | Est. Tokens | Est. Cost |
|-------|----------|------------|-----------|
| Research Design | Lead Researcher | ~40K | ~$6.00 |
| Data Collection | Source Analyst | ~120K | ~$7.20 |
| Analysis & Synthesis | Lead Researcher + Data Synthesizer + Fact Checker | ~140K | ~$9.00 |
| Deliverable Production | Report Writer + Lead Researcher | ~100K | ~$6.50 |
| **Total** | | **~400K** | **~$29-50** |

Note: Industry reports are the most token-intensive scenario due to breadth of coverage. Budget an additional 20% for iterations and emerging sub-questions.

---

## Edge Case: Fragmented Industry with No Dominant Data Source

When the industry lacks a single authoritative data source (e.g., no Gartner Magic Quadrant, no IBISWorld report):
- Source Analyst uses triangulation: combine government statistics, trade association data, and company filings
- Data Synthesizer builds bottom-up market sizing from individual company revenue data where available
- Report Writer documents the data fragmentation as a key limitation
- Lead Researcher adjusts confidence levels to reflect data quality constraints

## Edge Case: Cross-Industry Convergence

When the industry boundaries are blurring due to technology or market convergence:
- Lead Researcher explicitly defines what is in-scope and out-of-scope with justification
- Source Analyst researches adjacent industries that are converging with the target
- Data Synthesizer includes a section on convergence dynamics and their implications
- Report Writer frames the analysis with clear scope boundaries while acknowledging convergence

---

## Validation Criteria

- [ ] Market size figures are supported by 2+ independent sources with reconciliation of discrepancies
- [ ] Competitive analysis covers the top players representing 60%+ of market share
- [ ] Value chain analysis identifies where value is created and where margins are concentrated
- [ ] Regulatory section covers current requirements and pending changes
- [ ] Future scenarios are grounded in identified trends, not speculation
- [ ] All growth projections cite sources and document assumptions
- [ ] Report is suitable for the specified audience (internal strategy, investors, or publication)
- [ ] Executive summary stands alone without requiring the full report
- [ ] Limitations are documented: data availability, estimation methodology, forecast uncertainty
