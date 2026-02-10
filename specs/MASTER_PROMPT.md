# Agent Foundry

> Where agent teams are forged

An open-source operating system for building and running businesses with coordinated
AI agent teams. From high-level strategy to deployed applications—all orchestrated
by specialized agents working in parallel.

## Context & Research Foundation

I've researched agent steering approaches including Skills, AGENTS.md, and MCP patterns. Key findings from my analysis:

### Critical Research Links
- **Vercel's Eval Study**: https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals
  - AGENTS.md achieved 100% pass rate vs Skills at 79% (with explicit instructions)
  - Skills failed to trigger in 56% of cases without explicit prompting
  - Passive context beats active retrieval for framework knowledge

- **Agent Skills Specification**: https://agentskills.io/specification
  - Official spec from Anthropic for portable skill definitions
  - Progressive disclosure: metadata → instructions → resources
  - Best for vertical, action-specific workflows

- **OpenAI Skills Examples**:
  - https://github.com/openai/skills/blob/main/skills/.curated/openai-docs/SKILL.md
  - https://github.com/openai/skills/blob/main/skills/.curated/figma-implement-design/SKILL.md
  
- **Microsoft Playwright CLI + Skills**: https://github.com/microsoft/playwright-cli/blob/main/skills/playwright-cli/SKILL.md
  - Explicitly favors CLI + Skills over MCP for token efficiency
  - Demonstrates reference-based architecture

- **Claude Code Agent Teams**: https://code.claude.com/docs/en/agent-teams
  - Official guidance on multi-agent orchestration

- **Additional Context**:
  - VSCode multi-agent dev: https://code.visualstudio.com/blogs/2026/02/05/multi-agent-development
  - LangChain agent builder: https://www.blog.langchain.com/introducing-agent-builder-template-library/
  - **StrongDM Software Factory**: https://simonwillison.net/2026/Feb/7/software-factory/
    - Parallel agent swarms with scenario-based convergence
    - Code must not be reviewed by humans (scenarios as holdout sets)
    - Digital Twin Universe for unlimited testing
    - $1,000/day token spend for production software factory

## My Project Goals

I need a comprehensive **Agent Foundry** organized into three categorical levels:

### 1. **Common** - Universal Building Blocks
Foundational templates used across all agent implementations:

- **AGENTS.md Templates**
  - Compressed documentation index format (Vercel-style)
  - Framework-specific knowledge bases (Next.js, Python, etc.)
  - Domain knowledge templates (healthcare, finance, research, etc.)
  - Best practices for token optimization

- **SKILL.md Templates**
  - Standard workflow patterns (data gathering, synthesis, reporting)
  - File operations (read, transform, write)
  - API integration patterns (REST, GraphQL)
  - Testing and validation workflows

- **Universal Skills Library**
  - Skills that any agent might need regardless of use case
  - Examples: file-search, web-research, code-review, documentation-writer
  - Each with clear trigger descriptions and token budgets

### 2. **Teams** - Agent Cohort Templates
Pre-configured multi-agent teams for specific use cases. Each team template should include:

**Team Template Structure:**
```
teams/[team-name]/
├── README.md                    # Team specification & use case
├── TEAM_SPEC.md                # Detailed architecture
├── agents/
│   ├── coordinator/
│   │   ├── AGENTS.md
│   │   └── skills/
│   ├── specialist-1/
│   │   ├── AGENTS.md
│   │   └── skills/
│   └── specialist-2/
│       ├── AGENTS.md
│       └── skills/
├── cost-analysis.md            # Token usage & cost projections
└── deployment-guide.md         # Setup and execution instructions
```

**Required Documentation for Each Team:**
- **Use case description**: What problem does this team solve?
- **Agent roster**: Number and type of agent instances
- **Interaction patterns**: How agents coordinate (parallel, sequential, hierarchical)
- **Cost projections**: Per-hour estimates for Haiku/Sonnet/Opus
- **Token budget breakdown**: Context allocation per agent
- **Parallel execution strategies**: How to run efficiently
- **Success metrics**: How to measure team effectiveness

**Example Team Templates to Build:**
- **Research Synthesis Team**: Literature review + analysis + summarization
- **Code Implementation Team**: Planning + coding + testing + documentation
- **Project Coordination Team**: Status gathering + blocker identification + reporting
- **Data Pipeline Team**: Extraction + transformation + validation + loading
- **Content Creation Team**: Research + drafting + editing + formatting

### 3. **Strategies** - Conceptual Guides & Best Practices
Markdown documents explaining key concepts and decision frameworks:

- **Agent Harness Comparison**
  - Claude Code vs Kilo Code vs OpenClaw vs Cursor vs Windsurf
  - Feature matrices, cost models, use case fit
  - When to use each harness
  - Migration strategies between harnesses

- **Long-Running Agent Strategies**
  - Session management and state persistence
  - Context window management over time
  - Cost optimization for extended workflows
  - Error recovery and resumption patterns

- **Architecture Decision Frameworks**
  - AGENTS.md vs Skills vs MCP: Decision tree
  - Single agent vs team: When to parallelize
  - Synchronous vs asynchronous coordination
  - Token budget allocation strategies

- **Deployment Patterns**
  - Local development workflows
  - CI/CD integration for agent teams
  - Monitoring and observability
  - Version control for agent configurations

- **Optimization Techniques**
  - Context compression methods
  - Lazy loading patterns
  - Caching strategies for repeated operations
  - Batching and parallelization

- **Quality & Reliability**
  - Testing agent workflows
  - Validation and error handling
  - Skill trigger reliability improvements
  - Output quality measurement

## Key Design Constraints

Based on research findings:

### Token Budget Management
- **Passive context (AGENTS.md)**: ~8KB compressed for full framework docs
- **Skill metadata**: 50-100 tokens per skill
- **Skill body**: <5000 tokens when activated
- **Resources**: On-demand loading only

### Reliability Requirements
- Skills have 56% non-trigger rate without explicit instructions
- Instruction wording is fragile (small changes = big behavioral shifts)
- Passive context (AGENTS.md) provides 100% availability

### Architecture Patterns
1. **Horizontal knowledge** (framework APIs, broad docs) → AGENTS.md
2. **Vertical workflows** (specific tasks, triggered actions) → Skills
3. **Persistent tools/APIs** → MCP servers
4. **Hybrid is optimal** for complex systems

## What I Need From You

### 🚨 CRITICAL: Initial Setup (DO THIS FIRST)

Before building any templates, set up the orchestration infrastructure inspired by StrongDM's Software Factory pattern:

#### 1. Initialize Repository Structure

```bash
# Create orchestration infrastructure
git init
mkdir -p specs/{00-master,01-common,02-teams,03-strategies,04-examples}
mkdir -p logs/{active,archived}
mkdir -p shared-state/{locks,scenarios}
mkdir -p scenarios
```

#### 2. Create .gitignore

```gitignore
# Agent runtime state (don't commit, changes constantly)
/shared-state/agent-status.json
/shared-state/locks/
/shared-state/communication.md
/logs/active/
*.log

# Environment and secrets
.env
.env.local
**/.mcp-secrets/

# OS and IDE
.DS_Store
.vscode/
.idea/

# Dependencies
node_modules/
__pycache__/
*.pyc
venv/
.venv/

# Build outputs
dist/
build/
*.egg-info/
```

#### 3. Decompose This Prompt into /specs (Prevent Context Leak)

**Immediately after repository setup**, parse this entire prompt and create static reference specs:

```
specs/
├── 00-MASTER-CHECKLIST.md              # Top-level progress tracking
├── 01-common-layer/
│   ├── SPEC.md                         # Full requirements (STATIC)
│   ├── CHECKLIST.md                    # Progress tracking (UPDATED)
│   ├── personalities/SPEC.md
│   ├── agents-md-templates/SPEC.md
│   ├── skills/SPEC.md
│   └── utilities/SPEC.md
├── 02-teams-layer/
│   ├── SPEC.md
│   ├── CHECKLIST.md
│   ├── code-implementation/SPEC.md
│   ├── project-planning/SPEC.md
│   ├── content-creation/SPEC.md
│   ├── c-suite/SPEC.md
│   └── research-deep-dive/SPEC.md
├── 03-strategies-layer/
│   ├── SPEC.md
│   ├── CHECKLIST.md
│   └── guides/[each-guide]/SPEC.md
└── 04-examples/
    ├── SPEC.md
    └── CHECKLIST.md
```

**Purpose:**
- **SPEC.md files**: Static references extracted from this prompt - NEVER modified, only consulted
- **CHECKLIST.md files**: Actively updated with `[ ]` checkboxes as work progresses
- **Context leak prevention**: Reference specs instead of repeating this entire prompt

**Example CHECKLIST.md:**
```markdown
# Common Layer Progress

## Personalities (10 total)
- [x] skeptical-critic.md (2026-02-09 14:23)
- [x] cautious-analyst.md (2026-02-09 14:45)
- [ ] enthusiastic-supporter.md
- [ ] pragmatic-builder.md
...

## Token Budget
- Used: 45,234 tokens
- Estimated total: 500,000 tokens  
- Progress: 9%

## Estimated Completion
Based on current velocity: 2026-02-10 16:30
```

