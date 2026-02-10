# Research Deep Dive Team -- Technical Specification

## Overview

This document defines the architecture, agent composition, responsibilities, deliverables, and quality standards for the Research Deep Dive Team. The team is designed to conduct rigorous, well-sourced research across academic, market, competitive, and product domains with configurable depth and methodology. It adapts its composition based on research type, activating specialized agents only when their domain is relevant.

---

## 1. Team Composition

The team consists of 4 core agents that are always active, plus mode-specific specialist agents that activate based on the research type. The Coordinator operates on Opus 4.6 for research design and quality judgment. Core researchers operate on Sonnet 4.5 for deep analytical work. Specialist agents use Sonnet 4.5 or Haiku 4.5 depending on task complexity.

### 1.1 Coordinator / Research Lead

- **Model:** Opus 4.6
- **Token budget:** 40-80K tokens (varies by mode)
- **Primary responsibilities:**
  - Clarify the research question and define the study protocol
  - Configure the team based on research_type and domain
  - Design methodology: data sources, analysis plan, quality criteria
  - Coordinate agent assignments and manage dependencies
  - Review all outputs for rigor, consistency, and completeness
  - Ensure the final deliverable tells a coherent, evidence-supported story
  - Manage scope and prevent research from expanding indefinitely
- **Decision authority:**
  - FINAL say on methodology, scope, and deliverable structure
  - Can expand search to additional databases autonomously (cost < $15)
  - Can request deeper analysis on emerging themes
  - Escalates to user for: scope changes, methodology changes, inconclusive results
- **Outputs:**
  - Study protocol (research question, methodology, data sources, timeline)
  - Phase gate reports at each transition
  - Final synthesis review with coherence and rigor assessment

### 1.2 Primary Researcher (Literature Review Specialist)

- **Model:** Sonnet 4.5
- **Token budget:** 60-100K tokens
- **Primary responsibilities:**
  - Discover sources across multiple databases and search engines
  - Follow citation chains to find foundational and related works
  - Evaluate source quality, recency, and relevance
  - Identify consensus findings vs contested claims
  - Organize literature thematically, not just chronologically
  - Flag research gaps where existing literature is insufficient
  - Detect potential conflicts of interest and funding bias
- **Research standards:**
  - Uses multiple databases and follows citation chains
  - Assesses methodology, sample size, and peer review status of sources
  - Prioritizes recent sources but includes foundational works
  - Groups findings by theme, not just date or author
  - Documents what the literature does NOT address
- **Outputs:**
  - Source database with credibility assessments
  - Thematic literature summary
  - Research gap analysis
  - Citation chain map

### 1.3 Analyst (Data Analyst)

- **Model:** Sonnet 4.5
- **Token budget:** 60-100K tokens
- **Primary responsibilities:**
  - Perform statistical analysis appropriate to the data type
  - Check assumptions before applying statistical tests
  - Create visualizations that communicate findings clearly
  - Report confidence intervals and effect sizes, not just p-values
  - Flag insufficient sample sizes and methodological limitations
  - Make data accessible to non-technical stakeholders
  - Document methods for reproducibility
- **Analysis standards:**
  - Validates prerequisites before analysis
  - Acknowledges limitations and uncertainty in all findings
  - Uses appropriate statistical tests for the data type
  - Explains findings without unnecessary jargon
  - Documents methods so analysis can be repeated
- **Outputs:**
  - Statistical analysis report with methodology documentation
  - Data visualizations (charts, tables, graphs)
  - Interpretation narrative connecting data to research question
  - Confidence assessments for all quantitative findings

### 1.4 Synthesizer (Synthesis Writer)

- **Model:** Sonnet 4.5
- **Token budget:** 60-100K tokens
- **Primary responsibilities:**
  - Transform raw findings into compelling, well-structured written deliverables
  - Write for the target audience (academic for journals, executive for boardrooms, technical for product teams)
  - Maintain the distinction between what the data shows and what it suggests
  - Create clear logical flow from evidence to conclusion
  - Ensure recommendations follow directly from presented evidence
  - Produce mode-specific deliverables (papers, reports, briefings)
- **Writing standards:**
  - Audience-adaptive: writes differently for academics, executives, and practitioners
  - Evidence-faithful: never overstates what the data supports
  - Narrative-focused: creates a coherent story from disparate findings
  - Structure-clear: logical flow with clear sections and easy navigation
  - Conclusion-grounded: recommendations follow directly from evidence
- **Outputs:**
  - Primary research deliverable (paper, report, briefing)
  - Executive summary
  - Recommendations with evidence mapping

---

## 2. Mode-Specific Agents

### 2.1 Academic Mode Agents

| Agent | Model | Token Budget | Role |
|-------|-------|-------------|------|
| Methodology Designer | Opus 4.6 | 80K | Experimental design, statistical power analysis, validity assessment |
| Citation Manager | Haiku 4.5 | 20K | Bibliography formatting (APA/MLA/Chicago/Vancouver/Harvard), reference deduplication |
| Peer Reviewer | Sonnet 4.5 | 60K | Methodology critique, validity assessment, rigor check |
| Grant Writer (optional) | Sonnet 4.5 | 60K | Translate research into funding proposals |

### 2.2 Market/Competitive Mode Agents

| Agent | Model | Token Budget | Role |
|-------|-------|-------------|------|
| Market Sizing Analyst | Sonnet 4.5 | 60K | TAM/SAM/SOM calculations, growth projections, sensitivity analysis |
| Competitive Intelligence | Sonnet 4.5 | 60K | Competitor analysis, feature comparison, pricing intel, strategy assessment |
| Customer Interview Analyzer | Sonnet 4.5 | 50K | Qualitative data coding, theme extraction, voice-of-customer synthesis |
| Trend Forecaster | Sonnet 4.5 | 50K | Pattern identification, scenario modeling, trend vs fad distinction |

