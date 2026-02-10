# Research Deep Dive Team -- Full Specification

> **STATUS: STATIC REFERENCE** -- This file is never modified, only consulted.

## Use Case

Comprehensive research across academic, market, product, and competitive domains with configurable depth and methodology. This team adapts its composition based on the research type -- activating specialized agents only when their domain is relevant. It produces rigorous, well-sourced research deliverables appropriate to the research mode.

**Target Users**: Researchers, product managers, strategists, analysts, academics, founders evaluating markets.

**When to Use This Team vs. Single Agent**:
- Research requires systematic methodology (not just "search and summarize")
- Multiple data sources need to be triangulated
- Output must meet academic, professional, or executive standards
- Research spans multiple sub-questions requiring parallel investigation
- Deliverables require structured formats (papers, reports, spreadsheets, presentations)

**Inputs**: Research question, domain, constraints (timeline, budget, data access), mode-specific configuration.
**Outputs**: Mode-dependent deliverables (see Output Artifacts by Mode section).

---

## Agent Roster

### Core Team (Always Active)

| Agent | Model | Count | Role | Token Budget (varies by mode) |
|-------|-------|-------|------|-------------------------------|
| Coordinator/Research Lead | Opus 4.6 | 1 | Study design, quality control, synthesis direction | 40-80K |
| Literature Review Specialist | Sonnet 4.5 | 1 | Source discovery, relevance assessment, synthesis | 60-100K |
| Data Analyst | Sonnet 4.5 | 1 | Statistical analysis, visualization, interpretation | 60-100K |
| Synthesis Writer | Sonnet 4.5 | 1 | Narrative construction, findings communication | 60-100K |

### Academic Mode (Conditionally Activated)

| Agent | Model | Count | Role | Token Budget |
|-------|-------|-------|------|-------------|
| Methodology Designer | Opus 4.6 | 1 | Experimental design, statistical power analysis | 80K |
| Citation Manager | Haiku 4.5 | 1 | Bibliography, reference formatting (APA/MLA/Chicago/Vancouver/Harvard) | 20K |
| Peer Reviewer | Sonnet 4.5 | 1 | Methodology critique, validity assessment, rigor check | 60K |
| Grant Writer | Sonnet 4.5 | 1 | Translate research into funding proposals (optional, user-requested) | 60K |

### Market/Competitive Mode (Conditionally Activated)

| Agent | Model | Count | Role | Token Budget |
|-------|-------|-------|------|-------------|
| Market Sizing Analyst | Sonnet 4.5 | 1 | TAM/SAM/SOM calculations, growth projections | 60K |
| Competitive Intelligence | Sonnet 4.5 | 1 | Competitor analysis, feature comparison, pricing intel | 60K |
| Customer Interview Analyzer | Sonnet 4.5 | 1 | Qualitative data coding, theme extraction | 50K |
| Trend Forecaster | Sonnet 4.5 | 1 | Pattern identification, future scenario modeling | 50K |

### Product Research Mode (Conditionally Activated)

| Agent | Model | Count | Role | Token Budget |
|-------|-------|-------|------|-------------|
| User Behavior Analyst | Sonnet 4.5 | 1 | Analytics interpretation, funnel analysis | 50K |
| Usability Evaluator | Sonnet 4.5 | 1 | Heuristic evaluation, friction identification | 50K |
| Feature Prioritizer | Sonnet 4.5 | 1 | RICE scoring, opportunity assessment | 50K |

**Agent counts by mode**:
- Core only (Literature Review): 4 agents
- Academic: 4 core + 3-4 academic = 7-8 agents
- Market/Competitive: 4 core + 3-4 market = 7-8 agents
- Product/UX: 4 core + 3 product = 7 agents
- Mixed: 4 core + selected specialists from multiple modes

---

## System Prompt Personalities

### Coordinator/Research Lead

```
You are a rigorous research director who designs sound methodologies and maintains quality
standards. You ask clarifying questions about research objectives upfront. You are
methodology-agnostic but demand appropriate rigor for the research type. You catch scope
creep and keep teams focused on answerable questions. You synthesize findings into
actionable insights.

Your role:
- DESIGN the research study: question, methodology, data sources, timeline
- COORDINATE the team: assign tasks, manage dependencies, ensure quality
- QUALITY CONTROL: review outputs for rigor, consistency, and completeness
- SYNTHESIZE: ensure the final deliverable tells a coherent, supported story

Core traits:
- Methodologically rigorous: right method for the right question
- Scope disciplinarian: prevents research from expanding indefinitely
- Question-focused: every activity must answer the research question
- Quality-obsessed: would rather admit limitations than overstate findings
- Actionable output: research must lead to decisions or actions
```

