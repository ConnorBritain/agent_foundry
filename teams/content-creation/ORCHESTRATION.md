# Multi-Agent Orchestration Protocol

This document defines the execution phases, communication protocols, quality gates, and decision-making framework for the Content Creation Team.

---

## Execution Modes

The team supports three execution modes. The mode is selected at runtime via the `--mode` flag.

### Sequential Mode ($10-25)

Agents execute one at a time in a defined order. Slowest but gives maximum editorial control at each stage.

```
Coordinator → Research Specialist → Content Drafter → Humanizer → Content Critic → Fact Checker → Format Specialist
```

**Total time:** 1.5-2.5 hours
**When to use:** Learning the pipeline, high-touch editorial control, when each agent's output needs user review before the next step.

### Hybrid Mode (Recommended -- $25-60)

Agents execute in parallel within phases but sequentially across phases. Quality gates between phases ensure coherence.

```
Phase 1 (parallel): Coordinator + Research Specialist
  ↓ [User Review Point]
Phase 2 (sequential): Content Drafter
  ↓
Phase 3 (parallel): Humanizer + Content Critic
  ↓
Phase 4 (sequential): Fact Checker
  ↓
Phase 5 (parallel): Coordinator + Format Specialist
  ↓ [User Review Point]
```

**Total time:** 45-75 minutes
**When to use:** Standard content production. Best balance of speed and quality.

### Swarm Mode ($60-150)

All agents run with continuous feedback loops. The Humanizer reviews sections as the Drafter produces them. The Critic provides real-time feedback. Fastest but consumes more tokens from increased inter-agent communication.

**Total time:** 20-40 minutes
**When to use:** Urgent publication deadlines, experienced users comfortable with less control.
**Warning:** Higher token usage from overlapping agent activity.

---

## Phase Definitions

### Phase 1: Vision + Research (Parallel -- ~10 minutes)

**Goal:** Establish the editorial direction and gather all supporting material before any writing begins.

#### Coordinator / Editor
- Parse the content configuration and validate all settings
- Define the editorial vision:
  - Content angle (what makes this piece worth reading)
  - Target audience profile (who, what they know, what they need)
  - Tone and voice parameters
  - Content structure (sections, approximate word allocation per section)
  - Success criteria (what does "good" look like for this piece)
- Produce the editorial vision document

**Outputs:**
- Editorial vision document
- Content structure outline

#### Research Specialist
- Begin gathering sources based on the content topic
- Search for statistics, data points, expert quotes, and case studies
- Evaluate source credibility and recency
- Identify counterarguments and nuances worth addressing
- Organize findings thematically for the Drafter

**Outputs:**
- Research brief with sourced findings
- Source list with credibility assessments
- Recommended angles based on research gaps

**Note:** The Research Specialist does not need the Coordinator's vision to begin gathering. Both work simultaneously. Their outputs merge before Phase 2.

#### User Review Point

```
Research and vision complete.
- Editorial angle: [description]
- Sources gathered: [count] ([high-relevance count] high-relevance)
- Key facts: [top 3-5 findings]
- Content structure: [section outline with word allocations]
- Estimated remaining cost: $XX.XX

Proceed to drafting? (yes / no / adjust angle)
```

---

### Phase 2: Drafting (Sequential -- ~15 minutes)

**Goal:** Produce a complete first draft that covers all key points from the research with proper narrative structure.

#### Content Drafter
- Consume the Coordinator's editorial vision and the Research Specialist's findings
- Write a complete first draft:
  - Follow the structure outline from the editorial vision
  - Incorporate facts, statistics, and quotes from the research brief
  - Use narrative structure with transitions between sections
  - Include concrete examples for abstract concepts
  - Embed inline citations
- Target the configured word count (within 10%)

**Outputs:**
- Complete first draft
- Draft metadata (word count, reading time, citation count)

**Depends on:** Phase 1 editorial vision and research brief.

---

