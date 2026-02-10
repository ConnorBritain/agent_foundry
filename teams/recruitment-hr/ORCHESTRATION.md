# Orchestration Plan -- Recruitment & HR Team

## Execution Overview

The team operates in four phases. Phase 1 is sequential because strategy must precede execution. Phases 2 through 4 run agents in parallel within each phase, with structured handoffs between phases.

**Total estimated duration:** ~2 hours 20 minutes
**Total estimated cost:** ~$78 (default configuration)

```
Phase 1: Foundation      ████████████░░░░░░░░░░░░░░░░░░░░  ~30 min  (Sequential)
Phase 2: Infrastructure  ░░░░░░░░░░░░████████████████░░░░░  ~45 min  (Parallel)
Phase 3: Execution       ░░░░░░░░░░░░░░░░░░░░░░░░████████  ~45 min  (Parallel)
Phase 4: Optimization    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░████  ~20 min  (Parallel)
```

---

## Phase 1: Foundation (Sequential -- ~30 minutes)

**Purpose:** Establish the strategic foundation that all subsequent work builds upon. Culture, values, and role frameworks must be defined before hiring infrastructure, onboarding, or performance systems can be designed coherently.

**Why sequential:** Each step in this phase depends on the output of the previous step. The Coordinator defines the people strategy, which the Culture & Engagement Specialist uses to articulate values, which the Performance Management Specialist uses to create role frameworks. Running these in parallel would produce disconnected outputs.

### Step 1.1: People Strategy (Coordinator)

**Duration:** ~12 minutes
**Input:** CONFIG.md (company context, headcount plan, culture preferences)

**Tasks:**
1. Analyze company stage, growth trajectory, and business model
2. Define people strategy pillars (e.g., "attract senior engineers," "build management bench," "establish remote-first culture")
3. Design organizational structure with reporting relationships
4. Create headcount plan with hiring priorities and timeline
5. Establish decision principles for people operations (e.g., "we hire for trajectory over credentials," "we default to transparency on compensation")
6. Define success metrics for the People function

**Output:** `deliverables/people-strategy.md`
```yaml
output:
  strategy_pillars: [3-5 strategic priorities]
  org_chart: [structure with reporting lines]
  headcount_plan: [roles, timeline, dependencies]
  decision_principles: [5-8 principles for people decisions]
  success_metrics: [measurable outcomes]
  culture_direction: [high-level culture intent for Step 1.2]
  role_framework_direction: [high-level role architecture for Step 1.3]
```

**Quality Gate:**
- Strategy aligns with business objectives stated in CONFIG
- Headcount plan is financially feasible given stated runway
- Decision principles are specific enough to resolve real disagreements

### Step 1.2: Values & Culture Design (Culture & Engagement)

**Duration:** ~10 minutes
**Input:** People strategy output from Step 1.1, CONFIG.md culture section

**Tasks:**
1. Transform high-level culture direction into 3-5 specific, observable values
2. For each value, define: what it looks like in practice, what it does NOT look like, how to hire for it, how to measure it
3. Design core team rituals (all-hands, retrospectives, celebrations, informal connection)
4. Establish communication norms (response times, meeting defaults, async expectations)
5. Define the psychological safety baseline -- what does a safe team look like here?

**Output:** `deliverables/culture-framework.md`
```yaml
output:
  values: [3-5 values with behavioral definitions]
  rituals: [list with purpose, cadence, facilitation guide]
  communication_norms: [documented expectations]
  psychological_safety_baseline: [definition and indicators]
```

**Quality Gate:**
- Values are specific and differentiated (could not belong to any random company)
- Each value has concrete behavioral examples, not just aspirational language
- Rituals have clear purpose tied to values or team health

### Step 1.3: Role Frameworks & Career Ladders (Performance Management)

**Duration:** ~10 minutes
**Input:** People strategy and org chart from Step 1.1, values from Step 1.2

**Tasks:**
1. Create role framework taxonomy (individual contributor vs. management tracks)
2. Define levels (e.g., Associate, Mid, Senior, Staff, Principal / Manager, Sr. Manager, Director, VP)
3. For each function identified in the headcount plan, create level descriptors covering: scope, complexity, autonomy, influence, technical skill, leadership
4. Establish criteria for advancement between levels
5. Create initial OKR framework connecting company objectives to team and individual goals

**Output:** `deliverables/role-frameworks.md`, `deliverables/career-ladders.md`
```yaml
output:
  level_definitions: [company-wide level framework]
  career_ladders: [per-function ladders with criteria]
  advancement_criteria: [what it takes to reach each level]
  okr_framework: [structure for goal alignment]
```

