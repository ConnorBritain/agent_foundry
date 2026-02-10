# MCP Server Configuration

This directory contains the Model Context Protocol (MCP) server configurations used by the Web App Development Team agents to interact with external services.

---

## Overview

Each JSON file defines an MCP server connection that agents use to perform operations against external APIs. The configurations specify the service endpoint, capabilities, and required credentials.

| MCP Server | Config File | Used By | Purpose |
|-----------|-------------|---------|---------|
| Supabase | `supabase.json` | Cloud/DevOps, Database Engineer | Database operations, auth configuration, storage, edge functions |
| Vercel | `vercel.json` | Cloud/DevOps | Deployments, environment variables, domain management |
| Stripe | `stripe.json` | RevOps | Products, prices, subscriptions, webhooks, billing |
| GitHub | `github.json` | Cloud/DevOps | Repository management, Actions, secrets, branch protection |

---

## Prerequisites

Before running the team, you must have accounts and API credentials for each service. This section explains how to obtain each credential.

### Supabase

**Required environment variables:**
- `SUPABASE_URL` -- Your Supabase project URL
- `SUPABASE_SERVICE_ROLE_KEY` -- Service role key with full database access

**How to obtain:**

1. Create a Supabase account at [supabase.com](https://supabase.com)
2. Create a new project (or the Cloud/DevOps agent will create one during Phase 1)
3. Go to **Project Settings > API**
4. Copy the **Project URL** -- this is your `SUPABASE_URL`
5. Copy the **service_role key** (under "Project API keys") -- this is your `SUPABASE_SERVICE_ROLE_KEY`

You will also need a **Supabase Access Token** for CLI operations:

1. Go to [supabase.com/dashboard/account/tokens](https://supabase.com/dashboard/account/tokens)
2. Click **Generate new token**
3. Name it (e.g., "web-app-dev-team")
4. Copy the token and set it as `SUPABASE_ACCESS_TOKEN`

**What this MCP server provides:**
- **Database:** Run SQL queries, apply migrations, inspect schema
- **Auth:** Configure providers (Google, GitHub, etc.), manage redirect URLs, inspect users
- **Functions:** Deploy and invoke Supabase Edge Functions
- **Storage:** Create buckets, upload files, manage access policies
- **Realtime:** Configure realtime subscriptions and broadcast channels

**CLI verification:**

```bash
# Verify CLI is installed and authenticated
supabase --version
supabase projects list
```

---

### Vercel

**Required environment variables:**
- `VERCEL_TOKEN` -- Personal access token for Vercel API
- `VERCEL_ORG_ID` -- Your Vercel organization or account ID

**How to obtain:**

1. Create a Vercel account at [vercel.com](https://vercel.com)
2. Go to [vercel.com/account/tokens](https://vercel.com/account/tokens)
3. Click **Create** to generate a new token
4. Name it (e.g., "web-app-dev-team")
5. Set the scope to your account or team
6. Copy the token -- this is your `VERCEL_TOKEN`

To find your `VERCEL_ORG_ID`:

1. Go to [vercel.com/account](https://vercel.com/account)
2. Scroll to **Vercel ID** in General settings
3. Copy the ID -- this is your `VERCEL_ORG_ID`

**What this MCP server provides:**
- **Deployments:** Trigger production and preview deployments, list deployment history, rollback
- **Env-vars:** Create, update, and delete environment variables per environment (development, preview, production)
- **Domains:** Add custom domains, configure DNS settings, manage SSL certificates
- **Analytics:** Access Vercel Analytics data, Web Vitals metrics

**CLI verification:**

```bash
# Verify CLI is installed and authenticated
vercel --version
vercel whoami
```

---

### Stripe

**Required environment variables:**
- `STRIPE_SECRET_KEY` -- Stripe secret API key (use `sk_test_` for development)
- `STRIPE_WEBHOOK_SECRET` -- Webhook signing secret for signature verification

**How to obtain:**

1. Create a Stripe account at [stripe.com](https://stripe.com)
2. Go to [dashboard.stripe.com/test/apikeys](https://dashboard.stripe.com/test/apikeys) (ensure you are in **Test mode**)
3. Copy the **Secret key** (starts with `sk_test_`) -- this is your `STRIPE_SECRET_KEY`
4. Copy the **Publishable key** (starts with `pk_test_`) -- set this as `NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY`

For the webhook secret:
1. The `STRIPE_WEBHOOK_SECRET` is created during Phase 3 when the webhook endpoint is configured
2. For local development, run `stripe listen --forward-to localhost:3000/api/webhooks/stripe` and copy the `whsec_` value from the output
3. For production, create a webhook endpoint in the Stripe Dashboard and copy the signing secret

**What this MCP server provides:**
- **Products:** Create and manage product catalog
- **Prices:** Create monthly, annual, and usage-based pricing
- **Subscriptions:** Create, update, cancel, and query subscriptions
- **Webhooks:** Configure webhook endpoints, inspect event delivery
- **Customers:** Create and manage customer records
- **Invoices:** Query invoices, payment history, and billing details

**CLI verification:**

```bash
# Verify CLI is installed and authenticated
stripe --version
stripe config --list
```

---

### GitHub

**Required environment variables:**
- `GITHUB_TOKEN` -- Personal access token with repository and workflow permissions

**How to obtain:**

1. Go to [github.com/settings/tokens](https://github.com/settings/tokens)
2. Click **Generate new token (classic)**
3. Name it (e.g., "web-app-dev-team")
4. Select the following scopes:
   - `repo` -- Full control of private repositories
   - `workflow` -- Update GitHub Actions workflows
   - `admin:repo_hook` -- Manage repository webhooks
5. Click **Generate token**
6. Copy the token (starts with `ghp_`) -- this is your `GITHUB_TOKEN`

Alternatively, use a **fine-grained personal access token** with permissions:
- Repository access: your specific repository
- Permissions: Contents (read/write), Actions (read/write), Secrets (read/write), Administration (read/write)

**What this MCP server provides:**
- **Repos:** Create repositories, manage branch protection rules, configure settings
- **Actions:** Trigger workflows, inspect run results, manage workflow files
- **Secrets:** Create and update repository secrets for CI/CD
- **Deployments:** Create deployment records, track deployment status

**CLI verification:**

```bash
# Verify CLI is installed and authenticated
gh --version
gh auth status
```

---

## Environment Variable Summary

Set all required environment variables before running the team:

```bash
# Supabase
export SUPABASE_ACCESS_TOKEN=""          # CLI access token
export SUPABASE_URL=""                   # Project URL (set after project creation)
export SUPABASE_SERVICE_ROLE_KEY=""      # Service role key (set after project creation)
export SUPABASE_DB_PASSWORD=""           # Database password (set during project creation)

# Vercel
export VERCEL_TOKEN=""                   # Personal access token
export VERCEL_ORG_ID=""                  # Account or organization ID

# Stripe
export STRIPE_SECRET_KEY=""             # sk_test_... (test mode)
export STRIPE_WEBHOOK_SECRET=""         # whsec_... (set after webhook creation)
export NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=""  # pk_test_... (client-side)

# GitHub
export GITHUB_TOKEN=""                  # ghp_... (personal access token)

# Optional
export SENTRY_DSN=""                    # Sentry project DSN
export SENTRY_AUTH_TOKEN=""             # Sentry auth token for source maps
```

---

## Verification Checklist

Run this checklist before starting the team to ensure all MCP servers are accessible:

```bash
# 1. Supabase
echo "Supabase token: ${SUPABASE_ACCESS_TOKEN:+SET}"
supabase projects list 2>/dev/null && echo "Supabase CLI: OK" || echo "Supabase CLI: FAILED"

# 2. Vercel
echo "Vercel token: ${VERCEL_TOKEN:+SET}"
vercel whoami 2>/dev/null && echo "Vercel CLI: OK" || echo "Vercel CLI: FAILED"

# 3. Stripe
echo "Stripe key: ${STRIPE_SECRET_KEY:+SET}"
stripe config --list 2>/dev/null && echo "Stripe CLI: OK" || echo "Stripe CLI: FAILED"

# 4. GitHub
echo "GitHub token: ${GITHUB_TOKEN:+SET}"
gh auth status 2>/dev/null && echo "GitHub CLI: OK" || echo "GitHub CLI: FAILED"
```

All four should show "SET" and "OK". If any fail, revisit the credential setup steps above.

---

## Security Notes

- **Never commit credentials** to the repository. All environment variables should be set in your shell, `.env.local` (gitignored), or a secrets manager.
- **Use test mode credentials** for development and staging. Production credentials should only be set in Vercel production environment variables and GitHub Secrets.
- **Rotate tokens regularly.** If a token is exposed, revoke it immediately and generate a new one.
- **Scope tokens narrowly.** Give each token only the permissions it needs. Avoid tokens with full administrative access.
- **The `SUPABASE_SERVICE_ROLE_KEY` bypasses RLS.** It must never be exposed to client-side code or public endpoints. It is used only by the webhook handler and server-side operations that require elevated privileges.
