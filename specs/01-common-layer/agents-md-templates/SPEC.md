# AGENTS.md Templates Specification

> **STATUS**: STATIC REFERENCE -- Extracted from master prompt. Never modified, only consulted.

## Purpose

Provide reusable, compressed AGENTS.md templates that give agents passive access to framework knowledge, domain expertise, and tool integration patterns. Based on Vercel's research showing AGENTS.md achieves 100% pass rate vs Skills at 79%, these templates serve as the primary mechanism for horizontal knowledge delivery.

## Location

```
common/agents-md/
```

## Research Foundation

### Why AGENTS.md Over Skills for Knowledge

From the Vercel eval study (https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals):
- AGENTS.md achieved **100% pass rate** vs Skills at **79%** (with explicit instructions)
- Skills **failed to trigger in 56% of cases** without explicit prompting
- **Passive context beats active retrieval** for framework knowledge
- The instruction "Prefer retrieval-led reasoning over pre-training-led reasoning" is critical

### Architecture Pattern
- **Horizontal knowledge** (framework APIs, broad docs) -> AGENTS.md
- **Vertical workflows** (specific tasks, triggered actions) -> Skills
- AGENTS.md is always-available context; Skills are on-demand tools

## Template Categories

### Category 1: Framework Knowledge Templates (4 templates)

#### framework-nextjs.md
- **Size**: ~8KB compressed
- **Coverage**: App Router, Server Components, Server Actions, caching APIs
- **Version specificity**: Next.js 15, 14, 13 (version-tagged sections)
- **Critical instruction**: MUST include "Prefer retrieval-led reasoning" pattern
- **Contents**:
  - Routing: pages, layouts, loading states, error boundaries, route groups, parallel routes, intercepting routes
  - Data fetching: Server Components, Server Actions, use client directive, revalidation
  - Caching: Full Route Cache, Data Cache, Router Cache, cache invalidation
  - Rendering: Static, Dynamic, Streaming, PPR (Partial Prerendering)
  - Middleware: matcher config, edge runtime, request/response manipulation
  - API routes: Route Handlers, request/response types
  - Configuration: next.config.js options, environment variables
  - Deployment: Vercel-specific, self-hosted, Docker

#### framework-python-fastapi.md
- **Size**: ~6KB compressed
- **Coverage**: Routing, dependencies, async patterns, Pydantic models
- **Contents**:
  - Routing: path operations, path parameters, query parameters, request body
  - Dependencies: Depends(), security dependencies, database sessions
  - Async patterns: async def vs def, background tasks, WebSocket
  - Pydantic: model definition, validation, serialization, nested models
  - Middleware: CORS, authentication, logging, error handling
  - Database: SQLAlchemy integration, async database access
  - Testing: TestClient, pytest fixtures, dependency overrides
  - Deployment: uvicorn, gunicorn, Docker, production config

#### framework-react.md
- **Size**: ~7KB compressed
- **Coverage**: React hooks, patterns, best practices
- **Contents**:
  - Hooks: useState, useEffect, useContext, useReducer, useMemo, useCallback, useRef, useId
  - Custom hooks: patterns, rules, testing
  - Patterns: composition, render props, higher-order components, compound components
  - State management: local state, context, external stores (Zustand, Jotai)
  - Performance: React.memo, lazy loading, Suspense, concurrent features
  - Forms: controlled vs uncontrolled, form libraries integration
  - Error boundaries: implementation, error recovery
  - Server Components: RSC patterns, client/server boundary

#### framework-typescript.md
- **Size**: ~5KB compressed
- **Coverage**: TypeScript patterns and type system
- **Contents**:
  - Type system: union types, intersection types, literal types, template literals
  - Generics: constraints, inference, utility types, conditional types
  - Patterns: discriminated unions, branded types, builder pattern
  - Configuration: tsconfig.json options, strict mode
  - Module system: imports, exports, declaration files
  - Advanced: mapped types, infer keyword, recursive types
  - Practical: type narrowing, type guards, assertion functions
  - Integration: React types, Node.js types, third-party type definitions

### Category 2: Domain Knowledge Templates (3 templates)

#### domain-healthcare.md
- **Size**: ~10KB compressed
- **Coverage**: HIPAA compliance, medical terminology, healthcare workflows, HL7/FHIR
- **Contents**:
  - HIPAA: Privacy Rule, Security Rule, PHI handling, BAAs, minimum necessary principle
  - Data standards: HL7 v2, HL7 FHIR (resources, bundles, operations), ICD-10, SNOMED CT, LOINC
  - Clinical workflows: patient intake, orders, results, care coordination
  - Interoperability: SMART on FHIR, CDS Hooks, bulk data access
  - Security: encryption requirements, access controls, audit logging, breach notification
  - Terminology: common medical abbreviations, drug databases (RxNorm), lab value ranges
  - Compliance: meaningful use, ONC certification, state-specific regulations
  - Architecture patterns: EHR integration, patient portals, telehealth platforms

