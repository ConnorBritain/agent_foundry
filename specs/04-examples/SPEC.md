# Examples Section Specification

> **STATUS**: STATIC REFERENCE -- Extracted from master prompt. Never modified, only consulted.

## Purpose

Provide practical, end-to-end workflow examples demonstrating agent templates in action. These examples serve as both learning resources and starting points for users building their own workflows. Examples bridge the gap between abstract template specifications and real-world usage.

## Architecture Overview

```
examples/
├── README.md
├── single-agent-workflows/
│   ├── quick-script-example.md
│   ├── documentation-generation.md
│   └── code-review-workflow.md
└── multi-agent-workflows/
    ├── feature-implementation-flow.md
    ├── research-to-content-pipeline.md
    └── business-planning-session.md
```

## Single-Agent Workflow Examples

### 1. Quick Script Example (`quick-script-example.md`)

**Purpose**: Demonstrate the simplest possible agent workflow -- a single agent completing a focused coding task.

**Content Structure**:
- **Scenario**: User needs a utility script (e.g., CSV parser, file renamer, API client)
- **Setup**: Minimal AGENTS.md with language/framework context
- **Skills used**: file-search (to understand codebase), potentially test-generator
- **Execution**: Step-by-step walkthrough showing prompts and agent responses
- **Token usage**: Actual token counts at each step
- **Cost**: Total cost for the workflow
- **Time**: Wall-clock time from start to deliverable
- **Lessons**: What makes this work well, common pitfalls

**Key Demonstration Points**:
- How minimal AGENTS.md provides framework context
- When skills are triggered vs general knowledge used
- Cost-effectiveness of single-agent for simple tasks
- How to structure the initial prompt for best results

### 2. Documentation Generation (`documentation-generation.md`)

**Purpose**: Show a single agent generating comprehensive documentation from existing code.

**Content Structure**:
- **Scenario**: Generate API documentation, README, and inline comments for an existing project
- **Setup**: AGENTS.md with framework docs + documentation-writer skill
- **Skills used**: documentation-writer, file-search, api-docs-generator
- **Execution**: Multi-phase workflow (analyze -> outline -> draft -> polish)
- **Token usage**: Per-phase token counts
- **Cost**: Total cost broken down by phase
- **Quality**: How to validate generated documentation
- **Lessons**: When single-agent documentation works vs when a content team is needed

**Key Demonstration Points**:
- Progressive disclosure in action (skills loaded as needed)
- Documentation-writer skill trigger patterns
- AGENTS.md providing framework-specific documentation standards
- Output quality validation

### 3. Code Review Workflow (`code-review-workflow.md`)

**Purpose**: Demonstrate a structured code review using a single agent with the code-review skill.

**Content Structure**:
- **Scenario**: Review a pull request for quality, security, and style compliance
- **Setup**: AGENTS.md with framework docs + code-review skill + team style guide
- **Skills used**: code-review, file-search
- **Execution**: Structured review (security -> logic -> style -> performance)
- **Token usage**: Tokens consumed per review phase
- **Cost**: Total cost for review
- **Output format**: Structured review comments with severity levels
- **Lessons**: When single-agent review is sufficient vs when a Code Implementation Team reviewer is better

**Key Demonstration Points**:
- Code-review skill with high trigger reliability
- AGENTS.md providing team coding standards as passive context
- Structured output format for actionable feedback
- Comparison with multi-agent review quality

## Multi-Agent Workflow Examples

### 4. Feature Implementation Flow (`feature-implementation-flow.md`)

**Purpose**: Walk through a complete feature implementation using the Code Implementation Team template.

**Content Structure**:
- **Scenario**: Implement a user authentication feature (registration, login, password reset)
- **Team template**: Code Implementation Team (6 agents)
- **Framework**: Next.js with TypeScript (or configurable)
- **Execution phases**:
  1. Planning (Coordinator decomposes requirement)
  2. Parallel implementation (Specialist A: auth logic, Specialist B: UI components)
  3. Code review (Reviewer examines all changes)
  4. Testing (Test Engineer generates and runs tests)
  5. Documentation (Doc Writer creates API docs, updates README)
- **Coordination**: Show actual inter-agent handoffs and communication
- **Cost breakdown**: Per-agent, per-phase costs with model details
- **Deliverables**: Complete feature with tests and documentation
- **Lessons**: When to use full team vs reduced team, parallel vs sequential trade-offs

**Key Demonstration Points**:
- Multi-agent coordination in practice
- Branch-per-agent git strategy
- File lock manager preventing conflicts
- Coordinator decision-making (autonomous vs user-prompted)
- Scenario-based validation (Software Factory pattern)
- Cost vs quality vs speed trade-offs with actual numbers

### 5. Research-to-Content Pipeline (`research-to-content-pipeline.md`)

**Purpose**: Demonstrate chaining the Research Deep-Dive Team output into the Content Creation Team.

**Content Structure**:
- **Scenario**: Research a technical topic, then produce a publication-ready article
- **Phase 1 -- Research** (Research Team, market mode):
  1. Coordinator designs research study
  2. Literature Review Specialist gathers sources
  3. Data Analyst analyzes findings
  4. Synthesis Writer produces research report