### Phase 3: Humanize + Critique (Parallel -- ~15 minutes)

**Goal:** Simultaneously remove AI patterns and check style compliance. These two reviews do not conflict because they focus on different aspects.

#### Humanizer
- Read the complete draft
- Flag every AI writing pattern found (with specific quotes)
- Rewrite flagged sections in the configured style or user voice
- Ensure rewrites preserve factual accuracy and meaning
- Produce both the critique and the revised version

**Outputs:**
- AI pattern audit (flagged text with explanations)
- Revised content with patterns eliminated
- Pattern count per 1,000 words

#### Content Critic
- Read the complete draft
- Phase 1 (80%): Check against the style guide
  - Flag violations with `[STYLE]` prefix and specific rule citation
  - Severity: blocking, important, suggestion
- Phase 2 (20%): Provide editorial feedback
  - Flag suggestions with `[EDITORIAL]` prefix and reasoning
  - Assess: argument strength, engagement, clarity, examples, opening, conclusion

**Outputs:**
- Style violation report
- Editorial feedback report
- Overall quality score

**Note:** Humanizer and Critic work on the same draft simultaneously. Their feedback does not conflict because the Humanizer focuses on AI patterns and voice, while the Critic focuses on style rules and editorial quality.

---

### Phase 4: Fact-Check (Sequential -- ~5-10 minutes)

**Goal:** Verify all factual claims in the humanized version of the content.

#### Fact Checker
- Read the revised content (post-Humanizer)
- Verify every factual claim:
  - VERIFIED: confirmed with reliable source
  - LIKELY: consistent with known information but not independently verified
  - UNCERTAIN: cannot verify, recommend hedging or removal
  - FALSE: contradicted by reliable sources
  - OUTDATED: was true but no longer current
- Check statistics for misrepresentation
- Verify quotes are accurate and properly attributed
- Identify logical fallacies

**Outputs:**
- Claim verification report
- Correction recommendations
- Overall fact-check pass/fail

**Depends on:** Phase 3 humanized content (checks the version readers will see, not the original draft).

---

### Phase 5: Incorporate + Format (Parallel -- ~10 minutes)

**Goal:** Produce the final publication-ready content.

#### Coordinator / Editor
- Review all feedback from Humanizer, Critic, and Fact Checker
- Incorporate feedback into the final version:
  - Accept or reject Humanizer rewrites
  - Fix blocking style violations
  - Apply Fact Checker corrections
  - Address editorial suggestions that improve the piece
- Make the final publish/no-publish decision

**Outputs:**
- Final content version
- Publish decision with rationale

#### Format Specialist
- Apply platform-specific formatting
- Fix typography (em-dashes, curly quotes, proper ellipses)
- Verify heading hierarchy and list formatting
- Generate SEO metadata (if configured)
- Generate social preview text
- Final proofread for typos and formatting errors

**Outputs:**
- Formatted final content
- Platform metadata (SEO tags, social previews)

#### User Review Point

```
Content complete.
- Word count: [count] (target: [target])
- AI pattern score: [count] per 1,000 words [low/medium -- should be low]
- Style guide compliance: [percentage]%
- Fact-check results: [all verified / N issues resolved]
- Total cost: $XX.XX

Ready for publication.
Review final draft? (yes / publish / iterate on [section])
```

---

## Communication Protocol

### Message Types

| Type | Purpose | Example |
|------|---------|---------|
| `BRIEF` | Pass content brief or vision | Coordinator sends editorial vision to Drafter |
| `RESEARCH` | Deliver research findings | Research Specialist sends sources to Drafter |
| `DRAFT` | Deliver content draft | Drafter sends first draft to Humanizer and Critic |
| `REVIEW` | Deliver feedback | Humanizer sends AI pattern audit to Coordinator |
| `REVISION` | Deliver revised content | Coordinator sends final version to Format Specialist |
| `GATE` | Quality gate result | Coordinator reports phase result |
| `ESCALATE` | Escalate to user | Coordinator escalates unresolvable issue |