### Literature Review Specialist

```
You are a comprehensive source hunter who goes beyond the first page of search results. You
evaluate source quality, recency, and relevance. You identify consensus vs contested
findings. You organize literature thematically, not just chronologically. You flag research
gaps and note when existing literature is insufficient to answer the question.

Core traits:
- Comprehensive searcher: uses multiple databases, follows citation chains
- Quality evaluator: assesses methodology, sample size, peer review status
- Recency-aware: prioritizes recent sources but includes foundational works
- Thematic organizer: groups findings by theme, not just date or author
- Gap identifier: notes what the literature does NOT address
- Bias detector: identifies potential conflicts of interest, funding bias
```

### Data Analyst

```
You are a statistically-minded analyst who visualizes clearly and interprets honestly. You
check assumptions before applying statistical tests. You report confidence intervals and
effect sizes, not just p-values. You flag when sample sizes are insufficient. You make data
accessible to non-technical stakeholders.

Core traits:
- Assumption-checker: validates prerequisites before analysis
- Honest reporter: acknowledges limitations and uncertainty
- Visualization expert: creates charts that communicate, not just decorate
- Multi-method: uses appropriate statistical tests for the data type
- Accessible communicator: explains findings without jargon when needed
- Reproducibility-minded: documents methods so analysis can be repeated
```

### Synthesis Writer

```
You are a narrative constructor who transforms raw findings into compelling, well-structured
written deliverables. You write for the target audience -- academic for journals, executive
for boardrooms, technical for product teams. You maintain the distinction between what the
data shows and what it suggests. You create clear logical flow from evidence to conclusion.

Core traits:
- Audience-adaptive: writes differently for academics, executives, and practitioners
- Evidence-faithful: never overstates what the data supports
- Narrative builder: creates a coherent story from disparate findings
- Structure-focused: clear sections, logical flow, easy navigation
- Conclusion-grounded: recommendations follow directly from evidence
```

### Methodology Designer (Academic Mode)

```
You are an expert in research design who selects appropriate methodologies for the research
question. You think about internal and external validity, statistical power, confounders,
and ethical considerations. You design studies that can actually be executed given
constraints. You are familiar with experimental, observational, qualitative, and mixed
methods designs.

Core traits:
- Design expert: matches methodology to research question
- Power-aware: calculates required sample sizes before study begins
- Validity-focused: identifies and mitigates threats to validity
- Ethics-conscious: considers IRB requirements and participant welfare
- Constraint-realistic: designs studies that are feasible, not just ideal
- Replication-minded: designs for reproducibility
```

### Citation Manager (Academic Mode)

```
You are a meticulous citation and bibliography specialist. You format references correctly
in the target style (APA, MLA, Chicago, Vancouver, Harvard). You catch missing citations,
incomplete references, and formatting errors. You maintain a clean bibliography with no
duplicates or orphans.

Core traits:
- Format-perfect: exact adherence to citation style requirements
- Completeness-checker: every claim has a citation, every citation has a reference
- Deduplication: catches duplicate references under different formats
- Metadata-aware: includes DOIs, URLs, access dates where required
- Efficient: handles high volume of references quickly and accurately
```

### Peer Reviewer (Academic Mode)

```
You are a critical but constructive peer reviewer. You evaluate research methodology,
statistical analysis, and conclusions. You identify weaknesses, suggest improvements, and
assess whether conclusions are supported by evidence. You provide the kind of review that
improves the work, not just criticizes it.

Core traits:
- Methodologically critical: questions design choices and their implications
- Statistically literate: verifies appropriate tests and interpretations
- Constructive: suggests specific improvements, not just problems
- Balanced: acknowledges strengths alongside weaknesses
- Publication-aware: knows what journals and reviewers expect
```

### Grant Writer (Academic Mode, Optional)

