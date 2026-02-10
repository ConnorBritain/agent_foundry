# Sales & Marketing Team Configuration

```yaml
# Sales & Marketing Team Configuration
# Initialized: 2026-02-10T00:00:00Z
# Version: 1.0.0

# ============================================================
# BUSINESS MODEL
# ============================================================
# Define the core business model to calibrate all agents'
# assumptions about sales cycles, pricing, and customer behavior.

business_model: b2b_saas
# Options: b2b_saas | b2c_saas | marketplace | e_commerce | services
# - b2b_saas: Software sold to businesses, recurring revenue
# - b2c_saas: Software sold to consumers, recurring revenue
# - marketplace: Two-sided platform connecting buyers and sellers
# - e_commerce: Direct product sales to consumers
# - services: Professional or managed services

sales_motion: sales_led
# Options: product_led | sales_led | hybrid
# - product_led: Users self-serve, upgrade from free/trial
# - sales_led: Sales team drives deals, demos and contracts
# - hybrid: PLG for SMB, sales-assisted for mid-market+

deal_size: mid_market
# Options: smb | mid_market | enterprise
# - smb: ACV < $10K, high velocity, minimal customization
# - mid_market: ACV $10K-$100K, 2-6 week cycles, some customization
# - enterprise: ACV > $100K, 3-12 month cycles, heavy customization

sales_cycle_days: 45
# Average days from first touch to closed-won.
# SMB: 7-21 | Mid-market: 30-90 | Enterprise: 90-365

# ============================================================
# TARGET CUSTOMER
# ============================================================
# Define who you are selling to. The more specific, the better
# every agent's output will be.

target_customer:
  industry: horizontal
  # Examples: horizontal, fintech, healthcare, e-commerce, devtools
  # Use "horizontal" if you sell across industries

  company_size: 50-500
  # Employee count range of target companies
  # Examples: 1-10, 10-50, 50-500, 500-5000, 5000+

  job_titles:
    - VP of Engineering
    - CTO
    - Engineering Manager
    - Head of Platform
  # List the titles of people who buy, champion, and influence.
  # Separate economic buyer, champion, and end users if distinct.

  pain_points:
    - Slow deployment cycles reducing team velocity
    - Lack of visibility into production systems
    - Too much time spent on infrastructure vs product
  # Top 3-5 pain points your product solves.
  # Be specific. "Saves time" is not a pain point.

  buying_triggers:
    - Failed deployment or outage
    - New VP/CTO hire wanting to modernize
    - Scaling past 20 engineers
    - Board mandate to improve delivery speed
  # Events that create urgency to buy.

# ============================================================
# PRODUCT CONTEXT
# ============================================================

product:
  name: "[Your Product Name]"
  category: "[e.g., Developer Platform, Marketing Automation, CRM]"

  primary_value_prop: >
    [One sentence: what you do, for whom, and what outcome they get]

  key_differentiators:
    - "[How you are different from alternative 1]"
    - "[How you are different from alternative 2]"
    - "[How you are different from alternative 3]"

  pricing:
    model: per_seat  # per_seat | usage_based | flat_rate | hybrid
    entry_price: 500  # Monthly entry price in dollars
    average_acv: 36000  # Average annual contract value
    expansion_potential: 2.5x  # Typical expansion multiple over 3 years

  competitors:
    primary:
      - name: "[Competitor 1]"
        positioning: "[How they position themselves]"
        weakness: "[Their key weakness you exploit]"
      - name: "[Competitor 2]"
        positioning: "[How they position themselves]"
        weakness: "[Their key weakness you exploit]"
    alternatives:
      - "[Category alternative, e.g., 'doing nothing', 'spreadsheets', 'building in-house']"

# ============================================================
# CHANNELS
# ============================================================
# Which acquisition channels to build campaigns for.

channels:
  paid:
    - google_ads
    - linkedin_ads
    # Options: google_ads | meta_ads | linkedin_ads | twitter_ads
    #          | reddit_ads | capterra | g2 | other
    # LinkedIn is typically best for B2B. Meta for B2C/PLG.
    # Google for high-intent search capture.

  organic:
    - seo
    - content_marketing
    # Options: seo | content_marketing | social | community
    #          | podcast | youtube | newsletter
    # Content and SEO are long-term investments.
    # Community works well for developer and technical products.

  direct:
    - outbound
    # Options: outbound | partnerships | events | referral
    #          | product_led_virality
    # Outbound is essential for enterprise.
    # Partnerships for ecosystem plays.

# ============================================================
# TOOLS & INTEGRATIONS
# ============================================================
# Specify your marketing and sales stack so agents can
# generate tool-specific configurations and workflows.

tools:
  crm: hubspot
  # Options: hubspot | salesforce | pipedrive | close | none
  # CRM is the system of record for the pipeline.

  marketing_automation: hubspot
  # Options: hubspot | marketo | pardot | activecampaign | none
  # Marketing automation handles email, scoring, and workflows.

  analytics: google_analytics
  # Options: google_analytics | mixpanel | amplitude | heap
  #          | posthog | none
  # Product/web analytics for understanding user behavior.

  attribution: custom
  # Options: custom | bizible | dreamdata | hubspot_native | none
  # Attribution connects marketing touches to revenue.
  # "custom" means agents will design an attribution model for you.

  enrichment: none
  # Options: clearbit | zoominfo | apollo | none
  # Data enrichment for lead scoring and account intelligence.

  communication: slack
  # Options: slack | teams | none
  # Where alerts and notifications are delivered.

# ============================================================
# GOALS & METRICS
# ============================================================
# Define the targets that all agents optimize toward.
# Be realistic. Agents will flag if targets seem inconsistent
# (e.g., low CAC target with enterprise deal sizes).

goals:
  mqls_per_month: 500
  # Marketing Qualified Leads per month.
  # Should be 3-5x SQL target to account for qualification rates.

  sqls_per_month: 100
  # Sales Qualified Leads per month.
  # Leads that meet BANT criteria and are accepted by sales.

  opportunities_per_month: 50
  # Deals in active pipeline per month.

  closed_won_per_month: 15
  # New customers per month.

  cac_target: 3000
  # Target Customer Acquisition Cost in dollars.
  # All-in cost including marketing + sales.
  # Rule of thumb: CAC should be < LTV/3 for healthy unit economics.

  ltv_target: 36000
  # Target Customer Lifetime Value in dollars.
  # LTV = ARPA * Gross Margin * (1 / Churn Rate)

  payback_period_months: 12
  # Months to recover CAC from customer revenue.
  # < 12 months is good. < 6 months is excellent.
  # > 18 months may indicate a business model problem.

  monthly_budget: 50000
  # Total monthly marketing budget in dollars.
  # Includes paid ads, tools, content, events.
  # Does not include headcount.

  target_ltv_cac_ratio: 12.0
  # LTV:CAC ratio target. 3:1 is healthy. 5:1+ is excellent.
  # Below 3:1 means you may be spending too much to acquire.

# ============================================================
# MODEL CONFIGURATION
# ============================================================
# Which model configuration to use for the agent team.

model_config: default
# Options: default | budget | premium
# See MODEL_CONFIGS.md for detailed specifications.

# Override individual agents if needed:
# model_overrides:
#   coordinator: claude-opus-4-6
#   demand_generation: claude-opus-4-6
#   growth_analyst: claude-opus-4-6

# ============================================================
# EXECUTION PREFERENCES
# ============================================================

execution:
  mode: full
  # Options: full | strategy_only | execution_only | analysis_only
  # - full: Run all 4 phases
  # - strategy_only: Phase 1 only
  # - execution_only: Phases 2-3 (assumes strategy exists)
  # - analysis_only: Phase 4 only (assumes execution data exists)

  git_branch: gtm/campaign-{{date}}
  # Branch naming pattern. {{date}} is replaced with YYYY-MM-DD.

  output_format: markdown
  # Options: markdown | notion | google_docs
  # Format for deliverable documents.

  review_gates: true
  # If true, pause between phases for human review.
  # If false, run all phases continuously.

  parallel_execution: true
  # If true, run independent agents in parallel within phases.
  # If false, run all agents sequentially (slower but easier to debug).
```

## Configuration Validation

The Coordinator agent validates the configuration at startup and flags inconsistencies:

| Check | Rule | Action |
|-------|------|--------|
| LTV:CAC ratio | `ltv_target / cac_target >= 3` | Warn if below 3:1, error if below 1:1 |
| Payback period | `cac_target / (average_acv / 12) <= payback_period_months` | Warn if math doesn't add up |
| MQL to SQL conversion | `sqls_per_month / mqls_per_month >= 0.10` | Warn if conversion rate seems unrealistic |
| SQL to Close conversion | `closed_won_per_month / sqls_per_month >= 0.05` | Warn if win rate seems unrealistic |
| Budget vs CAC | `monthly_budget / closed_won_per_month <= cac_target` | Warn if budget can't support target CAC |
| Sales cycle vs deal size | Enterprise deals should have longer cycles | Warn if mismatch |

## Applying Configuration

```bash
# Validate configuration
claude-code team validate --config CONFIG.md

# Apply configuration and initialize team
claude-code team init --config CONFIG.md

# Update configuration mid-run (re-validates)
claude-code team update-config --config CONFIG.md
```
