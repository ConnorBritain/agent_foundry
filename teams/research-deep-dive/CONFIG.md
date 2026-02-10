# Research Deep Dive Team Configuration

```yaml
# Research Deep Dive Team Configuration
# Copy this file to CONFIG.local.md and fill in your values.
# CONFIG.local.md is gitignored and safe for sensitive defaults.
#
# Initialized: 2026-02-10T00:00:00Z

# ──────────────────────────────────────────────
# Research Question
# ──────────────────────────────────────────────
research_type: market                # Options: academic | market | competitive | product_ux | literature_review | mixed
domain: technology                   # Options: healthcare | finance | technology | education | climate | social_science | other
research_question: ""                # Primary question being investigated
sub_questions:                       # Specific sub-questions to address (optional)
  - ""
  # - ""
  # - ""

# ──────────────────────────────────────────────
# Constraints
# ──────────────────────────────────────────────
constraints:
  timeline_weeks: 0                  # 0 = single session, or number of weeks for ongoing research
  budget_available: no               # Options: yes | no (whether proprietary data sources are available)
  data_access: public                # Options: public | proprietary | mixed | none_yet

# ──────────────────────────────────────────────
# Academic Mode (only if research_type includes academic)
# ──────────────────────────────────────────────
academic_mode:
  enabled: false
  methodology: systematic_review     # Options: experimental | observational | meta_analysis | systematic_review | qualitative
  citation_style: apa                # Options: apa | mla | chicago | vancouver | harvard
  target_journal: "general"          # Journal name or "general"
  irb_required: no                   # Options: yes | no | unknown
  include_grant_proposal: false      # Activate Grant Writer agent

# ──────────────────────────────────────────────
# Market/Competitive Mode (only if research_type includes market or competitive)
# ──────────────────────────────────────────────
market_mode:
  enabled: false
  market_definition: ""              # Description of the market being analyzed
  geographic_scope: global           # Options: global | regional | local
  customer_segments:                 # Target customer segments
    - ""
    # - ""
  include_tam_sam_som: true          # Run TAM/SAM/SOM analysis
  include_competitive_landscape: true # Run competitive landscape mapping
  include_trend_analysis: true       # Run trend forecasting

# ──────────────────────────────────────────────
# Product/UX Mode (only if research_type includes product_ux)
# ──────────────────────────────────────────────
product_mode:
  enabled: false
  product_stage: growth              # Options: concept | mvp | growth | mature
  research_focus: validation         # Options: discovery | validation | optimization
  analytics_access: no               # Whether analytics data is available
  product_url: ""                    # URL of the product (for usability evaluation)
  analytics_data_path: ""            # Path to analytics export (optional)
  interview_transcripts_path: ""     # Path to interview transcripts (optional)

# ──────────────────────────────────────────────
# Source Discovery Configuration
# ──────────────────────────────────────────────
sources:
  depth: standard                    # Options: light | standard | deep
  max_sources: 25                    # Maximum number of sources to gather
  source_recency_years: 3            # Prefer sources from the last N years
  require_primary_sources: true      # Prefer original research over summaries
  allowed_source_types:
    - peer_reviewed
    - industry_reports
    - government_data
    - financial_filings
    - patent_databases
    - news_credible
    - expert_analysis
  blocked_domains:                   # Domains to exclude from research
    # - "example.com"
  additional_databases:              # Extra databases to search
    # - "arxiv"
    # - "pubmed"
    # - "ieee"

# ──────────────────────────────────────────────
# Analysis Configuration
# ──────────────────────────────────────────────
analysis:
  statistical_approach: descriptive  # Options: descriptive | inferential | both
  visualization_format: markdown     # Options: markdown | mermaid | both
  confidence_reporting: true         # Report confidence intervals for all estimates
  sensitivity_analysis: true         # Run sensitivity analysis on key assumptions

# ──────────────────────────────────────────────
# Output Configuration
# ──────────────────────────────────────────────
output:
  primary_format: markdown           # Options: markdown | latex | google_docs | notion
  include_executive_summary: true    # Always include a standalone executive summary
  include_source_database: true      # Include full source list with assessments
  include_methodology_notes: true    # Include methodology documentation
  include_limitation_analysis: true  # Include explicit limitations section
  include_recommendations: true      # Include actionable recommendations
  output_directory: "./output"

# ──────────────────────────────────────────────
# Agent Budget
# ──────────────────────────────────────────────
agent_budget:
  model_config: default              # Options: budget | default | premium | maximum
  max_total_tokens: 420000           # Base + 20% buffer (varies by mode)
  max_total_cost_usd: 50             # Maximum spend for this study
  max_autonomous_action_cost: 15     # Max cost for Coordinator autonomous decisions
```

## Usage

1. Copy this file:
   ```bash
   cp CONFIG.md CONFIG.local.md
   ```

2. Edit `CONFIG.local.md` with your research-specific values.

3. Pass it to the team runner:
   ```bash
   claude-agent team run ./teams/research-deep-dive --config CONFIG.local.md
   ```

## Configuration Validation

The Coordinator agent validates the configuration at the start of Phase 1 and will report errors for:

- Missing required fields (`research_type`, `domain`, `research_question`)
- Invalid enum values (e.g., `research_type: investigative` is not a valid option)
- Inconsistent settings (e.g., `academic_mode.enabled: true` with `research_type: market`)
- Budget conflicts (e.g., `max_total_cost_usd` lower than the selected mode's minimum estimate)
- Mode-specific fields missing (e.g., `market_mode.market_definition` empty when market mode is enabled)
- Source constraints that are too restrictive for the research question

## Environment Variables

These must be set in your shell before running the team:

```bash
# Required for source discovery
export SEARCH_API_KEY=""             # Web search API key (Brave, Google, etc.)

# Optional for academic mode
export ARXIV_API_KEY=""              # arXiv API access (if using arXiv MCP server)
export ZOTERO_API_KEY=""             # Zotero citation management
export PUBMED_API_KEY=""             # PubMed access for medical research

# Optional for market mode
export CRUNCHBASE_API_KEY=""         # Crunchbase company data
export SIMILARWEB_API_KEY=""         # SimilarWeb traffic analysis

# Optional for output delivery
export GOOGLE_DOCS_CREDENTIALS=""    # Path to Google service account JSON
export NOTION_API_KEY=""             # Notion integration token
```
