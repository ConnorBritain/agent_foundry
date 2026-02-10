# Code Implementation Team

A 6-agent team template for building production-ready features from requirements to deployment, with integrated code review, testing, and documentation.

## What This Team Does

This team takes a feature specification, user story, or requirements document and produces production-ready, tested, documented code through a coordinated multi-agent workflow. A typical feature run takes 45-90 minutes in hybrid mode and costs approximately $25-30.

- **Planning and decomposition** -- Break complex features into parallelizable work units with dependency analysis
- **Parallel implementation** -- Two Implementation Specialists work concurrently on independent sub-features
- **Code review** -- Structured review enforcing quality standards, security, and style compliance
- **Testing** -- Holdout scenario validation, unit tests, integration tests, and coverage analysis
- **Documentation** -- API docs, README updates, inline comments, and changelog entries

## When to Use This Template

Use this team when you need to:

- Implement a feature that spans multiple files or modules (>500 lines)
- Build a feature requiring code review, tests, and documentation
- Parallelize independent sub-features across two specialists
- Develop against an existing codebase with established conventions
- Ship a feature branch with passing CI, ready for merge

Do **not** use this team for:

- Greenfield application scaffolding (use the web-app-development team)
- One-file bug fixes or small patches (use a single agent)
- Infrastructure or DevOps tasks (use a dedicated ops template)
- Design or UX work (this team writes code, not designs)

## Team Composition

| Agent | Model | Role |
|-------|-------|------|
| Coordinator / Planner | Sonnet 4.5 | Task decomposition, dependency analysis, milestone tracking |
| Implementation Specialist A | Opus 4.6 | Primary feature development, complex logic |
| Implementation Specialist B | Opus 4.6 | Parallel secondary feature development |
| Code Reviewer | Opus 4.6 | Quality enforcement, security review, style adherence |
| Test Engineer | Sonnet 4.5 | Test generation, coverage analysis, holdout validation |
| Documentation Writer | Haiku 4.5 | API docs, README updates, inline comments |

## Quick Start

### 1. Prerequisites

Ensure you have:
- A GitHub repository with the target codebase
- A `GITHUB_TOKEN` with `repo` and `workflow` permissions
- A feature specification or requirements document

### 2. Configure the Team

```bash
cp CONFIG.md CONFIG.local.md
# Edit CONFIG.local.md with your project settings
```

Set the required environment variables:

```bash
export GITHUB_TOKEN="ghp_..."
```

### 3. Run the Team

Execute in hybrid mode (recommended):

```bash
claude-agent team run ./teams/code-implementation \
  --config CONFIG.local.md \
  --mode hybrid
```

### 4. Monitor Progress

The Coordinator logs phase transitions and user prompts at each gate:

```
[Phase 1/4] Planning -- Starting...
  [coordinator] Feature decomposed into 6 tasks
  [coordinator] Specialist A: 3 tasks (auth module, API routes, middleware)
  [coordinator] Specialist B: 3 tasks (notification service, email templates, queue)
[Phase 1/4] Planning -- Complete
```

## Estimated Cost

With default model configuration: **approximately $25-30** per feature.

See `cost-analysis.md` for detailed breakdowns and alternative configurations.

## Directory Structure

```
teams/code-implementation/
  README.md                          -- This file
  TEAM_SPEC.md                       -- Detailed architecture and specification
  MODEL_CONFIGS.md                   -- Model selection and cost comparison
  CONFIG.md                          -- Project configuration template
  ORCHESTRATION.md                   -- Multi-agent orchestration protocol
  cost-analysis.md                   -- Token budget and cost analysis
  deployment-guide.md                -- Step-by-step setup and run instructions
  agents/
    coordinator/AGENTS.md            -- Coordinator / Planner agent spec
    impl-specialist-a/AGENTS.md      -- Implementation Specialist A agent spec
    impl-specialist-b/AGENTS.md      -- Implementation Specialist B agent spec
    code-reviewer/AGENTS.md          -- Code Reviewer agent spec
    test-engineer/AGENTS.md          -- Test Engineer agent spec
    doc-writer/AGENTS.md             -- Documentation Writer agent spec
  mcp-servers/
    README.md                        -- MCP server setup guide
    github.json                      -- GitHub MCP server config
  scenarios/
    feature-development.md           -- Full feature development scenario
    bug-fix-workflow.md              -- Bug fix workflow scenario
    refactoring.md                   -- Code refactoring scenario
    api-endpoint.md                  -- API endpoint development scenario
  examples/
    crud-feature.md                  -- CRUD feature example
    auth-integration.md              -- Auth integration example
    api-migration.md                 -- API migration example
```

## Key Design Principles

1. **Parallel by default.** Implementation Specialists A and B work concurrently on independent sub-features. The Coordinator ensures no shared-file conflicts.
2. **Holdout testing.** The Test Engineer writes scenarios before seeing the implementation, preventing implementation bias in test design.
3. **Structured review.** The Code Reviewer separates blocking issues from suggestions. Only blockers require resolution before merge.
4. **Convention adherence.** All agents match the existing project's style, patterns, and conventions. No agent introduces new patterns without Coordinator approval.
5. **Cost awareness.** Every agent operates within a token budget. The Coordinator tracks total spend and alerts when approaching limits.

## Related Documentation

- [TEAM_SPEC.md](TEAM_SPEC.md) -- Full architecture specification
- [ORCHESTRATION.md](ORCHESTRATION.md) -- Phase-by-phase execution protocol
- [deployment-guide.md](deployment-guide.md) -- How to set up and run
- [cost-analysis.md](cost-analysis.md) -- Budget planning
