# Sforza Daemon — Claude Code Kickoff Prompt

Use this prompt to start a new Claude Code session for building the daemon.

---

## The Prompt

```
You are building the **Sforza Daemon** — the v2.0 flagship feature of the Sforza project.

## Context

Sforza (https://github.com/ConnorBritain/sforza) is an open-source operating system for building businesses with coordinated AI agent teams. v1.0 provides:

- 8 team templates (c-suite, web-app-development, sales-marketing, recruitment-hr, content-creation, code-implementation, project-planning, research-deep-dive)
- Each team is a set of agent system prompts (AGENTS.md files), orchestration plans, MCP configs, scenarios, and examples
- An Orchestrator agent (ORCHESTRATOR.md) that interviews users about their project and creates a PROJECT_CHARTER.md
- Launch scripts that open Claude Code sessions for each team
- A terminal control-plane.py dashboard
- Shared workspace coordination (project-status.json, cross-team-communication.md, dependency-tracker.md)

**The v1.0 limitation:** Users must manually open Claude Code sessions for each team, manually coordinate between them, and manually monitor progress. The daemon eliminates this.

## What You're Building

This repo (https://github.com/ConnorBritain/sforza_daemon) is a **standalone Python daemon + CLI** that:

1. **Manages multiple concurrent Anthropic API conversations** — one per agent team
2. **Coordinates cross-team dependencies** — when Business Planning produces positioning, Content Creation automatically unblocks
3. **Routes approval requests to the user** — via CLI, with a REST API for future UI
4. **Enforces budget guardrails** — tracks tokens/cost per team, alerts at thresholds, hard-stops at limits
5. **Persists all state to SQLite** — full conversation replay, checkpoint/resume, time-travel debugging

## Architecture

```
sforza-daemon/
├── pyproject.toml              # Package config (use uv/poetry)
├── README.md                   # Setup, usage, architecture
├── src/
│   └── sforza_daemon/
│       ├── __init__.py
│       ├── main.py             # Entry point, daemon lifecycle
│       ├── config.py           # Settings, env vars, defaults
│       │
│       ├── orchestrator/
│       │   ├── __init__.py
│       │   ├── engine.py       # Core orchestration loop
│       │   ├── interview.py    # User interview flow (mirrors ORCHESTRATOR.md)
│       │   ├── charter.py      # PROJECT_CHARTER.md generation
│       │   └── planner.py      # Team sequencing, dependency graph, scheduling
│       │
│       ├── agents/
│       │   ├── __init__.py
│       │   ├── manager.py      # Agent lifecycle (spawn, monitor, kill, restart)
│       │   ├── session.py      # Single agent conversation wrapper
│       │   └── prompt_loader.py # Load AGENTS.md + team context into system prompt
│       │
│       ├── messaging/
│       │   ├── __init__.py
│       │   ├── queue.py        # In-memory message queue (asyncio)
│       │   ├── router.py       # Cross-team message routing rules
│       │   └── models.py       # Message types (dependency_resolved, approval_needed, status_update, etc.)
│       │
│       ├── state/
│       │   ├── __init__.py
│       │   ├── database.py     # SQLite via aiosqlite
│       │   ├── models.py       # SQLAlchemy/dataclass models (Project, Team, Agent, Decision, Message, CostEntry)
│       │   └── migrations.py   # Schema versioning
│       │
│       ├── cost/
│       │   ├── __init__.py
│       │   ├── tracker.py      # Per-agent, per-team, per-project token/cost tracking
│       │   ├── budget.py       # Budget enforcement (alert at 80%, block at 100%)
│       │   └── pricing.py      # Anthropic pricing table (Opus/Sonnet/Haiku per-token rates)
│       │
│       ├── api/
│       │   ├── __init__.py
│       │   ├── server.py       # FastAPI REST server
│       │   ├── routes.py       # GET /status, POST /approve, GET /teams, POST /launch, etc.
│       │   └── websocket.py    # WebSocket for real-time dashboard updates
│       │
│       └── cli/
│           ├── __init__.py
│           └── commands.py     # Typer CLI: init, start, stop, status, approve, logs, export
│
├── tests/
│   ├── test_orchestrator.py
│   ├── test_agent_session.py
│   ├── test_messaging.py
│   ├── test_cost_tracker.py
│   └── conftest.py             # Fixtures with mock Anthropic client
│
└── docker/                     # Optional containerized deployment
    ├── Dockerfile
    └── docker-compose.yml
