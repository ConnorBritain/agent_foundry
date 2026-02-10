# Architecture Decision Framework Specification

> **STATUS**: STATIC REFERENCE -- Extracted from master prompt. Never modified, only consulted.

## Purpose

Provide a complete decision framework for all architectural choices when building agent workflows. Help users choose between AGENTS.md, Skills, and MCP; decide when to use single agents vs teams; select coordination patterns; and allocate token budgets effectively.

## Output File

`strategies/decision-framework.md`

## Content Structure

### 1. AGENTS.md vs Skills vs MCP Decision Tree

#### Primary Decision Flowchart

```
What type of capability are you adding?

├── Broad knowledge base (framework docs, API references, domain expertise)?
│   └── → AGENTS.md
│       Reason: 100% availability, passive context, horizontal knowledge
│       Budget: ~8KB compressed per knowledge domain
│
├── Specific triggered workflow (task-based action, multi-step process)?
│   └── → Skill (SKILL.md)
│       Reason: Progressive disclosure, on-demand loading, vertical workflow
│       Budget: 50-100 tokens metadata, <5000 tokens body
│       WARNING: 56% non-trigger rate without explicit instructions
│
├── Persistent external tool/API (database, third-party service, system tool)?
│   └── → MCP Server
│       Reason: Persistent connection, tool-based interface, external state
│       Budget: Minimal (tool definitions only)
│
└── Combination of the above?
    └── → Hybrid Approach
        - Framework knowledge in AGENTS.md
        - Task workflows as Skills
        - External integrations as MCP
        Reason: Research shows hybrid is optimal for complex systems
```

#### Key Design Constraints from Research

| Mechanism | Token Cost | Availability | Best For | Limitation |
|-----------|-----------|--------------|----------|------------|
| AGENTS.md | ~8KB compressed | 100% (always loaded) | Horizontal knowledge | Static, no triggered actions |
| Skills | 50-100 tokens (metadata), <5000 tokens (body) | Triggered (79% with explicit instructions, 44% without) | Vertical workflows | 56% non-trigger rate risk |
| MCP | Minimal (tool definitions) | Persistent (server-dependent) | External tools/APIs | Requires server infrastructure |

#### Decision Matrix by Use Case

| Use Case | AGENTS.md | Skills | MCP | Hybrid |
|----------|-----------|--------|-----|--------|
| Framework documentation | Best | - | - | - |
| Code review workflow | - | Best | - | Hybrid with AGENTS.md for standards |
| Jira integration | - | Acceptable | Best | - |
| Test generation | - | Best | - | Hybrid with AGENTS.md for patterns |
| Database queries | - | - | Best | - |
| Domain expertise (healthcare, finance) | Best | - | - | - |
| File search and transform | - | Best | - | - |
| Web research | - | Best | MCP for search API | Hybrid recommended |
| Status reporting | - | Best | MCP for data sources | Hybrid recommended |

#### Skill vs MCP Trade-off Analysis

For capabilities that could be either (e.g., Jira integration):

**Choose Skill when**:
- Workflow is multi-step with decision logic
- Token efficiency matters (Skills load on-demand)
- Portability across harnesses is important
- No persistent connection needed
- Workflow can operate on file-based input/output

**Choose MCP when**:
- Real-time data access required
- Persistent connection to external service needed
- Tool-based interaction pattern (query/response)
- Multiple agents need same external access
- State maintained on external server

**Choose Both (Hybrid) when**:
- Skill defines the workflow, MCP provides the tooling
- Example: Code review skill uses GitHub MCP for PR data
- Example: Status reporter skill uses Linear MCP for ticket data

### 2. Single Agent vs Team Decision Criteria

#### Decision Matrix

| Factor | Single Agent | Multi-Agent Team |
|--------|-------------|-----------------|
| Task complexity | Single domain, linear workflow | Multi-domain, branching workflow |
| Time constraint | Not time-critical | Time-critical (parallelism helps) |
| Quality requirements | Standard | High (multiple review perspectives) |
| Cost sensitivity | High (minimize spend) | Lower (willing to spend for quality/speed) |
| Workflow duration | <30 minutes | >30 minutes |
| Domain expertise needed | 1-2 domains | 3+ domains |
| Review/validation needed | Self-review acceptable | Independent review required |
| Token budget | <100K tokens | 100K-1M+ tokens |

