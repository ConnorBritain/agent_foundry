# Deployment Guide

## Prerequisites

### Required

1. **Claude Code CLI** (v2.0+) with multi-agent support enabled
   ```bash
   claude-code --version  # Verify v2.0+
   claude-code team --help  # Verify team commands available
   ```

2. **API Access** with sufficient quota for the chosen configuration
   - Default config: ~930K tokens per run
   - Ensure your API plan supports the required models (Opus 4.6, Sonnet 4.5, Haiku 4.5)

3. **Git** initialized in your project directory
   ```bash
   git init  # If not already initialized
   git checkout -b gtm/initial-setup
   ```

4. **Business Context** prepared:
   - Target customer profiles (industry, size, titles, pain points)
   - Product details (features, pricing, differentiators)
   - Competitive landscape (top 2-3 competitors with positioning)
   - Current metrics (if scaling existing motion): CAC, LTV, conversion rates
   - Monthly marketing budget

### Recommended

5. **CRM Access** (HubSpot, Salesforce, Pipedrive, or Close)
   - API key or OAuth credentials
   - Admin access for CRM configuration changes
   - Existing pipeline data (if available) for the Pipeline Manager to analyze

6. **Ad Platform Access** (for Demand Generation campaigns)
   - Google Ads account with billing set up
   - LinkedIn Campaign Manager access
   - Meta Business Manager access (if applicable)

7. **Analytics Platform** (Google Analytics, Mixpanel, Amplitude, or Heap)
   - Admin access for event configuration
   - Existing data for the Growth Analyst to analyze (if available)

---

## MCP Server Setup

MCP (Model Context Protocol) servers allow agents to interact with your marketing and sales tools directly. They are optional but significantly improve output quality by grounding agent work in real data.

### HubSpot MCP Server

```bash
# Install the HubSpot MCP server
claude-code mcp install hubspot --config mcp-servers/hubspot.json

# Set your API key
export HUBSPOT_API_KEY="your-api-key-here"

# Or use OAuth (recommended for production)
claude-code mcp auth hubspot --oauth
```

**Capabilities enabled**:
- Read/write contacts, companies, and deals
- Create and manage marketing campaigns
- Access analytics and reporting data
- Manage email sequences and workflows
- Read pipeline and deal data

**Required HubSpot permissions**:
- `crm.objects.contacts.read` / `.write`
- `crm.objects.deals.read` / `.write`
- `crm.objects.companies.read` / `.write`
- `marketing.campaigns.read` / `.write`
- `analytics.read`

### Google Ads MCP Server

```bash
# Install the Google Ads MCP server
claude-code mcp install google-ads --config mcp-servers/google-ads.json

# Authenticate with Google
claude-code mcp auth google-ads --oauth

# Set your customer ID
export GOOGLE_ADS_CUSTOMER_ID="123-456-7890"
```

**Capabilities enabled**:
- Create and manage campaigns, ad groups, and keywords
- Read performance data (impressions, clicks, conversions, cost)
- Manage bidding strategies and budgets
- Access keyword planner data

**Required Google Ads permissions**:
- Campaign management access
- Reporting access
- Keyword planner access

### LinkedIn Ads MCP Server

```bash
# Install the LinkedIn Ads MCP server
claude-code mcp install linkedin-ads --config mcp-servers/linkedin-ads.json

# Authenticate with LinkedIn
claude-code mcp auth linkedin-ads --oauth

# Set your ad account ID
export LINKEDIN_AD_ACCOUNT_ID="your-account-id"
```

**Capabilities enabled**:
- Create and manage sponsored content campaigns
- Access audience targeting options
- Read campaign analytics
- Manage creative assets

**Required LinkedIn permissions**:
- `r_ads` and `rw_ads` for campaign management
- `r_ads_reporting` for analytics

### Verifying MCP Connections

```bash
# Test all MCP connections
claude-code mcp test --all

# Test a specific server
claude-code mcp test hubspot

# List available capabilities
claude-code mcp capabilities hubspot
```

---

## Configuration

### Step 1: Copy and Customize CONFIG.md

