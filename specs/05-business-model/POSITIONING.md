# Sforza Positioning

## What Sforza Is

Sforza is a **general-purpose agent swarm orchestrator**. It coordinates teams of AI agents to accomplish complex, multi-step goals -- with the human making the important decisions.

It is NOT:
- A chatbot
- An "AI business builder"
- A prompt library
- A single-agent tool with a fancy wrapper

It IS:
- A platform primitive (like Monday.com boards or Notion databases, but for agent teams)
- A coordination layer that manages parallel AI agents working toward a shared goal
- A Decision Queue that surfaces the 30% of choices humans should make while agents handle the 70% of execution

## The Core Loop

```
Human has a goal
  -> Orchestrator breaks it into phases and teams
  -> Agent teams execute autonomously within constraints
  -> Decision Queue surfaces choices to the human
  -> Human reviews, approves, redirects (click, not type)
  -> Deliverables produced
  -> Next cycle
```

This loop is use-case agnostic. The platform doesn't know or care whether agents are writing a business plan, planning a wedding, or running a research study. **Templates** make the general engine feel purpose-built.

## The Platform Analogy

| Platform | Core Primitive | Templates Make It Feel Like... |
|----------|---------------|-------------------------------|
| Monday.com | Board + automations | CRM, sprint tracker, HR pipeline |
| Notion | Page + database | Wiki, task manager, journal |
| **Sforza** | **Agent team + orchestrator** | **Business builder, research lab, campaign planner** |

## What Makes This Real (Not Gimmicky)

The old C-Suite framing was gimmicky because it cosplayed as something it isn't. An AI agent calling itself "CFO" doesn't make it a CFO. What makes Sforza real:

1. **It does work, not chat.** People want digital employees, not chatbots. (OpenClaw: 160K developers building agents that DO things)
2. **It coordinates multiple agents.** No other consumer tool does this. Conductor runs parallel agents but they don't coordinate across teams.
3. **It keeps humans in the loop at decision points.** The 70/30 split -- agents work, humans decide. (OpenClaw's #1 finding)
4. **It tracks cost honestly.** You always know what you're spending. Per-agent, per-team, per-project.
5. **It ships with templates that work.** Not "prompt library" gimmicks -- real multi-agent workflows with defined deliverables.

Templates have **roles, not titles**. Not "CFO" -- "Financial Analyst Agent." Not "CEO" -- "Strategy Coordinator." The work is the same, the framing is honest.

## Positioning Statement

> **Sforza** -- Agent teams that do the work. You make the calls.

The word "team" is critical. Not "agents" (too technical), not "employees" (too literal), not "assistants" (too passive). Teams imply coordination, specialization, and a human leader.

## Why BYOLLM

From the $285B SaaS crash: per-seat pricing is dying. Data and accountability survive. Sforza's stance:

- **Not per-seat**: You don't pay per agent. You pay for the orchestrator.
- **Not per-outcome**: Too hard to price, too variable.
- **BYOLLM**: Users bring their own Claude (Max at $200/month or API key). Sforza doesn't intermediate the LLM cost. Total transparency.
- **The value proposition**: "Your Claude subscription gives you agents. Sforza gives you a team."

This avoids the per-seat trap, provides cost transparency (a moat in the post-crash era), and lets users control their own LLM spending.

## What Nobody Else Has (The Moat)

1. **Multi-agent coordination**: Conductor runs parallel agents that don't talk to each other. OpenClaw runs single agents. Sforza coordinates teams with dependency resolution across phases.
2. **Template system**: Anyone can create a template. Community growth engine. Network effects. This is the Monday.com "template gallery" equivalent.
3. **The Decision Queue**: The 70/30 interface that makes humans feel like leaders, not babysitters. One-click decisions, not paragraphs of typing.
4. **BYOLLM transparency**: No hidden API costs. Users see exactly what they spend.

## The Services-First Insight

From the SaaS trap analysis: 99% of solo dev SaaS fails. Services-first is smarter.

> "Services teach you what to build. Services fund your runway."

**Applied to Sforza**: The templates ARE the service layer. Each template is a productized service -- it's not "here's a tool, figure it out." It's "here's a structured workflow that produces specific deliverables." The Research Brief template isn't a tool -- it's a $10 research service that happens to be delivered by AI agents.

This framing matters for pricing: users don't pay for software, they pay for outcomes. The template system lets us test which outcomes people value most before investing in perfecting them.
