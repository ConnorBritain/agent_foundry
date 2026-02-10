# Universal Skills Library Specification

> **STATUS**: STATIC REFERENCE -- Extracted from master prompt. Never modified, only consulted.

## Purpose

Provide 10 universal SKILL.md templates for workflows that any agent might need regardless of use case. These skills conform to the agentskills.io specification and are designed to be portable across agent harnesses.

## Location

```
common/skills/
```

## Research Foundation

### Agent Skills Specification
- **Source**: https://agentskills.io/specification
- Official spec from Anthropic for portable skill definitions
- Progressive disclosure: metadata -> instructions -> resources
- Best for vertical, action-specific workflows

### Reference Implementations
- OpenAI skills: https://github.com/openai/skills/blob/main/skills/.curated/openai-docs/SKILL.md
- Figma implementation: https://github.com/openai/skills/blob/main/skills/.curated/figma-implement-design/SKILL.md
- Microsoft Playwright CLI: https://github.com/microsoft/playwright-cli/blob/main/skills/playwright-cli/SKILL.md

### Trigger Reliability Problem
From Vercel eval study:
- Skills have **56% non-trigger rate** without explicit instructions
- Instruction wording is fragile (small changes = big behavioral shifts)
- **Mitigation**: Multiple trigger patterns, explicit boundaries, examples of when to use AND when NOT to use

## Directory Structure

```
common/skills/
├── file-search/
│   ├── SKILL.md
│   ├── references/
│   │   ├── search-patterns.md
│   │   └── gitignore-rules.md
│   └── scripts/
│       └── recursive-search.sh
├── file-transform/
│   ├── SKILL.md
│   ├── references/
│   │   └── format-conversion-guide.md
│   └── scripts/
│       └── batch-processor.sh
├── web-research/
│   ├── SKILL.md
│   ├── references/
│   │   ├── search-strategies.md
│   │   └── source-evaluation.md
│   └── scripts/
│       └── citation-formatter.py
├── data-synthesizer/
│   ├── SKILL.md
│   ├── references/
│   │   └── synthesis-methodologies.md
│   └── scripts/
│       └── multi-source-combiner.py
├── code-review/
│   ├── SKILL.md
│   ├── references/
│   │   ├── language-linters.md
│   │   └── security-checklist.md
│   └── scripts/
│       └── static-analysis-runner.sh
├── test-generator/
│   ├── SKILL.md
│   ├── references/
│   │   └── testing-patterns.md
│   └── scripts/
│       └── test-template-generator.py
├── documentation-writer/
│   ├── SKILL.md
│   ├── references/
│   │   ├── doc-templates.md
│   │   └── style-guides.md
│   └── scripts/
│       └── doc-scaffolder.py
├── api-docs-generator/
│   ├── SKILL.md
│   ├── references/
│   │   └── openapi-patterns.md
│   └── scripts/
│       └── openapi-generator.py
├── status-reporter/
│   ├── SKILL.md
│   ├── references/
│   │   └── report-templates.md
│   └── scripts/
│       └── status-aggregator.py
└── blocker-identifier/
    ├── SKILL.md
    ├── references/
    │   └── dependency-analysis.md
    └── scripts/
        └── blocker-scanner.py
```

## SKILL.md Format (agentskills.io Compliant)

Every SKILL.md MUST follow this format:

```yaml
---
name: [lowercase-hyphenated-name]        # Required. Max 64 chars.
description: |                            # Required. Max 1024 chars.
  [Clear description of what this skill does,
   including multiple trigger patterns]
metadata:
  token_budget: [number]                  # Estimated tokens when fully loaded
  category: [file-ops|research|code-quality|documentation|project-mgmt]
  version: "1.0.0"
  author: "agent-template-library"
---

# [Skill Name]

## When to Invoke This Skill

[Multiple trigger patterns - addressing the 56% non-trigger problem]

### Trigger Phrases (USE this skill when you see these)
- "[phrase 1]"
- "[phrase 2]"
- "[phrase 3]"
- "[phrase 4]"

### DO NOT Use This Skill When
- [Counter-indicator 1]
- [Counter-indicator 2]

## Instructions

[Step-by-step workflow, <500 lines]

## References

[Pointers to references/ directory for on-demand loading]

## Scripts

[Pointers to scripts/ directory for executable code]
```

