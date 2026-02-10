# Deployment Guide

Step-by-step instructions for setting up the environment, configuring services, and running the Web App Development Team.

---

## Prerequisites

### Required Accounts

Create accounts on the following services before running the team:

| Service | URL | Purpose | Required Tier |
|---------|-----|---------|--------------|
| GitHub | github.com | Code repository and CI/CD | Free |
| Supabase | supabase.com | Database, auth, storage, edge functions | Free |
| Vercel | vercel.com | Hosting and deployment | Hobby (Free) |
| Stripe | stripe.com | Payments and billing | Free (test mode) |

### Optional Accounts

| Service | URL | Purpose | Required Tier |
|---------|-----|---------|--------------|
| Sentry | sentry.io | Error tracking | Developer (Free) |

### Required CLI Tools

Install the following tools on your local machine:

```bash
# Node.js 20+ (LTS)
# Visit https://nodejs.org or use a version manager:
nvm install 20
nvm use 20

# Verify
node --version  # Should be >= 20.0.0
npm --version   # Should be >= 10.0.0

# Supabase CLI
npm install -g supabase

# Verify
supabase --version

# Stripe CLI
# macOS:
brew install stripe/stripe-cli/stripe
# Linux:
# Download from https://github.com/stripe/stripe-cli/releases

# Verify
stripe --version

# Vercel CLI
npm install -g vercel

# Verify
vercel --version

# GitHub CLI
# macOS:
brew install gh
# Linux:
# See https://github.com/cli/cli/blob/trunk/docs/install_linux.md

# Verify
gh --version
```

### Authentication

Log in to each CLI tool:

```bash
# GitHub
gh auth login
# Follow the prompts to authenticate via browser

# Supabase
supabase login
# Opens browser for authentication

# Vercel
vercel login
# Opens browser for authentication

# Stripe
stripe login
# Opens browser for authentication
```

---

## Environment Variables

### Step 1: Generate API Keys

#### Supabase

1. Go to https://supabase.com/dashboard/account/tokens
2. Click "Generate new token"
3. Name it "web-app-dev-team"
4. Copy the token

#### Vercel

1. Go to https://vercel.com/account/tokens
2. Click "Create"
3. Name it "web-app-dev-team"
4. Set scope to your account or team
5. Copy the token

#### Stripe

1. Go to https://dashboard.stripe.com/test/apikeys
2. Copy the "Secret key" (starts with `sk_test_`)
3. For the webhook secret, you will create this after the webhook endpoint is configured in Phase 3

#### GitHub

1. Go to https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Name it "web-app-dev-team"
4. Select scopes: `repo`, `workflow`, `admin:repo_hook`
5. Copy the token

#### Sentry (Optional)

1. Go to https://sentry.io and create a new project (Next.js)
2. Copy the DSN from the project settings
3. For the auth token, go to Settings > Auth Tokens > Create New Token

### Step 2: Set Environment Variables

Create a `.env.team` file in the project root (this file should be gitignored):

```bash
# Required - Service Access Tokens
SUPABASE_ACCESS_TOKEN="sbp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
VERCEL_TOKEN="xxxxxxxxxxxxxxxxxxxxxxxx"
STRIPE_SECRET_KEY="sk_test_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
GITHUB_TOKEN="ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Required - Set after Supabase project creation (Phase 1)
NEXT_PUBLIC_SUPABASE_URL=""
NEXT_PUBLIC_SUPABASE_ANON_KEY=""
SUPABASE_SERVICE_ROLE_KEY=""
SUPABASE_DB_PASSWORD=""

# Required - Set after Stripe webhook creation (Phase 3)
STRIPE_WEBHOOK_SECRET=""

# Required - Stripe publishable key (for client-side)
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY="pk_test_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Optional - Sentry
SENTRY_DSN=""
SENTRY_AUTH_TOKEN=""

# Optional - Custom domain
CUSTOM_DOMAIN=""
```

Load the environment variables:

```bash
# Option 1: Source the file
source .env.team

# Option 2: Use direnv (recommended)
# Install direnv, then:
cp .env.team .envrc
direnv allow
```

### Step 3: Verify Environment

Run the verification script to ensure all required variables are set:

```bash
# Quick verification
echo "Supabase: ${SUPABASE_ACCESS_TOKEN:+SET}"
echo "Vercel: ${VERCEL_TOKEN:+SET}"
echo "Stripe: ${STRIPE_SECRET_KEY:+SET}"
echo "GitHub: ${GITHUB_TOKEN:+SET}"
```

All should print "SET". If any show blank, revisit the corresponding step above.

---

## MCP Server Setup

The team uses MCP (Model Context Protocol) servers to interact with external services. Configure each server before running the team.

### Supabase MCP Server

The Supabase MCP server provides direct access to database operations, auth configuration, and storage management.

```bash
# Verify Supabase CLI is authenticated
supabase projects list

# The MCP server configuration is at:
# mcp-servers/supabase.json
```

The Cloud/DevOps agent uses this to:
- Create and configure the Supabase project
- Run migrations
- Configure auth providers
- Set up storage buckets

