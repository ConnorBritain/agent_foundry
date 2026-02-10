# Scenario: Blog Post Creation

This scenario defines the end-to-end flow for producing a research-backed, SEO-optimized blog post. It validates the complete content pipeline from brief to publication-ready output.

---

## Scenario Overview

| Property | Value |
|----------|-------|
| **Priority** | Critical |
| **Content Type** | Long-form blog post (2,500-3,500 words) |
| **Validated After** | Phase 5 |
| **Primary Agents** | All 7 agents |
| **Estimated Duration** | ~55-60 minutes (hybrid mode) |
| **Estimated Cost** | ~$21 (default config) |

---

## Success Path: SEO Blog Post with Research

### Preconditions

- Content brief specifies topic, audience, and target keywords
- Style guide is configured with brand terminology and formatting rules
- Web search API key is set and has available quota
- Target platform is configured (WordPress, Markdown, or other)

### Steps

| Step | Agent | Action | Expected Outcome |
|------|-------|--------|------------------|
| 1 | Coordinator | Parse config, validate settings | Editorial vision document with angle, audience, structure, success criteria |
| 2 | Research Specialist | Gather sources on topic | Research brief with 10-15 sourced findings, credibility assessments |
| 3 | Coordinator | Review research, confirm angle | Gate 1 PASS: research supports editorial angle |
| 4 | Content Drafter | Write first draft using vision and research | Complete draft within 10% of word count target, all citations embedded |
| 5 | Humanizer | Flag and rewrite AI patterns | AI pattern audit with < 3 patterns per 1,000 words in revised version |
| 6 | Content Critic | Check style guide compliance | Style compliance >= 95%, 0 blocking violations |
| 7 | Fact Checker | Verify all claims | 0 FALSE claims, all UNCERTAIN claims flagged |
| 8 | Coordinator | Incorporate all feedback | Final content with all blocking issues resolved |
| 9 | Format Specialist | Apply platform formatting, generate metadata | Publication-ready content with SEO tags and social previews |

### Validation Criteria

- [ ] Word count within 10% of target
- [ ] AI pattern score < 3 per 1,000 words
- [ ] Style guide compliance >= 95%
- [ ] 0 FALSE claims in fact-check report
- [ ] All UNCERTAIN claims hedged or removed
- [ ] SEO meta description present and within character limit
- [ ] Primary keyword appears in title, H2, and body
- [ ] All citations include URL, author, date, and publication
- [ ] Content reads naturally from start to finish (human judgment)

---

## Edge Case: Research Returns Insufficient Sources

### Preconditions

- Topic is niche or very recent with limited available data

### Steps

| Step | Agent | Action | Expected Outcome |
|------|-------|--------|------------------|
| 1 | Research Specialist | Searches yield < 5 credible sources | Research brief flags gaps explicitly |
| 2 | Coordinator | Reviews thin research | Escalates to user: "Insufficient research for a data-driven article" |
| 3 | User | Decides: narrow the angle, provide sources, or proceed with caveats | Updated brief or proceed decision |
| 4 | Content Drafter | Drafts with available research, uses hedging language for unsupported claims | Draft clearly marks which sections have strong vs weak evidence |

### Validation Criteria

- [ ] Research gaps are explicitly documented
- [ ] User was prompted before proceeding with limited data
- [ ] Unsupported claims use hedging language ("reportedly," "according to limited data")

---

## Edge Case: Humanizer Cannot Reduce Patterns Below Threshold

### Preconditions

- First draft has > 5 AI patterns per 1,000 words
- First Humanizer pass reduces to 4.2 per 1,000 words (still above threshold of 3)

### Steps

| Step | Agent | Action | Expected Outcome |
|------|-------|--------|------------------|
| 1 | Humanizer | First pass: 8.5 reduced to 4.2 patterns per 1,000 words | Audit shows remaining patterns |
| 2 | Coordinator | Within iteration budget, requests second Humanizer pass | Second pass assigned |
| 3 | Humanizer | Second pass: 4.2 reduced to 2.8 patterns per 1,000 words | Below threshold, proceed |

If still above threshold after max iterations:
| 4 | Coordinator | Escalates to user | "AI pattern score is 3.5 after 2 passes. Proceed or request manual edit?" |

### Validation Criteria

- [ ] Multiple passes stay within configured `iteration_budget`
- [ ] Each pass shows measurable improvement in pattern score
- [ ] User is prompted if threshold cannot be met within budget

---

## Agents Responsible

| Agent | Responsibility |
|-------|---------------|
| **Coordinator / Editor** | Editorial vision, feedback incorporation, publish decision |
| **Research Specialist** | Source gathering and credibility assessment |
| **Content Drafter** | First draft with citations and narrative structure |
| **Humanizer** | AI pattern elimination and voice matching |
| **Content Critic** | Style guide enforcement and editorial feedback |
| **Fact Checker** | Claim verification |
| **Format Specialist** | Platform formatting and SEO metadata |
