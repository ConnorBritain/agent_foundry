# Content Creation Team -- Technical Specification

## Overview

This document defines the architecture, agent composition, responsibilities, deliverables, and quality standards for the Content Creation Team. The team is designed to produce publication-ready, research-backed content that avoids AI writing patterns and maintains consistent voice and style.

---

## 1. Team Composition

The team consists of 7 specialized agents. One operates on Opus 4.6 for editorial judgment and final authority. Four operate on Sonnet 4.5 for high-quality creative and analytical work. Two operate on Haiku 4.5 for efficient, pattern-based tasks.

### 1.1 Coordinator / Editor

- **Model:** Opus 4.6
- **Token budget:** ~30K tokens
- **Primary responsibilities:**
  - Receive the content brief and define the editorial vision
  - Decide the angle, target audience, tone, structure, and success criteria
  - Review all agent outputs against the editorial vision
  - Incorporate feedback from Humanizer, Critic, and Fact Checker into the final version
  - Make the publish/no-publish decision
  - Manage handoffs between phases
- **Decision authority:**
  - FINAL say on editorial angle, content structure, and publication readiness
  - Can reject any agent's output that does not meet the editorial vision
  - Escalates to user for: topic changes, audience changes, ignoring Fact Checker warnings
- **Outputs:**
  - Editorial vision document (angle, audience, tone, structure, success criteria)
  - Final content version with all feedback incorporated
  - Publish/no-publish decision with rationale

### 1.2 Research Specialist

- **Model:** Sonnet 4.5
- **Token budget:** ~40K tokens
- **Primary responsibilities:**
  - Gather supporting information for the content topic
  - Find statistics, data points, expert quotes, and case studies
  - Evaluate source credibility and recency
  - Identify counterarguments and nuances
  - Organize findings for the Drafter to consume
  - Provide properly formatted citations
- **Research standards:**
  - Every claim includes a source with URL, author, date, and publication
  - Primary sources preferred over secondary summaries
  - Data must be less than 2 years old unless historical context requires otherwise
  - Contested claims are flagged with competing perspectives
  - Sources are ranked by relevance and credibility
- **Outputs:**
  - Research brief with sourced facts, statistics, quotes, and counterarguments
  - Source list with credibility assessments
  - Recommended data visualizations or infographics

### 1.3 Content Drafter

- **Model:** Sonnet 4.5
- **Token budget:** ~60K tokens
- **Primary responsibilities:**
  - Create a complete first draft using the editorial vision and research brief
  - Structure content with narrative arcs, not just information lists
  - Use concrete examples to illustrate abstract concepts
  - Include all required sections from the editorial vision
  - Embed citations from the research brief
  - Produce a draft that is complete but not polished (polish comes later)
- **Drafting standards:**
  - Adapts tone to content type (blog, whitepaper, technical doc, email)
  - Prioritizes completeness over perfection in first drafts
  - Uses narrative structure (not just header-list-header-list)
  - Includes transitions between sections
  - Meets word count targets within 10%
- **Outputs:**
  - Complete first draft with all sections
  - Inline citations from research
  - Draft metadata (word count, reading time, section breakdown)

### 1.4 Humanizer

- **Model:** Sonnet 4.5
- **Token budget:** ~50K tokens
- **Primary responsibilities:**
  - Identify and eliminate AI writing patterns in the draft
  - Apply the selected writing style or match user voice samples
  - Rewrite flagged sections while preserving meaning and accuracy
  - Produce both a critique (what was wrong) and a revised version
  - Ensure varied sentence rhythm and natural voice
- **AI pattern detection:**
  - Structural patterns: "It's not X, it's Y" constructions, list-heavy responses, three-point structures, question-then-answer openings, unwarranted CTAs
  - Word-level patterns: delve, leverage, tapestry, landscape, ecosystem, journey, transformative, robust, comprehensive, multifaceted, nuanced, paradigm, synergy, holistic, streamline, cutting-edge, game-changer, empower, unlock, navigate, realm, foster, harness, pivotal, dynamic, innovative, revolutionize, seamless, cornerstone
  - Rhythm patterns: mechanical sentence rhythm, alternating short-long patterns, every paragraph starting with topic sentence, abstract nouns over concrete verbs, unnecessary passive voice
  - Tone patterns: relentlessly positive tone, false balance, corporate-speak, condescending explanations
- **Outputs:**
  - AI pattern audit (flagged text with explanations)
  - Revised content with patterns eliminated
  - Voice match score (if user samples provided)

### 1.5 Content Critic

- **Model:** Sonnet 4.5
- **Token budget:** ~50K tokens
- **Primary responsibilities:**
  - Phase 1 (80%): Enforce the style guide with specific violation citations
  - Phase 2 (20%): Provide subjective editorial feedback
  - Flag violations with severity levels (blocking, important, suggestion)
  - Assess argument strength, engagement, and clarity
- **Style enforcement checks:**
  - Terminology consistency (product names, technical terms, branded language)
  - Formatting rules (headings, lists, code blocks, emphasis)
  - Citation format compliance
  - Link hygiene (no broken links, appropriate anchor text)
  - Accessibility (alt text, heading hierarchy, reading level)
  - Platform requirements (word count, meta descriptions, SEO)
  - Voice and tone consistency
  - Grammar and punctuation standards
- **Outputs:**
  - Style violation report with `[STYLE]` prefixed items and rule citations
  - Editorial feedback report with `[EDITORIAL]` prefixed suggestions
  - Overall quality score (pass/conditional pass/fail)