- **Handoff**: Research report becomes input for Content Team
- **Phase 2 -- Content** (Content Creation Team):
  1. Coordinator/Editor sets content vision based on research
  2. Researcher validates/supplements with additional sources
  3. Drafter creates article from research findings
  4. Humanizer removes AI patterns, matches target voice
  5. Critic validates style guide compliance
  6. Fact-Checker validates claims against research sources
  7. Formatter prepares for publication platform
- **Cross-team coordination**: How research artifacts flow to content team
- **Cost breakdown**: Research phase cost + content phase cost
- **Deliverables**: Research report + publication-ready article
- **Lessons**: When to chain teams vs use a single larger team

**Key Demonstration Points**:
- Cross-team workflow orchestration
- Artifact-based handoff between teams
- Humanizer agent in action (before/after AI pattern removal)
- Progressive disclosure across team boundaries
- Total cost for multi-team workflow
- Quality improvement from research-backed content vs direct drafting

### 6. Business Planning Session (`business-planning-session.md`)

**Purpose**: Show the C-Suite Team creating a comprehensive business plan from a single idea.

**Content Structure**:
- **Scenario**: User has a SaaS business idea and needs a complete plan
- **Team template**: C-Suite (7 agents)
- **Execution phases**:
  1. CEO facilitates vision alignment meeting
  2. Parallel specialist deep-dives (all 6 specialists work simultaneously):
     - CFO: Financial model with P&L projections
     - CMO: Market sizing and competitive analysis
     - CTO: Technical architecture and build plan
     - COO: Org design and operational processes
     - VP Sales: Sales strategy and pipeline model
     - General Counsel: Entity structure and compliance
  3. CEO synthesizes integrated business plan
  4. Board review (all agents critique complete plan)
  5. Iteration to resolve conflicts
  6. Artifact generation
- **Coordination**: Show how specialists reference each others' work
- **Conflict resolution**: Show CEO resolving conflicting recommendations
- **Cost breakdown**: Per-agent costs, total session cost
- **Deliverables**: Complete business plan, financial model, pitch deck outline
- **Lessons**: ROI of comprehensive planning vs individual consultant sessions

**Key Demonstration Points**:
- Maximum parallelism with 7 agents
- Personality-driven diverse perspectives (CFO skepticism vs CMO optimism)
- Conflict resolution and synthesis
- Executable artifact generation
- Cost justification ($XX for comprehensive plan vs $XXX+ for human consultants)
- How artifacts feed into other team workflows (roadmap -> Code Implementation Team)

## README.md Content

The examples README should include:
- Overview of available examples
- Difficulty levels (beginner, intermediate, advanced)
- Prerequisites for each example
- How to adapt examples to your own use case
- Quick start: which example to try first
- Time and cost estimates for each example

```markdown
# Examples

| Example | Type | Difficulty | Est. Cost | Est. Time | Team Template |
|---------|------|-----------|-----------|-----------|---------------|
| Quick Script | Single-agent | Beginner | $0.50-2 | 5-15 min | None (standalone) |
| Documentation | Single-agent | Beginner | $2-5 | 15-30 min | None (standalone) |
| Code Review | Single-agent | Intermediate | $1-3 | 10-20 min | None (standalone) |
| Feature Implementation | Multi-agent | Intermediate | $10-30 | 30-60 min | Code Implementation |
| Research-to-Content | Multi-agent | Advanced | $20-50 | 1-2 hr | Research + Content |
| Business Planning | Multi-agent | Advanced | $30-80 | 1-3 hr | C-Suite |
```

## Writing Guidelines for All Examples

### Structure
- Every example follows the same template: Scenario, Setup, Execution, Cost, Deliverables, Lessons
- Include actual (or realistic estimated) token counts and costs
- Show representative prompts and agent responses
- Highlight decision points where user makes choices
- Include "what could go wrong" sections

### Quality
- Examples must be end-to-end (start to finish, no hand-waving)
- Include enough detail that a user can reproduce the workflow
- Show real trade-offs (cost vs quality vs speed)
- Reference which common layer templates and strategies are used
- Link to relevant strategy guides for deeper understanding

### Progression
- Single-agent examples build foundational understanding
- Multi-agent examples build on single-agent concepts
- Examples reference each other (e.g., "this uses the code-review skill from example 3")
- Advanced examples demonstrate concepts from multiple strategy guides

## Success Criteria

Examples are successful when:

- [ ] A new user can complete the Quick Script example in <15 minutes
- [ ] Cost estimates are within 30% of actual costs when users run the examples
- [ ] Examples demonstrate at least 3 strategy guide concepts each (multi-agent examples)
- [ ] Users can adapt examples to their own projects by changing configuration
- [ ] Each example has a clear "what you learned" summary
- [ ] Multi-agent examples clearly show the value over single-agent alternatives

## Cross-References

- **Master Prompt**: `specs/MASTER_PROMPT.md`
- **Common Layer**: `specs/01-common-layer/SPEC.md` (templates used in examples)
- **Teams Layer**: `specs/02-teams-layer/SPEC.md` (team templates used in multi-agent examples)
- **Strategies Layer**: `specs/03-strategies-layer/SPEC.md` (strategic concepts demonstrated)
- **Specific Strategy Guides**:
  - Decision Framework: `specs/03-strategies-layer/guides/decision-framework/SPEC.md`
  - Model Selection: `specs/03-strategies-layer/guides/model-selection/SPEC.md`
  - Optimization: `specs/03-strategies-layer/guides/optimization/SPEC.md`
  - Quality: `specs/03-strategies-layer/guides/quality/SPEC.md`