#### Decision Flowchart

```
Is the task multi-domain (requires different expertise areas)?
├── No → Can a single agent complete it in <100K tokens?
│   ├── Yes → SINGLE AGENT
│   └── No → Does it benefit from parallel execution?
│       ├── Yes → TEAM (2-3 agents)
│       └── No → SINGLE AGENT with checkpointing
│
└── Yes → Does quality require independent review?
    ├── Yes → TEAM (minimum: doer + reviewer)
    └── No → Are time constraints tight?
        ├── Yes → TEAM (parallel specialists)
        └── No → SINGLE AGENT (sequential, multiple passes)
```

#### Team Size Guidelines

| Team Size | When to Use | Coordination Overhead | Example |
|-----------|-------------|----------------------|---------|
| 1 agent | Simple tasks, tight budgets | None | Quick script generation |
| 2-3 agents | Review-required workflows | Low (10-15% overhead) | Code + review |
| 4-6 agents | Multi-domain projects | Medium (15-25% overhead) | Full feature implementation |
| 7+ agents | Complex business processes | High (25-40% overhead) | Business-in-a-box |

### 3. Sync vs Async Coordination Patterns

#### Synchronous Coordination
- **Pattern**: Agent A completes, passes output to Agent B
- **Best for**: Sequential workflows where each step depends on previous
- **Token efficiency**: High (no coordination overhead)
- **Latency**: High (total time = sum of all steps)
- **Example**: Draft -> Review -> Revise -> Publish

#### Asynchronous Coordination
- **Pattern**: Agents work in parallel, coordinator merges results
- **Best for**: Independent subtasks that can be merged
- **Token efficiency**: Medium (coordination overhead)
- **Latency**: Low (total time = max single step + merge)
- **Example**: Multiple implementation specialists working on different modules

#### Hybrid Coordination
- **Pattern**: Some phases parallel, some sequential
- **Best for**: Most real-world workflows
- **Token efficiency**: Medium
- **Latency**: Medium
- **Example**: Plan (sequential) -> Implement (parallel) -> Review (sequential) -> Test + Doc (parallel)

#### Coordination Pattern Decision Guide

```
Are subtasks independent (no data dependencies)?
├── Yes → Can they be merged without conflicts?
│   ├── Yes → ASYNC (parallel execution)
│   └── No → ASYNC with conflict resolution protocol
│
└── No → Is the dependency chain linear?
    ├── Yes → SYNC (sequential pipeline)
    └── No → HYBRID (DAG-based execution)
        - Identify independent subgraphs
        - Execute subgraphs in parallel
        - Synchronize at dependency points
```

### 4. Token Budget Allocation Formulas

#### Per-Agent Budget Formula

```
agent_budget = base_context + task_context + coordination_overhead

Where:
  base_context = AGENTS.md size + skill metadata + system prompt
                 (typically 5K-15K tokens)

  task_context = estimated_task_tokens * complexity_factor
                 (complexity_factor: simple=1.0, standard=1.5, complex=2.5)

  coordination_overhead = team_size * 500 tokens per coordination message
                          (for multi-agent teams only)
```

#### Team Budget Formula

```
team_budget = sum(agent_budgets) * overhead_factor

Where:
  overhead_factor:
    - 2-3 agents: 1.15 (15% overhead)
    - 4-6 agents: 1.25 (25% overhead)
    - 7+ agents: 1.40 (40% overhead)
```

#### Phase Budget Allocation

Recommended allocation by workflow phase:

| Phase | % of Total Budget | Rationale |
|-------|------------------|-----------|
| Planning | 10-15% | Critical decisions, lower volume |
| Implementation | 40-50% | Highest volume of work |
| Review/QA | 15-20% | Quality assurance, iteration |
| Documentation | 5-10% | Lower complexity |
| Coordination | 10-15% | Inter-agent communication |
| Buffer | 10% | Retries, unexpected complexity |