```

## Technical Decisions

### Stack
- **Python 3.12+** with full async/await (asyncio)
- **anthropic** SDK (latest) for API conversations
- **FastAPI** for REST API + WebSocket
- **Typer** for CLI
- **SQLite** via **aiosqlite** for state (no heavy DB dependency)
- **Pydantic** for data models and validation
- **uv** for package management

### Key Design Principles
1. **Async-first** — All agent conversations run concurrently via asyncio tasks
2. **State is truth** — SQLite is the single source of truth. If the daemon crashes, it resumes from DB state.
3. **Sforza templates are external** — The daemon reads team templates from a configured `FOUNDRY_ROOT` path (the sforza repo clone). It does NOT embed templates.
4. **Anthropic API conversations are stateless** — Each API call sends the full conversation history. The daemon manages this history in SQLite.
5. **Budget is a hard constraint** — The daemon NEVER exceeds budget without explicit user approval via the approve flow.

### How Agent Conversations Work

Each "agent" is a conversation with the Anthropic Messages API:

```python
# Simplified — the actual implementation uses streaming
async def run_agent_turn(session: AgentSession) -> str:
    """Send the current conversation to Anthropic and get the next response."""
    response = await anthropic_client.messages.create(
        model=session.model,  # opus-4-6 for coordinators, sonnet-4-5 for specialists
        max_tokens=8192,
        system=session.system_prompt,  # Loaded from AGENTS.md + team context + charter
        messages=session.conversation_history,  # Full history from SQLite
        tools=session.tools,  # MCP-style tools if configured
    )

    # Persist response to SQLite
    await state.save_message(session.id, response)

    # Track cost
    await cost_tracker.record(session.team_id, response.usage)

    # Check for cross-team messages in response
    await router.process_agent_output(session, response)

    # Check for approval requests
    if needs_user_approval(response):
        await queue.publish(ApprovalNeeded(session=session, decision=extract_decision(response)))

    return response.content
```

### Cross-Team Coordination

The daemon replaces the file-based shared-workspace with an in-memory message queue:

```python
# When Business Planning produces positioning:
await queue.publish(DependencyResolved(
    from_team="c-suite",
    to_team="content-creation",
    dependency="brand_positioning",
    artifact_path="/path/to/positioning.md"
))

# Content Creation's orchestration engine picks this up:
async def on_dependency_resolved(msg: DependencyResolved):
    session = await manager.get_session(msg.to_team)
    # Inject the artifact into the agent's next turn
    session.inject_message(f"Dependency resolved: {msg.dependency}. "
                          f"Read the artifact at: {msg.artifact_path}")
    # Resume the agent
    await engine.resume_agent(session)
```

### User Approval Flow

```python
# CLI: sforza approve
@app.command()
def approve(decision_id: str, choice: str = None):
    """Approve a pending decision."""
    decision = state.get_decision(decision_id)
    if choice:
        decision.resolve(choice)
    else:
        # Interactive: show options, let user pick
        display_decision(decision)
        choice = prompt_user(decision.options)
        decision.resolve(choice)

    # Unblock the waiting agent
    queue.publish(DecisionApproved(decision_id=decision_id, choice=choice))

# REST API: POST /api/approve
@router.post("/api/approve/{decision_id}")
async def approve_decision(decision_id: str, body: ApprovalBody):
    # Same logic, for web/Electron frontend
    ...
