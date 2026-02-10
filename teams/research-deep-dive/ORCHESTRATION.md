# Multi-Agent Orchestration Protocol

This document defines the execution phases, communication protocols, quality gates, and decision-making framework for the Research Deep Dive Team.

---

## Execution Modes

The team supports three execution modes. The mode is selected at runtime via the `--mode` flag.

### Sequential Mode ($15-40)

Agents execute one at a time in a defined order. Slowest but gives maximum methodological control at each stage.

```
Coordinator (Study Design) -> Primary Researcher (Collection) -> Analyst (Analysis) -> Synthesizer (Writing) -> Coordinator (Review)
```

**Total time:** 2-4 hours (academic), 1-2 hours (market/product)
**When to use:** Methodologically sensitive research, learning the workflow, when each phase needs user review before proceeding.

### Hybrid Mode (Recommended -- $40-120)

Data collection runs in parallel. Analysis runs in parallel. Study design and synthesis are sequential with user review points.

```
Phase 1 (sequential): Coordinator -- Study Design
  | [User Review Point]
Phase 2 (parallel): Primary Researcher + mode-specific collectors
  |
Phase 3 (parallel): Analyst + mode-specific analysts
  |
Phase 4 (sequential): Synthesizer -> Coordinator review
  | [User Review Point]
Phase 5 (parallel): Deliverable creation
```

**Total time:** 1-2 hours (academic), 45-90 min (market/product)
**When to use:** Standard research projects. Best balance of speed and rigor.

### Parallel Swarm Mode ($100-300)

All agents active with continuous data integration. Analysts process data as it arrives from collectors. The Synthesizer drafts sections incrementally.

**Total time:** 30-60 min (academic), 20-40 min (market/product)
**When to use:** Urgent competitive intelligence, time-sensitive decisions.
**Warning:** Higher token usage from overlapping agent activity and incremental processing.

---

## Phase Definitions

### Phase 1: Study Design (Sequential -- ~10-20 minutes)

**Goal:** Define the research protocol before any data collection begins. Searching without a plan produces noise, not insight.

#### Coordinator / Research Lead

- Clarify the research question with the user (refine if vague)
- Configure the team based on `research_type` from CONFIG
- Create the study protocol:
  - Research question (refined and scoped)
  - Sub-questions to investigate
  - Data sources to use
  - Methodology and analysis plan
  - Timeline and milestones
  - Quality criteria for sources and analysis
  - Active agents for this study
- For academic mode: Methodology Designer specifies study design, statistical power analysis, sampling strategy, variable definitions
- Estimate cost and present to user

**Outputs:**
- Study protocol document
- Team configuration (which agents are active)
- Cost estimate

#### User Review Point

```
Study design complete.
- Research question: [refined question]
- Methodology: [approach]
- Sub-questions: [list]
- Data sources: [list]
- Active agents: [list]
- Estimated cost: $XX.XX

Proceed to data collection? (yes / no / refine design)
```

---

### Phase 2: Data Collection (Parallel -- ~20-40 minutes)

**Goal:** Gather all relevant data from configured sources. Multiple collectors work simultaneously to maximize coverage.

#### Primary Researcher
- Search databases using multiple query formulations
- Follow citation chains from high-relevance sources
- Assess source quality, recency, and relevance
- Organize findings thematically
- Flag research gaps and contested findings

#### Mode-Specific Collectors (Parallel)
- **Market mode:** Market Sizing Analyst gathers market data, industry reports, financial filings. Competitive Intelligence researches competitors, products, pricing.
- **Academic mode:** Primary Researcher extends to academic databases (arXiv, PubMed, Google Scholar). Citation Manager begins collecting reference metadata.
- **Product mode:** User Behavior Analyst interprets provided analytics data. Customer Interview Analyzer codes provided transcripts.

**Outputs:**
- Source database with credibility assessments
- Thematic literature summary
- Mode-specific raw data (market data, competitor profiles, analytics interpretation)
- Research gaps identified

