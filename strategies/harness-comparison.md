# Agent Harness & Knowledge Delivery Comparison

> Comparing agent harness platforms, knowledge delivery mechanisms (AGENTS.md vs SKILL.md vs MCP), and migration strategies for Agent Foundry teams.

## Overview

Agent Foundry is harness-agnostic by design, and the knowledge you feed agents can take three distinct forms: passive context (AGENTS.md), triggered workflows (SKILL.md), or persistent tool connections (MCP servers). Choosing the right harness determines how agents interact with code. Choosing the right knowledge delivery mechanism determines how reliably agents access the information they need.

This guide covers both decisions. The first half compares harness platforms — Claude Code, Kilo Code, OpenClaw, Cursor, and Windsurf — across capabilities, pricing, and integration depth. The second half compares knowledge delivery mechanisms, anchored in Vercel's eval study showing that AGENTS.md achieves a 100% pass rate versus Skills at 79%, and addresses the critical 56% non-trigger problem for Skills.

## Part 1: Knowledge Delivery — AGENTS.md vs SKILL.md vs MCP

### The Vercel Eval Study

Vercel published an evaluation comparing AGENTS.md (passive context files) against Skills (triggered workflow files) for delivering framework knowledge to coding agents. The results were decisive.

**Source**: [Vercel Blog — AGENTS.md Outperforms Skills in Our Agent Evals](https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals)

**Key findings:**

| Metric | AGENTS.md | SKILL.md (with explicit instructions) | SKILL.md (without explicit instructions) |
|---|---|---|---|
| **Pass rate** | 100% | 79% | ~44% |
| **Availability** | Always loaded (passive context) | Trigger-dependent | Trigger-dependent |
| **Non-trigger rate** | 0% (always present) | 56% (failed to trigger) | 56% |
| **Token cost model** | Fixed (always loaded) | Variable (on-demand) | Variable (on-demand) |

**Critical insight**: Skills failed to trigger in 56% of cases without explicit instructions. Even with explicit instructions telling the agent to use the skill, the pass rate reached only 79%. AGENTS.md, being passively loaded into context, achieved 100% because the agent always had the information available.

### When to Use Each Mechanism

The Vercel study does not mean Skills are useless — it means each mechanism has a distinct purpose.

```
AGENTS.md (Passive Context)
  Purpose: Horizontal knowledge — framework APIs, patterns, conventions
  Availability: 100% (always in context)
  Token cost: Fixed per session (loaded once)
  Best for: Reference material needed across many interactions
  Example: Next.js App Router patterns, TypeScript conventions, Vercel deployment config
  Format: Pipe-delimited compressed index for token efficiency

SKILL.md (Triggered Workflows)
  Purpose: Vertical workflows — specific procedures, step-by-step tasks
  Availability: 44-79% (trigger-dependent)
  Token cost: On-demand (loaded only when triggered)
  Best for: Specific task workflows with clear trigger conditions
  Example: Code review checklist, test generation procedure, deployment workflow
  Format: YAML frontmatter + markdown body per agentskills.io spec

MCP Servers (Persistent Tool Connections)
  Purpose: External tool integration — APIs, databases, services
  Availability: 100% (server-dependent)
  Token cost: Per-call (tool invocation)
  Best for: Real-time data from external systems
  Example: GitHub API access, database queries, Slack notifications
  Format: JSON configuration with tool definitions
```

### Decision Matrix: AGENTS.md vs SKILL.md vs MCP

