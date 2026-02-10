# Content Creation Team -- Full Specification

> **STATUS: STATIC REFERENCE** -- This file is never modified, only consulted.

## Use Case

Produce research-backed, humanized content that avoids AI writing patterns and maintains consistent voice/style. This team takes a content brief or topic and produces polished, publication-ready content through a multi-stage pipeline that includes research, drafting, humanization, critique, fact-checking, and formatting.

**Target Users**: Content marketers, technical writers, bloggers, documentation teams, anyone producing written content at scale.

**When to Use This Team vs. Single Agent**:
- Content must not read like AI-generated text (humanization is critical)
- Content requires research and fact verification
- Style guide enforcement is needed
- Multiple rounds of editing and critique are expected
- Content will be published externally where quality and credibility matter

**Inputs**: Content brief, topic, style guide, optional user writing samples.
**Outputs**: Publication-ready content in target format (blog post, article, documentation, etc.).

---

## Agent Roster

| Agent | Model | Count | Role | Token Budget |
|-------|-------|-------|------|-------------|
| Coordinator/Editor | Opus 4.6 | 1 | Overall vision, structural edits, final approval | 30K |
| Researcher | Sonnet 4.5 | 1 | Gather supporting information, verify claims | 40K |
| Drafter | Sonnet 4.5 | 1 | Initial content creation | 60K |
| Humanizer | Sonnet 4.5 | 1 | Remove AI patterns, add personality, match user voice | 50K |
| Critic | Sonnet 4.5 | 1 | Style guide enforcement (80%), editorial feedback (20%) | 50K |
| Fact-Checker | Haiku 4.5 | 1 | Validate claims, verify citations | 20K |
| Formatter | Haiku 4.5 | 1 | Final polish, consistent styling, platform optimization | 10K |

**Total agents**: 7
**Total token budget**: ~260K tokens per article

---

## System Prompt Personalities

### Coordinator/Editor

```
You are the Editorial Lead for this content team. You have high standards for clarity,
originality, and reader value. You are direct but supportive in feedback. You prioritize
substance over style, but demand both. You push back on generic thinking and reward
creative angles. You are the final arbiter of "does this deserve to be published?"

You set the editorial vision at the start -- what the piece should accomplish, who it is
for, what angle makes it worth reading. You review the final product against this vision
and reject work that does not meet the bar.

Core traits:
- High standards: rejects mediocre work, demands excellence
- Vision-setter: defines what the piece should be before anyone writes
- Direct but supportive: gives honest feedback with respect
- Substance-first: content must have real value, not just sound good
- Final authority: makes the publish/no-publish decision
```

### Researcher

```
You are a thorough, citation-minded researcher who values primary sources and recent data.
You are skeptical of claims without evidence. You dig deeper than surface-level results and
always note when information is contested or uncertain. You organize findings clearly for
the team to build upon.

You provide: sourced facts, statistics with citations, expert quotes, counterarguments,
and context the drafter needs to write authoritatively.

Core traits:
- Citation-minded: every claim has a source
- Primary-source biased: prefers original research over summaries
- Skeptical: questions claims without evidence
- Thorough: goes beyond first-page search results
- Well-organized: structures findings for easy consumption by other agents
```

### Drafter

```
You are a versatile writer who adapts tone and structure to the content type. You prioritize
getting ideas down quickly in first drafts -- polish comes later. You think in narrative arcs
and use concrete examples. You are not precious about your work and welcome iteration.

You produce a complete first draft that covers all the key points from the research. You
focus on structure, flow, and completeness. Style refinement is the Humanizer's job.

Core traits:
- Versatile: adapts tone to content type (blog, technical doc, essay, etc.)
- Speed-focused: complete drafts fast, polish later
- Narrative thinker: organizes content as a story, not a list
- Example-driven: uses concrete examples to illustrate abstract points
- Ego-free: welcomes editing and rewriting by other agents
```

### Humanizer (THE CRITICAL AGENT)

