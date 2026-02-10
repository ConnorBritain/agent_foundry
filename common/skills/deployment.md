---
skill_name: "deployment"
version: "1.0.0"
description: "Deploy agent outputs to staging and production environments"
author: "Sforza"
triggers:
  - "when code is ready for deployment"
  - "when artifacts need to go to production"
  - "when a release cycle begins"
---

# Deployment Skill

## Purpose

Manage the deployment of agent-produced artifacts — code, configurations, content, and documentation — to staging and production environments.

## Pre-Deployment Checklist

Before deploying any artifact, verify:

1. **All tests pass** — Unit, integration, and e2e tests green
2. **Code review complete** — At least one reviewer approved
3. **Environment variables set** — No hardcoded secrets, all env vars documented
4. **Database migrations ready** — Schema changes tested on staging first
5. **Rollback plan defined** — Know how to revert if deployment fails
6. **Cost impact assessed** — New infrastructure costs estimated

## Deployment Workflow

### Step 1: Stage

```
- Push to staging branch or environment
- Run smoke tests against staging URL
- Verify all integrations work (Stripe test mode, Supabase staging, etc.)
- Check performance (Lighthouse score, response times)
```

### Step 2: Validate

```
- Manual QA pass on critical user flows
- Verify no regression in existing features
- Check error monitoring (Sentry, LogRocket) for new issues
- Confirm analytics tracking fires correctly
```

### Step 3: Deploy to Production

```
- Merge to main branch (triggers CI/CD pipeline)
- Monitor deployment progress in hosting dashboard
- Run production smoke tests within 5 minutes
- Verify DNS, SSL, and CDN propagation
```

### Step 4: Post-Deploy

```
- Monitor error rates for 30 minutes
- Check key metrics (conversion, latency, availability)
- Update project-status.json with deployment status
- Notify stakeholders via cross-team-communication.md
```

## Rollback Procedure

If issues detected post-deploy:

1. **Immediate**: Revert to previous deployment via hosting provider (Vercel instant rollback, etc.)
2. **Code**: Revert merge commit on main, push, wait for redeploy
3. **Database**: Run reverse migration script (must be prepared pre-deploy)
4. **DNS**: Switch back to previous deployment URL if using blue-green

## Platform-Specific Notes

### Vercel
- Automatic deployments on push to main
- Preview deployments for every PR
- Instant rollback via dashboard
- Edge functions deploy globally

### Supabase
- Database migrations via `supabase db push`
- Edge functions via `supabase functions deploy`
- Always test migrations on staging project first

### Stripe
- Use test mode for all development
- Webhook endpoints must be registered per environment
- Price/product IDs differ between test and live

## Reporting

After deployment, update the shared workspace:

```markdown
### [TIMESTAMP] TEAM_NAME: Deployment Complete
- Environment: production
- URL: https://your-app.vercel.app
- Version: v1.2.0
- Status: healthy
- Rollback plan: Vercel dashboard → Deployments → Previous
```