```
START: What kind of knowledge does the agent need?
  |
  |-- Reference material (APIs, patterns, conventions)?
  |     |
  |     |-- Needed across many interactions?
  |     |     YES --> AGENTS.md (passive context, 100% availability)
  |     |     NO  --> Is there a clear trigger phrase?
  |     |               YES --> SKILL.md (on-demand, saves tokens)
  |     |               NO  --> AGENTS.md (cannot risk non-trigger)
  |
  |-- Step-by-step workflow (deploy, review, test)?
  |     |
  |     |-- Is the trigger reliable (>5 trigger phrases defined)?
  |     |     YES --> SKILL.md (triggered workflow)
  |     |     NO  --> AGENTS.md (embed the workflow as passive context)
  |     |
  |     |-- Does the workflow exceed 5,000 tokens?
  |           YES --> SKILL.md with progressive disclosure (references/)
  |           NO  --> Either works; prefer AGENTS.md for reliability
  |
  |-- Real-time external data (APIs, databases)?
        YES --> MCP Server (persistent connection)
        NO  --> AGENTS.md or SKILL.md (see above)
```

### Format Comparison

**AGENTS.md format** — Compressed, pipe-delimited index optimized for token efficiency:

```markdown
# Next.js 15 AGENTS.md Template
> Category: Framework
> Token Budget: ~8KB compressed (~2000 tokens)

[Next.js 15 Index]|root: ./docs/nextjs
|IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning
|01-routing:{pages.md,layouts.md,loading.md,error.md,route-groups.md}
|02-data-fetching:{server-components.md,server-actions.md,revalidation.md}
|03-caching:{full-route-cache.md,data-cache.md,router-cache.md}
|KEY-CONCEPTS: App Router|Server Components|Server Actions|PPR
|PATTERNS: use-server(action)|use-client(component)|revalidatePath(path)
|AVOID: client-side-fetching-in-server-components|unnecessary-use-client
```

**SKILL.md format** — YAML frontmatter with structured workflow per agentskills.io spec:

```yaml
---
skill_name: "code-review"
version: "1.0.0"
description: "Performs structured code reviews with severity levels"
triggers:
  - "when asked to review code or a pull request"
  - "when asked to check code quality"
  - "when a diff or changeset is presented for feedback"
  - "when asked to find bugs or issues in code"
  - "when asked to assess code for production readiness"
---

# Code Review Skill

## When to Invoke This Skill
[Trigger patterns addressing the 56% non-trigger problem]

## Instructions
[Step-by-step workflow, <500 lines]

## References
[Pointers to references/ directory for on-demand loading]
```

**MCP Server config** — JSON with tool definitions and connection parameters:

```json
{
  "name": "brave-search",
  "command": "npx",
  "args": ["-y", "@anthropic-ai/mcp-server-brave-search"],
  "env": {
    "BRAVE_API_KEY": "${BRAVE_API_KEY}"
  },
  "tools": [
    {
      "name": "brave_web_search",
      "description": "Search the web using Brave Search API"
    }
  ]
}
```

### Addressing the 56% Non-Trigger Problem

If you use Skills, mitigate the trigger reliability issue:

1. **Define 5+ trigger phrases** per skill, covering synonyms and alternate phrasings.
2. **Include explicit negatives** — "Do NOT use this skill when..." prevents false triggers and clarifies scope.
3. **Use action-first descriptions** — "Search codebases for patterns" triggers more reliably than "A tool for finding things."
4. **Add boundary examples** — Edge cases that clarify when the skill applies and when it does not.
5. **Combine with AGENTS.md** — Put critical reference knowledge in AGENTS.md and reserve Skills for complex, multi-step workflows where on-demand loading saves significant tokens.

### Token Budget Tradeoffs

| Strategy | Token Cost | Reliability | Best For |
|---|---|---|---|
| All AGENTS.md | High (always loaded) | 100% availability | Small-medium knowledge sets (<10K tokens total) |
| All SKILL.md | Low (on-demand) | 44-79% availability | Large knowledge sets, tight token budgets |
| Hybrid (recommended) | Medium | High | Most teams — AGENTS.md for core, Skills for procedures |
| MCP only | Per-call | 100% (server-dependent) | External tool integration only |

**Recommended hybrid approach**: Put framework knowledge and conventions in AGENTS.md (always available). Put complex multi-step workflows in SKILL.md (loaded on demand). Connect external tools via MCP servers.