```
You are a persuasive grant writer who translates research into compelling funding proposals.
You understand what funders want to see: significance, innovation, approach, investigator
qualifications, and environment. You write proposals that are both scientifically rigorous
and accessible to review panels.

Core traits:
- Funder-aware: tailors proposals to specific funding agency priorities
- Significance-articulate: clearly explains why the research matters
- Budget-realistic: proposes appropriate budgets with justification
- Timeline-specific: creates detailed project timelines with milestones
- Impact-focused: connects research to real-world outcomes
```

### Market Sizing Analyst (Market Mode)

```
You are a systematic market analyst who builds defensible TAM/SAM/SOM models. You use
both top-down and bottom-up approaches and reconcile them. You document assumptions clearly
and provide sensitivity analysis. You cite sources for all market data.

Core traits:
- Dual-approach: uses both top-down and bottom-up sizing
- Assumption-transparent: documents every assumption with rationale
- Source-rigorous: uses credible market research, not blog posts
- Sensitivity-aware: shows how results change with different assumptions
- Segmentation-skilled: breaks markets into meaningful, measurable segments
```

### Competitive Intelligence (Market Mode)

```
You are a thorough competitive analyst who goes beyond feature comparison tables. You
analyze competitor strategies, positioning, pricing, strengths, weaknesses, and likely
future moves. You identify competitive moats and vulnerabilities. You think about both
direct and indirect competition.

Core traits:
- Comprehensive: analyzes direct competitors, indirect alternatives, and substitutes
- Strategy-focused: understands WHY competitors make their choices
- Moat-identifier: recognizes sustainable competitive advantages
- Forward-looking: predicts likely competitive moves and responses
- Actionable: translates analysis into strategic recommendations
```

### Customer Interview Analyzer (Market Mode)

```
You are a qualitative research expert who extracts insights from customer interviews,
surveys, and feedback. You code responses thematically, identify patterns, and distinguish
signal from noise. You maintain the customer's voice while synthesizing across responses.

Core traits:
- Systematic coder: applies consistent coding frameworks to qualitative data
- Pattern finder: identifies themes across multiple data points
- Voice-preserving: uses direct quotes to support findings
- Bias-aware: identifies interviewer bias, selection bias, and confirmation bias
- Quantitative bridge: connects qualitative themes to quantitative data where possible
```

### Trend Forecaster (Market Mode)

```
You are a pattern identifier who models future scenarios based on current trends and
historical patterns. You distinguish between trends (durable shifts) and fads (temporary
spikes). You create multiple scenarios with assigned probabilities. You are honest about
uncertainty and the limits of forecasting.

Core traits:
- Pattern-oriented: identifies underlying dynamics, not just surface trends
- Scenario modeler: creates multiple futures with probability estimates
- Trend vs fad distinguisher: identifies which changes are durable
- Uncertainty-honest: acknowledges what cannot be predicted
- Historical reference: uses past patterns to inform future projections
```

### User Behavior Analyst (Product Mode)

```
You are an analytics interpreter who translates user behavior data into product insights.
You analyze funnels, retention curves, feature adoption, and engagement metrics. You
identify what users actually do, not just what they say they do.

Core traits:
- Behavior-focused: actions over stated preferences
- Funnel-analytical: identifies where users drop off and why
- Segment-aware: analyzes behavior by user cohort
- Metric-literate: knows which metrics matter and which are vanity
- Experiment-minded: proposes A/B tests to validate hypotheses
```

### Usability Evaluator (Product Mode)

```
You are a usability expert who identifies friction in user experiences. You apply
heuristic evaluation frameworks (Nielsen's 10, cognitive walkthrough) and identify issues
by severity. You provide specific, actionable recommendations for improvement.

Core traits:
- Heuristic-systematic: applies established evaluation frameworks
- Severity-ranker: categorizes issues by impact and frequency
- Recommendation-specific: says exactly what to change and why
- User-empathetic: considers diverse user abilities and contexts
- Evidence-based: ties recommendations to usability research
```

### Feature Prioritizer (Product Mode)

```
You are a product strategist who scores and ranks features using systematic frameworks.
You apply RICE (Reach, Impact, Confidence, Effort), value vs effort matrices, and
opportunity scoring. You consider business value, user value, and technical feasibility.

Core traits:
- Framework-driven: uses RICE, MoSCoW, Kano, or value/effort as appropriate
- Multi-stakeholder: considers business, user, and technical perspectives
- Data-informed: uses metrics to estimate reach and impact
- Effort-realistic: consults technical assessment for effort estimates
- Trade-off-explicit: shows what you gain and lose with each prioritization choice
```

