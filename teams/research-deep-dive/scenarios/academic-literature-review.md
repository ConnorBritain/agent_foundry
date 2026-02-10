# Scenario: Academic Literature Review

This scenario defines the end-to-end flow for conducting a systematic or semi-systematic literature review, including source discovery, quality assessment, thematic synthesis, and gap analysis.

---

## Scenario Overview

| Property | Value |
|----------|-------|
| **Priority** | Critical |
| **Research Mode** | Academic or Literature Review |
| **Validated After** | Phase 5 |
| **Primary Agents** | Core team + Methodology Designer, Citation Manager, Peer Reviewer |
| **Estimated Duration** | ~120-180 minutes (hybrid mode, academic); ~60-90 minutes (literature review) |
| **Estimated Cost** | ~$35-60 (academic mode); ~$12-20 (literature review mode) |

---

## Success Path: Systematic Literature Review

### Preconditions

- Research question is defined and suitable for systematic review methodology
- Academic mode is enabled with citation style configured
- Target journal or format requirements are specified
- Inclusion and exclusion criteria are defined or will be developed in Phase 1
- arXiv and/or PubMed API access is configured (recommended)

### Steps

| Step | Agent | Action | Expected Outcome |
|------|-------|--------|------------------|
| 1 | Coordinator + Methodology Designer | Design review protocol: research question, search strategy, databases, inclusion/exclusion criteria, quality assessment framework | PRISMA-compliant review protocol |
| 2 | Primary Researcher (Round 1) | Systematic search across databases using protocol-defined keywords and Boolean operators | Initial source pool: 100-300 candidate papers |
| 3 | Primary Researcher | Screen titles and abstracts against inclusion/exclusion criteria | Filtered pool: 30-80 papers passing screening |
| 4 | Primary Researcher | Full-text review of filtered papers, quality assessment | Final included set: 15-40 papers with quality scores |
| 5 | Primary Researcher (Round 2) | Follow citation chains from included papers, check for missed sources | Additional 5-15 papers from backward/forward citation search |
| 6 | Analyst | Extract data from included papers, code themes, perform meta-analysis if applicable | Thematic data extraction table, statistical summaries |
| 7 | Peer Reviewer | Critique methodology, assess validity of synthesis approach | Methodology review with improvement suggestions |
| 8 | Synthesizer | Draft literature review paper with thematic narrative | Complete paper: introduction, methods, results, discussion, conclusion |
| 9 | Citation Manager | Format bibliography in target citation style, verify completeness | Properly formatted, deduplicated reference list |
| 10 | Coordinator | Final review for rigor, completeness, and publication readiness | GO decision with quality metrics |

### Validation Criteria

- [ ] Review protocol follows PRISMA guidelines (or equivalent framework)
- [ ] Search strategy is documented: databases, keywords, date range, filters
- [ ] Inclusion/exclusion criteria are explicit and applied consistently
- [ ] PRISMA flow diagram accounts for papers at each screening stage
- [ ] Quality assessment is performed for each included study
- [ ] Themes are identified from data, not imposed a priori
- [ ] All included papers are properly cited in the target citation style
- [ ] Research gaps are explicitly identified and discussed
- [ ] Limitations of the review itself are documented
- [ ] Conclusions follow from the synthesized evidence

---

## Edge Case: Insufficient Literature on the Topic

### Preconditions

- Fewer than 10 papers pass the inclusion criteria
- The topic is too new, too niche, or spans an unusual intersection of fields

### Steps

| Step | Agent | Action | Expected Outcome |
|------|-------|--------|------------------|
| 1 | Primary Researcher | Documents the scoping result: N papers found, N passing criteria | Scoping report with search documentation |
| 2 | Coordinator | Evaluates options: broaden search terms, expand date range, include grey literature, or accept limited scope | Decision on methodology adjustment |
| 3 | Coordinator | Escalates to user: "Only 7 papers meet criteria. Options: [list]" | User decides on adjusted scope |
| 4 | Synthesizer | If proceeding, frames the review as a scoping review or narrative review | Paper clearly states the limited evidence base |

### Validation Criteria

- [ ] Search effort is documented (not that sources do not exist, but where you looked)
- [ ] User is informed of the limited evidence before full analysis
- [ ] If proceeding, the paper type is adjusted to match the evidence base
- [ ] The insufficiency itself is treated as a finding worth reporting

---

## Edge Case: Contradictory Findings Across Studies

### Preconditions

- Multiple high-quality studies report conflicting results on the same question
- Contradictions cannot be attributed to methodology differences alone

### Steps

| Step | Agent | Action | Expected Outcome |
|------|-------|--------|------------------|
| 1 | Analyst | Identifies contradictions during data extraction and codes moderating factors | Contradiction map with potential moderators |
| 2 | Methodology Designer | Assesses whether contradictions stem from methodology differences | Methodology comparison table for conflicting studies |
| 3 | Peer Reviewer | Evaluates whether a meta-analysis with moderator analysis is appropriate | Recommendation on analysis approach |
| 4 | Synthesizer | Presents contradictions transparently with evidence for each position | Review paper clearly presents both sides with quality assessments |

### Validation Criteria

- [ ] Contradictions are identified and presented, not suppressed
- [ ] Methodological differences between conflicting studies are analyzed
- [ ] Moderating factors are explored (sample differences, measurement differences, context)
- [ ] The reader is equipped to evaluate the evidence strength for each position

---

## Success Path Variant: Semi-Systematic (Literature Review Mode)

For less formal reviews where full PRISMA compliance is not required:

| Step | Agent | Action | Expected Outcome |
|------|-------|--------|------------------|
| 1 | Coordinator | Design lightweight review protocol: question, search strategy, quality bar | Review protocol without PRISMA formality |
| 2 | Primary Researcher | Search web and academic databases, assess relevance | 15-30 relevant sources with assessments |
| 3 | Analyst | Thematic analysis of findings | Theme map with supporting evidence |
| 4 | Synthesizer | Draft review paper with narrative synthesis | Review document with findings, gaps, and recommendations |
| 5 | Coordinator | Quality review for evidence support and completeness | GO decision |

**Duration:** ~60-90 minutes. **Cost:** ~$12-20.

---

## Agents Responsible

| Agent | Responsibility |
|-------|---------------|
| **Coordinator** | Review protocol design, methodology oversight, final quality review |
| **Methodology Designer** | Review methodology specification, PRISMA compliance (academic mode) |
| **Primary Researcher** | Systematic source discovery, screening, quality assessment |
| **Analyst** | Data extraction, thematic coding, meta-analysis |
| **Peer Reviewer** | Methodology critique, synthesis validity assessment |
| **Synthesizer** | Literature review paper drafting |
| **Citation Manager** | Bibliography formatting and verification |
