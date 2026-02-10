# Example: Building a React Native Mobile App

## Scenario

A health and wellness startup needs a mobile application for iOS and Android. The app provides workout tracking, exercise library browsing, progress visualization, and social features (sharing achievements). The backend API already exists -- this team builds the mobile client that consumes it.

## Project Charter Inputs

```yaml
project_type: mobile_app
primary_language: typescript
framework: react-native
testing_framework: jest
package_manager: npm

repository:
  url: https://github.com/acme/fittrack-mobile
  default_branch: main

feature:
  name: fittrack-mvp
  description: |
    React Native mobile app (Expo):
    - Authentication screens (login, register, forgot password)
    - Workout tracking: start workout, add exercises, log sets/reps/weight, finish workout
    - Exercise library with search, filtering by muscle group, and video previews
    - Progress dashboard with charts (weekly volume, personal records, streak)
    - Social feed: share workout summaries, like and comment on friends' workouts
    - Push notifications for workout reminders and social interactions
    - Offline support: cache workouts locally, sync when online
    - Navigation: bottom tab bar (Home, Workouts, Library, Social, Profile)

code_style: airbnb
agent_budget:
  model_config: default
  max_total_cost_usd: 40
```

## Team Execution

### Phase 1: App Architecture and Decomposition (12 min, $0.28)
- Coordinator sets up Expo project with TypeScript, React Navigation, and Zustand
- Designs navigation structure: bottom tabs with nested stacks per tab
- Plans state management: Zustand stores for auth, workouts, exercises, social, offline queue
- Assigns Specialist A: auth screens, workout tracking flow, offline sync, data layer
- Assigns Specialist B: exercise library, progress dashboard, social feed, UI components
- Shared interfaces: `Workout`, `Exercise`, `Set`, `UserProfile`, `SocialPost` types
- Identifies shared components: Button, Card, Input, Avatar, EmptyState

### Phase 2: Parallel Implementation (50 min, $20.20)
**Specialist A builds:**
- `src/screens/auth/LoginScreen.tsx` -- Email/password login with validation
- `src/screens/auth/RegisterScreen.tsx` -- Registration with field validation
- `src/screens/auth/ForgotPasswordScreen.tsx` -- Password reset flow
- `src/screens/workout/ActiveWorkoutScreen.tsx` -- Live workout tracking with timer
- `src/screens/workout/ExercisePickerScreen.tsx` -- Add exercises to active workout
- `src/screens/workout/WorkoutSummaryScreen.tsx` -- Post-workout summary and save
- `src/stores/authStore.ts` -- Authentication state, token management, auto-refresh
- `src/stores/workoutStore.ts` -- Active workout state, exercise/set management
- `src/stores/offlineStore.ts` -- Offline queue with background sync
- `src/services/api.ts` -- Axios client with interceptors (auth, retry, offline detection)
- `src/services/storage.ts` -- AsyncStorage wrapper for offline data persistence
- `src/navigation/AuthNavigator.tsx` -- Auth stack (login, register, forgot password)
- `src/navigation/WorkoutNavigator.tsx` -- Workout stack (active, picker, summary)

**Specialist B builds:**
- `src/screens/library/ExerciseLibraryScreen.tsx` -- Search, filter by muscle group, list view
- `src/screens/library/ExerciseDetailScreen.tsx` -- Exercise info, video preview, history
- `src/screens/dashboard/DashboardScreen.tsx` -- Weekly stats, charts, streak counter
- `src/screens/social/SocialFeedScreen.tsx` -- Friend workout feed with like/comment
- `src/screens/social/WorkoutShareScreen.tsx` -- Share workout summary as social post
- `src/screens/profile/ProfileScreen.tsx` -- User profile, settings, logout
- `src/components/charts/VolumeChart.tsx` -- Weekly training volume bar chart
- `src/components/charts/PRChart.tsx` -- Personal records line chart
- `src/components/ui/Button.tsx` -- Themed button with loading state
- `src/components/ui/Card.tsx` -- Content card with shadow and border radius
- `src/components/ui/Input.tsx` -- Themed text input with validation display
- `src/components/workout/SetRow.tsx` -- Individual set entry (reps, weight, RPE)
- `src/components/workout/ExerciseCard.tsx` -- Exercise summary within workout
- `src/navigation/TabNavigator.tsx` -- Bottom tab bar with icons
- `src/navigation/LibraryNavigator.tsx` -- Library stack (list, detail)
- `src/navigation/SocialNavigator.tsx` -- Social stack (feed, share, comments)