### Validation Rules (from agentskills.io)
1. YAML frontmatter is valid YAML
2. `name` field: lowercase, hyphens only, max 64 characters
3. `description` field: max 1024 characters, clear trigger language
4. All file references in the skill body must point to files that actually exist
5. No deeply nested references (max 1 level of indirection)
6. Total loaded size <5000 tokens

## The 10 Universal Skills

### Skill 1: file-search

**Category**: File Operations

```yaml
name: file-search
description: |
  Search codebases, documentation, and file systems for specific patterns,
  implementations, or content. Use when asked to find files, locate code,
  search for patterns, or discover implementations across a project.
metadata:
  token_budget: 3000
  category: file-ops
```

**Trigger Patterns**:
- "find files matching..."
- "search codebase for..."
- "locate implementation of..."
- "where is the code for..."
- "find all references to..."
- "grep for..." / "look for..."

**When NOT to Use**:
- Single file read (use direct file read instead)
- File creation or modification (use file-transform)
- Web search (use web-research)

**References**:
- `references/search-patterns.md`: Regex patterns, glob patterns, ripgrep flags
- `references/gitignore-rules.md`: Understanding which files to skip

**Scripts**:
- `scripts/recursive-search.sh`: Recursive search with filtering, respects .gitignore

**Token Budget**: ~3,000 tokens when fully loaded

---

### Skill 2: file-transform

**Category**: File Operations

```yaml
name: file-transform
description: |
  Batch file operations including format conversions, renaming, restructuring,
  and bulk modifications. Use when asked to convert files, rename patterns,
  restructure directories, or perform batch operations on multiple files.
metadata:
  token_budget: 2500
  category: file-ops
```

**Trigger Patterns**:
- "convert all X files to Y"
- "rename files matching..."
- "restructure the directory..."
- "batch update files..."
- "change format of..."
- "migrate files from... to..."

**When NOT to Use**:
- Searching for files (use file-search)
- Single file edit (use direct edit)
- Code refactoring (use code-review for analysis first)

**References**:
- `references/format-conversion-guide.md`: Supported format conversions and rules

**Scripts**:
- `scripts/batch-processor.sh`: Batch processing utilities with dry-run mode

**Token Budget**: ~2,500 tokens when fully loaded

---

### Skill 3: web-research

**Category**: Research and Analysis

```yaml
name: web-research
description: |
  Conduct structured web research with proper citation and source evaluation.
  Use when asked to research topics, find latest information, gather data
  from the web, or compile information from online sources.
metadata:
  token_budget: 4000
  category: research
```

**Trigger Patterns**:
- "research [topic]"
- "find latest information on..."
- "what is the current state of..."
- "gather data about..."
- "look up..." / "find out about..."
- "compile information on..."

**When NOT to Use**:
- Information already available in local files (use file-search)
- Codegen from known patterns (use framework AGENTS.md context)
- Opinion or analysis (use data-synthesizer after gathering facts)

**References**:
- `references/search-strategies.md`: Boolean operators, site-specific search, date filtering
- `references/source-evaluation.md`: CRAAP test, source reliability criteria, bias detection

**Outputs**: Cited findings in structured format with source URLs, reliability ratings, and date accessed.

**Token Budget**: ~4,000 tokens when fully loaded

---

### Skill 4: data-synthesizer

**Category**: Research and Analysis

```yaml
name: data-synthesizer
description: |
  Combine information from multiple sources into coherent analysis.
  Use when asked to synthesize findings, combine data, create summaries
  from multiple inputs, or produce integrated analysis reports.
metadata:
  token_budget: 3500
  category: research
```

**Trigger Patterns**:
- "synthesize findings from..."
- "combine data from..."
- "summarize across these sources..."
- "create an integrated view of..."
- "merge information from..."
- "what do these sources tell us about..."

**When NOT to Use**:
- Single source summary (use direct summarization)
- Data gathering (use web-research or file-search first)
- Formatting only (use documentation-writer or status-reporter)