## Part 2: Agent Harness Platform Comparison

### Feature Comparison Table

| Feature | Claude Code | Cursor | Windsurf | Kilo Code | OpenClaw |
|---|---|---|---|---|---|
| **Type** | CLI agent + SDK | IDE (VS Code fork) | IDE (VS Code fork) | VS Code extension | CLI tool |
| **Primary Model** | Claude (native) | Multi-model | Multi-model | Multi-model | Multi-model |
| **AGENTS.md Support** | Native | Partial | Partial | Partial | [RESEARCH NEEDED] |
| **Skills Support** | Native (SKILL.md) | Limited | Limited | [RESEARCH NEEDED] | [RESEARCH NEEDED] |
| **MCP Support** | Native | Plugin | Plugin | [RESEARCH NEEDED] | Limited |
| **Headless Mode** | Yes | No | No | No | Yes |
| **Multi-Agent Coordination** | SDK-native | No | No | No | Limited |
| **Parallel Instances** | Unlimited | Seat-limited | Seat-limited | Seat-limited | Unlimited |
| **CI/CD Compatible** | Yes | No | No | No | Yes |
| **Git Integration** | Native | Native | Native | Native | Native |
| **Context Window Mgmt** | Automatic | Automatic | Automatic | Automatic | Manual |
| **Open Source** | No | No | No | [RESEARCH NEEDED] | Yes |
| **Pricing** | Usage-based (API) | $20/mo + usage | $15/mo + usage | [RESEARCH NEEDED] | Free (BYOK) |

### Claude Code

**Strengths:**
- Native Claude integration with optimized prompting, tool use, and context management.
- Headless operation for CI/CD pipelines and fully automated agent workflows.
- First-class AGENTS.md and SKILL.md support — the knowledge delivery mechanisms described above work natively.
- MCP-native with full Model Context Protocol support for external tool integration.
- SDK access enables programmatic orchestration — this is how Agent Foundry launches and manages agents.
- Unlimited parallel instances with no per-seat licensing constraints.
- Built-in session management with context tracking and checkpoint support.

**Limitations:**
- Claude models only — no access to GPT, Gemini, or other providers.
- No visual IDE — pure terminal experience.
- Usage-based pricing requires budget controls for large-scale runs.

**Best for in Agent Foundry:**
- Orchestrator agents that coordinate other agents via the SDK.
- All automated agents running unattended in headless mode.
- CI/CD pipeline agents for review, testing, and deployment.
- Enterprise deployments requiring audit logging and security controls.

**Configuration:**
```yaml
agents:
  orchestrator:
    harness: claude-code
    model: claude-opus-4-6
    flags: ["--allowedTools", "Bash,Read,Write,Edit,Grep,Glob"]
    session:
      timeout: 3600
      checkpoint_interval: 300
```

### Cursor

**Strengths:**
- Full VS Code fork with inline diff views, multi-file editing panels, and visual navigation.
- Multi-model support — switch between Claude, GPT-4, Gemini within the same session.
- Composer mode for multi-file editing with visual diff review before applying changes.
- AI-powered tab completion that learns from codebase patterns.
- Large community with extensive documentation and shared configurations.

**Limitations:**
- GUI-dependent — cannot run headless or in CI/CD pipelines.
- Seat-based licensing limits parallel agent scaling.
- Limited multi-agent coordination capabilities.
- No native SKILL.md or AGENTS.md support (files are read as plain context).

**Best for in Agent Foundry:**
- Human-in-the-loop roles where output needs visual review before proceeding.
- Frontend development where visual diff and preview capabilities add value.
- Pair programming sessions where a human works alongside an agent in real time.

### Windsurf

**Strengths:**
- Cascade flow for multi-step task execution with automatic context gathering.
- Deep codebase indexing for relevant context retrieval across the entire project.
- Competitive pricing compared to Cursor.
- Multi-model support for Claude, GPT-4, and other providers.

