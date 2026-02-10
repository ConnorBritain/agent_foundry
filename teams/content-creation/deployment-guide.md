# Deployment Guide

Step-by-step instructions for setting up the environment, configuring services, and running the Content Creation Team.

---

## Prerequisites

### Required Accounts

| Service | URL | Purpose | Required Tier |
|---------|-----|---------|--------------|
| Brave Search (or equivalent) | brave.com/search/api | Web research for the Research Specialist | Free (up to 2,000 queries/month) |

### Optional Accounts

| Service | URL | Purpose | Required Tier |
|---------|-----|---------|--------------|
| WordPress | wordpress.com or self-hosted | Content publishing | Any |
| Google Workspace | workspace.google.com | Google Docs publishing | Business Starter |

### Required CLI Tools

```bash
# Node.js 20+ (LTS)
# Visit https://nodejs.org or use a version manager:
nvm install 20
nvm use 20

# Verify
node --version  # Should be >= 20.0.0

# GitHub CLI (for version control of content)
# macOS:
brew install gh
# Linux:
# See https://github.com/cli/cli/blob/trunk/docs/install_linux.md

# Verify
gh --version
```

### Authentication

```bash
# GitHub (if using git-based content management)
gh auth login
# Follow the prompts to authenticate via browser
```

---

## Environment Variables

### Step 1: Generate API Keys

#### Web Search API

1. Go to https://brave.com/search/api/ (or your configured search provider)
2. Sign up for an API key
3. Copy the API key

#### WordPress (Optional)

1. Log in to your WordPress admin panel
2. Go to **Users > Profile > Application Passwords**
3. Create a new application password named "content-creation-team"
4. Copy the generated password

#### Google Docs (Optional)

1. Go to https://console.cloud.google.com
2. Create a service account with Google Docs API access
3. Download the JSON key file
4. Save it to a secure location

### Step 2: Set Environment Variables

Create a `.env.team` file in the project root (this file should be gitignored):

```bash
# Required - Web Search for Research Phase
SEARCH_API_KEY="your-search-api-key-here"

# Optional - WordPress Publishing
WORDPRESS_URL="https://your-site.com"
WORDPRESS_USERNAME="your-username"
WORDPRESS_APP_PASSWORD="xxxx xxxx xxxx xxxx xxxx xxxx"

# Optional - Google Docs Publishing
GOOGLE_DOCS_CREDENTIALS="/path/to/service-account.json"
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
echo "WordPress: ${WORDPRESS_URL:+SET}"
echo "Google Docs: ${GOOGLE_DOCS_CREDENTIALS:+SET}"
```

The Search API key should show "SET". WordPress and Google Docs are optional.

---

## MCP Server Setup

The team uses MCP servers to interact with external services. Configure each server before running the team.

### Web Search MCP Server

The Research Specialist uses web search to gather sources and verify claims.

```bash
# Verify the search API key is set
echo "Search API: ${SEARCH_API_KEY:+SET}"

# The MCP server configuration is at:
# mcp-servers/brave-search.json (or equivalent)
```

### WordPress MCP Server (Optional)

```bash
# Verify WordPress credentials
echo "WordPress URL: ${WORDPRESS_URL:+SET}"
echo "WordPress User: ${WORDPRESS_USERNAME:+SET}"
echo "WordPress Pass: ${WORDPRESS_APP_PASSWORD:+SET}"

# The MCP server configuration is at:
# mcp-servers/wordpress.json
```

The Format Specialist uses this to publish directly to WordPress.

### Google Docs MCP Server (Optional)

```bash
# Verify Google credentials
echo "Google Docs: ${GOOGLE_DOCS_CREDENTIALS:+SET}"

# The MCP server configuration is at:
# mcp-servers/google-docs.json
```

The Format Specialist uses this to create formatted Google Docs.

---

## Running the Team

### Step 1: Configure the Project

```bash
# Navigate to the template directory
cd teams/content-creation

# Copy and edit the configuration
cp CONFIG.md CONFIG.local.md

# Edit CONFIG.local.md with your content settings
# At minimum, fill in:
#   - content_type
#   - topic
#   - target_audience
#   - target_word_count
#   - writing_style
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
claude-agent team run ./teams/content-creation \
  --config CONFIG.local.md \
  --mode hybrid

# Expected duration: ~45-75 minutes
# Expected cost: ~$21 (default config, long-form article)
```

