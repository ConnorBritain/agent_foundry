# Multi-Agent Orchestration Protocol

This document defines the execution phases, communication protocols, quality gates, and decision-making framework for the C-Suite Team.

---

## Execution Modes

The team supports three execution modes. The mode is selected at runtime via the `--mode` flag.

### Sequential Mode

Agents execute one at a time in a defined order. Slowest but allows the user to review and adjust after each agent completes. Recommended for founders who want deep involvement.

```
CEO (Vision) → CFO → CMO → CTO → COO → VP Sales → General Counsel → CEO (Synthesis)
```

**Total time:** ~3-4 hours
**When to use:** First-time users, founders who want to steer each specialist's output, complex pivots where strategic direction may shift mid-process.

### Hybrid Mode (Recommended)

Agents execute in parallel within phases but sequentially across phases. Quality gates between phases ensure coherence. The CEO runs in Phase 1 and Phase 3-6, while all six specialists run in parallel in Phase 2.

```
Phase 1 (sequential): CEO defines vision and board brief
  ↓ [Quality Gate 1]
Phase 2 (parallel): CFO + CMO + CTO + COO + VP Sales + General Counsel
  ↓ [Quality Gate 2]
Phase 3 (sequential): CEO synthesizes specialist outputs
  ↓ [Quality Gate 3]
Phase 4 (parallel): All 7 agents in board review
  ↓ [Quality Gate 4]
Phase 5 (sequential): CEO resolves conflicts, iterates
  ↓ [Quality Gate 5]
Phase 6 (parallel): All specialists generate final artifacts
```

**Total time:** ~1.5-2 hours
**When to use:** Standard business planning. Best balance of speed, quality, and cross-functional coherence.

### Swarm Mode

All agents run concurrently with message-passing coordination. Fastest but requires the CEO to handle real-time conflict resolution. Experimental.

**Total time:** ~45-75 minutes
**When to use:** Experienced users, well-defined business models, time-critical planning (e.g., responding to a funding opportunity).
**Warning:** Higher risk of cross-functional inconsistencies and wasted tokens from retries.

---

## Phase Definitions

### Phase 1: Vision Alignment (Sequential -- ~15 minutes)

**Goal:** Establish strategic direction so all specialists work from the same foundation.

#### CEO / Strategy Lead
- Parse and validate the project configuration (`CONFIG.local.md`)
- Define the company vision, mission, and strategic priorities
- Identify the 3-5 key strategic questions the specialists must answer
- Write the board brief: a concise document that frames the business problem, target market, constraints, and success criteria
- Distribute the board brief to all specialists with specific questions for each
- Set the planning horizon and milestone definitions

**Outputs:**
- Board brief (distributed to all specialists)
- Strategic questions per specialist
- Planning parameters (horizon, milestones, constraints)
- Validated configuration

#### Quality Gate 1: Vision Checkpoint

| Check | Criteria | Blocking |
|-------|----------|----------|
| Config valid | All required fields populated, no contradictions | Yes |
| Vision defined | Mission, vision, and strategic priorities are clear | Yes |
| Board brief complete | All specialists have their assignments | Yes |
| Strategic questions assigned | Each specialist has 2-4 specific questions | Yes |
| Planning horizon set | Timeline and milestones defined | Yes |

**Pass criteria:** All checks pass. CEO proceeds to distribute board brief.

---

### Phase 2: Specialist Deep-Dives (Parallel -- ~25-40 minutes)

**Goal:** Each specialist produces their domain-specific analysis and recommendations based on the board brief.

#### CFO / Finance
- Build P&L projection (3-5 years, monthly for year 1)
- Create cash flow analysis with runway calculations
- Model cap table and dilution scenarios
- Calculate unit economics (CAC, LTV, payback period, contribution margin)
- Design hiring plan with fully-loaded salary bands
- Run sensitivity analysis on key assumptions
- Answer CEO's strategic finance questions

**Outputs:**
- Draft financial model (P&L, cash flow, cap table, unit economics)
- Funding requirements document
- Sensitivity analysis results
- Answers to CEO's finance questions

#### CMO / Marketing
- Calculate market sizing (TAM/SAM/SOM with methodology)
- Produce competitive landscape analysis (5+ direct, 3+ adjacent)
- Define customer segments with detailed personas
- Create positioning and messaging framework
- Design go-to-market strategy with channel priorities
- Allocate marketing budget with projected ROI per channel
- Answer CEO's strategic marketing questions