```bash
# Copy the template configuration
cp CONFIG.md my-gtm-config.md
```

Edit `my-gtm-config.md` with your specific business context. The most critical fields to customize:

1. **business_model**: Determines agent assumptions about sales cycles, pricing, and customer behavior
2. **target_customer**: The more specific your persona descriptions, the better every agent's output
3. **product**: Especially `competitors` and `key_differentiators` - these drive battle cards and positioning
4. **goals**: Set realistic targets; agents will flag inconsistencies (e.g., CAC target incompatible with deal size)

### Step 2: Validate Configuration

```bash
# Run validation checks
claude-code team validate --config my-gtm-config.md
```

The validator checks for:
- Required fields are present and non-empty
- LTV:CAC ratio is at least 3:1
- Payback period is mathematically consistent with ACV and CAC
- Conversion rate assumptions (MQL-to-SQL, SQL-to-Close) are realistic
- Budget can support the target number of closed-won deals at the target CAC

### Step 3: Initialize the Team

```bash
# Initialize with your configuration
claude-code team init \
  --template teams/sales-marketing \
  --config my-gtm-config.md \
  --workspace ./gtm-workspace
```

This creates:
- The workspace directory structure
- Agent configurations with your business context injected
- MCP server connections (if configured)
- Git branch for the work

---

## Phase Execution

### Running All Phases

```bash
# Full execution with review gates (recommended for first run)
claude-code team run \
  --config my-gtm-config.md \
  --phases all \
  --review-gates true

# Full execution without review gates (faster, for experienced users)
claude-code team run \
  --config my-gtm-config.md \
  --phases all \
  --review-gates false
```

### Phase 1: Strategy & Foundation

```bash
claude-code team run --phase strategy --config my-gtm-config.md
```

**What happens**:
1. Coordinator analyzes your CONFIG and produces the GTM strategy
2. Brand & Messaging creates the messaging framework based on the strategy
3. Growth Analyst designs the analytics foundation

**Duration**: ~30 minutes

**Review before proceeding**:
- Does the GTM strategy accurately reflect your market understanding?
- Are the personas specific enough to drive targeted campaigns?
- Does the positioning differentiate you from competitors?
- Is the budget allocation aligned with your channel priorities?

```bash
# Review Phase 1 outputs
ls gtm-workspace/strategy/
ls gtm-workspace/messaging/
ls gtm-workspace/analytics/

# Approve and proceed to Phase 2
claude-code team approve --phase strategy
```

### Phase 2: Pipeline Building

```bash
claude-code team run --phase pipeline-building --config my-gtm-config.md
```

**What happens** (4 agents in parallel):
1. Demand Generation designs campaigns, landing pages, and email sequences
2. Sales Enablement builds pitch decks, battle cards, and demo scripts
3. Pipeline Manager configures CRM stages, scoring, and forecasting
4. Customer Success designs onboarding, health scoring, and expansion playbooks

**Duration**: ~45 minutes

**Review before proceeding**:
- Do campaign designs target the right audiences with compelling creative?
- Are battle cards accurate and actionable for your sales team?
- Do CRM stages match your actual sales process?
- Is the onboarding sequence achievable within your product's capabilities?

```bash
# Review Phase 2 outputs
ls gtm-workspace/demand-gen/campaigns/
ls gtm-workspace/sales-enablement/
ls gtm-workspace/pipeline/
ls gtm-workspace/customer-success/

# Approve and proceed to Phase 3
claude-code team approve --phase pipeline-building
```

### Phase 3: Execution & Optimization

```bash
claude-code team run --phase execution --config my-gtm-config.md
```

**What happens** (5 agents in parallel):
1. Demand Generation finalizes campaign configs and A/B test plans
2. Sales Enablement creates training modules and coaching frameworks
3. Pipeline Manager builds operational cadences and stuck-deal coaching
4. Customer Success maps customer journeys and expansion workflows
5. Growth Analyst designs dashboards and experiments

**Duration**: ~60 minutes