**References**:
- `references/synthesis-methodologies.md`: Thematic synthesis, narrative synthesis, framework synthesis, meta-synthesis

**Scripts**:
- `scripts/multi-source-combiner.py`: Structured input combination with conflict detection

**Token Budget**: ~3,500 tokens when fully loaded

---

### Skill 5: code-review

**Category**: Code Quality

```yaml
name: code-review
description: |
  Review code changes with systematic quality checks covering correctness,
  security, performance, and style. Use when asked to review code, check
  for issues, assess code quality, or provide feedback on implementations.
metadata:
  token_budget: 5000
  category: code-quality
```

**Trigger Patterns**:
- "review this code"
- "check for issues in..."
- "what problems do you see in..."
- "is this implementation correct?"
- "review my changes"
- "code review for..."
- "assess the quality of..."

**When NOT to Use**:
- Writing new code (use the code implementation workflow)
- Generating tests (use test-generator)
- Reviewing documentation (use documentation-writer conventions)

**References**:
- `references/language-linters.md`: ESLint, Pylint, Clippy, golint rules and configurations
- `references/security-checklist.md`: OWASP Top 10, injection patterns, auth issues, data exposure

**Scripts**:
- `scripts/static-analysis-runner.sh`: Run linters and static analysis tools, aggregate results

**Review Dimensions**:
1. **Correctness**: Logic errors, edge cases, error handling
2. **Security**: Injection, auth bypass, data exposure, secrets
3. **Performance**: N+1 queries, unnecessary allocations, algorithmic complexity
4. **Maintainability**: Naming, complexity, duplication, documentation
5. **Style**: Consistency with project conventions, formatting
6. **Testing**: Adequate coverage, edge case tests, mocking strategy

**Token Budget**: ~5,000 tokens when fully loaded

---

### Skill 6: test-generator

**Category**: Code Quality

```yaml
name: test-generator
description: |
  Create test cases from requirements, code, or specifications. Generates
  unit tests, integration tests, and edge case tests. Use when asked to
  generate tests, create test coverage, or write test cases for code.
metadata:
  token_budget: 4000
  category: code-quality
```

**Trigger Patterns**:
- "generate tests for..."
- "create test coverage for..."
- "write tests for this function"
- "what tests should I write?"
- "test this code"
- "add test cases for..."
- "create unit tests for..."

**When NOT to Use**:
- Running existing tests (use direct command execution)
- Reviewing test quality (use code-review)
- Test infrastructure setup (use framework AGENTS.md context)

**References**:
- `references/testing-patterns.md`: Patterns by framework (pytest, Jest, Vitest, XCTest, JUnit), mocking strategies, fixture patterns, parameterized tests

**Scripts**:
- `scripts/test-template-generator.py`: Generate test file scaffolding from function signatures

**Test Categories Generated**:
1. **Happy path**: Normal inputs, expected outputs
2. **Edge cases**: Boundary values, empty inputs, max values
3. **Error cases**: Invalid inputs, missing data, timeout/failure
4. **Integration**: Component interactions, API contracts
5. **Regression**: Previously-fixed bugs, known failure modes

**Token Budget**: ~4,000 tokens when fully loaded

---

### Skill 7: documentation-writer

**Category**: Documentation

```yaml
name: documentation-writer
description: |
  Generate documentation from code, specifications, or requirements.
  Produces READMEs, API docs, inline comments, and user guides.
  Use when asked to document code, create READMEs, or write guides.
metadata:
  token_budget: 3500
  category: documentation
```

**Trigger Patterns**:
- "document this API"
- "create README for..."
- "write documentation for..."
- "add inline comments to..."
- "create a user guide for..."
- "generate docs for this project"
- "explain this code in documentation"

**When NOT to Use**:
- API reference docs specifically (use api-docs-generator)
- Status reports (use status-reporter)
- Content writing / blog posts (use Content Creation Team)

**References**:
- `references/doc-templates.md`: README template, contributing guide template, architecture doc template
- `references/style-guides.md`: Technical writing best practices, audience-appropriate language

**Scripts**:
- `scripts/doc-scaffolder.py`: Generate documentation file structure from project layout

