# Recruitment & HR Team Configuration

```yaml
# Recruitment & HR Team Configuration
# Initialized: 2026-02-10T00:00:00Z
#
# Instructions: Fill in all bracketed values before running the team.
# This configuration drives every agent's context and output calibration.
# Be specific -- vague inputs produce generic outputs.

# ─────────────────────────────────────────────
# COMPANY CONTEXT
# ─────────────────────────────────────────────

company_name: [Your Company Name]
company_stage: [pre_seed|seed|series_a|series_b|growth|public]
industry: [saas|fintech|healthtech|ecommerce|devtools|marketplace|hardware|other]
business_model: [b2b|b2c|b2b2c|marketplace|api_platform]
founding_date: [YYYY-MM-DD]
funding_raised: [amount or "bootstrapped"]
runway_months: [number or "profitable"]

# ─────────────────────────────────────────────
# HEADCOUNT & GROWTH
# ─────────────────────────────────────────────

current_headcount: [number]
target_headcount: [number]
hiring_timeline_months: [number]
departments:
  engineering: [current_count]
  product: [current_count]
  design: [current_count]
  sales: [current_count]
  marketing: [current_count]
  operations: [current_count]
  customer_success: [current_count]
  people: [current_count]
  finance: [current_count]

# ─────────────────────────────────────────────
# CULTURE & VALUES
# ─────────────────────────────────────────────

culture:
  # List 3-5 core values. Be specific. "Innovation" is useless.
  # "We ship before we are ready and learn from real usage" is useful.
  values:
    - [value_1: one sentence describing the behavior, not the aspiration]
    - [value_2: one sentence describing the behavior, not the aspiration]
    - [value_3: one sentence describing the behavior, not the aspiration]
    # - [value_4: optional]
    # - [value_5: optional]

  work_model: [remote|hybrid|office]
  # If hybrid, specify:
  hybrid_details:
    office_days_per_week: [number]
    office_locations: [list of cities]
    flexibility: [strict_schedule|team_decides|fully_flexible]

  meeting_culture: [async_first|meeting_heavy|balanced]
  decision_making: [consensus|disagree_and_commit|founder_decides|distributed]
  communication_tools:
    primary: [slack|teams|discord|other]
    async: [notion|confluence|linear|github_discussions|other]
    video: [zoom|meet|teams|around|other]

  # What does your culture actually reward? Be honest.
  rewarded_behaviors:
    - [e.g., "shipping fast even if imperfect"]
    - [e.g., "writing detailed specs before building"]
    - [e.g., "publicly disagreeing with leadership when you have data"]

  # What does your culture actually punish (even if unintentionally)?
  punished_behaviors:
    - [e.g., "raising concerns that slow down a launch"]
    - [e.g., "spending time on documentation instead of features"]

# ─────────────────────────────────────────────
# HIRING PRIORITIES
# ─────────────────────────────────────────────

hiring_priorities:
  # Ordered by urgency. Include level and team.
  open_roles:
    - role: [title]
      level: [junior|mid|senior|staff|principal|director|vp]
      team: [department]
      urgency: [critical|high|medium|low]
      reason: [backfill|new_headcount|new_function]
    - role: [title]
      level: [level]
      team: [department]
      urgency: [urgency]
      reason: [reason]

  must_have_skills:
    - [skill_1]
    - [skill_2]
    - [skill_3]

  nice_to_have_skills:
    - [skill_1]
    - [skill_2]

  # Where have you successfully hired from before?
  proven_sources:
    - [e.g., "referrals from current engineering team"]
    - [e.g., "open source contributors to our project"]
    - [e.g., "LinkedIn outreach to people at [competitor]"]

  # What hiring mistakes have you made?
  lessons_learned:
    - [e.g., "hired for resume over culture fit; person left in 3 months"]
    - [e.g., "skipped reference checks; discovered performance issues too late"]

# ─────────────────────────────────────────────
# COMPENSATION PHILOSOPHY
# ─────────────────────────────────────────────

compensation_philosophy:
  # Where do you want to land vs. market?
  salary_positioning: [50th_percentile|75th_percentile|90th_percentile]

  # Geographic pay strategy
  geo_strategy: [location_based|national_median|sf_benchmark|cost_of_living_adjusted]
  reference_markets: [list of cities/regions for benchmarking]

  equity:
    equity_budget_percent: [percentage of fully diluted shares reserved for employees]
    preferred_vehicle: [iso_options|nso_options|rsus|phantom_equity|profit_sharing]
    standard_vesting: [e.g., "4 years with 1 year cliff"]
    refresh_grants: [yes|no]
    early_exercise: [yes|no]

  benefits_tier: [basic|competitive|exceptional]
  benefits_notes: [any specific benefits you want to offer or avoid]

  variable_compensation:
    sales_commission: [yes|no]
    engineering_bonus: [yes|no]
    company_wide_bonus: [yes|no]
    bonus_structure: [description if applicable]

# ─────────────────────────────────────────────
# PERFORMANCE MANAGEMENT
# ─────────────────────────────────────────────

performance:
  review_cadence: [quarterly|semi_annual|annual]
  goal_framework: [okrs|kpis|rocks|custom]
  goal_setting_cadence: [quarterly|semi_annual|annual]
  feedback_culture: [continuous|structured_cycles|manager_driven]

  # Do you currently have career ladders?
  career_ladders_exist: [yes|no|partial]
  functions_needing_ladders:
    - [engineering]
    - [product]
    - [sales]
    # Add all functions that need career ladder design

  # Current pain points with performance management
  pain_points:
    - [e.g., "reviews feel arbitrary and inconsistent across managers"]
    - [e.g., "no connection between performance and compensation"]
    - [e.g., "high performers leave because they see no growth path"]

# ─────────────────────────────────────────────
# TOOLS & INFRASTRUCTURE
# ─────────────────────────────────────────────

tools:
  ats: [lever|greenhouse|ashby|workable|none]
  hris: [bamboohr|gusto|rippling|workday|justworks|none]
  engagement: [lattice|culture_amp|peakon|officevibe|none]
  learning: [lessonly|trainual|notion|none]
  payroll: [gusto|rippling|adp|justworks|manual]
  benefits_broker: [broker_name|none]
  background_checks: [checkr|goodhire|none]

  # MCP integrations to activate
  mcp_integrations:
    lever: [true|false]
    bamboohr: [true|false]

# ─────────────────────────────────────────────
# CONSTRAINTS & PREFERENCES
# ─────────────────────────────────────────────

constraints:
  budget_for_tools: [monthly_amount or "minimal"]
  legal_jurisdiction: [us_only|us_and_international|international_only]
  compliance_requirements:
    - [e.g., "SOC 2 background checks required"]
    - [e.g., "GDPR compliance for EU candidates"]
    - [e.g., "EEO reporting required"]

  # What should the team NOT do?
  out_of_scope:
    - [e.g., "do not design a parental leave policy; we already have one"]
    - [e.g., "do not create engineering-specific interview questions; our eng team handles that"]

# ─────────────────────────────────────────────
# EXECUTION PREFERENCES
# ─────────────────────────────────────────────

execution:
  model_config: [default|budget|premium]

  # Which phases to run (all by default)
  phases:
    foundation: true
    infrastructure: true
    execution: true
    optimization: true

  # Output preferences
  output:
    format: [markdown|google_docs|notion]
    detail_level: [comprehensive|focused|minimal]
    include_templates: true
    include_examples: true

  # Git configuration for deliverable tracking
  git:
    branch_prefix: "people-ops"
    commit_convention: "conventional"  # feat:, fix:, docs:, etc.
    review_required: true
```

