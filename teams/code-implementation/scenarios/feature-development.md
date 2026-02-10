# Scenario: Feature Development -- Adding a Major Feature to an Existing Codebase

## Context

An established SaaS application needs a new notifications system. The existing codebase is a Next.js application with a PostgreSQL database, an established API layer, and a component library. The team must integrate the new feature into the existing architecture without disrupting current functionality.

The notification system includes in-app notifications, email digests, user preference management, and real-time delivery via WebSockets.

## Trigger

The Coordinator receives a feature specification covering:
- Notification data model (types, channels, read/unread state, timestamps)
- In-app notification bell with unread count badge and dropdown list
- Email digest system (immediate, daily, weekly based on user preferences)
- User notification preferences page (per-type, per-channel toggles)
- Real-time notification delivery via existing WebSocket infrastructure
- API endpoints for CRUD operations on notifications and preferences

## Team Configuration

| Agent | Model | Role in This Scenario |
|-------|-------|-----------------------|
| Coordinator | Sonnet 4.5 | Analyze existing codebase, decompose feature, assign parallel work |
| Specialist A | Opus 4.6 | Notification API, database schema, preference management, email digest |
| Specialist B | Opus 4.6 | UI components, notification bell, preferences page, real-time hooks |
| Code Reviewer | Sonnet 4.5 | Review against existing patterns, verify backward compatibility |
| Test Engineer | Sonnet 4.5 | Holdout scenarios, unit tests, integration tests for new endpoints |
| DevOps Specialist | Sonnet 4.5 | Update CI for new migration steps, configure email service credentials |

## Workflow

### Phase 1: Codebase Analysis and Planning (~10 min)
- Coordinator reads existing codebase to identify conventions, patterns, and structure
- Maps the notification feature onto existing architecture (existing API patterns, component patterns, database conventions)
- Identifies shared files that need modification (e.g., sidebar component, user settings page)
- Assigns file ownership: A owns backend files, B owns frontend files
- Defines shared interfaces: Notification type, NotificationPreference type, API response shapes
- Identifies risk areas: database migration on production table, WebSocket message format compatibility

### Phase 2: Parallel Implementation (~25-40 min)
- **Specialist A:** Database migration (notifications table, preferences table), API route handlers (GET /notifications, PATCH /notifications/:id/read, GET/PUT /preferences), email digest service with scheduling, notification creation utility
- **Specialist B:** NotificationBell component with unread badge, notification dropdown with infinite scroll, preferences page with toggle grid, real-time notification hook using existing WebSocket client, toast notification for new arrivals
- **Test Engineer:** Writes holdout scenarios for notification CRUD, preference updates, email digest scheduling, real-time delivery, read/unread state management

### Phase 3: Code Review (~15-20 min)
- Reviewer verifies new code matches existing project patterns (naming, file structure, error handling)
- Checks database migration is reversible and safe for production
- Verifies notification endpoints enforce authentication and authorization
- Confirms WebSocket message format is backward-compatible
- Validates email content is sanitized (no XSS in email templates)

### Phase 4: Testing and Documentation (~15 min)
- Test Engineer runs holdout scenarios against feature branch
- Generates unit tests for notification service, preference logic, and API handlers
- Generates integration tests for full notification lifecycle (create, deliver, read, delete)
- Documentation Writer updates API docs with new endpoints and updates README with notification configuration

## Expected Outputs

- 15-25 new or modified files across frontend and backend
- Database migration files (up and down)
- New API endpoints with request/response documentation
- Frontend components matching existing design system
- Unit and integration tests with >= 80% coverage on new code
- Updated API documentation and changelog entry

## Estimated Cost

| Configuration | Est. Tokens | Est. Cost | Est. Time |
|--------------|-------------|-----------|-----------|
| Budget (all Sonnet) | ~490K | ~$10 | ~80 min |
| Default (mixed) | ~490K | ~$25 | ~65 min |
| Premium (all Opus) | ~490K | ~$45 | ~60 min |

Note: Feature development on an existing codebase is the standard use case. Token usage matches the baseline estimate. The Default configuration is recommended -- Opus for implementation catches integration issues with the existing codebase.