#### domain-finance.md
- **Size**: ~9KB compressed
- **Coverage**: SOC2, PCI-DSS, payment processing security, financial data handling
- **Contents**:
  - SOC2: Trust Service Criteria, evidence collection, audit preparation
  - PCI-DSS: cardholder data environment, SAQ types, network segmentation, tokenization
  - Payment processing: payment gateways, 3D Secure, recurring billing, refunds
  - Financial data: transaction processing, reconciliation, double-entry bookkeeping
  - Regulatory: KYC/AML, GDPR for financial data, SEC/FINRA (if applicable)
  - Security: encryption at rest/transit, key management, fraud detection
  - APIs: Stripe, Plaid, open banking standards
  - Architecture patterns: event sourcing for ledgers, idempotency, saga pattern

#### domain-research.md
- **Size**: ~8KB compressed
- **Coverage**: Academic standards, research methodologies, citation formats
- **Contents**:
  - Methodologies: experimental design, observational studies, meta-analysis, systematic review, qualitative methods
  - Statistical methods: hypothesis testing, regression, Bayesian methods, effect sizes, power analysis
  - Citation formats: APA 7th, MLA 9th, Chicago 17th, Vancouver, Harvard
  - Literature review: systematic search strategies, PRISMA guidelines, inclusion/exclusion criteria
  - Data management: research data management plans, FAIR principles, open data
  - Ethics: IRB requirements, informed consent, data anonymization
  - Publication: journal selection, peer review process, preprint servers
  - Tools: reference managers (Zotero, Mendeley), statistical software, LaTeX

### Category 3: Tool Integration Templates (4 templates)

#### tools-jira.md
- **Size**: ~5KB compressed
- **Coverage**: Jira API patterns, JQL syntax, common workflows
- **Contents**:
  - REST API: issue CRUD, transitions, comments, attachments, bulk operations
  - JQL syntax: field operators, functions, ORDER BY, sub-queries
  - Workflows: status transitions, custom workflows, automation rules
  - Project management: boards (Scrum/Kanban), sprints, epics, versions
  - Custom fields: creation, configuration, context
  - Webhooks: event types, payload structure, registration
  - Common patterns: issue creation templates, status reporting queries, sprint metrics
  - Authentication: API tokens, OAuth 2.0, personal access tokens

#### tools-linear.md
- **Size**: ~4KB compressed
- **Coverage**: Linear API, project structure, workflow automation
- **Contents**:
  - GraphQL API: queries, mutations, subscriptions
  - Data model: teams, projects, issues, cycles, labels, milestones
  - Workflow: issue states, automations, templates
  - Integration: webhooks, OAuth, API keys
  - Common patterns: issue creation, bulk updates, cycle planning
  - Triage: inbox management, auto-assignment, SLA tracking

#### tools-notion.md
- **Size**: ~6KB compressed
- **Coverage**: Notion API, database operations, page creation
- **Contents**:
  - REST API: pages, databases, blocks, users, search
  - Database operations: create, query (filters, sorts), update properties
  - Block types: text, headings, lists, code, callout, toggle, table
  - Page creation: templates, properties, content blocks
  - Properties: title, rich text, number, select, multi-select, date, relation, rollup, formula
  - Pagination: cursor-based, handling large datasets
  - Common patterns: knowledge base creation, project tracking databases, content calendars
  - Authentication: internal integration, public integration, OAuth

#### tools-github.md
- **Size**: ~7KB compressed
- **Coverage**: GitHub API, PR workflows, Actions
- **Contents**:
  - REST API v3: repos, issues, pulls, reviews, comments, releases
  - GraphQL API v4: queries, mutations, node IDs
  - PR workflows: creation, review assignment, status checks, merge strategies
  - Actions: workflow syntax, triggers, jobs, steps, matrix strategies, secrets
  - Webhooks: event types, payload delivery, security validation
  - Code review: review comments, suggestions, required reviewers, CODEOWNERS
  - Releases: semantic versioning, changelogs, assets
  - Authentication: GitHub Apps, personal access tokens, GITHUB_TOKEN in Actions

## Compression Format

All templates MUST use pipe-delimited index style for token efficiency.

### Format Specification

```
[Template Name Index]|root: ./[path-to-docs]
|IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning
|01-section-name:{file1.md,file2.md,file3.md}
|02-section-name:{file1.md,file2.md}
|03-section-name:{file1.md}
|KEY-CONCEPTS: concept1|concept2|concept3
|PATTERNS: pattern1(params)|pattern2(params)
|AVOID: anti-pattern1|anti-pattern2
```

### Compression Guidelines

1. **API references**: Use function signatures with parameter types, pipe-separated
   ```
   |GET /api/endpoint(param1:type,param2:type)->ResponseType
   |POST /api/endpoint{body:BodyType}->ResponseType
   ```

2. **Prose guides**: Extract key principles, compress to single-line rules
   ```
   |RULE: Always use server components for data fetching
   |RULE: Client components only for interactivity (useState, useEffect, event handlers)
   ```

3. **Code examples**: Reference file paths instead of inlining
   ```
   |EXAMPLE: server-action-form -> references/server-action-form.tsx
   |EXAMPLE: api-route-handler -> references/api-route-handler.ts
   ```

