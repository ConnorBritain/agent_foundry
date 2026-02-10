---
skill_name: "checkpoint"
version: "1.0.0"
description: "Save session state for resume after interruption or context limit"
author: "Sforza"
triggers:
  - "when approaching context window limit"
  - "when session is ending unexpectedly"
  - "at the end of each major phase"
  - "when user requests a checkpoint"
---

# Checkpoint Skill

## Purpose

Preserve session state so that work can resume in a new Claude Code session without loss of progress. Critical for long-running teams that may hit context limits or rate caps.

## When to Checkpoint

1. **Phase completion** — Natural checkpoint at each orchestration phase boundary
2. **Context approaching limit** — When conversation exceeds ~150K tokens (75% of 200K window)
3. **Rate limit hit** — When Claude Max plan throttles, save state before pausing
4. **End of day** — If user is stopping for the day, checkpoint current state
5. **Before risky operations** — Before major refactors or destructive operations

## Checkpoint Format

Write a checkpoint file to the team workspace:

```markdown
# Checkpoint: [Team Name]

**Created**: [timestamp]
**Session**: [session identifier or description]
**Phase**: [current phase number and name]
**Progress**: [percentage complete]

## Completed Work

### Phase 1: [Phase Name] — COMPLETE
- [x] Task 1 — output at: [path]
- [x] Task 2 — output at: [path]

### Phase 2: [Phase Name] — IN PROGRESS (60%)
- [x] Task 3 — output at: [path]
- [ ] Task 4 — started, draft at: [path]
- [ ] Task 5 — not started

## Key Decisions Made
- Decision 1: [choice] — [rationale]
- Decision 2: [choice] — [rationale]

## Current Context
- Working on: [specific task description]
- Blocked by: [nothing / dependency description]
- Next step: [exactly what to do when resuming]

## Files Created This Session
1. [path/to/file1.md] — [description]
2. [path/to/file2.md] — [description]

## Important Context for Resume
[Any information the next session needs that isn't captured in files.
This might include user preferences, rejected approaches, or
intermediate reasoning that informed decisions.]

## Cost So Far
- Tokens used: [input/output]
- Estimated cost: $XX.XX
- Budget remaining: $XX.XX

## Resume Instructions
1. Read this checkpoint file
2. Read the project charter at: [path]
3. Read the latest artifacts at: [paths]
4. Continue with: [specific next task]
```

## Checkpoint Location

Save checkpoints to:
```
projects/<project>/<team>-workspace/checkpoints/
├── checkpoint-phase-1-complete.md
├── checkpoint-phase-2-partial.md
└── checkpoint-latest.md  (always overwrite this with most recent)
```

## Resuming from Checkpoint

When starting a new session after interruption:

1. **Load checkpoint**: Read `checkpoints/checkpoint-latest.md`
2. **Load charter**: Read `PROJECT_CHARTER.md` for project context
3. **Load recent artifacts**: Read files listed in checkpoint
4. **Verify state**: Check that files mentioned in checkpoint still exist
5. **Continue**: Pick up from the "Next step" in the checkpoint

### Resume Prompt Template

```
You are resuming work on the [TEAM_NAME] team for an Sforza project.

Read the checkpoint at: [CHECKPOINT_PATH]
Read the project charter at: [CHARTER_PATH]

Continue from where the previous session left off. The checkpoint
describes exactly what was completed and what needs to happen next.
```

## Automatic Checkpointing

Teams should checkpoint automatically:
- After every phase completion (natural boundary)
- Every ~50K tokens of conversation (preventive)
- Whenever writing a major deliverable to artifacts (incremental)

## Context Window Management

To stay within the 200K token window:
- Summarize earlier conversation when context grows large
- Reference files by path rather than including full content repeatedly
- Use checkpoint-resume for work that will exceed one session
- Break large teams into multiple sessions if needed (e.g., Phase 1-2 in session 1, Phase 3-4 in session 2)