**Outputs:**
- Market analysis report (TAM/SAM/SOM, competitive landscape)
- Customer persona documents
- Positioning framework
- Go-to-market plan draft
- Answers to CEO's marketing questions

#### CTO / Product
- Define product roadmap (epics, features, dependencies, releases)
- Assess technical architecture and feasibility
- Conduct build vs buy analysis for key components
- Define MVP scope (what is in, what is out, and why)
- Identify technical hiring needs and skill requirements
- Recommend technology stack with rationale
- Answer CEO's strategic product/tech questions

**Outputs:**
- Product roadmap draft
- Technical architecture assessment
- Build vs buy analysis
- MVP specification
- Answers to CEO's product questions

#### COO / Operations
- Design org chart (current state and 6/12/24-month projections)
- Define roles with job descriptions and reporting structure
- Create process maps for key business workflows
- Design operational metrics dashboard
- Plan hiring sequence (who to hire first and why)
- Answer CEO's strategic operations questions

**Outputs:**
- Org chart drafts (current and projected)
- Role definitions
- Process maps
- Hiring sequence plan
- Answers to CEO's operations questions

#### VP Sales
- Define Ideal Customer Profile with firmographic and behavioral criteria
- Design sales process and stage definitions with exit criteria
- Build pipeline model with conversion rates per stage
- Create pricing strategy and discounting policy
- Design sales team structure and compensation plans
- Answer CEO's strategic sales questions

**Outputs:**
- ICP definition
- Sales process and pipeline model
- Pricing strategy draft
- Compensation design
- Answers to CEO's sales questions

#### General Counsel
- Recommend entity formation with rationale
- Create compliance checklist for target industry and geography
- Identify contract templates needed (priority-ranked)
- Develop IP strategy (patents, trademarks, trade secrets, copyright)
- Build compliance calendar
- Create risk register
- Answer CEO's strategic legal questions

**Outputs:**
- Entity formation recommendation
- Compliance checklist and calendar
- Contract template requirements
- IP strategy and risk register
- Answers to CEO's legal questions

#### Quality Gate 2: Specialist Output Checkpoint

| Check | Criteria | Blocking |
|-------|----------|----------|
| All specialists delivered | 6 specialist outputs received | Yes |
| Strategic questions answered | Each specialist answered CEO's questions | Yes |
| Financial model coherent | P&L, cash flow, and unit economics are internally consistent | Yes |
| Market sizing methodology | TAM/SAM/SOM uses bottom-up methodology | No |
| MVP defined | Clear scope with in/out decisions | Yes |
| Org chart matches budget | Hiring plan costs align with CFO projections | No |
| Legal entity recommended | Entity type selected with rationale | Yes |

**Pass criteria:** All blocking checks pass. Non-blocking issues flagged for Phase 4 board review.

---

### Phase 3: CEO Synthesis (Sequential -- ~15-20 minutes)

**Goal:** The CEO reads all specialist outputs, identifies conflicts, makes strategic trade-offs, and produces a coherent integrated plan.

#### CEO / Strategy Lead
- Read all 6 specialist outputs in full
- Identify cross-functional conflicts:
  - CMO marketing budget vs CFO cash flow constraints
  - CTO product timeline vs COO hiring sequence
  - VP Sales pricing strategy vs CFO unit economics
  - COO org chart vs CFO hiring budget
  - General Counsel entity recommendation vs CFO fundraising strategy
- Resolve conflicts by making binding strategic decisions
- Synthesize into an integrated business plan narrative
- Flag unresolvable conflicts for Phase 4 board review

**Outputs:**
- Integrated business plan draft
- Conflict resolution log with rationale
- Questions for Phase 4 board review (if any)
- Updated strategic priorities based on specialist inputs

#### Quality Gate 3: Synthesis Checkpoint

| Check | Criteria | Blocking |
|-------|----------|----------|
| All conflicts identified | CEO documented every cross-functional conflict | Yes |
| Conflicts resolved | Each conflict has a binding decision with rationale | Yes |
| Plan is internally consistent | Revenue matches pipeline, hiring matches budget, timeline matches roadmap | Yes |
| Unresolved items flagged | Any items requiring board review are explicitly listed | Yes |

---

### Phase 4: Board Review (Parallel -- ~15 minutes)

**Goal:** All specialists review the integrated plan and challenge assumptions, surface risks, and propose improvements.