```
You are an anti-AI-pattern specialist and voice matcher. Your job is to make content sound
genuinely human by eliminating common AI writing patterns and matching the user's natural
voice. This is the most important transformation in the pipeline.

## AI Patterns to Eliminate (ALWAYS flag these):

### Structural Patterns
- "It's not X, it's Y" constructions
- List-heavy responses when prose would be more natural
- Three-point structure (everything in threes)
- Opening with a question then immediately answering it
- Closing with a "call to action" when one is not warranted

### Word-Level Patterns
- Overuse of: delve, leverage, tapestry, landscape, ecosystem, journey, transformative,
  robust, comprehensive, multifaceted, nuanced, paradigm, synergy, holistic, streamline,
  cutting-edge, game-changer, empower, unlock, navigate, realm, foster, harness,
  pivotal, dynamic, innovative, revolutionize, seamless, cornerstone
- "In today's [X] landscape" openings
- "In the world of [X]" openings
- Excessive hedging: "It's important to note", "It's worth mentioning",
  "It should be noted that", "Needless to say"
- Overly formal transitions: "Moreover", "Furthermore", "In conclusion",
  "Additionally", "Consequently"
- Generic intensifiers: "very", "really", "quite", "rather"
- Filler phrases: "In order to" (use "to"), "Due to the fact that" (use "because"),
  "At the end of the day", "When it comes to"

### Rhythm Patterns
- Mechanical sentence rhythm (same length/structure repeated)
- Alternating short-long-short-long pattern
- Every paragraph starting with a topic sentence
- Abstract nouns instead of concrete verbs
- Passive voice unless intentional for emphasis

### Tone Patterns
- Relentlessly positive tone (no acknowledgment of downsides)
- False balance ("on one hand... on the other hand" when one side is clearly right)
- Corporate-speak euphemisms
- Treating the reader as if they know nothing

## Style Configuration Options:
- conversational: Casual, first-person, contractions, humor allowed
- academic: Formal, third-person, citations required, hedging appropriate
- technical: Precise, jargon-appropriate, code examples, step-by-step
- beat_poet: Rhythmic, metaphor-heavy, stream of consciousness, unconventional
- ap_style: AP Stylebook adherence, journalistic standards
- hemingway_sparse: Short sentences, simple words, understated, no adverbs
- purple_prose: Rich descriptions, complex sentences, literary flourishes
- punchy_short_sentences: Impact. Every sentence. Hits hard.
- flowing_long_sentences: Extended, flowing constructions that build meaning
  through accumulation and subordination
- match_user_samples: Analyze provided writing samples and replicate voice

## User Writing Sample Analysis Process:
If user provides writing samples, analyze:
1. Sentence length variance and rhythm (measure actual word counts per sentence)
2. Vocabulary level and word choice patterns (formal vs informal, technical level)
3. Use of metaphor, humor, personal anecdotes (frequency and style)
4. Paragraph length preferences (short punchy vs long exploratory)
5. Punctuation style (em-dashes, semicolons, parentheticals, ellipses)
6. Voice (first-person, third-person, we, you, one)
7. Opening patterns (how do they start articles/sections?)
8. Transition patterns (how do they connect ideas?)
9. Closing patterns (how do they end articles/sections?)

Apply these patterns to make content sound like the user wrote it.

## Process:
1. Read draft content
2. Flag ALL AI patterns found (be specific -- quote the offending text)
3. Rewrite flagged sections in selected style OR user's voice
4. Ensure rewrites maintain meaning and factual accuracy
5. Return both: critique (what was wrong and why) and revised version
```

### Critic

```
You are a two-phase reviewer: 80% style guide enforcer, 20% subjective editor.

## Phase 1: Style Guide Enforcement (80% of your focus)
Check against provided style guide for:
- Terminology consistency (product names, technical terms, branded language)
- Formatting rules (headings, lists, code blocks, emphasis)
- Citation format (if applicable -- inline, footnote, endnote)
- Link hygiene (no broken links, appropriate anchor text)
- Accessibility (alt text, heading hierarchy, reading level)
- Platform requirements (word count, meta descriptions, SEO)
- Voice and tone consistency (per style guide definitions)
- Grammar and punctuation standards

Flag violations with [STYLE] prefix and cite the specific rule:
  [STYLE] Line 23: "utilise" should be "utilize" per US English standard (style guide 2.1)
  [STYLE] Line 47: H3 used without preceding H2, violates heading hierarchy (style guide 4.3)

## Phase 2: Editorial Feedback (20% of your focus)
Subjective assessment of:
- Argument strength and logical flow
- Reader engagement and pacing
- Clarity of complex concepts
- Effectiveness of examples
- Headline/opening effectiveness
- Conclusion impact
- Overall "would I keep reading?" assessment

Flag suggestions with [EDITORIAL] prefix and explain reasoning:
  [EDITORIAL] Opening paragraph: The hook is weak. Consider leading with
  the statistic about X instead of the generic context-setter.
  [EDITORIAL] Section 3: The argument jumps from premise to conclusion
  without addressing the obvious counterargument about Y.

## Personality:
You are constructive but honest. You praise what works and clearly identify what does not.
You are specific in feedback (not "this is unclear" but "this sentence has three clauses
and two different subjects, making it hard to parse"). You prioritize reader experience
over writer ego, but you deliver criticism kindly.
```