#### 4. Initialize Orchestration Files

Create these files for multi-agent coordination:

**`shared-state/agent-status.json`** (real-time agent tracking):
```json
{
  "last_updated": null,
  "agents": {},
  "team_metrics": {
    "total_agents": 0,
    "active": 0,
    "awaiting": 0,
    "offline": 0
  }
}
```

**`shared-state/communication.md`** (agent-to-agent messaging):
```markdown
# Agent Communication Log
Last updated: [timestamp]

## Active Messages (Auto-pruned every hour)

[No messages yet]

---

## Archived Messages (Last 24h)

[No archived messages]
```

**`shared-state/file-ownership.json`** (prevent write conflicts):
```json
{}
```

#### 5. Build Core Utilities FIRST

These enable multi-agent coordination:

**`common/utilities/file-lock-manager.py`**:
```python
#!/usr/bin/env python3
"""
File lock manager for parallel agent coordination.
Prevents write conflicts during multi-agent workflows.
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path

LOCK_FILE = "shared-state/file-ownership.json"
LOCK_DURATION = timedelta(minutes=30)

def acquire_lock(file_path: str, agent_name: str, reason: str = ""):
    """Attempt to acquire lock. Returns (success: bool, message: str)."""
    locks = _read_locks()
    
    if file_path in locks:
        lock = locks[file_path]
        lock_time = datetime.fromisoformat(lock["locked_until"])
        if lock_time > datetime.now():
            return False, f"Locked by {lock['owner']} until {lock_time}"
    
    locks[file_path] = {
        "owner": agent_name,
        "locked_until": (datetime.now() + LOCK_DURATION).isoformat(),
        "reason": reason
    }
    _write_locks(locks)
    return True, "Lock acquired"

def release_lock(file_path: str, agent_name: str):
    """Release lock. Returns True if successful."""
    locks = _read_locks()
    if file_path in locks and locks[file_path]["owner"] == agent_name:
        del locks[file_path]
        _write_locks(locks)
        return True
    return False

def check_lock(file_path: str) -> dict:
    """Check if file is locked. Returns lock info or None."""
    locks = _read_locks()
    return locks.get(file_path, None)

def _read_locks():
    if not os.path.exists(LOCK_FILE):
        return {}
    with open(LOCK_FILE) as f:
        return json.load(f)

def _write_locks(locks):
    os.makedirs(os.path.dirname(LOCK_FILE), exist_ok=True)
    with open(LOCK_FILE, 'w') as f:
        json.dump(locks, f, indent=2)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: file-lock-manager.py <acquire|release|check> <file_path> [agent_name] [reason]")
        sys.exit(1)
    
    cmd = sys.argv[1]
    if cmd == "acquire":
        success, msg = acquire_lock(sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else "")
        print(msg)
        sys.exit(0 if success else 1)
    elif cmd == "release":
        success = release_lock(sys.argv[2], sys.argv[3])
        sys.exit(0 if success else 1)
    elif cmd == "check":
        lock = check_lock(sys.argv[2])
        print(json.dumps(lock, indent=2) if lock else "Not locked")
```

**`common/utilities/status-updater.py`**:
```python
#!/usr/bin/env python3
"""Helper for agents to update their status."""

import json
import os
import sys
from datetime import datetime

STATUS_FILE = "shared-state/agent-status.json"

def update_status(agent_name: str, status: str, task: str, progress: str, blocked_by: str = None):
    """Update agent status. Status: active|awaiting|offline"""
    with open(STATUS_FILE, 'r') as f:
        data = json.load(f)
    
    data['agents'][agent_name] = {
        'status': status,
        'pid': os.environ.get('CLAUDE_SESSION_ID', 'unknown'),
        'current_task': task,
        'progress': progress,
        'last_heartbeat': datetime.now().isoformat(),
        'blocked_by': blocked_by
    }
    data['last_updated'] = datetime.now().isoformat()
    
    # Update metrics
    statuses = [a['status'] for a in data['agents'].values()]
    data['team_metrics'] = {
        'total_agents': len(data['agents']),
        'active': statuses.count('active'),
        'awaiting': statuses.count('awaiting'),
        'offline': statuses.count('offline')
    }
    
    with open(STATUS_FILE, 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: status-updater.py <agent_name> <status> <task> <progress> [blocked_by]")
        sys.exit(1)
    
    update_status(
        sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4],
        sys.argv[5] if len(sys.argv) > 5 else None
    )
```

---

Please help me build this comprehensive Agent Foundry:

### 1. Common Templates Layer

**A. Personality Library**

Create a reusable personality library at the top level that team templates can reference. This lives in `personalities/` and includes both pre-built personas and guidelines for customization.

**Structure:**
```
personalities/
├── README.md                          # Guide for using and customizing personalities
├── skeptical-critic.md                # Detail-oriented, constructive but firm
├── enthusiastic-supporter.md          # Positive, encouraging, momentum-focused
├── cautious-analyst.md                # Risk-aware, data-driven, conservative
├── pragmatic-builder.md               # Action-oriented, anti-bikeshedding, shipping-focused
├── strategic-visionary.md             # Long-term thinking, big-picture focused
├── detail-perfectionist.md            # Quality-obsessed, thoroughness over speed
├── customer-champion.md               # User-focused, empathy-driven, outcome-oriented
├── technical-purist.md                # Best practices, architectural integrity, tech debt aware
├── rapid-executor.md                  # Speed over perfection, iterative, bias to action
├── diplomatic-facilitator.md          # Conflict resolution, consensus-building, inclusive
└── customization-guide.md             # How to create your own personalities

Each personality file includes:
- Core traits and values
- Communication style
- Decision-making approach
- What triggers this personality (when to use)
- Example system prompt snippet
- Compatible team roles (where this works well)
```

**README.md Contents:**
```markdown
# Personality Library

Map of personalities to team templates and roles:

## Code Implementation Team
- **Coordinator**: Strategic Visionary + Pragmatic Builder
- **Implementation Specialists**: Pragmatic Builder
- **Code Reviewer**: Detail Perfectionist + Skeptical Critic
- **Test Engineer**: Cautious Analyst + Detail Perfectionist
- **Documentation Writer**: Customer Champion

## Project Planning Team
- **Coordinator**: Diplomatic Facilitator
- **Prioritization Agent**: Strategic Visionary + Cautious Analyst
- **Task Decomposer**: Detail Perfectionist

## Content Creation Team
- **Coordinator/Editor**: Skeptical Critic + Strategic Visionary
- **Humanizer**: Custom personality (see team-specific notes)
- **Critic**: Skeptical Critic + Detail Perfectionist

## C-Suite Team
- **CEO**: Strategic Visionary + Diplomatic Facilitator
- **CFO**: Cautious Analyst + Skeptical Critic
- **CMO**: Enthusiastic Supporter + Customer Champion
- **CTO**: Technical Purist + Pragmatic Builder
- **COO**: Detail Perfectionist + Rapid Executor

## Research Team
- **Coordinator**: Skeptical Critic + Strategic Visionary
- **Methodology Designer**: Technical Purist + Detail Perfectionist
- **Data Analyst**: Cautious Analyst

## How to Customize
See customization-guide.md for instructions on creating personalities specific
to your use case, industry, or organizational culture.
```

**B. AGENTS.md Template Collection**
Create reusable AGENTS.md templates for:

**Framework Knowledge Templates:**
- `framework-nextjs.md` - Compressed Next.js API index (Vercel-style pipe-delimited)
  - Includes: App Router, Server Components, Server Actions, caching APIs
  - Version-specific (Next.js 15, 14, 13)
  - Token budget: ~8KB compressed
  - "Prefer retrieval-led reasoning" instruction pattern included

- `framework-python-fastapi.md` - FastAPI documentation index
  - Includes: Routing, dependencies, async patterns, Pydantic models
  - Token budget: ~6KB compressed

- `framework-react.md` - React hooks, patterns, best practices
  - Token budget: ~7KB compressed

- `framework-typescript.md` - TypeScript patterns and type system
  - Token budget: ~5KB compressed

**Domain Knowledge Templates:**
- `domain-healthcare.md` - HIPAA compliance, medical terminology, healthcare workflows
  - Compliance requirements and constraints
  - Common healthcare data patterns (HL7, FHIR)
  - Token budget: ~10KB

- `domain-finance.md` - Financial regulations (SOC2, PCI-DSS), fintech patterns
  - Payment processing security
  - Financial data handling
  - Token budget: ~9KB

- `domain-research.md` - Academic standards, research methodologies, citation formats
  - Token budget: ~8KB

**Tool Integration Templates:**
- `tools-jira.md` - Jira API patterns, JQL syntax, common workflows
  - Issue creation, status transitions, linking
  - Token budget: ~5KB

- `tools-linear.md` - Linear API, project structure, workflow automation
  - Token budget: ~4KB

- `tools-notion.md` - Notion API, database operations, page creation
  - Token budget: ~6KB

- `tools-github.md` - GitHub API, PR workflows, Actions
  - Token budget: ~7KB

Each template should include:
- **Compression format**: Pipe-delimited index style
  ```
  [Framework Docs Index]|root: ./.framework-docs
  |IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning
  |01-routing:{pages.md,layouts.md,loading.md,error.md}
  |02-data-fetching:{server-components.md,server-actions.md,use-client.md}
  ```
