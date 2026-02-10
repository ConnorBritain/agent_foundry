# Long-Running Agent Strategies

> Managing agents that exceed single context windows through checkpointing, session resumption, and multi-session workflows.

## Overview

Most Sforza tasks complete within a single context window. But some don't. Large refactoring jobs, multi-day feature implementations, and complex debugging sessions can push agents past the 200K token context limit. When that happens, the agent loses track of earlier context, starts repeating itself, or simply fails.

Long-running agents require deliberate strategies: checkpointing progress, compressing context, resuming sessions cleanly, and splitting work across multiple sessions. Without these strategies, you waste tokens re-explaining context and risk inconsistent outputs as the agent forgets what it did earlier.

This guide covers practical patterns for managing agents that outlive a single context window, including concrete implementations you can apply to your Sforza team configurations.

## Understanding Context Window Limits

### The 200K Token Budget

All current Claude models share a 200K token context window. This sounds large, but in practice it fills faster than expected.

**Typical token consumption per interaction cycle:**

| Component | Tokens | Notes |
|---|---|---|
| System prompt | 500-2,000 | Agent personality, instructions, constraints |
| Codebase context (files read) | 10,000-50,000 | Each file read adds to context |
| Tool calls and results | 2,000-10,000 | Per tool invocation round-trip |
| Conversation history | Grows continuously | Every message adds to the total |
| Model output | 1,000-8,000 | Per response |

**A single development session** with 20 interaction cycles, reading 15 files, and executing 10 commands can consume 80,000-150,000 tokens. Complex sessions can exceed the window in 30-40 cycles.

### Signs an Agent Is Hitting Context Limits

- The agent starts "forgetting" decisions it made earlier in the session.
- Responses become repetitive, re-reading files it already processed.
- The agent contradicts its own earlier output.
- Error rates increase on tasks that were previously handled correctly.
- The harness truncates or summarizes earlier conversation turns.

## Strategy 1: Checkpointing

Checkpointing saves a snapshot of the agent's progress at defined intervals so work can be resumed without re-processing everything.

### What to Checkpoint

A useful checkpoint contains:

```yaml
checkpoint:
  timestamp: "2026-02-10T14:30:00Z"
  agent: "backend-developer"
  session_id: "sess_abc123"

  # What has been accomplished
  completed_tasks:
    - "Created database schema for user_profiles table"
    - "Implemented GET /api/users endpoint"
    - "Added input validation middleware"

  # What comes next
  pending_tasks:
    - "Implement POST /api/users endpoint"
    - "Add authentication middleware"
    - "Write integration tests"

  # Key decisions made (so the next session doesn't re-debate them)
  decisions:
    - "Using PostgreSQL with Drizzle ORM (not Prisma) per architect guidance"
    - "REST API, not GraphQL, per specification"
    - "JWT tokens stored in httpOnly cookies"

  # Files modified (so the next session knows what exists)
  modified_files:
    - path: "src/db/schema.ts"
      status: "complete"
    - path: "src/routes/users.ts"
      status: "in_progress"
    - path: "src/middleware/validate.ts"
      status: "complete"

  # Current blockers or open questions
  blockers:
    - "Waiting on auth team to provide JWT signing key format"
```

### Checkpoint Triggers

Set checkpoints based on events, not just time:

| Trigger | When | Why |
|---|---|---|
| **Task completion** | After each discrete task finishes | Natural pause point with clean state |
| **Token threshold** | At 60% and 80% of context window | Proactive, before context degrades |
| **Error recovery** | After resolving a significant error | Preserve the debugging context |
| **Decision point** | After making an architectural decision | Decisions are expensive to re-derive |
| **File milestone** | After completing changes to a file | Atomic unit of work |

### Implementing Checkpoints

Sforza checkpoints are written to the shared state directory:

```bash
# Checkpoint file location
shared-state/{team-name}/{agent-name}/checkpoints/checkpoint_{timestamp}.yaml

# Latest checkpoint symlink
shared-state/{team-name}/{agent-name}/checkpoints/latest.yaml
```

Include a checkpoint instruction in the agent's system prompt:

```
After completing each task, write a checkpoint file to your shared state directory.
The checkpoint must include: completed tasks, pending tasks, key decisions, and
modified files. This checkpoint will be used to resume your work if the session ends.
```

