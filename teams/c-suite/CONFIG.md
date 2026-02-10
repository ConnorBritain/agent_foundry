# C-Suite Team Configuration

```yaml
# C-Suite Team Configuration
# Copy this file to CONFIG.local.md and fill in your values.
# CONFIG.local.md is gitignored and safe for sensitive context.
#
# Initialized: 2026-02-10T00:00:00Z

# ──────────────────────────────────────────────
# Business Identity
# ──────────────────────────────────────────────
business_name: "My Startup"
business_description: |
  A 2-3 sentence description of the business idea. Include: what the product does,
  who it serves, and what problem it solves.
business_stage: idea              # Options: idea | pre_seed | seed | series_a | growth | restructuring
business_model: saas              # Options: saas | marketplace | ecommerce | services | content | hardware | other

# ──────────────────────────────────────────────
# Market Context
# ──────────────────────────────────────────────
target_market:
  industry: technology            # Options: technology | healthcare | finance | education | retail | manufacturing | other
  geography: us                   # Options: us | europe | global | asia | latam | other
  segment: smb                    # Options: consumer | smb | mid_market | enterprise | government
  size_estimate: ""               # Optional: your estimate of market size (e.g., "$5B TAM")

competitors:
  - name: ""                      # Known competitor name
    url: ""                       # Competitor website
    notes: ""                     # What they do well, what they do poorly
  # - name: ""
  #   url: ""
  #   notes: ""

# ──────────────────────────────────────────────
# Founding Team
# ──────────────────────────────────────────────
founders:
  - name: ""
    role: "CEO"
    background: ""                # 1-2 sentences on relevant experience
    equity_percent: 50
  # - name: ""
  #   role: "CTO"
  #   background: ""
  #   equity_percent: 50

team_size_current: 1              # Current number of people (including founders)
team_size_target_12mo: 5          # Target team size in 12 months

# ──────────────────────────────────────────────
# Financial Constraints
# ──────────────────────────────────────────────
funding:
  current_cash: 0                 # Current cash on hand (USD)
  monthly_burn: 0                 # Current monthly expenses (USD)
  funding_seeking: true           # Are you planning to raise funding?
  funding_target: 500000          # Target raise amount (USD)
  funding_type: pre_seed          # Options: bootstrapped | pre_seed | seed | series_a | series_b | other
  valuation_expectation: ""       # Optional: expected pre-money valuation

revenue:
  current_mrr: 0                  # Current monthly recurring revenue (USD)
  current_arr: 0                  # Current annual recurring revenue (USD)
  customers_current: 0            # Current number of paying customers
  pricing_model: subscription     # Options: subscription | transaction | usage_based | freemium | one_time | custom

# ──────────────────────────────────────────────
# Product Context
# ──────────────────────────────────────────────
product:
  stage: concept                  # Options: concept | prototype | mvp | launched | growth
  platform: web                   # Options: web | mobile | desktop | api | hardware | multi_platform
  tech_stack_preference: ""       # Optional: any technology preferences or constraints
  key_features:                   # Top 3-5 features of the product
    - ""
    - ""
    - ""
  differentiation: ""             # What makes this different from competitors (1-2 sentences)

# ──────────────────────────────────────────────
# Strategic Priorities
# ──────────────────────────────────────────────
priorities:
  primary_goal: launch_mvp        # Options: launch_mvp | raise_funding | acquire_customers | scale_revenue | pivot | restructure
  timeline_months: 6              # Timeline for primary goal (months)
  top_risks:                      # Top 3 concerns or unknowns
    - ""
    - ""
    - ""
  key_assumptions:                # Assumptions the plan should test
    - ""
    - ""

# ──────────────────────────────────────────────
# Legal Context
# ──────────────────────────────────────────────
legal:
  entity_formed: false            # Has the company been formally incorporated?
  entity_type: ""                 # If formed: llc | c_corp | s_corp | sole_prop | other
  jurisdiction: ""                # State/country of incorporation
  regulatory_concerns:            # Industry-specific regulations to consider
    - ""
  ip_assets:                      # Existing IP (patents, trademarks, domain names)
    - ""

# ──────────────────────────────────────────────
# Output Preferences
# ──────────────────────────────────────────────
outputs:
  financial_model: true           # Generate Google Sheets financial model
  business_plan: true             # Generate Notion business plan
  pitch_deck: true                # Generate Google Slides pitch deck
  product_roadmap: true           # Generate Linear product roadmap
  sales_playbook: true            # Generate Notion sales playbook
  marketing_plan: true            # Generate Notion marketing plan
  legal_checklist: true           # Generate Notion legal checklist
  org_chart: true                 # Generate org chart with hiring plan

  projection_years: 3             # Financial projection horizon (3 or 5 years)
  pitch_deck_slides: 10           # Number of pitch deck slides (8-15)

# ──────────────────────────────────────────────
# MCP Server Integration
# ──────────────────────────────────────────────
integrations:
  google_sheets: true             # Required for financial model
  notion: true                    # Required for business plan and playbooks
  linear: false                   # Optional: product roadmap
  google_slides: false            # Optional: pitch deck

# ──────────────────────────────────────────────
# Agent Budget
# ──────────────────────────────────────────────
agent_budget:
  model_config: default           # Options: budget | default | premium | hybrid_finance
  max_total_tokens: 840000        # 700K base + 20% buffer
  max_total_cost_usd: 150
  execution_mode: hybrid          # Options: sequential | hybrid | swarm
```

## Usage

1. Copy this file:
   ```bash
   cp CONFIG.md CONFIG.local.md
   ```

2. Edit `CONFIG.local.md` with your business-specific context. At minimum, fill in:
   - `business_name` and `business_description`
   - `business_stage` and `business_model`
   - `target_market` section
   - `funding` section
   - `priorities` section

3. Pass it to the team runner:
   ```bash
   claude-agent team run ./teams/c-suite --config CONFIG.local.md
   ```

## Configuration Validation

The CEO agent validates the configuration at the start of Phase 1 and will report errors for:

- Missing required fields (`business_name`, `business_description`, `business_model`)
- Inconsistent settings (e.g., `funding_seeking: false` with `funding_target: 500000`)
- Unrealistic combinations (e.g., `business_stage: idea` with `customers_current: 1000`)
- Missing market context (empty `target_market` section)
- Budget conflicts (`max_total_cost_usd` lower than selected `model_config` estimate)

## Environment Variables

Set these in your shell if using MCP server integrations:

```bash
# Google Sheets (for financial model)
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account.json"

# Notion (for business plan, playbooks)
export NOTION_API_KEY="secret_..."

# Linear (optional, for product roadmap)
export LINEAR_API_KEY="lin_api_..."

# Google Slides (optional, for pitch deck)
# Uses same GOOGLE_APPLICATION_CREDENTIALS as Sheets
```
