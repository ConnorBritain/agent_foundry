---
skill_name: "documentation"
version: "1.0.0"
description: "Generates structured documentation for APIs, READMEs, architecture decisions, and codebases"
author: "Agent Foundry"
triggers:
  - "when asked to write or generate documentation"
  - "when asked to document an API endpoint or module"
  - "when asked to create a README"
  - "when asked to write architecture docs or ADRs"
  - "when asked to explain how code works for documentation purposes"
---

# Documentation Skill

## Purpose
Generate clear, accurate, and maintainable documentation from code, specifications, or requirements. Produce documents that serve their intended audience and follow established standards.

## Document Types & Templates

### 1. API Documentation
Generate from code analysis or OpenAPI spec.

#### Endpoint Documentation Format
```markdown
## `METHOD /path/to/endpoint`

**Description**: What this endpoint does in one sentence.

**Authentication**: Required | Optional | None

**Request**
| Parameter | Location | Type | Required | Description |
|---|---|---|---|---|
| id | path | string (UUID) | yes | Resource identifier |
| limit | query | integer | no | Max results (default: 20, max: 100) |

**Request Body** (if applicable)
\`\`\`json
{
  "field": "value",
  "nested": { "key": "value" }
}
\`\`\`

**Response** `200 OK`
\`\`\`json
{
  "data": { ... },
  "meta": { "request_id": "req_abc" }
}
\`\`\`

**Error Responses**
| Status | Code | Description |
|---|---|---|
| 400 | VALIDATION_ERROR | Invalid request parameters |
| 401 | UNAUTHORIZED | Missing or invalid auth token |
| 404 | NOT_FOUND | Resource does not exist |

**Example**
\`\`\`bash
curl -X GET https://api.example.com/path \
  -H "Authorization: Bearer token"
\`\`\`
```

### 2. README Template
```markdown
# Project Name

Brief description of what this project does and who it's for.

## Features
- Feature 1: description
- Feature 2: description

## Quick Start

### Prerequisites
- Node.js 20+
- pnpm 9+

### Installation
\`\`\`bash
pnpm install
cp .env.example .env.local
# Configure environment variables
pnpm dev
\`\`\`

### Environment Variables
| Variable | Required | Description |
|---|---|---|
| DATABASE_URL | yes | PostgreSQL connection string |
| NEXTAUTH_SECRET | yes | Random string for session encryption |

## Project Structure
\`\`\`
src/
  app/           # Next.js App Router pages
  components/    # React components
  lib/           # Shared utilities
  server/        # Server-side code
\`\`\`

## Development
\`\`\`bash
pnpm dev        # Start dev server
pnpm build      # Production build
pnpm test       # Run tests
pnpm lint       # Lint code
\`\`\`

## Deployment
Deployed via [platform]. See deployment docs for details.

## Contributing
See CONTRIBUTING.md for guidelines.
```

### 3. Architecture Decision Record (ADR)
```markdown
# ADR-{number}: {Title}

**Date**: YYYY-MM-DD
**Status**: Proposed | Accepted | Deprecated | Superseded by ADR-X
**Deciders**: [list of people]

## Context
What is the issue that motivates this decision? What forces are at play?

## Decision
What is the change proposed or decided?

## Consequences

### Positive
- Benefit 1
- Benefit 2

### Negative
- Tradeoff 1
- Tradeoff 2

### Risks
- Risk 1 and mitigation

## Alternatives Considered

### Option A: [Name]
- Pros: ...
- Cons: ...

### Option B: [Name]
- Pros: ...
- Cons: ...
```

### 4. Module/Component Documentation
```markdown
# Module: {Name}

## Overview
What this module does and its role in the system.

## Dependencies
- External: list of external dependencies
- Internal: list of internal modules this depends on

## Public API

### `functionName(params): ReturnType`
Description of what it does.
- `param1` (Type): description
- Returns: description of return value
- Throws: conditions that cause errors

## Usage Examples
\`\`\`typescript
import { functionName } from '@/modules/name';
const result = functionName(input);
\`\`\`

## Configuration
Explain any configuration options.

## Architecture Notes
Key design decisions and patterns used.
```

## Documentation Generation Process

### Step 1: Analyze Source
- Read the code/files to be documented
- Identify public API surface (exports, routes, components)
- Map dependencies and relationships
- Note configuration requirements

### Step 2: Identify Audience
| Audience | Focus | Tone |
|---|---|---|
| New developers | Setup, getting started, concepts | Detailed, step-by-step |
| Team members | Architecture, decisions, patterns | Concise, reference-style |
| API consumers | Endpoints, auth, examples | Precise, code-heavy |
| End users | Features, how-to guides | Plain language, task-oriented |

### Step 3: Write with Standards
- Use clear, simple language (no jargon without definition)
- Include working code examples for every public API
- Keep examples minimal but complete (copy-pasteable)
- Use tables for structured reference data
- Use consistent formatting and heading hierarchy
- Include "last updated" dates for time-sensitive docs

### Step 4: Validate
- Verify code examples compile/run
- Check all links are valid
- Confirm environment variable names match code
- Ensure API documentation matches actual implementation

## Documentation Quality Rules
| Rule | Detail |
|---|---|
| Accuracy | Docs must match current code — outdated docs are worse than none |
| Completeness | Cover all public APIs, required config, error cases |
| Conciseness | Say it once, say it clearly, don't repeat |
| Examples | Every API needs at least one working example |
| Searchability | Use descriptive headings, consistent naming |
| Maintenance | Prefer generated docs from code over hand-written |

## Anti-Patterns to Avoid
- Documentation that restates the code ("increments counter by 1")
- Missing error cases and edge conditions
- Examples that don't work or require unstated prerequisites
- Mixing reference docs with tutorials
- Documenting internal/private APIs (they change frequently)
- Using screenshots of text (not searchable, not accessible)
