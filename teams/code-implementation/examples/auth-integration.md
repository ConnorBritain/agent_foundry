# Example: Auth Integration -- OAuth Provider Addition

## Feature Overview

Add GitHub OAuth as an additional authentication provider to an existing application that currently supports Google OAuth only. The feature includes the OAuth callback handler, profile data sync, account linking for users who already have a Google account, and UI updates to the login and signup pages.

## Configuration

```yaml
project_type: web_app
primary_language: typescript
framework: nextjs
testing_framework: vitest
code_style: airbnb
review_strictness: strict  # Auth features get strict review

feature:
  name: github-oauth
  description: "Add GitHub OAuth provider with account linking for existing users"
  priority: high

agent_budget:
  model_config: default
  max_total_cost_usd: 40
```

## Phase 1: Planning (~10 min)

### Coordinator
- Analyzes existing auth implementation: identifies Supabase Auth setup, callback handler, profile creation trigger
- Identifies risk: account linking when a user has the same email on both Google and GitHub
- Decomposes into 8 tasks across 2 Specialists

**Task Assignment:**

| Task | Specialist | Complexity | Dependencies |
|------|-----------|------------|-------------|
| Supabase Auth provider configuration | B | Low | None |
| OAuth callback handler update | A | High | Provider config |
| Account linking logic | A | High | None |
| Login page UI update (add GitHub button) | A | Low | None |
| Signup page UI update (add GitHub button) | A | Low | None |
| Profile sync for GitHub-specific fields | B | Medium | None |
| Database migration (add provider fields) | B | Medium | None |
| Settings page: linked accounts display | A | Medium | Profile sync |

**Shared Interfaces:**
```typescript
// types/auth.ts (owned by Specialist A)
type AuthProvider = 'google' | 'github';

interface LinkedAccount {
  provider: AuthProvider;
  providerAccountId: string;
  email: string;
  connectedAt: string;
}
```

## Phase 2: Implementation (~35 min, parallel)

### Specialist A (Primary -- Callback + UI)
- Updates the OAuth callback handler to support multiple providers
- Implements account linking: when a GitHub login matches an existing Google user's email, link the accounts instead of creating a duplicate
- Adds "Continue with GitHub" button to login and signup pages
- Adds linked accounts section to user settings page
- Handles edge case: GitHub user has no public email configured

**Files created/modified:**
- `app/(auth)/callback/route.ts` (modified, +45 lines)
- `app/(auth)/login/page.tsx` (modified, +12 lines)
- `app/(auth)/signup/page.tsx` (modified, +12 lines)
- `app/(app)/settings/linked-accounts.tsx` (new, 75 lines)
- `lib/auth/account-linking.ts` (new, 85 lines)
- `lib/auth/providers.ts` (new, 30 lines)
- `types/auth.ts` (modified, +15 lines)
- `components/auth/oauth-buttons.tsx` (modified, +20 lines)

### Specialist B (Secondary -- Backend + Config)
- Configures GitHub OAuth provider in Supabase Auth settings
- Creates database migration adding `provider` and `provider_account_id` columns to profiles
- Implements profile sync that pulls GitHub-specific data (username, avatar, bio)
- Backfills existing Google users' provider data in migration

**Files created/modified:**
- `supabase/migrations/005_add_auth_provider_fields.sql` (new, 40 lines)
- `lib/auth/profile-sync.ts` (new, 65 lines)
- `supabase/config.toml` (modified, +8 lines)

### Test Engineer (Scenario Writing)
- Designs scenarios for: new GitHub signup, existing user account linking, GitHub user with no email, disconnect provider, login with linked account
- Focuses on security edge cases: session hijacking via account linking, email mismatch attacks

## Phase 3: Code Review (~20 min)

### Code Reviewer (Strict Mode)
- Reviews Specialist A: deep focus on account linking security
- Reviews Specialist B: validates migration safety, backfill correctness
- Cross-references: ensures provider enum is consistent across all files

**Findings:**
- BLOCKER: Account linking does not verify email ownership before linking (security risk -- attacker could link to any account by setting their GitHub email)
- BLOCKER: Missing CSRF protection on the account linking endpoint
- BLOCKER: Migration backfill does not handle users with multiple auth identities
- SUGGESTION: Add rate limiting on OAuth callback to prevent abuse
- SUGGESTION: Log account linking events for audit trail

**Resolution:**
- Specialist A adds email verification step before account linking
- Specialist A adds CSRF token to the linking flow
- Specialist B fixes migration to handle multi-identity users
- Reviewer approves on third pass (strict mode, 3 blocking rounds)

## Phase 4: Testing + Documentation (~15 min, parallel)

### Test Engineer
- Runs holdout scenarios: 14/15 pass (93.3% satisfaction)
- Failed scenario: disconnect last provider (edge case -- should prevent, not crash)
- Generates 12 unit tests and 10 integration tests
- Coverage: 91% lines, 88% branches
- Security-focused tests: email mismatch attack, CSRF bypass attempt, session fixation

### Documentation Writer
- Updates auth section of README with GitHub OAuth setup instructions
- Documents account linking behavior and limitations
- Adds API docs for the new linked accounts endpoint
- Adds changelog entry with security notes

## Deliverables Produced

1. **GitHub OAuth integration** -- Full OAuth flow with Supabase Auth
2. **Account linking** -- Secure email-verified linking between providers
3. **UI updates** -- Login, signup, and settings pages updated
4. **Database migration** -- Provider fields with backfill for existing users
5. **Profile sync** -- GitHub-specific profile data (username, avatar)
6. **Tests** -- 12 unit, 10 integration, security-focused test suite
7. **Documentation** -- Setup guide, API docs, changelog

## Cost Summary

| Phase | Agent | Tokens | Cost |
|-------|-------|--------|------|
| Planning | Coordinator | 25K | $0.20 |
| Implementation | Specialist A | 145K | $9.43 |
| Implementation | Specialist B | 70K | $4.55 |
| Implementation | Test Engineer (scenarios) | 15K | $0.12 |
| Review | Code Reviewer | 78K | $5.07 |
| Testing | Test Engineer | 52K | $0.42 |
| Documentation | Doc Writer | 18K | $0.01 |
| **Total** | | **403K** | **~$19.80** |

## Key Learnings

- **Strict review mode was justified.** The account linking security issue would have been a critical vulnerability in production. The extra review cycles cost ~$3 but prevented a serious bug.
- **Account linking is deceptively complex.** What seems like a simple "add a button" feature involves email verification, CSRF protection, multi-identity handling, and provider disconnection logic.
- **Security scenarios are essential.** The Test Engineer's security-focused holdout scenarios caught the "disconnect last provider" edge case that neither Specialist anticipated.