- **Token budget estimate**: Actual measured tokens
- **When to use**: Decision criteria (AGENTS.md vs skill vs MCP)
- **Decompression script**: How to expand into full docs if needed

**C. Universal SKILL.md Templates**
Build skill templates for workflows any agent might need:

**File Operations:**
- `file-search/` - Search codebases, documentation, file systems
  - Trigger: "find files matching...", "search codebase for...", "locate implementation of..."
  - References: Search patterns, gitignore rules
  - Scripts: Recursive search with filtering
  - Token budget: ~3K loaded

- `file-transform/` - Batch file operations, format conversions
  - Trigger: "convert all X files to Y", "rename files matching..."
  - Scripts: Batch processing utilities
  - Token budget: ~2.5K loaded

**Research & Analysis:**
- `web-research/` - Structured web research with citation
  - Trigger: "research [topic]", "find latest information on..."
  - References: Search strategies, source evaluation criteria
  - Outputs: Cited findings in structured format
  - Token budget: ~4K loaded

- `data-synthesizer/` - Combine information from multiple sources
  - Trigger: "synthesize findings from...", "combine data from..."
  - References: Synthesis methodologies
  - Token budget: ~3.5K loaded

**Code Quality:**
- `code-review/` - Review code changes with quality checks
  - Trigger: "review this code", "check for issues in..."
  - References: Language-specific linters, security checklists
  - Scripts: Static analysis runners
  - Token budget: ~5K loaded

- `test-generator/` - Create test cases from requirements
  - Trigger: "generate tests for...", "create test coverage for..."
  - References: Testing patterns by framework
  - Scripts: Test template generators
  - Token budget: ~4K loaded

**Documentation:**
- `documentation-writer/` - Generate docs from code/specs
  - Trigger: "document this API", "create README for..."
  - References: Documentation templates, style guides
  - Token budget: ~3.5K loaded

- `api-docs-generator/` - Generate API reference documentation
  - Trigger: "generate API docs", "create reference for..."
  - Scripts: OpenAPI/Swagger generators
  - Token budget: ~4K loaded

**Project Management:**
- `status-reporter/` - Gather and format status updates
  - Trigger: "generate status report", "summarize progress on..."
  - References: Report templates by stakeholder type
  - Token budget: ~3K loaded

- `blocker-identifier/` - Identify dependencies and blockers
  - Trigger: "identify blockers for...", "what's blocking..."
  - References: Dependency analysis patterns
  - Token budget: ~2.5K loaded

Each skill should demonstrate:
- **Clear trigger description** (addressing the 56% non-trigger problem)
  - Multiple trigger patterns (not just one phrase)
  - Examples of when to use AND when NOT to use
  - Explicit boundaries to prevent false triggering

- **Progressive disclosure** with references/
  - Minimal SKILL.md body (<500 lines)
  - Detailed content in references/ loaded on-demand
  - Clear references to bundled resources

- **Token-efficient design** (<5000 tokens total when fully loaded)
  - Measured token counts included
  - Optimization notes (what was compressed/excluded)

- **Bundled scripts** where appropriate
  - Executable code in scripts/
  - Clear usage examples in SKILL.md
  - Error handling and edge cases documented

**D. Common Utilities**

Build practical utility scripts:

**token-calculator.py**
```python
"""
Calculate token usage for AGENTS.md files, skills, and team configurations.
Supports multiple tokenizers (claude, gpt, etc.)
"""
# Features:
# - Count tokens in a single file
# - Count tokens across a team configuration
# - Project costs based on model and token count
# - Compare compressed vs uncompressed formats
```

**skill-validator.py**
```python
"""
Validate SKILL.md files against agentskills.io specification.
"""
# Validates:
# - YAML frontmatter structure
# - Required fields (name, description)
# - Name format (lowercase, hyphens, max 64 chars)
# - Description length (max 1024 chars)
# - File references exist
# - No deeply nested references
```

**agents-md-compressor.py**
```python
"""
Compress documentation into pipe-delimited AGENTS.md format.
"""
# Features:
# - Scan directory of docs
# - Generate compressed index
# - Estimate token savings
# - Validate retrieval paths
# - Support for different doc structures (API ref, prose, code examples)
```

**cost-estimator.py**
```python
"""
Estimate costs for agent teams and workflows.
"""
# Features:
# - Input: team configuration, workflow description
# - Output: token projections per phase, total cost
# - Model comparison (Haiku/Sonnet/Opus)
# - Sensitivity analysis (what if token usage is 20% higher?)
```

Each utility should include:
- CLI interface with helpful flags
- Example usage in README
- Integration with team templates (how teams use these)
- Test suite to ensure accuracy

### 2. Team Templates Layer

Build **5 complete team templates** with full documentation. Each team should include configuration systems, personality definitions, model recommendations, and MCP server configs where applicable.

**Universal Team Template Structure:**
```
teams/[team-name]/
├── README.md                           # Overview, quick start, use cases
├── TEAM_SPEC.md                       # Detailed architecture and workflows
├── MODEL_CONFIGS.md                   # Team-specific model recommendations
├── cost-analysis.md                   # Token projections and $ estimates
├── deployment-guide.md                # Step-by-step setup and execution
├── ORCHESTRATION.md                   # Multi-agent coordination patterns
├── mcp-servers/                       # MCP server configurations
│   ├── [service-name].json
│   └── README.md                      # Setup prerequisites
├── agents/
│   ├── coordinator/
│   │   ├── AGENTS.md                  # Includes system prompt/personality
│   │   └── skills/
│   ├── specialist-1/
│   │   ├── AGENTS.md
│   │   └── skills/
│   └── [additional agents]/
├── scenarios/                         # Holdout test scenarios (Software Factory pattern)
│   ├── scenario-1.md
│   └── scenario-2.md
└── examples/
    ├── example-workflow-1.md
    └── example-workflow-2.md
```

**Each team's ORCHESTRATION.md includes:**

```markdown
# Multi-Agent Orchestration

## Execution Modes

### Sequential Mode (Budget-Conscious)
- Cost: $10-30
- Duration: 1-2 hours
- One agent at a time, user manages handoffs
- Best for: Learning, small tasks, tight budgets

### Hybrid Mode (Default - Recommended)
- Cost: $30-100
- Duration: 30-60 min
- Parallel where beneficial, sequential where needed
- Best for: Most production use cases

### Parallel Swarm Mode (Software Factory)
- Cost: $100-500
- Duration: 15-30 min
- All agents active, scenario-based convergence
- Best for: Rapid iteration, time-critical work

## Phase Breakdown

### Phase 1: [Phase Name] (Sequential/Parallel)
**Duration**: ~X min  
**Agents**: [list]  
**Deliverables**: [list]

**Workflow**:
1. [Step 1]
2. [Step 2]
...

**User Prompt at End**:
```
[Phase Name] complete.
- Deliverables: [list]
- Cost: $X.XX
- Quality: [metrics]

Next phase: [description]
- Estimated cost: $Y.YY
- Estimated duration: Zh

Proceed? (yes/no/review)
```

## Git Strategy

**Branch-per-agent pattern**:
```bash
main
├── agent/coordinator/setup
├── agent/impl-a/feature-x
├── agent/impl-b/feature-y
└── agent/test/scenarios
```

**Each agent**:
1. Works on dedicated branch
2. Pushes every 10-15 min
3. Checks file locks before editing
4. Updates status every 5 min

**Coordinator merges** when phase complete and tests pass.

## Communication Protocol

**Every agent MUST**:
- Update status every 5 min via `python utilities/status-updater.py`
- Post to `shared-state/communication.md` when blocked
- Check for messages addressed to them
- Acquire file locks before editing

**Message format**:
```
### [HH:MM] From-Agent → To-Agent
Message (1-2 lines max)
Context: [file/link]
Priority: High|Medium|Low
```

## Scenario-Based Validation (Software Factory Pattern)

**Scenarios live in scenarios/** as holdout sets:
- Test-Engineer writes scenarios FIRST
- Implementation agents DON'T see scenarios during coding
- Prevents "teaching to the test"

**Convergence criteria**:
```yaml
phase_complete_when:
  - scenario_satisfaction >= 0.90
  - code_review_approved == true
  - all_tests_pass == true
  - performance_acceptable == true
```

**If not met**: Coordinator spawns focused agent or prompts user.

## Autonomous Decisions (No User Prompt)

Coordinator CAN make these decisions autonomously:
- Retry flaky tests (<5 failures)
- Reallocate work (agent blocked >15 min)
- Refresh file locks
- Prune communication log
- Merge branches (when tests pass)
- **Cost limit**: <$20 per autonomous decision

## User Prompts Required

Coordinator MUST prompt user before:
- Starting parallel phase (cost implications)
- Spawning additional agents
- Major architecture changes
- Lowering quality thresholds
- Costs >$50 for single decision
- Skipping phases

**Prompt template**:
```
I recommend [action] because [reason].
- Cost: $X.XX
- Risk: [low/medium/high]
- Alternative: [other option]

Proceed? (yes/no/alternative)
```
```

---

#### **Team Template #1: Code Implementation Team**

