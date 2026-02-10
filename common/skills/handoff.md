---
skill_name: "handoff"
version: "1.0.0"
description: "Transfer deliverables and context between teams via shared workspace"
author: "Sforza"
triggers:
  - "when a dependency is resolved for another team"
  - "when a team completes and the next team needs context"
  - "when artifacts are ready for cross-team consumption"
---

# Handoff Skill

## Purpose

Manage the transfer of deliverables, context, and decisions between Sforza teams through the shared workspace coordination layer.

## Handoff Types

### 1. Dependency Resolution
One team produces an artifact another team is waiting for.

**Example**: C-Suite produces brand positioning → Content Creation unblocks.

### 2. Phase Transition
One team completes, and a subsequent team needs its outputs as input.

**Example**: C-Suite completes → Web App Development uses business plan for product requirements.

### 3. Parallel Coordination
Teams running simultaneously need to share intermediate findings.

**Example**: Research discovers competitor feature → Web App Development adjusts roadmap.

## Handoff Protocol

### Step 1: Prepare the Artifact

- Ensure the deliverable passes quality check (see quality-check skill)
- Place final version in `shared-workspace/artifacts/<your-team>/`
- Use clear, descriptive filename

### Step 2: Post Notification

Write to `shared-workspace/cross-team-communication.md`:

```markdown
### [TIMESTAMP] SOURCE_TEAM → TARGET_TEAM
Handoff: DEPENDENCY_NAME
Artifact: shared-workspace/artifacts/SOURCE_TEAM/filename.md
Summary: Brief description of what's included and how to use it.
Priority: High | Medium | Low
```

### Step 3: Update Dependency Tracker

Update `shared-workspace/dependency-tracker.md`:

```markdown
| From Team | To Team | Dependency | Status | Completed |
|-----------|---------|------------|--------|-----------|
| Content | C-Suite | Brand positioning | Resolved | 2026-02-10 |
```

### Step 4: Update Project Status

Update `shared-workspace/project-status.json` to reflect the dependency resolution.

## Context Package

For major handoffs (phase transitions), prepare a context package:

```markdown
# Handoff: C-Suite → Web App Development

## Key Deliverables
1. Business Plan: artifacts/c-suite/business-plan-v1.md
2. Financial Model: artifacts/c-suite/financial-model.md
3. Brand Positioning: artifacts/c-suite/brand-positioning.md

## Key Decisions Made
- Target market: Time-starved parents (25-45)
- Pricing: $8.99/month subscription
- Tech stack preference: Next.js + Supabase (from CTO recommendation)

## Constraints for Next Team
- MVP must launch within 2 weeks
- Budget for web-app-development: $315
- Must support Stripe for payments (per financial model)

## Open Questions
- Logo design not finalized (Content team still working)
- Exact feature set for MVP vs v2 needs prioritization
```

## Common Handoff Paths

| From | To | What's Handed Off |
|------|----|-------------------|
| C-Suite | Web App Dev | Business plan, requirements, tech preferences |
| C-Suite | Content | Brand positioning, messaging framework |
| C-Suite | Sales & Marketing | GTM strategy, pricing, target segments |
| Research | C-Suite | Market validation, competitive landscape |
| Research | Content | Target personas, topic research |
| Content | Sales & Marketing | Brand guidelines, messaging, copy |
| Web App Dev | Code Implementation | Architecture, API specs, tech debt list |
| Project Planning | ALL | Schedules, dependencies, resource allocation |

## Handoff Failures

If a handoff artifact is missing, incomplete, or unclear:

1. Post a clarification request to cross-team-communication.md
2. Be specific about what's missing or unclear
3. Continue any work that doesn't depend on the missing information
4. Escalate to user if the producing team has already completed
