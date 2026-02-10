# Agent Foundry User Guide

> **From idea to deployed business -- all agents.**

This guide walks you through everything you need to know to use Agent Foundry, an open-source system for building businesses with coordinated AI agent teams. Whether you are launching a SaaS startup, a content business, or an internal tool, Agent Foundry provides the teams to get it done.

---

## Table of Contents

1. [Getting Started](#1-getting-started)
2. [Understanding Your Project Charter](#2-understanding-your-project-charter)
3. [Running Teams](#3-running-teams)
4. [The 8 Teams](#4-the-8-teams)
5. [Monitoring Progress](#5-monitoring-progress)
6. [Working with Outputs](#6-working-with-outputs)
7. [Multi-Team Projects](#7-multi-team-projects)
8. [Session Management](#8-session-management)
9. [Customization](#9-customization)
10. [Troubleshooting](#10-troubleshooting)
11. [Complete Example: Sarah's SaaS Startup](#complete-example-sarahs-saas-startup)

---

## 1. Getting Started

### Prerequisites

Before you begin, make sure you have:

- **Claude Max Plan** ($200/month recommended) or an **Anthropic API key** with sufficient credits
- **Python 3** (3.10 or later recommended)
- **Git** (2.30 or later)
- **Claude Code CLI** installed ([installation docs](https://docs.anthropic.com/en/docs/claude-code))

The Claude Max Plan at $200/month provides the best experience for running multiple agent teams. The $100/month tier works but you will hit rate limits more frequently. API-only usage gives you the most control over spending but requires careful budget management.

### Step 1: Clone the Repository

```bash
git clone https://github.com/ConnorBritain/agent_foundry.git
cd agent-foundry
```

### Step 2: Run the Initialization Script

```bash
./initialize.sh
```

Or, if you already have a project name in mind:

```bash
./initialize.sh my-saas-startup
```

The script will:

1. **Check your dependencies** -- verifies that Claude Code CLI, Python 3, and Git are installed.
2. **Prompt for a project name** -- if you did not pass one as an argument. Use lowercase with hyphens (e.g., `fitness-tracker-app`).
3. **Create your project workspace** at `projects/<your-project-slug>/` with the full directory structure.
4. **Launch the Orchestrator Agent** in Claude Code.

### Step 3: The Orchestrator Interview

Once the Orchestrator launches, it will conduct a 10-15 minute interview to understand your project. Be prepared to answer questions about:

- **What you are building** -- describe your product or business idea in plain language.
- **Your current stage** -- just an idea, validated concept, MVP already built, or early traction.
- **Your primary goal for the next 30 days** -- what does success look like?
- **Your Claude plan and budget** -- which plan you are on and how much you are willing to spend.
- **Your preferred execution mode** -- sequential (one team at a time), parallel (2-3 teams), or fully orchestrated.
- **Your involvement level** -- high-touch (approve everything), balanced (approve major decisions), or autonomous (set goals and check in weekly).

After the interview, the Orchestrator generates your `PROJECT_CHARTER.md` -- the master plan that drives all team activity.

---

## 2. Understanding Your Project Charter

### What PROJECT_CHARTER.md Contains

The Project Charter is the single source of truth for your entire project. It lives at `projects/<your-project>/PROJECT_CHARTER.md` and contains:

| Section | What It Defines |
|---------|----------------|
| Vision | Your business description and value proposition |
| Current Stage | Where you are today (idea, validated, MVP, traction) |
| Primary Goal | What you want to achieve in the next 30 days |
| Claude Plan & Budget | Your plan type, rate limit strategy, and spending limits |
| Execution Strategy | Sequential, parallel, or orchestrated mode |
| Involvement Level | How hands-on you want to be |
| Active Teams (Phased) | Which teams run in Phase 1, Phase 2, Phase 3 |
| Success Metrics | Milestones with target dates |
| Communication Protocol | How and when you receive updates |
| Workspace Structure | Where everything lives |

### How to Customize It

The charter is a living document. You can edit it at any time:

```bash
# Open in your editor
code projects/my-startup/PROJECT_CHARTER.md
# or
vim projects/my-startup/PROJECT_CHARTER.md
```

Common customizations:

- **Reorder team phases** -- move a team from Phase 2 to Phase 1 if priorities change.
- **Adjust success criteria** -- refine what "done" means for each phase.
- **Change involvement level** -- switch from autonomous to balanced if you want more control.
- **Add or remove teams** -- not every project needs all 8 teams.

### Budget and Plan Configuration

The budget section of your charter controls spending guardrails:

```markdown
## Claude Plan & Budget

- **Plan**: Max 200 ($200/mo)
- **Rate limit strategy**: Hard stop at plan limits
- **Per-session budget**: $50
- **Weekly budget**: $150
- **Monthly budget**: $500
- **Alert threshold**: 80% of weekly budget
```

**Plan comparison for Agent Foundry usage:**

| Plan | Monthly Cost | Best For | Limitation |
|------|-------------|----------|------------|
| Pro ($20/mo) | $20 | Exploring one team at a time | Strict rate limits; expect frequent pauses |
| Max 100 ($100/mo) | $100 | Running 1-2 teams per week | Moderate rate limits; plan sessions carefully |
| Max 200 ($200/mo) | $200 | Full multi-team projects | Best throughput; can run parallel teams |
| API Direct | Variable | Maximum control and scale | No rate limits, but pay per token |

---

## 3. Running Teams

Agent Foundry supports three execution modes. Choose the one that matches your budget and timeline.

### Serial Execution (Budget-Conscious)

Run one team at a time. This is the most economical approach and gives you the most control.

**How it works:**

1. Launch one team using its launch script:

   ```bash
   ./launch-scripts/start-c-suite.sh projects/my-startup
   ```

2. Wait for the team to complete. Monitor progress in your terminal or with the dashboard.

3. Review the team's outputs in `shared-workspace/artifacts/<team>/`.

4. When satisfied, launch the next team:

   ```bash
   ./launch-scripts/start-web-app-development.sh projects/my-startup
   ```

**Available launch scripts:**

```
./launch-scripts/start-c-suite.sh <project-dir>
./launch-scripts/start-web-app-development.sh <project-dir>
./launch-scripts/start-sales-marketing.sh <project-dir>
./launch-scripts/start-recruitment-hr.sh <project-dir>
./launch-scripts/start-content-creation.sh <project-dir>
./launch-scripts/start-code-implementation.sh <project-dir>
./launch-scripts/start-project-planning.sh <project-dir>
./launch-scripts/start-research-deep-dive.sh <project-dir>
```

Each launch script passes your project directory to the team so agents know where to find the charter, read outputs from other teams, and write their own deliverables.

**Advantages:** Lowest cost, easiest to follow, review between each team.
**Disadvantages:** Slowest total wall-clock time.

### Parallel Execution (Time-Optimized)

Run 2-3 teams simultaneously in separate terminal windows or tabs.

**How it works:**

1. Open two or three terminal windows.

2. In Terminal 1:

   ```bash
   ./launch-scripts/start-c-suite.sh projects/my-startup
   ```

3. In Terminal 2:

   ```bash
   ./launch-scripts/start-research-deep-dive.sh projects/my-startup
   ```

4. In Terminal 3 (optional):

   ```bash
   ./launch-scripts/start-content-creation.sh projects/my-startup
   ```

5. Teams coordinate automatically through the shared workspace. When the C-Suite team publishes a brand positioning document, the Content Creation team can pick it up without any manual intervention.

**How teams coordinate via shared-workspace/:**

- Teams write deliverables to `shared-workspace/artifacts/<team>/`.
- Teams post cross-team messages to `shared-workspace/cross-team-communication.md`.
- Dependencies are tracked in `shared-workspace/dependency-tracker.md`.
- Real-time status is recorded in `shared-workspace/project-status.json`.

**Tips for parallel execution:**

- Start independent teams first (C-Suite + Research can always run in parallel).
- Avoid launching teams that have hard dependencies on unfinished work (do not start Sales & Marketing before C-Suite has produced the go-to-market strategy).
- Monitor `dependency-tracker.md` for blocked dependencies.
- Keep one terminal free for monitoring with `project-status-dashboard.py`.

**Advantages:** 2-3x faster than serial. Still manageable.
**Disadvantages:** Higher burst cost, requires more attention.

### Orchestrated Mode (Premium)

Full parallel execution with automated monitoring and coordination. Best suited for the Max 200 plan or API usage.

**How it works:**

1. Launch the control plane:

   ```bash
   python3 common/utilities/project-status-dashboard.py --project projects/my-startup
   ```

2. The control plane reads your Project Charter and launches teams according to your phased plan.

3. It monitors `project-status.json` for phase transitions, resolves dependencies, and alerts you when attention is needed.

4. You review outputs and approve phase transitions as defined by your involvement level.

**Advantages:** Fastest possible execution, hands-off coordination.
**Disadvantages:** Highest cost, requires Max 200 plan or API credits.

---

## 4. The 8 Teams

Each team is a self-contained group of specialized AI agents that work together on a domain. Here is what each team does, what it produces, and when to use it.

### C-Suite (~$150-200, 3-4 hours)

A board of AI executives -- CEO, CFO, CMO, CTO, COO, VP Sales, and General Counsel -- that collaboratively develop your business strategy.

**What it produces:**
- Business model canvas and strategy document
- Financial projections and unit economics
- Investor pitch deck
- Organizational design and hiring roadmap
- Go-to-market strategy
- Legal and compliance checklist

**When to use it:** At the start of every new venture. The C-Suite team's outputs feed into nearly every other team. If you only run one team, make it this one.

**Agents:** 7

---

### Web App Development (~$105, 2.75 hours)

Builds and deploys full-stack SaaS applications using Next.js, Supabase, Vercel, and Stripe.

**What it produces:**
- Marketing/landing site
- Functional web application with authentication
- Database schema and API layer (Supabase)
- Payment integration (Stripe)
- Deployment pipeline (Vercel)
- Technical documentation and API docs

**When to use it:** After the C-Suite team has defined the product vision, or when you have a clear product spec ready to build.

**Agents:** 7

---

### Sales & Marketing (~$80-120, 2-3 hours)

Complete go-to-market execution from brand positioning to pipeline generation.

**What it produces:**
- Brand positioning and messaging framework
- Demand generation campaigns (email sequences, ad copy, landing pages)
- Sales enablement materials (battle cards, objection handling, scripts)
- Pipeline management playbook
- Customer success onboarding flows
- Growth analytics dashboards

**When to use it:** After C-Suite defines the go-to-market strategy, or in parallel with Web App Development to have marketing materials ready at launch.

**Agents:** 7

---

### Recruitment & HR (~$70-100, 2-2.5 hours)

End-to-end people operations from job design to performance management.

**What it produces:**
- Job descriptions and role definitions
- Interview question banks and evaluation rubrics
- Onboarding checklists and 30-60-90 day plans
- Company culture handbook
- Performance review frameworks
- Compensation and equity guidelines

**When to use it:** When you are ready to hire (typically after your MVP is validated). Also useful for solo founders documenting processes for eventual team growth.

**Agents:** 6

---

### Content Creation (~$60-80, 2 hours)

Research-backed, humanized content at scale with AI pattern removal and brand voice matching.

**What it produces:**
- Blog posts and thought leadership articles
- Social media content calendars and copy
- Email newsletter templates
- Whitepapers and case studies
- Brand voice guide
- SEO-optimized content with fact-checking

**When to use it:** In parallel with or after Sales & Marketing. Pairs well with the Research team for data-backed content.

**Agents:** 7

---

### Code Implementation (~$40-60, 1 hour)

Feature development from requirements to deployment with code review, testing, and documentation.

**What it produces:**
- Implemented features with full test coverage
- Code review reports
- Technical documentation
- Deployment scripts
- Performance benchmarks

**When to use it:** After Web App Development has built the initial application. Use this team for ongoing feature work, bug fixes, and iterations.

**Agents:** 6

---

### Project Planning (~$50-80, 1.5 hours)

Transforms goals into actionable plans across multiple frameworks (SAFe, Agile, Scrum). Integrates with Linear, Google Calendar, and Jira.

**What it produces:**
- Multi-team project roadmaps
- Sprint plans and backlog prioritization
- Dependency maps and critical path analysis
- Resource allocation plans
- Risk registers
- Integration with project management tools

**When to use it:** Before launching a multi-team effort, or when you need to coordinate complex work across several teams and timelines.

**Agents:** 7

---

### Research (~$80-120, 2-3 hours)

Comprehensive research with configurable modes: academic, market, competitive, and product.

**What it produces:**
- Market size and opportunity analysis (TAM/SAM/SOM)
- Competitive landscape reports
- Academic literature reviews
- Product research and feature comparisons
- Customer persona research
- Technology trend analysis

**When to use it:** At the start of a project (in parallel with C-Suite) or whenever you need deep domain understanding before making decisions.

**Agents:** 4-12 (progressively disclosed based on research depth)

---

### Cost Summary Table

| Team | Estimated Cost | Duration | Agents |
|------|---------------|----------|--------|
| C-Suite | $150-200 | 3-4 hours | 7 |
| Web App Development | ~$105 | 2.75 hours | 7 |
| Sales & Marketing | $80-120 | 2-3 hours | 7 |
| Research | $80-120 | 2-3 hours | 4-12 |
| Recruitment & HR | $70-100 | 2-2.5 hours | 6 |
| Content Creation | $60-80 | 2 hours | 7 |
| Project Planning | $50-80 | 1.5 hours | 7 |
| Code Implementation | $40-60 | 1 hour | 6 |

Cost estimates assume Claude Sonnet 4.5 as the default model. Using Opus 4.6 will cost approximately 5x more. Using Haiku 4.5 will cost approximately 12x less. Run the cost estimator for precise numbers:

```bash
python3 common/utilities/cost-estimator.py teams/c-suite/ --compare-models
```

---

## 5. Monitoring Progress

### Using the Project Status Dashboard

The dashboard gives you a real-time view of all active teams:

```bash
python3 common/utilities/project-status-dashboard.py --project projects/my-startup
```

Output example:

```
============================================================
  My Startup - Project Status
  Initialized: 2026-02-10T14:30:00Z
============================================================

ACTIVE TEAMS
Team                      Status     Phase                     Progress
----------------------------------------------------------------------
c-suite                   [*]        financial-modeling         65%
research-deep-dive        [*]        competitive-analysis       40%
web-app-development       [~]        awaiting-dependencies      0%

DEPENDENCIES
From                 To                   Need                           Status
--------------------------------------------------------------------------------
web-app-development  c-suite              Product requirements doc       Pending
content-creation     c-suite              Brand guidelines               Pending
```

### Reading project-status.json

For programmatic access, read the status file directly:

```bash
cat projects/my-startup/shared-workspace/project-status.json
```

The JSON structure contains:

- `project_name` -- your project's display name.
- `active_teams` -- array of currently running teams with their status, phase, progress percentage, and last update timestamp.
- `completed_teams` -- array of teams that have finished.
- `dependencies` -- inter-team dependencies with from/to/status fields.
- `budget` -- spending data (daily, weekly, monthly limits and actuals).
- `phase` -- overall project phase (initialization, execution, review).

### Understanding cross-team-communication.md

This file is the message board where teams coordinate. Each message includes:

- **Timestamp and direction** (e.g., `C-Suite -> Web App Development`)
- **Message content** (what the team needs or is sharing)
- **Priority** (High, Medium, Low)

Check it periodically for inter-team requests:

```bash
cat projects/my-startup/shared-workspace/cross-team-communication.md
```

### Budget Tracking

Use the cost estimator to project costs before launching a team:

```bash
# Estimate cost for a specific team
python3 common/utilities/cost-estimator.py teams/web-app-development/

# Compare costs across models
python3 common/utilities/cost-estimator.py teams/c-suite/ --compare-models

# Run sensitivity analysis (+/- 20%)
python3 common/utilities/cost-estimator.py teams/research-deep-dive/ --sensitivity

# Get results as JSON for scripting
python3 common/utilities/cost-estimator.py teams/sales-marketing/ --json
```

Your charter's budget section sets alert thresholds. The system will notify you when spending reaches 80% of your weekly budget.

---

## 6. Working with Outputs

### Where Deliverables Go

Every team writes its outputs to a dedicated directory inside the shared workspace:

```
projects/my-startup/shared-workspace/artifacts/
├── c-suite/                  # Strategy docs, financials, pitch decks
├── web-app-development/      # Deployed app code, API docs, configs
├── sales-marketing/          # Campaign assets, sales materials
├── recruitment-hr/           # Job descriptions, handbooks, processes
├── content-creation/         # Blog posts, social copy, brand guides
├── code-implementation/      # Feature code, test reports, docs
├── project-planning/         # Roadmaps, sprint plans, risk registers
└── research-deep-dive/       # Research reports, market analyses
```

### How to Review and Iterate

1. **Browse artifacts** after a team completes:

   ```bash
   ls projects/my-startup/shared-workspace/artifacts/c-suite/
   ```

2. **Read key deliverables** and assess quality.

3. **Request iterations** by relaunching the team with specific feedback. Add a note to your charter or pass instructions through the launch script:

   ```bash
   # Relaunch with specific instructions
   ./launch-scripts/start-c-suite.sh projects/my-startup
   # Then in the Claude session, provide feedback:
   # "Revise the financial projections to use a more conservative 5% monthly growth rate"
   ```

4. **Approve and move on** when the outputs meet your success criteria. Update `project-status.json` to mark the team as completed (this happens automatically in orchestrated mode).

### Exporting and Sharing

Artifacts are standard files (Markdown, JSON, code files) that you can:

- **Copy to another repository** for version control.
- **Share via cloud storage** (Google Drive, Dropbox, etc.).
- **Publish directly** -- blog posts are ready-to-publish Markdown; pitch decks can be imported into presentation tools.
- **Feed into other tools** -- JSON outputs can be imported into project management platforms.

---

## 7. Multi-Team Projects

### How Teams Coordinate

Teams in Agent Foundry coordinate through four shared mechanisms:

1. **Artifact sharing** -- Teams read each other's outputs from `shared-workspace/artifacts/<team>/`. When the C-Suite team publishes brand guidelines, the Content Creation team automatically picks them up.

2. **Cross-team communication** -- Teams post messages to `shared-workspace/cross-team-communication.md` when they need something from another team or want to share a decision.

3. **Dependency tracking** -- Hard dependencies are recorded in `shared-workspace/dependency-tracker.md` with status (Pending, In Progress, Resolved).

4. **Status broadcasting** -- Every team updates `shared-workspace/project-status.json` at phase transitions so all other teams (and you) can see the current state.

### Dependencies Between Teams

Some teams depend on outputs from others. Here are the most common dependencies:

| Team | Typically Depends On | What It Needs |
|------|---------------------|---------------|
| Web App Development | C-Suite | Product requirements, tech stack decisions |
| Sales & Marketing | C-Suite | Go-to-market strategy, positioning |
| Content Creation | C-Suite, Sales & Marketing | Brand guidelines, messaging framework |
| Recruitment & HR | C-Suite | Org chart, hiring plan, budget |
| Code Implementation | Web App Development | Existing codebase, architecture |
| Project Planning | C-Suite | Strategic priorities, team roster |
| Research | None (can run independently) | Research questions from any team |
| C-Suite | None (typically runs first) | Your interview answers |

### Typical Project Sequences

**Sequence 1: Full Startup Launch (4-6 weeks)**

```
Week 1:    C-Suite + Research (parallel)
Week 2:    Web App Development + Content Creation (parallel)
Week 3:    Sales & Marketing + Project Planning (parallel)
Week 4:    Code Implementation (iterate on MVP)
Week 5-6:  Recruitment & HR + ongoing iterations
```

**Sequence 2: MVP Sprint (1-2 weeks)**

```
Day 1-2:   C-Suite (focused on product spec only)
Day 3-5:   Web App Development
Day 6-7:   Code Implementation (polish and iterate)
```

**Sequence 3: Go-to-Market Push (2-3 weeks)**

```
Week 1:    Research (market + competitive) + C-Suite (positioning refresh)
Week 2:    Sales & Marketing + Content Creation (parallel)
Week 3:    Iterations and launch
```

### The Shared Workspace Structure

```
projects/my-startup/
├── PROJECT_CHARTER.md                    # Master plan (generated by Orchestrator)
├── shared-workspace/
│   ├── artifacts/                        # Team deliverables
│   │   ├── c-suite/
│   │   ├── web-app-development/
│   │   ├── sales-marketing/
│   │   ├── recruitment-hr/
│   │   ├── content-creation/
│   │   ├── code-implementation/
│   │   ├── project-planning/
│   │   └── research-deep-dive/
│   ├── project-status.json               # Real-time team dashboard
│   ├── cross-team-communication.md       # Inter-team message board
│   ├── dependency-tracker.md             # Blocking dependency tracker
│   └── weekly-summaries/                 # Orchestrator's weekly reports
├── scenarios/                            # Project-specific validation scenarios
└── logs/                                 # Execution logs per team
```

---

## 8. Session Management

### Handling Rate Limits

**Claude Max Plan users:**

The Max plan has usage limits that reset periodically. When you hit a rate limit:

1. The agent session will pause and inform you.
2. Wait for the rate limit window to reset (typically 15-60 minutes depending on your tier).
3. Resume the session -- agents are designed to pick up where they left off.

**Tips to minimize rate limit interruptions:**

- Run teams during off-peak hours when possible.
- On the $100/month Max plan, run one team at a time and space sessions throughout the day.
- On the $200/month Max plan, you can comfortably run 2-3 teams in parallel.
- If you need maximum throughput, consider supplementing with API credits.

**API key users:**

No rate limits (beyond Anthropic's standard API rate limits), but you pay per token. Monitor spending with the cost estimator and set budget alerts in your charter.

### Checkpointing and Resuming

Agent teams naturally checkpoint their progress:

- **Phase transitions** are recorded in `project-status.json`.
- **Completed artifacts** are written to the shared workspace immediately.
- **Dependencies** are tracked and persisted in `dependency-tracker.md`.

To resume after an interruption:

1. Check the status file to see what was completed:

   ```bash
   python3 common/utilities/project-status-dashboard.py --project projects/my-startup
   ```

2. Relaunch the team that was interrupted:

   ```bash
   ./launch-scripts/start-web-app-development.sh projects/my-startup
   ```

3. The team will read the existing artifacts and status, recognize what has already been done, and continue from where it left off.

### What to Do If a Session Ends Unexpectedly

If a Claude Code session terminates unexpectedly (crash, network issue, rate limit):

1. **Do not panic.** All artifacts written to `shared-workspace/artifacts/` are persisted.

2. **Check what was saved:**

   ```bash
   ls -la projects/my-startup/shared-workspace/artifacts/<team>/
   ```

3. **Review the status file** for the last recorded progress:

   ```bash
   cat projects/my-startup/shared-workspace/project-status.json | python3 -m json.tool
   ```

4. **Relaunch the team.** The agents will assess the current state of artifacts and continue:

   ```bash
   ./launch-scripts/start-<team>.sh projects/my-startup
   ```

5. If the team starts from scratch instead of resuming, you can prompt it explicitly: "Review existing artifacts in `shared-workspace/artifacts/<team>/` and continue from where the previous session left off."

---

## 9. Customization

### Modifying Team Templates

Team templates live in the `teams/` directory. Each team has the following structure:

```
teams/<team-name>/
├── README.md              # Team overview
├── TEAM_SPEC.md           # Detailed specification
├── agents/                # Individual agent definitions
│   ├── agent-1/
│   ├── agent-2/
│   └── ...
├── scenarios/             # Validation scenarios
├── examples/              # Example outputs
└── mcp-servers/           # Tool integrations (if any)
```

To modify a team, edit the files in its directory. Changes take effect the next time you launch that team.

### Adding Custom Scenarios

Scenarios define how agents validate their work. Add new scenarios to a team's `scenarios/` directory:

1. Browse existing scenarios for the format:

   ```bash
   ls teams/c-suite/scenarios/
   ```

2. Create a new scenario file following the same structure.

3. Reference it in the team's configuration.

You can also add project-specific scenarios to `projects/<your-project>/scenarios/`.

### Adjusting Agent Prompts

Each agent's behavior is defined by files in its directory under `teams/<team>/agents/<agent>/`. These typically include:

- **AGENTS.md** -- the agent's core knowledge and instructions.
- **SKILL.md** -- specific skills and workflows the agent can execute.

To adjust an agent's behavior:

1. Read the current prompt:

   ```bash
   cat teams/c-suite/agents/<agent-name>/AGENTS.md
   ```

2. Edit the file to modify instructions, add domain knowledge, or change the agent's personality.

3. Test by running the team on a small project first.

Agent personalities are also available as reusable templates in `common/agents-md/` -- you can reference these shared profiles across multiple teams.

### Creating New Teams

To create a new team from scratch:

1. Copy an existing team as a starting point:

   ```bash
   cp -r teams/code-implementation teams/my-custom-team
   ```

2. Edit `README.md` and `TEAM_SPEC.md` to define the new team's purpose.

3. Modify or add agents in the `agents/` subdirectory.

4. Add scenarios for validation.

5. Create a launch script:

   ```bash
   cp launch-scripts/start-code-implementation.sh launch-scripts/start-my-custom-team.sh
   ```

   Edit the script to reference your new team directory.

6. Test the team on a small project before using it in production.

---

## 10. Troubleshooting

### Common Issues and Fixes

**"Claude Code CLI not found" during initialization**

Install Claude Code CLI following the [official docs](https://docs.anthropic.com/en/docs/claude-code). If installed but not found, ensure it is on your PATH:

```bash
which claude
```

**Team launches but does not produce artifacts**

- Verify the project directory path is correct: `ls projects/my-startup/shared-workspace/`.
- Check that `PROJECT_CHARTER.md` exists in the project directory.
- Review logs in `projects/my-startup/logs/` for error messages.

**Teams are not reading each other's outputs**

- Confirm artifacts exist: `ls shared-workspace/artifacts/<producing-team>/`.
- Check `dependency-tracker.md` for unresolved dependencies.
- Ensure all teams are pointed at the same project directory.

**Rate limit errors on Claude Max Plan**

- Wait for the rate limit window to reset (check the error message for timing).
- Switch to serial execution to reduce concurrent usage.
- Consider upgrading from Max 100 to Max 200 for higher limits.
- Supplement with API credits for burst capacity.

**Session ended mid-team with partial outputs**

- Check what was saved in `shared-workspace/artifacts/<team>/`.
- Relaunch the team -- agents are designed to detect and continue from partial work.
- If the agent starts over, explicitly instruct it to review existing artifacts first.

**Cost estimator shows unexpectedly high numbers**

- The estimator uses conservative estimates with a 3x session multiplier.
- Actual costs are typically lower than the high estimate.
- Run `--sensitivity` to see the range: `python3 common/utilities/cost-estimator.py teams/<team>/ --sensitivity`.
- Use `--compare-models` to find cheaper model options for non-critical teams.

**"Project directory already exists" error**

The initialization script detected a previous project with the same name. You can:
- Choose to overwrite when prompted.
- Use a different project name.
- Manually continue with the existing project: `./launch-scripts/start-<team>.sh projects/<existing-project>`.

### Getting Help

- **GitHub Issues:** Report bugs and request features on the project's GitHub repository.
- **Discussions:** Ask questions and share your builds in the GitHub Discussions tab.
- **Community:** Join the Agent Foundry community for tips, templates, and project showcases.
- **README:** See the project [README.md](../README.md) for architecture details and links to inspiration.

---

## Complete Example: Sarah's SaaS Startup

This walkthrough follows Sarah, a solo founder, as she uses Agent Foundry to go from idea to deployed MVP. Every step, cost, and timeline is based on realistic usage with the Claude Max 200 plan.

### The Idea

Sarah wants to build **FitTrack Pro**, a B2B SaaS platform that helps personal trainers manage clients, track workouts, and process payments. She has validated the idea through 20 customer interviews and is ready to build.

### Day 1: Initialization (30 minutes, $0)

Sarah clones the repo and runs initialization:

```bash
git clone https://github.com/ConnorBritain/agent_foundry.git
cd agent-foundry
./initialize.sh fittrack-pro
```

The Orchestrator interviews her for 15 minutes. She explains:
- She is building a SaaS for personal trainers.
- She has a validated idea with 20 interviews completed.
- Her 30-day goal is a deployed MVP with 5 beta users.
- She is on the Claude Max 200 plan with a $600 monthly budget.
- She wants parallel execution with balanced involvement.

The Orchestrator generates her `PROJECT_CHARTER.md` with a three-phase plan:

- **Phase 1 (Week 1-2):** C-Suite + Research (parallel)
- **Phase 2 (Week 2-3):** Web App Development + Content Creation (parallel)
- **Phase 3 (Week 3-4):** Sales & Marketing + Code Implementation (parallel)

### Day 1-2: Phase 1 -- Strategy and Research (~$250, 6 hours)

Sarah opens two terminals and launches both teams:

**Terminal 1 -- C-Suite:**
```bash
./launch-scripts/start-c-suite.sh projects/fittrack-pro
```

**Terminal 2 -- Research:**
```bash
./launch-scripts/start-research-deep-dive.sh projects/fittrack-pro
```

She checks in periodically using the dashboard:
```bash
python3 common/utilities/project-status-dashboard.py --project projects/fittrack-pro
```

**C-Suite produces (~$175, 3.5 hours):**
- Business model canvas with SaaS unit economics
- Financial projections showing path to $10K MRR in 6 months
- 15-slide investor pitch deck
- Product requirements document for the MVP
- Go-to-market strategy targeting CrossFit gym owners

**Research produces (~$95, 2.5 hours):**
- Competitive analysis of 12 existing fitness SaaS platforms
- Market sizing: $2.4B TAM, $340M SAM, $12M SOM
- Feature comparison matrix
- Pricing benchmarking across competitors
- Technology trend report on fitness API integrations

Sarah reviews the outputs that evening, makes a few notes in the charter, and moves to Phase 2.

### Day 3-6: Phase 2 -- Building the Product (~$165, 5 hours)

**Terminal 1 -- Web App Development:**
```bash
./launch-scripts/start-web-app-development.sh projects/fittrack-pro
```

**Terminal 2 -- Content Creation:**
```bash
./launch-scripts/start-content-creation.sh projects/fittrack-pro
```

The Web App Development team reads the product requirements from C-Suite's artifacts and the competitive analysis from Research. It builds:

**Web App Development produces (~$105, 2.75 hours):**
- Next.js application with Supabase backend
- Authentication and user management
- Client management dashboard for trainers
- Workout logging and tracking features
- Stripe payment integration for subscriptions
- Deployed to Vercel with custom domain setup instructions
- API documentation

**Content Creation produces (~$65, 2 hours):**
- Landing page copy aligned with C-Suite's positioning
- 4 blog posts about personal training business management
- Email onboarding sequence (5 emails)
- Social media content calendar for 30 days
- Brand voice guide

### Day 7-10: Phase 3 -- Go-to-Market (~$140, 4 hours)

**Terminal 1 -- Sales & Marketing:**
```bash
./launch-scripts/start-sales-marketing.sh projects/fittrack-pro
```

**Terminal 2 -- Code Implementation:**
```bash
./launch-scripts/start-code-implementation.sh projects/fittrack-pro
```

**Sales & Marketing produces (~$90, 2.5 hours):**
- Outbound email campaign targeting CrossFit gym owners
- Sales battle cards for common objections
- Partnership playbook for gym equipment brands
- Customer success onboarding checklist
- Growth analytics dashboard specification

**Code Implementation produces (~$50, 1 hour):**
- Polished onboarding flow based on customer feedback
- Mobile-responsive improvements
- Performance optimizations
- Automated test suite
- Bug fixes from Sarah's manual testing

### Day 11-14: Iteration and Launch

Sarah spends the final days:
- Testing the MVP manually with 3 trainer friends.
- Using Code Implementation for quick fixes (~$30 additional).
- Sending the first outbound campaign from Sales & Marketing's templates.
- Publishing the blog posts from Content Creation.

### Results

| Metric | Result |
|--------|--------|
| Total time | 14 days (about 20 hours of agent work) |
| Total cost | ~$585 |
| Deliverables | Deployed SaaS MVP, marketing site, 4 blog posts, sales materials, pitch deck, financial model |
| Beta users | 5 trainers signed up by Day 14 |
| Teams used | 6 of 8 (skipped Recruitment & HR and Project Planning) |

**Cost breakdown:**

| Team | Cost | Duration |
|------|------|----------|
| C-Suite | $175 | 3.5 hours |
| Research | $95 | 2.5 hours |
| Web App Development | $105 | 2.75 hours |
| Content Creation | $65 | 2 hours |
| Sales & Marketing | $90 | 2.5 hours |
| Code Implementation (x2 sessions) | $80 | 2 hours |
| **Total** | **$585** | **~15 hours of agent time** |

For comparison, hiring freelancers or an agency for the same scope of work would typically cost $15,000-30,000 and take 2-3 months.

### Sarah's Tips

1. **Start with C-Suite.** The strategy documents save enormous time for every downstream team.
2. **Run Research in parallel with C-Suite.** They do not depend on each other and the research enriches everything.
3. **Review between phases.** Spending 30 minutes reviewing Phase 1 outputs before launching Phase 2 prevents wasted work.
4. **Use Code Implementation for iteration.** It is the cheapest team and great for polish.
5. **Do not skip the Orchestrator interview.** The more detail you give upfront, the better every team performs.

---

## Quick Reference

### Key Commands

```bash
# Initialize a new project
./initialize.sh <project-name>

# Launch a team
./launch-scripts/start-<team-name>.sh projects/<project-name>

# Monitor progress
python3 common/utilities/project-status-dashboard.py --project projects/<project-name>

# Estimate costs
python3 common/utilities/cost-estimator.py teams/<team-name>/ --compare-models

# Check project status
cat projects/<project-name>/shared-workspace/project-status.json

# View cross-team messages
cat projects/<project-name>/shared-workspace/cross-team-communication.md

# View dependencies
cat projects/<project-name>/shared-workspace/dependency-tracker.md
```

### Key File Locations

| File | Purpose |
|------|---------|
| `projects/<name>/PROJECT_CHARTER.md` | Master plan for your project |
| `projects/<name>/shared-workspace/project-status.json` | Real-time team status |
| `projects/<name>/shared-workspace/artifacts/<team>/` | Team deliverables |
| `projects/<name>/shared-workspace/cross-team-communication.md` | Inter-team messages |
| `projects/<name>/shared-workspace/dependency-tracker.md` | Dependency tracking |
| `teams/<team>/agents/` | Agent definitions (editable) |
| `common/utilities/cost-estimator.py` | Cost estimation tool |
| `common/utilities/project-status-dashboard.py` | Status dashboard |
| `templates/PROJECT_CHARTER.md` | Charter template |

---

*This guide is part of the Agent Foundry project. For architecture details, see the [README](../README.md). For contributing, see [CONTRIBUTING.md](../CONTRIBUTING.md).*