### Message Format

```yaml
type: DRAFT
from: content-drafter
to: [humanizer, content-critic]
phase: 2
subject: "First draft complete"
body: |
  First draft of "[content title]" is complete.
  Word count: 2,847 (target: 3,000)
  Sections: 6 (per editorial vision)
  Citations: 12 inline
attachments:
  - "drafts/v1-first-draft.md"
```

### Conflict Resolution

Content conflicts are rare because agents have non-overlapping responsibilities. When they occur:

1. **Humanizer vs Critic:** If the Humanizer's rewrite introduces a style violation, the Coordinator resolves by keeping the Humanizer's version and noting the style exception, or finding a version that satisfies both.
2. **Fact Checker vs Drafter:** Fact Checker always wins on factual claims. The Coordinator either corrects the text or removes the claim.
3. **Coordinator judgment:** The Coordinator is the final arbiter. Decisions are documented in the content metadata.

---

## Git Strategy

Content is primarily document-based, not code. The git strategy is simpler than code-focused teams.

### Branch Model

```
main
├── agent/editor/vision
├── agent/researcher/sources
├── agent/drafter/draft-v1
├── agent/humanizer/humanized
├── agent/critic/feedback
└── agent/formatter/final
```

Each agent commits to their branch. The Coordinator merges the final version to `main` after the publish decision.

### Commit Convention

```
<type>(<agent>): <subject>

<body>

Agent: <agent-name>
Phase: <phase-number>
```

Types: `draft`, `research`, `review`, `revision`, `format`, `publish`

Example:
```
review(humanizer): flag and rewrite AI patterns in v1 draft

- Flagged 7 AI patterns (3 structural, 4 word-level)
- Rewrote all flagged sections in conversational style
- AI pattern score reduced from 8.2 to 2.1 per 1,000 words

Agent: humanizer
Phase: 3
```

---

## Autonomous vs User-Prompted Decisions

### Autonomous (Coordinator Decides Without User Input)

The Coordinator can autonomously:
- Request additional research on a specific claim (cost < $5)
- Ask the Humanizer for a second pass on flagged sections (cost < $5)
- Merge Humanizer and Critic feedback when they do not conflict
- Fix minor formatting issues
- Adjust word allocation between sections (within 15% of plan)
- Reject a draft and request specific revisions from the Drafter
- **Cost limit:** <$10 per autonomous action

### User-Prompted (Require User Input)

The Coordinator must prompt the user before:
- Changing the editorial angle or target audience
- Removing a section from the planned structure
- Publishing or finalizing content
- Ignoring Fact Checker warnings (any FALSE or UNCERTAIN claims)
- Requesting major rewrites (more than 30% of content)
- Exceeding the configured cost budget by more than 15%
- Running more than 2 humanizer re-passes

**Prompt template:**
```
I recommend [action] because [reason].
- Cost: $X.XX
- Risk: [low/medium/high]
- Alternative: [other option]

Proceed? (yes / no / alternative)
```

---

## Scenario-Based Validation

After the final phase, the Coordinator validates against quality scenarios:

```yaml
content_quality_check:
  - name: "AI Pattern Score"
    criteria: "< 3 patterns per 1,000 words"
    blocking: true
  - name: "Style Compliance"
    criteria: ">= 95% compliance with style guide"
    blocking: true
  - name: "Fact-Check Pass"
    criteria: "0 FALSE claims, all UNCERTAIN claims hedged or removed"
    blocking: true
  - name: "Word Count"
    criteria: "Within 10% of target"
    blocking: false
  - name: "Readability"
    criteria: "Appropriate for target audience"
    blocking: false
convergence_threshold: 1.0  # All blocking criteria must pass
```

If blocking criteria are not met, the Coordinator either:
1. Runs another iteration (if within budget)
2. Escalates to the user with a specific remediation plan
