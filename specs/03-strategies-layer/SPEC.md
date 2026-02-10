# Strategies Layer Specification

> **STATUS**: STATIC REFERENCE -- Extracted from master prompt. Never modified, only consulted.

## Purpose

The Strategies Layer provides 7 comprehensive markdown guides covering all strategic aspects of agent development. These are conceptual guides and best practices documents that help users make informed decisions about agent architecture, harness selection, model choice, deployment, optimization, and quality assurance.

Unlike the Common and Teams layers which provide executable templates, the Strategies Layer provides the knowledge framework for using those templates effectively. These guides are the "why" and "when" to complement the "what" and "how" of the template layers.

## Architecture Overview

```
strategies/
├── README.md
├── harness-comparison.md             # Full feature matrix, migration guides
├── model-selection.md                # Language/framework model recommendations
├── long-running-agents.md            # Checkpointing, context management, cost
├── decision-framework.md             # AGENTS.md vs Skills vs MCP decision tree
├── deployment.md                     # CI/CD, monitoring, operations
├── optimization.md                   # Token/cost optimization techniques
└── quality.md                        # Testing, validation, reliability
```

## Guide Specifications

Each guide has its own detailed SPEC.md in `specs/03-strategies-layer/guides/`.

### 1. Agent Harness Comparison (`harness-comparison.md`)

**Spec**: `specs/03-strategies-layer/guides/harness-comparison/SPEC.md`

Complete comparison of major agent harness platforms including Claude Code, Kilo Code, OpenClaw, Cursor, and Windsurf. Covers feature matrices, cost models, migration strategies, and a selection decision tree. Includes deep-dives for each harness with use-case-specific recommendations and benchmark performance data where available.

### 2. Model Selection Strategy (`model-selection.md`)

**Spec**: `specs/03-strategies-layer/guides/model-selection/SPEC.md`

Universal guide for choosing models across all team templates. Covers task-to-model mapping, language-specific recommendations (Swift, Kotlin, Python, JS/TS, Rust, Go), framework-specific guidance (Next.js, FastAPI), upgrade triggers and ROI thresholds, and A/B testing processes for model choices.

### 3. Long-Running Agent Strategies (`long-running-agents.md`)

**Spec**: `specs/03-strategies-layer/guides/long-running-agents/SPEC.md`

Comprehensive guide for extended agent sessions covering session management, context window management, cost optimization for long workflows, error recovery patterns, and real-time monitoring with alert thresholds.

### 4. Architecture Decision Framework (`decision-framework.md`)

**Spec**: `specs/03-strategies-layer/guides/decision-framework/SPEC.md`

Complete decision framework for all architectural choices. Covers AGENTS.md vs Skills vs MCP decision trees, single agent vs team criteria, sync vs async coordination patterns, token budget allocation formulas, trade-off matrices, and real-world decision examples.

### 5. Deployment and Operations (`deployment.md`)

**Spec**: `specs/03-strategies-layer/guides/deployment/SPEC.md`

Practical guide for deploying agent systems covering local development workflows, CI/CD integration, monitoring and cost tracking, version control for agent configs, team collaboration best practices, environment management, secrets handling, and production readiness checklists.

### 6. Optimization Playbook (`optimization.md`)

**Spec**: `specs/03-strategies-layer/guides/optimization/SPEC.md`

Concrete techniques for token and cost optimization including context compression, lazy loading patterns, caching strategies, batching and parallelization, measuring token efficiency, before/after case studies, and tooling for measuring improvements.

### 7. Quality and Reliability (`quality.md`)

**Spec**: `specs/03-strategies-layer/guides/quality/SPEC.md`

Testing, validation, and quality measurement for agent workflows covering unit/integration/end-to-end testing, validation and error handling patterns, skill trigger reliability improvements (addressing the 56% problem), output quality measurement, regression testing, quality metrics/KPIs, and debugging strategies.

## Key Design Constraints (from Research)

### Writing Standards
- All guides must reference research findings, not just opinions
- Include concrete examples and code snippets where applicable
- Provide actionable checklists and decision trees
- Use tables and matrices for comparison data
- Include cost estimates with calculation methodology

### Research Foundation
- Vercel AGENTS.md eval study findings (100% vs 79% pass rates, 56% non-trigger rate)
- Agent Skills Specification from agentskills.io
- StrongDM Software Factory patterns ($1,000/day token spend reference)
- Microsoft Playwright CLI + Skills approach (token efficiency)
- Claude Code Agent Teams documentation

### Audience
- Software engineers building agent workflows
- Engineering managers coordinating multi-agent systems
- Product teams integrating AI agents into products
- Researchers automating literature review and analysis
- Data teams building intelligent pipelines

### Quality Standards
- Documentation must be clear enough for junior developers
- Strategies must reference research (not just opinions)
- Cost projections must include calculation methodology
- Include "when NOT to use" guidance, not just "when to use"

## Success Criteria

The Strategies Layer is successful when:

- [ ] Users can make confident harness selection decisions using the comparison guide
- [ ] Long-running agent costs are optimized by 40%+ using the optimization guide
- [ ] Users choose AGENTS.md vs Skills vs MCP correctly 95%+ of the time using the decision framework
- [ ] Agents can be deployed in CI/CD with confidence using the deployment guide
- [ ] Quality improves through systematic testing using the quality guide
- [ ] Model selection is data-driven using the model selection guide
- [ ] Guides are referenced by team templates for role-specific recommendations

## Cross-References

- **Master Prompt**: `specs/MASTER_PROMPT.md`
- **Common Layer**: `specs/01-common-layer/SPEC.md` (building blocks these guides help use)
- **Teams Layer**: `specs/02-teams-layer/SPEC.md` (consumers of strategy guidance)
- **Examples**: `specs/04-examples/SPEC.md` (practical demonstrations of strategies)
- **Research Foundation**:
  - Vercel AGENTS.md eval study: https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals
  - Agent Skills Specification: https://agentskills.io/specification
  - Microsoft Playwright CLI + Skills: https://github.com/microsoft/playwright-cli/blob/main/skills/playwright-cli/SKILL.md
  - Claude Code Agent Teams: https://code.claude.com/docs/en/agent-teams
  - StrongDM Software Factory: https://simonwillison.net/2026/Feb/7/software-factory/

## Technical Questions to Address

These questions from the master prompt must be answered by guides in this layer:

1. **Harness migration**: If I build templates for Claude Code, what's required to migrate to OpenClaw or Cursor? Can I maintain harness-agnostic templates?
2. **Long-running sessions**: For agents running >1 hour, when should I checkpoint state vs continuous operation? What's the token budget crossover point?
3. **Quality metrics**: How do I measure if a team template is working well? What metrics beyond cost should I track?
4. **Skill vs MCP tradeoff**: For the same capability (e.g., Jira integration), when should it be a skill vs MCP server? What's the decision framework?
5. **Model selection**: When do language-specific benchmark leaders (minimax2.5 for Swift/Kotlin) outweigh the general-purpose leader (Opus 4.6)?
6. **Cost estimation accuracy**: What factors affect actual vs estimated token usage? How do I build cost projections within 20% of actuals?
7. **Deployment patterns**: How do agent configurations integrate with existing CI/CD pipelines and version control workflows?