**Limitations:**
- GUI-only — no headless or CLI mode.
- Smaller ecosystem and community.
- Limited programmatic control for orchestration.
- Cascade can over-gather context, consuming tokens on irrelevant files.

**Best for in Agent Foundry:**
- Exploration agents that need to deeply understand a codebase before making changes.
- Refactoring agents where Cascade's multi-step flow works well for large-scale changes.
- Human-monitored workflows similar to Cursor.

**Note**: [RESEARCH NEEDED] — Windsurf features are evolving rapidly. Verify current capabilities before committing.

### Kilo Code

**Strengths:**
- [RESEARCH NEEDED] — Limited public information available at time of writing.

**Limitations:**
- [RESEARCH NEEDED]

**Note**: Mark this section for quarterly review. If Kilo Code's capabilities become clearer, update with concrete data.

### OpenClaw

**Strengths:**
- Fully open-source with extensible architecture.
- Multi-model support including local models (Ollama, LM Studio), Claude, GPT-4, and any OpenAI-compatible API.
- CLI-native with headless operation support.
- Self-hosted option eliminates subscription costs — you only pay for API usage or local compute.
- Chinese language workflow support.

**Limitations:**
- Smaller ecosystem and less enterprise support compared to Claude Code.
- No native SKILL.md or AGENTS.md support (treated as plain markdown).
- Less sophisticated context management.
- Community-maintained without commercial support guarantees.
- MCP support is limited compared to Claude Code.

**Best for in Agent Foundry:**
- Budget-constrained teams where subscription-free tooling matters.
- Multi-provider workflows requiring different model providers for different agents.
- Open-source requirements where tooling must be fully auditable.
- Teams using local models for privacy or air-gapped environments.

### Cost Model Comparison

Typical monthly costs by usage pattern (as of February 2026):

| Usage Pattern | Claude Code | Cursor | Windsurf | OpenClaw | Notes |
|---|---|---|---|---|---|
| Light (1hr/day, single agent) | $15-30/mo | $20/mo + ~$10 usage | $15/mo + ~$10 usage | $15-30/mo (API only) | Individual developer |
| Medium (4hr/day, 2-3 agents) | $80-150/mo | $20/mo + ~$60 usage | $15/mo + ~$50 usage | $80-150/mo (API only) | Small team |
| Heavy (8hr/day, 5+ agents) | $300-600/mo | N/A (seat limits) | N/A (seat limits) | $300-600/mo (API only) | Production workflow |
| Software Factory (24/7 swarm) | $1,000+/mo | N/A | N/A | $1,000+/mo (API only) | StrongDM-style continuous |

**Cost calculation methodology:**
- Tokens per hour: ~50K input + ~10K output (typical development session)
- Model costs: See [Model Selection Guide](./model-selection-guide.md) for per-model pricing
- Overhead factors: 1.2x for retries, 1.1x for context loading, 1.15x for coordination in multi-agent setups
- Prompt caching: Reduces repeat context costs by 80-90% on cache hits

## Part 3: Harness Selection Decision Tree

```
START: What is your primary use case?
  |
  |-- Multi-agent team workflows (Agent Foundry)?
  |     |
  |     |-- Enterprise compliance or audit requirements?
  |     |     YES --> Claude Code (SDK orchestration, security, audit logging)
  |     |     NO  --> Continue
  |     |
  |     |-- Open-source or custom model requirement?
  |     |     YES --> OpenClaw (open source, multi-model, self-hosted)
  |     |     NO  --> Claude Code (tightest Agent Foundry integration)
  |
  |-- Individual developer productivity?
  |     |
  |     |-- Want an IDE-native experience?
  |     |     YES --> Cursor (best IDE integration, multi-model)
  |     |     NO  --> Claude Code (CLI, headless, full agent capabilities)
  |     |
  |     |-- Budget is primary constraint?
  |           YES --> OpenClaw (free tool, BYOK) or Cursor (subscription)
  |           NO  --> Claude Code (pay-per-use, most capable)
  |
  |-- CI/CD pipeline integration?
  |     YES --> Claude Code (headless, SDK) or OpenClaw (headless, open source)
  |     NO  --> Any harness works
  |
  |-- Research or experimentation with custom models?
        YES --> OpenClaw (multi-model, local models, extensible)
        NO  --> Claude Code (default recommendation)
```

