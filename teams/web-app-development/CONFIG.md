# Web App Development Team Configuration

```yaml
# Web App Development Team Configuration
# Copy this file to CONFIG.local.md and fill in your values.
# CONFIG.local.md is gitignored and safe for sensitive defaults.
#
# Initialized: 2026-02-10T00:00:00Z

# ──────────────────────────────────────────────
# Project Identity
# ──────────────────────────────────────────────
project_name: "my-saas-app"
project_description: "A brief description of what the app does and who it serves."
project_type: saas              # Options: saas | marketplace | content_platform | internal_tool
target_audience: b2b            # Options: b2b | b2c | b2b2c

# ──────────────────────────────────────────────
# Authentication
# ──────────────────────────────────────────────
auth_strategy: oauth_only       # Options: oauth_only | email_magic_link | email_password | phone_sms
oauth_providers:                # Applicable when auth_strategy includes OAuth
  - google
  # - github
  # - apple
  # - azure_ad
session_duration_hours: 168     # 7 days default; adjust for security requirements
mfa_enabled: false              # Multi-factor authentication; recommended for B2B

# ──────────────────────────────────────────────
# Payment and Billing
# ──────────────────────────────────────────────
payment_model: subscription     # Options: subscription | one_time | usage_based | freemium | none
stripe_mode: test               # Options: test | live (NEVER set to live until launch)

subscription_plans:
  - name: Free
    stripe_price_id: ""         # Leave empty; RevOps agent will create
    monthly_price_cents: 0
    annual_price_cents: 0
    features:
      - "Up to 3 projects"
      - "Basic analytics"
      - "Community support"
    limits:
      projects: 3
      api_calls_per_month: 1000
      storage_gb: 1

  - name: Pro
    stripe_price_id: ""
    monthly_price_cents: 2900   # $29/month
    annual_price_cents: 29000   # $290/year (save ~17%)
    features:
      - "Unlimited projects"
      - "Advanced analytics"
      - "Priority support"
      - "API access"
      - "Custom integrations"
    limits:
      projects: -1              # -1 = unlimited
      api_calls_per_month: 50000
      storage_gb: 50

  - name: Enterprise
    stripe_price_id: ""
    monthly_price_cents: 9900   # $99/month
    annual_price_cents: 99000   # $990/year (save ~17%)
    features:
      - "Everything in Pro"
      - "SSO / SAML"
      - "Audit logs"
      - "Dedicated support"
      - "SLA guarantee"
      - "Custom contracts"
    limits:
      projects: -1
      api_calls_per_month: -1
      storage_gb: 500

trial:
  enabled: true
  duration_days: 14
  plan: Pro                     # Which plan the trial grants access to
  require_payment_method: false # If true, collect card upfront

dunning:
  retry_attempts: 3
  retry_schedule_days: [3, 5, 7]  # Days after initial failure
  grace_period_days: 7            # Days after final retry before downgrade
  downgrade_to: Free              # Plan to downgrade to after grace period
  notify_on_failure: true         # Email user on payment failure
  notify_before_downgrade: true   # Email user before downgrade

# ──────────────────────────────────────────────
# Tech Stack
# ──────────────────────────────────────────────
stack:
  frontend_framework: nextjs    # Options: nextjs | remix | sveltekit
  frontend_version: "15"
  react_version: "19"
  typescript_version: "5"
  tailwind_version: "4"
  backend: supabase             # Options: supabase | firebase | custom_node
  hosting: vercel               # Options: vercel | netlify | fly_io | railway
  database: supabase_postgres   # Options: supabase_postgres | planetscale | neon | custom_postgres
  auth_provider: supabase_auth  # Options: supabase_auth | clerk | auth0 | custom
  payment_provider: stripe      # Options: stripe | paddle | lemon_squeezy | none
  error_tracking: sentry        # Options: sentry | bugsnag | none
  analytics: vercel_analytics   # Options: vercel_analytics | plausible | posthog | none

# ──────────────────────────────────────────────
# Deployment
# ──────────────────────────────────────────────
deployment_region: us_east      # Options: us_east | us_west | eu_west | ap_southeast | multi_region

environments:
  development:
    supabase_project: ""        # Created by Cloud/DevOps agent
    vercel_project: ""          # Created by Cloud/DevOps agent
    stripe_mode: test
    url: "http://localhost:3000"

  staging:
    supabase_project: ""
    vercel_project: ""
    stripe_mode: test
    url: ""                     # Set after Vercel deployment

  production:
    supabase_project: ""
    vercel_project: ""
    stripe_mode: live           # Only after launch approval
    url: ""                     # Set after custom domain configuration
    custom_domain: ""           # e.g., "app.example.com"

github:
  org_or_user: ""               # GitHub org or username
  repo_name: ""                 # Repository name
  default_branch: main
  branch_protection: true       # Require PR reviews and CI pass
  required_checks:
    - typecheck
    - lint
    - test
    - build

# ──────────────────────────────────────────────
# Cost and Budget
# ──────────────────────────────────────────────
cost_budget:
  monthly_limit_usd: 50        # Total infrastructure spend limit
  alert_threshold: 0.80        # Alert at 80% of limit
  breakdown:
    supabase_usd: 25           # Supabase Pro plan
    vercel_usd: 20             # Vercel Pro plan
    stripe_percentage: 2.9     # Stripe fee percentage
    stripe_fixed_cents: 30     # Stripe fixed fee per transaction
    sentry_usd: 0              # Sentry free tier
    github_usd: 0              # GitHub free tier (public) or included

agent_budget:
  model_config: default         # Options: budget | default | premium | hybrid_a | hybrid_b
  max_total_tokens: 1050000
  max_total_cost_usd: 105

# ──────────────────────────────────────────────
# Timeline
# ──────────────────────────────────────────────
launch_timeline:
  mvp_deadline: "2026-03-15"    # When MVP must be ready
  public_launch: "2026-04-01"   # When the app goes live
  beta_users: 10                # Number of beta testers before public launch

# ──────────────────────────────────────────────
# Features (toggle on/off)
# ──────────────────────────────────────────────
features:
  marketing_site: true
  blog: false
  changelog: false
  docs_site: false
  dark_mode: true
  i18n: false
  pwa: false
  email_notifications: true
  in_app_notifications: false
  file_uploads: true
  realtime: false
  api_keys: false               # User-facing API key management
  webhooks_outbound: false      # User-facing webhook configuration
  audit_log: false
  admin_panel: false
  onboarding_wizard: true

# ──────────────────────────────────────────────
# SEO and Marketing
# ──────────────────────────────────────────────
seo:
  site_title: "My SaaS App"
  site_description: "A brief marketing description for search engines."
  og_image: "/og-image.png"
  twitter_handle: ""
  google_site_verification: ""

analytics_events:
  - signup_started
  - signup_completed
  - pricing_page_viewed
  - checkout_started
  - checkout_completed
  - feature_used
  - upgrade_clicked

# ──────────────────────────────────────────────
# Compliance and Legal
# ──────────────────────────────────────────────
compliance:
  cookie_consent: true          # Show cookie consent banner
  privacy_policy_url: ""
  terms_of_service_url: ""
  gdpr_compliant: false         # If true, adds data export/deletion features
  data_residency: ""            # Required region for data storage
```