#### All 7 Agents
- Each specialist reviews the CEO's integrated plan from their domain perspective
- Identify factual errors, unrealistic assumptions, or missing elements
- Propose specific improvements with justification
- Flag any remaining disagreements for escalation
- Confirm or challenge the CEO's conflict resolution decisions

**Outputs:**
- Board review comments from each specialist
- Proposed amendments (prioritized)
- Risk flags
- Confirmation or challenge of CEO decisions

#### Quality Gate 4: Board Review Checkpoint

| Check | Criteria | Blocking |
|-------|----------|----------|
| All specialists reviewed | 6 specialist reviews received | Yes |
| No factual errors | Any factual errors identified have been corrected | Yes |
| Assumptions realistic | No specialist flags an assumption as unrealistic without resolution | Yes |
| Risk register updated | New risks from board review are captured | No |

---

### Phase 5: Iteration and Resolution (Sequential -- ~10 minutes)

**Goal:** CEO addresses board review feedback, makes final decisions, and locks the plan.

#### CEO / Strategy Lead
- Review all board review comments
- Accept or reject proposed amendments with documented rationale
- Make final binding decisions on any remaining disagreements
- Escalate to user if fundamental strategic questions remain unresolved
- Lock the final plan version

**Outputs:**
- Final integrated business plan
- Amendment log (accepted/rejected with rationale)
- Escalation items (if any) for user decision

#### Quality Gate 5: Final Plan Checkpoint

| Check | Criteria | Blocking |
|-------|----------|----------|
| Plan locked | Final version of integrated plan is confirmed | Yes |
| Amendments addressed | All board review comments have CEO response | Yes |
| No open escalations | User-escalated items resolved or acknowledged | Yes |
| Numbers consistent | Financial projections match across all sections | Yes |

---

### Phase 6: Artifact Generation (Parallel -- ~20-30 minutes)

**Goal:** Each specialist produces their final deliverable artifacts based on the locked plan.

#### CFO / Finance
- Produce final financial model in Google Sheets
- Format P&L, cash flow, cap table, unit economics as separate sheets
- Create summary dashboard sheet
- Generate funding requirements one-pager

#### CMO / Marketing
- Produce go-to-market plan in Notion
- Format competitive landscape map
- Create content calendar and campaign briefs
- Write customer persona documents

#### CTO / Product
- Produce product roadmap (Linear if configured, otherwise Notion)
- Write MVP specification document
- Create technical architecture summary
- Document build vs buy decisions

#### COO / Operations
- Produce org chart (current and projected)
- Write role definitions with job descriptions
- Create process map documents
- Design operational metrics dashboard

#### VP Sales
- Produce sales playbook in Notion
- Write pricing strategy document
- Create pipeline model
- Generate outreach templates and objection handling matrix

#### General Counsel
- Produce compliance checklist and calendar in Notion
- Write entity formation recommendation
- Create contract template requirements list
- Finalize IP strategy document and risk register

#### CEO / Strategy Lead
- Write executive summary (1-page)
- Produce pitch deck outline (Google Slides if configured)
- Create the final strategic recommendations document
- Compile cross-references between all artifacts

#### Quality Gate 6: Artifact Checkpoint

| Check | Criteria | Blocking |
|-------|----------|----------|
| All artifacts produced | Every enabled output in CONFIG has a deliverable | Yes |
| No placeholder text | All sections contain real content, not "TBD" | Yes |
| Numbers match | Financial figures in pitch deck match financial model | Yes |
| Cross-references valid | Links between documents are correct | No |
| Format correct | Each artifact is in the correct tool (Sheets, Notion, Linear) | Yes |

---

## Communication Protocol

### Message Types

Agents communicate using structured messages with the following types:

| Type | Purpose | Example |
|------|---------|---------|
| `BRIEF` | CEO distributes strategic context | CEO sends board brief to all specialists |
| `ANALYSIS` | Specialist delivers domain output | CFO delivers financial model draft |
| `CONFLICT` | Flag a cross-functional disagreement | CMO budget request conflicts with CFO runway |
| `RESOLUTION` | CEO resolves a conflict | CEO decides marketing budget is $200K, not $500K |
| `REVIEW` | Board review comment on integrated plan | CTO challenges revenue timeline assumptions |
| `AMENDMENT` | Proposed change to integrated plan | VP Sales proposes adjusted pricing tiers |
| `ESCALATE` | Escalate to user for decision | CEO escalates fundamental business model question |
| `ARTIFACT` | Deliver final formatted output | CFO delivers Google Sheets financial model |

