# Scenario: Data CRUD Operations

This scenario defines Create, Read, Update, and Delete operations on core application entities with Row Level Security enforcement. It is validated after Phase 2 and again in Phase 4.

---

## Scenario Overview

| Property | Value |
|----------|-------|
| **Priority** | Critical |
| **Validated After** | Phase 2, Phase 4 |
| **Primary Agents** | Senior Full-Stack, Database Engineer, QA/Test |
| **Estimated Test Time** | ~8 minutes (E2E) |

---

## Context

This scenario uses a generic "project" entity as the example, representing the primary object users create and manage in the application. The specific entity name and fields will vary by project configuration (e.g., "project" for a project management tool, "listing" for a marketplace, "report" for a dashboard tool).

### Entity Schema (Example)

```sql
CREATE TABLE public.projects (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  name TEXT NOT NULL,
  description TEXT,
  status TEXT NOT NULL DEFAULT 'active' CHECK (status IN ('active', 'archived')),
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

ALTER TABLE public.projects ENABLE ROW LEVEL SECURITY;

CREATE INDEX idx_projects_user_id ON public.projects(user_id);
CREATE INDEX idx_projects_status ON public.projects(status);
```

---

## Success Path: Create

### Preconditions

- User is authenticated and on the dashboard
- User is within their plan's entity limit (e.g., Free plan allows 3 projects)

### Steps

| Step | User Action | Expected Outcome |
|------|------------|------------------|
| 1 | Click "New Project" button on dashboard | Create form/modal appears |
| 2 | Enter project name: "My First Project" | Name field validates (non-empty, reasonable length) |
| 3 | Enter description: "A test project for validation" | Description field accepts the input |
| 4 | Click "Create" | Server Action fires, validates input with Zod, inserts into database |
| 5 | (Server) RLS check: `auth.uid() = user_id` on INSERT | Insert succeeds because `user_id` is set to the authenticated user's ID |
| 6 | (Server) Response returned | Success response with new project data |
| 7 | User is redirected to project list or detail view | New project appears in the list with correct name, description, and "active" status |

### Validation Criteria

- [ ] Project record exists in database with correct `user_id`, `name`, `description`
- [ ] `created_at` and `updated_at` are set to the current time
- [ ] `status` defaults to `active`
- [ ] `id` is a valid UUID
- [ ] UI reflects the new project immediately (no page refresh required)
- [ ] Zod validation rejects empty name (error message shown)
- [ ] Zod validation rejects excessively long name (>255 characters)

---

## Success Path: Read (List View)

### Preconditions

- User is authenticated
- User has 3 projects in the database

### Steps

| Step | User Action | Expected Outcome |
|------|------------|------------------|
| 1 | Navigate to `/dashboard` or `/projects` | Project list page loads |
| 2 | (Server) Supabase query: `SELECT * FROM projects WHERE user_id = auth.uid()` | Returns only the authenticated user's projects |
| 3 | Project list renders | Shows 3 projects with name, status, and created date |
| 4 | Projects are sorted by `created_at` descending | Most recent project appears first |

### Validation Criteria

- [ ] Only the authenticated user's projects are displayed (RLS enforced)
- [ ] All 3 projects are shown with correct data
- [ ] Sort order is newest first
- [ ] Empty state is shown when user has no projects ("No projects yet. Create your first project.")
- [ ] Loading state is shown while data is being fetched
- [ ] Error state is shown if the query fails

---

## Success Path: Read (Detail View)

### Preconditions

- User is authenticated
- User has a project with a known ID

### Steps

| Step | User Action | Expected Outcome |
|------|------------|------------------|
| 1 | Click on a project in the list | Navigate to `/projects/[id]` |
| 2 | (Server) Supabase query with project ID | Returns the project if `user_id = auth.uid()` |
| 3 | Project detail page renders | Shows name, description, status, timestamps, and related data |

### Validation Criteria

- [ ] Project data is displayed correctly
- [ ] Related data (if any) is loaded and displayed
- [ ] Edit and delete buttons are visible
- [ ] Breadcrumb navigation shows the project name
- [ ] 404 page shown if project ID does not exist
- [ ] 404 page shown if project belongs to another user (RLS prevents access)

---

## Success Path: Update

### Preconditions

- User is authenticated
- User is viewing a project they own

### Steps

| Step | User Action | Expected Outcome |
|------|------------|------------------|
| 1 | Click "Edit" on the project detail page | Edit form appears with current values pre-filled |
| 2 | Change the name to "Updated Project Name" | Name field updates |
| 3 | Change the description to "Updated description" | Description field updates |
| 4 | Click "Save" | Server Action fires, validates input with Zod, updates the database |
| 5 | (Server) RLS check: `auth.uid() = user_id` on UPDATE | Update succeeds because user owns the project |
| 6 | (Server) `updated_at` trigger fires | `updated_at` is set to the current time |
| 7 | User sees the updated project | Detail view shows new name and description with updated timestamp |

### Validation Criteria

- [ ] Project record in database reflects the changes
- [ ] `updated_at` is later than `created_at`
- [ ] `created_at` is unchanged
- [ ] UI reflects changes immediately
- [ ] Validation rejects invalid input (empty name)
- [ ] Optimistic UI update shown with rollback on failure (optional, depending on UX strategy)

---

## Success Path: Delete

### Preconditions

- User is authenticated
- User is viewing a project they own

### Steps

| Step | User Action | Expected Outcome |
|------|------------|------------------|
| 1 | Click "Delete" on the project detail page | Confirmation dialog appears: "Are you sure you want to delete 'Project Name'? This action cannot be undone." |
| 2 | Click "Confirm Delete" | Server Action fires, deletes the record from the database |
| 3 | (Server) RLS check: `auth.uid() = user_id` on DELETE | Delete succeeds because user owns the project |
| 4 | User is redirected to project list | Project no longer appears in the list |

