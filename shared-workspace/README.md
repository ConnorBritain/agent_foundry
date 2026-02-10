# Shared Workspace

The shared workspace is the coordination hub for multi-team Agent Foundry projects. All teams read from and write to this directory to stay synchronized.

## Structure

```
shared-workspace/
├── artifacts/                  # Team deliverables
│   ├── c-suite/               # Strategy docs, financials, pitch decks
│   ├── web-app-development/   # Deployed apps, API docs, source code
│   ├── sales-marketing/       # GTM strategy, campaigns, CRM setup
│   ├── recruitment-hr/        # Job descriptions, onboarding, culture docs
│   ├── content-creation/      # Brand guidelines, copy, content calendar
│   ├── code-implementation/   # Features, tests, documentation
│   ├── project-planning/      # Plans, timelines, dependency maps
│   └── research-deep-dive/    # Market analysis, competitive intel, reports
├── project-status.json         # Real-time team status dashboard
├── cross-team-communication.md # Inter-team messaging log
├── dependency-tracker.md       # Blocking dependency registry
└── weekly-summaries/           # Orchestrator weekly reports
```

## How Teams Use This

### Writing Artifacts

Each team writes its deliverables to `artifacts/<team-name>/`:

```
artifacts/c-suite/
├── business-plan-v1.md
├── financial-model.md
├── pitch-deck-outline.md
└── org-design.md
```

Teams should use descriptive filenames and include version numbers when iterating.

### Reading Dependencies

Teams check `dependency-tracker.md` for required inputs from other teams. When a dependency is resolved, the providing team:

1. Writes the artifact to `artifacts/<their-team>/`
2. Updates the dependency status in `dependency-tracker.md`
3. Posts a message in `cross-team-communication.md`

### Status Updates

Teams update `project-status.json` at each phase transition:

```json
{
  "team": "business-planning",
  "status": "active",
  "phase": "financial-modeling",
  "progress": "65%",
  "artifacts_path": "shared-workspace/artifacts/c-suite/",
  "last_update": "2026-02-09T20:30:00Z"
}
```

### Cross-Team Communication

Teams post messages to `cross-team-communication.md`:

```markdown
### [14:32] Business Planning → Content Creation
Brand positioning document is ready at artifacts/c-suite/positioning.md
Priority: High
```

## Monitoring

Use the control plane dashboard to monitor all teams:

```bash
python3 common/utilities/control-plane.py --project projects/your-project
```

## Conventions

- **File ownership**: Only the producing team writes to its artifacts directory
- **Read-only access**: Teams read from other teams' artifacts but never modify them
- **Timestamps**: Use ISO 8601 format (e.g., `2026-02-09T14:32:00Z`)
- **Versioning**: Use `-v1`, `-v2` suffixes for iterations (e.g., `business-plan-v2.md`)
- **Status values**: `active`, `awaiting`, `completed`, `blocked`, `paused`