### Vercel MCP Server

```bash
# Verify Vercel CLI is authenticated
vercel whoami

# The MCP server configuration is at:
# mcp-servers/vercel.json
```

The Cloud/DevOps agent uses this to:
- Create the Vercel project
- Set environment variables
- Trigger deployments
- Configure domains

### Stripe MCP Server

```bash
# Verify Stripe CLI is authenticated
stripe config --list

# The MCP server configuration is at:
# mcp-servers/stripe.json
```

The RevOps agent uses this to:
- Create products and prices
- Configure webhook endpoints
- Set up the billing portal
- Query subscription data

### GitHub MCP Server

```bash
# Verify GitHub CLI is authenticated
gh auth status

# The MCP server configuration is at:
# mcp-servers/github.json
```

The Cloud/DevOps agent uses this to:
- Create the repository
- Configure branch protection
- Set repository secrets
- Manage GitHub Actions workflows

---

## Running the Team

### Step 1: Configure the Project

```bash
# Navigate to the template directory
cd teams/web-app-development

# Copy and edit the configuration
cp CONFIG.md CONFIG.local.md

# Edit CONFIG.local.md with your project settings
# At minimum, fill in:
#   - project_name
#   - project_description
#   - project_type
#   - target_audience
#   - auth_strategy
#   - payment_model
#   - subscription_plans (if payment_model is subscription)
#   - github.org_or_user
#   - github.repo_name
```

### Step 2: Select Model Configuration

Choose your model configuration in `CONFIG.local.md`:

```yaml
agent_budget:
  model_config: default  # Options: budget, default, premium, hybrid_a, hybrid_b
```

See `MODEL_CONFIGS.md` for detailed comparison.

### Step 3: Run Phase 1 (Foundation)

```bash
claude-agent team run ./teams/web-app-development \
  --config CONFIG.local.md \
  --mode hybrid \
  --phase 1

# Expected duration: ~30 minutes
# Expected cost: ~$20 (default config)
```

**What happens:**
1. Coordinator parses config and writes architecture decisions
2. Cloud/DevOps creates GitHub repo, Supabase project, Vercel project
3. Database Engineer designs schema and writes migration 001
4. Senior Full-Stack scaffolds Next.js project

**After Phase 1 completes:**
- Update `.env.team` with the Supabase URL and keys created by Cloud/DevOps
- Review `ARCHITECTURE.md` for any decisions you want to override
- Verify the GitHub repo was created and CI workflow is present

```bash
# Update environment with Supabase values
# The Cloud/DevOps agent will output these values
export NEXT_PUBLIC_SUPABASE_URL="https://xxxxx.supabase.co"
export NEXT_PUBLIC_SUPABASE_ANON_KEY="eyJ..."
export SUPABASE_SERVICE_ROLE_KEY="eyJ..."
```

### Step 4: Run Phase 2 (Core Features)

```bash
claude-agent team run ./teams/web-app-development \
  --config CONFIG.local.md \
  --mode hybrid \
  --phase 2

# Expected duration: ~60 minutes
# Expected cost: ~$40 (default config)
```

**What happens:**
1. Senior Full-Stack builds auth flows, dashboard, CRUD views
2. Database Engineer writes RLS policies and edge functions
3. Marketing Frontend builds landing and pricing pages
4. QA/Test sets up Playwright and writes initial E2E tests

**After Phase 2 completes:**
- Test authentication flow manually (signup, login, logout)
- Review the marketing landing page
- Verify E2E tests pass locally

### Step 5: Run Phase 3 (Integration & Revenue)

```bash
# Start Stripe webhook forwarding (in a separate terminal)
stripe listen --forward-to localhost:3000/api/webhooks/stripe

# Note the webhook signing secret output and set it:
export STRIPE_WEBHOOK_SECRET="whsec_..."

# Run Phase 3
claude-agent team run ./teams/web-app-development \
  --config CONFIG.local.md \
  --mode hybrid \
  --phase 3

# Expected duration: ~45 minutes
# Expected cost: ~$30 (default config)
```

**What happens:**
1. Senior Full-Stack builds payment UI and checkout flow
2. RevOps configures Stripe products, prices, webhooks, billing portal
3. Database Engineer writes payment tables and webhook helpers
4. Cloud/DevOps configures webhook endpoints and secrets
5. Marketing Frontend integrates pricing page with Stripe

**After Phase 3 completes:**
- Test a complete checkout with Stripe test card (4242 4242 4242 4242)
- Verify the webhook processes correctly (subscription created in DB)
- Test the billing portal

### Step 6: Run Phase 4 (Launch Prep)

```bash
claude-agent team run ./teams/web-app-development \
  --config CONFIG.local.md \
  --mode hybrid \
  --phase 4

# Expected duration: ~30 minutes
# Expected cost: ~$15 (default config)
```

**What happens:**
1. QA/Test runs full E2E suite including payment flows
2. RevOps tests complete payment lifecycle
3. Cloud/DevOps deploys to production and sets up monitoring
4. Marketing Frontend does final SEO and accessibility audit
5. Coordinator reviews everything and produces launch checklist

