# Teams Layer Specification

> **STATUS: STATIC REFERENCE** -- This file is never modified, only consulted.

## Purpose

The Teams Layer provides pre-configured multi-agent team templates for specific use cases. Each team template is a complete, deployable package containing agent definitions, coordination patterns, cost projections, and execution guides.

Teams are the primary unit of work in Agent Foundry. A user selects a team, configures it for their context, and deploys it to accomplish a complex goal that would be impractical for a single agent.

---

## Team Registry

| Team | Primary Use Case | Agent Count | Default Cost Range | Complexity |
|------|-----------------|-------------|-------------------|------------|
| Code Implementation | Build features from requirements to deployment | 6 | $30-150/feature | High |
| Project Planning | Transform goals into actionable project plans | 7 | $20-80/session | Medium |
| Content Creation | Research-backed, humanized content production | 7 | $15-60/article | Medium |
| C-Suite | Comprehensive business planning with executable artifacts | 7 | $50-200/plan | High |
| Research Deep Dive | Academic, market, or product research with configurable depth | 4-11 (modal) | $20-120/study | Variable |

---

## Universal Team Template Structure

Every team MUST follow this directory structure:

```
teams/[team-name]/
├── README.md                           # Overview, quick start, use cases
├── TEAM_SPEC.md                       # Detailed architecture and workflows
├── MODEL_CONFIGS.md                   # Team-specific model recommendations
├── ORCHESTRATION.md                   # Multi-agent coordination patterns
├── cost-analysis.md                   # Token projections and $ estimates
├── deployment-guide.md                # Step-by-step setup and execution
├── mcp-servers/
│   ├── [service-name].json
│   └── README.md                      # Setup prerequisites
├── agents/
│   ├── coordinator/
│   │   ├── AGENTS.md                  # Includes system prompt/personality
│   │   └── skills/
│   └── [specialists]/
│       ├── AGENTS.md
│       └── skills/
├── scenarios/                         # Holdout test scenarios (Software Factory pattern)
│   ├── scenario-1.md
│   └── scenario-2.md
└── examples/
    ├── example-workflow-1.md
    └── example-workflow-2.md
```

---

## Required Documentation Per Team

Each team template MUST include:

### 1. Use Case Description
- What problem does this team solve?
- Who is the target user?
- What are the inputs and outputs?
- When should a user choose this team vs. a single agent?

### 2. Agent Roster
- Number and type of agent instances
- Model assignment per agent (Haiku 4.5 / Sonnet 4.5 / Opus 4.6 / specialized)
- Personality profile per agent (reference common/personalities/ or define custom)
- Skills loaded per agent
- AGENTS.md content per agent (system prompt embedded)

### 3. Interaction Patterns
- How agents coordinate (parallel, sequential, hierarchical)
- Data flow between agents (what passes from one to the next)
- Conflict resolution (when agents disagree)
- Handoff protocols (how work transfers between phases)

### 4. Cost Projections
- Per-hour estimates for Haiku/Sonnet/Opus configurations
- Token budget breakdown per agent per phase
- Total token budget per workflow completion
- Cost comparison across model configurations (all-Opus vs mixed vs all-Sonnet)

### 5. Token Budget Breakdown
- Context allocation per agent
- Phase-by-phase token consumption
- Parallel vs sequential token math (parallel phases consume tokens simultaneously but save wall-clock time)
- Buffer allocation (recommended 15-20% overhead)

### 6. Parallel Execution Strategies
- Which phases can run in parallel
- Which phases MUST be sequential (dependency-gated)
- Resource contention management (file locks, shared state)
- How to degrade gracefully to sequential mode under budget constraints

### 7. Success Metrics
- How to measure team effectiveness
- Quality metrics (accuracy, completeness, style adherence)
- Efficiency metrics (tokens per output unit, wall-clock time)
- Cost metrics (actual vs projected spend)

---

## Required ORCHESTRATION.md Per Team

Every team MUST include an ORCHESTRATION.md covering:

### Execution Modes

**Sequential Mode (Budget-Conscious)**
- Cost: $10-30
- Duration: 1-2 hours
- One agent at a time, user manages handoffs
- Best for: Learning, small tasks, tight budgets

**Hybrid Mode (Default -- Recommended)**
- Cost: $30-100
- Duration: 30-60 min
- Parallel where beneficial, sequential where needed
- Best for: Most production use cases