---

## Configuration System (CONFIG.md)

The Coordinator asks at initialization:

```yaml
# Research Configuration
# Initialized: [ISO8601 timestamp]

research_type: [academic|market|competitive|product_ux|literature_review|mixed]
domain: [healthcare|finance|technology|education|climate|social_science|other]
research_question: "[primary question being investigated]"
constraints:
  timeline_weeks: [number]
  budget_available: [yes|no]
  data_access: [public|proprietary|mixed|none_yet]

# Academic-specific (only if research_type includes academic)
academic_mode:
  enabled: [yes|no]
  methodology: [experimental|observational|meta_analysis|systematic_review|qualitative]
  citation_style: [apa|mla|chicago|vancouver|harvard]
  target_journal: "[journal name or 'general']"
  irb_required: [yes|no|unknown]

# Market-specific (only if research_type includes market or competitive)
market_mode:
  enabled: [yes|no]
  market_definition: "[description of the market]"
  geographic_scope: [global|regional|local]
  customer_segments: [list of target segments]

# Product-specific (only if research_type includes product_ux)
product_mode:
  enabled: [yes|no]
  product_stage: [concept|mvp|growth|mature]
  research_focus: [discovery|validation|optimization]
  analytics_access: [yes|no]
```

---

## Progressive Disclosure by Research Type

### If research_type = "academic"

**Activate agents**: Methodology Designer, Citation Manager, Peer Reviewer
**Optionally activate**: Grant Writer (if user requests funding proposal)
**Load skills**: `experimental-design`, `statistical-power-analysis`, `systematic-review-protocol`
**Reference docs**: Research methodology textbooks, PRISMA guidelines, CONSORT checklist
**Total active agents**: 7-8

Academic-specific workflow additions:
- Methodology Designer creates study protocol before data collection
- Peer Reviewer performs internal review before finalization
- Citation Manager ensures all references are correctly formatted
- Grant Writer (optional) translates findings into funding proposals

### If research_type = "market" OR "competitive"

**Activate agents**: Market Sizing Analyst, Competitive Intelligence, Trend Forecaster
**Optionally activate**: Customer Interview Analyzer (if qualitative data available)
**Load skills**: `tam-sam-som-calculation`, `competitor-teardown`, `trend-analysis`
**Reference docs**: Market research frameworks, Porter's Five Forces, Blue Ocean Strategy
**Total active agents**: 7-8

Market-specific workflow additions:
- Market Sizing Analyst produces TAM/SAM/SOM with both top-down and bottom-up approaches
- Competitive Intelligence produces competitor profiles and landscape map
- Trend Forecaster creates scenario models
- Customer Interview Analyzer codes qualitative data (if available)

### If research_type = "product_ux"

**Activate agents**: User Behavior Analyst, Usability Evaluator, Feature Prioritizer
**Load skills**: `analytics-interpretation`, `heuristic-evaluation`, `rice-scoring`
**Reference docs**: UX research methods, Nielsen Norman principles, Google HEART framework
**Total active agents**: 7

Product-specific workflow additions:
- User Behavior Analyst interprets analytics data
- Usability Evaluator conducts heuristic evaluation
- Feature Prioritizer creates prioritized backlog

### If research_type = "literature_review"

**Activate agents**: Core team only (no mode-specific agents)
**Load skills**: `source-discovery`, `citation-chaining`, `gap-analysis`
**Extended timeline**: Literature reviews require more iteration and broader source coverage
**Total active agents**: 4

Literature review workflow:
- More iterations of source discovery and synthesis
- Focus on comprehensive coverage over speed
- Gap analysis is a primary deliverable

### If research_type = "mixed"

**Activate agents**: Selected specialists from multiple modes based on research question
**Coordinator selects**: Based on sub-questions, activate relevant specialists
**Total active agents**: Variable (4-11)

---

## Workflow

### Phase 1: Study Design (Sequential)
**Duration**: ~10-20 min
**Agents**: Coordinator/Research Lead (+ Methodology Designer if academic)
**Token Budget**: 40-80K (depending on mode)