## Usage

1. Copy this file:
   ```bash
   cp CONFIG.md CONFIG.local.md
   ```

2. Edit `CONFIG.local.md` with your project-specific values.

3. Pass it to the team runner:
   ```bash
   claude-agent team run ./teams/web-app-development --config CONFIG.local.md
   ```

## Configuration Validation

The Coordinator agent validates the configuration at the start of Phase 1 and will report errors for:

- Missing required fields (`project_name`, `project_type`, `auth_strategy`, `payment_model`)
- Invalid enum values (e.g., `project_type: blog` is not a valid option)
- Inconsistent settings (e.g., `payment_model: none` with subscription plans defined)
- Budget conflicts (e.g., `max_total_cost_usd` lower than the selected `model_config` estimate)
- Timeline issues (e.g., `mvp_deadline` in the past)

## Environment Variables

These must be set in your shell before running the team. They are never stored in config files.

```bash
# Required
export SUPABASE_ACCESS_TOKEN=""      # From supabase.com/dashboard/account/tokens
export SUPABASE_DB_PASSWORD=""       # Set during project creation
export VERCEL_TOKEN=""               # From vercel.com/account/tokens
export STRIPE_SECRET_KEY=""          # From dashboard.stripe.com/apikeys (use sk_test_*)
export STRIPE_WEBHOOK_SECRET=""      # From Stripe webhook endpoint configuration
export GITHUB_TOKEN=""               # From github.com/settings/tokens

# Optional
export SENTRY_DSN=""                 # From sentry.io project settings
export SENTRY_AUTH_TOKEN=""          # For source map uploads
export NEXT_PUBLIC_SUPABASE_URL=""   # Set after Supabase project creation
export NEXT_PUBLIC_SUPABASE_ANON_KEY="" # Set after Supabase project creation
```