### 1.6 Fact Checker

- **Model:** Haiku 4.5
- **Token budget:** ~20K tokens
- **Primary responsibilities:**
  - Verify every factual claim in the content
  - Assess claims as: VERIFIED, LIKELY, UNCERTAIN, FALSE, or OUTDATED
  - Provide citations for corrections
  - Check statistics for accuracy and proper context
  - Verify quotes are accurate and properly attributed
  - Identify logical fallacies and non sequiturs
- **Verification standards:**
  - Every claim gets a confidence rating
  - FALSE claims include correction and source
  - OUTDATED claims include updated information
  - UNCERTAIN claims recommend hedging language or removal
  - Statistics checked for misrepresentation or cherry-picking
- **Outputs:**
  - Claim verification report (each claim with status and source)
  - Correction recommendations
  - Overall fact-check pass/fail

### 1.7 Format Specialist

- **Model:** Haiku 4.5
- **Token budget:** ~10K tokens
- **Primary responsibilities:**
  - Fix typography (em-dashes, en-dashes, curly quotes, proper ellipses)
  - Ensure consistent formatting (heading levels, list styles, code blocks)
  - Optimize for target platform (SEO meta descriptions, social preview text)
  - Verify visual hierarchy (paragraph spacing, section breaks, pull quotes)
  - Final proofread (typos, double spaces, orphaned words)
  - Cross-reference checks (TOC matches headings, internal links work)
- **Formatting standards:**
  - Platform-specific optimization (WordPress, Medium, Ghost, Notion, email)
  - Consistent heading hierarchy (no skipped levels)
  - Proper list formatting (parallel structure, consistent punctuation)
  - Image alt text present for all images
- **Outputs:**
  - Formatted final content
  - Platform-specific metadata (SEO tags, social previews)
  - Formatting change log

---

## 2. Content Pipeline Specification

### 2.1 Input Requirements

| Input | Required | Description |
|-------|----------|-------------|
| Content brief | Yes | Topic, purpose, target audience, desired length |
| Style guide | Recommended | Terminology, formatting rules, tone guidelines |
| Writing samples | Optional | 2-5 samples from target author for voice matching |
| Brand guidelines | Optional | Brand voice, terminology, visual identity notes |
| Target platform | Recommended | WordPress, Medium, email, social, etc. |
| Keywords/SEO targets | Optional | Primary and secondary keywords for SEO content |

### 2.2 Output Artifacts

| Artifact | Format | Description |
|----------|--------|-------------|
| Final content | Markdown, HTML, or platform-specific | Publication-ready content |
| Research brief | Markdown | Sources, statistics, and citations used |
| AI pattern audit | Markdown | Patterns found and how they were fixed |
| Style compliance report | Markdown | Style guide violations found and resolved |
| Fact-check report | Markdown | Every claim with verification status |
| Content metadata | YAML | Word count, reading time, keywords, SEO tags |

---

## 3. Token Budget

### 3.1 Budget by Agent

| Agent | Model | Est. Tokens | Est. Cost |
|-------|-------|-------------|-----------|
| Coordinator / Editor | Opus 4.6 | ~30K | ~$4.50 |
| Research Specialist | Sonnet 4.5 | ~40K | ~$2.40 |
| Content Drafter | Sonnet 4.5 | ~60K | ~$3.60 |
| Humanizer | Sonnet 4.5 | ~50K | ~$3.00 |
| Content Critic | Sonnet 4.5 | ~50K | ~$3.00 |
| Fact Checker | Haiku 4.5 | ~20K | ~$0.50 |
| Format Specialist | Haiku 4.5 | ~10K | ~$0.25 |
| **Total** | | **~260K** | **~$17.25** |

Note: Estimates include a base long-form article. Actual costs vary by content type and length. A 20% buffer (~$3.50) is recommended for iteration, bringing the effective total to approximately $21.

### 3.2 Budget by Phase

| Phase | Duration | Agents | Tokens | Cost |
|-------|----------|--------|--------|------|
| Vision + Research | ~10 min | 2 parallel | ~70K | ~$7 |
| Drafting | ~15 min | 1 | ~60K | ~$4 |
| Humanize + Critique | ~15 min | 2 parallel | ~100K | ~$6 |
| Fact-Check | ~5-10 min | 1 | ~20K | ~$0.50 |
| Incorporate + Format | ~10 min | 2 parallel | ~10K | ~$0.75 |
| **Total** | **~55-60 min** | | **~260K** | **~$18.25** |

---

## 4. Quality Standards

### 4.1 AI Pattern Score

- Target: fewer than 3 AI patterns per 1,000 words
- Measured by: Humanizer analysis pass
- Blocking: content with more than 5 patterns per 1,000 words is rejected

### 4.2 Style Guide Compliance

- Target: 95% or higher compliance rate
- Measured by: Critic Phase 1 pass rate
- Blocking violations must be fixed before publication

### 4.3 Fact-Check Pass Rate

- Target: 100% of claims VERIFIED or appropriately hedged
- Any FALSE claims are blocking
- UNCERTAIN claims must be hedged or removed

### 4.4 Word Count Accuracy

- Target: within 10% of the brief's target word count
- Measured by: Format Specialist final count

### 4.5 Readability

- Target: appropriate for the target audience
- Measured by: Flesch-Kincaid or equivalent readability score
- Technical content: grade level 12-16
- General audience: grade level 8-10
- Consumer content: grade level 6-8

### 4.6 Budget Adherence

- Target: actual cost within 20% of estimated cost
- Measured by: token usage tracking per agent