**After Phase 4 completes:**
- Review `LAUNCH_CHECKLIST.md`
- Verify production deployment is accessible
- Check monitoring is active (Sentry, Vercel Analytics)
- Make the go/no-go launch decision

### Running All Phases at Once

If you prefer to run all phases sequentially without manual intervention between phases:

```bash
claude-agent team run ./teams/web-app-development \
  --config CONFIG.local.md \
  --mode hybrid \
  --phase all

# Expected duration: ~2.75 hours
# Expected cost: ~$105 (default config)
```

Note: Running all phases at once means you cannot update environment variables between phases. Ensure all variables are set before starting, or the agents will use placeholder values and you will need to update them post-run.

---

## Post-Deployment Verification

After the team completes, verify the deployment manually:

### 1. Application Health

```bash
# Check the health endpoint
curl -s https://your-app.vercel.app/api/health | jq .

# Expected response:
# {
#   "status": "healthy",
#   "timestamp": "2026-...",
#   "database": "connected",
#   "stripe": "connected"
# }
```

### 2. Authentication

1. Visit the signup page and create a test account
2. Verify the email confirmation (if email auth enabled)
3. Log in and verify dashboard access
4. Log out and verify redirect to login

### 3. Payment Flow

1. Log in as a test user
2. Navigate to upgrade/pricing
3. Select a plan and complete checkout with test card `4242 4242 4242 4242`
4. Verify subscription is active in the dashboard
5. Open the billing portal and verify plan display
6. Check Supabase for the subscription record

### 4. Marketing Pages

1. Visit the landing page
2. Check mobile responsiveness (Chrome DevTools)
3. Run Lighthouse audit (target: >= 90 on all categories)
4. Verify meta tags and OG tags (use https://metatags.io)

### 5. Monitoring

1. Check Sentry for any errors
2. Check Vercel Analytics for traffic data
3. Verify GitHub Actions CI passes on the latest commit

---

## Switching to Production Stripe

When you are ready to go live with real payments:

1. **Update Stripe keys:**
   ```bash
   # In Vercel environment variables (production only):
   STRIPE_SECRET_KEY="sk_live_..."
   NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY="pk_live_..."
   ```

2. **Create production webhook endpoint in Stripe Dashboard:**
   - URL: `https://your-domain.com/api/webhooks/stripe`
   - Events: Same as test webhook
   - Copy the new webhook signing secret

3. **Update webhook secret:**
   ```bash
   STRIPE_WEBHOOK_SECRET="whsec_..." # New production secret
   ```

4. **Create production products and prices:**
   - The RevOps agent created test-mode products. You need to recreate them in live mode, or use Stripe's "copy to live mode" feature.

5. **Redeploy:**
   ```bash
   vercel --prod
   ```

6. **Test with a real card** (use a low-value plan, then refund).

---

## Rollback Procedures

### Vercel Deployment Rollback

```bash
# List recent deployments
vercel ls

# Rollback to a specific deployment
vercel rollback <deployment-url>

# Or use the Vercel Dashboard:
# Go to Deployments > click the three dots on a previous deployment > Promote to Production
```

### Database Migration Rollback

```bash
# Connect to Supabase
supabase db remote commit

# Manually apply a rollback migration
# Each migration file should have a corresponding rollback section
# or a separate rollback migration file

# Example: rollback migration 004
supabase db push --include 004_payment_tables_rollback.sql
```

### Stripe Rollback

Stripe changes (products, prices) cannot be "rolled back" in the traditional sense. Instead:
- Archive products and prices that should no longer be available
- Create new products/prices to replace them
- Update the application to reference the new IDs

### Full Rollback

If a critical issue requires reverting everything:

1. Rollback Vercel deployment to last known good version
2. Apply database rollback migrations
3. Update Stripe webhook to point to the rolled-back deployment
4. Verify health check passes
5. Monitor error rates for 30 minutes

See `scenarios/deployment-rollback.md` for detailed rollback scenarios.

---

## Troubleshooting

### Common Issues

**Supabase project creation fails:**
- Verify `SUPABASE_ACCESS_TOKEN` is valid
- Check if you have reached the free tier project limit (2 projects)
- Ensure the project name is unique

**Vercel deployment fails:**
- Check build logs in Vercel Dashboard
- Verify all environment variables are set
- Ensure `next build` passes locally

**Stripe webhook not receiving events:**
- Verify the webhook URL is correct and publicly accessible
- Check that the correct events are selected in Stripe Dashboard
- Verify `STRIPE_WEBHOOK_SECRET` matches the webhook endpoint
- If testing locally, ensure `stripe listen` is running

**GitHub Actions CI fails:**
- Check that repository secrets are set correctly
- Verify Node.js version matches local development
- Review the specific step that failed in the Actions log

**RLS errors (permission denied):**
- Verify RLS policies are applied correctly
- Check that the Supabase client is using the correct auth context
- Test with the Supabase SQL editor using `set role authenticated`

**Type errors after schema change:**
- Regenerate database types: `supabase gen types typescript --local > types/database.ts`
- Ensure all agents are using the latest type definitions