**Documentation Types**:
1. **README**: Overview, quickstart, installation, usage, contributing
2. **API docs**: Endpoints, parameters, responses, examples (see api-docs-generator for full reference)
3. **Architecture**: System design, data flow, component relationships
4. **User guide**: Step-by-step instructions, screenshots, troubleshooting
5. **Inline comments**: Function/class docstrings, complex logic explanation

**Token Budget**: ~3,500 tokens when fully loaded

---

### Skill 8: api-docs-generator

**Category**: Documentation

```yaml
name: api-docs-generator
description: |
  Generate API reference documentation from code, OpenAPI specs, or
  endpoint definitions. Produces structured API references with examples.
  Use when asked to generate API docs, create reference documentation,
  or document REST/GraphQL endpoints.
metadata:
  token_budget: 4000
  category: documentation
```

**Trigger Patterns**:
- "generate API docs"
- "create reference for these endpoints"
- "document the REST API"
- "create OpenAPI spec for..."
- "generate Swagger docs"
- "document this GraphQL schema"
- "create API reference documentation"

**When NOT to Use**:
- General project documentation (use documentation-writer)
- Code-level documentation (use documentation-writer for inline docs)
- Status reports about API changes (use status-reporter)

**References**:
- `references/openapi-patterns.md`: OpenAPI 3.1 spec patterns, schema definitions, example generation

**Scripts**:
- `scripts/openapi-generator.py`: Generate OpenAPI spec from code annotations or route definitions

**Output Formats**:
1. **OpenAPI 3.1 YAML/JSON**: Machine-readable API specification
2. **Markdown reference**: Human-readable endpoint documentation
3. **Example collection**: Request/response examples per endpoint
4. **Client SDK stubs**: Type definitions for API consumers

**Token Budget**: ~4,000 tokens when fully loaded

---

### Skill 9: status-reporter

**Category**: Project Management

```yaml
name: status-reporter
description: |
  Gather and format status updates for projects, sprints, or workflows.
  Produces reports tailored to different stakeholder types (technical,
  executive, team). Use when asked to report status, summarize progress,
  or create updates.
metadata:
  token_budget: 3000
  category: project-mgmt
```

**Trigger Patterns**:
- "generate status report"
- "summarize progress on..."
- "what is the current status of..."
- "create a standup update"
- "prepare status for stakeholders"
- "weekly update for..."
- "sprint report for..."

**When NOT to Use**:
- Detailed code analysis (use code-review)
- Research summary (use data-synthesizer)
- Project planning (use Project Planning Team)

**References**:
- `references/report-templates.md`: Templates by stakeholder type (executive, technical, team, client), cadence (daily, weekly, sprint, monthly)

**Scripts**:
- `scripts/status-aggregator.py`: Pull status from multiple sources (git log, issue tracker, shared-state)

**Report Sections**:
1. **Summary**: One-paragraph overview
2. **Completed**: What was done since last report
3. **In Progress**: What is actively being worked on
4. **Blocked**: What is stuck and why
5. **Upcoming**: What is next
6. **Metrics**: Velocity, burndown, cycle time (where applicable)
7. **Risks**: New or changed risks

**Token Budget**: ~3,000 tokens when fully loaded

---

### Skill 10: blocker-identifier

**Category**: Project Management

```yaml
name: blocker-identifier
description: |
  Identify dependencies, blockers, and risks in projects or workflows.
  Analyzes task relationships, resource constraints, and external
  dependencies. Use when asked to find blockers, identify dependencies,
  or assess what is preventing progress.
metadata:
  token_budget: 2500
  category: project-mgmt
```

**Trigger Patterns**:
- "identify blockers for..."
- "what is blocking..."
- "find dependencies for..."
- "what is preventing progress on..."
- "risk assessment for..."
- "dependency analysis for..."
- "what could go wrong with..."

**When NOT to Use**:
- Code dependency analysis (use static analysis tools directly)
- General research (use web-research)
- Status reporting (use status-reporter, which may invoke this skill)

**References**:
- `references/dependency-analysis.md`: Dependency mapping patterns, critical path identification, risk matrix construction