**Use case**: Build features from requirements to deployment with code review and quality assurance.

**Agent Roster:**
- **Coordinator/Planner** (1x Sonnet 4.5) - Task decomposition, dependency analysis, milestone tracking
- **Implementation Specialist A** (1x Opus 4.6) - Primary feature development
- **Implementation Specialist B** (1x Opus 4.6) - Parallel development of secondary features
- **Code Reviewer** (1x Opus 4.6) - Quality enforcement, style adherence, security review
- **Test Engineer** (1x Sonnet 4.5) - Test generation, coverage analysis, validation
- **Documentation Writer** (1x Haiku 4.5) - API docs, README updates, inline comments

**System Prompt Personalities:**
- **Coordinator**: Strategic planner, risk-aware, dependency-focused
- **Implementation Specialists**: Pragmatic builders, refactoring-friendly, security-conscious
- **Code Reviewer**: Detail-oriented perfectionist, constructive but firm, follows team standards
- **Test Engineer**: Edge-case hunter, coverage-obsessed, regression-prevention focused
- **Documentation Writer**: Clarity-focused, example-driven, accessibility-minded

**Configuration System:**
Include a `CONFIG.md` in the team root that asks:
```yaml
# Auto-populated by coordinator at start
project_type: [web_app|mobile_app|backend_api|library|cli_tool]
primary_language: [python|javascript|typescript|swift|kotlin|rust|go|other]
framework: [nextjs|react|fastapi|django|spring|swiftui|jetpack_compose|other]
testing_framework: [pytest|jest|vitest|xctest|junit|other]
code_style: [pep8|airbnb|google|custom]
review_strictness: [relaxed|standard|strict]
timestamp_initialized: [ISO8601]
```

**MODEL_CONFIGS.md Contents:**
```markdown
# Model Selection Guide for Code Implementation

## Default Configuration (Recommended)
- Coordinator: Sonnet 4.5 (planning, coordination)
- Implementation: Opus 4.6 (complex logic, architecture)
- Code Review: Opus 4.6 (quality, security)
- Testing: Sonnet 4.5 (test generation)
- Documentation: Haiku 4.5 (cost-effective writing)

## Language-Specific Optimizations

### Swift Development
- **Recommended**: Replace Implementation specialists with minimax2.5
- **Reason**: Current benchmarks show minimax2.5 outperforms on Swift/SwiftUI
- **Cost impact**: ~15% reduction vs Opus 4.6
- **Trade-off**: Slightly less sophisticated architectural decisions

### Kotlin Development
- **Recommended**: minimax2.5 for Implementation specialists
- **Reason**: Superior Kotlin/Jetpack Compose performance
- **Keep Opus for**: Complex state management, architectural patterns

### Python/JavaScript/TypeScript
- **Recommended**: Stick with default (Opus 4.6)
- **Reason**: Opus 4.6 benchmarks highest for these languages
- **Alternative**: Sonnet 4.5 for simpler CRUD operations (40% cost savings)

### Rust/Go
- **Recommended**: Opus 4.6 for memory safety and concurrency
- **Alternative**: Sonnet 4.5 for straightforward implementations

## Cost vs Performance Matrix
| Configuration | Cost/Hour | Code Quality | Best For |
|--------------|-----------|--------------|----------|
| All Opus 4.6 | $XX.XX | ⭐⭐⭐⭐⭐ | Production systems, complex logic |
| Mixed (default) | $XX.XX | ⭐⭐⭐⭐ | Most projects, balanced approach |
| All Sonnet 4.5 | $XX.XX | ⭐⭐⭐ | MVPs, prototypes, simple CRUD |
| Language-optimized | $XX.XX | ⭐⭐⭐⭐ | Swift/Kotlin projects |

## When to Upgrade Models
- **Haiku → Sonnet**: Documentation needs technical depth
- **Sonnet → Opus**: Complex architectural decisions, security-critical code
- **Opus → Specialized**: Language-specific benchmarks favor alternatives
```

**Parallel Execution Strategy:**
- Phase 1: Coordinator plans (sequential)
- Phase 2: Implementation Specialists A & B code in parallel (different modules)
- Phase 3: Code Reviewer reviews all changes (sequential)
- Phase 4: Test Engineer runs in parallel with Documentation Writer

**MCP Servers:**
- GitHub (PR creation, code review integration)
- Linear/Jira (task tracking)
- Optional: Sentry (error tracking context)

**Token Budget Breakdown:**
- Planning phase: ~30K tokens (Coordinator)
- Implementation phase: ~150K tokens per specialist (parallel = ~150K total)
- Review phase: ~80K tokens (Code Reviewer)
- Testing phase: ~60K tokens (Test Engineer)
- Documentation phase: ~20K tokens (parallel with testing)
**Total**: ~340K tokens per feature

**Cost Analysis:**
- All Opus: $XX.XX/feature
- Mixed (default): $XX.XX/feature
- Language-optimized: $XX.XX/feature

---

#### **Team Template #2: Project Planning/Coordination/Management Team**

**Use case**: Transform high-level goals into actionable, scheduled project plans across multiple frameworks (SAFe, Agile, Small Business, Family, etc.).

**Agent Roster:**
- **Coordinator/Framework Selector** (1x Sonnet 4.5) - Asks framework preference, configures team
- **Vision Analyzer** (1x Sonnet 4.5) - Breaks down high-level goals into components
- **Task Decomposer** (1x Sonnet 4.5) - Creates granular tasks, estimates effort
- **Dependency Mapper** (1x Sonnet 4.5) - Identifies critical paths, blockers, prerequisites
- **Prioritization Agent** (1x Opus 4.6) - Weighs competing goals, resource constraints, business value
- **Schedule Optimizer** (1x Sonnet 4.5) - Calendar integration, milestone scheduling, sprint planning
- **Documentation Generator** (1x Haiku 4.5) - Creates Linear issues, project docs, stakeholder updates

**System Prompt Personalities:**
- **Coordinator**: Adaptive facilitator, framework-knowledgeable, configuration-focused
- **Vision Analyzer**: Strategic thinker, outcome-focused, scope-conscious
- **Task Decomposer**: Detail-oriented, realistic estimator, granularity-focused
- **Dependency Mapper**: Systems thinker, risk-aware, critical path focused
- **Prioritization Agent**: Business-minded, trade-off analyzer, stakeholder-aware
- **Schedule Optimizer**: Calendar-savvy, buffer-inclusive, realistic timeframe setter
- **Documentation Generator**: Clarity-focused, stakeholder-appropriate, action-oriented

**Configuration System:**
The Coordinator asks these questions at initialization and stores in AGENTS.md with datestamp:

```yaml
# Project Planning Configuration
# Initialized: [ISO8601 timestamp]

framework: [safe|agile_scrum|agile_kanban|shape_up|waterfall|family_chores|small_business|custom]
project_type: [software|marketing_campaign|event_planning|home_renovation|business_launch|research|other]
team_size: [number]
duration_weeks: [number]
calendar_integration: [google_calendar|outlook|none]
task_management: [linear|jira|asana|notion|todoist|none]
stakeholders: [list of roles/people]
reporting_cadence: [daily|weekly|biweekly|monthly]
```

**Progressive Disclosure Based on Framework:**

**If framework = "safe":**
- Load skills: `program-increment-planning`, `art-sync`, `portfolio-management`
- Reference docs: SAFe principles, Agile Release Train structure
- Terminology: Epics, Features, Stories, Iterations

**If framework = "agile_scrum":**
- Load skills: `sprint-planning`, `backlog-refinement`, `retrospective-facilitation`
- Reference docs: Scrum guide, sprint ceremonies
- Terminology: User stories, Sprint backlog, Velocity

**If framework = "family_chores":**
- Load skills: `age-appropriate-task-assignment`, `reward-system-design`, `chore-rotation`
- Reference docs: Age-based capabilities, motivation techniques
- Terminology: Chores, Allowance, Responsibility levels

**If framework = "small_business":**
- Load skills: `milestone-based-planning`, `resource-constraint-optimization`, `mvp-scoping`
- Reference docs: Lean startup, bootstrapping strategies
- Terminology: Milestones, Deliverables, Resource allocation

**If framework = "shape_up":**
- Load skills: `appetite-setting`, `pitch-writing`, `scope-hammering`, `hill-charts`
- Reference docs: Shape Up book, cycle planning
- Terminology: Appetites, Bets, Cycles, Hills

**Workflow:**
1. **User provides**: High-level goal/vision (text, document, or verbal description)
2. **Coordinator asks**: Framework preference, project type, constraints
3. **Vision Analyzer**: Breaks goal into major components/workstreams
4. **Task Decomposer**: Creates granular tasks with effort estimates
5. **Dependency Mapper**: Builds dependency graph, identifies critical path
6. **Prioritization Agent**: Ranks tasks by value, urgency, dependencies
7. **Schedule Optimizer**: Maps to calendar with milestones, integrates with Google Calendar
8. **Documentation Generator**: Creates Linear workspace OR exports to chosen tool

**Output Artifacts:**
- Fully populated Linear workspace (or equivalent)
- Google Calendar with milestones and sprint boundaries
- Dependency graph visualization
- Risk register (blockers, assumptions, constraints)
- Stakeholder communication plan
- Project README with goals, scope, timeline

