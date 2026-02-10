# Content Creation Team

A 7-agent team template for producing research-backed, humanized content that avoids AI writing patterns and maintains consistent brand voice across all content types.

## What This Team Produces

This team delivers publication-ready content through a multi-stage pipeline that includes research, drafting, humanization, critique, fact-checking, and formatting:

- **Blog posts and articles** -- SEO-optimized, research-backed, AI-pattern-free long-form content
- **White papers and reports** -- Data-driven, properly cited, executive-ready documents
- **Email sequences** -- Conversion-optimized drip campaigns with consistent voice
- **Social media campaigns** -- Platform-specific content with unified messaging
- **Technical documentation** -- Accurate, accessible, properly structured reference material
- **Thought leadership** -- Original-angle pieces that establish authority in a domain

## When to Use This Template

Use this team when you need to:

- Produce content that must not read like AI-generated text
- Create research-backed content with verified facts and citations
- Maintain a consistent brand voice across multiple content pieces
- Enforce a style guide across all published content
- Generate high-volume content without sacrificing quality
- Match a specific author's writing style from provided samples

Do **not** use this team for:

- Quick, informal internal communications (use a single agent)
- Code documentation (use the Web App Development or Code Implementation team)
- Visual design or graphic content (this team produces text only)
- Real-time content like chat responses or live commentary

## Content Types Supported

| Content Type | Word Count | Est. Cost (Default) | Duration |
|-------------|------------|---------------------|----------|
| Short blog post | 800-1,200 | $12-18 | 30-45 min |
| Long-form article | 2,500-4,000 | $18-30 | 45-75 min |
| Technical documentation | 1,500-3,000 | $15-25 | 40-60 min |
| White paper | 4,000-8,000 | $25-45 | 60-120 min |
| Email newsletter | 500-800 | $8-15 | 20-35 min |
| Social media campaign (10 posts) | 2,000-3,000 total | $15-25 | 40-60 min |

## Quick Start

### 1. Prerequisites

Prepare the following before running the team:

- A content brief or topic description
- A style guide (optional but recommended)
- Writing samples from the target author (optional, for voice matching)
- API keys for web search (required for research phase)

### 2. Configure the Team

Copy and edit the configuration file:

```bash
cp CONFIG.md CONFIG.local.md
# Edit CONFIG.local.md with your content settings
```

### 3. Run the Team

Execute in hybrid mode (recommended):

```bash
claude-agent team run ./teams/content-creation \
  --config CONFIG.local.md \
  --mode hybrid
```

Or in sequential mode for maximum editorial control:

```bash
claude-agent team run ./teams/content-creation \
  --config CONFIG.local.md \
  --mode sequential
```

### 4. Monitor Progress

The coordinator logs phase transitions and quality metrics:

```
[Phase 1/5] Vision + Research -- Starting...
  [coordinator] Editorial vision defined: angle, audience, structure
  [research-specialist] 14 sources gathered, 5 high-relevance
[Phase 1/5] Vision + Research -- Complete

[Phase 2/5] Drafting -- Starting...
  [content-drafter] First draft complete: 2,847 words
[Phase 2/5] Drafting -- Complete

[Phase 3/5] Humanize + Critique -- Starting...
  [humanizer] 7 AI patterns flagged and rewritten
  [content-critic] 3 style violations, 2 editorial suggestions
[Phase 3/5] Humanize + Critique -- Complete
```

## Team Composition

| Agent | Model | Role |
|-------|-------|------|
| Coordinator / Editor | Opus 4.6 | Editorial vision, structural edits, final publish decision |
| Research Specialist | Sonnet 4.5 | Source gathering, fact finding, citation preparation |
| Content Drafter | Sonnet 4.5 | First draft creation, narrative structure, example development |
| Humanizer | Sonnet 4.5 | AI pattern elimination, voice matching, style application |
| Content Critic | Sonnet 4.5 | Style guide enforcement (80%), editorial feedback (20%) |
| Fact Checker | Haiku 4.5 | Claim verification, citation validation, accuracy auditing |
| Format Specialist | Haiku 4.5 | Typography, platform optimization, final proofreading |

## Estimated Cost

With default model configuration: **approximately $25** per long-form article (2,500-4,000 words).

See `cost-analysis.md` for detailed breakdowns and alternative configurations.

## Directory Structure

```
teams/content-creation/
  README.md                              -- This file
  TEAM_SPEC.md                           -- Detailed architecture and specification
  MODEL_CONFIGS.md                       -- Model selection and cost comparison
  CONFIG.md                              -- Project configuration template
  ORCHESTRATION.md                       -- Multi-agent orchestration protocol
  cost-analysis.md                       -- Token budget and cost analysis
  deployment-guide.md                    -- Step-by-step setup and execution
  agents/
    coordinator/AGENTS.md                -- Coordinator / Editor agent spec
    research-specialist/AGENTS.md        -- Research Specialist agent spec
    content-drafter/AGENTS.md            -- Content Drafter agent spec
    humanizer/AGENTS.md                  -- Humanizer agent spec
    content-critic/AGENTS.md             -- Content Critic agent spec
    fact-checker/AGENTS.md               -- Fact Checker agent spec
    format-specialist/AGENTS.md          -- Format Specialist agent spec
  mcp-servers/
    README.md                            -- MCP server setup guide
    wordpress.json                       -- WordPress MCP server config
    google-docs.json                     -- Google Docs MCP server config
  scenarios/
    blog-post-creation.md                -- Blog post end-to-end scenario
    whitepaper-development.md            -- White paper development scenario
    social-media-campaign.md             -- Social campaign scenario
    email-sequence.md                    -- Email drip sequence scenario
  examples/
    thought-leadership-series.md         -- Thought leadership example
    product-launch-content.md            -- Product launch content example
    seo-content-strategy.md              -- SEO content strategy example
```

## Key Design Principles

1. **Humanization is the differentiator.** The Humanizer agent is the most critical agent in the pipeline. Content that reads like AI wrote it is a failure, regardless of how accurate or well-structured it is.
2. **Research before writing.** Every factual claim must have a source. The Research Specialist works before the Drafter touches anything.
3. **Style guide is law.** The Critic enforces the style guide with 80% of its attention. Subjective editorial feedback is secondary.
4. **Facts are non-negotiable.** The Fact Checker verifies every claim. Unverified claims are either cited, hedged, or removed.
5. **Cost awareness.** Every agent tracks token usage. Content budgets are transparent before work begins.

## Related Documentation

- [TEAM_SPEC.md](TEAM_SPEC.md) -- Full architecture specification
- [ORCHESTRATION.md](ORCHESTRATION.md) -- Phase-by-phase execution protocol
- [deployment-guide.md](deployment-guide.md) -- How to set up and run
- [cost-analysis.md](cost-analysis.md) -- Budget planning