```

## Reference Material

Clone the Sforza repo to understand the template format:
```bash
git clone https://github.com/ConnorBritain/sforza.git ../sforza
```

Key files to study:
- `ORCHESTRATOR.md` — The orchestrator's full system prompt and interview flow. The daemon's `orchestrator/interview.py` should implement this programmatically.
- `specs/ORCHESTRATOR_DAEMON.md` — The full vision doc for this daemon (architecture options, UX walkthrough, build plan, honest assessment)
- `specs/USER_INITIALIZATION_WORKFLOW.md` — How users interact with Sforza, the question flow, session management strategies
- `teams/web-app-development/TEAM_SPEC.md` — Example team spec (how agents are defined, their roles, orchestration phases)
- `teams/web-app-development/agents/coordinator/AGENTS.md` — Example agent system prompt
- `teams/web-app-development/ORCHESTRATION.md` — Example multi-phase execution plan
- `shared-workspace/project-status.json` — The status format the daemon should generate
- `common/utilities/control-plane.py` — The v1.0 terminal dashboard (the daemon's API replaces this)

## Build Plan

### Phase 1: Core daemon (Week 1-2)
1. Project scaffolding (pyproject.toml, src layout, basic tests)
2. `config.py` — Settings from env vars / config file (ANTHROPIC_API_KEY, FOUNDRY_ROOT, DB_PATH, etc.)
3. `state/database.py` + `state/models.py` — SQLite schema: projects, teams, agents, messages, decisions, cost_entries
4. `agents/prompt_loader.py` — Load AGENTS.md from Sforza templates, inject charter context
5. `agents/session.py` — Single agent conversation wrapper (send/receive with Anthropic API, persist to SQLite)
6. `agents/manager.py` — Spawn, monitor, and manage multiple concurrent sessions
7. `cost/tracker.py` + `cost/pricing.py` — Token counting and cost tracking per session

**Milestone: Can spawn a single agent team (e.g., c-suite coordinator) via script and have a conversation persisted to SQLite.**

### Phase 2: Orchestration (Week 2-3)
8. `messaging/models.py` + `messaging/queue.py` — Message types and async queue
9. `messaging/router.py` — Cross-team dependency routing
10. `orchestrator/engine.py` — Core orchestration loop (manage team lifecycle, phase transitions, dependency resolution)
11. `orchestrator/planner.py` — Build execution plan from charter (team order, parallelism, dependencies)
12. `cost/budget.py` — Budget enforcement with alerts and hard stops

**Milestone: Can run 2 teams in parallel with one dependency between them, automatically coordinating the handoff.**

### Phase 3: User Interface (Week 3-4)
13. `cli/commands.py` — Typer CLI (init, start, stop, status, approve, logs)
14. `orchestrator/interview.py` + `orchestrator/charter.py` — Interactive interview and charter generation
15. `api/server.py` + `api/routes.py` — FastAPI REST endpoints
16. `api/websocket.py` — Real-time status updates

**Milestone: Full CLI workflow: `sforza-daemon init "My SaaS"` → interview → `sforza-daemon start` → teams run → `sforza-daemon approve <id>` → deliverables appear.**

### Phase 4: Polish (Week 4)
17. Error recovery (agent crashes, API timeouts, network issues)
18. Checkpoint/resume (daemon restart picks up where it left off)
19. Integration test with real Sforza templates
20. Documentation

## CLI Interface

```bash
# Initialize a new project
sforza init "My SaaS Startup"
# Runs the interview, creates PROJECT_CHARTER.md

# Start the daemon (runs teams per charter)
sforza start
# Daemon runs in background, teams execute

# Check status
sforza status
# Shows active teams, progress, cost, pending decisions

# Approve a decision
sforza approve
# Interactive: shows pending decisions, lets you pick

sforza approve <decision-id> --choice "option_a"
# Non-interactive approval

# View logs
sforza logs                    # All teams
sforza logs c-suite            # Specific team
sforza logs c-suite --tail 50  # Last 50 messages

# Stop the daemon
sforza stop

# Export deliverables
sforza export --format zip --output ./deliverables.zip
```

## Environment Variables

```bash
ANTHROPIC_API_KEY=sk-ant-...          # Required
FOUNDRY_ROOT=/path/to/sforza   # Path to cloned sforza repo
AF_DB_PATH=~/.sforza/state.db  # SQLite database location
AF_LOG_LEVEL=INFO                     # Logging level
AF_API_PORT=8420                      # FastAPI server port
AF_DEFAULT_MODEL=claude-sonnet-4-5-20250929  # Default model for agents
AF_COORDINATOR_MODEL=claude-opus-4-6  # Model for coordinator agents
```

## Start Building

Begin with Phase 1. Set up the project scaffolding, then implement the SQLite state layer and single-agent conversation wrapper. Get a single agent talking to the Anthropic API with full conversation persistence before moving to multi-agent orchestration.

Focus on correctness over speed. The hardest problems are:
1. Managing concurrent async conversations without state corruption
2. Reliable cross-team message delivery and dependency resolution
3. Accurate cost tracking that matches Anthropic billing

Write tests as you go — mock the Anthropic client for unit tests, use a real API key for integration tests.
```

---

_Save this file for reference. Copy the content between the triple backticks to paste into Claude Code._