### Validation Criteria

- [ ] Project record is removed from the database (or soft-deleted if using soft delete)
- [ ] Confirmation dialog prevents accidental deletion
- [ ] User is redirected to list view after deletion
- [ ] Deleted project does not appear in subsequent queries
- [ ] Related data is cascade deleted (if configured) or handled appropriately
- [ ] Toast notification: "Project deleted successfully"

---

## RLS Enforcement Tests

These tests verify that Row Level Security prevents unauthorized data access.

### Test: User A Cannot Read User B's Data

| Step | Action | Expected Outcome |
|------|--------|------------------|
| 1 | User A creates a project (ID: `project-a-1`) | Project created successfully |
| 2 | User B authenticates and queries for `project-a-1` | Query returns empty result (RLS blocks access) |
| 3 | User B navigates to `/projects/project-a-1` | 404 page displayed (not a 403 -- do not leak existence) |
| 4 | User B calls the API directly with `project-a-1` ID | API returns 404 or empty result |

### Test: User A Cannot Update User B's Data

| Step | Action | Expected Outcome |
|------|--------|------------------|
| 1 | User A creates a project (ID: `project-a-1`) | Project created successfully |
| 2 | User B attempts to update `project-a-1` via Server Action | Update fails (RLS blocks, zero rows affected) |
| 3 | User B attempts to update via direct Supabase client call | Update fails (RLS blocks) |
| 4 | Project data is unchanged | User A's project retains original values |

### Test: User A Cannot Delete User B's Data

| Step | Action | Expected Outcome |
|------|--------|------------------|
| 1 | User A creates a project (ID: `project-a-1`) | Project created successfully |
| 2 | User B attempts to delete `project-a-1` via Server Action | Delete fails (RLS blocks, zero rows affected) |
| 3 | Project still exists | User A can still access the project |

### Test: User Cannot Insert Data for Another User

| Step | Action | Expected Outcome |
|------|--------|------------------|
| 1 | User A attempts to create a project with `user_id` set to User B's ID | Insert fails (RLS `WITH CHECK` blocks) |
| 2 | No project created | Database has no record with User B's ID from User A |

### Validation Criteria for RLS

- [ ] Users can only SELECT their own rows
- [ ] Users can only INSERT rows where `user_id` matches their `auth.uid()`
- [ ] Users can only UPDATE their own rows
- [ ] Users can only DELETE their own rows
- [ ] Cross-user access returns empty results, not permission errors (avoid leaking information)
- [ ] Service role key bypasses RLS (used by webhook handlers and background jobs)

---

## Edge Cases

### Concurrent Updates

| Step | Action | Expected Outcome |
|------|--------|------------------|
| 1 | User opens project in two browser tabs | Same project data shown in both |
| 2 | User updates name in Tab A, saves | Update succeeds, `updated_at` changes |
| 3 | User updates description in Tab B, saves | Update succeeds (different field, no conflict) |
| 4 | Both tabs show correct data after refresh | Name from Tab A, description from Tab B |

For conflicting updates (same field):

| Step | Action | Expected Outcome |
|------|--------|------------------|
| 1 | Tab A and Tab B both have the same project open | Same data in both |
| 2 | Tab A changes name to "Name A", saves | Update succeeds |
| 3 | Tab B changes name to "Name B", saves | Update succeeds (last write wins) |
| 4 | Final state | Name is "Name B" (last write wins is acceptable for MVP) |

### Soft Delete

If the project uses soft delete (recommended for production):

| Step | Action | Expected Outcome |
|------|--------|------------------|
| 1 | User clicks "Delete" and confirms | `status` set to `archived` or `deleted_at` set to current time |
| 2 | Project disappears from active list | RLS or query filter excludes soft-deleted records |
| 3 | Project data is preserved in database | Available for recovery or compliance |
| 4 | Soft-deleted project does not count toward plan limits | Limit check excludes archived projects |

### Pagination

| Step | Action | Expected Outcome |
|------|--------|------------------|
| 1 | User has 50 projects | List view shows first page (e.g., 20 projects) |
| 2 | User scrolls or clicks "Next page" | Next 20 projects loaded |
| 3 | Verify all 50 projects are accessible | No data loss across pages |
| 4 | Verify sort order is consistent across pages | Projects do not appear on multiple pages or skip |

### Plan Limit Enforcement

| Step | Action | Expected Outcome |
|------|--------|------------------|
| 1 | Free user has 3 projects (at limit) | Dashboard shows "3/3 projects used" |
| 2 | User clicks "New Project" | Error: "You have reached the project limit for your plan. Upgrade to Pro for unlimited projects." |
| 3 | User upgrades to Pro | Project limit is lifted |
| 4 | User can now create more projects | "New Project" button works again |

---

## Test Data Requirements

| Data Item | Value | Purpose |
|-----------|-------|---------|
| User A account | Seeded in `seed.sql` with 3 projects | CRUD operations testing |
| User B account | Seeded in `seed.sql` with 2 projects | Cross-user RLS testing |
| Free-tier user | Account at plan limit (3 projects) | Limit enforcement testing |
| Pro-tier user | Account with many projects | Pagination testing |

---

## Agents Responsible

| Agent | Responsibility |
|-------|---------------|
| **Senior Full-Stack Developer** | CRUD UI (list, detail, create, edit, delete), Server Actions, form validation |
| **Database Engineer** | Table schema, RLS policies (SELECT, INSERT, UPDATE, DELETE), indexes, triggers |
| **QA / Test Engineer** | CRUD E2E tests, RLS bypass tests, edge case tests (concurrent updates, pagination, limits) |
| **Coordinator** | Defines entity model, validates CRUD meets requirements |