**Scripts**:
- `scripts/blocker-scanner.py`: Scan issue tracker and git history for blocked items, stale branches, dependency cycles

**Blocker Categories**:
1. **Technical**: Missing APIs, infrastructure not ready, performance issues
2. **Resource**: People unavailable, skills gap, capacity constraints
3. **External**: Third-party dependencies, vendor delays, regulatory
4. **Process**: Approval needed, review pending, environment access
5. **Knowledge**: Unclear requirements, missing documentation, domain expertise needed

**Token Budget**: ~2,500 tokens when fully loaded

## Skill Design Principles

### 1. Trigger Reliability (Addressing the 56% Problem)

Every skill MUST include:
- **Minimum 5 trigger phrases**: Different ways users express the same intent
- **Explicit negatives**: "Do NOT use this skill when..." (prevents false triggering)
- **Boundary examples**: Edge cases that clarify skill scope
- **Active verb descriptions**: Start with action verbs in the description field

**Top 5 Description Patterns That Maximize Trigger Reliability**:

1. **Action-first**: "Search codebases, documentation, and file systems for..." (starts with what the skill DOES)
2. **Multi-synonym**: Include synonyms in description ("find, locate, search, discover, grep")
3. **Context-rich**: Describe the situation, not just the action ("Use when asked to find files, locate code, search for patterns")
4. **Negative boundary**: "Use for X. Do NOT use for Y." (explicit scope)
5. **Output-oriented**: Describe what the skill produces ("Produces cited findings in structured format")

### 2. Progressive Disclosure

```
SKILL.md (metadata + instructions)    # Always loaded: 50-100 tokens (metadata only)
  └── references/                      # Loaded on-demand: variable
       ├── detailed-guide.md           # Deep reference material
       └── examples.md                 # Extended examples
  └── scripts/                         # Loaded on-demand: variable
       └── helper-script.py            # Executable code
```

- **SKILL.md body**: <500 lines, focused on workflow steps
- **references/**: Detailed content loaded only when the skill is activated
- **scripts/**: Executable code loaded only when needed
- **Total loaded**: <5000 tokens (body + loaded references + loaded scripts)

### 3. Token-Efficient Design

- Target: <5000 tokens total when fully loaded
- Metadata only: 50-100 tokens
- Body only: 200-500 tokens
- Body + references: 1500-4000 tokens
- Body + references + scripts: 2500-5000 tokens
- Include measured token counts in metadata
- Document what was compressed or excluded and why

### 4. Bundled Scripts

Scripts MUST include:
- Shebang line and language identifier
- Usage comment at top
- Error handling for common failures
- Dry-run mode where applicable (especially for destructive operations)
- Exit codes (0=success, 1=error, 2=warning)
- stdin/stdout/stderr usage following Unix conventions

## Universal vs Team-Specific Skills: Decision Criteria

A skill belongs in `common/skills/` (universal) when:
- It is used by 3+ team templates
- It has no domain-specific assumptions
- It works with any programming language or framework
- It does not require team-specific configuration

A skill belongs in `teams/[team]/agents/[agent]/skills/` (team-specific) when:
- It is used by only 1-2 team templates
- It requires domain-specific knowledge (e.g., HIPAA compliance checks)
- It depends on team-specific configuration or context
- It references team-specific tools or workflows

## Validation

All skills MUST pass validation via `common/utilities/skill-validator.py`:
- YAML frontmatter is valid
- `name` matches format: lowercase, hyphens, max 64 chars
- `description` is present and max 1024 chars
- All file references resolve to existing files
- No deeply nested references (max 1 level)
- Token budget is specified and accurate (within 10%)

## Cross-References

- **Implementation location**: `common/skills/`
- **Validator utility**: `common/utilities/skill-validator.py` (see `specs/01-common-layer/utilities/SPEC.md`)
- **Token calculator**: `common/utilities/token-calculator.py`
- **agentskills.io spec**: https://agentskills.io/specification
- **Consumer templates**: All team templates reference these skills
- **Parent spec**: `specs/01-common-layer/SPEC.md`
- **Master prompt**: `specs/MASTER_PROMPT.md` (Section: 1C - Universal SKILL.md Templates)
