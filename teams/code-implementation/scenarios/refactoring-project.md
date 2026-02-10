# Scenario: Refactoring Project -- Monolith to Modules

## Context

A growing application has an entangled monolithic codebase where business logic, data access, and UI concerns are mixed across files. The team must refactor the codebase from a flat structure into well-defined modules with clear boundaries, without changing any user-facing behavior.

The target architecture uses a modular monolith pattern: each domain (users, billing, notifications, tasks) gets its own module directory with isolated types, services, and data access. Shared utilities and cross-cutting concerns move to a `shared/` module.

## Trigger

The Coordinator receives a refactoring specification covering:
- Current structure: flat `src/` directory with 80+ files, mixed concerns, circular dependencies
- Target structure: `src/modules/{users,billing,notifications,tasks}/` with `{types,services,routes,data}/` subdirectories per module
- Constraint: zero behavior changes -- all existing tests must continue to pass
- Goal: eliminate circular dependencies, enforce module boundaries, enable future extraction to separate services

## Team Configuration

| Agent | Model | Role in This Scenario |
|-------|-------|-----------------------|
| Coordinator | Sonnet 4.5 | Map dependency graph, plan migration order, assign module ownership |
| Specialist A | Opus 4.6 | Refactor core modules (users, billing) -- highest dependency count |
| Specialist B | Opus 4.6 | Refactor secondary modules (notifications, tasks) in parallel |
| Code Reviewer | Sonnet 4.5 | Verify no behavior changes, check module boundary enforcement |
| Test Engineer | Sonnet 4.5 | Run existing tests after each move, verify zero regressions |
| DevOps Specialist | Sonnet 4.5 | Update import aliases, build configuration, and CI path filters |

## Workflow

### Phase 1: Dependency Analysis and Migration Plan (~15 min)
- Coordinator analyzes the codebase to map the full dependency graph
- Identifies circular dependencies and plans resolution order
- Groups files by domain: which files belong to which module
- Plans migration order: shared utilities first, then leaf modules, then core modules
- Assigns module ownership: A gets users + billing, B gets notifications + tasks
- Defines the shared module (types, utilities, middleware used by multiple modules)
- Creates the target directory structure as empty scaffolding
- Identifies import path updates needed across the codebase

### Phase 2: Parallel Module Extraction (~30-50 min)
- **Specialist A:** Extracts shared types and utilities to `src/modules/shared/`. Moves user-related files to `src/modules/users/`. Moves billing-related files to `src/modules/billing/`. Updates all import paths. Resolves circular dependencies by extracting shared interfaces.
- **Specialist B:** Moves notification-related files to `src/modules/notifications/`. Moves task-related files to `src/modules/tasks/`. Updates all import paths. Creates module index files (barrel exports) for clean public APIs.
- **Test Engineer:** Runs existing test suite after each batch of file moves to detect regressions immediately. Flags any test that breaks due to import path changes.

### Phase 3: Code Review (~20-25 min)
- Reviewer verifies every moved file has identical content (no logic changes)
- Checks that module boundaries are clean (no module imports another module's internal files)
- Verifies all circular dependencies are resolved
- Confirms barrel exports expose only the intended public API
- Validates that import paths follow the new convention consistently

### Phase 4: Validation and Cleanup (~15-20 min)
- Test Engineer runs full test suite and confirms 100% pass rate (zero regressions)
- Test Engineer runs lint and typecheck to verify no broken imports remain
- DevOps Specialist updates path aliases in tsconfig.json (or equivalent)
- DevOps Specialist updates CI configuration for module-aware caching and path filters
- Documentation Writer updates project structure documentation in README
- Coordinator creates a single PR with the complete refactoring

## Expected Outputs

- Restructured codebase with 4+ domain modules and a shared module
- Zero behavior changes -- all existing tests pass without modification
- Circular dependencies eliminated
- Clean module boundaries with barrel exports
- Updated import paths across all files
- Updated tsconfig path aliases and CI configuration
- Updated README with new project structure documentation

## Estimated Cost

| Configuration | Est. Tokens | Est. Cost | Est. Time |
|--------------|-------------|-----------|-----------|
| Budget (all Sonnet) | ~800K | ~$18 | ~2.5 hr |
| Default (mixed) | ~800K | ~$45 | ~2 hr |
| Premium (all Opus) | ~800K | ~$70 | ~1.5 hr |

Note: Refactoring projects use approximately 1.6x the standard token budget because every file move requires reading the file, understanding its dependencies, updating import paths across the codebase, and verifying no behavior changes. The Default configuration is recommended -- Opus for Specialists is critical because incorrect import path updates or missed circular dependencies cause cascading failures.