## Strategy 2: Context Compression

When context is growing but the session is not yet complete, compress the existing context to free up space.

### Summarize-and-Replace Pattern

At a defined threshold (e.g., 60% of context window), the agent summarizes its conversation history into a compact state document and starts a "fresh" turn with that summary as context.

**Implementation approach:**

1. Agent reaches the token threshold.
2. Agent writes a comprehensive state summary to a file.
3. The orchestrator starts a new session for the agent.
4. The new session loads the summary file as initial context.

```yaml
# Context compression configuration
context_management:
  compression_threshold: 0.6  # Trigger at 60% of context window
  strategy: summarize_and_resume
  summary_location: "shared-state/{team}/{agent}/context_summary.md"
  summary_instructions: |
    Write a detailed summary of your current session including:
    1. All tasks completed with specific file paths and changes made
    2. Current task in progress and exact state
    3. All decisions made and their rationale
    4. Any open questions or blockers
    5. The next steps you would take
```

### Progressive Summarization

Instead of one big compression event, progressively summarize older context as it ages:

```
[Most recent 40% of context] -- Full detail, verbatim
[Middle 30% of context] -- Summarized to key actions and decisions
[Oldest 30% of context] -- Compressed to one-paragraph overview
```

This keeps recent work in full fidelity while preserving awareness of earlier work.

### File-Based Context Offloading

Move detailed context into files that the agent can re-read on demand:

```
# Instead of keeping all code changes in conversation history,
# write progress notes to a working document:

shared-state/{team}/{agent}/working-notes.md

# The agent reads this file at the start of each turn
# and appends to it at the end of each turn.
# Conversation history only needs to reference the file, not contain its contents.
```

## Strategy 3: Session Resumption

When a session ends (context exhaustion, timeout, crash, or rate limit), the next session must resume cleanly.

### Resumption Protocol

```
Session Start Protocol:
1. Check for latest checkpoint file
2. Read the checkpoint to understand current state
3. Read the working notes file for detailed context
4. Verify the state of modified files (are changes still there?)
5. Identify the next pending task
6. Continue work from that point
```

### Resumption Prompt Template

Include this in the agent's system prompt when resuming:

```markdown
You are resuming a previous work session. Your checkpoint file is at:
{checkpoint_path}

Read the checkpoint first. It contains:
- Tasks you already completed (do NOT redo these)
- Your next pending tasks
- Key decisions already made (follow these, do not re-debate)
- Files you modified (verify they exist and contain your changes)

If any previously completed work is missing or corrupted, flag it as a blocker
rather than silently redoing it.
```

### State Verification

A resumed agent should verify its environment before continuing:

```yaml
resumption:
  verification_steps:
    - action: "Read checkpoint file"
      on_failure: "Start fresh — no prior state exists"
    - action: "Verify modified files exist"
      on_failure: "Log missing files, add to pending tasks"
    - action: "Run tests on completed work"
      on_failure: "Add failing tests to pending tasks"
    - action: "Check for new instructions from orchestrator"
      on_failure: "Continue with existing pending tasks"
```

## Strategy 4: Multi-Session Workflows

For very large tasks, plan for multiple sessions from the start rather than trying to fit everything into one.

### Task Decomposition for Multi-Session Work

Break large tasks into session-sized chunks:

```
Large Task: "Migrate authentication system from sessions to JWT"

Session 1: Analysis and Planning
  - Read all auth-related files
  - Document current authentication flow
  - Design JWT implementation plan
  - Checkpoint: plan document + file inventory

Session 2: Core Implementation
  - Implement JWT token generation
  - Implement token validation middleware
  - Update login endpoint
  - Checkpoint: core JWT code complete

Session 3: Migration
  - Update all protected routes to use JWT
  - Migrate session storage to token-based
  - Update client-side token handling
  - Checkpoint: migration complete

Session 4: Testing and Cleanup
  - Write tests for new auth flow
  - Remove deprecated session code
  - Update documentation
  - Final checkpoint: task complete
```

### Session Budget Estimation

Estimate how many sessions a task will require:

| Task Size | Files Involved | Estimated Sessions | Model Recommendation |
|---|---|---|---|
| Small (single feature) | 1-5 files | 1 session | Sonnet 4.5 |
| Medium (multi-file feature) | 5-15 files | 1-2 sessions | Sonnet 4.5 |
| Large (cross-cutting change) | 15-40 files | 2-4 sessions | Sonnet 4.5 + Opus for planning |
| Very Large (system migration) | 40+ files | 4-8 sessions | Opus for planning, Sonnet for execution |