### 5. Trade-Off Matrices

#### Speed vs Cost vs Quality Triangle

| Priority | Model Strategy | Team Strategy | Token Strategy |
|----------|---------------|---------------|----------------|
| Speed first | All Opus, parallel | Maximum parallelism | Generous budgets |
| Cost first | Haiku where possible | Minimal agents | Tight budgets, caching |
| Quality first | Opus for critical paths | Dedicated reviewers | Allow iteration budget |
| Balanced | Mixed models by role | Right-sized team | Phased with buffers |

#### Complexity vs Automation Matrix

| Task Complexity | Low Automation Need | High Automation Need |
|----------------|--------------------|--------------------|
| Low | Single agent, Haiku | Skill-based workflow |
| Medium | Single agent, Sonnet | Small team (2-3 agents) |
| High | Single agent, Opus | Full team (4-6 agents) |
| Very High | Multi-session, Opus | Software Factory pattern |

### 6. Real-World Decision Examples

#### Example 1: "Should I use AGENTS.md or a Skill for Next.js knowledge?"

**Analysis**:
- Next.js is horizontal knowledge (broad framework docs)
- Agent needs it constantly, not just for specific tasks
- Vercel eval shows AGENTS.md achieves 100% pass rate
- **Decision**: AGENTS.md with compressed documentation index
- **Implementation**: `common/agents-md/framework-nextjs.md`

#### Example 2: "Single agent or team for a code review?"

**Analysis**:
- Single domain (code quality)
- Benefits from independent perspective (reviewer != author)
- Standard quality requirements
- Time: not critical
- **Decision**: 2 agents (implementer + reviewer) if budget allows, single agent with self-review prompt if not
- **Budget impact**: 2x tokens but measurably higher quality

#### Example 3: "MCP or Skill for Jira integration?"

**Analysis**:
- Jira requires persistent API connection
- Multiple agents may need ticket data
- Workflow involves both reading and writing tickets
- Real-time data freshness matters
- **Decision**: MCP server for Jira API access + Skill for workflow logic (hybrid)
- **Implementation**: MCP for CRUD operations, Skill for "create sprint from requirements" workflow

#### Example 4: "How many agents for a business plan?"

**Analysis**:
- Multi-domain: finance, marketing, product, operations, legal, sales
- Benefits from diverse perspectives (CFO challenges CEO assumptions)
- Quality requires cross-functional review
- High value output justifies higher cost
- **Decision**: 7-agent team (Business-in-a-Box template)
- **Budget**: ~700K tokens, justified by output value

#### Example 5: "Sync or async for content creation?"

**Analysis**:
- Some phases independent (research || vision setting)
- Some phases sequential (draft must precede review)
- Humanizer and Critic can work in parallel on draft
- Fact-checker sequential after content changes
- **Decision**: Hybrid coordination
- **Pattern**: Phase 1 parallel -> Phase 2 sequential -> Phase 3 parallel -> Phase 4 sequential -> Phase 5 parallel

## Writing Guidelines

- Use flowcharts and decision trees liberally
- Include "wrong choice" examples (what happens if you pick incorrectly)
- Provide concrete token counts and cost estimates
- Reference research findings (Vercel eval, agentskills.io spec)
- Include copy-paste decision templates users can fill in

## Dependencies

- Research data on AGENTS.md vs Skills effectiveness
- Token pricing for cost calculations
- Team template specifications for real-world examples

## Cross-References

- **Strategies Layer**: `specs/03-strategies-layer/SPEC.md`
- **Common Layer**: `specs/01-common-layer/SPEC.md` (AGENTS.md, Skills, and MCP building blocks)
- **Teams Layer**: `specs/02-teams-layer/SPEC.md` (team architecture decisions)
- **Model Selection**: `specs/03-strategies-layer/guides/model-selection/SPEC.md` (model choices)
- **Optimization Guide**: `specs/03-strategies-layer/guides/optimization/SPEC.md` (token budget optimization)
- **Research Foundation**:
  - Vercel AGENTS.md eval study: https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals
  - Agent Skills Specification: https://agentskills.io/specification