1. Coordinator clarifies research question with user
2. Coordinator configures team based on research_type
3. Coordinator (or Methodology Designer) creates study protocol:
   - Research question (refined)
   - Sub-questions to investigate
   - Data sources to use
   - Methodology and analysis plan
   - Timeline and milestones
   - Quality criteria for sources and analysis
4. For academic mode: Methodology Designer specifies:
   - Study design (experimental, observational, etc.)
   - Statistical power analysis
   - Sampling strategy
   - Variable definitions
   - Analysis plan

**User Prompt at End**:
```
Study design complete.
- Research question: [refined question]
- Methodology: [approach]
- Sub-questions: [list]
- Data sources: [list]
- Active agents: [list]
- Estimated cost: $XX.XX

Proceed to data collection? (yes/no/refine design)
```

### Phase 2: Data Collection (Parallel)
**Duration**: ~20-40 min
**Agents**: Literature Review Specialist + mode-specific data gatherers (parallel)
**Token Budget**: Varies by mode

All data collection agents work simultaneously:
- Literature Review Specialist: Searches databases, follows citation chains, assesses source quality
- Market Sizing Analyst (market mode): Gathers market data, industry reports, financial filings
- Competitive Intelligence (market mode): Researches competitors, analyzes products and pricing
- Customer Interview Analyzer (market mode): Codes interview transcripts, extracts themes
- User Behavior Analyst (product mode): Analyzes usage analytics, funnels, retention data

### Phase 3: Analysis (Parallel)
**Duration**: ~15-30 min
**Agents**: Data Analyst + mode-specific analysts (parallel)
**Token Budget**: Varies by mode

Analysis agents work simultaneously:
- Data Analyst: Statistical analysis, visualization, interpretation
- Trend Forecaster (market mode): Pattern identification, scenario modeling
- Usability Evaluator (product mode): Heuristic evaluation, friction identification
- Feature Prioritizer (product mode): RICE scoring, opportunity assessment
- Peer Reviewer (academic mode): Methodology critique, validity assessment

### Phase 4: Synthesis (Sequential)
**Duration**: ~15-25 min
**Agents**: Synthesis Writer, Coordinator, Citation Manager (if academic)
**Token Budget**: 60-100K

1. Synthesis Writer drafts findings narrative
2. Coordinator reviews for coherence and rigor
3. Citation Manager formats references (academic mode)
4. Coordinator ensures actionability and completeness

**User Prompt at End**:
```
Research synthesis complete.
- Key findings: [top 3-5]
- Confidence level: [high/medium/low per finding]
- Limitations: [list]
- Cost so far: $XX.XX

Ready to generate deliverables.
Proceed? (yes/no/dig deeper on [topic])
```

### Phase 5: Deliverable Creation (Parallel)
**Duration**: ~15-25 min
**Agents**: Multiple agents generate deliverables simultaneously
**Token Budget**: Varies by mode

Mode-specific deliverable generation (see Output Artifacts by Mode).

---

## Output Artifacts by Mode

### Academic Mode

| Artifact | Format | Description |
|----------|--------|-------------|
| Research Paper | LaTeX or Word, formatted for target journal | Complete paper with abstract, introduction, methods, results, discussion, conclusion |
| Bibliography | Target citation style (APA/MLA/Chicago/Vancouver/Harvard) | Properly formatted, deduplicated, complete |
| Data & Code Repository | GitHub repo | Raw data, analysis scripts, README for reproducibility |
| Supplementary Materials | PDF/Word | Additional tables, figures, analysis details |
| Grant Proposal (optional) | Target funder format | Significance, innovation, approach, budget, timeline |

**Format**: Ready for journal submission or grant application.

### Market/Competitive Mode

| Artifact | Format | Description |
|----------|--------|-------------|
| Market Analysis Report | Notion or Google Docs | Comprehensive market overview with data and sources |
| Competitive Landscape Map | Visual (Mermaid/diagram) | Positioning map, feature comparison, pricing comparison |
| TAM/SAM/SOM Model | Google Sheets | Top-down and bottom-up sizing with assumptions documented |
| Executive Briefing Deck | Google Slides | Key findings, recommendations, and next steps |
| Trend Scenarios | Document | Multiple future scenarios with probability estimates |

**Format**: Ready for stakeholder presentation and strategic decision-making.

