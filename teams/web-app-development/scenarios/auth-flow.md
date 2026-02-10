# Scenario: Authentication Flow

This scenario defines the complete authentication flow, including signup, login, session management, and logout. It is validated after Phase 2 and again in Phase 4.

---

## Scenario Overview

| Property | Value |
|----------|-------|
| **Priority** | Critical |
| **Validated After** | Phase 2, Phase 4 |
| **Primary Agents** | Senior Full-Stack, Database Engineer, QA/Test |
| **Estimated Test Time** | ~5 minutes (E2E) |

---

## Success Path: Google OAuth Signup

### Preconditions

- Supabase project is live with Google OAuth configured
- Google OAuth redirect URLs include localhost (dev) and production URL
- The `profiles` table exists with the `handle_new_user` trigger active
- Next.js middleware is configured to protect `/app/*` routes

### Steps

| Step | User Action | Expected Outcome |
|------|------------|------------------|
| 1 | Visit the application root URL (`/`) | Landing page loads with "Sign up" and "Log in" buttons visible |
| 2 | Click "Sign up" | Redirect to `/signup` page |
| 3 | Click "Continue with Google" | Redirect to Google's OAuth consent screen |
| 4 | Authenticate with Google account and grant consent | Google redirects back to `/auth/callback` with authorization code |
| 5 | (Automatic) Callback handler exchanges code for session | Supabase creates a new user in `auth.users`, the `handle_new_user` trigger creates a profile in `public.profiles` |
| 6 | (Automatic) Redirect to `/dashboard` | Dashboard loads with the user's Google display name and avatar visible |
| 7 | Verify session persistence: refresh the page | Dashboard reloads, user is still authenticated, no redirect to login |
| 8 | Navigate to `/settings` | Settings page loads with profile information pre-filled from Google (name, email, avatar) |
| 9 | Click "Log out" | Session is destroyed, user is redirected to `/` or `/login` |
| 10 | Attempt to visit `/dashboard` directly | User is redirected to `/login` (middleware blocks unauthenticated access) |

### Validation Criteria

- [ ] User record exists in `auth.users` with Google provider data
- [ ] Profile record exists in `public.profiles` with correct `id`, `email`, `full_name`, `avatar_url`
- [ ] Session cookie is set with correct expiry (per `session_duration_hours` in CONFIG)
- [ ] No sensitive data (tokens, secrets) in browser localStorage or console
- [ ] Redirect to original destination after login (if user was redirected from a protected page)

---

## Success Path: Returning User Login

### Preconditions

- User has previously signed up and has an existing account
- User is not currently authenticated (no active session)

### Steps

| Step | User Action | Expected Outcome |
|------|------------|------------------|
| 1 | Visit `/login` | Login page loads with OAuth and/or email options |
| 2 | Click "Continue with Google" | Redirect to Google's OAuth consent screen (may auto-select account if previously authorized) |
| 3 | Select the existing Google account | Google redirects back to `/auth/callback` |
| 4 | (Automatic) Callback handler creates session for existing user | No new user created, existing profile loaded |
| 5 | (Automatic) Redirect to `/dashboard` | Dashboard loads with existing user data (projects, settings, subscription status) |

### Validation Criteria

- [ ] No duplicate user record created in `auth.users`
- [ ] No duplicate profile record created in `public.profiles`
- [ ] Existing user data (projects, settings) is intact
- [ ] Session token is fresh (new session, not reuse of old session)

---

## Edge Case: OAuth Consent Denied

### Preconditions

- User is on the Google OAuth consent screen

### Steps

| Step | User Action | Expected Outcome |
|------|------------|------------------|
| 1 | Click "Cancel" or deny consent on Google's screen | Google redirects back to the callback URL with an error parameter |
| 2 | (Automatic) Callback handler detects the error | User is redirected to `/login` (or `/signup`) with an error message |
| 3 | Error message is displayed | Message reads: "Authentication was cancelled. Please try again." or similar |

### Validation Criteria

- [ ] No user record created in `auth.users`
- [ ] No profile record created in `public.profiles`
- [ ] Error message is user-friendly (not a raw error code)
- [ ] User can retry authentication immediately
- [ ] No unhandled errors in Sentry

---

## Edge Case: Existing User Signs Up Again

### Preconditions

- User already has an account (previously signed up with Google)
- User clicks "Sign up" instead of "Log in"

### Steps

| Step | User Action | Expected Outcome |
|------|------------|------------------|
| 1 | Visit `/signup` | Signup page loads |
| 2 | Click "Continue with Google" | Redirect to Google's OAuth consent screen |
| 3 | Authenticate with the same Google account | Google redirects back to callback |
| 4 | (Automatic) Supabase detects existing user | Existing user is logged in (not a duplicate created) |
| 5 | (Automatic) Redirect to `/dashboard` | Dashboard loads with existing data |