## Configuration Examples

### Seed-Stage Startup (12 people, hiring to 25)

```yaml
company_stage: seed
current_headcount: 12
target_headcount: 25
hiring_timeline_months: 6

culture:
  values:
    - "Ship daily -- progress beats perfection"
    - "Say the hard thing -- silence is more expensive than conflict"
    - "Own the outcome, not just the task"
  work_model: remote
  meeting_culture: async_first

compensation_philosophy:
  salary_positioning: 75th_percentile
  geo_strategy: national_median
  equity:
    equity_budget_percent: 15
    preferred_vehicle: iso_options
    standard_vesting: "4 years with 1 year cliff"
  benefits_tier: competitive

execution:
  model_config: default
```

### Series B Company (80 people, hiring to 150)

```yaml
company_stage: series_b
current_headcount: 80
target_headcount: 150
hiring_timeline_months: 12

culture:
  values:
    - "Customers first -- every decision passes the customer impact test"
    - "High standards, high support -- we expect excellence and invest in people"
    - "Data over opinions -- bring evidence, change minds"
    - "Build to last -- we optimize for the next 10 years, not the next quarter"
  work_model: hybrid
  hybrid_details:
    office_days_per_week: 3
    office_locations: ["San Francisco", "New York"]
    flexibility: team_decides
  meeting_culture: balanced

compensation_philosophy:
  salary_positioning: 75th_percentile
  geo_strategy: cost_of_living_adjusted
  equity:
    equity_budget_percent: 10
    preferred_vehicle: rsus
    standard_vesting: "4 years with 1 year cliff"
    refresh_grants: yes
  benefits_tier: exceptional

execution:
  model_config: premium
```
