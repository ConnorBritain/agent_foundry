# Research Deep Dive Team

A configurable multi-agent team for conducting rigorous research across academic, market, competitive, and product domains. The team adapts its composition based on research type, activating specialized agents only when their domain is relevant.

## What This Team Produces

This team delivers well-sourced, methodologically sound research through a multi-phase pipeline that includes study design, data collection, analysis, and synthesis:

- **Academic research** -- Literature reviews, systematic reviews, meta-analyses with proper citations and methodology
- **Market research** -- TAM/SAM/SOM models, market sizing, industry analysis with defensible assumptions
- **Competitive intelligence** -- Competitor profiles, landscape maps, feature comparisons, pricing analysis
- **Product/UX research** -- User behavior analysis, usability evaluations, feature prioritization with RICE scoring
- **Literature reviews** -- Comprehensive source discovery, thematic synthesis, gap analysis
- **Mixed-method studies** -- Cross-domain research combining multiple modes for complex questions

## When to Use This Template

Use this team when you need to:

- Conduct research that requires systematic methodology (not just "search and summarize")
- Triangulate findings across multiple data sources
- Produce outputs that meet academic, professional, or executive standards
- Investigate questions with multiple sub-questions requiring parallel investigation
- Generate structured deliverables (papers, reports, market models, prioritized backlogs)

Do **not** use this team for:

- Quick fact-checking or simple search queries (use a single agent)
- Content creation or writing (use the Content Creation team)
- Code implementation or technical architecture (use the Web App Development team)
- Real-time monitoring or ongoing data collection (this team produces point-in-time research)

## Research Modes

| Mode | Agents | Est. Cost | Duration | Deliverables |
|------|--------|-----------|----------|-------------|
| Literature Review | 4 core | $12-20 | 1-2 hours | Review paper, source analysis, gap report |
| Academic (full) | 7-8 agents | $35-60 | 2-3 hours | Research paper, bibliography, supplementary materials |
| Market Research | 7-8 agents | $25-45 | 1-2 hours | Market report, TAM/SAM/SOM model, trend scenarios |
| Competitive Intelligence | 7-8 agents | $20-35 | 45-90 min | Competitor profiles, landscape map, executive briefing |
| Product/UX Research | 7 agents | $18-30 | 45-90 min | Findings report, prioritized backlog, experiment proposals |

## Quick Start

### 1. Prerequisites

Prepare the following before running the team:

- A clear research question or area of investigation
- Domain context and constraints (timeline, data access, budget)
- API keys for web search (required for source discovery)
- Mode-specific data (interview transcripts, analytics exports, etc.) if available

### 2. Configure the Team

Copy and edit the configuration file:

```bash
cp CONFIG.md CONFIG.local.md
# Edit CONFIG.local.md with your research settings
```

### 3. Run the Team

Execute in hybrid mode (recommended):

```bash
claude-agent team run ./teams/research-deep-dive \
  --config CONFIG.local.md \
  --mode hybrid
```

Or in sequential mode for maximum methodological control:

```bash
claude-agent team run ./teams/research-deep-dive \
  --config CONFIG.local.md \
  --mode sequential
```

### 4. Monitor Progress

The coordinator logs phase transitions and quality metrics:

```
[Phase 1/5] Study Design -- Starting...
  [coordinator] Research protocol defined: question, methodology, sources
  [coordinator] Team configured: academic mode, 7 agents active
[Phase 1/5] Study Design -- Complete

[Phase 2/5] Data Collection -- Starting...
  [primary-researcher] 47 sources found, 12 high-relevance
  [primary-researcher] Gap identified: no studies on [sub-topic] since 2023
[Phase 2/5] Data Collection -- Complete

[Phase 3/5] Analysis -- Starting...
  [analyst] Statistical analysis complete, 3 key findings
  [analyst] Confidence intervals computed for all estimates
[Phase 3/5] Analysis -- Complete
```

## Team Composition

### Core Team (Always Active)

| Agent | Model | Role |
|-------|-------|------|
| Coordinator / Research Lead | Opus 4.6 | Study design, quality control, synthesis direction |
| Primary Researcher | Sonnet 4.5 | Source discovery, relevance assessment, data collection |
| Analyst | Sonnet 4.5 | Statistical analysis, visualization, data interpretation |
| Synthesizer | Sonnet 4.5 | Narrative construction, findings communication |

### Mode-Specific Agents (Conditionally Activated)

See `TEAM_SPEC.md` for the full roster of 11+ conditional agents across academic, market, and product modes.

## Estimated Cost

With default model configuration: **$12-60 per study** depending on mode and complexity.

See `cost-analysis.md` for detailed breakdowns by mode and configuration.

## Directory Structure

```
teams/research-deep-dive/
  README.md                                  -- This file
  TEAM_SPEC.md                               -- Detailed architecture and specification
  MODEL_CONFIGS.md                           -- Model selection and cost comparison
  CONFIG.md                                  -- Project configuration template
  ORCHESTRATION.md                           -- Multi-agent orchestration protocol
  cost-analysis.md                           -- Token budget and cost analysis
  deployment-guide.md                        -- Step-by-step setup and execution
  agents/
    coordinator/AGENTS.md                    -- Coordinator / Research Lead agent spec
    primary-researcher/AGENTS.md             -- Primary Researcher agent spec
    analyst/AGENTS.md                        -- Analyst agent spec
    synthesizer/AGENTS.md                    -- Synthesizer agent spec
  mcp-servers/
    README.md                                -- MCP server setup guide
    brave-search.json                        -- Brave Search MCP server config
    arxiv.json                               -- arXiv MCP server config
  scenarios/
    market-sizing.md                         -- Market sizing end-to-end scenario
    competitive-analysis.md                  -- Competitive analysis scenario
    academic-literature-review.md            -- Academic literature review scenario
    product-discovery.md                     -- Product discovery scenario
  examples/
    saas-market-research.md                  -- SaaS market research example
    technology-landscape.md                  -- Technology landscape example
    user-research-study.md                   -- User research study example
```

## Key Design Principles

1. **Methodology drives everything.** The Coordinator designs the research protocol before any data collection begins. Searching without a plan produces noise, not insight.
2. **Sources are auditable.** Every factual claim traces back to a specific source with credibility assessment. The team documents what it could NOT find as rigorously as what it did find.
3. **Conclusions follow from evidence.** The Synthesizer never overstates what the data supports. Limitations are documented alongside findings.
4. **Modes activate relevant specialists.** The team does not load market sizing agents for an academic literature review, or citation managers for competitive intelligence. Configuration drives composition.
5. **Cost scales with depth.** A focused literature review costs $12-20. A full academic study costs $35-60. Users choose the depth that matches their needs.

## Related Documentation

- [TEAM_SPEC.md](TEAM_SPEC.md) -- Full architecture specification
- [ORCHESTRATION.md](ORCHESTRATION.md) -- Phase-by-phase execution protocol
- [deployment-guide.md](deployment-guide.md) -- How to set up and run
- [cost-analysis.md](cost-analysis.md) -- Budget planning