### Orchestrator-Managed Sessions

The orchestrator agent can manage multi-session workflows:

```yaml
orchestrator_config:
  multi_session:
    enabled: true
    max_sessions_per_task: 8
    session_handoff:
      method: "checkpoint_file"
      require_verification: true
    escalation:
      on_stuck: "reassign_to_opus"
      on_repeated_failure: "alert_human"
```

## Strategy 5: Handling Rate Limits

Rate limits can interrupt agent sessions unexpectedly. Plan for graceful degradation.

### Rate Limit Response Strategies

| Situation | Strategy |
|---|---|
| **Brief rate limit (< 60s)** | Wait and retry automatically |
| **Extended rate limit (1-5 min)** | Checkpoint current state, wait, resume |
| **Sustained rate limit (> 5 min)** | Checkpoint, pause agent, redistribute work to other agents |
| **Quota exhaustion** | Checkpoint all agents, stop team, alert user |

### Backoff Configuration

```yaml
rate_limits:
  retry:
    initial_delay: 5      # seconds
    max_delay: 300         # seconds
    backoff_multiplier: 2
    max_retries: 10
  on_quota_exhaustion:
    action: "checkpoint_and_halt"
    alert: true
    message: "API quota exhausted. All agents checkpointed. Resume with: af resume {team}"
```

### Load Balancing Across Rate Limit Tiers

If you have multiple API keys or rate limit tiers, distribute agent load:

```yaml
api_keys:
  primary:
    key_env: "ANTHROPIC_API_KEY_PRIMARY"
    rate_limit_tier: 4
    assigned_agents: ["orchestrator", "lead-developer"]
  secondary:
    key_env: "ANTHROPIC_API_KEY_SECONDARY"
    rate_limit_tier: 2
    assigned_agents: ["test-writer", "formatter", "doc-writer"]
```

## Strategy 6: Context-Efficient Agent Design

Design agents to use context efficiently from the start, reducing the need for the strategies above.

### Minimize File Reads

```
# Bad: Agent reads every file to "understand the project"
Read all files in src/ directory

# Good: Agent reads only what it needs for the current task
Read the specific file I need to modify and its direct imports
```

### Use Structured Output

```
# Bad: Agent writes long prose explanations in conversation
"I've analyzed the codebase and found that the authentication module
uses a session-based approach with Redis storage. The sessions are
created in the login handler at src/auth/login.ts and validated by..."

# Good: Agent writes structured summaries
ANALYSIS:
- Auth: session-based, Redis storage
- Login: src/auth/login.ts
- Validation: src/middleware/auth.ts
- Decision: Migrate to JWT (per spec)
```

### Externalize State

```
# Bad: Keep all state in conversation context
(Agent remembers everything through conversation history)

# Good: Write state to files, read on demand
Write progress to: shared-state/team/agent/progress.md
Read only when needed for the current task
```

## Recommendations

### For tasks expected to fit in one session
Add a single checkpoint instruction at the 60% context mark. This costs almost nothing and provides a safety net if the task runs longer than expected.

### For tasks that will require 2-3 sessions
Plan session boundaries around natural task boundaries. Use the checkpoint-and-resume pattern. Include state verification in the resumption prompt.

### For tasks requiring 4+ sessions
Use orchestrator-managed multi-session workflows. Decompose the work into discrete phases. Use Opus for the planning phase and Sonnet for execution phases.

### For unpredictable workloads
Implement progressive context compression. Set token threshold alerts at 50%, 70%, and 90%. Configure automatic checkpointing on all threshold events.

### For teams with rate limit concerns
Distribute agents across multiple API keys. Configure exponential backoff with automatic checkpointing on rate limits. Assign critical-path agents to higher-tier API keys.

## Related Resources

- [Model Selection Guide](./model-selection-guide.md) — Model capabilities and context window details
- [Optimization Guide](./optimization-guide.md) — Token budgeting and prompt caching strategies
- [Decision Framework](./decision-framework.md) — Planning team configurations and execution strategies
- [Quality Assurance](./quality-assurance.md) — Validating outputs across multi-session workflows