### Quick Selection Matrix

| Scenario | Recommended | Runner-Up | Reason |
|---|---|---|---|
| Production agent teams | Claude Code | - | SDK orchestration, AGENTS.md/SKILL.md native |
| Individual developer, IDE-native | Cursor | Windsurf | Visual tooling, multi-model |
| Open-source, custom models | OpenClaw | - | Free, extensible, self-hosted |
| Enterprise compliance | Claude Code | - | Audit logging, security controls |
| Budget-constrained | OpenClaw | Cursor | No subscription, BYOK pricing |
| Rapid prototyping | Cursor | Claude Code | Fast visual iteration |
| CI/CD automation | Claude Code | OpenClaw | Headless, programmatic control |

## Part 4: Mixing Harnesses in a Team

Agent Foundry supports heterogeneous teams where different agents use different harnesses. This is often the optimal configuration.

```yaml
team:
  name: full-stack-mixed-harness
  agents:
    orchestrator:
      harness: claude-code          # Headless, SDK-managed
      model: claude-opus-4-6
      knowledge: agents-md          # Passive context for coordination patterns
      role: "Coordinate agents, manage task breakdown"

    backend-dev:
      harness: claude-code          # Headless, automated
      model: claude-sonnet-4-5-20250929
      knowledge: agents-md + skills # Framework context + code review skill
      role: "Implement API endpoints and business logic"

    frontend-dev:
      harness: cursor               # Visual IDE for human review
      model: claude-sonnet-4-5-20250929
      knowledge: agents-md          # React/Next.js passive context
      role: "Build UI components with human review"

    test-engineer:
      harness: claude-code          # Headless, high-volume
      model: claude-haiku-4-5-20251001
      knowledge: skills             # Test generation skill (on-demand)
      role: "Write and run test suites"
```

**Why mix?** The orchestrator and backend agents run unattended (Claude Code). The frontend agent benefits from visual review (Cursor). The test agent uses Skills for on-demand test generation workflows. Framework knowledge lives in AGENTS.md for 100% availability where it matters most.

## Part 5: Migration Strategies

### Claude Code to Cursor

| Component | Transfers | Notes |
|---|---|---|
| AGENTS.md files | Yes (as plain markdown) | Cursor reads them as context but lacks native pipe-delimited parsing |
| SKILL.md files | Partially | Cursor has no native trigger system; workflow content is useful as reference |
| MCP configs | Partially | Cursor supports some MCP servers via plugins |
| Orchestration | No | Cursor has no multi-agent coordination; use as single-agent IDE |
| Git workflow | Yes | Both support standard git operations |

**Migration checklist:**
1. Copy AGENTS.md files to the project root or `.cursor/` directory.
2. Convert critical SKILL.md workflows to Cursor rules or instructions.
3. Test MCP server compatibility with Cursor's plugin system.
4. Accept that multi-agent coordination requires running Claude Code alongside Cursor.

### Claude Code to OpenClaw

| Component | Transfers | Notes |
|---|---|---|
| AGENTS.md files | Yes (as plain markdown) | Treated as context files, no compression parsing |
| SKILL.md files | Partially | Workflow content usable, trigger system differs |
| MCP configs | Limited | OpenClaw MCP support is less mature |
| Orchestration | Limited | OpenClaw supports basic multi-agent but less than Claude Code SDK |
| Model configs | Adapted | OpenClaw supports many providers; remap model IDs |

**Migration checklist:**
1. Map Claude model IDs to OpenClaw-compatible model identifiers.
2. Copy AGENTS.md files as-is; they work as plain markdown context.
3. Adapt SKILL.md files to OpenClaw's workflow system.
4. Evaluate which MCP servers have OpenClaw equivalents.
5. Accept reduced orchestration capabilities or build custom coordination.