**Review before proceeding**:
- Are A/B test designs statistically sound?
- Do training materials cover the full sales process?
- Are dashboards answering the right questions?
- Are experiment hypotheses testable and valuable?

```bash
# Review Phase 3 outputs
ls gtm-workspace/demand-gen/campaign-configs/
ls gtm-workspace/sales-enablement/training/
ls gtm-workspace/analytics/dashboards/

# Approve and proceed to Phase 4
claude-code team approve --phase execution
```

### Phase 4: Analysis & Iteration

```bash
claude-code team run --phase analysis --config my-gtm-config.md
```

**What happens**:
1. Growth Analyst produces performance analysis and recommendations
2. Coordinator synthesizes analysis into strategy updates
3. All agents update playbooks with learnings

**Duration**: ~20 minutes

**Note**: Phase 4 is most valuable when run after real execution data is available. On the first run, it produces template analysis frameworks and hypothetical recommendations based on benchmarks.

```bash
# Review final outputs
ls gtm-workspace/analytics/
ls gtm-workspace/strategy/iteration-brief.md

# Commit all work
claude-code team commit --message "Complete GTM execution cycle 1"
```

---

## Post-Deployment

### Ongoing Usage Patterns

| Cadence | What to Run | Purpose |
|---------|-------------|---------|
| Weekly | Growth Analyst (single agent) | Campaign performance review |
| Bi-weekly | Demand Gen + Growth Analyst | Campaign optimization cycle |
| Monthly | Phase 4 (Analysis) | Monthly performance review and budget reallocation |
| Quarterly | Phases 1 + 4 | Strategy refresh with quarterly data |
| As needed | Sales Enablement (single agent) | New battle cards, updated pitch deck |
| As needed | Customer Success (single agent) | Churn analysis, onboarding updates |

### Integrating with Existing Workflows

**With existing CRM data**:
```bash
# Export CRM data for analysis
claude-code mcp export hubspot --type deals --period last-90-days > crm-data.json

# Run Pipeline Manager with real data
claude-code agent run pipeline-manager \
  --task "Analyze pipeline health and forecast accuracy" \
  --data crm-data.json
```

**With existing campaign data**:
```bash
# Export ad platform data
claude-code mcp export google-ads --period last-30-days > ads-data.json

# Run Growth Analyst with real performance data
claude-code agent run growth-analyst \
  --task "Analyze campaign performance and recommend budget reallocation" \
  --data ads-data.json
```

**With existing customer data**:
```bash
# Run Customer Success with product usage data
claude-code agent run customer-success \
  --task "Identify churn risks and design intervention workflows" \
  --data product-usage.json
```

### Customizing Agent Behavior

To customize an agent's behavior for your specific needs, edit the corresponding AGENTS.md file:

```bash
# Example: Add industry-specific knowledge to the Coordinator
vim teams/sales-marketing/agents/coordinator/AGENTS.md

# Add to the system prompt:
# - Industry-specific regulations or compliance requirements
# - Company-specific brand guidelines or messaging constraints
# - Historical performance data or benchmarks
# - Specific competitive intelligence
```

### Troubleshooting

| Issue | Cause | Resolution |
|-------|-------|------------|
| Agent produces generic content | CONFIG.md not specific enough | Add more detail to target_customer, product, and competitors sections |
| MCP connection fails | Invalid credentials or permissions | Run `claude-code mcp test [server]` and check error messages |
| Phase 2 output is inconsistent | Phase 1 strategy is too vague | Re-run Phase 1 with more specific CONFIG inputs |
| Cost exceeds estimate | Large context from MCP data | Reduce MCP data scope or use budget configuration |
| Agent conflicts in Phase 2 | Messaging inconsistency | Ensure Brand & Messaging completes before other Phase 2 agents start |

### Backing Up and Versioning

```bash
# Tag each completed cycle
git tag -a gtm-cycle-1 -m "First GTM execution cycle"

# Archive workspace for comparison
cp -r gtm-workspace gtm-workspace-cycle-1

# Compare cycles
diff -r gtm-workspace-cycle-1/strategy gtm-workspace-cycle-2/strategy
```