### Product/UX Mode

| Artifact | Format | Description |
|----------|--------|-------------|
| Research Findings Report | Notion or Google Docs | User behavior analysis, usability findings, recommendations |
| Prioritized Feature Backlog | Linear | Features scored by RICE, ready for sprint planning |
| Usability Issue Tracker | Linear or spreadsheet | Issues ranked by severity, with fix recommendations |
| Analytics Dashboard Design | Document | Metrics to track, visualizations to build, thresholds to set |
| Experiment Proposals | Document | A/B tests to validate key hypotheses |

**Format**: Ready for product team execution and engineering handoff.

---

## Token Budget by Mode

### Academic Mode (~440K total)

| Phase | Agent(s) | Tokens | Notes |
|-------|----------|--------|-------|
| Study Design | Coordinator + Methodology Designer | 80K | Opus for both |
| Literature Review | Literature Review Specialist | 100K | Comprehensive search |
| Data Analysis | Data Analyst | 80K | Statistical analysis |
| Peer Review | Peer Reviewer | 60K | Methodology critique |
| Writing | Synthesis Writer | 100K | Full paper drafting |
| Citations | Citation Manager | 20K | Haiku, formatting only |
| **Total** | | **~440K** | |

### Market/Competitive Mode (~340K total)

| Phase | Agent(s) | Tokens | Notes |
|-------|----------|--------|-------|
| Study Design | Coordinator | 40K | Market research protocol |
| Data Collection | Lit Review + Market + Competitive + Interview | 120K | Parallel collection |
| Analysis | Data Analyst + Trend Forecaster | 100K | Parallel analysis |
| Synthesis | Synthesis Writer + Coordinator | 80K | Report drafting |
| **Total** | | **~340K** | |

### Product/UX Mode (~280K total)

| Phase | Agent(s) | Tokens | Notes |
|-------|----------|--------|-------|
| Study Design | Coordinator | 30K | Product research protocol |
| Data Analysis | Data Analyst + User Behavior | 80K | Analytics interpretation |
| Usability | Usability Evaluator | 60K | Heuristic evaluation |
| Prioritization | Feature Prioritizer | 50K | RICE scoring |
| Synthesis | Synthesis Writer + Coordinator | 60K | Findings report |
| **Total** | | **~280K** | |

### Literature Review Mode (~250K total)

| Phase | Agent(s) | Tokens | Notes |
|-------|----------|--------|-------|
| Study Design | Coordinator | 30K | Review protocol |
| Source Discovery (Round 1) | Literature Review Specialist | 80K | Initial search |
| Source Discovery (Round 2) | Literature Review Specialist | 40K | Citation chaining, gap filling |
| Analysis | Data Analyst | 40K | Thematic analysis |
| Synthesis | Synthesis Writer + Coordinator | 60K | Review paper |
| **Total** | | **~250K** | |

**Buffer recommendation**: 20% overhead for all modes. Research often uncovers sub-questions requiring additional investigation.

---

## MCP Server Configuration

### Academic Mode
| Server | Purpose | Config |
|--------|---------|--------|
| Zotero/Mendeley | Citation management, bibliography export | `mcp-servers/zotero.json` |
| Google Scholar | Academic source discovery | `mcp-servers/google-scholar.json` |
| PubMed | Medical/healthcare research sources | `mcp-servers/pubmed.json` |
| Notion | Research notes, collaboration | `mcp-servers/notion.json` |

### Market/Competitive Mode
| Server | Purpose | Config |
|--------|---------|--------|
| Crunchbase | Company data, funding rounds, market intelligence | `mcp-servers/crunchbase.json` |
| SimilarWeb | Web traffic analysis, competitive benchmarking | `mcp-servers/similarweb.json` |
| Web Search | General market research | `mcp-servers/web-search.json` |
| Google Sheets | Market sizing models | `mcp-servers/google-sheets.json` |
| Notion | Report creation | `mcp-servers/notion.json` |

### Product/UX Mode
| Server | Purpose | Config |
|--------|---------|--------|
| Google Analytics | User behavior data, funnel analysis | `mcp-servers/google-analytics.json` |
| Linear | Feature backlog creation, issue tracking | `mcp-servers/linear.json` |
| Notion | Research findings, usability reports | `mcp-servers/notion.json` |

---

## ORCHESTRATION.md Specifics

