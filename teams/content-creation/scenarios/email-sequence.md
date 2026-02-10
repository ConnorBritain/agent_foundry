# Scenario: Email Sequence

This scenario defines the flow for producing a multi-email drip campaign with conversion optimization, consistent voice, and proper sequencing.

---

## Scenario Overview

| Property | Value |
|----------|-------|
| **Priority** | High |
| **Content Type** | Email drip sequence (4-8 emails) |
| **Validated After** | Phase 5 |
| **Primary Agents** | All 7 agents |
| **Estimated Duration** | ~40-60 minutes (hybrid mode) |
| **Estimated Cost** | ~$15-25 (default config) |

---

## Success Path: SaaS Onboarding Drip Sequence

### Preconditions

- Content brief specifies the product, target audience, and conversion goal
- Email count and sending cadence are defined (e.g., 6 emails over 14 days)
- Brand voice guidelines are configured
- Platform target is set to `email_html` with max-width and plain-text settings

### Steps

| Step | Agent | Action | Expected Outcome |
|------|-------|--------|------------------|
| 1 | Coordinator | Define sequence strategy: email purposes, progression arc, CTAs per email | Sequence brief with per-email goals, subject line direction, and CTA hierarchy |
| 2 | Research Specialist | Gather data on email benchmarks, competitor sequences, conversion patterns | Research brief with open rate benchmarks, CTA best practices, and relevant data |
| 3 | Content Drafter | Draft all emails maintaining progression and building toward conversion | Complete email sequence with subject lines, preheaders, body, and CTAs |
| 4 | Humanizer | Eliminate AI patterns; ensure each email sounds personal and direct | Revised emails that read like a real person wrote them individually |
| 5 | Content Critic | Check voice consistency across sequence; verify CTA clarity | Consistency report and per-email quality assessment |
| 6 | Fact Checker | Verify any claims about product, industry, or benchmarks | Fact-check report for data-driven claims in the sequence |
| 7 | Format Specialist | Format for email: inline CSS, responsive width, plain-text version | Email-ready HTML and plain-text versions for each email |

### Per-Email Validation

For each email in the sequence:
- [ ] Subject line is under 60 characters and avoids spam trigger words
- [ ] Preheader text complements the subject line (not repeats it)
- [ ] Body is under 300 words (for drip emails)
- [ ] Single clear CTA per email
- [ ] CTA button text is action-oriented ("Start your free trial" not "Click here")
- [ ] Unsubscribe link placeholder is present
- [ ] Plain-text version is readable and complete

### Sequence-Level Validation

- [ ] Emails progress logically (awareness -> value -> proof -> action)
- [ ] Voice is consistent across all emails
- [ ] CTAs escalate appropriately (soft ask -> hard ask)
- [ ] No email repeats content from a previous email
- [ ] AI pattern score < 3 per 1,000 words across all emails

---

## Edge Case: Sequence Too Long for Budget

### Preconditions

- Brief requests 8 emails but token budget only supports 5-6

### Steps

| Step | Agent | Action | Expected Outcome |
|------|-------|--------|------------------|
| 1 | Coordinator | Estimates token cost for 8 emails exceeds budget | Escalates to user with recommendation |
| 2 | Coordinator | Proposes: reduce to 6 emails or increase budget | User decides |
| 3 | Content Drafter | Drafts the agreed number of emails | Sequence covers essential progression within budget |

### Validation Criteria

- [ ] User was informed of budget constraint before drafting began
- [ ] Reduced sequence still covers the full progression arc
- [ ] No essential email purpose was dropped without user approval

---

## Edge Case: Subject Line A/B Variants

### Preconditions

- User requests A/B test variants for subject lines

### Steps

| Step | Agent | Action | Expected Outcome |
|------|-------|--------|------------------|
| 1 | Coordinator | Allocates token budget for 2 subject line variants per email | Budget updated |
| 2 | Content Drafter | Writes 2 subject line options per email with different approaches | Variant A: benefit-focused; Variant B: curiosity-focused (or similar split) |
| 3 | Humanizer | Reviews all variants for AI patterns | All variants sound natural |

### Validation Criteria

- [ ] Each variant pair uses meaningfully different approaches
- [ ] Both variants are under 60 characters
- [ ] Variants are labeled clearly for the user

---

## Agents Responsible

| Agent | Responsibility |
|-------|---------------|
| **Coordinator / Editor** | Sequence strategy, email progression design, publish decision |
| **Research Specialist** | Email benchmarks, conversion data, competitor analysis |
| **Content Drafter** | Email copy with subject lines, preheaders, bodies, and CTAs |
| **Humanizer** | AI pattern elimination, personal voice enforcement |
| **Content Critic** | Voice consistency, CTA clarity, brand compliance |
| **Fact Checker** | Verification of product claims and benchmark data |
| **Format Specialist** | Email HTML formatting, responsive design, plain-text fallback |