4. **Version-specific content**: Tag with version markers
   ```
   |[v15] PPR: Partial Prerendering enabled by default
   |[v14] App Router: stable, recommended for new projects
   |[v13] App Router: experimental, use pages/ for production
   ```

### Token Budget Targets

| Template | Compressed Size | Uncompressed Estimate | Compression Ratio |
|----------|-----------------|----------------------|-------------------|
| framework-nextjs.md | ~8KB (~2000 tokens) | ~40KB (~10000 tokens) | 80% |
| framework-python-fastapi.md | ~6KB (~1500 tokens) | ~30KB (~7500 tokens) | 80% |
| framework-react.md | ~7KB (~1750 tokens) | ~35KB (~8750 tokens) | 80% |
| framework-typescript.md | ~5KB (~1250 tokens) | ~25KB (~6250 tokens) | 80% |
| domain-healthcare.md | ~10KB (~2500 tokens) | ~50KB (~12500 tokens) | 80% |
| domain-finance.md | ~9KB (~2250 tokens) | ~45KB (~11250 tokens) | 80% |
| domain-research.md | ~8KB (~2000 tokens) | ~40KB (~10000 tokens) | 80% |
| tools-jira.md | ~5KB (~1250 tokens) | ~25KB (~6250 tokens) | 80% |
| tools-linear.md | ~4KB (~1000 tokens) | ~20KB (~5000 tokens) | 80% |
| tools-notion.md | ~6KB (~1500 tokens) | ~30KB (~7500 tokens) | 80% |
| tools-github.md | ~7KB (~1750 tokens) | ~35KB (~8750 tokens) | 80% |

Target: 80%+ compression ratio across all templates (Vercel benchmark).

## Template Requirements

Each template MUST include:

### 1. Header Block
```markdown
# [Template Name] AGENTS.md Template
> Category: [Framework|Domain|Tool Integration]
> Token Budget: ~[X]KB compressed (~[Y] tokens)
> Last Updated: [ISO8601]
> Versions: [applicable versions or "N/A"]
```

### 2. Compression Format Section
The actual pipe-delimited index content.

### 3. Usage Instructions
```markdown
## When to Use
- [Decision criteria for including this template]

## When NOT to Use
- [Counter-indicators]

## How to Include
1. Copy this file to your agent's directory
2. Reference in AGENTS.md: `@import ./[template-name].md`
3. Customize version-specific sections as needed
```

### 4. Decompression Script Reference
```markdown
## Decompression
To expand this compressed index into full documentation:
```bash
python common/utilities/agents-md-compressor.py decompress [template-name].md --output ./docs/
```
```

### 5. Customization Points
Clearly marked sections that users should modify for their specific use case.

## Decision Criteria: AGENTS.md vs Skill vs MCP

Include this decision matrix in each template:

| Criterion | AGENTS.md | Skill | MCP |
|-----------|-----------|-------|-----|
| Knowledge type | Horizontal, reference | Vertical, workflow | Persistent, API |
| Availability | 100% (passive context) | ~44-79% (trigger-dependent) | 100% (server-dependent) |
| Token cost | Always loaded | On-demand | Per-call |
| Best for | Framework docs, patterns | Specific tasks, workflows | External tool APIs |
| Update frequency | Per-deployment | Per-activation | Real-time |

**Use this template (AGENTS.md) when**:
- Knowledge is needed across many interactions
- Consistent availability is critical
- Content is reference material, not a workflow
- Token budget allows always-loaded context

**Use a Skill instead when**:
- Content is a specific workflow or procedure
- Token budget requires on-demand loading
- Trigger patterns are well-defined and reliable

**Use MCP instead when**:
- Real-time data from external APIs is needed
- Persistent tool connections are required
- The tool has its own server infrastructure

## Cross-References

- **Implementation location**: `common/agents-md/`
- **Compressor utility**: `common/utilities/agents-md-compressor.py` (see `specs/01-common-layer/utilities/SPEC.md`)
- **Token calculator**: `common/utilities/token-calculator.py`
- **Consumer templates**: All team templates in `teams/*/agents/*/AGENTS.md`
- **Parent spec**: `specs/01-common-layer/SPEC.md`
- **Master prompt**: `specs/MASTER_PROMPT.md` (Section: 1B - AGENTS.md Template Collection)
- **Research**: Vercel eval study, agentskills.io specification

## Optimization Guidance

### Compression Techniques by Content Type

#### API References
- Strip descriptions, keep signatures
- Use abbreviated type notation (s=string, n=number, b=boolean, a=array, o=object)
- Group by HTTP method
- Reference external docs for detailed descriptions

#### Configuration Options
- Key=default format, one per line
- Group by category
- Only include non-obvious options

#### Patterns and Best Practices
- One-line rules with RULE: prefix
- AVOID: prefix for anti-patterns
- PREFER: prefix for recommended approaches

#### Code Examples
- Reference files instead of inlining
- Keep only the minimal example that demonstrates the pattern
- Strip comments unless critical for understanding

### Measuring Token Efficiency
Use `common/utilities/token-calculator.py` to:
1. Measure token count of compressed template
2. Compare with uncompressed equivalent
3. Verify compression ratio meets 80% target
4. Validate total context budget when combined with other templates
