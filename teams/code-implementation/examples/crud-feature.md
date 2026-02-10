# Example: CRUD Feature -- Task Management Module

## Feature Overview

Add a task management module to an existing project management application. Users can create, view, update, and delete tasks within their projects. Tasks have status tracking, priority levels, and assignee support.

## Configuration

```yaml
project_type: web_app
primary_language: typescript
framework: nextjs
testing_framework: vitest
code_style: airbnb
review_strictness: standard

feature:
  name: task-management
  description: "CRUD operations for tasks within projects, with status, priority, and assignment"
  priority: standard

agent_budget:
  model_config: default
  max_total_cost_usd: 35
```

## Phase 1: Planning (~10 min)

### Coordinator
- Analyzes existing codebase: identifies project model, route patterns, and data access layer
- Decomposes into 7 tasks across 2 Specialists

**Task Assignment:**

| Task | Specialist | Complexity | Dependencies |
|------|-----------|------------|-------------|
| Database migration (tasks table) | B | Medium | None |
| Task service layer (data access) | B | Medium | Migration |
| Task API routes (CRUD handlers) | A | High | Service layer interface |
| Task validation schemas (Zod) | A | Low | None |
| Task list component with filters | A | Medium | API routes |
| Task detail/edit form component | A | Medium | API routes |
| Shared types (Task, TaskStatus, TaskPriority) | A (owner) | Low | Migration |

**Shared Interfaces:**
```typescript
// types/task.ts (owned by Specialist A, consumed by B)
interface Task {
  id: string;
  projectId: string;
  title: string;
  description: string | null;
  status: 'todo' | 'in_progress' | 'done';
  priority: 'low' | 'medium' | 'high';
  assigneeId: string | null;
  createdAt: string;
  updatedAt: string;
}
```

## Phase 2: Implementation (~30 min, parallel)

### Specialist A (Primary -- API Routes + UI)
- Creates `app/api/projects/[projectId]/tasks/route.ts` (GET list, POST create)
- Creates `app/api/projects/[projectId]/tasks/[taskId]/route.ts` (GET, PUT, DELETE)
- Adds Zod validation schemas for create/update request bodies
- Creates task list page with status filters and priority sorting
- Creates task detail view with edit form
- Adds auth middleware check on all task routes

**Files created/modified:**
- `app/api/projects/[projectId]/tasks/route.ts` (new, 95 lines)
- `app/api/projects/[projectId]/tasks/[taskId]/route.ts` (new, 120 lines)
- `lib/validations/task.ts` (new, 35 lines)
- `app/(app)/projects/[projectId]/tasks/page.tsx` (new, 85 lines)
- `app/(app)/projects/[projectId]/tasks/[taskId]/page.tsx` (new, 110 lines)
- `components/tasks/task-list.tsx` (new, 65 lines)
- `components/tasks/task-form.tsx` (new, 90 lines)
- `types/task.ts` (new, 25 lines)

### Specialist B (Secondary -- Database + Service)
- Creates migration `003_add_tasks_table.sql` with columns, indexes, and RLS
- Implements task service: `createTask`, `getTasks`, `getTask`, `updateTask`, `deleteTask`
- Adds pagination support to `getTasks` with cursor-based pagination
- Implements RLS policy: users can only access tasks in their own projects

**Files created/modified:**
- `supabase/migrations/003_add_tasks_table.sql` (new, 65 lines)
- `lib/services/task-service.ts` (new, 110 lines)

### Test Engineer (Scenario Writing)
- Writes holdout scenarios for task CRUD operations
- Designs edge cases: empty project, maximum title length, invalid status transitions

## Phase 3: Code Review (~15 min)

### Code Reviewer
- Reviews Specialist A: validates auth checks, input validation, error responses
- Reviews Specialist B: validates SQL migration, RLS policies, service layer error handling
- Cross-references: verifies Task type matches migration columns, service layer matches API expectations

**Findings:**
- BLOCKER: Missing pagination on task list API (unbounded query)
- BLOCKER: Delete endpoint does not check project ownership (auth bypass)
- SUGGESTION: Consider adding `ORDER BY` to task list query for deterministic results
- SUGGESTION: Add optimistic UI update on task status change

**Resolution:** Specialists fix both blockers. Reviewer approves on second pass.

## Phase 4: Testing + Documentation (~15 min, parallel)

### Test Engineer
- Runs holdout scenarios: 11/12 pass (91.7% satisfaction)
- Failed scenario: concurrent task update (not implemented, logged as future work)
- Generates 18 unit tests and 8 integration tests
- Coverage: 87% lines, 83% branches

### Documentation Writer
- Adds JSDoc to all task service functions
- Creates API docs for 5 task endpoints with examples
- Updates README with task management feature description
- Adds changelog entry

## Deliverables Produced

1. **Database migration** -- tasks table with indexes and RLS
2. **API routes** -- 5 CRUD endpoints with auth and validation
3. **UI components** -- Task list page, task detail page, task form
4. **Service layer** -- Data access functions with pagination
5. **Tests** -- 18 unit tests, 8 integration tests, 87% coverage
6. **Documentation** -- API docs, JSDoc, changelog entry

## Cost Summary

| Phase | Agent | Tokens | Cost |
|-------|-------|--------|------|
| Planning | Coordinator | 22K | $0.18 |
| Implementation | Specialist A | 130K | $8.45 |
| Implementation | Specialist B | 85K | $5.53 |
| Implementation | Test Engineer (scenarios) | 12K | $0.10 |
| Review | Code Reviewer | 65K | $4.23 |
| Testing | Test Engineer | 45K | $0.36 |
| Documentation | Doc Writer | 15K | $0.01 |
| **Total** | | **374K** | **~$18.86** |
