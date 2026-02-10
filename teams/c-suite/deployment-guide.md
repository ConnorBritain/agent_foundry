# Deployment Guide

Step-by-step instructions for setting up the environment, configuring services, and running the C-Suite Team.

---

## Prerequisites

### Required Accounts

Create accounts on the following services before running the team:

| Service | URL | Purpose | Required Tier |
|---------|-----|---------|--------------|
| Google Workspace | workspace.google.com | Financial model (Sheets), pitch deck (Slides) | Free (personal Gmail) or Business |
| Notion | notion.so | Business plan, sales playbook, marketing plan, legal checklist | Free |

### Optional Accounts

| Service | URL | Purpose | Required Tier |
|---------|-----|---------|--------------|
| Linear | linear.app | Product roadmap (epics, features, timeline) | Free |

### Required CLI Tools

No CLI tools are strictly required for the C-Suite Team, as it primarily outputs documents to Google Sheets and Notion via MCP servers. However, ensure you have:

```bash
# Node.js 20+ (LTS) -- required for MCP server runtime
# Visit https://nodejs.org or use a version manager:
nvm install 20
nvm use 20

# Verify
node --version  # Should be >= 20.0.0
npm --version   # Should be >= 10.0.0
```

---

## Environment Variables

### Step 1: Generate API Keys

#### Google Workspace (Sheets and Slides)

The Google Sheets MCP server requires a service account with access to Google Sheets API and (optionally) Google Slides API.

