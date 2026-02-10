# Scenario: Product Discovery Research

This scenario defines the end-to-end flow for conducting product discovery research, including user behavior analysis, usability evaluation, feature prioritization, and experiment design.

---

## Scenario Overview

| Property | Value |
|----------|-------|
| **Priority** | High |
| **Research Mode** | Product/UX |
| **Validated After** | Phase 5 |
| **Primary Agents** | Core team + User Behavior Analyst, Usability Evaluator, Feature Prioritizer |
| **Estimated Duration** | ~60-90 minutes (hybrid mode) |
| **Estimated Cost** | ~$18-30 (default config) |

---

## Success Path: Product Discovery for a Growth-Stage Product

### Preconditions

- Product mode is enabled with `research_focus: discovery` or `validation`
- Product URL is provided for usability evaluation
- Analytics data export is available (optional but recommended)
- Interview transcripts or user feedback are available (optional)
- Research question specifies what product decisions need to be informed

### Steps

| Step | Agent | Action | Expected Outcome |
|------|-------|--------|------------------|
| 1 | Coordinator | Design product research protocol: research questions, data sources, evaluation frameworks, success metrics | Study protocol with clear decision criteria |
| 2 | Primary Researcher | Gather external data: comparable product research, industry benchmarks, UX best practices, competitor UX teardowns | Source database with product research and benchmarks |
| 3 | User Behavior Analyst | Analyze provided analytics: funnel analysis, retention curves, feature adoption, engagement metrics | Behavior report with drop-off points, engagement patterns, cohort differences |
| 4 | Usability Evaluator | Conduct heuristic evaluation of the product using Nielsen's 10 heuristics | Usability issue list ranked by severity and impact |
| 5 | Analyst | Cross-reference behavior data with usability findings, identify patterns | Integrated analysis connecting quantitative behavior to qualitative friction |
| 6 | Feature Prioritizer | Score improvement opportunities using RICE framework | Prioritized feature/improvement backlog with scores and rationale |
| 7 | Synthesizer | Draft product research report with executive summary, key findings, and prioritized recommendations | Complete report with experiment proposals |
| 8 | Coordinator | Review for actionability: recommendations are specific, testable, and tied to evidence | GO decision with quality metrics |

### Validation Criteria

- [ ] Research protocol maps research questions to specific product decisions
- [ ] Behavior analysis identifies top 3-5 user friction points with data
- [ ] Usability evaluation follows a recognized framework (Nielsen, WCAG, etc.)
- [ ] Each usability issue has a severity rating and remediation recommendation
- [ ] Feature backlog is scored with RICE (Reach, Impact, Confidence, Effort)
- [ ] Recommendations are specific enough for engineering to act on
- [ ] Experiment proposals include hypothesis, metric, success criteria, and sample size
- [ ] Findings distinguish between "users say" and "users do" when applicable
- [ ] Competitive UX benchmarks provide context for usability assessment

---

## Edge Case: No Analytics Data Available

### Preconditions

- Product is at concept or early MVP stage with no usage analytics
- Only qualitative data (interviews, surveys, prototype feedback) is available

### Steps

| Step | Agent | Action | Expected Outcome |
|------|-------|--------|------------------|
| 1 | Coordinator | Adjusts protocol: remove behavior analysis, emphasize competitive benchmarks and heuristic evaluation | Revised protocol focused on available data |
| 2 | Primary Researcher | Expands competitive UX research to compensate for missing behavior data | Deeper competitive analysis with UX patterns |
| 3 | Usability Evaluator | Conducts heuristic evaluation against prototypes or mockups | Usability assessment of planned experience |
| 4 | Feature Prioritizer | Uses qualitative signals and competitive analysis for RICE scoring | Backlog with higher uncertainty, wider confidence ranges |

### Validation Criteria

- [ ] Missing data is documented as a limitation, not silently ignored
- [ ] RICE confidence scores are appropriately lower without quantitative data
- [ ] Competitive UX analysis provides proxy benchmarks
- [ ] Experiment proposals are designed to generate the missing data

---

## Edge Case: Conflicting Signals Between Quantitative and Qualitative Data

### Preconditions

- Users say they want feature X in interviews, but behavior data shows feature X has low adoption
- Or: users complain about friction Y, but funnel data shows no significant drop-off at that step

### Steps

| Step | Agent | Action | Expected Outcome |
|------|-------|--------|------------------|
| 1 | User Behavior Analyst | Flags discrepancy between stated preferences and actual behavior | Discrepancy report with both data sets |
| 2 | Analyst | Investigates potential explanations: discoverability issue, sampling bias in interviews, behavioral segments | Analysis of why signals conflict |
| 3 | Coordinator | Determines whether to trust behavior data (generally preferred) or investigate further | Decision on how to weight conflicting signals |
| 4 | Feature Prioritizer | Adjusts RICE scores based on the resolution, adds uncertainty | Updated backlog with documented reasoning |

### Validation Criteria

- [ ] Conflict is documented, not resolved by ignoring one signal
- [ ] Behavioral data is given appropriate weight (actions over words)
- [ ] Potential explanations for the conflict are explored
- [ ] Experiment proposals are designed to resolve the ambiguity

---

## Edge Case: Product Discovery for a New Category

### Preconditions

- No directly comparable products exist for competitive analysis
- Product creates a new category or serves an unmet need

### Steps

| Step | Agent | Action | Expected Outcome |
|------|-------|--------|------------------|
| 1 | Primary Researcher | Researches adjacent categories and substitute products | Analysis of how users currently solve the problem |
| 2 | Coordinator | Frames research around jobs-to-be-done rather than product comparison | Updated protocol using JTBD framework |
| 3 | Usability Evaluator | Evaluates current workarounds and substitute products for friction | Understanding of current experience pain points |
| 4 | Feature Prioritizer | Prioritizes based on unmet needs rather than competitive parity | Needs-based prioritization rather than feature-matching |

### Validation Criteria

- [ ] Research frames the opportunity in terms of user needs, not product features
- [ ] Current workarounds and substitutes are analyzed
- [ ] Prioritization is based on user value, not competitive feature matching
- [ ] Recommendations identify the minimum viable experience to test demand

---

## Agents Responsible

| Agent | Responsibility |
|-------|---------------|
| **Coordinator** | Research protocol design, conflict resolution, actionability review |
| **Primary Researcher** | External research: benchmarks, best practices, competitor UX teardowns |
| **User Behavior Analyst** | Analytics interpretation: funnels, retention, feature adoption, cohorts |
| **Usability Evaluator** | Heuristic evaluation, friction identification, severity ranking |
| **Analyst** | Cross-referencing behavior and usability data, pattern identification |
| **Feature Prioritizer** | RICE scoring, opportunity assessment, backlog construction |
| **Synthesizer** | Product research report, experiment proposals, executive summary |