**What happens:**
1. Coordinator defines editorial vision while Research Specialist gathers sources
2. Content Drafter writes the first draft using vision and research
3. Humanizer eliminates AI patterns while Critic checks style compliance
4. Fact Checker verifies all claims
5. Coordinator incorporates feedback while Format Specialist prepares for platform

**User review points:**
- After Phase 1: Review editorial angle and research findings
- After Phase 5: Review final content before publication

### Step 4: Run in Sequential Mode (Maximum Control)

```bash
claude-agent team run ./teams/content-creation \
  --config CONFIG.local.md \
  --mode sequential

# Expected duration: ~1.5-2.5 hours
# Expected cost: ~$21 (same token usage, slower execution)
```

Use sequential mode when you want to review and adjust each agent's output before the next agent begins.

### Step 5: Run in Swarm Mode (Fastest)

```bash
claude-agent team run ./teams/content-creation \
  --config CONFIG.local.md \
  --mode swarm

# Expected duration: ~20-40 minutes
# Expected cost: ~$30-40 (higher due to overlapping agent activity)
```

Use swarm mode for urgent deadlines when you are comfortable with less control.

---

## Post-Completion Verification

After the team completes, verify the output:

### 1. Content Quality

- Read the final content end-to-end
- Check that the editorial angle from Phase 1 is maintained throughout
- Verify the content sounds natural (not AI-generated)
- Confirm word count meets the target (within 10%)

### 2. Review Reports

Check the output directory for these reports:

```bash
ls ./output/
# Expected files:
# final-content.md          -- Publication-ready content
# research-brief.md         -- Sources and findings
# ai-pattern-audit.md       -- AI patterns found and fixed
# style-compliance.md       -- Style guide violations and resolution
# fact-check-report.md      -- Claim verification results
# content-metadata.yaml     -- Word count, reading time, SEO tags
```

### 3. Fact-Check Report

Review the fact-check report for any UNCERTAIN or LIKELY claims:
- VERIFIED claims are safe to publish
- LIKELY claims should include hedging language ("approximately," "reportedly")
- UNCERTAIN claims should be removed or independently verified by you
- There should be zero FALSE claims in the final version

### 4. Platform Publishing

If publishing directly via MCP server:
- **WordPress:** Verify the post appears correctly in draft mode before publishing
- **Google Docs:** Verify formatting translated correctly to the Google Docs format

---

## Troubleshooting

### Common Issues

**Research phase returns few sources:**
- Verify `SEARCH_API_KEY` is valid and has remaining quota
- Check that `research.blocked_domains` is not overly restrictive
- Try broadening the topic or adjusting search angles

**Humanizer flags too many patterns:**
- This is normal for first drafts -- the Humanizer is designed to be thorough
- If patterns per 1,000 words exceeds 5 after the first pass, the Coordinator will request a second pass
- Consider upgrading the Drafter to Opus (premium config) to reduce source patterns

**Style compliance below 90%:**
- Check that the style guide in CONFIG.local.md is correctly formatted
- Verify terminology entries use exact match strings
- Review blocking violations first -- they must be resolved before publication

**Fact Checker flags FALSE claims:**
- The Coordinator will not publish content with FALSE claims
- Review the correction recommendation and verify it is accurate
- If the Fact Checker is wrong (rare), escalate to the user for a manual override

**WordPress publishing fails:**
- Verify `WORDPRESS_URL`, `WORDPRESS_USERNAME`, and `WORDPRESS_APP_PASSWORD` are all set
- Check that the application password has not expired
- Verify the WordPress REST API is accessible (`curl https://your-site.com/wp-json/wp/v2/posts`)

**Token budget exceeded:**
- The Coordinator tracks token usage per phase
- If budget is projected to exceed the limit by more than 15%, the Coordinator escalates
- To reduce cost: lower `research.depth`, reduce `iteration_budget`, or switch to Budget config