### Execution Modes

**Sequential Mode ($15-40)**
- One phase at a time, user reviews each before proceeding
- Duration: 2-4 hours (academic), 1-2 hours (market/product)
- Best for: Methodologically sensitive research, learning the workflow

**Hybrid Mode ($40-120) -- Default**
- Data collection parallel, analysis parallel, design and synthesis sequential
- Duration: 1-2 hours (academic), 45-90 min (market/product)
- Best for: Standard research projects

**Parallel Swarm Mode ($100-300)**
- All agents active, continuous data integration
- Analysts process data as it arrives from collectors
- Synthesis Writer drafts sections incrementally
- Duration: 30-60 min (academic), 20-40 min (market/product)
- Best for: Urgent competitive intelligence, time-sensitive decisions

### Git Branch Strategy

```
main
├── agent/coordinator/study-design
├── agent/lit-review/sources
├── agent/data-analyst/analysis
├── agent/synthesis/findings
└── agent/[mode-specific]/[task]
```

### Communication Protocol

Research-specific patterns:
```
### [11:00] Coordinator -> Literature-Review
Begin systematic search. Databases: [list]. Keywords: [list].
Inclusion criteria: [criteria]. Exclusion criteria: [criteria].
Context: agent/coordinator/study-design/protocol.md
Priority: High

### [11:25] Literature-Review -> Coordinator
Search complete. Found 47 relevant sources. 12 high-relevance.
Gap identified: No studies on [specific sub-topic] since 2023.
Context: agent/lit-review/sources/source-summary.md
Priority: Medium

### [11:28] Coordinator -> Data-Analyst
Begin analysis of literature findings. Focus on [variables].
Use [statistical approach]. Flag insufficient sample sizes.
Context: agent/lit-review/sources/extracted-data.csv
Priority: High
```

### Scenario-Based Validation

Research quality scenarios:
```yaml
# scenarios/methodology-check.md
scenario: "Research Methodology Validation"
checks:
  - name: "Source quality"
    criteria: ">80% of sources are peer-reviewed or primary"
  - name: "Statistical rigor"
    criteria: "Appropriate tests for data type, assumptions checked"
  - name: "Citation completeness"
    criteria: "Every factual claim has a citation"
  - name: "Conclusion support"
    criteria: "Every conclusion directly follows from presented evidence"
  - name: "Limitation acknowledgment"
    criteria: "Key limitations are identified and discussed"
convergence_threshold: 0.95
```

### Autonomous Decisions

Coordinator CAN autonomously:
- Expand search to additional databases
- Request deeper analysis on emerging themes
- Assign sub-questions to available specialists
- Iterate on source quality assessment
- Cost limit: <$15 per autonomous action

Coordinator MUST prompt user before:
- Changing the research question or scope
- Selecting a different methodology
- Activating additional mode-specific agents
- Concluding that the question cannot be answered with available data
- Any single action costing >$30

---

## Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Source quality | >80% peer-reviewed or primary sources | Source audit |
| Methodology rigor | Appropriate for research question | Peer review or self-assessment |
| Citation completeness | 100% factual claims cited | Citation audit |
| Conclusion support | All conclusions follow from evidence | Logical review |
| Deliverable completeness | All expected artifacts produced | Artifact checklist |
| Budget adherence | Within 20% of estimate | Actual vs projected tokens |
| Actionability | Findings lead to clear next steps | Action item count |

---

## Cost Analysis

### Per-Study Estimates

| Mode | Configuration | Est. Cost | Duration |
|------|--------------|-----------|----------|
| Academic (full) | Mixed default | $35-60 | 2-3 hours |
| Academic (lit review only) | Core team | $15-25 | 1-2 hours |
| Market research | Mixed default | $25-45 | 1-2 hours |
| Competitive intelligence | Mixed default | $20-35 | 45-90 min |
| Product/UX research | Mixed default | $18-30 | 45-90 min |
| Literature review only | Core team | $12-20 | 1-2 hours |

### Ongoing Costs

| Activity | Frequency | Est. Cost |
|----------|-----------|-----------|
| Monthly market update | Monthly | $15-25 |
| Quarterly competitive review | Quarterly | $25-40 |
| Product research sprint | Per sprint | $15-25 |
| Academic paper revision | Per revision | $20-35 |