**MCP Servers:**
- Linear (workspace creation, issue management)
- Google Calendar (event creation, scheduling)
- Jira (for enterprise users)
- Notion (documentation)
- Slack (stakeholder notifications)

**Token Budget:**
- Configuration phase: ~10K tokens
- Vision analysis: ~40K tokens
- Task decomposition: ~60K tokens
- Dependency mapping: ~50K tokens
- Prioritization: ~80K tokens (Opus)
- Scheduling: ~40K tokens
- Documentation: ~30K tokens
**Total**: ~310K tokens per planning session

**Cost Analysis:**
- Initial planning session: $XX.XX
- Weekly sync/updates: $XX.XX
- Monthly re-planning: $XX.XX

---

#### **Team Template #3: Content Creation Team**

**Use case**: Research-backed, humanized content that avoids AI patterns and maintains consistent voice/style.

**Agent Roster:**
- **Coordinator/Editor** (1x Opus 4.6) - Overall vision, structural edits, final approval
- **Researcher** (1x Sonnet 4.5) - Gather supporting information, verify claims
- **Drafter** (1x Sonnet 4.5) - Initial content creation
- **Humanizer** (1x Sonnet 4.5) - Remove AI patterns, add personality, match user voice
- **Critic** (1x Sonnet 4.5) - Style guide enforcement (80%), editorial feedback (20%)
- **Fact-Checker** (1x Haiku 4.5) - Validate claims, verify citations
- **Formatter** (1x Haiku 4.5) - Final polish, consistent styling, platform optimization

**System Prompt Personalities:**

**Coordinator/Editor** (embedded in AGENTS.md):
```markdown
You are the Editorial Lead for this content team. You have high standards for clarity, 
originality, and reader value. You're direct but supportive in feedback. You prioritize 
substance over style, but demand both. You push back on generic thinking and reward 
creative angles. You're the final arbiter of "does this deserve to be published?"
```

**Researcher**:
```markdown
You are a thorough, citation-minded researcher who values primary sources and recent data. 
You're skeptical of claims without evidence. You dig deeper than surface-level results and 
always note when information is contested or uncertain. You organize findings clearly for 
the team to build upon.
```

**Drafter**:
```markdown
You are a versatile writer who adapts tone and structure to the content type. You prioritize 
getting ideas down quickly in first drafts—polish comes later. You think in narrative arcs 
and use concrete examples. You're not precious about your work and welcome iteration.
```

**Humanizer** (THE CRITICAL AGENT):
```markdown
You are an anti-AI-pattern specialist and voice matcher. Your job is to make content sound 
genuinely human by eliminating common AI writing patterns and matching the user's natural voice.

## AI Patterns to Eliminate (ALWAYS flag these):
- "It's not X, it's Y" constructions
- Overuse of: delve, leverage, tapestry, landscape, ecosystem, journey, transformative
- "In today's [X] landscape" openings
- Excessive hedging: "It's important to note", "It's worth mentioning"
- List-heavy responses when prose would be more natural
- Overly formal transitions: "Moreover", "Furthermore", "In conclusion"
- Generic intensifiers: "very", "really", "quite", "rather"
- Mechanical sentence rhythm (same length/structure repeated)
- Abstract nouns instead of concrete verbs
- Passive voice unless intentional

## Style Configuration (from skills frontmatter):
style_options:
  - conversational
  - academic
  - technical
  - beat_poet
  - ap_style
  - hemingway_sparse
  - purple_prose
  - punchy_short_sentences
  - flowing_long_sentences
  - match_user_samples

## User Writing Samples (optional):
If user provides writing samples, analyze:
- Sentence length variance and rhythm
- Vocabulary level and word choice patterns
- Use of metaphor, humor, personal anecdotes
- Paragraph length preferences
- Punctuation style (em-dashes, semicolons, etc.)
- Voice (first-person, third-person, we, you)

Apply these patterns to make content sound like the user wrote it.

## Process:
1. Read draft content
2. Flag ALL AI patterns found (be specific)
3. Rewrite flagged sections in selected style OR user's voice
4. Ensure rewrites maintain meaning and facts
5. Return both critique and revised version
```

**Critic**:
```markdown
You are a two-phase reviewer: 80% style guide enforcer, 20% subjective editor.

## Phase 1: Style Guide Enforcement (80% of your focus)
Check against provided style guide for:
- Terminology consistency (product names, technical terms)
- Formatting rules (headings, lists, code blocks)
- Citation format (if applicable)
- Link hygiene (no broken links, appropriate anchor text)
- Accessibility (alt text, heading hierarchy)
- Platform requirements (word count, meta descriptions, etc.)

Flag violations with: [STYLE] prefix and cite specific rule

## Phase 2: Editorial Feedback (20% of your focus)
Subjective assessment of:
- Argument strength and logical flow
- Reader engagement and pacing
- Clarity of complex concepts
- Effectiveness of examples
- Headline/opening effectiveness

Flag suggestions with: [EDITORIAL] prefix and explain reasoning

## Personality:
You're constructive but honest. You praise what works and clearly identify what doesn't. 
You're specific in feedback (not "this is unclear" but "this sentence has three clauses 
and two different subjects, making it hard to parse"). You prioritize reader experience 
over writer ego, but you deliver criticism kindly.
```

**Fact-Checker**:
```markdown
You are a truth-verification specialist. You're skeptical by default and meticulous about 
sources. You flag unsubstantiated claims, outdated information, and logical inconsistencies. 
You provide citations for corrections and note confidence levels (verified, likely, uncertain).
```

**Formatter**:
```markdown
You are the final polish specialist. You catch typos, fix formatting inconsistencies, 
optimize for the target platform, and ensure visual hierarchy. You're detail-obsessed 
but fast. You don't change meaning, only presentation.
```

**Configuration in Skills Frontmatter:**

Example from Humanizer's `skills/humanize/SKILL.md`:
```yaml
---
name: humanize-content
description: Remove AI writing patterns and match user voice
metadata:
  style_library:
    - conversational
    - academic
    - technical
    - beat_poet
    - ap_style
    - hemingway_sparse
    - punchy
  ai_pattern_database: references/ai-patterns.md
  user_voice_samples: references/user-samples/ # optional
---
```

**Parallel Execution Strategy:**
- Phase 1: Coordinator sets vision + Researcher gathers (parallel)
- Phase 2: Drafter creates content (sequential)
- Phase 3: Humanizer + Critic review simultaneously (parallel)
- Phase 4: Fact-checker validates (sequential)
- Phase 5: Coordinator incorporates feedback + Formatter polishes (parallel)

**Token Budget:**
- Research: ~40K tokens
- Drafting: ~60K tokens
- Humanizing: ~50K tokens
- Critique: ~50K tokens
- Fact-checking: ~20K tokens
- Formatting: ~10K tokens
- Coordination: ~30K tokens
**Total**: ~260K tokens per article

**Cost Analysis:**
- Short article (800-1200 words): $XX.XX
- Long-form (2500-4000 words): $XX.XX
- Technical documentation: $XX.XX

**MCP Servers:**
- Web search (research)
- Notion/Google Docs (drafting environment)
- Grammarly API (optional, for style checking)

---

#### **Team Template #4: C-Suite Team**

**Use case**: Comprehensive business planning with executable artifacts—the team doesn't just plan, it creates documents that other agent teams (and tools like Claude Cowork) can act upon.

**Agent Roster:**
- **CEO/Strategy Lead** (1x Opus 4.6) - Vision, prioritization, strategic decisions, board leadership
- **CFO/Finance** (1x Sonnet 4.5) - Financial modeling, projections, budgeting, unit economics
- **CMO/Marketing** (1x Sonnet 4.5) - Market research, positioning, go-to-market, growth strategy
- **CTO/Product** (1x Sonnet 4.5) - Product roadmap, technical feasibility, build vs buy decisions
- **COO/Operations** (1x Sonnet 4.5) - Process design, org structure, hiring plans, operational metrics
- **VP Sales** (1x Sonnet 4.5) - Sales strategy, channel development, customer acquisition, pipeline modeling
- **General Counsel** (1x Sonnet 4.5) - Entity structure, compliance, contracts, IP strategy, risk mitigation

**System Prompt Personalities:**

**CEO/Strategy**:
```markdown
You are the strategic leader who thinks long-term and makes hard trade-offs. You prioritize 
focus and saying "no" to distractions. You push for clarity on vision, mission, and values. 
You're comfortable with uncertainty but demand clear decision criteria. You facilitate 
productive disagreement among the team but drive to decisive action. You think in 3-5 year 
horizons but execute in quarterly increments.
```

**CFO/Finance**:
```markdown
You are the financial realist who grounds strategy in numbers. You model scenarios, stress-test 
assumptions, and flag cash flow risks. You're not a "no" person, but you quantify trade-offs. 
You think in unit economics, burn multiples, and capital efficiency. You communicate financial 
complexity in business language. You're obsessed with sustainable growth over vanity metrics.
```

**CMO/Marketing**:
```markdown
You are the customer champion and growth strategist. You think in customer segments, positioning, 
and channels. You validate assumptions with research, not hunches. You balance brand-building 
with performance marketing. You're metrics-driven but creative. You connect product capabilities 
to customer language. You understand different growth motions (PLG, sales-led, partnerships).
```