**Quality Gate:**
- Levels are clearly differentiated (you can tell which level someone is by reading their work)
- Advancement criteria are observable and measurable, not subjective
- IC and management tracks are valued equally
- OKR framework connects individual work to company objectives

### Phase 1 Handoff

Upon completion of all three steps, the following artifacts are available to Phase 2:

| Artifact | Produced By | Consumed By |
|----------|------------|-------------|
| People strategy | Coordinator | All agents |
| Org chart and headcount plan | Coordinator | Talent Acquisition, Compensation |
| Values and rituals | Culture & Engagement | Onboarding, Talent Acquisition |
| Role frameworks and levels | Performance Management | Talent Acquisition, Compensation |
| OKR framework | Performance Management | Onboarding |

---

## Phase 2: Hiring Infrastructure (Parallel -- ~45 minutes)

**Purpose:** Build the systems and materials needed to hire, onboard, and compensate employees. These three workstreams are independent enough to run in parallel, with defined interfaces.

**Why parallel:** Talent Acquisition needs role frameworks and salary bands (from Phase 1 and Compensation), but can begin job description drafting immediately. Onboarding can design the program structure while Compensation builds salary bands. Coordination happens through shared artifacts.

### Stream 2A: Hiring Playbook (Talent Acquisition)

**Duration:** ~45 minutes
**Input:** People strategy, headcount plan, role frameworks, values

**Tasks:**
1. Write job descriptions for all open roles (prioritized by urgency)
   - Include: role summary, responsibilities, success criteria (not just requirements), compensation range, culture pitch
   - Anti-pattern check: no "rockstar/ninja" language, no unrealistic requirement lists, no missing compensation info
2. Design structured interview process by role type:
   - Phone screen (30 min): culture and motivation screen
   - Technical/functional assessment (60 min): role-specific evaluation
   - Team interview (45 min): collaboration and values alignment
   - Final interview (30 min): leadership alignment and offer conversation
3. Create interview scorecards with behavioral indicators
   - Specific questions mapped to specific competencies
   - Scoring rubric (1-5) with anchor descriptions
   - Red flags and green flags for each competency
4. Build sourcing playbook:
   - Channel strategy by role type (referrals, LinkedIn, communities, events, job boards)
   - Outreach templates (initial, follow-up, re-engagement)
   - Diversity sourcing tactics
5. Create offer template with negotiation parameters
6. Design candidate experience (communication cadence, feedback timeline, rejection templates)

**Output:** `deliverables/hiring-playbook/`
```
hiring-playbook/
  job-descriptions/
    [role-name].md (one per open role)
  interview-guides/
    phone-screen.md
    technical-assessment.md
    team-interview.md
    final-interview.md
  scorecards/
    [role-type]-scorecard.md
  sourcing/
    sourcing-playbook.md
    outreach-templates.md
  offers/
    offer-template.md
    negotiation-guide.md
  candidate-experience/
    communication-cadence.md
    rejection-templates.md
```

### Stream 2B: Onboarding Program (Onboarding & Enablement)

**Duration:** ~40 minutes
**Input:** People strategy, values, role frameworks, OKR framework

**Tasks:**
1. Design pre-boarding experience (offer acceptance to Day 1):
   - Welcome email sequence
   - Equipment and access provisioning checklist
   - Pre-reading materials (culture doc, team wiki, product overview)
   - Buddy assignment and introduction
2. Create Day 1 plan:
   - Morning: Welcome, workspace setup, team introduction
   - Midday: Lunch with buddy (virtual or in-person)
   - Afternoon: Tools walkthrough, first small task, end-of-day check-in
   - Goal: New hire goes home feeling "I made the right choice"
3. Design Week 1 plan:
   - Daily structure with learning blocks and social time
   - Key meetings: manager 1:1, skip-level intro, team standup
   - First deliverable (something small but real -- not a toy project)
   - End-of-week reflection and feedback
4. Create Month 1 milestone plan:
   - Week-by-week expectations with increasing scope
   - Bi-weekly check-ins with manager
   - First OKR draft (aligned with OKR framework)
   - Onboarding survey at Day 30
5. Design Quarter 1 ramp plan:
   - Month 2: Independent contribution, deeper relationships, first feedback cycle
   - Month 3: Full productivity target, peer feedback, development plan draft
   - 90-day review format
6. Build buddy program:
   - Buddy selection criteria and matching matrix
   - Buddy responsibilities and time commitment
   - Conversation guides for buddy check-ins