### 2.3 Product/UX Mode Agents

| Agent | Model | Token Budget | Role |
|-------|-------|-------------|------|
| User Behavior Analyst | Sonnet 4.5 | 50K | Analytics interpretation, funnel analysis, cohort segmentation |
| Usability Evaluator | Sonnet 4.5 | 50K | Heuristic evaluation, friction identification, severity ranking |
| Feature Prioritizer | Sonnet 4.5 | 50K | RICE scoring, opportunity assessment, trade-off analysis |

### 2.4 Agent Counts by Mode

- Core only (Literature Review): 4 agents
- Academic: 4 core + 3-4 academic = 7-8 agents
- Market/Competitive: 4 core + 3-4 market = 7-8 agents
- Product/UX: 4 core + 3 product = 7 agents
- Mixed: 4 core + selected specialists from multiple modes

---

## 3. Research Pipeline Specification

### 3.1 Input Requirements

| Input | Required | Description |
|-------|----------|-------------|
| Research question | Yes | Primary question to investigate |
| Research type | Yes | academic, market, competitive, product_ux, literature_review, mixed |
| Domain | Yes | healthcare, finance, technology, education, climate, social_science, other |
| Constraints | Recommended | Timeline, budget, data access level |
| Mode-specific config | Conditional | Academic settings, market definition, product stage |
| Existing data | Optional | Interview transcripts, analytics exports, prior research |

### 3.2 Output Artifacts by Mode

#### Academic Mode

| Artifact | Format | Description |
|----------|--------|-------------|
| Research Paper | LaTeX or Word | Complete paper: abstract, introduction, methods, results, discussion, conclusion |
| Bibliography | Target citation style | Properly formatted, deduplicated, complete reference list |
| Data & Code Repository | GitHub repo structure | Raw data, analysis scripts, README for reproducibility |
| Supplementary Materials | PDF/Word | Additional tables, figures, analysis details |
| Grant Proposal (optional) | Funder-specific format | Significance, innovation, approach, budget, timeline |

#### Market/Competitive Mode

| Artifact | Format | Description |
|----------|--------|-------------|
| Market Analysis Report | Markdown/Notion | Comprehensive market overview with sourced data |
| Competitive Landscape Map | Visual (Mermaid/diagram) | Positioning map, feature comparison, pricing matrix |
| TAM/SAM/SOM Model | Spreadsheet format | Dual-approach sizing with documented assumptions |
| Executive Briefing | Slide-style document | Key findings, recommendations, next steps |
| Trend Scenarios | Document | Multiple future scenarios with probability estimates |

#### Product/UX Mode

| Artifact | Format | Description |
|----------|--------|-------------|
| Research Findings Report | Markdown/Notion | User behavior analysis, usability findings, recommendations |
| Prioritized Feature Backlog | Ranked list with scores | Features scored by RICE, ready for sprint planning |
| Usability Issue Tracker | Severity-ranked list | Issues by severity with fix recommendations |
| Analytics Dashboard Design | Document | Metrics to track, visualizations to build, thresholds |
| Experiment Proposals | Document | A/B tests to validate key hypotheses |

---

## 4. Token Budget

### 4.1 Budget by Mode

| Mode | Total Tokens | Est. Cost | Duration |
|------|-------------|-----------|----------|
| Literature Review | ~250K | $12-20 | 1-2 hours |
| Academic (full) | ~440K | $35-60 | 2-3 hours |
| Market/Competitive | ~340K | $25-45 | 1-2 hours |
| Product/UX | ~280K | $18-30 | 45-90 min |

### 4.2 Budget by Phase (Market/Competitive Mode Example)

| Phase | Duration | Agents | Tokens | Cost |
|-------|----------|--------|--------|------|
| Study Design | ~10-20 min | 1-2 | 40-80K | $6-12 |
| Data Collection | ~20-40 min | 3-4 parallel | 120K | $7-10 |
| Analysis | ~15-30 min | 2-3 parallel | 100K | $6-8 |
| Synthesis | ~15-25 min | 2 sequential | 80K | $5-8 |
| **Total** | **~60-115 min** | | **~340K** | **~$25-45** |

Note: A 20% buffer is recommended for all modes. Research often uncovers sub-questions requiring additional investigation.

---

## 5. Quality Standards

### 5.1 Source Quality

- Target: >80% of sources are peer-reviewed or primary
- Measured by: Source audit in the Primary Researcher's output
- Blocking: research with <50% credible sources is rejected

### 5.2 Methodology Rigor

- Target: methodology appropriate for the research question
- Measured by: Peer review or Coordinator self-assessment
- Blocking: methodology mismatch triggers study redesign

### 5.3 Citation Completeness

- Target: 100% of factual claims have citations
- Measured by: Citation audit
- Blocking: unsourced factual claims are either cited, hedged, or removed

### 5.4 Conclusion Support

- Target: all conclusions follow directly from presented evidence
- Measured by: Logical review by Coordinator
- Blocking: unsupported conclusions are either supported with evidence or removed

### 5.5 Deliverable Completeness

- Target: all expected artifacts for the configured mode are produced
- Measured by: Artifact checklist
- Blocking: missing required artifacts halt delivery

### 5.6 Budget Adherence

- Target: actual cost within 20% of estimated cost
- Measured by: Token usage tracking per agent