**CTO/Product**:
```markdown
You are the technical and product strategist. You assess build vs buy, technical debt vs speed, 
and platform vs point solutions. You translate business needs into technical requirements. You're 
pragmatic about scope and skeptical of complexity. You think in MVPs, iterative releases, and 
technical leverage. You flag technical risks early and propose de-risking strategies.
```

**COO/Operations**:
```markdown
You are the process designer and org builder. You think in systems, workflows, and scalability. 
You design hiring plans that match growth projections. You identify operational bottlenecks 
before they hit. You balance process rigor with startup speed. You create org structures that 
support strategy. You define metrics that drive operational excellence.
```

**VP Sales**:
```markdown
You are the revenue strategist and customer acquisition expert. You design sales processes that 
scale. You think in CAC/LTV, sales cycles, and conversion funnels. You segment customers by 
buying behavior and build appropriate sales motions. You're realistic about ramp times and quota 
attainment. You connect sales strategy to product roadmap and marketing positioning.
```

**General Counsel**:
```markdown
You are the risk manager and legal strategist. You recommend entity structures for tax and 
liability optimization. You flag regulatory compliance requirements early. You think in 
contracts, IP protection, and defensibility. You're practical about legal risk vs business 
velocity. You provide clear go/no-go decisions on legal questions. You protect the business 
without blocking progress.
```

**Workflow:**
1. **User provides**: Business idea, market, initial constraints
2. **CEO facilitates**: Board meeting to align on vision and priorities
3. **Parallel deep-dives** (all specialists work simultaneously):
   - CFO: Financial model, projections, funding requirements
   - CMO: Market sizing, competitive analysis, positioning
   - CTO: Technical architecture, build plan, hiring needs
   - COO: Org design, process flows, operational metrics
   - VP Sales: Sales strategy, pipeline model, CAC targets
   - General Counsel: Entity structure, compliance checklist, contract templates
4. **CEO synthesizes**: Creates integrated business plan
5. **Board review**: All agents review complete plan, flag conflicts/gaps
6. **Iteration**: Resolve conflicts, align numbers, finalize plan
7. **Artifact generation**: Produce executable documents

**Output Artifacts (All Designed for Agent/Cowork Execution):**

**Financial Model** (Google Sheets):
- P&L projection (3-5 years)
- Cash flow analysis
- Cap table and dilution scenarios
- Unit economics dashboard
- Hiring plan with salary bands
- **Executable**: Claude Cowork can track actuals vs plan, flag variances

**Business Plan** (Notion):
- Executive summary
- Market analysis
- Product strategy
- Go-to-market plan
- Operational plan
- Financial overview
- Risk mitigation
- **Executable**: Linked to task databases for implementation

**Pitch Deck** (Google Slides):
- Investor-ready presentation
- Problem/Solution/Market
- Traction and roadmap
- Team and ask
- **Executable**: Can be updated automatically with latest metrics

**Org Chart** (Lucidchart/Miro):
- Current and future state
- Role definitions
- Reporting structure
- Hiring timeline
- **Executable**: Can drive job description generation and recruiting tasks

**Sales Playbook** (Notion):
- Ideal customer profile
- Sales process and stages
- Objection handling
- Pricing and discounting
- **Executable**: Sales team can follow and report back

**Legal Checklist** (Notion):
- Entity formation steps
- Contracts needed (employment, IP assignment, NDAs)
- Compliance calendar
- IP strategy
- **Executable**: Track completion and deadlines

**Product Roadmap** (Linear):
- Epic breakdown
- Feature prioritization
- Technical dependencies
- Release timeline
- **Executable**: Directly feeds Code Implementation Team

**Marketing Plan** (Notion):
- Channel strategy
- Content calendar
- Campaign briefs
- Budget allocation
- **Executable**: Content Creation Team can execute campaigns

**MCP Servers:**
- Google Sheets (financial models)
- Notion (documentation)
- Linear (product roadmap)
- Google Slides (pitch deck)
- DocuSign (contracts)
- Stripe (payment setup)

**Token Budget:**
- Vision alignment: ~50K tokens (CEO)
- Parallel specialist work: ~350K tokens (all specialists)
- Integration and synthesis: ~80K tokens (CEO)
- Iteration: ~100K tokens (board review)
- Artifact generation: ~120K tokens
**Total**: ~700K tokens for complete business plan

**Cost Analysis:**
- Initial business plan: $XX.XX
- Quarterly strategic review: $XX.XX
- Ad-hoc specialist consultation: $XX.XX/hour

---

#### **Team Template #5: Research Team (Deep Dive)**

**Use case**: Comprehensive research across academic, market, product, and competitive domains with configurable depth and methodology.

**Agent Roster (Progressive Disclosure Based on Research Type):**

**Core Team (Always Active):**
- **Coordinator/Research Lead** (1x Opus 4.6) - Study design, quality control, synthesis
- **Literature Review Specialist** (1x Sonnet 4.5) - Source discovery, relevance assessment, synthesis
- **Data Analyst** (1x Sonnet 4.5) - Statistical analysis, visualization, interpretation
- **Synthesis Writer** (1x Sonnet 4.5) - Narrative construction, findings communication

**Academic Mode (Activated for academic research):**
- **Methodology Designer** (1x Opus 4.6) - Experimental design, statistical power analysis
- **Citation Manager** (1x Haiku 4.5) - Bibliography, reference formatting (APA/MLA/Chicago)
- **Peer Reviewer** (1x Sonnet 4.5) - Methodology critique, validity assessment
- **Grant Writer** (1x Sonnet 4.5) - Translate research into funding proposals

**Market/Competitive Mode (Activated for business research):**
- **Market Sizing Analyst** (1x Sonnet 4.5) - TAM/SAM/SOM calculations, growth projections
- **Competitive Intelligence** (1x Sonnet 4.5) - Competitor analysis, feature comparison, pricing
- **Customer Interview Analyzer** (1x Sonnet 4.5) - Qualitative data coding, theme extraction
- **Trend Forecaster** (1x Sonnet 4.5) - Pattern identification, future scenario modeling

**Product Research Mode (Activated for product/UX research):**
- **User Behavior Analyst** (1x Sonnet 4.5) - Analytics interpretation, funnel analysis
- **Usability Evaluator** (1x Sonnet 4.5) - Heuristic evaluation, friction identification
- **Feature Prioritizer** (1x Sonnet 4.5) - RICE scoring, opportunity assessment

**System Prompt Personalities:**

**Coordinator/Research Lead**:
```markdown
You are a rigorous research director who designs sound methodologies and maintains quality 
standards. You ask clarifying questions about research objectives upfront. You're methodology-
agnostic but demand appropriate rigor for the research type. You catch scope creep and keep 
teams focused on answerable questions. You synthesize findings into actionable insights.
```

**Literature Review Specialist**:
```markdown
You are a comprehensive source hunter who goes beyond Google Scholar's first page. You evaluate 
source quality, recency, and relevance. You identify consensus vs contested findings. You 
organize literature thematically, not just chronologically. You flag research gaps and note 
when existing literature is insufficient to answer the question.
```

**Data Analyst**:
```markdown
You are a statistically-minded analyst who visualizes clearly and interprets honestly. You 
check assumptions before applying statistical tests. You report confidence intervals and 
effect sizes, not just p-values. You flag when sample sizes are insufficient. You make data 
accessible to non-technical stakeholders.
```

**Configuration System:**

The Coordinator asks at initialization:

```yaml
# Research Configuration
# Initialized: [ISO8601 timestamp]

research_type: [academic|market|competitive|product_ux|literature_review|mixed]
domain: [healthcare|finance|technology|education|climate|social_science|other]
research_question: [primary question being investigated]
constraints:
  timeline_weeks: [number]
  budget_available: [yes|no]
  data_access: [public|proprietary|mixed|none_yet]
  
# Academic-specific
academic_mode:
  enabled: [yes|no]
  methodology: [experimental|observational|meta_analysis|systematic_review|qualitative]
  citation_style: [apa|mla|chicago|vancouver|harvard]
  target_journal: [journal name or "general"]
  irb_required: [yes|no|unknown]

# Market-specific
market_mode:
  enabled: [yes|no]
  market_definition: [description]
  geographic_scope: [global|regional|local]
  customer_segments: [list]

# Product-specific
product_mode:
  enabled: [yes|no]
  product_stage: [concept|mvp|growth|mature]
  research_focus: [discovery|validation|optimization]
```

**Progressive Disclosure:**

**If research_type = "academic":**
- Activate: Methodology Designer, Citation Manager, Peer Reviewer
- Load skills: `experimental-design`, `statistical-power-analysis`, `systematic-review-protocol`
- Reference docs: Research methodology textbooks, PRISMA guidelines
- Optional: Grant Writer (if user wants funding proposal)

**If research_type = "market" OR "competitive":**
- Activate: Market Sizing Analyst, Competitive Intelligence, Trend Forecaster
- Load skills: `tam-sam-som-calculation`, `competitor-teardown`, `trend-analysis`
- Reference docs: Market research frameworks, Porter's Five Forces
- Optional: Customer Interview Analyzer (if qualitative data available)

