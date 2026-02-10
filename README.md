# Agent Foundry

> From idea to deployed business—all agents.

An open-source operating system for building and running businesses with coordinated AI agent teams. Whether you're a solo founder building a SaaS app or a small team launching a new venture, Agent Foundry provides battle-tested team templates that handle everything from business strategy to production deployment.

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/ConnorBritain/agent_foundry.git
cd agent_foundry

# 2. Initialize your project (launches the Orchestrator interview)
./initialize.sh

# 3. Launch teams (after Orchestrator creates your plan)
./launch-scripts/start-c-suite.sh projects/your-project

# 4. Monitor progress
python3 common/utilities/control-plane.py --project projects/your-project
```

**What you need:** Claude Max Plan ($200/month recommended) or API key, Python 3, Git

**What you get:** A complete business built by coordinated agent teams — from strategy to deployed product.

See [docs/USER_GUIDE.md](docs/USER_GUIDE.md) for the full walkthrough. See [ROADMAP.md](ROADMAP.md) for what's coming next.

## What is Agent Foundry?

Agent Foundry provides complete team templates for running every aspect of a business:
- **C-Suite**: Strategy, financials, pitch decks, org design
- **Web App Development**: Full-stack SaaS with Supabase + Vercel + Stripe
- **Sales & Marketing**: Go-to-market strategy, demand generation, sales enablement, pipeline management
- **Recruitment & HR**: Hiring pipeline, onboarding, culture building, performance management
- **Content Creation**: Research-backed, humanized content at scale
- **Code Implementation**: Feature development with testing and deployment
- **Project Coordination**: Multi-team orchestration and dependency tracking
- **Research**: Academic, market, competitive, and product research

## Inspired by StrongDM's Software Factory

Built on patterns from [StrongDM's groundbreaking work](https://simonwillison.net/2026/Feb/7/software-factory/):
- Parallel agent swarms with scenario-based convergence
- Multi-team coordination without human bottlenecks
- Cost-optimized workflows with autonomous decision-making
- Comprehensive orchestration infrastructure

## Project Structure

```
agent_foundry/
├── initialize.sh           # Project setup & Orchestrator launch
├── ORCHESTRATOR.md         # Orchestrator agent system prompt
├── ROADMAP.md              # v1.0 → v3.0 roadmap
├── templates/              # Project charter template
├── launch-scripts/         # Team launch scripts (one per team)
├── docs/                   # User guide & documentation
├── common/                 # Reusable building blocks
│   ├── personalities/      # 10+ agent personalities
│   ├── agents-md/          # Framework & domain knowledge templates
│   ├── skills/             # Universal workflow skills
│   └── utilities/          # File locks, status tracking, cost estimation, control plane
├── teams/                  # 8 complete team templates
│   ├── c-suite/
│   ├── code-implementation/
│   ├── content-creation/
│   ├── project-planning/
│   ├── recruitment-hr/
│   ├── research-deep-dive/
│   ├── sales-marketing/
│   └── web-app-development/
├── strategies/             # 7 decision guides (model selection, deployment, optimization, etc.)
├── shared-workspace/       # Multi-team coordination
├── projects/               # Your project workspaces (created by initialize.sh)
└── specs/                  # Detailed specifications
```

## Team Templates

### C-Suite
Board of AI directors (CEO, CFO, CMO, CTO, COO, VP Sales, General Counsel) that create executable business plans.

**Agents**: 7 | **Cost**: ~$150-200 | **Duration**: ~3-4 hours

### Web App Development
Build and deploy full-stack SaaS applications with Next.js, Supabase, Vercel, and Stripe. Handles marketing site, web app, infrastructure, payments, and revenue operations.

**Agents**: 7 | **Cost**: ~$105 | **Duration**: ~2.75 hours

### Sales & Marketing
Complete go-to-market execution from positioning to pipeline generation. Includes demand generation, sales enablement, pipeline management, customer success, and growth analytics.

**Agents**: 7 | **Cost**: ~$80-120 | **Duration**: ~2-3 hours

### Recruitment & HR
End-to-end people operations from hiring to performance management. Includes job design, candidate sourcing, interviewing, onboarding, culture building, and retention strategies.

**Agents**: 6 | **Cost**: ~$70-100 | **Duration**: ~2-2.5 hours

### Content Creation
Research-backed content with AI pattern removal and brand voice matching. Includes fact-checking and editorial review.

**Agents**: 7 | **Cost**: ~$60-80 | **Duration**: ~2 hours

### Code Implementation
Feature development from requirements to deployment with parallel implementation, code review, testing, and documentation.

**Agents**: 7 | **Cost**: ~$40-60 | **Duration**: ~1 hour

### Project Planning
Transform goals into actionable plans across multiple frameworks (SAFe, Agile, Scrum, even family chores). Integrates with Linear, Google Calendar, Jira.

**Agents**: 7 | **Cost**: ~$50-80 | **Duration**: ~1.5 hours

### Research (Deep Dive)
Comprehensive research with configurable modes (academic, market, competitive, product). Includes lead researcher, source analysis, data synthesis, fact-checking, and report writing.

**Agents**: 9 | **Cost**: ~$80-120 | **Duration**: ~2-3 hours

## Multi-Team Projects

Run multiple teams on the same project with automated coordination:

```
shared-workspace/
├── artifacts/
│   ├── c-suite/              # Strategy docs, financials
│   ├── web-app-development/  # Deployed apps, API docs
│   └── content-creation/     # Brand guidelines, copy
├── project-status.json       # Real-time team dashboard
└── dependency-tracker.md     # Inter-team dependencies
```

## Cost Transparency

- **Single team task**: $40-100
- **Complex feature**: $100-300
- **Complete MVP**: $200-500
- **Multi-team project**: $300-800

Compare to hiring equivalent human team: $10,000-50,000+/month

## Inspiration & Research

- [StrongDM's Software Factory](https://simonwillison.net/2026/Feb/7/software-factory/) - Parallel agents, scenario validation
- [Vercel's AGENTS.md Study](https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals) - Passive context beats active retrieval
- [Anthropic's Agent Skills Spec](https://agentskills.io/specification) - Progressive disclosure, portable skills

## License

MIT License (see LICENSE file)

---

Built with love for founders forging the future