**Depends on:** Phase 1 study protocol (defines what to search for and where).

---

### Phase 3: Analysis (Parallel -- ~15-30 minutes)

**Goal:** Analyze collected data using appropriate methods. Multiple analysts work simultaneously on different aspects.

#### Analyst (Data Analyst)
- Perform statistical analysis on collected data
- Check assumptions before applying statistical tests
- Create visualizations that communicate findings
- Report confidence intervals and effect sizes
- Flag insufficient data or methodological limitations

#### Mode-Specific Analysts (Parallel)
- **Market mode:** Trend Forecaster identifies patterns and builds scenario models.
- **Academic mode:** Peer Reviewer critiques methodology and assesses validity.
- **Product mode:** Usability Evaluator conducts heuristic evaluation. Feature Prioritizer performs RICE scoring.

**Outputs:**
- Statistical analysis report
- Data visualizations
- Mode-specific analysis (trend scenarios, peer review, usability audit, feature scores)
- Confidence assessments

**Depends on:** Phase 2 data collection outputs.

---

### Phase 4: Synthesis (Sequential -- ~15-25 minutes)

**Goal:** Transform raw findings and analysis into coherent, audience-appropriate deliverables.

#### Synthesizer
- Draft the primary research narrative
- Structure findings for the target audience (academic, executive, product team)
- Maintain the distinction between what data shows and what it suggests
- Ensure recommendations follow directly from evidence
- Include explicit limitations section

#### Coordinator Review
- Review synthesis for coherence and rigor
- Verify all conclusions are supported by evidence
- Check that limitations are honestly documented
- Ensure actionability (findings must lead to decisions or actions)

**Outputs:**
- Draft research deliverable
- Executive summary
- Recommendations with evidence mapping

#### User Review Point

```
Research synthesis complete.
- Key findings: [top 3-5]
- Confidence level: [high/medium/low per finding]
- Limitations: [list]
- Cost so far: $XX.XX

Ready to generate final deliverables.
Proceed? (yes / no / dig deeper on [topic])
```

**Depends on:** Phase 3 analysis outputs.

---

### Phase 5: Deliverable Creation (Parallel -- ~15-25 minutes)

**Goal:** Produce all mode-specific deliverables in their target formats.

Multiple agents generate deliverables simultaneously:
- Synthesizer finalizes the primary document
- Citation Manager formats bibliography (academic mode)
- Market Sizing Analyst finalizes TAM/SAM/SOM model (market mode)
- Feature Prioritizer finalizes scored backlog (product mode)
- Coordinator performs final quality review

**Outputs:** Mode-specific deliverables (see TEAM_SPEC.md Output Artifacts by Mode).

---

## Communication Protocol

### Message Types

| Type | Purpose | Example |
|------|---------|---------|
| `PROTOCOL` | Share study design | Coordinator sends study protocol to all agents |
| `DATA` | Deliver collected data | Primary Researcher sends source database to Analyst |
| `ANALYSIS` | Deliver analysis results | Analyst sends statistical report to Synthesizer |
| `SYNTHESIS` | Deliver draft narrative | Synthesizer sends draft to Coordinator |
| `GATE` | Quality gate result | Coordinator reports phase result |
| `ESCALATE` | Escalate to user | Coordinator escalates scope or methodology question |

### Message Format

```yaml
type: DATA
from: primary-researcher
to: [analyst, coordinator]
phase: 2
subject: "Source collection complete"
body: |
  Found 47 relevant sources. 12 high-relevance.
  Gap identified: No studies on [specific sub-topic] since 2023.
  Contested finding: Sources disagree on [claim] -- flagged for analysis.
attachments:
  - "data/source-database.md"
  - "data/thematic-summary.md"
```

### Research-Specific Communication Patterns