### Validation Criteria

- [ ] No duplicate user record created
- [ ] Existing data is preserved
- [ ] User is seamlessly logged in
- [ ] No error message shown (this is a valid flow, not an error)

---

## Edge Case: Network Failure During OAuth

### Preconditions

- User has initiated OAuth flow and authenticated with Google
- Network connection is interrupted between Google's redirect and the callback handler

### Steps

| Step | User Action | Expected Outcome |
|------|------------|------------------|
| 1 | Google redirects to `/auth/callback` but the request fails (network error) | Browser shows a connection error page |
| 2 | User restores network connection and refreshes the page | The callback URL still has the authorization code in the query parameters |
| 3 | (Automatic) If the authorization code is still valid, the callback processes | User is authenticated and redirected to dashboard |
| 4 | If the code has expired, error is handled | User is redirected to `/login` with message: "Session expired. Please sign in again." |

### Validation Criteria

- [ ] Authorization code expiry is handled gracefully (not a 500 error)
- [ ] User can always retry authentication
- [ ] Partial state is not left in the database (no orphaned records)

---

## Edge Case: Expired Session

### Preconditions

- User was previously authenticated
- Session has expired (exceeds `session_duration_hours`)
- User has the application open in a browser tab

### Steps

| Step | User Action | Expected Outcome |
|------|------------|------------------|
| 1 | User interacts with the dashboard (e.g., clicks a link, submits a form) | The Supabase client detects the expired session |
| 2 | (Automatic) Middleware intercepts the request | User is redirected to `/login` with a return URL parameter |
| 3 | User authenticates again | User is redirected back to the page they were trying to access |

### Validation Criteria

- [ ] Expired sessions do not cause 500 errors
- [ ] User is redirected to login, not shown a blank page
- [ ] Return URL is preserved so the user returns to their original destination
- [ ] Session refresh works if the refresh token is still valid (no re-authentication needed)
- [ ] No data loss from in-progress form submissions (form state should be recoverable)

---

## Edge Case: Multiple Browser Tabs

### Preconditions

- User is authenticated and has the application open in multiple browser tabs

### Steps

| Step | User Action | Expected Outcome |
|------|------------|------------------|
| 1 | User logs out in Tab A | Session is destroyed |
| 2 | User interacts with the application in Tab B | Tab B detects the invalidated session |
| 3 | (Automatic) Tab B redirects to login | User is redirected to `/login` in Tab B |

### Validation Criteria

- [ ] Logout in one tab invalidates sessions in all tabs
- [ ] No stale session tokens remain in other tabs
- [ ] No errors when trying to use the invalidated session

---

## Edge Case: Protected API Routes

### Preconditions

- User is not authenticated
- User attempts to call a protected API route directly (e.g., via curl or browser DevTools)

### Steps

| Step | User Action | Expected Outcome |
|------|------------|------------------|
| 1 | Send a GET request to `/api/health` | Returns 200 (public endpoint) |
| 2 | Send a GET request to a protected API route (e.g., `/api/user/profile`) | Returns 401 Unauthorized with JSON error body |
| 3 | Send a POST request to a protected Server Action | Returns 401 Unauthorized |
| 4 | Send a GET request to `/dashboard` via fetch (no cookies) | Returns redirect response (302) to `/login` |

### Validation Criteria

- [ ] All protected API routes return 401, not 500
- [ ] Error responses are structured JSON, not HTML error pages
- [ ] No data leakage in error responses (no user IDs, no internal paths)
- [ ] Rate limiting is applied to authentication endpoints (prevent brute force)

---

## Test Data Requirements

| Data Item | Value | Purpose |
|-----------|-------|---------|
| Test Google account | Configured in Supabase test environment | OAuth flow testing |
| Test email account | `test-user@example.com` / `TestPassword123!` | Email/password flow testing |
| Seeded user profile | Exists in `public.profiles` with test data | Returning user tests |
| Expired session token | Generated with past expiry | Expired session tests |

---

## Agents Responsible

| Agent | Responsibility |
|-------|---------------|
| **Senior Full-Stack Developer** | Implements auth pages, callback handler, middleware, session management |
| **Database Engineer** | Creates `profiles` table, `handle_new_user` trigger, RLS policies |
| **Cloud / DevOps Engineer** | Configures Supabase auth providers, redirect URLs |
| **QA / Test Engineer** | Writes E2E tests covering all paths above |