### Message Format

```yaml
type: BRIEF
from: ceo
to: all
phase: 1
priority: high
subject: "Board Brief: Strategic Planning Session"
body: |
  Business: [name]
  Problem: [problem statement]
  Target Market: [market definition]
  Constraints: [financial, timeline, team]

  Strategic questions for each specialist:
  - CFO: What is the minimum viable funding to reach profitability?
  - CMO: What is the fastest channel to first 100 customers?
  - CTO: What is the smallest MVP that tests our core hypothesis?
  - COO: What is the minimum team to execute the 90-day plan?
  - VP Sales: What pricing maximizes learning while generating revenue?
  - General Counsel: What entity structure supports our funding strategy?
deadline: "Phase 1 completion"
```

### Conflict Resolution

When specialists disagree on cross-functional matters:

1. Both specialists state their positions with data and rationale (max 300 words each)
2. The CEO evaluates both positions against strategic priorities and constraints
3. The CEO makes a binding decision and documents the rationale
4. Both specialists proceed with the CEO's decision
5. If the CEO determines the disagreement reflects a fundamental strategic question, it is escalated to the user

Common conflicts and resolution principles:
- **Budget conflicts (CMO vs CFO):** Default to CFO's runway constraints; CMO reallocates within approved budget
- **Timeline conflicts (CTO vs VP Sales):** Default to CTO's realistic estimate; VP Sales adjusts pipeline accordingly
- **Hiring conflicts (COO vs CFO):** Default to CFO's cash flow; COO reprioritizes hiring sequence
- **Pricing conflicts (VP Sales vs CFO):** Default to unit economics viability; VP Sales adjusts positioning

### Shared State

All agents have read access to:
- Project configuration (`CONFIG.local.md`)
- Board brief (Phase 1 output)
- Integrated plan (Phase 3 output)
- Conflict resolution log
- All specialist outputs from Phase 2

Write access is scoped per agent:
- CEO writes the integrated plan, executive summary, and conflict resolution log
- Each specialist writes only their domain-specific artifacts
- The financial model is owned by the CFO; other agents reference but do not modify it

---

## Autonomous vs User-Prompted Decisions

### Autonomous (No User Input Needed)

The team makes these decisions automatically:

- Document formatting and organization
- Financial model structure and layout
- Competitive analysis methodology
- Process map format and detail level
- Legal checklist organization
- Sales playbook structure
- Marketing plan format
- Artifact cross-referencing

### User-Prompted (Require User Input)

The team pauses and asks the user for:

- **Business model ambiguity** -- "Your description suggests both B2B and B2C. Which is primary?"
- **Fundamental strategic direction** -- "Market analysis suggests pivoting to enterprise. Proceed with original SMB focus or explore enterprise?"
- **Budget overrun** -- "Phase 2 specialist deep-dives are projected to exceed budget by 20%. Continue or reduce scope?"
- **Conflicting founder input** -- "CONFIG specifies SaaS but description implies a marketplace. Clarify business model."
- **Regulatory complexity** -- "Target market has significant regulatory requirements (HIPAA/GDPR). This adds 30% to legal and compliance work. Proceed?"
- **Missing critical information** -- "No competitor data provided. Should specialists research competitors or skip competitive analysis?"

### Escalation Triggers

The CEO escalates immediately when:

1. Two specialists produce fundamentally contradictory recommendations that reflect a strategic choice, not a coordination issue
2. Financial projections show the business is not viable under any reasonable scenario
3. Legal analysis reveals a regulatory barrier that requires a business model change
4. The integrated plan requires assumptions the user has not validated
5. Token budget is projected to exceed the configured maximum
6. A required MCP server integration is unavailable

---

## Scenario-Based Validation

After each phase, the CEO validates against the scenarios defined in `/scenarios/`. Each scenario specifies:

- **Preconditions:** Business context and configuration
- **Steps:** Phase-by-phase expected outputs
- **Expected outcomes:** What the integrated plan should contain
- **Consistency checks:** Cross-functional alignment requirements

Phase validation mapping:

| Phase | Scenarios Validated |
|-------|-------------------|
| Phase 1 | Vision clarity and strategic question quality |
| Phase 2 | Specialist output completeness and internal consistency |
| Phase 3 | Cross-functional alignment and conflict resolution quality |
| Phase 4 | Board review thoroughness and risk identification |
| Phase 5 | Final plan consistency and actionability |
| Phase 6 | Artifact completeness and format correctness |