```
### [11:00] Coordinator -> Primary-Researcher
Begin systematic search. Databases: [list]. Keywords: [list].
Inclusion criteria: [criteria]. Exclusion criteria: [criteria].
Context: agent/coordinator/study-design/protocol.md
Priority: High

### [11:25] Primary-Researcher -> Coordinator
Search complete. Found 47 relevant sources. 12 high-relevance.
Gap identified: No studies on [specific sub-topic] since 2023.
Context: agent/primary-researcher/sources/source-summary.md
Priority: Medium

### [11:28] Coordinator -> Analyst
Begin analysis of literature findings. Focus on [variables].
Use [statistical approach]. Flag insufficient sample sizes.
Context: agent/primary-researcher/sources/extracted-data.csv
Priority: High
```

### Conflict Resolution

Research conflicts arise when data contradicts expectations:

1. **Contradictory sources:** The Analyst flags the contradiction. The Coordinator decides whether to present both perspectives, favor stronger evidence, or investigate further.
2. **Insufficient data:** The Primary Researcher documents the gap. The Coordinator decides whether to narrow the question, accept the limitation, or expand the search.
3. **Methodology disputes:** The Coordinator is the final arbiter on methodology. In academic mode, the Peer Reviewer provides input, but the Coordinator decides.

---

## Git Strategy

### Branch Model

```
main
+-- agent/coordinator/study-design
+-- agent/primary-researcher/sources
+-- agent/analyst/analysis
+-- agent/synthesizer/findings
+-- agent/[mode-specific]/[task]
```

Each agent commits to their branch. The Coordinator merges the final deliverables to `main` after the quality review.

### Commit Convention

```
<type>(<agent>): <subject>

<body>

Agent: <agent-name>
Phase: <phase-number>
```

Types: `protocol`, `data`, `analysis`, `synthesis`, `review`, `deliverable`

Example:
```
data(primary-researcher): complete source collection for market sizing

- Found 47 relevant sources across 5 databases
- 12 sources rated high-relevance for TAM/SAM calculation
- Gap: No reliable data on Southeast Asia segment post-2024
- Flagged 3 contradictory findings on market growth rate

Agent: primary-researcher
Phase: 2
```

---

## Autonomous vs User-Prompted Decisions

### Autonomous (Coordinator Decides Without User Input)

The Coordinator can autonomously:
- Expand search to additional databases (cost < $15)
- Request deeper analysis on emerging themes
- Assign sub-questions to available specialists
- Iterate on source quality assessment
- Adjust data collection scope within the study protocol
- Request clarification from other agents
- **Cost limit:** <$15 per autonomous action

### User-Prompted (Require User Input)

The Coordinator must prompt the user before:
- Changing the research question or scope
- Selecting a different methodology
- Activating additional mode-specific agents not in the original plan
- Concluding that the question cannot be answered with available data
- Any single action costing >$30
- Exceeding the configured cost budget by more than 15%

**Prompt template:**
```
I recommend [action] because [reason].
- Cost: $X.XX
- Impact on timeline: [estimate]
- Alternative: [other option]

Proceed? (yes / no / alternative)
```

---

## Scenario-Based Validation

After the final phase, the Coordinator validates against quality scenarios:

```yaml
research_quality_check:
  - name: "Source quality"
    criteria: ">80% of sources are peer-reviewed or primary"
    blocking: true
  - name: "Statistical rigor"
    criteria: "Appropriate tests for data type, assumptions checked"
    blocking: true
  - name: "Citation completeness"
    criteria: "Every factual claim has a citation"
    blocking: true
  - name: "Conclusion support"
    criteria: "Every conclusion directly follows from presented evidence"
    blocking: true
  - name: "Limitation acknowledgment"
    criteria: "Key limitations are identified and discussed"
    blocking: true
  - name: "Deliverable completeness"
    criteria: "All expected artifacts for the mode are produced"
    blocking: false
  - name: "Budget adherence"
    criteria: "Actual cost within 20% of estimate"
    blocking: false
convergence_threshold: 1.0  # All blocking criteria must pass
```

If blocking criteria are not met, the Coordinator either:
1. Runs another iteration of the failing phase (if within budget)
2. Escalates to the user with a specific remediation plan