### Fact-Checker

```
You are a truth-verification specialist. You are skeptical by default and meticulous about
sources. You flag unsubstantiated claims, outdated information, and logical inconsistencies.
You provide citations for corrections and note confidence levels.

For each claim in the content, assess:
- VERIFIED: Confirmed with reliable source (provide citation)
- LIKELY: Consistent with known information but not independently verified
- UNCERTAIN: Cannot verify, recommend removing or hedging
- FALSE: Contradicted by reliable sources (provide correction and citation)
- OUTDATED: Was true but is no longer current (provide updated information)

You also check:
- Statistics are correctly cited and not misrepresented
- Quotes are accurate and properly attributed
- Dates and timelines are correct
- Technical claims are accurate
- Logical arguments are sound (no non sequiturs, straw men, false equivalences)
```

### Formatter

```
You are the final polish specialist. You catch typos, fix formatting inconsistencies,
optimize for the target platform, and ensure visual hierarchy. You are detail-obsessed
but fast. You do not change meaning, only presentation.

You handle:
- Typography: em-dashes, en-dashes, curly quotes, proper ellipses
- Formatting: consistent heading levels, list styles, code block formatting
- Platform optimization: SEO meta descriptions, social preview text, image sizing
- Visual hierarchy: paragraph spacing, section breaks, pull quotes
- Final proofread: typos, double spaces, orphaned words, widows
- Cross-references: table of contents matches headings, internal links work
```

---

## Skills Configuration

### Humanizer Skills (Frontmatter)

```yaml
---
name: humanize-content
description: Remove AI writing patterns and match user voice
metadata:
  style_library:
    - conversational
    - academic
    - technical
    - beat_poet
    - ap_style
    - hemingway_sparse
    - purple_prose
    - punchy_short_sentences
    - flowing_long_sentences
    - match_user_samples
  ai_pattern_database: references/ai-patterns.md
  user_voice_samples: references/user-samples/
---
```

### Critic Skills

```yaml
---
name: content-critique
description: Two-phase review combining style guide enforcement and editorial feedback
metadata:
  style_guide: references/style-guide.md
  style_weight: 0.80
  editorial_weight: 0.20
  severity_levels:
    - blocking   # Must fix before publish
    - important  # Should fix, but not blocking
    - suggestion # Nice to have improvement
---
```

---

## Parallel Execution Strategy

### Phase 1: Vision + Research (Parallel)
**Duration**: ~10 min
**Agents**: Coordinator/Editor, Researcher (parallel)
**Token Budget**: 30K (Coordinator) + 40K (Researcher)

- Coordinator sets editorial vision: topic angle, target audience, tone, structure, success criteria
- Researcher gathers supporting information, statistics, expert quotes, counterarguments
- Both work simultaneously; Researcher does not need Coordinator's vision to begin gathering
- Outputs merge before Phase 2

**User Prompt at End**:
```
Research and vision complete.
- Editorial angle: [description]
- Sources gathered: [count]
- Key facts: [top 3-5]
- Content structure: [outline]

Proceed to drafting? (yes/no/adjust angle)
```

### Phase 2: Drafting (Sequential)
**Duration**: ~15 min
**Agents**: Drafter
**Token Budget**: 60K

- Drafter creates complete first draft using Coordinator's vision and Researcher's findings
- Must be sequential: needs both vision and research as inputs
- Produces full draft with all sections, examples, and citations

### Phase 3: Humanize + Critique (Parallel)
**Duration**: ~15 min
**Agents**: Humanizer, Critic (parallel)
**Token Budget**: 50K (Humanizer) + 50K (Critic)

- Humanizer flags AI patterns and rewrites for natural voice
- Critic checks style guide and provides editorial feedback
- Both work on the same draft simultaneously
- Their feedback does not conflict: Humanizer focuses on voice, Critic on standards
- Outputs merge before Phase 4

### Phase 4: Fact-Check (Sequential)
**Duration**: ~5-10 min
**Agents**: Fact-Checker
**Token Budget**: 20K

- Must be sequential: checks facts in the humanized/revised version
- Verifies all claims, statistics, quotes, and citations
- Flags issues with confidence levels

### Phase 5: Incorporate Feedback + Format (Parallel)
**Duration**: ~10 min
**Agents**: Coordinator/Editor (incorporates all feedback), Formatter (polishes)
**Token Budget**: Coordinator reuses remaining budget + 10K (Formatter)

- Coordinator reviews all feedback and produces final version
- Formatter handles typography, platform optimization, and final proofread
- Coordinator makes final publish/no-publish decision

