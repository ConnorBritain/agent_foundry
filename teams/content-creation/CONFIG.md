# Content Creation Team Configuration

```yaml
# Content Creation Team Configuration
# Copy this file to CONFIG.local.md and fill in your values.
# CONFIG.local.md is gitignored and safe for sensitive defaults.
#
# Initialized: 2026-02-10T00:00:00Z

# ──────────────────────────────────────────────
# Content Brief
# ──────────────────────────────────────────────
content_type: long_form_article    # Options: blog_post | long_form_article | white_paper | technical_doc | email_sequence | social_campaign | newsletter
topic: ""                          # Primary topic or title
purpose: ""                        # What should the content accomplish?
target_audience: ""                # Who is reading this?
target_word_count: 3000            # Desired word count (team targets within 10%)
key_points:                        # Must-cover points (optional)
  - ""
  # - ""
  # - ""

# ──────────────────────────────────────────────
# Voice and Style
# ──────────────────────────────────────────────
writing_style: conversational      # Options: conversational | academic | technical | ap_style | hemingway_sparse | purple_prose | punchy_short_sentences | flowing_long_sentences | match_user_samples
voice_person: first_person         # Options: first_person | second_person | third_person | we
formality_level: medium            # Options: casual | medium | formal | academic

user_writing_samples:              # Paths to writing samples for voice matching (used when style = match_user_samples)
  # - "samples/blog-post-example.md"
  # - "samples/newsletter-example.md"

brand_voice_notes: ""              # Free-text description of brand personality and tone

# ──────────────────────────────────────────────
# Style Guide
# ──────────────────────────────────────────────
style_guide:
  source: ""                       # Path to style guide file, or "none"
  terminology:                     # Product names, branded terms that must be used consistently
    # - term: "Sforza"
    #   usage: "Always capitalize. Never lowercase or as one word."
    # - term: "AI agent"
    #   usage: "Lowercase 'agent'. Never 'Agent' unless starting a sentence."
  formatting:
    heading_style: atx             # Options: atx (# Heading) | setext (Heading\n===)
    list_style: dash               # Options: dash (-) | asterisk (*) | number (1.)
    emphasis: bold                 # Options: bold (**text**) | italic (*text*) | both
    code_style: fenced             # Options: fenced (```) | indented (4 spaces)
  citation_format: inline_link     # Options: inline_link | footnote | endnote | academic_apa | academic_mla
  language: en_us                  # Options: en_us | en_gb | en_au
  oxford_comma: true
  max_sentence_length: 35          # Words; longer sentences flagged for review
  max_paragraph_length: 6          # Sentences; longer paragraphs flagged

# ──────────────────────────────────────────────
# SEO Configuration (optional)
# ──────────────────────────────────────────────
seo:
  enabled: false
  primary_keyword: ""
  secondary_keywords:
    # - ""
  target_keyword_density: 1.5      # Percentage (1-3% typical)
  meta_description_length: 155     # Characters
  include_schema_markup: false
  internal_links:                  # URLs to link to within content
    # - url: ""
    #   anchor_text: ""

# ──────────────────────────────────────────────
# Research Configuration
# ──────────────────────────────────────────────
research:
  depth: standard                  # Options: light | standard | deep
  max_sources: 15                  # Maximum number of sources to gather
  source_recency_years: 2          # Prefer sources from the last N years
  require_primary_sources: true    # Prefer original research over summaries
  allowed_source_types:
    - peer_reviewed
    - industry_reports
    - government_data
    - reputable_news
    - expert_blogs
  blocked_domains:                 # Domains to exclude from research
    # - "example.com"

# ──────────────────────────────────────────────
# Humanization Configuration
# ──────────────────────────────────────────────
humanization:
  aggressiveness: standard         # Options: light | standard | aggressive
  # light: flag obvious patterns only
  # standard: flag and rewrite common AI patterns
  # aggressive: rewrite any text that could plausibly be AI-detected
  preserve_technical_accuracy: true
  allow_humor: false               # Allow the Humanizer to inject humor
  allow_personal_anecdotes: false  # Allow fabricated personal anecdotes (clearly fictional)
  max_ai_patterns_per_1000_words: 3

# ──────────────────────────────────────────────
# Target Platform
# ──────────────────────────────────────────────
platform:
  target: markdown                 # Options: markdown | wordpress | medium | ghost | notion | email_html | google_docs
  wordpress_settings:              # Only used when platform = wordpress
    category: ""
    tags: []
    featured_image: true
    excerpt_length: 55             # Words
  email_settings:                  # Only used when platform = email_html
    preheader_text: ""
    max_width_px: 600
    include_plain_text: true

# ──────────────────────────────────────────────
# Agent Budget
# ──────────────────────────────────────────────
agent_budget:
  model_config: default            # Options: budget | default | premium | maximum
  max_total_tokens: 312000         # 260K base + 20% buffer
  max_total_cost_usd: 25
  iteration_budget: 2              # Max number of humanizer re-passes

# ──────────────────────────────────────────────
# Output Configuration
# ──────────────────────────────────────────────
output:
  include_research_brief: true
  include_ai_pattern_audit: true
  include_style_report: true
  include_fact_check_report: true
  include_metadata: true
  output_directory: "./output"
```

## Usage

1. Copy this file:
   ```bash
   cp CONFIG.md CONFIG.local.md
   ```

2. Edit `CONFIG.local.md` with your content-specific values.

3. Pass it to the team runner:
   ```bash
   claude-agent team run ./teams/content-creation --config CONFIG.local.md
   ```

## Configuration Validation

The Coordinator agent validates the configuration at the start of Phase 1 and will report errors for:

- Missing required fields (`content_type`, `topic`, `target_audience`)
- Invalid enum values (e.g., `writing_style: freestyle` is not a valid option)
- Inconsistent settings (e.g., `style: match_user_samples` with no samples provided)
- Budget conflicts (e.g., `max_total_cost_usd` lower than the selected `model_config` estimate)
- SEO enabled without keywords defined
- Word count below 200 or above 15,000

## Environment Variables

These must be set in your shell before running the team:

```bash
# Required for research phase
export SEARCH_API_KEY=""            # Web search API key (Brave, Google, etc.)

# Optional for platform publishing
export WORDPRESS_URL=""             # WordPress site URL
export WORDPRESS_USERNAME=""        # WordPress username
export WORDPRESS_APP_PASSWORD=""    # WordPress application password
export GOOGLE_DOCS_CREDENTIALS=""   # Path to Google service account JSON
```
