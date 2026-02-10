# Orchestrator Daemon: Technical Specification & UX Design

**Sforza v2.0 Flagship Feature**

---

## Table of Contents

1. [What is a Daemon?](#what-is-a-daemon)
2. [The Vision](#the-vision)
3. [Technical Architecture](#technical-architecture)
4. [Implementation Options](#implementation-options)
5. [Detailed UX Walkthrough](#detailed-ux-walkthrough)
6. [User-Friendly Design Principles](#user-friendly-design-principles)
7. [Realistic Build Plan](#realistic-build-plan)
8. [Honest Assessment](#honest-assessment)

---

## What is a Daemon?

### Simple Explanation

A daemon is a program that runs in the background on your computer, like Dropbox, Spotify, or your antivirus software. You don't interact with it directly most of the time—it just quietly does its job. You interact with it through a separate interface (like a menu bar icon, web page, or app window).

### For Sforza

The Sforza Orchestrator Daemon would be a background service that:

- **Manages all your AI agent sessions** - Keeps track of multiple teams working simultaneously
- **Coordinates handoffs between teams** - When Business Planning finishes positioning, automatically notifies Content Creation
- **Sends you notifications when decisions are needed** - "Business Planning needs your input on pricing strategy"
- **Runs continuously** - 24/7 or whenever you tell it to run
- **Handles the complexity** - You focus on strategic decisions, it handles execution

### Real-World Analogy

Think of it like a smart home hub (like Nest or Alexa):
- The hub runs in the background
- It controls all your devices (in our case, AI agents)
- You interact with it via an app or voice commands
- It handles coordination automatically
- You just approve major decisions

The Orchestrator Daemon is your AI project manager that never sleeps.

---

## The Vision

### What Success Looks Like

**Monday morning:**
```
Sarah opens Sforza app
Sarah: "Build me a SaaS meal planning app"
Orchestrator: "I'll need Business Planning, Research, and Content teams"
Sarah: "Approved, budget is $500"
Orchestrator: "Starting all three teams now..."
```

**Monday lunch (on her phone):**
```
📱 Notification: "Business Planning needs input on pricing"
Sarah reviews 3 options, taps "Option A"
Teams automatically unblock and continue
```

**Friday afternoon:**
```
📱 Notification: "Phase 1 complete!"
Sarah opens app, downloads:
- Complete business plan
- Market research
- Financial model
- Brand guidelines
- Pitch deck

Total cost: $284
Time invested: ~3 hours of approvals
```

**Following week:**
```
Sarah: "Now build the MVP"
Orchestrator launches Web App Development Team
By Friday: Deployed app at mealplan-ai-staging.vercel.app
```

### The Promise

**For non-engineers:**
- No terminal, no code, no Claude Code sessions to manage
- Click buttons and approve decisions
- Preview everything in the app
- Get a complete business in 2-4 weeks

**For junior devs:**
- Familiar Slack-like interface
- Can inspect agent work if curious
- CLI available for power users
- Full customization if needed

**For everyone:**
- From idea to deployed business
- Mostly hands-off execution
- Pay only for work done
- Professional quality output

---

## Technical Architecture

### Option 1: Desktop App (Electron) - **RECOMMENDED**

This is the recommended approach for Sforza v2.0.

#### Why Desktop App?

- ✅ Runs locally (full data control, works offline for viewing)
- ✅ Familiar UX (like Slack, Discord, VS Code)
- ✅ Can use both Claude Max plan AND API key
- ✅ No cloud hosting costs
- ✅ Cross-platform (Mac, Windows, Linux)
- ✅ One-time install, auto-updates built-in

#### Architecture Diagram

```
┌─────────────────────────────────────────────────────────┐
│  Frontend: Electron + React                             │
│  ─────────────────────────────────────────────────────  │
│  • Dashboard UI (team status, progress, deliverables)   │
│  • Approval interface (decisions, phase transitions)    │
│  • File browser (preview PDFs, docs, code)             │
│  • Settings (budget, notifications, preferences)        │
│  • Runs on: macOS, Windows, Linux                       │
│  • Install: One-time download or `brew install`         │
└────────────────────────┬────────────────────────────────┘
                         │
                         ↓ IPC (Inter-Process Communication)
                         │
┌────────────────────────▼────────────────────────────────┐
│  Backend Daemon: Python                                 │
│  ─────────────────────────────────────────────────────  │
│  • Agent Lifecycle Manager                              │
│    - Spawn agents via Anthropic API                     │
│    - Monitor agent health and progress                  │
│    - Handle agent failures and retries                  │
│                                                          │
│  • Orchestration Engine                                 │
│    - Coordinate cross-team dependencies                 │
│    - Manage phase transitions                           │
│    - Route messages between agents                      │
│    - Enforce orchestration rules                        │
│                                                          │
│  • State Manager (SQLite)                               │
│    - Conversation history (full replay capability)      │
│    - Agent status and progress                          │
│    - User decisions and approvals                       │
│    - Deliverable metadata                               │
│                                                          │
│  • Message Queue (In-Memory/Redis Lite)                 │
│    - Agent-to-agent messages                            │
│    - User approval requests                             │
│    - System notifications                               │
│                                                          │
│  • Cost Tracker                                         │
│    - Token usage per team/agent                         │
│    - Budget enforcement                                 │
│    - Spending projections                               │
│                                                          │
│  • File Manager                                         │
│    - Organize deliverables                              │
│    - Handle shared workspace                            │
│    - Manage checkpoints                                 │
└────────────────────────┬────────────────────────────────┘
                         │
                         ↓ HTTPS API Calls
                         │
┌────────────────────────▼────────────────────────────────┐
│  Anthropic API (claude.ai)                              │
│  ─────────────────────────────────────────────────────  │
│  • Multiple concurrent conversations (one per agent)    │
│  • Streaming responses for real-time updates           │
│  • Tool use for MCP server integration                 │
└─────────────────────────────────────────────────────────┘
```

#### Data Flow Example

**User approves a decision:**

```
1. User clicks "Approve Option A" in Electron app
   ↓
2. React frontend sends IPC message to Python daemon
   ↓
3. Daemon updates SQLite state
   ↓
4. Daemon sends message to Business Planning Agent via API
   ↓
5. Agent receives decision, continues work
   ↓
6. Agent posts message to message queue: "Positioning finalized"
   ↓
7. Daemon routes message to Content Creation Agent
   ↓
8. Content team unblocks automatically
   ↓
9. Daemon sends status update to frontend
   ↓
10. Dashboard updates: "Content Creation: Phase 1 - 42%"
```

#### File Structure

```
sforza-desktop/
├── electron/                    # Electron main process
│   ├── main.js                 # App entry point
│   ├── ipc-handlers.js         # Communication with daemon
│   └── auto-updater.js         # Automatic updates
│
├── frontend/                    # React UI
│   ├── src/
│   │   ├── components/
│   │   │   ├── Dashboard.tsx
│   │   │   ├── TeamCard.tsx
│   │   │   ├── ApprovalModal.tsx
│   │   │   ├── FileViewer.tsx
│   │   │   └── Settings.tsx
│   │   ├── hooks/
│   │   │   ├── useProjectStatus.ts
│   │   │   ├── useTeamData.ts
│   │   │   └── useNotifications.ts
│   │   └── App.tsx
│   └── package.json
│
├── daemon/                      # Python backend
│   ├── orchestrator/
│   │   ├── agent_manager.py    # Spawn, monitor agents
│   │   ├── coordination.py     # Cross-team logic
│   │   ├── state.py            # SQLite operations
│   │   └── messaging.py        # Message queue
│   ├── api/
│   │   └── anthropic_client.py # Anthropic API wrapper
│   ├── cost/
│   │   └── tracker.py          # Token/cost tracking
│   ├── files/
│   │   └── manager.py          # File operations
│   └── main.py                 # Daemon entry point
│
├── shared/                      # Shared between frontend/backend
│   ├── types.ts                # TypeScript types
│   └── constants.py            # Python constants
│
└── installer/                   # Platform-specific installers
    ├── macos/
    ├── windows/
    └── linux/
```

---

### Option 2: Web App + Browser Extension

This is a lighter-weight alternative that works entirely in the browser.

#### Architecture Diagram

```
┌──────────────────────────────────────────────────────┐
│  Web App: React (hosted on Vercel)                   │
│  URL: app.agentfoundry.ai                            │
│  ───────────────────────────────────────────────────│
│  • Dashboard UI                                       │
│  • Real-time updates via WebSocket                   │
│  • Approval interface                                 │
│  • File downloads                                     │
└────────────────────┬─────────────────────────────────┘
                     │
                     ↓ WebSocket / REST API
                     │
┌────────────────────▼─────────────────────────────────┐
│  Browser Extension: Chrome/Firefox                    │
│  ───────────────────────────────────────────────────│
│  • Monitors claude.ai tabs                           │
│  • Intercepts agent sessions                         │
│  • Sends status updates to web app                   │
│  • Manages multiple Claude Code tabs                 │
└────────────────────┬─────────────────────────────────┘
                     │
                     ↓ Browser Tab Management
                     │
┌────────────────────▼─────────────────────────────────┐
│  Multiple claude.ai tabs (one per agent)             │
│  ───────────────────────────────────────────────────│
│  • Each tab runs one agent team                      │
│  • Extension coordinates between tabs                │
│  • Uses Claude Max plan (no API key needed)          │
└──────────────────────────────────────────────────────┘
```

#### Pros & Cons

**Pros:**
- ✅ No installation (just browser extension)
- ✅ Works on any device with Chrome/Firefox
- ✅ Instant updates (web-based)
- ✅ Lower development cost (~$25K vs $50K)

**Cons:**
- ❌ Can't use API key directly (only works with Claude Max plan)
- ❌ Limited by browser tab management (can't truly spawn sessions programmatically)
- ❌ Requires constant internet connection
- ❌ More fragile (depends on claude.ai UI staying stable)

**Verdict:** Good for v1.5 (bridge to full daemon), not ideal for v2.0.

---

### Option 3: Hosted SaaS Service

This is the most user-friendly option but requires significant infrastructure.

#### Architecture Diagram

```
┌──────────────────────────────────────────────────────┐
│  Web Dashboard: Next.js (Vercel)                     │
│  URL: app.agentfoundry.ai                            │
│  ───────────────────────────────────────────────────│
│  • User authentication (email/password)              │
│  • Project dashboard                                  │
│  • Real-time team status                             │
│  • Approval interface                                 │
│  • Mobile-responsive                                  │
└────────────────────┬─────────────────────────────────┘
                     │
                     ↓ HTTPS + WebSocket
                     │
┌────────────────────▼─────────────────────────────────┐
│  Backend API: Node.js/Python (AWS/GCP)               │
│  ───────────────────────────────────────────────────│
│  • REST API endpoints                                 │
│  • WebSocket server (real-time updates)              │
│  • Authentication & authorization                     │
│  • Rate limiting & quotas                            │
└────────────────────┬─────────────────────────────────┘
                     │
         ┌───────────┼───────────┐
         ▼           ▼           ▼
    [Database]  [Queue]    [Workers]
    PostgreSQL   Redis    Python/Node
         │           │           │
         └───────────┴───────────┘
                     │
                     ↓
         Anthropic API (many concurrent sessions)
```

#### Infrastructure Components

**Database (PostgreSQL):**
- User accounts and authentication
- Project configurations
- Agent conversation history
- Deliverable metadata
- Billing and usage tracking

**Message Queue (Redis):**
- Agent-to-agent messages
- User approval requests
- Background job queue
- Real-time event streaming

**Worker Pool (Python):**
- Agent session managers (one per active agent)
- Orchestration logic
- Cost tracking
- File processing

**Object Storage (S3):**
- Deliverable files (PDFs, docs, code)
- Agent checkpoints
- Backup/restore

#### Pros & Cons

**Pros:**
- ✅ Zero installation (just visit website)
- ✅ Works on any device (phone, tablet, laptop)
- ✅ Agents run 24/7 (even when you're offline)
- ✅ Multi-user collaboration
- ✅ Automatic updates
- ✅ Most user-friendly UX
- ✅ Push notifications
- ✅ Enterprise features possible (SSO, compliance)

**Cons:**
- ⚠️ Requires hosting infrastructure ($2-5K/month)
- ⚠️ Need to manage user data securely (GDPR, SOC2)
- ⚠️ Users pay for both Sforza subscription + Anthropic API usage
- ⚠️ Most complex to build ($80K MVP vs $50K desktop)
- ⚠️ Ongoing operational costs

#### Business Model (if SaaS)

```
Free Tier:
- 1 project
- Up to 3 teams simultaneously
- Community support
- Max $50/month API usage

Pro: $29/month
- Unlimited projects
- Unlimited teams
- Priority support
- Team collaboration (up to 5 users)
- Max $500/month API usage (then overage charges)

Enterprise: Custom pricing
- SSO (SAML, OAuth)
- On-premises deployment option
- SLA guarantees
- Dedicated support
- Custom integrations
- Audit logs and compliance
```

**Revenue model:**
- Subscription fees ($29/mo/user)
- API usage markup (20-30% on Anthropic costs)
- Example: If user spends $100 on Anthropic API, Sforza charges $120-130

---

## Implementation Options: Comparison Matrix

| Feature | Desktop App | Browser Extension | Hosted SaaS |
|---------|------------|-------------------|-------------|
| **Installation** | One-time download | One-click extension | None (web-based) |
| **Platform** | Mac, Windows, Linux | Chrome, Firefox | Any (mobile too) |
| **API Key Support** | ✅ Full support | ❌ Max plan only | ✅ Full support |
| **Works Offline** | ✅ View past work | ❌ Requires internet | ❌ Requires internet |
| **Data Control** | ✅ Fully local | ⚠️ Local + cloud | ❌ Cloud-hosted |
| **Auto-updates** | ✅ Built-in | ✅ Automatic | ✅ Instant |
| **Multi-device** | ⚠️ Sync required | ✅ Via account | ✅ Seamless |
| **Multi-user** | ❌ Single user | ❌ Single user | ✅ Team collaboration |
| **Agent Spawning** | ✅ Programmatic | ⚠️ Limited | ✅ Fully autonomous |
| **24/7 Operation** | ⚠️ While app open | ❌ Browser must be open | ✅ Background workers |
| **Development Cost** | $50K | $25K | $80K |
| **Hosting Cost** | $0 | $0 | $3-5K/month |
| **Time to MVP** | 3 months | 2 months | 4 months |
| **Best For** | Solo founders, full control | Light users, testing | Teams, enterprise |

**Recommendation for v2.0:** Start with Desktop App, consider SaaS for v3.0.

---

## Detailed UX Walkthrough

This walkthrough shows exactly what using the Desktop App version would feel like for a real user.

### Day 1: Installation & First Project

#### 10:00 AM - Sarah Downloads Sforza

**On macOS:**
```bash
# Sarah opens Terminal and runs:
brew install sforza

# Output:
==> Downloading sforza-2.0.0-darwin-arm64.dmg
==> Installing Sforza...
==> Application installed to /Applications/Sforza.app
✓ Sforza installed successfully!

# Or, Sarah visits agentfoundry.ai/download
# Clicks "Download for Mac"
# Double-clicks Sforza.dmg
# Drags app to Applications folder
```

**Icon appears in Applications. Sarah double-clicks to open.**

---

#### 10:02 AM - Setup Wizard

**Screen 1: Welcome**
```
┌──────────────────────────────────────────────────────┐
│                                                      │
│              🔨 Sforza                        │
│                                                      │
│         Where agent teams are forged                 │
│                                                      │
│                                                      │
│  Welcome! Let's set up your workspace.              │
│                                                      │
│  This will take about 5 minutes.                    │
│                                                      │
│                                                      │
│                                                      │
│                                                      │
│                                                      │
│                    [Get Started →]                   │
│                                                      │
└──────────────────────────────────────────────────────┘
```

**Screen 2: Connect Anthropic**
```
┌──────────────────────────────────────────────────────┐
│  Step 1/3: Connect Anthropic                         │
│  ───────────────────────────────────────────────────│
│                                                      │
│  Sforza uses Claude to power your teams.     │
│  Choose how you want to connect:                    │
│                                                      │
│  ○ I have Claude Max 200 plan ($200/month)         │
│     Sign in with your Anthropic account             │
│     [Sign in with Anthropic →]                      │
│                                                      │
│     Note: Works within your plan's rate limits.     │
│     Best for: Moderate usage, 3-5 teams/day         │
│                                                      │
│  ● I have an API key (pay-as-you-go)               │
│     Get one at console.anthropic.com/keys           │
│                                                      │
│     API Key: [sk-ant-api03-••••••••••••••••]        │
│                                                      │
│     Note: No rate limits, pure usage-based cost.    │
│     Best for: Unlimited teams, faster execution     │
│                                                      │
│                                                      │
│                [← Back]        [Next →]             │
└──────────────────────────────────────────────────────┘
```

**Screen 3: Project Storage**
```
┌──────────────────────────────────────────────────────┐
│  Step 2/3: Choose Project Location                   │
│  ───────────────────────────────────────────────────│
│                                                      │
│  Where should Sforza store your projects?    │
│                                                      │
│  Default location:                                   │
│  📁 /Users/sarah/Documents/Sforza              │
│                                                      │
│  [Browse...] [Use Default]                          │
│                                                      │
│  All your projects, deliverables, and agent work    │
│  will be saved here. You can change this later.     │
│                                                      │
│  Disk space required:                               │
│  • Minimum: 500 MB (for app and basic projects)    │
│  • Recommended: 5 GB (for multiple projects)        │
│                                                      │
│  Available space: 234 GB ✓                          │
│                                                      │
│                                                      │
│                [← Back]        [Next →]             │
└──────────────────────────────────────────────────────┘
```

**Screen 4: Budget & Preferences**
```
┌──────────────────────────────────────────────────────┐
│  Step 3/3: Budget & Preferences                      │
│  ───────────────────────────────────────────────────│
│                                                      │
│  Set your spending limits:                          │
│                                                      │
│  Daily budget:    $ [500]   per day                 │
│  Weekly budget:   $ [2000]  per week                │
│  Monthly budget:  $ [6000]  per month               │
│                                                      │
│  ☑ Alert me when reaching 80% of budget             │
│  ☑ Require approval before exceeding budget         │
│                                                      │
│  ─────────────────────────────────────────────────  │
│                                                      │
│  Notifications:                                      │
│                                                      │
│  ☑ Desktop notifications                            │
│  ☑ Email notifications (sarah@example.com)          │
│  ☐ SMS notifications (optional)                     │
│                                                      │
│  Notify me when:                                    │
│  ☑ Decision needed                                  │
│  ☑ Team completes phase                             │
│  ☑ All deliverables ready                           │
│                                                      │
│                [← Back]     [Launch Sforza →]│
└──────────────────────────────────────────────────────┘
```

---

#### 10:05 AM - First Project Creation

**Sarah clicks "Launch Sforza". App opens to main dashboard:**

```
┌──────────────────────────────────────────────────────┐
│  Sforza              sarah@example.com  [⚙️] [↓]│
├──────────────────────────────────────────────────────┤
│                                                      │
│              Welcome to Sforza!               │
│                                                      │
│                         🔨                           │
│                                                      │
│              Ready to forge your first               │
│                  agent-powered business?             │
│                                                      │
│                                                      │
│                  [+ Create Project]                  │
│                                                      │
│                                                      │
│  Or explore:                                        │
│  • Example projects                                 │
│  • Template library                                 │
│  • Documentation                                     │
│                                                      │
└──────────────────────────────────────────────────────┘
```

**Sarah clicks "+ Create Project". Modal opens:**

```
┌──────────────────────────────────────────────────────┐
│  Create New Project                            [×]  │
├──────────────────────────────────────────────────────┤
│                                                      │
│  Project name:                                       │
│  [MealPlan AI                                    ]  │
│                                                      │
│  What are you building? (2-3 sentences)             │
│  ┌────────────────────────────────────────────────┐ │
│  │ An AI-powered meal planning app for busy      │ │
│  │ parents. It generates weekly meal plans based │ │
│  │ on dietary preferences, creates shopping      │ │
│  │ lists, and provides step-by-step recipes.     │ │
│  └────────────────────────────────────────────────┘ │
│                                                      │
│  Current stage:                                      │
│  ● Just an idea - need validation                   │
│  ○ Validated - ready to build MVP                   │
│  ○ Have MVP - need to launch                        │
│  ○ Have customers - need to scale                   │
│                                                      │
│  Primary goal (next 30 days):                       │
│  ○ Validate business idea                           │
│  ○ Build and deploy MVP                             │
│  ● Get first 10 customers                           │
│  ○ Raise funding                                    │
│  ○ Other: _______________                           │
│                                                      │
│               [Cancel]    [Create Project →]        │
└──────────────────────────────────────────────────────┘
```

---

#### 10:07 AM - Orchestrator Interview

**Sarah clicks "Create Project". Orchestrator agent initializes:**

```
┌──────────────────────────────────────────────────────┐
│  MealPlan AI                                    [×] │
├──────────────────────────────────────────────────────┤
│                                                      │
│  👋 Hi Sarah! I'm your Orchestrator.                │
│                                                      │
│  I've reviewed your project goals. Let me help you  │
│  create an execution plan.                          │
│                                                      │
│  ─────────────────────────────────────────────────  │
│                                                      │
│  Your Goal: Get first 10 customers (30 days)        │
│  Your Stage: Just an idea                           │
│  Your Budget: $6,000/month                          │
│                                                      │
│  To reach your goal, I recommend this plan:         │
│                                                      │
│  📅 Week 1-2: Validate & Plan                       │
│  ✓ Business Planning Team                           │
│    Create business model, pricing, financials       │
│    Duration: ~3 hours  │  Cost: ~$150              │
│                                                      │
│  ✓ Research Team                                    │
│    Market validation, competitor analysis           │
│    Duration: ~2 hours  │  Cost: ~$80               │
│                                                      │
│  ✓ Content Creation Team                            │
│    Brand messaging, value props, pitch materials    │
│    Duration: ~2 hours  │  Cost: ~$60               │
│                                                      │
│  📅 Week 3-4: Build MVP                             │
│  ✓ Web App Development Team                         │
│    Next.js app with auth, payments, meal planner    │
│    Duration: 3 days  │  Cost: ~$315                │
│                                                      │
│  📅 Week 5-6: Launch & Acquire                      │
│  ✓ Sales & Marketing Team                           │
│    Landing page, ads, email sequences, CRM setup    │
│    Duration: 2 days  │  Cost: ~$285                │
│                                                      │
│  ─────────────────────────────────────────────────  │
│                                                      │
│  Total estimated cost: $890                         │
│  Total estimated time: 6 weeks                      │
│  Your involvement: ~2-3 hours/week for approvals    │
│                                                      │
│  Since you have an API key, I can run Phase 1       │
│  teams (Business, Research, Content) in parallel    │
│  to finish in 2 days instead of 5.                  │
│                                                      │
│              [Customize Plan]   [Looks Good! →]     │
└──────────────────────────────────────────────────────┘
```

---

#### 10:08 AM - Sarah Approves, Teams Launch

**Sarah clicks "Looks Good!". Orchestrator confirms:**

```
┌──────────────────────────────────────────────────────┐
│  Ready to Launch Phase 1                        [×] │
├──────────────────────────────────────────────────────┤
│                                                      │
│  I'll start these teams now:                        │
│                                                      │
│  • Business Planning Team                           │
│  • Research Team                                     │
│  • Content Creation Team                            │
│                                                      │
│  They'll run in parallel and coordinate via the     │
│  shared workspace.                                   │
│                                                      │
│  Estimated completion: Wednesday, 4:00 PM           │
│  Estimated cost: $290                               │
│                                                      │
│  I'll notify you when:                              │
│  • Teams need your input on decisions               │
│  • Any team completes a phase                       │
│  • All deliverables are ready                       │
│                                                      │
│  You can monitor progress anytime in the dashboard. │
│                                                      │
│                                                      │
│                 [Cancel]     [Start Teams →]        │
└──────────────────────────────────────────────────────┘
```

**Sarah clicks "Start Teams →".**

**Behind the scenes (Sarah doesn't see this):**
```python
# Daemon spawns 3 agent workers
orchestrator.spawn_agent(
    team="business-planning",
    workspace="/Users/sarah/Documents/Sforza/MealPlan-AI/business-planning/",
    charter="/Users/sarah/Documents/Sforza/MealPlan-AI/PROJECT_CHARTER.md",
    budget_limit=200,
    priority="high"
)

orchestrator.spawn_agent(
    team="research",
    workspace="/Users/sarah/Documents/Sforza/MealPlan-AI/research/",
    charter="/Users/sarah/Documents/Sforza/MealPlan-AI/PROJECT_CHARTER.md",
    budget_limit=100,
    priority="high"
)

orchestrator.spawn_agent(
    team="content-creation",
    workspace="/Users/sarah/Documents/Sforza/MealPlan-AI/content/",
    charter="/Users/sarah/Documents/Sforza/MealPlan-AI/PROJECT_CHARTER.md",
    budget_limit=80,
    priority="medium",
    depends_on=["business-planning"]  # Waits for positioning
)

# Each agent worker starts making Anthropic API calls
# Agents read PROJECT_CHARTER.md for context
# Agents coordinate via message queue
# Daemon monitors all agents
# Dashboard updates in real-time
```

---

#### 10:09 AM - Dashboard Shows Active Teams

**Main dashboard updates to show active work:**

```
┌──────────────────────────────────────────────────────┐
│  Sforza           sarah@example.com   [⚙️] [↓] │
├──────┬───────────────────────────────────────────────┤
│      │                                               │
│ 🗂️    │  MealPlan AI              ●  3 teams active  │
│ My   │  ────────────────────────────────────────────│
│ SaaS │                                               │
│      │  📊 Business Planning    Phase 1/4   15%     │
│ ○    │     Setting up workspace and loading context  │
│ Idea │     Agent: Coordinator                        │
│      │     Started: 2 minutes ago                    │
│ ○    │                                               │
│ Paused│  🔬 Research             Phase 1/4   10%     │
│      │     Analyzing market size and opportunity     │
│ [+]  │     Agent: Coordinator                        │
│ New  │     Started: 2 minutes ago                    │
│      │                                               │
│      │  ✍️  Content Creation    Waiting             │
│      │     Dependencies: Awaiting brand positioning  │
│      │     Will start when Business Planning ready   │
│      │                                               │
│      │  ────────────────────────────────────────────│
│      │                                               │
│      │  💰 Budget                                    │
│      │  $12.34 spent / $290 budgeted (Phase 1)      │
│      │  ████░░░░░░░░░░░░░░░░░░░░░░░░░ 4%            │
│      │                                               │
│      │  ⏱️  Timeline                                 │
│      │  Started: 2 minutes ago                       │
│      │  Est. completion: Wednesday 4:00 PM (2 days)  │
│      │                                               │
│      │  📁 Deliverables (0)                          │
│      │  Teams haven't produced outputs yet           │
│      │                                               │
└──────┴───────────────────────────────────────────────┘
```

**Auto-refreshes every 5 seconds. Sarah can minimize and come back anytime.**

---

### 11:30 AM - First Decision Needed

**Sarah is making lunch. Her phone buzzes:**

```
─────────────────────────────────
📱 iPhone Notification

Sforza

Business Planning Team needs 
your input

"Market positioning decision"

        [View]
─────────────────────────────────
```

**Sarah taps notification. Sforza app opens on her Mac (syncs via iCloud):**

```
┌──────────────────────────────────────────────────────┐
│  Decision Needed: Market Positioning            [×] │
├──────────────────────────────────────────────────────┤
│                                                      │
│  Business Planning Team - Coordinator                │
│  Timestamp: Monday 11:28 AM                         │
│                                                      │
│  ─────────────────────────────────────────────────  │
│                                                      │
│  I've analyzed the market and identified 3 viable   │
│  positioning strategies. Which should we pursue?     │
│                                                      │
│  ◉ Option A: Time-Starved Parents                  │
│    Target: Busy working parents (25-45 years old)   │
│    Price: $8.99/month                               │
│    Value prop: "Dinner sorted in 5 minutes"         │
│                                                      │
│    Market size: 15M US households                   │
│    Competition: HelloFresh, Blue Apron (meal kits)  │
│    Differentiation: AI personalization, no cooking  │
│                                                      │
│    Est. CAC: $35   │   Est. LTV: $180               │
│    Payback: 4 months                                │
│                                                      │
│  ○ Option B: Health-Conscious Families             │
│    Target: Nutrition-focused parents                │
│    Price: $14.99/month                              │
│    Value prop: "Nutritionist-designed meals"        │
│                                                      │
│    Market size: 8M US households                    │
│    Competition: Noom, MyFitnessPal                  │
│    Differentiation: AI meal planning + nutrition    │
│                                                      │
│    Est. CAC: $45   │   Est. LTV: $320               │
│    Payback: 3 months                                │
│                                                      │
│  ○ Option C: Tiered Pricing (Both Segments)        │
│    Basic: $8.99 (convenience)                       │
│    Premium: $14.99 (nutrition + convenience)        │
│                                                      │
│    Broader market but complex positioning           │
│    Higher CAC ($50) due to split messaging          │
│                                                      │
│  [View Full Analysis (PDF) →]                       │
│                                                      │
│            [Ask Question]    [Approve Selected]     │
└──────────────────────────────────────────────────────┘
```

**Sarah clicks "View Full Analysis". PDF viewer opens in app:**

```
┌──────────────────────────────────────────────────────┐
│  Market_Positioning_Analysis.pdf                [×] │
├──────────────────────────────────────────────────────┤
│                                                      │
│  [PDF Viewer showing:                               │
│   - Market size calculations                         │
│   - Competitor SWOT analysis                         │
│   - Customer persona profiles                        │
│   - Pricing sensitivity research                     │
│   - CAC/LTV financial models                         │
│   - Risk analysis per option]                        │
│                                                      │
│  [Page 1 of 12]    [← →]    [Download] [Print]     │
└──────────────────────────────────────────────────────┘
```

**Sarah reads for 5 minutes. Decides Option A makes sense (larger market, faster payback).**

**Closes PDF, returns to decision screen, selects Option A, clicks "Approve Selected":**

```
┌──────────────────────────────────────────────────────┐
│  Confirm Decision                               [×] │
├──────────────────────────────────────────────────────┤
│                                                      │
│  You selected: Option A (Time-Starved Parents)      │
│                                                      │
│  This will guide:                                   │
│  • Product features (speed, simplicity)             │
│  • Pricing strategy ($8.99/month)                   │
│  • Marketing messaging (convenience-focused)         │
│  • Brand personality (friendly, helpful)            │
│                                                      │
│  Once confirmed, the Business Planning Team will    │
│  build financials around this positioning, and      │
│  Content Creation Team will craft messaging.        │
│                                                      │
│  You can always revisit this decision later.        │
│                                                      │
│                                                      │
│                  [← Back]    [Confirm →]            │
└──────────────────────────────────────────────────────┘
```

**Sarah clicks "Confirm →". Confirmation appears:**

```
┌──────────────────────────────────────────────────────┐
│                                                      │
│                        ✓                             │
│                                                      │
│                  Decision Recorded                   │
│                                                      │
│  Business Planning Team will continue with           │
│  Option A (Time-Starved Parents)                    │
│                                                      │
│  Content Creation Team has been notified and        │
│  will begin brand messaging work.                   │
│                                                      │
│                                                      │
│                      [Close]                         │
└──────────────────────────────────────────────────────┘
```

**Behind the scenes:**
```python
# Daemon receives approval
decision = {
    "team": "business-planning",
    "decision_id": "positioning-strategy",
    "choice": "option_a",
    "timestamp": "2026-02-09T11:32:00Z",
    "user": "sarah@example.com"
}

# Store in database
db.save_decision(decision)

# Notify Business Planning agent
agent_manager.send_message(
    to_agent="business-planning",
    message={
        "type": "decision_approved",
        "decision": "positioning",
        "choice": "option_a",
        "details": {
            "target": "time-starved-parents",
            "price": 8.99,
            "value_prop": "dinner-sorted-5-minutes"
        }
    }
)

# Business Planning agent unblocks, continues Phase 2

# Cross-team notification
agent_manager.send_message(
    to_agent="content-creation",
    from_agent="orchestrator",
    message={
        "type": "dependency_resolved",
        "dependency": "brand_positioning",
        "data": {
            "target": "time-starved-parents",
            "tone": "friendly, helpful, empathetic",
            "value_prop": "dinner-sorted-5-minutes",
            "price": 8.99
        }
    }
)

# Content Creation agent automatically unblocks and starts Phase 1
```

**Dashboard updates automatically:**

```
┌──────────────────────────────────────────────────────┐
│  MealPlan AI                      ●  3 teams active  │
│  ────────────────────────────────────────────────────│
│                                                      │
│  📊 Business Planning         Phase 2/4   ████  68% │
│     ✓ Positioning decision approved                 │
│     Now: Building financial model...                │
│                                                      │
│  🔬 Research                  Phase 3/4   ███  89% │
│     Finalizing competitor feature matrix...         │
│                                                      │
│  ✍️  Content Creation         Phase 1/4   ██   42% │
│     ✓ Unblocked! Writing brand guidelines...        │
│     Based on positioning: Time-starved parents      │
│                                                      │
│  💰 $87.23 / $290 budgeted (30%)                    │
│  ⏱️  Est. completion: Today 6:30 PM (accelerated!)  │
│                                                      │
└──────────────────────────────────────────────────────┘
```

---

### 2:30 PM - Check-In (Optional)

**Sarah opens app to check progress while in a meeting:**

```
┌──────────────────────────────────────────────────────┐
│  MealPlan AI                      ●  3 teams active  │
│  ────────────────────────────────────────────────────│
│                                                      │
│  📊 Business Planning         Phase 3/4   ████  85% │
│     Validating financial projections...             │
│     Recent: Created 3-year revenue model            │
│                                                      │
│  🔬 Research                  Complete!   ████ 100% │
│     ✓ All deliverables ready                        │
│     [View Research Report →]                        │
│                                                      │
│  ✍️  Content Creation         Phase 2/4   ███   78% │
│     Writing messaging framework...                  │
│                                                      │
│  💰 $156.89 / $290 budgeted (54%)                   │
│  ⏱️  Est. completion: Today 5:45 PM                 │
│                                                      │
│  📁 Recent Deliverables (3)                         │
│  • Competitor_Analysis.pdf        1.2 MB  12m ago  │
│  • Market_Sizing_Model.xlsx       485 KB  18m ago  │
│  • Customer_Personas.pdf          892 KB  35m ago  │
│                                                      │
└──────────────────────────────────────────────────────┘
```

**Sarah can click on any deliverable to preview. She's happy with progress, closes app, goes back to meeting.**

---

### 6:45 PM - Phase 1 Complete

**Sarah's phone buzzes:**

```
─────────────────────────────────
📱 iPhone Notification

Sforza

🎉 Phase 1 Complete!

All 3 teams finished
6 deliverables ready

Cost: $284.56

          [View]
─────────────────────────────────
```

**Sarah opens app:**

```
┌──────────────────────────────────────────────────────┐
│  MealPlan AI - Phase 1 Complete ✓               [×] │
├──────────────────────────────────────────────────────┤
│                                                      │
│  🎉 Congratulations Sarah!                          │
│                                                      │
│  All Phase 1 teams have completed their work.       │
│                                                      │
│  ─────────────────────────────────────────────────  │
│                                                      │
│  📁 Deliverables (6 files)                          │
│                                                      │
│  📄 Business_Plan_v1.pdf                 2.3 MB    │
│     42 pages  •  Created 10 mins ago                │
│     [Open] [Download] [Share Link]                  │
│                                                      │
│  📊 Financial_Model_3yr.xlsx             856 KB    │
│     P&L, Cash Flow, Cap Table                       │
│     [Open] [Download] [Share Link]                  │
│                                                      │
│  📈 Market_Research_Report.pdf           1.8 MB    │
│     TAM/SAM/SOM, Growth projections                 │
│                                                      │
│  📋 Competitor_Analysis.xlsx             642 KB    │
│     Feature matrix, Pricing, Positioning            │
│                                                      │
│  🎨 Brand_Guidelines_v1.pdf              3.1 MB    │
│     Logo concepts, Colors, Typography, Voice        │
│                                                      │
│  📽️  Investor_Pitch_Deck.pptx            4.2 MB    │
│     15 slides  •  Ready to present                  │
│                                                      │
│  ─────────────────────────────────────────────────  │
│                                                      │
│  💰 Total Cost: $284.56                             │
│  ⏱️  Total Time: 8 hours 36 minutes                 │
│  👤 Your Time: ~47 minutes (approvals & reviews)    │
│                                                      │
│  [Download All as ZIP]   [Open Folder in Finder]   │
│                                                      │
│  ─────────────────────────────────────────────────  │
│                                                      │
│  What's Next?                                       │
│                                                      │
│  Based on your goal (get first 10 customers),       │
│  I recommend:                                        │
│                                                      │
│  → Launch Web App Development Team                  │
│     Build your MVP with Next.js, Supabase, Stripe   │
│     Duration: 3 days  │  Cost: ~$315                │
│                                                      │
│  This will give you a working product to show       │
│  potential customers and validate your pricing.     │
│                                                      │
│              [Not Yet]    [Start Building →]        │
└──────────────────────────────────────────────────────┘
```

**Sarah clicks through each deliverable:**

- **Business Plan**: Opens in built-in PDF viewer, looks comprehensive
- **Financial Model**: Opens in Excel (via macOS Quick Look), projections look reasonable
- **Market Research**: Solid analysis, validates her assumptions
- **Competitor Analysis**: Useful feature comparison
- **Brand Guidelines**: Logo concepts look great (can iterate later)
- **Pitch Deck**: Clean, investor-ready

**Sarah is happy with Phase 1 deliverables. Clicks "Start Building →":**

```
┌──────────────────────────────────────────────────────┐
│  Launch Phase 2: MVP Development                [×] │
├──────────────────────────────────────────────────────┤
│                                                      │
│  I'll start the Web App Development Team.           │
│                                                      │
│  They'll build:                                     │
│  • Landing page (marketing site)                    │
│  • User authentication (OAuth + email)              │
│  • Meal planning interface (core product)           │
│  • Stripe payment integration ($8.99/month)         │
│  • Database with Supabase (user data, meals)        │
│  • Deployment to Vercel (production-ready)          │
│                                                      │
│  Team roster (7 agents):                            │
│  • Coordinator/Tech Lead                            │
│  • Senior Full-Stack Developer                      │
│  • Cloud/DevOps Engineer                            │
│  • Marketing Frontend Developer                     │
│  • Database Engineer                                 │
│  • Revenue Operations Specialist                    │
│  • QA/Test Engineer                                  │
│                                                      │
│  Estimated completion: Thursday evening             │
│  Estimated cost: $315                               │
│                                                      │
│  Your involvement: ~2 hours for phase approvals     │
│                                                      │
│                                                      │
│                  [Cancel]     [Launch Team →]       │
└──────────────────────────────────────────────────────┘
```

**Sarah clicks "Launch Team →". Web App Development Team starts working overnight...**

---

### 3 Days Later - MVP Complete

**Thursday 7:15 PM - Sarah gets notification:**

```
─────────────────────────────────
📱 iPhone Notification

Sforza

🚀 MVP Deployed!

Your app is live:
mealplan-ai.vercel.app

Cost: $307.23

        [View]
─────────────────────────────────
```

**Sarah opens app, sees:**

```
┌──────────────────────────────────────────────────────┐
│  MealPlan AI - MVP Deployed ✓                   [×] │
├──────────────────────────────────────────────────────┤
│                                                      │
│  🚀 Your app is live!                               │
│                                                      │
│  Production URL:                                    │
│  https://mealplan-ai.vercel.app                     │
│  [Open in Browser →]                                │
│                                                      │
│  ─────────────────────────────────────────────────  │
│                                                      │
│  What was built:                                    │
│                                                      │
│  ✓ Landing page with hero, features, pricing       │
│  ✓ User signup/login (Google OAuth + email)        │
│  ✓ Meal planning dashboard                         │
│  ✓ Weekly meal plan generator (AI-powered)         │
│  ✓ Shopping list export                            │
│  ✓ Stripe payment flow ($8.99/month)               │
│  ✓ User profile and settings                       │
│  ✓ Responsive design (mobile + desktop)            │
│  ✓ Database schema (Supabase)                      │
│  ✓ Authentication middleware                        │
│  ✓ Payment webhooks (Stripe)                       │
│                                                      │
│  Technical stack:                                   │
│  • Next.js 15 (App Router)                         │
│  • React 19 + TypeScript                           │
│  • Supabase (Postgres + Auth)                      │
│  • Stripe (payments)                                │
│  • Vercel (hosting + deployment)                   │
│  • Tailwind CSS (styling)                          │
│                                                      │
│  ─────────────────────────────────────────────────  │
│                                                      │
│  📁 Deliverables (8 items)                          │
│                                                      │
│  💻 Source Code                                     │
│     [Open in VS Code] [View on GitHub]             │
│                                                      │
│  📄 Technical Documentation                         │
│     API endpoints, Database schema, Deployment      │
│     [View Docs →]                                   │
│                                                      │
│  🧪 Test Coverage Report                            │
│     87% coverage, 342 tests passing                 │
│                                                      │
│  📊 Performance Report                              │
│     Lighthouse: 96/100 Performance                  │
│                                                      │
│  🔐 Security Audit                                  │
│     No critical issues, 2 minor suggestions         │
│                                                      │
│  💳 Stripe Dashboard Setup                          │
│     Products, prices, webhooks configured           │
│                                                      │
│  ☁️  Deployment Pipeline                            │
│     GitHub Actions CI/CD configured                 │
│                                                      │
│  📖 README & Setup Guide                            │
│     For future developers                           │
│                                                      │
│  ─────────────────────────────────────────────────  │
│                                                      │
│  💰 Phase 2 Cost: $307.23                           │
│  💰 Total Cost (All Phases): $591.79                │
│                                                      │
│  Remaining budget: $5,408 / $6,000 this month       │
│                                                      │
│  ─────────────────────────────────────────────────  │
│                                                      │
│  What's Next?                                       │
│                                                      │
│  You now have a working MVP! Ready to acquire       │
│  your first customers.                              │
│                                                      │
│  I recommend:                                        │
│                                                      │
│  → Launch Sales & Marketing Team                    │
│     Set up ads, landing page optimization, CRM,     │
│     email sequences to drive your first signups.    │
│     Duration: 2 days  │  Cost: ~$285                │
│                                                      │
│                [Not Yet]    [Let's Get Customers →] │
└──────────────────────────────────────────────────────┘
```

**Sarah clicks "Open in Browser →". Her MVP loads. She can:**
- Sign up as a test user
- Generate a meal plan
- See the Stripe checkout flow
- Test all features

**Sarah is amazed. 10 days ago, this was just an idea. Now she has a deployed product.**

---

## User-Friendly Design Principles

### For Non-Engineers

#### 1. No Terminal, No Code

**Bad UX (typical dev tools):**
```bash
$ git clone https://github.com/...
$ cd sforza
$ npm install
$ cp .env.example .env
$ # Now edit .env with your API key...
$ npm run dev
$ # Open http://localhost:3000
```

**Good UX (Sforza):**
```
1. Download Sforza app
2. Double-click to install
3. Enter API key in setup wizard
4. Click "Create Project"
5. Done!
```

#### 2. Clear Decisions with Context

**Bad UX:**
```
Configure parameter "market_segment_strategy":
Options: [A, B, C]
Enter choice: _
```

**Good UX:**
```
┌─────────────────────────────────────┐
│ Which market should we target?      │
│                                     │
│ ○ Time-Starved Parents              │
│   Larger market (15M)               │
│   Lower price ($8.99)               │
│   Faster payback (4 months)         │
│                                     │
│ ○ Health-Conscious Families         │
│   Smaller market (8M)               │
│   Higher price ($14.99)             │
│   Better LTV ($320)                 │
│                                     │
│ [View Full Analysis] [Approve]     │
└─────────────────────────────────────┘
```

**Key differences:**
- Natural language question, not parameter name
- Visual selection (radio buttons), not typing
- Context shown inline (market size, price, payback)
- Can drill into full analysis if needed
- Clear action button

#### 3. Notifications at the Right Time

**Bad UX:**
```
[14:23] Agent needs input
[14:24] Agent needs input
[14:25] Agent needs input
[14:26] Agent needs input
```

**Good UX:**
```
Only notify when:
- Decision actually blocks progress
- User can reasonably respond (not 2am)
- Consolidate multiple decisions into one session

[14:30] "3 decisions needed (10 min total)"
```

**Smart batching:**
- Group related decisions together
- Show all 3 at once, user approves in sequence
- Respects user's time

#### 4. Budget Guardrails

**Always visible:**
```
┌─────────────────────────────────┐
│ Budget                          │
│ $284 / $500 this week           │
│ ████████████░░░░░░░ 57%         │
│                                 │
│ ⚠️  Approaching limit (80%)     │
└─────────────────────────────────┘
```

**Automatic enforcement:**
```
┌─────────────────────────────────────┐
│ Budget Limit Approaching            │
│                                     │
│ Current spend: $392 / $500         │
│                                     │
│ Business Planning Team wants to    │
│ run additional market research.    │
│                                     │
│ Estimated cost: $125               │
│ This would exceed your weekly      │
│ budget by $17.                     │
│                                     │
│ [Cancel] [Approve Overage]         │
└─────────────────────────────────────┘
```

#### 5. Progress Visibility

**Simple progress indicators:**
```
📊 Business Planning     ████████  85%
   Building financial model...
```

**Detailed view on click:**
```
┌──────────────────────────────────────┐
│ Business Planning Team               │
│                                      │
│ Phase 3 of 4: Financial Modeling    │
│                                      │
│ Started: 2:15 PM                    │
│ Estimated completion: 4:30 PM       │
│                                      │
│ Recent activity:                    │
│ ✓ Created revenue projections       │
│ ✓ Built cost model                  │
│ ⚙️  Validating assumptions          │
│ ○ Generate financial statements     │
│                                      │
│ Cost so far: $87.23                 │
└──────────────────────────────────────┘
```

---

### For Junior Devs

#### 1. Familiar Interface

**Looks like Slack/Discord:**
- Sidebar with projects
- Main content area with team cards
- Real-time updates
- Threads for discussions

**Looks like GitHub Actions:**
- Visual pipeline
- Green checkmarks for complete
- Orange for in-progress
- Red for errors

**Looks like Vercel:**
- Deployment status
- Preview URLs
- Logs available
- One-click actions

#### 2. Can Inspect Under the Hood

**View agent prompts:**
```
[Click on team card]
→ [⋮ Menu] → "View Agent Details"

Shows:
- Full AGENTS.md prompt
- Skills loaded
- Configuration
- Token usage breakdown
```

**View API calls:**
```
[⋮ Menu] → "View API Logs"

Shows:
- Timestamp
- Agent
- API endpoint
- Request payload (truncated)
- Response (truncated)
- Token count
- Cost
```

**Export conversation:**
```
[⋮ Menu] → "Export Conversation"

Downloads:
- conversation-business-planning.json
- Full conversation history
- Can replay in Claude Code manually
```

#### 3. Customization Options

**Edit team templates:**
```
Settings → Teams → Business Planning → Edit

Can modify:
- Agent system prompts
- Skills included
- Budget limits
- Phase definitions
- Approval requirements
```

**Add custom scenarios:**
```
Project → Scenarios → Add New

Create custom validation scenarios
Teams will test against these
```

**Create new agent types:**
```
Settings → Teams → Create Custom Team

Define:
- Agent roster
- Orchestration rules
- Required skills
- Cost estimates
```

#### 4. CLI Still Available

**For power users:**
```bash
# Check status
sforza status

# Output:
MealPlan AI
  Business Planning: Phase 3/4 (85%)
  Research: Complete
  Content Creation: Phase 2/4 (78%)

# View logs
sforza logs business-planning

# Approve decision
sforza approve decision-positioning-123

# Export deliverables
sforza export --format zip

# Start team manually
sforza start web-app-development
```

---

## Realistic Build Plan

### Phase 1: Minimum Viable Daemon (3 months, $50K)

**Goal:** Desktop app that manages agent sessions with basic orchestration.

#### What You Get

✅ **Desktop app (macOS only initially)**
- Electron shell
- React dashboard UI
- Runs locally on user's computer

✅ **Basic team management**
- Manual team launch (user clicks to start each team)
- Can't auto-spawn yet
- One team at a time or parallel if user opens multiple

✅ **Dashboard**
- Team status cards
- Progress indicators
- Budget tracking
- File browser for deliverables

✅ **Approval flow**
- Notifications when decisions needed
- Modal dialogs for approvals
- Context provided inline

✅ **File organization**
- Automatic workspace creation
- Deliverables organized by team
- Built-in PDF/image viewer
- Export/download/share capabilities

✅ **Budget tracking**
- Real-time cost calculation
- Alerts at 80% of budget
- Require approval before exceeding

✅ **Basic notifications**
- Desktop notifications (macOS Notification Center)
- Email notifications
- In-app notification center

#### What's NOT Yet

❌ Automatic agent spawning (user launches teams manually)
❌ Cross-platform (Windows/Linux come later)
❌ Web version
❌ Mobile app
❌ Multi-user collaboration
❌ Advanced orchestration (agents spawning sub-agents)
❌ 24/7 background operation (daemon runs only when app open)

#### Tech Stack

**Frontend:**
- Electron (app shell)
- React 18 + TypeScript
- Tailwind CSS (styling)
- Recharts (progress visualizations)
- React PDF Viewer (deliverable previews)

**Backend (Daemon):**
- Python 3.11
- SQLite (state persistence)
- Anthropic SDK (API client)
- Redis Lite (in-memory message queue)
- FastAPI (IPC with Electron)

**Infrastructure:**
- No cloud hosting (all local)
- GitHub for version control
- GitHub Actions for builds
- Notarization for macOS (Apple requirement)

#### Team

**1 Full-Stack Developer** ($35/hour, full-time, 3 months)
- Electron app structure
- React dashboard UI
- Python daemon logic
- API integration
- **Cost:** ~$18K

**1 Designer** ($50/hour, part-time 20 hours/week, 3 months)
- UI/UX design
- Component design system
- Icon set
- **Cost:** ~$12K

**1 Technical Writer** ($40/hour, part-time 10 hours/week, 6 weeks)
- User documentation
- Setup guides
- Troubleshooting docs
- **Cost:** ~$2.4K

**Misc expenses:**
- Apple Developer account: $99/year
- Hosting for marketing site: $20/month
- Testing devices: $1K
- Buffer (15%): ~$5K

**Total:** ~$50K

#### Timeline

**Week 1-4:** Architecture & Foundation
- Electron app structure
- Python daemon skeleton
- Basic IPC between frontend/backend
- SQLite database schema
- API client wrapper

**Week 5-8:** Core Features
- Dashboard UI components
- Team launch workflow
- Agent lifecycle management
- Real-time status updates
- Budget tracking

**Week 9-10:** Approvals & Notifications
- Decision approval flow
- Notification system
- Context display for decisions

**Week 11-12:** File Management & Deliverables
- Workspace organization
- File browser
- PDF/image preview
- Export/share capabilities

**Week 13:** Polish & Testing
- Bug fixes
- Performance optimization
- User acceptance testing
- Documentation

**Week 13-14:** Beta Release
- Limited beta (50 users)
- Gather feedback
- Iterate

---

### Phase 2: Full v2.0 Vision (Additional 3 months, +$70K)

**Goal:** Full-featured orchestration daemon with advanced capabilities.

#### Additional Features

✅ **Automatic agent spawning**
- Orchestrator can launch new agents programmatically
- Agents can spawn sub-agents
- Dynamic team scaling

✅ **Cross-platform**
- Windows support
- Linux support
- Platform-specific installers

✅ **Advanced orchestration**
- Hierarchical teams (teams spawn sub-teams)
- Agent-to-agent negotiation
- Conditional workflows (if-then logic)
- Dynamic agent recruitment mid-session

✅ **Web version (optional)**
- Access dashboard from browser
- Same features as desktop
- Syncs with desktop app

✅ **Mobile notifications**
- iOS/Android push notifications
- Quick approvals from phone
- Mobile-optimized approval interface

✅ **Multi-user collaboration**
- Invite co-founders to project
- Role-based approvals (CEO approves strategy, CTO approves tech)
- Comments and feedback on deliverables

✅ **Template marketplace**
- Community-contributed team templates
- One-click installation
- Rating and reviews

✅ **Enhanced analytics**
- Team performance metrics
- Cost efficiency analysis
- Quality scoring for deliverables
- Historical trends

✅ **Better state management**
- Full conversation replay
- Time-travel debugging
- Checkpoint/restore
- Branch from past states

#### Additional Team

**+1 Full-Stack Developer** ($35/hour, full-time, 3 months): ~$18K
**+1 DevOps Engineer** ($40/hour, part-time 20 hours/week, 3 months): ~$10K
**+1 Mobile Developer** ($40/hour, part-time 20 hours/week, 2 months): ~$6K
**Infrastructure costs** (hosting for web version): ~$2K
**Testing & QA**: ~$5K
**Buffer (15%)**: ~$6K

**Additional Total:** ~$70K

#### Full v2.0 Total

**Phase 1 + Phase 2:** ~$120K over 6 months

**Team size at peak:** 4-5 people (1 full-time, 3-4 part-time)

---

### Phase 3: SaaS Option (Alternative to Desktop)

**If you want to go the hosted SaaS route instead:**

**6 months, $150K**

Includes:
- Web app (Next.js)
- Backend API (Node.js/Python)
- Database (PostgreSQL)
- Message queue (Redis)
- Worker pool for agents
- Object storage (S3)
- User authentication
- Billing integration (Stripe)
- Multi-tenancy
- Security hardening
- DevOps/infrastructure
- Ongoing hosting ($3-5K/month)

**Trade-offs:**
- More expensive to build
- Ongoing operational costs
- But: More user-friendly (no installation)
- And: Can monetize via subscription

---

## Honest Assessment

### Is This Feasible?

**Yes, absolutely.**

This is very similar in complexity to:
- **Cursor** (AI code editor with background daemon)
- **Raycast** (command bar with extensions and background sync)
- **Linear** (project management with real-time coordination)
- **Notion** (docs + database with sync engine)

All of these are successful products built by small teams.

### Is It Hard?

**Moderate difficulty.**

**Hard parts:**
1. Managing multiple concurrent API conversations without conflicts
2. State synchronization between agents (who knows what, when)
3. UX for complex approval flows (showing enough context without overwhelming)
4. Cost tracking and prediction (accurate token counting)
5. Robust error handling (agent failures, API timeouts, network issues)

**Easier parts:**
1. Desktop app shell (Electron is mature, well-documented)
2. Dashboard UI (React patterns are well-established)
3. File management (standard filesystem operations)
4. Anthropic API integration (SDK is clean and reliable)
5. Basic notifications (OS notification centers work well)

**Comparable to:**
- Building a real-time chat app (similar state sync challenges)
- Building a CI/CD dashboard (similar status tracking)
- Building a desktop IDE (similar file management)

**Definitely easier than:**
- Building a real-time multiplayer game (harder sync)
- Building a video editor (harder media processing)
- Building a compiler (harder algorithms)

### Would People Use It?

**100% yes, for the right users.**

#### ✅ Perfect For:

**Solo founders building startups**
- Want a complete business, not just code
- Willing to pay $500-1K to get to market faster
- Value professional quality outputs
- Don't have time to manage contractors

**Small agencies running client projects**
- Can charge clients $5-10K for "business setup"
- Use Sforza to deliver in days, not weeks
- Still profitable at $1K internal cost
- Can serve 5-10 clients/month

**Product managers prototyping ideas**
- Need to validate ideas quickly
- Want working MVPs to show stakeholders
- Budget for exploration phase
- Prefer AI agents to offshore devs

**Junior devs learning to build**
- See professional-quality work
- Learn architecture patterns
- Understand business strategy
- Can inspect and modify

#### ❌ NOT For:

**People who want to code themselves**
- Hands-on developers
- Enjoy the building process
- This removes the fun part for them

**Teams with established workflows**
- Already have contractors/employees
- Existing project management
- Don't need more tools

**Enterprise (initially)**
- Need compliance/security guarantees
- Require on-prem deployment
- Want SLAs and support
- (But: Good market for v3.0)

**People with <$500 budget**
- Free/cheap tools exist
- Sforza is premium
- Better for them: Learn Claude Code manually

### What's the Killer Feature?

**The ability to say "build me a SaaS business" on Monday morning, review decisions on your phone during lunch, and have a deployed MVP by Friday.**

**That's not possible today without:**
- Hiring developers ($10K+ and weeks of coordination)
- Learning to code yourself (months of learning)
- Using low-code tools (limited functionality)

**Sforza makes it possible for $500-1K and 5-10 hours of your time.**

**That's the value proposition.**

### Realistic Market Size

**Total Addressable Market (TAM):**
- Solo founders with tech ideas: ~500K globally
- Small agencies: ~100K globally
- Product managers at companies: ~1M globally
- **Total:** ~1.6M potential users

**Serviceable Addressable Market (SAM):**
- Those with budget for AI tools: ~400K (25% of TAM)
- Those building SaaS products: ~200K (50% of those)
- Those willing to pay $200-500/month: ~50K (25% of those)
- **Total:** ~50K realistic users

**Serviceable Obtainable Market (SOM):**
- Year 1 realistic: 500 users (1% of SAM)
- Year 2 with growth: 2,500 users (5% of SAM)
- Year 3 with maturity: 10,000 users (20% of SAM)

**Revenue potential (SaaS model at $49/month):**
- Year 1: 500 users × $49 = $24.5K/month = $294K/year
- Year 2: 2,500 users × $49 = $122.5K/month = $1.47M/year
- Year 3: 10,000 users × $49 = $490K/month = $5.88M/year

Plus usage-based revenue (20% markup on API costs):
- If avg user spends $200/month on API
- Sforza charges $240/month ($40 markup)
- Year 1: 500 × $40 = $20K/month = $240K/year
- Year 2: 2,500 × $40 = $100K/month = $1.2M/year
- Year 3: 10,000 × $40 = $400K/month = $4.8M/year

**Total Year 3 potential:** ~$10M ARR

### What Could Go Wrong?

**Technical risks:**
- Anthropic API changes breaking integration (mitigation: version pinning, adapter pattern)
- Claude performance degradation (mitigation: multi-model support)
- Cost explosion from poor token management (mitigation: strict budgets, monitoring)
- State corruption in daemon (mitigation: robust checkpointing, recovery)

**Market risks:**
- Anthropic launches competing product (mitigation: build defensible UX, community)
- AI gets so good people don't need orchestration (unlikely short-term)
- Market too small / unwilling to pay (mitigation: validate with beta early)

**Execution risks:**
- Underestimate complexity (mitigation: MVP with limited scope first)
- Can't hire right talent (mitigation: remote-first, competitive pay)
- Burn too much funding (mitigation: bootstrap, revenue from early users)

**Mitigation strategy:**
- Start with desktop MVP ($50K)
- Get 50 paying beta users ($5K MRR)
- Use revenue to fund v2.0
- Only raise funding if traction proven

### Bottom Line

**This is a real product that solves a real problem.**

The problem: Solo founders can't build complete businesses alone.
The solution: AI agent teams that do the work.
The moat: Excellent UX, orchestration, and community.

**It's technically feasible** (moderate difficulty, 3-6 months, $50-120K).

**It's commercially viable** (50K+ potential users, $10M+ ARR potential).

**It's defensible** (network effects from template marketplace, switching costs from project data).

**It should be built.**

And it starts with the desktop app MVP: 3 months, $50K, and a small team.

---

## Conclusion

The Orchestrator Daemon is the future of Sforza. It transforms the project from "interesting template library" to "complete business-building platform."

**v1.0 (current):** Manual orchestration, learn the patterns
**v2.0 (daemon):** Automated orchestration, production-ready
**v3.0 (future):** Autonomous operations, enterprise-ready

The path is clear. The technology is ready. The market is waiting.

**Let's build it.**