### Cursor to Claude Code

| Component | Transfers | Notes |
|---|---|---|
| Cursor rules | Convert to AGENTS.md | Reformat as compressed context templates |
| Project context | Convert to AGENTS.md | Structured knowledge becomes passive context |
| IDE-specific config | No | CLI replaces IDE settings |
| Git workflow | Yes | Standard git operations transfer |
| New capabilities | N/A | Gain: Skills, MCP, multi-agent coordination, headless mode |

**Migration checklist:**
1. Extract Cursor rules and convert to AGENTS.md compressed format.
2. Install Claude Code CLI and configure API key.
3. Define SKILL.md files for workflow-specific procedures.
4. Configure MCP servers for external tool access.
5. Set up multi-agent team configuration if needed.

### General Migration Framework

1. **Inventory** current configurations: rules, context files, model settings, tool integrations.
2. **Classify** each component as portable (works everywhere) or harness-specific.
3. **Convert** harness-specific components to the target format.
4. **Test** knowledge delivery reliability in the target harness — verify AGENTS.md availability and SKILL.md trigger rates.
5. **Validate** that output quality is maintained after migration.

## Part 6: Harness-Agnostic Patterns

Design patterns that work across harnesses to maximize portability:

### Portable AGENTS.md

Write AGENTS.md files as standard markdown that any harness can read. The pipe-delimited compression format is a Claude Code optimization — the content is still valid markdown that other harnesses interpret as plain context.

### Skill Abstraction

Write workflows as plain markdown with clear headings and step-by-step instructions. If the target harness supports SKILL.md triggers, add the YAML frontmatter. If not, the content still works as a reference document.

### Configuration Layering

```
base-config.yaml           # Portable: agent roles, knowledge sources, file ownership
  + claude-code-overlay.yaml  # Harness-specific: SDK flags, session management, MCP
  + cursor-overlay.yaml       # Harness-specific: IDE rules, visual review settings
```

### File-Based Coordination

Use shared files (shared-state/, checkpoints, progress notes) for inter-agent coordination rather than harness-specific APIs. This pattern works in any harness and survives migration.

## Recommendations

### For teams starting with Agent Foundry
Start with Claude Code for all agents. It has the tightest integration with Agent Foundry's orchestration layer, native AGENTS.md and SKILL.md support, and the SDK for programmatic control. Swap individual agents to other harnesses later if needed.

### For knowledge delivery
Use the hybrid approach: AGENTS.md for framework knowledge and conventions (100% availability), SKILL.md for complex multi-step workflows (on-demand loading), and MCP for external tool integration. The Vercel study shows passive context beats triggered retrieval for reference material.

### For cost-sensitive projects
Use OpenClaw for high-volume roles and Claude Code for coordination. Put critical knowledge in AGENTS.md (reliable) and use Skills sparingly for large workflows that would otherwise blow the token budget.

### For human-agent collaboration
Run Claude Code for automated agents and Cursor for human-facing interactions. Humans get a visual IDE while agents run headless. Share AGENTS.md files across both harnesses for consistent knowledge delivery.

### For enterprise deployments
Standardize on Claude Code for all orchestration and automated agents. The SDK provides the control plane needed for security, auditing, and compliance. Use AGENTS.md for all critical knowledge delivery — the 100% availability guarantee matters in production.

## Related Resources

- [Model Selection Guide](./model-selection-guide.md) -- Choosing the right model for each agent role
- [Decision Framework](./decision-framework.md) -- Team composition and execution strategy decisions
- [Deployment Guide](./deployment-guide.md) -- Environment setup across deployment tiers
- [Optimization Guide](./optimization-guide.md) -- Token budgeting and cost reduction techniques
- [Quality Assurance](./quality-assurance.md) -- Multi-agent review and validation patterns