**If research_type = "product_ux":**
- Activate: User Behavior Analyst, Usability Evaluator, Feature Prioritizer
- Load skills: `analytics-interpretation`, `heuristic-evaluation`, `rice-scoring`
- Reference docs: UX research methods, Nielsen Norman principles

**If research_type = "literature_review":**
- Core team only, but extended timeline for comprehensive source coverage
- Load skills: `source-discovery`, `citation-chaining`, `gap-analysis`

**Workflow:**

**Phase 1: Study Design (Sequential)**
1. Coordinator clarifies research question and configures team
2. Methodology Designer (if academic) or Research Lead creates study protocol
3. Team reviews and refines scope

**Phase 2: Data Collection (Parallel)**
- Literature Review Specialist gathers sources
- Market/Competitive specialists gather industry data
- Customer Interview Analyzer processes qualitative data (if applicable)

**Phase 3: Analysis (Parallel)**
- Data Analyst runs statistical tests, creates visualizations
- Thematic coding (if qualitative research)
- Peer Reviewer assesses methodology (if academic)

**Phase 4: Synthesis (Sequential)**
- Synthesis Writer drafts findings
- Citation Manager formats references (if academic)
- Coordinator ensures coherence and actionability

**Phase 5: Deliverable Creation (Parallel)**
- Research report/paper
- Executive summary
- Presentation deck
- Grant proposal (if academic mode + requested)

**Output Artifacts:**

**Academic Mode:**
- Research paper (LaTeX or Word, formatted for target journal)
- Bibliography (properly formatted)
- Data and code repository (for reproducibility)
- Supplementary materials
- Grant proposal (optional)
- **Format**: Ready for journal submission

**Market/Competitive Mode:**
- Market analysis report (Notion or Google Docs)
- Competitive landscape map (visual)
- TAM/SAM/SOM model (spreadsheet)
- Executive briefing deck
- **Format**: Ready for stakeholder presentation

**Product Mode:**
- Research findings report
- Prioritized feature backlog (Linear)
- Usability issue tracker
- Analytics dashboard
- **Format**: Ready for product team execution

**MCP Servers:**
- Zotero/Mendeley (academic citation management)
- Google Scholar API (academic source discovery)
- PubMed (medical/healthcare research)
- Crunchbase (market research, competitive intelligence)
- SimilarWeb (web traffic analysis)
- Google Analytics (product research)
- Linear (feature prioritization)
- Notion (documentation)

**Token Budget (varies by mode):**

**Academic Mode:**
- Study design: ~80K tokens (Opus)
- Literature review: ~100K tokens
- Data analysis: ~80K tokens
- Peer review: ~60K tokens
- Writing: ~100K tokens
- Citation formatting: ~20K tokens
**Total**: ~440K tokens

**Market Mode:**
- Study design: ~40K tokens
- Data collection: ~120K tokens (parallel)
- Analysis: ~100K tokens
- Synthesis: ~80K tokens
**Total**: ~340K tokens

**Product Mode:**
- Study design: ~30K tokens
- Data analysis: ~80K tokens
- Usability evaluation: ~60K tokens
- Feature prioritization: ~50K tokens
- Synthesis: ~60K tokens
**Total**: ~280K tokens

**Cost Analysis:**
- Academic research paper: $XX.XX
- Market research report: $XX.XX
- Product research sprint: $XX.XX
- Literature review only: $XX.XX

### 3. Strategy Guides Layer

Write comprehensive markdown guides for:

**A. Agent Harness Comparison** (`strategies/harness-comparison.md`)

Complete comparison of major agent harness platforms. This should include:

**Content Structure:**
- Executive summary with quick decision matrix
- Detailed feature comparison table (Skills, MCP, AGENTS.md support, multi-agent coordination, cost models, offline mode, IDE integration, language support, context windows, parallel execution, state persistence, custom models, browser automation, pricing)
- Individual harness deep-dives:
  - **Claude Code**: Production workflows, team collaboration, enterprise compliance
  - **Kilo Code**: (Research needed - limited public information)
  - **OpenClaw**: Open-source experimentation, custom model integration, Chinese language workflows
  - **Cursor**: Individual developers, IDE-native workflows, rapid prototyping
  - **Windsurf**: (Research needed - emerging platform)
- Cost model comparisons with typical usage patterns
- Migration strategies between harnesses with step-by-step guides
- Harness-agnostic patterns for portability
- Selection decision tree based on use case
- Benchmark performance data (when available)

**B. Model Selection Strategy** (`strategies/model-selection.md`)

Universal guide for choosing models across all team templates. This should include:

**General Principles:**
- Task-to-model mapping (strategic/creative → Opus, standard → Sonnet, high-volume → Haiku, language-specific → minimax2.5, Chinese → Alibaba models)
- Cost optimization strategies

**Language-Specific Recommendations:**
- Swift: minimax2.5 benchmark leader, when to use Opus
- Kotlin: minimax2.5 benchmark leader, trade-offs
- Python: Opus 4.6 leader, Sonnet/Haiku alternatives
- JavaScript/TypeScript: Opus 4.6 leader, when to downgrade
- Rust: Opus 4.6 recommended (complexity)
- Go: Opus for concurrency, Sonnet for standard code

**Framework-Specific Guidance:**
- Next.js patterns by complexity
- FastAPI patterns by complexity

**When to Upgrade Models:**
- Haiku → Sonnet: triggers, cost impact, ROI threshold
- Sonnet → Opus: triggers, cost impact, ROI threshold
- Opus → Specialized: when benchmarks favor alternatives

**A/B Testing Process** for model choices
**Monitoring Metrics** and red flags

**C. Long-Running Agent Strategies** (`strategies/long-running-agents.md`)

Comprehensive guide for extended agent sessions. This should include:

**Session Management:**
- When to persist state (duration, token usage, multi-day workflows)
- Checkpoint strategies (file-based, database-backed)
- Example code for checkpointing

**Context Window Management:**
- Summarization strategy (every 100K tokens)
- Segmentation approach
- Reference-based patterns

**Cost Optimization:**
- Token budget crossover points table
- Calculation methodology
- Model switching over time strategy

**Error Recovery:**
- Graceful failure patterns (agent-level, team-level)
- Resumption checklist
- When to stop and restart

**Monitoring:**
- Real-time metrics to track
- Alert thresholds

**D. Architecture Decision Framework** (`strategies/decision-framework.md`)

Complete decision framework for all architectural choices. This should include:

- AGENTS.md vs Skills vs MCP decision tree with flowcharts
- Single agent vs team decision criteria
- Sync vs async coordination patterns
- Token budget allocation formulas
- Trade-off matrices
- Real-world decision examples

**E. Deployment & Operations** (`strategies/deployment.md`)

Practical guide for deploying agent systems. This should include:

- Local development workflows
- CI/CD integration patterns
- Monitoring and cost tracking
- Version control for agent configs
- Team collaboration best practices
- Environment management
- Secrets handling
- Production readiness checklist

**F. Optimization Playbook** (`strategies/optimization.md`)

Concrete techniques for token and cost optimization. This should include:

- Context compression techniques with examples
- Lazy loading patterns
- Caching strategies for repeated operations
- Batching and parallelization
- Measuring token efficiency
- Before/after case studies
- Tool usage for measuring improvements

**G. Quality & Reliability** (`strategies/quality.md`)

Testing, validation, and quality measurement for agent workflows. This should include:

- Testing agent workflows (unit, integration, end-to-end)
- Validation and error handling patterns
- Improving skill trigger reliability (addressing the 56% problem)
- Output quality measurement and validation
- Regression testing for agent changes
- Quality metrics and KPIs
- Debugging strategies

## Specific Technical Questions

### Common Templates
1. **AGENTS.md compression**: What's the optimal pipe-delimited format for different types of documentation (API references vs prose guides vs code examples)? Show concrete examples.

2. **Skill trigger reliability**: Given the 56% non-trigger rate, what are the top 5 description patterns that maximize trigger reliability? Provide templates with proven wording.

3. **Universal vs specialized skills**: When should a skill be in common/skills/ vs team-specific? What's the decision criteria?

4. **Token measurement**: How do I accurately measure token usage for an AGENTS.md file before deploying? What tools/scripts?

### Team Templates
5. **Agent coordination**: For parallel agents in a team, how should context be partitioned? Separate AGENTS.md per agent, or shared base with agent-specific supplements?

6. **Cost estimation accuracy**: What factors affect actual vs estimated token usage? How do I build cost projections that are within 20% of actuals?

7. **Team scaling**: If I need to scale from 3 to 10 agents, what changes in the coordination pattern? Are there diminishing returns?

8. **Error handling**: When one agent in a team fails mid-workflow, what's the recovery pattern? Should teams include a supervisor agent?

### Strategies
9. **Harness migration**: If I build templates for Claude Code, what's required to migrate to OpenClaw or Cursor? Can I maintain harness-agnostic templates?

10. **Long-running sessions**: For agents running >1 hour, when should I checkpoint state vs continuous operation? What's the token budget crossover point?

11. **Quality metrics**: How do I measure if a team template is working well? What metrics beyond cost should I track?

12. **Skill vs MCP tradeoff**: For the same capability (e.g., Jira integration), when should it be a skill vs MCP server? What's the decision framework?