1. Go to [console.cloud.google.com](https://console.cloud.google.com)
2. Create a new project (e.g., "c-suite-team")
3. Enable the **Google Sheets API** (and **Google Slides API** if using pitch deck generation)
4. Go to **IAM & Admin > Service Accounts**
5. Click **Create Service Account**
6. Name it (e.g., "c-suite-agent")
7. Click **Create and Continue** (no additional roles needed)
8. Click **Done**
9. Click on the created service account, go to **Keys** tab
10. Click **Add Key > Create new key > JSON**
11. Download the JSON file and save it securely
12. Set the path as `GOOGLE_APPLICATION_CREDENTIALS`

**Important:** When the CFO agent creates a Google Sheet, it will be owned by the service account. To access it, the agent will share it with your personal Google account email.

#### Notion

1. Go to [notion.so/my-integrations](https://www.notion.so/my-integrations)
2. Click **New integration**
3. Name it (e.g., "C-Suite Team")
4. Select the workspace where artifacts should be created
5. Set capabilities: **Read content**, **Update content**, **Insert content**
6. Click **Submit**
7. Copy the **Internal Integration Secret** (starts with `secret_`)

**Important:** You must also share the target Notion pages/databases with the integration. In Notion, open the page where you want artifacts created, click the three-dot menu, and select **Add connections > C-Suite Team**.

#### Linear (Optional)

1. Go to [linear.app/settings/api](https://linear.app/settings/api)
2. Click **Create key**
3. Name it (e.g., "C-Suite Team")
4. Copy the API key (starts with `lin_api_`)

### Step 2: Set Environment Variables

Create a `.env.team` file in the project root (this file should be gitignored):

```bash
# Required -- Google Workspace
GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account.json"

# Required -- Notion
NOTION_API_KEY="secret_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Optional -- Linear (for product roadmap)
LINEAR_API_KEY="lin_api_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
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
echo "Google Credentials: ${GOOGLE_APPLICATION_CREDENTIALS:+SET}"
echo "Notion: ${NOTION_API_KEY:+SET}"
echo "Linear: ${LINEAR_API_KEY:+SET (optional)}"
```

Google Credentials and Notion should print "SET". Linear is optional.

---

## MCP Server Setup

The team uses MCP (Model Context Protocol) servers to interact with external services. Configure each server before running the team.

### Google Sheets MCP Server

The Google Sheets MCP server allows the CFO agent to create and populate spreadsheets with the financial model.

```bash
# Verify the credentials file exists
ls -la "$GOOGLE_APPLICATION_CREDENTIALS"

# The MCP server configuration is at:
# mcp-servers/google-sheets.json
```

The CFO agent uses this to:
- Create the financial model spreadsheet
- Populate P&L, cash flow, cap table, and unit economics sheets
- Format cells, add formulas, and create charts
- Share the spreadsheet with the user's email

### Notion MCP Server

```bash
# The MCP server configuration is at:
# mcp-servers/notion.json
```

Multiple agents use this to:
- CEO: Create the business plan document
- CMO: Create the go-to-market plan and marketing calendar
- VP Sales: Create the sales playbook
- General Counsel: Create the compliance checklist and calendar
- COO: Create the org chart document

---

## Running the Team

### Step 1: Configure the Project

```bash
# Navigate to the template directory
cd teams/c-suite

# Copy and edit the configuration
cp CONFIG.md CONFIG.local.md

# Edit CONFIG.local.md with your business context
# At minimum, fill in:
#   - business_name and business_description
#   - business_stage and business_model
#   - target_market (industry, geography, segment)
#   - funding (current_cash, funding_seeking, funding_target)
#   - priorities (primary_goal, timeline_months, top_risks)
```

### Step 2: Select Model Configuration

Choose your model configuration in `CONFIG.local.md`:

```yaml
agent_budget:
  model_config: default  # Options: budget, default, premium, hybrid_finance
```

See `MODEL_CONFIGS.md` for detailed comparison.

### Step 3: Run the Team

```bash
# Recommended: Hybrid mode
claude-agent team run ./teams/c-suite \
  --config CONFIG.local.md \
  --mode hybrid

# Expected duration: ~1.5-2 hours
# Expected cost: ~$80-150 (default config)
```

**What happens:**

1. **Phase 1 (Vision Alignment, ~15 min):** CEO reads your CONFIG, defines vision and strategic priorities, creates board brief, distributes to specialists
2. **Phase 2 (Specialist Deep-Dives, ~25-40 min):** All 6 specialists work in parallel on their domain analysis
3. **Phase 3 (CEO Synthesis, ~15-20 min):** CEO reads all specialist outputs, resolves conflicts, creates integrated plan
4. **Phase 4 (Board Review, ~15 min):** All specialists review the integrated plan and provide feedback
5. **Phase 5 (Iteration, ~10 min):** CEO addresses feedback and locks final plan
6. **Phase 6 (Artifact Generation, ~20-30 min):** All specialists produce formatted deliverables

### Step 4: Review Outputs

After the team completes:

1. **Google Sheets** -- Open the financial model shared to your email. Verify P&L, cash flow, unit economics, and cap table.
2. **Notion** -- Check your Notion workspace for the business plan, sales playbook, marketing plan, and legal checklist.
3. **Linear (if configured)** -- Review the product roadmap for epics, features, and timeline.
4. **Executive Summary** -- Review the 1-page executive summary for accuracy and completeness.

### Running Individual Phases

If you want to run phases individually for more control:

```bash
# Run only Phase 1 (Vision Alignment)
claude-agent team run ./teams/c-suite \
  --config CONFIG.local.md \
  --mode hybrid \
  --phase 1

# Review the board brief, then run Phase 2
claude-agent team run ./teams/c-suite \
  --config CONFIG.local.md \
  --mode hybrid \
  --phase 2

# Continue through phases...
```

This approach lets you review and adjust the CEO's strategic direction before specialists begin their deep-dives.

---

## Post-Run Verification

### 1. Financial Model Integrity

- Open the Google Sheets financial model
- Verify formulas are calculating correctly (spot-check 3-5 cells)
- Confirm P&L revenue matches the sales pipeline assumptions
- Check that hiring plan costs align with cash flow projections
- Verify runway calculation against current cash and burn rate

### 2. Business Plan Consistency

- Open the Notion business plan
- Read the executive summary -- does it accurately summarize the full plan?
- Verify market sizing numbers match between CMO analysis and CFO projections
- Confirm product roadmap timeline aligns with hiring plan
- Check that legal entity recommendation supports the fundraising strategy

### 3. Cross-Document Alignment

- Revenue figures in the pitch deck match the financial model
- Pricing in the sales playbook matches the financial model assumptions
- Marketing budget in the go-to-market plan matches the P&L allocation
- Hiring sequence in the org chart matches the cash flow timeline
- Competitive landscape in the pitch deck matches the market analysis

### 4. Artifact Completeness

- All enabled outputs in CONFIG have been generated
- No sections contain placeholder text ("TBD", "Lorem ipsum", etc.)
- All numbers are calculated, not estimated
- Cross-references between documents resolve correctly

---

## Iterating on the Plan

### Quick Iteration (Same Session)

If you want to adjust a specific section:

```bash
# Re-run a specific specialist with updated context
claude-agent team run ./teams/c-suite \
  --config CONFIG.local.md \
  --mode sequential \
  --agent cfo \
  --context "Revise the P&L to assume 50% lower conversion rate in year 1"
```

### Full Re-Run (New Session)

If the plan needs fundamental changes:

1. Update `CONFIG.local.md` with new strategic direction
2. Re-run the full team
3. Compare outputs with the previous version

### Partial Re-Run

If only certain specialists need to redo their work:

```bash
# Re-run Phase 2 with only CFO and VP Sales
claude-agent team run ./teams/c-suite \
  --config CONFIG.local.md \
  --mode hybrid \
  --phase 2 \
  --agents cfo,vp-sales
```

---

## Troubleshooting

### Common Issues

**Google Sheets creation fails:**
- Verify `GOOGLE_APPLICATION_CREDENTIALS` points to a valid JSON file
- Ensure the Google Sheets API is enabled in the Google Cloud project
- Check that the service account has not exceeded quota

**Notion page creation fails:**
- Verify `NOTION_API_KEY` is valid and starts with `secret_`
- Ensure the integration has been added to the target Notion page
- Check that the integration has Insert content capability

**CEO synthesis produces inconsistencies:**
- This usually means specialist outputs had conflicting assumptions
- Re-run Phase 3 with explicit conflict resolution instructions
- Consider upgrading to Premium config for more nuanced CEO reasoning

**Specialists produce shallow analysis:**
- Provide more context in CONFIG (competitors, market data, constraints)
- Consider upgrading specific specialists to Opus 4.6
- Run in sequential mode so each specialist sees prior outputs

**Token budget exceeded:**
- Disable unused outputs (e.g., `pitch_deck: false`)
- Use 3-year projections instead of 5
- Switch to Budget model configuration
- Reduce CONFIG complexity (fewer competitors, simpler market description)

**Linear integration not working:**
- Verify `LINEAR_API_KEY` is valid
- Ensure the API key has access to the target workspace
- Check that `integrations.linear: true` is set in CONFIG