7. Create role-specific training paths:
   - Engineering: codebase tour, architecture overview, deployment process, on-call rotation
   - Sales: product training, demo certification, CRM workflow, shadowing schedule
   - General: tools, processes, communication norms, culture orientation

**Output:** `deliverables/onboarding-program/`
```
onboarding-program/
  pre-boarding-checklist.md
  day-1-plan.md
  week-1-plan.md
  month-1-milestones.md
  quarter-1-ramp.md
  buddy-program-guide.md
  training-paths/
    engineering.md
    sales.md
    general.md
  surveys/
    day-30-survey.md
    day-90-survey.md
```

### Stream 2C: Compensation & Benefits (Compensation & Benefits Analyst)

**Duration:** ~35 minutes
**Input:** People strategy, role frameworks, career ladders, CONFIG compensation section

**Tasks:**
1. Build salary bands for all roles and levels:
   - Base salary range (min, mid, max) per level
   - Geographic adjustments if applicable
   - Band overlap between levels (typically 10-15%)
   - Placement guidelines for new hires vs. promotions
2. Design equity compensation guidelines:
   - Grant ranges by level
   - Vesting schedule and cliff details
   - Refresh grant policy
   - Equity value communication (how to explain equity to candidates)
3. Select and design benefits package:
   - Health insurance (medical, dental, vision)
   - Retirement (401k, match percentage)
   - Paid time off (vacation, sick, parental, bereavement)
   - Professional development budget
   - Home office stipend (if remote/hybrid)
   - Wellness benefits
   - Other perks aligned with culture and stage
4. Conduct pay equity analysis framework:
   - Methodology for detecting pay gaps
   - Correction process and timeline
   - Ongoing audit schedule
5. Create total rewards statement template:
   - Base salary + equity + benefits + perks = total compensation
   - Visual format for candidate offers and employee communication
6. Model compensation budget:
   - Current headcount cost
   - Projected cost at target headcount
   - Merit increase budget (typically 3-5% annually)
   - Promotion budget (typically 1-2% of payroll)

**Output:** `deliverables/compensation-package/`
```
compensation-package/
  salary-bands.md
  equity-guidelines.md
  benefits-package.md
  pay-equity-framework.md
  total-rewards-template.md
  compensation-budget-model.md
```

### Phase 2 Handoff

| Artifact | Produced By | Consumed By |
|----------|------------|-------------|
| Job descriptions | Talent Acquisition | Used in Phase 3 sourcing |
| Interview guides | Talent Acquisition | Used in Phase 3 interviews |
| Salary bands | Compensation & Benefits | Talent Acquisition (offers) |
| Onboarding plans | Onboarding & Enablement | Used in Phase 3 execution |
| Benefits package | Compensation & Benefits | Talent Acquisition (selling the opportunity) |

---

## Phase 3: Process Execution (Parallel -- ~45 minutes)

**Purpose:** Put the infrastructure to work. Source candidates, execute onboarding for any new hires, launch culture programs, and activate performance systems.

**Why parallel:** Each agent operates within their domain using the infrastructure built in Phase 2. Coordination points are defined, but the work itself is independent.

### Stream 3A: Active Recruiting (Talent Acquisition)

**Duration:** ~45 minutes
**Input:** Hiring playbook, salary bands, benefits package

**Tasks:**
1. Execute sourcing strategy for highest-priority roles:
   - Identify target candidate pools
   - Draft personalized outreach for top 20 prospects
   - Design referral program activation message for current team
2. Create candidate pipeline tracking:
   - Pipeline stages (sourced, engaged, phone screen, interview, offer, accepted)
   - Stage conversion targets and velocity metrics
   - Weekly pipeline review template
3. Simulate interview calibration:
   - Sample candidate profiles for interview practice
   - Calibration exercise: all interviewers rate the same candidate independently
   - Discuss scoring discrepancies and align on standards
4. Draft offer packages for expected hires:
   - Pre-calculate salary + equity + benefits for likely levels
   - Prepare competing offer response strategy
   - Create exploding offer policy (or anti-policy: "we give you a week, no pressure tactics")
5. Design hiring manager kickoff template:
   - Role requirements discussion guide
   - Timeline and process alignment
   - Interview panel selection criteria

**Output:** `deliverables/recruiting-operations/`

### Stream 3B: Onboarding Execution (Onboarding & Enablement)

**Duration:** ~35 minutes
**Input:** Onboarding program, values documentation, OKR framework

