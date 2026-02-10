---
skill_name: "file-management"
version: "1.0.0"
description: "Organize workspace files, manage artifacts, and maintain directory structure"
author: "Sforza"
triggers:
  - "when creating new deliverables"
  - "when organizing workspace output"
  - "when preparing artifacts for handoff"
---

# File Management Skill

## Purpose

Maintain consistent file organization across team workspaces and the shared artifact directory.

## Directory Structure

Each team operates within two directories:

```
# Team workspace (working files, drafts, intermediate outputs)
projects/<project>/<team>-workspace/
├── drafts/
├── research/
├── logs/
└── temp/

# Shared artifacts (final deliverables for other teams and the user)
projects/<project>/shared-workspace/artifacts/<team>/
├── <deliverable-v1>.md
├── <deliverable-v2>.md
└── ...
```

## Naming Conventions

### Files
- Use kebab-case: `business-plan-v1.md`, not `Business Plan v1.md`
- Include version suffix for iterated docs: `-v1`, `-v2`, `-v3`
- Use descriptive names: `competitor-feature-matrix.md`, not `analysis.md`
- Date-prefix logs: `2026-02-10-phase-1-log.md`

### Directories
- Use kebab-case: `market-research/`, not `Market Research/`
- Group by category, not by date

## Artifact Lifecycle

### 1. Draft (workspace only)
```
<team>-workspace/drafts/business-plan-draft.md
```
Working document, may change frequently. Not visible to other teams.

### 2. Review (workspace)
```
<team>-workspace/business-plan-review.md
```
Ready for internal team review. Still in workspace.

### 3. Published (shared artifacts)
```
shared-workspace/artifacts/<team>/business-plan-v1.md
```
Final deliverable. Visible to all teams and the user. Treat as immutable — create v2 instead of editing.

## File Operations

### Creating Artifacts
1. Write draft to workspace
2. Review and refine
3. Copy final version to `shared-workspace/artifacts/<team>/`
4. Post notification to `cross-team-communication.md`
5. Update `project-status.json` with artifact path

### Versioning
- Never overwrite a published artifact
- Create new version: `business-plan-v1.md` → `business-plan-v2.md`
- Note version in cross-team communication

### Cleanup
- Remove temp files after use
- Archive drafts when final version is published
- Keep workspace organized — don't let files accumulate

## Cross-Team File Access

**Read**: Any team can read any artifact in `shared-workspace/artifacts/`
**Write**: Teams only write to their own artifact directory
**Never**: Modify another team's artifacts — create your own derivative instead

## Large Outputs

For deliverables over 500 lines:
- Split into logical sections (e.g., `business-plan-executive-summary.md`, `business-plan-financials.md`)
- Create an index file listing all parts
- Reference section files from the index
