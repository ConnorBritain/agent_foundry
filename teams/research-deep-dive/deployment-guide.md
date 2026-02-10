# Deployment Guide

Step-by-step instructions for setting up the environment, configuring services, and running the Research Deep Dive Team.

---

## Prerequisites

### Required Accounts

| Service | URL | Purpose | Required Tier |
|---------|-----|---------|--------------|
| Brave Search (or equivalent) | brave.com/search/api | Web source discovery for the Primary Researcher | Free (up to 2,000 queries/month) |

### Optional Accounts

| Service | URL | Purpose | Required Tier |
|---------|-----|---------|--------------|
| arXiv API | arxiv.org/help/api | Academic paper access | Free |
| PubMed / NCBI | ncbi.nlm.nih.gov | Medical and biomedical research | Free (API key recommended) |
| Crunchbase | crunchbase.com | Company data and funding intelligence | Basic (free) or Pro |
| SimilarWeb | similarweb.com | Web traffic and competitive benchmarking | Pro |
| Google Workspace | workspace.google.com | Google Docs/Sheets output delivery | Business Starter |
| Notion | notion.so | Report creation and collaboration | Plus |

### Required CLI Tools

```bash
# Node.js 20+ (LTS)
# Visit https://nodejs.org or use a version manager:
nvm install 20
nvm use 20

# Verify
node --version  # Should be >= 20.0.0

# GitHub CLI (for version control of research outputs)
# macOS:
brew install gh
# Linux:
# See https://github.com/cli/cli/blob/trunk/docs/install_linux.md

# Verify
gh --version
```

### Authentication

```bash
# GitHub (if using git-based output management)
gh auth login
# Follow the prompts to authenticate via browser
```

---

## Environment Variables

### Step 1: Generate API Keys

#### Web Search API (Required)

1. Go to https://brave.com/search/api/ (or your configured search provider)
2. Sign up for an API key
3. Copy the API key

#### arXiv API (Optional, Academic Mode)

1. arXiv API is freely accessible without a key for moderate usage
2. For high-volume access, register at https://info.arxiv.org/help/api/index.html
3. Respect rate limits: 1 request per 3 seconds

#### Crunchbase API (Optional, Market Mode)

1. Go to https://www.crunchbase.com/
2. Sign up for a Basic or Pro account
3. Navigate to the API section and generate a key

### Step 2: Set Environment Variables

Create a `.env.team` file in the project root (this file should be gitignored):

```bash
# Required - Web Search for Source Discovery
SEARCH_API_KEY="your-search-api-key-here"

# Optional - Academic Mode
ARXIV_API_KEY=""
PUBMED_API_KEY=""
ZOTERO_API_KEY=""

# Optional - Market Mode
CRUNCHBASE_API_KEY=""
SIMILARWEB_API_KEY=""

# Optional - Output Delivery
GOOGLE_DOCS_CREDENTIALS="/path/to/service-account.json"
NOTION_API_KEY=""
```

Load the environment variables:

```bash
# Option 1: Source the file
source .env.team

# Option 2: Use direnv (recommended)
cp .env.team .envrc
direnv allow
```

### Step 3: Verify Environment

```bash
# Quick verification
echo "Search API: ${SEARCH_API_KEY:+SET}"
echo "arXiv: ${ARXIV_API_KEY:+SET}"
echo "Crunchbase: ${CRUNCHBASE_API_KEY:+SET}"
echo "Google Docs: ${GOOGLE_DOCS_CREDENTIALS:+SET}"
echo "Notion: ${NOTION_API_KEY:+SET}"
```

The Search API key should show "SET". All other keys are optional depending on your research mode.

---

## MCP Server Setup

The team uses MCP servers to interact with external services. Configure each server before running the team.

### Web Search MCP Server (Required)

The Primary Researcher uses web search for source discovery.

```bash
# Verify the search API key is set
echo "Search API: ${SEARCH_API_KEY:+SET}"

# The MCP server configuration is at:
# mcp-servers/brave-search.json
```

### arXiv MCP Server (Optional, Academic Mode)

```bash
# The MCP server configuration is at:
# mcp-servers/arxiv.json

# arXiv API is rate-limited to 1 request per 3 seconds
# The MCP server handles rate limiting automatically
```

The Primary Researcher uses this for academic paper discovery and metadata retrieval.

---

## Running the Team

### Step 1: Configure the Project

