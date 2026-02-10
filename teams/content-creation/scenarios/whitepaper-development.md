# Scenario: White Paper Development

This scenario defines the end-to-end flow for producing a research-intensive white paper with executive-level quality, proper citations, and data-driven arguments.

---

## Scenario Overview

| Property | Value |
|----------|-------|
| **Priority** | High |
| **Content Type** | White paper (4,000-8,000 words) |
| **Validated After** | Phase 5 |
| **Primary Agents** | All 7 agents (Premium config recommended) |
| **Estimated Duration** | ~90-120 minutes (hybrid mode) |
| **Estimated Cost** | ~$35-45 (default), ~$55-70 (premium) |

---

## Success Path: Data-Driven Industry White Paper

### Preconditions

- Content brief specifies thesis, target executive audience, and industry vertical
- Research depth is set to "deep" in configuration
- Style guide includes formal tone, third-person voice, academic citation format
- Maximum word count is configured between 4,000-8,000

### Steps

| Step | Agent | Action | Expected Outcome |
|------|-------|--------|------------------|
| 1 | Coordinator | Define editorial vision with thesis-driven structure | Vision includes: executive summary, problem statement, analysis sections, methodology, conclusions, recommendations |
| 2 | Research Specialist | Deep research with 15-25 sources | Research brief with peer-reviewed studies, industry reports, government data |
| 3 | Coordinator | Review research depth and thesis support | Gate 1 PASS: research supports thesis with sufficient evidence |
| 4 | Content Drafter | Write complete draft with formal structure | Draft with executive summary, numbered sections, embedded citations, data tables |
| 5 | Humanizer | Pattern elimination with formal voice preservation | Revised content maintaining authoritative tone without AI patterns |
| 6 | Content Critic | Enforce academic/formal style compliance | Style compliance >= 95%, citation format verified |
| 7 | Fact Checker | Verify all statistics, study citations, and data claims | 0 FALSE claims, all data points traced to primary sources |
| 8 | Coordinator | Incorporate feedback, finalize executive summary | Publication-ready white paper with all feedback addressed |
| 9 | Format Specialist | Apply formatting, generate metadata | Properly formatted document with table of contents anchors |

### Validation Criteria

- [ ] Executive summary stands alone as a coherent overview (300-500 words)
- [ ] Thesis is stated clearly in the introduction and supported throughout
- [ ] All statistics cite primary sources (not secondary summaries)
- [ ] Word count within 10% of target
- [ ] AI pattern score < 3 per 1,000 words
- [ ] Formal tone maintained throughout (no casual language)
- [ ] Conclusions follow directly from presented evidence
- [ ] Recommendations are specific and actionable

---

## Edge Case: Contradictory Research Findings

### Preconditions

- Research Specialist finds credible sources that disagree on a key claim

### Steps

| Step | Agent | Action | Expected Outcome |
|------|-------|--------|------------------|
| 1 | Research Specialist | Flags contradictory findings in research brief | Both positions documented with source credibility assessments |
| 2 | Coordinator | Decides: present both perspectives, favor stronger evidence, or escalate | Editorial vision updated to include counterargument section |
| 3 | Content Drafter | Drafts section presenting both perspectives fairly | Reader can evaluate both positions based on presented evidence |
| 4 | Fact Checker | Verifies both sets of claims independently | Each claim verified against its own source |

### Validation Criteria

- [ ] Contradictory evidence is presented, not suppressed
- [ ] Stronger evidence is given appropriate weight without dismissing weaker position
- [ ] Reader is equipped to form their own conclusion

---

## Edge Case: Word Count Significantly Over Target

### Preconditions

- First draft exceeds target word count by more than 15%

### Steps

| Step | Agent | Action | Expected Outcome |
|------|-------|--------|------------------|
| 1 | Content Drafter | Delivers draft at 9,200 words (target: 7,000) | Draft metadata flags the overage |
| 2 | Coordinator | Reviews section-by-section word allocation | Identifies sections that exceeded allocation |
| 3 | Coordinator | Requests Drafter to tighten specific sections with guidance | Revised draft within 10% of target |

### Validation Criteria

- [ ] Coordinator identifies which sections are over allocation
- [ ] Cuts preserve the argument structure and evidence
- [ ] No citations or key data points are lost in trimming

---

## Agents Responsible

| Agent | Responsibility |
|-------|---------------|
| **Coordinator / Editor** | Thesis-driven editorial vision, structural review, publish decision |
| **Research Specialist** | Deep research with academic and industry sources |
| **Content Drafter** | Formal first draft with data tables and citations |
| **Humanizer** | Pattern elimination while preserving authoritative voice |
| **Content Critic** | Academic style enforcement and argument assessment |
| **Fact Checker** | Verification of all statistics and study citations |
| **Format Specialist** | Table of contents, formal formatting, metadata |