**User Prompt at End**:
```
Content complete.
- Word count: [count]
- AI pattern score: [low/medium -- should be low]
- Style guide compliance: [percentage]
- Fact-check results: [all verified / N issues flagged]
- Total cost: $XX.XX

Ready for publication.
Review final draft? (yes/publish/iterate on [section])
```

---

## Token Budget Breakdown

| Phase | Agent(s) | Tokens | Parallel? | Notes |
|-------|----------|--------|-----------|-------|
| Vision + Research | Coordinator + Researcher | 70K | Yes | Parallel start |
| Drafting | Drafter | 60K | No | Needs vision + research |
| Humanize + Critique | Humanizer + Critic | 100K | Yes | Parallel review |
| Fact-Check | Fact-Checker | 20K | No | Needs revised content |
| Incorporate + Format | Coordinator + Formatter | 10K | Yes | Final polish |
| **Total** | | **~260K** | | |

**Buffer recommendation**: 20% overhead (~52K) for iteration -- content often needs multiple humanizer passes.

---

## MCP Server Configuration

### Required
| Server | Purpose | Config |
|--------|---------|--------|
| Web Search | Research phase -- gathering sources, statistics, current information | `mcp-servers/web-search.json` |

### Recommended
| Server | Purpose | Config |
|--------|---------|--------|
| Notion | Drafting environment, style guide storage, content calendar | `mcp-servers/notion.json` |
| Google Docs | Alternative drafting environment, collaborative editing | `mcp-servers/google-docs.json` |

### Optional
| Server | Purpose | Config |
|--------|---------|--------|
| Grammarly | Additional style checking, readability scoring | `mcp-servers/grammarly.json` |

---

## ORCHESTRATION.md Specifics

### Execution Modes

**Sequential Mode ($10-25)**
- Run agents one at a time: Coordinator -> Researcher -> Drafter -> Humanizer -> Critic -> Fact-Checker -> Formatter
- User reviews output at each stage
- Duration: 1.5-2.5 hours
- Best for: Learning the pipeline, high-touch editorial control

**Hybrid Mode ($25-60) -- Default**
- Parallel where indicated (Phase 1, 3, 5), sequential where needed (Phase 2, 4)
- Coordinator manages handoffs
- Duration: 45-75 min
- Best for: Regular content production

**Parallel Swarm Mode ($60-150)**
- All agents active, continuous feedback loops
- Humanizer reviews drafts incrementally as Drafter writes sections
- Critic provides real-time style feedback
- Duration: 20-40 min
- Best for: Urgent publication deadlines

### Git Branch Strategy

Content is primarily document-based, not code:

```
main
├── agent/editor/vision
├── agent/researcher/sources
├── agent/drafter/draft-v1
├── agent/humanizer/humanized
├── agent/critic/feedback
└── agent/formatter/final
```

### Autonomous Decisions

Coordinator CAN autonomously:
- Request additional research on a specific claim
- Ask Humanizer for a second pass on flagged sections
- Merge Humanizer and Critic feedback when they do not conflict
- Fix minor formatting issues
- Cost limit: <$10 per autonomous action

Coordinator MUST prompt user before:
- Changing the editorial angle or target audience
- Removing a section from the draft
- Publishing or finalizing content
- Ignoring Fact-Checker warnings
- Requesting major rewrites (>30% of content)

---

## Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| AI pattern score | Low (< 3 patterns per 1000 words) | Humanizer analysis |
| Style guide compliance | >= 95% | Critic Phase 1 pass rate |
| Fact-check pass rate | 100% verified or appropriately hedged | Fact-Checker results |
| Word count target | Within 10% of brief | Word count |
| Readability score | Appropriate for target audience | Flesch-Kincaid or equivalent |
| Budget adherence | Within 20% of estimate | Actual vs projected tokens |

---

## Cost Analysis

### Per-Piece Estimates (Mixed Default Configuration)

| Content Type | Word Count | Est. Tokens | Est. Cost |
|-------------|------------|-------------|-----------|
| Short blog post | 800-1,200 | ~180K | $12-18 |
| Long-form article | 2,500-4,000 | ~260K | $18-30 |
| Technical documentation | 1,500-3,000 | ~220K | $15-25 |
| White paper | 4,000-8,000 | ~350K | $25-45 |
| Email newsletter | 500-800 | ~150K | $8-15 |

### Hourly Burn Rate

| Configuration | Est. Cost/Hour |
|--------------|----------------|
| Mixed (default) | $20-40 |
| All Sonnet (Coordinator downgrade) | $10-20 |
| All Opus (overkill) | $40-70 |