```bash
# Navigate to the template directory
cd teams/research-deep-dive

# Copy and edit the configuration
cp CONFIG.md CONFIG.local.md

# Edit CONFIG.local.md with your research settings
# At minimum, fill in:
#   - research_type
#   - domain
#   - research_question
#   - Enable the appropriate mode (academic_mode, market_mode, or product_mode)
```

### Step 2: Select Model Configuration

Choose your model configuration in `CONFIG.local.md`:

```yaml
agent_budget:
  model_config: default  # Options: budget, default, premium, maximum
```

See `MODEL_CONFIGS.md` for detailed comparison.

### Step 3: Run in Hybrid Mode (Recommended)

```bash
claude-agent team run ./teams/research-deep-dive \
  --config CONFIG.local.md \
  --mode hybrid

# Expected duration: ~45-120 minutes (varies by mode)
# Expected cost: ~$25-45 (default config, market mode)
```

**What happens:**
1. Coordinator designs the study protocol and configures the team
2. Primary Researcher and mode-specific collectors gather data in parallel
3. Analyst and mode-specific analysts process data in parallel
4. Synthesizer drafts the research narrative
5. All agents produce final deliverables

**User review points:**
- After Phase 1: Review study design and methodology
- After Phase 4: Review key findings before final deliverable creation

### Step 4: Run in Sequential Mode (Maximum Control)

```bash
claude-agent team run ./teams/research-deep-dive \
  --config CONFIG.local.md \
  --mode sequential

# Expected duration: ~2-4 hours
# Expected cost: ~$25-45 (same token usage, slower execution)
```

Use sequential mode when you want to review each phase's output before proceeding. Recommended for methodologically sensitive academic research.

### Step 5: Run in Swarm Mode (Fastest)

```bash
claude-agent team run ./teams/research-deep-dive \
  --config CONFIG.local.md \
  --mode swarm

# Expected duration: ~20-60 minutes
# Expected cost: ~$40-70 (higher due to overlapping agent activity)
```

Use swarm mode for urgent competitive intelligence or time-sensitive market research.

---

## Post-Completion Verification

After the team completes, verify the output:

### 1. Research Quality

- Read the executive summary for coherence and actionability
- Verify the methodology matches what was approved in Phase 1
- Check that conclusions follow from the presented evidence
- Confirm limitations are honestly documented

### 2. Review Deliverables

Check the output directory for mode-specific deliverables:

```bash
ls ./output/
# Expected files vary by mode. Market mode example:
# executive-summary.md          -- Standalone summary of findings
# market-analysis-report.md     -- Comprehensive market analysis
# competitive-landscape.md      -- Competitor profiles and positioning
# tam-sam-som-model.md          -- Market sizing with assumptions
# trend-scenarios.md            -- Future scenario analysis
# source-database.md            -- All sources with assessments
# methodology-notes.md          -- Research protocol documentation
```

### 3. Source Audit

Review the source database for quality:
- >80% of sources should be peer-reviewed or primary
- All sources should have credibility assessments
- Research gaps should be explicitly documented
- Contested findings should present multiple perspectives

### 4. Verify Reproducibility

- The methodology notes should contain enough detail to repeat the study
- All data sources and search queries should be documented
- Statistical methods and assumptions should be clearly stated

---

## Troubleshooting

### Common Issues

**Source discovery returns few results:**
- Verify `SEARCH_API_KEY` is valid and has remaining quota
- Check that `sources.blocked_domains` is not overly restrictive
- Try broadening the research question or adjusting search terms
- For academic mode, verify arXiv/PubMed API access

**Methodology design takes too long:**
- This is common for complex academic research questions
- The Coordinator may request clarification from the user
- Consider using a more specific research_type instead of "mixed"

**Contradictory findings in analysis:**
- This is expected behavior, not an error
- The Analyst flags contradictions for the Coordinator to resolve
- The Synthesizer presents both perspectives with evidence strength assessments

**Budget exceeded before synthesis phase:**
- Source discovery was likely too broad
- Use `sources.depth: light` for focused research
- Set `sources.max_sources` to a lower number
- Consider Budget model configuration

**Mode-specific agents not activating:**
- Verify the correct mode is enabled in CONFIG (e.g., `market_mode.enabled: true`)
- Check that `research_type` matches the enabled mode
- The Coordinator logs which agents are activated in Phase 1

**Deliverable format issues:**
- Verify `output.primary_format` matches your intended delivery method
- For Google Docs output, verify `GOOGLE_DOCS_CREDENTIALS` is set
- For Notion output, verify `NOTION_API_KEY` is set and has workspace access