**Tasks:**
1. Create onboarding execution playbook for hiring managers:
   - Pre-Day-1 checklist (accounts, equipment, buddy, calendar invites)
   - Day 1 facilitator guide
   - Week 1 daily check-in templates
   - Month 1 milestone tracking sheet
2. Build the welcome experience:
   - Welcome email templates (from CEO, from manager, from buddy)
   - First-day Slack/Teams introduction template
   - Virtual/physical welcome kit contents
3. Create manager onboarding toolkit:
   - How to write a good first-week plan
   - 1:1 question bank for new hire's first month
   - Common onboarding pitfalls and how to avoid them
4. Design self-service knowledge base structure:
   - Company overview and history
   - Product documentation
   - Process and tools guides
   - "Who to ask about what" directory

**Output:** `deliverables/onboarding-execution/`

### Stream 3C: Culture Launch (Culture & Engagement)

**Duration:** ~40 minutes
**Input:** Values documentation, team rituals, communication norms

**Tasks:**
1. Create values launch plan:
   - All-hands presentation introducing values with stories and examples
   - Values cards or digital assets for reference
   - Manager discussion guide for team-level values conversations
2. Launch team rituals:
   - Pilot schedule for first 4 weeks
   - Facilitation guides for each ritual
   - Feedback mechanism to iterate on rituals
3. Deploy engagement measurement:
   - eNPS survey instrument (baseline measurement)
   - Pulse survey design (5 questions, bi-weekly)
   - 1:1 sentiment questions for managers to use
4. Create feedback system:
   - Peer feedback templates and cadence
   - Upward feedback mechanism (anonymous or attributed)
   - Team retrospective format
5. Design recognition program:
   - Peer recognition channel/system
   - Values-linked recognition categories
   - Monthly/quarterly celebration format

**Output:** `deliverables/culture-launch/`

### Stream 3D: Performance Activation (Performance Management)

**Duration:** ~40 minutes
**Input:** Role frameworks, career ladders, OKR framework, values

**Tasks:**
1. Create OKR setting templates and guides:
   - Company OKR template
   - Team OKR template
   - Individual OKR template
   - OKR writing guide with good/bad examples
   - OKR scoring methodology
2. Design 1:1 meeting framework:
   - Recommended cadence and duration
   - Question bank organized by purpose (check-in, development, feedback, blockers)
   - 1:1 document template
   - Anti-patterns to avoid (status updates, monologues, skipping them)
3. Build review cycle:
   - Self-review template
   - Manager review template
   - Peer review template (optional, depending on company stage)
   - Review conversation guide
   - Calibration session design
4. Create development planning tools:
   - Individual development plan (IDP) template
   - Skill assessment matrix by role
   - Learning resource recommendations by skill area
5. Design PIP process (if needed):
   - When to use a PIP vs. other interventions
   - PIP template with clear expectations, support, and timeline
   - Documentation requirements
   - Exit process if PIP is not successful

**Output:** `deliverables/performance-system/`

### Phase 3 Handoff

| Artifact | Produced By | Consumed By |
|----------|------------|-------------|
| Pipeline metrics | Talent Acquisition | Coordinator (Phase 4) |
| Onboarding feedback | Onboarding & Enablement | All agents (Phase 4) |
| Engagement baseline | Culture & Engagement | Coordinator (Phase 4) |
| OKR completion data | Performance Management | Coordinator (Phase 4) |

---

## Phase 4: Optimization (Parallel -- ~20 minutes)

**Purpose:** Measure effectiveness, identify bottlenecks, and refine processes based on data and feedback from Phase 3.

### Stream 4A: System-Wide Analysis (Coordinator)

**Duration:** ~20 minutes
**Input:** All Phase 3 outputs, metrics, and feedback

**Tasks:**
1. Review hiring pipeline health:
   - Conversion rates by stage
   - Time-to-fill vs. target
   - Candidate experience scores
   - Source effectiveness
2. Assess onboarding effectiveness:
   - Day 30 and Day 90 survey scores
   - Time-to-first-contribution
   - New hire retention rate
   - Buddy program feedback
3. Evaluate culture program adoption:
   - Ritual attendance and engagement
   - eNPS baseline score
   - Feedback system usage rates
   - Recognition frequency
4. Check performance system health:
   - OKR completion rates
   - 1:1 cadence adherence
   - Review cycle participation
   - Career development plan completion
5. Identify cross-functional bottlenecks:
   - Where are handoffs breaking down?
   - Which processes are too slow, too complex, or being skipped?
   - What feedback are we getting from managers and employees?