**Parallel Swarm Mode (Software Factory)**
- Cost: $100-500
- Duration: 15-30 min
- All agents active, scenario-based convergence
- Best for: Rapid iteration, time-critical work

### Phase Breakdowns with User Prompt Points

Each phase must specify:
- Duration estimate
- Active agents
- Deliverables produced
- User prompt template at phase boundary

User prompt template format:
```
[Phase Name] complete.
- Deliverables: [list]
- Cost: $X.XX
- Quality: [metrics]

Next phase: [description]
- Estimated cost: $Y.YY
- Estimated duration: Zh

Proceed? (yes/no/review)
```

### Git Branch-Per-Agent Strategy

```
main
├── agent/coordinator/setup
├── agent/[specialist-a]/[task]
├── agent/[specialist-b]/[task]
└── agent/test/scenarios
```

Rules:
- Each agent works on a dedicated branch
- Push every 10-15 minutes
- Check file locks before editing shared files
- Update status every 5 minutes
- Coordinator merges when phase complete and tests pass

### Communication Protocol

Every agent MUST:
- Update status every 5 min via `python utilities/status-updater.py`
- Post to `shared-state/communication.md` when blocked
- Check for messages addressed to them
- Acquire file locks before editing shared files

Message format:
```
### [HH:MM] From-Agent -> To-Agent
Message (1-2 lines max)
Context: [file/link]
Priority: High|Medium|Low
```

### Scenario-Based Validation (Software Factory Pattern)

Scenarios live in `scenarios/` as holdout sets:
- Test Engineer writes scenarios FIRST
- Implementation agents DO NOT see scenarios during coding
- Prevents "teaching to the test"

Convergence criteria:
```yaml
phase_complete_when:
  - scenario_satisfaction >= 0.90
  - code_review_approved == true
  - all_tests_pass == true
  - performance_acceptable == true
```

If criteria not met: Coordinator spawns focused agent or prompts user.

### Autonomous vs User-Prompted Decision Criteria

**Coordinator CAN decide autonomously:**
- Retry flaky tests (<5 failures)
- Reallocate work (agent blocked >15 min)
- Refresh file locks
- Prune communication log
- Merge branches (when tests pass)
- Cost limit: <$20 per autonomous decision

**Coordinator MUST prompt user before:**
- Starting parallel phase (cost implications)
- Spawning additional agents
- Major architecture changes
- Lowering quality thresholds
- Costs >$50 for single decision
- Skipping phases

Prompt template:
```
I recommend [action] because [reason].
- Cost: $X.XX
- Risk: [low/medium/high]
- Alternative: [other option]

Proceed? (yes/no/alternative)
```

---

## Cross-Team Integration

Teams can chain together for complex workflows:

| Source Team | Output | Target Team | Input |
|------------|--------|------------|-------|
| C-Suite | Product Roadmap (Linear) | Code Implementation | Feature requirements |
| C-Suite | Marketing Plan | Content Creation | Content briefs |
| Research Deep Dive | Market Analysis | C-Suite | Market context |
| Project Planning | Sprint Plan | Code Implementation | Task assignments |
| Research Deep Dive | Product Research | Project Planning | Feature priorities |

---

## Shared Dependencies

All teams depend on these common layer components:

- `common/utilities/file-lock-manager.py` -- Prevents write conflicts
- `common/utilities/status-updater.py` -- Agent status tracking
- `common/utilities/cost-estimator.py` -- Real-time cost tracking
- `common/utilities/token-calculator.py` -- Token budget management
- `shared-state/agent-status.json` -- Real-time agent state
- `shared-state/communication.md` -- Inter-agent messaging
- `shared-state/file-ownership.json` -- File lock registry

---

## Design Principles

1. **Passive context over active retrieval**: AGENTS.md provides 100% availability vs Skills at 56% without explicit prompting (Vercel benchmark).
2. **Progressive disclosure**: Load only what the current phase needs. Do not front-load all agent context.
3. **Cost predictability**: Every phase has a token budget. Users know costs before committing.
4. **Graceful degradation**: Every parallel workflow can fall back to sequential mode under budget constraints.
5. **Scenario-based quality**: Holdout test scenarios prevent "teaching to the test" and ensure genuine quality.
6. **User control at boundaries**: Agents run autonomously within phases, but users approve phase transitions.
7. **Branch isolation**: Each agent works on its own git branch. No direct main commits during execution.
8. **Personality consistency**: Agent personalities are defined once and referenced, not reinvented per session.
