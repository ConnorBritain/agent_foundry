---
skill_name: "status-reporting"
version: "1.0.0"
description: "Report progress, phase transitions, and blockers to the shared workspace"
author: "Agent Foundry"
triggers:
  - "at the start of each phase"
  - "at the completion of each phase"
  - "when blocked on a dependency"
  - "when user requests status"
---

# Status Reporting Skill

## Purpose

Maintain real-time visibility into team progress by updating shared workspace files at key moments during execution.

## When to Report

1. **Phase start** — Team begins a new execution phase
2. **Phase complete** — Team finishes a phase, deliverables ready
3. **Blocker encountered** — Team cannot proceed without external input
4. **Blocker resolved** — Dependency met, resuming work
5. **Decision needed** — User approval required before continuing
6. **Team complete** — All phases finished, final deliverables ready

## Status Update Format

### project-status.json Entry

```json
{
  "team": "content-creation",
  "status": "active",
  "phase": "Phase 2: Content Drafting",
  "phase_number": 2,
  "total_phases": 4,
  "progress_pct": 45,
  "current_task": "Drafting blog post series on meal planning",
  "blockers": [],
  "cost_to_date": 34.50,
  "last_update": "2026-02-10T14:30:00Z",
  "artifacts_produced": [
    "shared-workspace/artifacts/content-creation/research-brief.md",
    "shared-workspace/artifacts/content-creation/content-outline.md"
  ]
}
```

### Status Values

| Status | Meaning |
|--------|---------|
| `initializing` | Reading specs, setting up workspace |
| `active` | Actively working on current phase |
| `awaiting` | Waiting on dependency from another team |
| `blocked` | Cannot proceed — needs user input |
| `paused` | Intentionally paused (rate limit, budget) |
| `completed` | All phases finished |
| `error` | Encountered unrecoverable error |

## Cross-Team Communication

Post messages to `shared-workspace/cross-team-communication.md`:

### Phase Completion
```markdown
### [14:32] Content Creation → ALL
Phase 2 complete. Blog post drafts ready at:
artifacts/content-creation/blog-drafts/
Priority: Medium
```

### Dependency Request
```markdown
### [10:15] Content Creation → C-Suite
BLOCKED: Need brand positioning document to begin messaging work.
Dependency: brand_positioning
Priority: High
```

### Dependency Resolution
```markdown
### [11:45] C-Suite → Content Creation
Brand positioning document ready at:
artifacts/c-suite/brand-positioning.md
Resolves: brand_positioning
Priority: High
```

## Blocker Escalation

If blocked for more than 30 minutes:
1. Post to cross-team-communication.md (if dependency on another team)
2. Update project-status.json with blocker details
3. If user input needed, format a clear decision request with options
4. Continue any unblocked parallel work while waiting

## Final Report

When team completes all phases:

```markdown
## Team Complete: [Team Name]

**Duration**: X hours Y minutes
**Total Cost**: $XX.XX
**Phases**: N/N complete

### Deliverables
1. [artifact-name.md](path) — Description
2. [artifact-name.md](path) — Description

### Key Decisions Made
- Decision 1: [choice] — rationale
- Decision 2: [choice] — rationale

### Recommendations for Next Steps
- Suggested follow-up team or action
```