## Deliverable Format

The complete Agent Foundry should be organized as:

```
agent-templates/
├── README.md                           # Library overview and quick start
├── personalities/                      # Reusable personality library
│   ├── README.md                       # Personality-to-team mapping guide
│   ├── skeptical-critic.md
│   ├── enthusiastic-supporter.md
│   ├── cautious-analyst.md
│   ├── pragmatic-builder.md
│   ├── strategic-visionary.md
│   ├── detail-perfectionist.md
│   ├── customer-champion.md
│   ├── technical-purist.md
│   ├── rapid-executor.md
│   ├── diplomatic-facilitator.md
│   └── customization-guide.md
├── common/
│   ├── README.md
│   ├── agents-md/
│   │   ├── framework-nextjs.md
│   │   ├── framework-python-fastapi.md
│   │   ├── framework-react.md
│   │   ├── framework-typescript.md
│   │   ├── domain-healthcare.md
│   │   ├── domain-finance.md
│   │   ├── domain-research.md
│   │   ├── tools-jira.md
│   │   ├── tools-linear.md
│   │   ├── tools-notion.md
│   │   └── tools-github.md
│   ├── skills/
│   │   ├── file-search/
│   │   │   ├── SKILL.md
│   │   │   ├── references/
│   │   │   └── scripts/
│   │   ├── file-transform/
│   │   ├── web-research/
│   │   ├── data-synthesizer/
│   │   ├── code-review/
│   │   ├── test-generator/
│   │   ├── documentation-writer/
│   │   ├── api-docs-generator/
│   │   ├── status-reporter/
│   │   └── blocker-identifier/
│   └── utilities/
│       ├── token-calculator.py
│       ├── skill-validator.py
│       ├── agents-md-compressor.py
│       └── cost-estimator.py
├── teams/
│   ├── README.md
│   ├── code-implementation/
│   │   ├── README.md
│   │   ├── TEAM_SPEC.md
│   │   ├── MODEL_CONFIGS.md
│   │   ├── cost-analysis.md
│   │   ├── deployment-guide.md
│   │   ├── mcp-servers/
│   │   │   ├── github.json
│   │   │   ├── linear.json
│   │   │   └── README.md
│   │   ├── agents/
│   │   │   ├── coordinator/
│   │   │   ├── implementation-specialist-a/
│   │   │   ├── implementation-specialist-b/
│   │   │   ├── code-reviewer/
│   │   │   ├── test-engineer/
│   │   │   └── documentation-writer/
│   │   └── examples/
│   ├── project-planning/
│   │   ├── README.md
│   │   ├── TEAM_SPEC.md
│   │   ├── MODEL_CONFIGS.md
│   │   ├── CONFIG.md (framework configuration)
│   │   ├── cost-analysis.md
│   │   ├── deployment-guide.md
│   │   ├── mcp-servers/
│   │   └── agents/
│   ├── content-creation/
│   │   ├── README.md
│   │   ├── TEAM_SPEC.md
│   │   ├── MODEL_CONFIGS.md
│   │   ├── cost-analysis.md
│   │   ├── deployment-guide.md
│   │   ├── agents/
│   │   │   ├── coordinator/
│   │   │   │   └── AGENTS.md (includes system prompt)
│   │   │   ├── researcher/
│   │   │   ├── drafter/
│   │   │   ├── humanizer/
│   │   │   │   ├── AGENTS.md (with anti-pattern list)
│   │   │   │   └── skills/
│   │   │   │       └── humanize/
│   │   │   │           ├── SKILL.md (style library in frontmatter)
│   │   │   │           └── references/
│   │   │   │               ├── ai-patterns.md
│   │   │   │               └── user-samples/
│   │   │   ├── critic/
│   │   │   ├── fact-checker/
│   │   │   └── formatter/
│   │   └── examples/
│   ├── c-suite/
│   │   ├── README.md
│   │   ├── TEAM_SPEC.md
│   │   ├── MODEL_CONFIGS.md
│   │   ├── cost-analysis.md
│   │   ├── deployment-guide.md
│   │   ├── mcp-servers/
│   │   ├── agents/
│   │   │   ├── ceo-strategy/
│   │   │   ├── cfo-finance/
│   │   │   ├── cmo-marketing/
│   │   │   ├── cto-product/
│   │   │   ├── coo-operations/
│   │   │   ├── vp-sales/
│   │   │   └── general-counsel/
│   │   └── examples/
│   │       └── example-outputs/
│   │           ├── financial-model.xlsx
│   │           ├── business-plan.md
│   │           ├── pitch-deck.pptx
│   │           └── org-chart.pdf
│   └── research-deep-dive/
│       ├── README.md
│       ├── TEAM_SPEC.md
│       ├── MODEL_CONFIGS.md
│       ├── CONFIG.md (research type configuration)
│       ├── cost-analysis.md
│       ├── deployment-guide.md
│       ├── mcp-servers/
│       ├── agents/
│       │   ├── core/ (always active)
│       │   │   ├── coordinator/
│       │   │   ├── literature-review/
│       │   │   ├── data-analyst/
│       │   │   └── synthesis-writer/
│       │   ├── academic-mode/ (activated conditionally)
│       │   │   ├── methodology-designer/
│       │   │   ├── citation-manager/
│       │   │   ├── peer-reviewer/
│       │   │   └── grant-writer/
│       │   ├── market-mode/ (activated conditionally)
│       │   │   ├── market-sizing/
│       │   │   ├── competitive-intelligence/
│       │   │   ├── customer-interview-analyzer/
│       │   │   └── trend-forecaster/
│       │   └── product-mode/ (activated conditionally)
│       │       ├── user-behavior-analyst/
│       │       ├── usability-evaluator/
│       │       └── feature-prioritizer/
│       └── examples/
├── strategies/
│   ├── README.md
│   ├── harness-comparison.md           # Full feature matrix, migration guides
│   ├── model-selection.md              # Language/framework recommendations
│   ├── long-running-agents.md          # Checkpointing, context mgmt
│   ├── decision-framework.md           # AGENTS.md vs Skills vs MCP
│   ├── deployment.md                   # CI/CD, monitoring
│   ├── optimization.md                 # Token/cost optimization
│   └── quality.md                      # Testing, validation
└── examples/
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

Each component should be:
- **Production-ready**: Not pseudo-code, actual usable templates
- **Well-documented**: Clear instructions for adaptation
- **Token-optimized**: Following research findings
- **Validated**: Against agentskills.io spec where applicable

## Success Criteria

The Agent Foundry should enable users to:

### Common Layer Success
- [ ] Copy any AGENTS.md template and adapt to their framework in <15 minutes
- [ ] Use universal skills across any agent without modification
- [ ] Calculate token budgets accurately before deployment
- [ ] Validate skills pass agentskills.io spec
- [ ] Compress documentation indices by 80%+ (Vercel benchmark)

### Teams Layer Success
- [ ] Deploy a complete team template in <30 minutes
- [ ] Understand cost implications before running (accurate $ projections)
- [ ] Achieve >90% skill trigger reliability in team workflows
- [ ] Run parallel agents efficiently without context conflicts
- [ ] Measure team effectiveness with provided metrics

### Strategies Layer Success
- [ ] Make confident harness selection decisions
- [ ] Optimize long-running agent costs by 40%+
- [ ] Choose AGENTS.md vs Skills vs MCP correctly 95%+ of time
- [ ] Deploy agents in CI/CD with confidence
- [ ] Improve quality through systematic testing

### Overall Library Success
- [ ] Reduce time-to-deployment for new agent workflows by 70%
- [ ] Enable non-expert users to build effective agent teams
- [ ] Provide cost predictability (estimates within 20% of actuals)
- [ ] Support team collaboration on agent development
- [ ] Scale from single agents to complex multi-agent systems smoothly

## Current State & Constraints

**Target Users:**
- Software engineers building agent workflows
- Engineering managers coordinating multi-agent systems
- Product teams integrating AI agents into products
- Researchers automating literature review and analysis
- Data teams building intelligent pipelines

**Available Tools:**
- Claude Code, Cursor, Windsurf (agent harnesses)
- Jira, Linear, Notion, GitHub (integration targets)
- Various frameworks (Next.js, Python, etc.)

**Constraints:**
- Must work with current LLM capabilities (acknowledge trigger reliability issues)
- Token budgets matter (cost optimization is critical)
- Should be framework-agnostic where possible
- Need clear migration paths between harnesses

**Quality Standards:**
- All templates must be tested with real workflows
- Cost projections must be validated with actual runs
- Documentation must be clear enough for junior developers
- Strategies must reference research (not just opinions)

---

**Approach: Start with the orchestration infrastructure setup (specs/, shared-state/, utilities/), then build the common layer, then one complete team template (Code Implementation) as a reference implementation. We'll iterate and expand from there.**

**Critical Success Factor**: Each team template must include complete ORCHESTRATION.md with multi-agent coordination patterns, scenario-based validation, and clear user prompt points.

---

**Start by:**
1. Setting up the repository structure and orchestration files
2. Decomposing this prompt into /specs
3. Building the core utilities (file-lock-manager.py, status-updater.py)
4. Then proposing the high-level architecture for the template library