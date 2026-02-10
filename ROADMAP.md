# Agent Foundry Roadmap

> **From idea to deployed business — all agents.**

Agent Foundry is an open-source operating system for building businesses with coordinated AI agent teams. This roadmap outlines our journey from the current launch release through our long-term vision for fully autonomous business operations.

---

## v1.0 — Launch Release (Current)

The foundation: complete team templates, multi-team orchestration, and a terminal-based control plane.

- [x] 8 complete team templates
  - [x] `c-suite` — Executive strategy, decision-making, and business oversight
  - [x] `web-app-development` — Full-stack web application development
  - [x] `sales-marketing` — Sales pipeline and marketing campaign management
  - [x] `recruitment-hr` — Talent acquisition and human resources operations
  - [x] `content-creation` — Content strategy, writing, and publishing
  - [x] `code-implementation` — Focused software engineering and code delivery
  - [x] `project-planning` — Project scoping, scheduling, and tracking
  - [x] `research-deep-dive` — In-depth research, analysis, and reporting
- [x] Multi-team orchestration infrastructure (`shared-workspace/`)
- [x] Orchestrator agent for project initialization (`ORCHESTRATOR.md`)
- [x] Manual/scripted session management (`launch-scripts/`)
- [x] Plan-aware recommendations (Pro / Max 100 / Max 200 / API)
- [x] Terminal-based control plane dashboard (`control-plane.py`)
- [x] Shared workspace coordination protocols
- [x] Cost tracking and budget alerts

---

## v1.1 — Near-Term Improvements (1-2 Months Post-Launch)

Polishing the developer experience, expanding the template library, and bridging toward full automation.

### 1. Enhanced Launch Scripts (CLI)

- tmux/screen session automation for multi-agent workflows
- Checkpoint and resume support for long-running sessions
- Pre-flight checks (API key validation, dependency verification, budget confirmation)

### 2. Improved Control Plane

- Real-time cost visualization with per-agent and per-team breakdowns
- Dependency graph rendering across teams and deliverables
- Export reports (PDF, CSV, JSON) for project summaries and cost audits
- Slack and email notification integrations for status updates and budget alerts

### 3. Team Templates Expansion

- **Legal & Compliance** — Contract review, regulatory analysis, policy drafting
- **Customer Support** — Ticket triage, knowledge base management, escalation workflows
- **Finance & Accounting** — Budgeting, forecasting, invoice processing, financial reporting
- **Data & Analytics** — Data pipeline design, dashboarding, statistical analysis

### 4. Skill Library Growth

- Mobile development skills (React Native, Flutter, Swift, Kotlin)
- Advanced infrastructure skills (Kubernetes, Terraform, multi-cloud)
- ML/AI skills (model training pipelines, evaluation, deployment)
- Enterprise integration skills (SAP, Salesforce, ServiceNow)

### 5. Quality of Life

- Interactive tutorial for first-time users
- Example projects with pre-built configurations
- Video walkthroughs for common workflows
- Community template sharing and discovery

---

## v2.0 — Major Release (3-6 Months Post-Launch)

**Primary Goal: The Orchestration Daemon** — fully automated multi-agent orchestration that eliminates manual session management entirely.

### Orchestration Daemon

The flagship feature of v2.0. A background service that manages the full lifecycle of agent teams.

```
agent-foundry-daemon start
```

- Background orchestration service with programmatic agent spawning via the Anthropic API
- Advanced orchestration patterns:
  - Dynamic agent spawning based on workload
  - Hierarchical team structures with delegation
  - Agent-to-agent negotiation protocols
  - Conditional workflows with branching logic
- State management backed by SQLite
  - Full conversation replay
  - Time-travel debugging for diagnosing agent decisions

### Desktop Application

An Electron + React application providing a native desktop experience.

- Visual team builder with drag-and-drop configuration
- Real-time agent activity monitoring
- Integrated terminal for direct agent interaction
- System tray integration for background operation

### Web Dashboard (Control Plane 2.0)

A full-featured web dashboard served at `localhost:3000`.

- Project overview with live agent status
- Cost analytics and forecasting
- Team performance metrics
- Workflow visualization and editing

### Python SDK

First-class programmatic access for developers who want to embed Agent Foundry in their own tools.

```python
from agent_foundry import Orchestrator

orc = Orchestrator(project="my-startup")
orc.spawn_team("web-app-development")
orc.assign_task("Build the landing page")
```

### Additional v2.0 Features

- **Multi-user collaboration** — Shared projects with role-based access
- **Agent memory and learning** — Persistent context across sessions, improving over time
- **Template marketplace** — Publish, discover, and install community-built templates
- **Advanced analytics** — Token usage trends, agent efficiency scores, ROI tracking
- **Integration ecosystem:**
  - GitHub Actions for CI/CD-triggered agent workflows
  - Slack for conversational agent control
  - Linear / Jira for issue-driven task assignment
  - Google Drive for document input and output

### Technical Architecture

```
+---------------------------+
|   Desktop App / Web UI    |
|   (Electron + React)      |
+------------+--------------+
             |
             v
+---------------------------+
|      Python Daemon        |
|  - Agent lifecycle mgmt   |
|  - Message queue           |
|  - State management        |
|  - Anthropic API client    |
+------------+--------------+
             |
             v
+---------------------------+
|     Anthropic API         |
+---------------------------+
```

### Estimated Investment

| Milestone | Estimated Cost |
|-----------|---------------|
| MVP (daemon + basic dashboard) | ~$50K |
| Full v2.0 release | ~$120K |

---

## v3.0 — Future Vision (6-12 Months Post-Launch)

The long-term vision: Agent Foundry as a continuously operating business engine.

### 1. Autonomous Business Operations

- Agents run continuously with weekly and monthly execution cycles
- Self-healing workflows that detect and recover from failures
- Automated reporting and stakeholder updates on recurring schedules

### 2. Multi-Project Management

- Portfolio-level oversight across multiple businesses or product lines
- Cross-project resource allocation and priority balancing
- Unified dashboard for executive-level visibility

### 3. Advanced AI Capabilities

- Custom fine-tuned models for domain-specific tasks
- Multi-modal agent support (vision, audio, document understanding)
- Real-world action execution (API calls, transactions, deployments)

### 4. Enterprise Features

- SSO and identity provider integration (SAML, OIDC)
- Comprehensive audit logs for compliance and governance
- On-premises deployment option for regulated industries
- SLA guarantees with uptime and performance commitments

---

## Implementation Priority

The order in which major initiatives will be tackled:

| Priority | Initiative | Target |
|----------|-----------|--------|
| 1 | **Orchestration Daemon** | v2.0 flagship feature |
| 2 | **Web Dashboard** | v2.0 companion interface |
| 3 | **Enhanced Launch Scripts** | v1.1 bridge to automation |
| 4 | **Template Expansion** | Ongoing across all releases |

---

## Contributing

Agent Foundry is open source. If any of these roadmap items excite you, we welcome contributions. Check the individual team template directories for contribution guidelines, or open an issue to discuss new ideas.