6. Produce adjustment recommendations:
   - Strategy modifications
   - Process simplifications
   - Resource reallocation
   - Timeline adjustments

**Output:** `deliverables/optimization-report.md`

### Stream 4B: Agent-Specific Refinements (All Specialists)

**Duration:** ~15 minutes (parallel with Stream 4A)
**Input:** Phase 3 outputs, coordinator feedback

**Tasks (per agent):**
1. Review own deliverables against quality criteria
2. Incorporate feedback from Phase 3 execution
3. Update templates and guides based on lessons learned
4. Identify automation opportunities
5. Create maintenance schedule for ongoing processes

**Output:** Updated deliverables with version notes

---

## Execution Modes

### Full Execution (Default)
Run all four phases sequentially. Best for greenfield People operations or major overhauls.
- Duration: ~2 hours 20 minutes
- Cost: ~$78

### Foundation Only
Run Phase 1 only. Best when you need strategy and frameworks but will build infrastructure yourself.
- Duration: ~30 minutes
- Cost: ~$15

### Hiring Sprint
Run Phase 1 (foundation), then Phase 2 Stream 2A (hiring playbook) and 2C (compensation). Skip onboarding, culture, and performance. Best when you need to hire urgently.
- Duration: ~1 hour 15 minutes
- Cost: ~$45

### Culture Reset
Run Phase 1 (foundation), then Phase 2 Stream 2B (onboarding) and Phase 3 Stream 3C (culture launch). Best after a crisis, layoff, or cultural drift.
- Duration: ~1 hour 15 minutes
- Cost: ~$40

### Performance Overhaul
Run Phase 1 Step 1.3 (role frameworks), then Phase 3 Stream 3D (performance activation). Best when culture and hiring are healthy but performance management is broken.
- Duration: ~50 minutes
- Cost: ~$25

---

## Git Strategy

### Branch Structure
```
main
  └── people-ops/foundation
  └── people-ops/hiring-infrastructure
  └── people-ops/onboarding-program
  └── people-ops/culture-framework
  └── people-ops/performance-system
  └── people-ops/compensation-package
  └── people-ops/optimization
```

### Commit Convention
```
feat(people): add people strategy and org design
feat(hiring): create job descriptions for Q1 roles
feat(onboarding): design day-1 through quarter-1 plans
feat(culture): define values and team rituals
feat(performance): create OKR framework and career ladders
feat(comp): build salary bands and equity guidelines
fix(hiring): adjust interview scorecard based on calibration
docs(people): add optimization report and recommendations
```

### Review Process
1. Each agent commits to its own branch
2. Coordinator reviews all branches before merge
3. Cross-functional dependencies trigger review by affected agents
4. Final merge to main after all quality gates pass

---

## Communication Protocol

### Message Format
```yaml
message:
  from: [agent_name]
  to: [agent_name | "all"]
  type: [deliverable | question | decision_request | status_update | escalation]
  priority: [high | normal | low]
  subject: [one-line summary]
  body: [content]
  needs_response_by: [phase_step or "end_of_phase"]
```

### Escalation Rules
1. **Immediate escalation to Coordinator:**
   - Conflicting requirements between agents
   - Decisions affecting multiple domains
   - Budget or timeline concerns
   - Anything involving individual people decisions

2. **Direct agent-to-agent communication:**
   - Data sharing within established interfaces
   - Clarifying questions about deliverables
   - Status updates on shared dependencies

---

## Scenario Validation

Before executing any phase, validate the scenario against these criteria:

### Go/No-Go Checklist
- [ ] CONFIG.md is fully populated with no placeholder values
- [ ] Company stage and headcount numbers are realistic
- [ ] Values section contains specific behavioral descriptions, not generic platitudes
- [ ] Compensation philosophy is consistent with company stage and funding
- [ ] Tool selections reflect actual or planned subscriptions
- [ ] Open roles are prioritized and have clear urgency levels
- [ ] Constraints and out-of-scope items are documented

### Decision Criteria for Phase Transitions
| Transition | Criteria |
|-----------|---------|
| Phase 1 to Phase 2 | All Phase 1 quality gates pass. Coordinator approves strategy. |
| Phase 2 to Phase 3 | Infrastructure deliverables reviewed by Coordinator. Salary bands and job descriptions are internally consistent. |
| Phase 3 to Phase 4 | At least one execution cycle completed. Baseline metrics collected. |
| Phase 4 to Complete | Optimization report reviewed. Action items assigned. Maintenance schedule defined. |
