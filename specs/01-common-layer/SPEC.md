# Common Layer Specification

> **STATUS**: STATIC REFERENCE -- Extracted from master prompt. Never modified, only consulted.

## Purpose

The Common Layer provides universal building blocks used across all agent implementations in Agent Foundry. These are foundational templates, skills, personalities, and utilities that any team template or standalone agent can reference.

## Architecture Overview

```
common/
├── agents-md/                         # Reusable AGENTS.md templates
│   ├── framework-nextjs.md
│   ├── framework-python-fastapi.md
│   ├── framework-react.md
│   ├── framework-typescript.md
│   ├── domain-healthcare.md
│   ├── domain-finance.md
│   ├── domain-research.md
│   ├── tools-jira.md
│   ├── tools-linear.md
│   ├── tools-notion.md
│   └── tools-github.md
├── skills/                            # Universal SKILL.md templates
│   ├── file-search/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   └── scripts/
│   ├── file-transform/
│   ├── web-research/
│   ├── data-synthesizer/
│   ├── code-review/
│   ├── test-generator/
│   ├── documentation-writer/
│   ├── api-docs-generator/
│   ├── status-reporter/
│   └── blocker-identifier/
└── utilities/
    ├── token-calculator.py
    ├── skill-validator.py
    ├── agents-md-compressor.py
    └── cost-estimator.py

personalities/                         # Top-level personality library
├── README.md
├── skeptical-critic.md
├── enthusiastic-supporter.md
├── cautious-analyst.md
├── pragmatic-builder.md
├── strategic-visionary.md
├── detail-perfectionist.md
├── customer-champion.md
├── technical-purist.md
├── rapid-executor.md
├── diplomatic-facilitator.md
└── customization-guide.md
```

## Subsections

The Common Layer is composed of four subsections, each with its own detailed SPEC.md:

### 1. Personalities (`personalities/`)

**Spec**: `specs/01-common-layer/personalities/SPEC.md`

A reusable personality library that team templates reference. Contains 10 pre-built personas plus a customization guide. Each personality defines core traits, communication style, decision-making approach, trigger conditions, example system prompt snippets, and compatible team roles.

Personalities live at the top level (`personalities/`) rather than inside `common/` because they are cross-cutting concerns referenced by every team template.

### 2. AGENTS.md Templates (`common/agents-md/`)

**Spec**: `specs/01-common-layer/agents-md-templates/SPEC.md`

Compressed documentation index templates in three categories:
- **Framework Knowledge** (4 templates): Next.js, FastAPI, React, TypeScript
- **Domain Knowledge** (3 templates): Healthcare, Finance, Research
- **Tool Integration** (4 templates): Jira, Linear, Notion, GitHub

All templates use Vercel-style pipe-delimited compression format for token efficiency. Based on research showing AGENTS.md achieves 100% pass rate vs Skills at 79%.

### 3. Universal Skills (`common/skills/`)

**Spec**: `specs/01-common-layer/skills/SPEC.md`

10 universal skill templates conforming to the agentskills.io specification. Each skill provides a workflow that any agent might need regardless of use case. Skills use progressive disclosure (metadata -> instructions -> resources) and stay under 5000 tokens when fully loaded.

### 4. Common Utilities (`common/utilities/`)

**Spec**: `specs/01-common-layer/utilities/SPEC.md`

4 Python utility scripts that support development, validation, and cost estimation for the entire library:
- Token calculator
- Skill validator
- AGENTS.md compressor
- Cost estimator

## Key Design Constraints (from Research)

### Token Budget Management
- **Passive context (AGENTS.md)**: ~8KB compressed for full framework docs
- **Skill metadata**: 50-100 tokens per skill
- **Skill body**: <5000 tokens when activated
- **Resources**: On-demand loading only

### Reliability Requirements
- Skills have 56% non-trigger rate without explicit instructions (Vercel eval study)
- Instruction wording is fragile (small changes = big behavioral shifts)
- Passive context (AGENTS.md) provides 100% availability
- All skills must address trigger reliability with multiple trigger patterns, explicit boundaries, and examples of when to use AND when NOT to use

### Architecture Patterns
1. **Horizontal knowledge** (framework APIs, broad docs) -> AGENTS.md
2. **Vertical workflows** (specific tasks, triggered actions) -> Skills
3. **Persistent tools/APIs** -> MCP servers
4. **Hybrid is optimal** for complex systems

## Success Criteria

The Common Layer is successful when:
- [ ] Any AGENTS.md template can be copied and adapted to a specific framework in <15 minutes
- [ ] Universal skills work across any agent without modification
- [ ] Token budgets can be calculated accurately before deployment
- [ ] Skills pass agentskills.io spec validation
- [ ] Documentation indices achieve 80%+ compression (Vercel benchmark)
- [ ] Skill trigger reliability exceeds 90% in team workflows

## Cross-References

- **Master Prompt**: `specs/MASTER_PROMPT.md`
- **Teams Layer**: `specs/02-teams-layer/SPEC.md` (consumers of common layer)
- **Strategies Layer**: `specs/03-strategies-layer/SPEC.md` (guides for using common layer)
- **Research Foundation**:
  - Vercel AGENTS.md eval study: https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals
  - Agent Skills Specification: https://agentskills.io/specification
  - Microsoft Playwright CLI + Skills: https://github.com/microsoft/playwright-cli/blob/main/skills/playwright-cli/SKILL.md
  - Claude Code Agent Teams: https://code.claude.com/docs/en/agent-teams

## Technical Questions to Address

These questions from the master prompt must be answered by implementations in this layer:

1. **AGENTS.md compression**: What is the optimal pipe-delimited format for different types of documentation (API references vs prose guides vs code examples)?
2. **Skill trigger reliability**: Given the 56% non-trigger rate, what are the top 5 description patterns that maximize trigger reliability?
3. **Universal vs specialized skills**: When should a skill be in `common/skills/` vs team-specific? What is the decision criteria?
4. **Token measurement**: How to accurately measure token usage for an AGENTS.md file before deploying?