**Test Engineer writes:**
- Holdout scenarios for auth flow (login, register, token refresh, logout)
- Holdout scenarios for workout tracking (start, add exercise, log sets, finish, save)
- Holdout scenarios for offline mode (create workout offline, sync when reconnected)
- Holdout scenarios for exercise library (search, filter, view detail)
- Holdout scenarios for social feed (share workout, like post, add comment)

### Phase 3: Code Review (20 min, $5.10)
- Reviewer flags 3 blockers:
  - BLOCKER: Auth token stored in plain AsyncStorage without encryption
  - BLOCKER: Active workout state lost on app crash (no periodic persistence)
  - BLOCKER: Social feed loads all posts without pagination (performance issue on large feeds)
- Reviewer notes 5 suggestions:
  - SUGGESTION: Add haptic feedback on set completion
  - SUGGESTION: Implement skeleton loading states for library and feed screens
  - SUGGESTION: Use React.memo on SetRow to prevent unnecessary re-renders during workout
  - SUGGESTION: Add pull-to-refresh on social feed
  - SUGGESTION: Cache exercise images for offline viewing
- Specialist A fixes token storage (uses expo-secure-store) and adds periodic workout state persistence
- Specialist B fixes social feed pagination (cursor-based infinite scroll)
- Reviewer approves on second pass

### Phase 4: Testing and Documentation (15 min, $0.55)
- Test Engineer runs holdout scenarios: 20/22 pass (91% satisfaction)
  - 2 failures: edge case with offline queue ordering and chart rendering with no data
- Generates 44 Jest unit tests and 8 Detox E2E tests
- Coverage: 82% on new code
- DevOps Specialist configures:
  - EAS Build configuration for iOS and Android
  - GitHub Actions: lint --> typecheck --> test --> EAS build (preview)
  - Environment variable management via expo-constants
  - Push notification setup with Expo Notifications
- Documentation Writer updates README with development setup, running on simulators, and env configuration

## Deliverables

```
fittrack-mobile/
  src/
    screens/
      auth/LoginScreen.tsx, RegisterScreen.tsx, ForgotPasswordScreen.tsx
      workout/ActiveWorkoutScreen.tsx, ExercisePickerScreen.tsx, WorkoutSummaryScreen.tsx
      library/ExerciseLibraryScreen.tsx, ExerciseDetailScreen.tsx
      dashboard/DashboardScreen.tsx
      social/SocialFeedScreen.tsx, WorkoutShareScreen.tsx
      profile/ProfileScreen.tsx
    components/
      ui/Button.tsx, Card.tsx, Input.tsx, Avatar.tsx, EmptyState.tsx, Skeleton.tsx
      charts/VolumeChart.tsx, PRChart.tsx, StreakBadge.tsx
      workout/SetRow.tsx, ExerciseCard.tsx, WorkoutTimer.tsx
    stores/
      authStore.ts, workoutStore.ts, exerciseStore.ts, socialStore.ts, offlineStore.ts
    services/
      api.ts, storage.ts, notifications.ts
    navigation/
      TabNavigator.tsx, AuthNavigator.tsx, WorkoutNavigator.tsx
      LibraryNavigator.tsx, SocialNavigator.tsx
    types/
      index.ts
    theme/
      colors.ts, spacing.ts, typography.ts
  tests/
    unit/ (44 files)
    e2e/ (8 files)
    fixtures/
  .github/workflows/ci.yml
  app.json
  eas.json
  .env.example
  README.md
```

## Cost Estimate

| Phase | Tokens | Cost |
|-------|--------|------|
| Planning | ~32K | $0.28 |
| Implementation | ~370K | $20.20 |
| Code Review | ~88K | $5.10 |
| Testing + Docs | ~60K | $0.55 |
| **Total** | **~550K** | **$26.13** |

## Expected Outcomes

- Cross-platform mobile app (iOS + Android) from a single codebase
- Secure authentication with encrypted token storage
- Full workout tracking with offline support and background sync
- Exercise library with search and filtering
- Progress visualization with interactive charts
- Social feed with infinite scroll and real-time interactions
- 82% test coverage with unit and E2E tests
- EAS Build configuration for preview and production builds
- CI/CD pipeline with automated testing and build triggers
