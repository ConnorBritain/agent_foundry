# Sforza v1: The Agent Swarm Harness

## Context

Three inputs converge to define what Sforza should become:

1. **The Conductor decomp** (0.91 confidence, 242 entities) — reveals the proven architecture for managing parallel AI agents: bidirectional communication, git checkpointing, session reuse, per-session locks, cost transparency, multi-channel notifications. These are engineering patterns to steal.

2. **The market signal** ($285B SaaS crash + OpenClaw's 160K developers) — reveals that per-seat pricing is dying, people want agents that DO things (not chatbots), the 70/30 human-AI split is the product requirement, and "the company that figures out capability + control owns the next platform."

3. **The money model** (Hormozi) — reveals how to structure offers so one customer pays for two more in 30 days, and why you build one stage at a time: Attraction → Upsell → Downsell → Continuity. "Simple scales, fancy fails."

**The strategic reframe**: Sforza is NOT "an AI business builder for solo founders." That's gimmicky. Sforza is a **general-purpose agent swarm orchestrator** — a platform primitive — that ships with **templates** adapted to many use cases. The C-Suite is a template, not the brand.

---

## Part 1: What Sforza Actually Is

### The Core Primitive

Sforza's core loop is use-case agnostic:

```
Human has a goal → Orchestrator breaks it into work → Agent teams execute →
Human reviews/decides (70/30 split) → Deliverables produced → Next cycle
```

This loop works for anyone with a complex goal that benefits from coordinated agent work. The platform doesn't know or care if the agents are writing a business plan, planning a wedding, or running a research study.

### The Monday.com / Notion Analogy

| Platform | Core Primitive | Templates Make It Feel Like... |
|----------|---------------|-------------------------------|
| Monday | Board + automations | CRM, sprint tracker, HR pipeline |
| Notion | Page + database | Wiki, task manager, journal |
| **Sforza** | **Agent team + orchestrator** | **Business builder, research lab, campaign planner, personal assistant** |

### The Avatar Spectrum

The platform serves a spectrum, not a single persona:

| User | Use Case | Template | Budget Tolerance |
|------|----------|----------|-----------------|
| Solo founder | Build a SaaS from idea | Business Builder | $100-500/project |
| Agency operator | Client deliverables at scale | Campaign Planner | $50-200/client |
| Key employee | First-90-days ramp-up plan | Onboarding Playbook | $50-100 one-time |
| Researcher | Literature review + synthesis | Research Deep Dive | $50-150/study |
| Parent/planner | Wedding, move, renovation | Event Coordinator | $20-50 one-time |
| Content creator | Multi-platform content calendar | Content Engine | $100/month ongoing |

**Primary avatar for v1**: Solo founder / operator (you). This is who we optimize for first because they have the highest willingness to pay, the most complex use case, and the broadest template needs. But the architecture must never assume this is the only user.

### What Makes This Not Gimmicky

The C-Suite metaphor is gimmicky because it cosplays as something it isn't. An AI agent calling itself "CFO" doesn't make it a CFO. What makes Sforza real:

1. **It does work, not chat.** (OpenClaw's #1 finding: people want digital employees, not chatbots)
2. **It coordinates multiple agents.** (No other consumer tool does this — Conductor runs parallel agents but they don't coordinate)
3. **It keeps humans in the loop at decision points.** (The 70/30 split — agents work, humans decide)
4. **It tracks cost honestly.** (You always know what you're spending)
5. **It ships with templates that actually work.** (Not "prompt library" gimmicks — real multi-agent workflows with defined deliverables)

Templates have roles, not titles. Not "CFO" — "Financial Analyst Agent." Not "CEO" — "Strategy Coordinator." The work is the same, the framing is honest.

---

## Part 2: The Architecture

### What Changes from Today's Sforza

Today's Sforza has the right bones. The refactor adds three things:

1. **Template system** — Make teams declarative configs, not hardcoded directories
2. **Interactive agent loop** — Bidirectional communication (from Conductor)
3. **Dashboard** — The product surface that makes it real

### Template Architecture (Declarative YAML)

Templates become the growth engine. Instead of 8 hardcoded team directories, templates are YAML configs that define:

```yaml
# templates/business-builder.yaml
name: Business Builder
description: Go from idea to deployed business
avatar: solo-founder  # helps Orchestrator adapt questions
estimated_cost: $150-400
estimated_duration: 3-6 hours

phases:
  - name: Strategy
    teams:
      - strategy-team
    approval_gate: true  # human must approve before next phase

  - name: Build
    teams:
      - development-team
      - content-team
    parallel: true
    depends_on: [Strategy]

  - name: Launch
    teams:
      - marketing-team
    depends_on: [Build]

teams:
  strategy-team:
    agents:
      - role: strategy-coordinator
        model: opus
        personality: common/personalities/analytical-strategist.md
        tools: [web-search, document-write]
      - role: market-researcher
        model: sonnet
        personality: common/personalities/thorough-researcher.md
        tools: [web-search]
      - role: financial-modeler
        model: sonnet
        tools: [spreadsheet, document-write]
    deliverables:
      - business-plan.md
      - financial-model.xlsx
      - competitive-analysis.md
    constraints:
      budget: $50
      require_approval_for: [final-deliverables]

  development-team:
    # ... similar structure
```

**Why YAML**: Anyone can create a template. Community templates. Premium templates. Custom templates a user builds for their own workflow. This is the Monday.com "template gallery" equivalent.

**Migration path**: Convert existing `teams/` directories into YAML configs. The agent markdown files, personalities, and utilities stay as-is — they're referenced by templates, not replaced.

### The Interactive Agent Loop (From Conductor)

Six patterns stolen from Conductor, adapted for Sforza's multi-team model:

| Pattern | Conductor | Sforza Adaptation |
|---------|-----------|-------------------|
| Bidirectional comms | Agent calls back to frontend via JSON-RPC | Agent sends decision to dashboard via WebSocket |
| Plan mode / approval | Per-session approval gate | Per-phase approval gate (template-defined) |
| Session reuse | Hash settings, reuse if match | Same, per-agent within a team run |
| Message lock | One turn per session at a time | One coordinating turn per team at a time |
| Git checkpointing | Private refs per turn | Private refs per team per turn |
| Cost tracking | Per-session, optional display | Per-agent → per-team → per-project, always visible |

The critical new capability: **the Decision Queue**. This is Sforza's version of the OpenClaw 70/30 split. Agents work autonomously within their constraints. When they need a human decision, they surface it as a structured request with options. The human clicks a button. The agent continues.

```
The Decision Queue is the product.
Everything else is infrastructure that makes the Decision Queue possible.
```

### The Dashboard

Four views, in priority order:

**1. Home / Mission Control**
- Active projects with progress, cost burn, phase status
- Decision Queue badge: "3 decisions waiting"
- One-click to start new project from template gallery
- This is the screen you see every time you open Sforza

**2. Decision Queue** (the killer feature)
- Pending decisions, sorted by urgency (blocking other teams = highest)
- Each decision has: context, agent reasoning, options as buttons
- One-click to approve/reject/answer
- 80% of interactions happen here — no typing required
- Notifications push you here when decisions are pending

**3. Project View**
- Team progress, phase status, dependency graph
- Cost breakdown per team
- Deliverables list with preview/download
- "Peek" into individual agent conversations (streaming)

**4. Template Gallery**
- Browse/search templates by category
- Preview template: phases, teams, estimated cost/time
- "Start Project" button → Orchestrator interview (adapted to template)
- Community templates, premium templates, custom template builder (later)

---

## Part 3: The Money Model (Hormozi Framework, Applied to Software)

### The Core Economics

Sforza is BYOLLM (Bring Your Own LLM). Users bring their own Claude Max ($200/month) or API key. Sforza charges for the orchestrator, templates, and dashboard. This avoids the per-seat trap from the $285B crash.

**The value proposition**: "Your Claude subscription gives you agents. Sforza gives you a team."

Hormozi's cardinal rule: **make enough profit from one customer to get and service at least two more in 30 days.** Every pricing decision below serves that rule.

### The Full Money Model Sequence

Hormozi's framework: Attraction → Upsell → Downsell → Continuity. But: **perfect one offer at a time. Don't launch all four simultaneously.** Start at Stage I, get it reliable, then add.

---

#### Stage I: Attraction Offer — The Decoy

Hormozi's Decoy Offer: advertise a free/cheap thing. When leads engage, present a premium version side-by-side. The free version is the decoy that makes the premium look obvious.

**Free tier (the Decoy)**:
- Open-source orchestrator core
- One project at a time
- One template: Research Brief (low stakes, immediately useful)
- CLI-only interface — no dashboard
- Community templates only

**Pro tier ($25/week — see billing note below)**:
- Unlimited projects, all pro templates
- Dashboard with Decision Queue
- Multi-channel notifications
- Git checkpointing, budget enforcement
- Priority support

The free tier is genuinely useful — not crippled. But the moment you want the Dashboard or Business Builder template, you upgrade. The free tier is the decoy.

**How to present the Decoy** (Hormozi's framing): Don't ask "do you want Pro?" Ask: "Are you here to try an AI tool, or to actually ship something? ...Great. Most people who want results go with Pro because the Decision Queue is where the magic happens. Want me to get you set up?"

**Hormozi's billing insight** (his "highest value per word note"): Bill every 4 weeks, not monthly. There are 13 four-week cycles per year vs. 12 months. Same $25/week price, but $1,300/year vs $1,200/year. **8.3% more revenue for changing a setting.** At 20% margins, this alone adds ~41% to annual profit. Nobody notices or cares — "$25/week" sounds cheaper than "$100/month" anyway.

---

#### Stage I (Alternative): Win Your Money Back

Hormozi's strongest attraction offer for results-based businesses:

- Pay $100 for the first month. If you ship a working MVP using Business Builder within 30 days, get your next month free as store credit.
- **Criteria** (Hormozi says: easy to track, gets results, advertises the business):
  1. Complete all Decision Queue items within 24 hours (easy to track — the system logs it)
  2. All template phases completed (gets results — they actually built the thing)
  3. Post a public review/testimonial with your deliverables (advertises the business)
- **Apply the credit over time** (Hormozi's key insight): Don't give them a free month. Give them $25/week off for 4 weeks, keeping them paying. Or better: "$100 credit toward your next template run" — rolling them into the next project.
- **Make everyone a winner**: Halfway through, regardless of progress, tell them privately: "You started. That's the biggest victory. We'll credit your whole first month toward staying with us." This keeps them as customers regardless.

---

#### Stage II: Upsell Offers

Hormozi: "Your first offer doesn't always make the profit. You make it on the second, third, and fourth offers." Every offer reveals a new problem. Solve it immediately.

**The BAMFAM Upsell (Book A Meeting From A Meeting)**:
When a template run completes, the Orchestrator immediately suggests the next one:
- "Your Research Brief is done. The next step for most people is the Business Builder template — want me to set it up? Your research will carry over as input."
This is Sforza's "Do you want fries with that?" It costs nothing to ask.

**The Rollover Upsell** (Hormozi's life-changing pattern):
Credit previous template spend toward the next, more expensive template:
- "You spent $15 on the Research Brief. I'll credit that toward the Business Builder ($150 value). You're basically $15 ahead already."
- For winback: "You ran a Research Brief 3 months ago. We'll credit that $15 toward any template you run this week." One email, reactivates churned users.

**The Menu Upsell** (Unsell → Prescribe → A/B → Card on File):
The Orchestrator uses this when recommending templates:
1. **Unsell**: "You don't need the full 8-team Business Builder. You've already got your strategy. You just need Web Dev and Marketing."
2. **Prescribe**: "Here's what I'd run: Web Dev first (2 hours, ~$60), then Marketing (1.5 hours, ~$40). The marketing team will pull from your web dev deliverables automatically."
3. **A/B**: "Would you rather start with Web Dev or Marketing first?"
4. **Card on file**: "Want to use the same API key and billing? ...Great."

This builds massive trust. You're telling them what NOT to buy. They love you for it.

**The Anchor Upsell** (show the expensive thing first):
- **Enterprise tier ($200/week)**: Dedicated support, custom template builder, SLA, team collaboration (multiple humans), priority rate-limit queue, audit trail export
- **Pro tier ($25/week)**: Everything a solo operator needs
- Present Enterprise first on the pricing page. Pro looks like a steal by comparison. And some people will actually take Enterprise.

**Premium Templates** ($20-50 one-time):
Domain-expert templates. Community creates and sells. Sforza takes 30% (App Store model). This is both an upsell and a continuity retention engine — new templates = new reasons to stay.

---

#### Stage III: Downsell Offers

Hormozi's rules: Never drop the price for the same thing. Change what they get, or how they pay. "Customers talk about price."

**Feature Downsell** (when someone balks at $25/week):
Don't discount. Remove features:
1. Remove premium templates, keep dashboard: "$15/week — you get the Decision Queue and 3 core templates"
2. Remove dashboard, keep all templates: "$10/week — CLI-only with all templates"
3. The "Minimum Package": "$5/week — just the Research Brief template with CLI"

Hormozi: "Name your cheapest combination 'The Minimum.' It implies they have to get at least that." When presenting: "So nothing more than the minimum package then?" — they say yes because "minimum" feels like the floor, not a choice.

**Payment Plan Downsell** (for annual/large template purchases):
- "It's $960 if you prepay for the year — you save 20%. That's what most people do."
- If no: "Want to just split it? $480 now, $480 in 30 days?"
- If no: "What's the most you can put down today?"
- Align billing with paydays. (Hormozi: this alone recovers 1/3 of declined payments.)

**Trial With Penalty** (for the free-to-Pro conversion):
"Try Pro for 14 days free. Complete at least one template run and answer all Decision Queue items within 24 hours. If you do, the trial is free. If you skip the decisions, the agents stall and you'll be billed $25 for the week."
- This works because: (a) the "penalty" actions are exactly what makes great customers, (b) completing a template run proves the value, (c) card is already on file.
- Hormozi: "Always get a credit card. 'That's just how we've always done it.'"

**Temperature Check** (Hormozi's key tactic):
After two downsells, ask: "On a scale from 1-10, how bad do you want this?" If 8+, keep downselling payment structures. If 7 or below, ask "What would a 10 look like?" — then recombine features to match their actual need.

---

#### Stage IV: Continuity Offers

The $25/week subscription IS the continuity. Strengthen retention with all three of Hormozi's continuity patterns:

**Continuity Bonus** (get them to start):
"Sign up for Pro today and get the Business Builder template free ($50 value). Plus, VIP members get early access to new templates, priority support, and a member title in the community."
- Focus the pitch on the bonus, not the subscription. "Join to get Business Builder free" > "Subscribe for $25/week"
- More bonuses = more sign-ups. Stack them: free template + early access + member badge + onboarding call

**Continuity Discount** (get them to commit):
"Pay $25/week month-to-month. Or commit for a year and keep $20/week for life."
- Apply the discount spread over time, not up front (Hormozi: this keeps them paying)
- Offer a "lifetime discount" at your highest-churn month. If average retention is 4 months, offer the discount at month 3: "You're about to unlock your lifetime rate. One more month and you're locked in at $20/week forever."

**Waived Fee** (get them to stay):
- $100 setup fee for month-to-month. Waived with a 6-month commitment.
- If they cancel early, they pay the fee. "It costs us money to onboard you. If you commit, we cover it. If you leave early, you cover it. Fair enough?"
- Hormozi: make the fee 3-5x the weekly rate. $100 is 4x $25. This is the sweet spot.

**Template unlock cadence** (retention engine):
Each month you stay, unlock one premium template permanently. After 12 months, you own the full library even if you cancel. This is the "title/status" play — "Month 6 member: you've unlocked Campaign Planner, Event Coordinator, and Content Engine."

---

### Unit Economics Target

```
Billing: $25/week (4-week cycles, 13 per year)
Annual revenue per customer: $1,300
Monthly effective: ~$100

CAC: ~$50 (content marketing, open-source community, word of mouth)
30-Day Revenue: $100 (4 weekly payments)
30-Day COGS: ~$5 (infrastructure per user)
30-Day Gross Profit: $95
30-Day Net after CAC: $45
Payback: <30 days ✓

LTV (8-month avg retention): $1,300 × (8/12) = ~$867
LTV:CAC: 17:1 (target >3:1) ✓

With upsells (templates, annual commit):
LTV with one $40 template purchase + annual commit: ~$1,100
LTV:CAC: 22:1 ✓
```

**Hormozi's 30-day rule is met.** One customer's first month covers the cost to acquire two more.

The free tier feeds the funnel. Templates are the retention engine (new templates = new reasons to stay). The Decision Queue is the daily engagement hook. The BAMFAM upsell (Orchestrator suggesting next template) drives template velocity.

### What NOT to do (Hormozi's warnings applied)

- **Don't discount.** If someone wants Pro for less, downsell features — never the same thing for less. "Customers talk about price."
- **Don't launch all four stages at once.** Start with the Decoy Offer. Get it working reliably. Then add upsells. Then downsells. Then continuity mechanics. "Perfect one offer at a time."
- **Don't make the free tier too good.** It should be genuinely useful but create a clear problem: "I finished my Research Brief but now I need Business Builder, and that requires Pro." The free tier creates the problem; Pro solves it.
- **Don't hide pricing.** The $285B crash lesson: transparency is the new moat. Show exactly what agents cost (BYOLLM), what Sforza costs ($25/week), and what each template run costs (estimated in YAML). "Simple scales, fancy fails."

---

## Part 4: What to Build for MVP

### The "Start With Friction" Principle (From OpenClaw)

OpenClaw's data shows: start with high-frequency, low-stakes tasks where the cost of failure is low. Build confidence. Expand scope as trust develops.

For Sforza, this means the MVP should NOT lead with the full Business Builder (high stakes, $150+, 3-6 hours). It should lead with something smaller that proves the Decision Queue works:

**MVP Template: "Research Brief"**
- 3 agents: Researcher, Analyst, Writer
- 1 phase, ~30 minutes, ~$5-15 in API costs
- Deliverable: A well-researched brief on any topic
- 2-3 decisions: "Focus on X or Y angle?", "Academic or practitioner sources?", "How deep on the competitive landscape?"

This is the "email management" equivalent — high frequency, immediately useful, low risk. Once someone trusts Sforza with a $10 research brief, they'll trust it with a $200 business plan.

### MVP Feature Set

In priority order:

1. **Template engine** — Parse YAML templates, resolve agent configs, validate constraints
2. **Orchestrator** — Adaptive interview (3-5 questions based on template), charter generation
3. **Agent execution** — Launch agent teams per template phases, with session locks
4. **Decision Queue** — Bidirectional WS, structured decision requests, button responses
5. **Cost tracking** — 3-level hierarchy, real-time display, budget enforcement
6. **Dashboard** — Home, Decision Queue, Project View (three screens, not four — skip Template Gallery for MVP, use CLI to start projects)
7. **Notifications** — System notifications when decisions are pending

NOT in MVP: Template Gallery UI, community templates, premium template marketplace, git checkpointing (add in v1.1), session forking, analytics view.

### Technical Implementation

**Files to modify (sforza_daemon)**:
- `src/sforza_daemon/orchestrator/engine.py` — Template-driven phase execution, approval gates, budget checks
- `src/sforza_daemon/agents/manager.py` — Session locks, bidirectional callbacks
- `src/sforza_daemon/api/websocket.py` — Bidirectional Decision Queue channel
- `src/sforza_daemon/api/routes.py` — Cost endpoints, decision endpoints
- `src/sforza_daemon/state/models.py` — Template model, Decision model
- `src/sforza_daemon/cost/tracker.py` — Expose 3-level hierarchy via API

**New files to create**:
- `src/sforza_daemon/templates/loader.py` — Parse and validate YAML templates
- `src/sforza_daemon/templates/registry.py` — Template discovery and listing
- `src/sforza_daemon/orchestrator/approval.py` — Decision Queue backend (pending decisions, resolve/reject)
- `src/sforza_daemon/agents/session_lock.py` — Per-team message lock

**Files to modify (sforza)**:
- Convert `teams/*/` directories into YAML template configs
- Keep `common/personalities/`, `common/agents-md/`, `common/utilities/` as shared resources referenced by templates

**Dashboard (packages/dashboard)**:
- 3 views: Home (project list + decision badge), Decision Queue (pending decisions with buttons), Project View (team progress + cost + deliverables)
- WebSocket client for real-time updates
- Minimal but polished — this is the product surface

### Conductor Patterns to Implement

**Must have for MVP**:
1. **Bidirectional agent communication** → Decision Queue (agents surface decisions, dashboard sends responses)
2. **Per-team session locks** → Prevent race conditions in concurrent team execution
3. **Cost tracking exposure** → Real-time 3-level cost display in dashboard
4. **Budget enforcement** → Hard stop + "approve to continue?" when budget exceeded

**Add in v1.1**:
5. **Git checkpointing** → Per-team per-turn checkpoints with private refs
6. **Session reuse** → Hash session config, reuse if unchanged
7. **Multi-channel notifications** → System notifications, sound effects

---

## Part 5: Strategic Positioning

### The $285B Crash Lesson

Per-seat SaaS is dying. The data and accountability underneath it are not. Sforza's positioning:

- **Not per-seat**: You don't pay per agent. You pay for the orchestrator that coordinates them.
- **Not per-outcome**: Too hard to price, too variable. Monthly subscription for the platform.
- **BYOLLM**: Users bring their own Claude. Sforza doesn't intermediate the LLM cost. Total transparency.
- **The "single ringable neck"**: When agents do something wrong, Sforza's checkpointing and audit trail (Chronicle) provide accountability. This is your enterprise edge later.

### The OpenClaw Lesson

People want capability AND control. The 70/30 split is the product requirement:

- **70% agent execution**: Agents work autonomously within template-defined constraints
- **30% human decision**: The Decision Queue surfaces the important choices
- **Approval gates**: Template-defined phase transitions require human sign-off
- **Budget as guardrail**: Cost limits prevent runaway execution
- **Spec quality = outcome quality**: Templates are the "well-written specification" that separates the $4200 car deal from the 500-message spam disaster

### Your Moat (What Nobody Else Has)

1. **Multi-agent coordination**: Conductor runs parallel agents but they don't talk to each other. OpenClaw runs single agents. Sforza coordinates teams with dependency resolution.
2. **Template system**: Anyone can create a template. Community growth engine. Network effects.
3. **The Decision Queue**: The 70/30 interface that makes humans feel like leaders, not babysitters.
4. **BYOLLM transparency**: No hidden API costs. Users see exactly what they spend.

### What to Name It

The C-Suite framing is dead. Possible positioning:

- "Sforza — Your AI team, orchestrated."
- "Sforza — Tell it what you want. It assembles the team."
- "Sforza — Agent teams that do the work. You make the calls."

The word "team" is critical. Not "agents" (too technical), not "employees" (too literal), not "assistants" (too passive). Teams imply coordination, specialization, and a human leader.

---

## Part 6: Verification

### How to test MVP end-to-end

1. **Template loading**: Parse the Research Brief YAML template. Verify agent configs resolve, constraints validate, phases are ordered correctly.

2. **Orchestrator interview**: Start a new project with Research Brief template. Verify the Orchestrator asks 3-5 adaptive questions, generates a charter, presents it for approval.

3. **Decision Queue**: Run Research Brief agents. When an agent surfaces a decision, verify it appears in the dashboard Decision Queue with options as buttons. Click an answer. Verify the agent receives it and continues.

4. **Cost tracking**: Run a full Research Brief project. Verify per-agent, per-team, and per-project costs display in real-time. Verify they match API billing within 5%.

5. **Budget enforcement**: Set a $2 budget on a Research Brief project. Run agents. Verify they hard-stop at $2 and the Decision Queue shows "Budget exceeded — approve additional $X to continue?"

6. **Dashboard flow**: Open dashboard → see Home with project list → start Research Brief → see project in Project View → answer 2 decisions in Decision Queue → view deliverables. Mouse-only except for the initial goal description.

---

## Key References

### Conductor (decompiled, read-only)
- `juba/docs/SFORZA_INTEGRATION_GUIDE.md` — Pattern-by-pattern mapping with code
- `juba/docs/SFORZA_LESSONS.md` — Architectural patterns
- `juba/docs/CONDUCTOR_DECOMP_REPORT.md` — Full technical analysis

### Sforza (to be modified)
- `sforza_daemon/src/sforza_daemon/orchestrator/engine.py` — Phase execution
- `sforza_daemon/src/sforza_daemon/agents/manager.py` — Agent lifecycle
- `sforza_daemon/src/sforza_daemon/api/websocket.py` — WebSocket
- `sforza_daemon/src/sforza_daemon/api/routes.py` — REST API
- `sforza_daemon/src/sforza_daemon/cost/tracker.py` — Cost tracking
- `sforza_daemon/packages/dashboard/` — Next.js dashboard

### Strategy Inputs
- `$285 Billion Crash` — Per-seat pricing death, data + accountability edges survive
- `OpenClaw` — 70/30 split, capability + control, start with friction not ambition
- `$100M Money Models` — Attraction → Upsell → Downsell → Continuity, one stage at a time
