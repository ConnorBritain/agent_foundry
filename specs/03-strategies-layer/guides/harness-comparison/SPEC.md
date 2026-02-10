# Harness Comparison Guide Specification

> **STATUS**: STATIC REFERENCE -- Extracted from master prompt. Never modified, only consulted.

## Purpose

Provide a complete comparison of major agent harness platforms to help users select the right tool for their use case, understand migration paths between harnesses, and build portable agent configurations.

## Output File

`strategies/harness-comparison.md`

## Content Structure

### 1. Executive Summary with Quick Decision Matrix

A quick-reference table mapping use cases to recommended harnesses:

| Use Case | Recommended Harness | Runner-Up |
|----------|-------------------|-----------|
| Production team workflows | Claude Code | - |
| Individual developer, IDE-native | Cursor | Windsurf |
| Open-source, custom models | OpenClaw | - |
| Enterprise compliance | Claude Code | - |
| Budget-constrained | OpenClaw | Cursor |
| Chinese language workflows | OpenClaw | - |
| Rapid prototyping | Cursor | Claude Code |

### 2. Detailed Feature Comparison Table

Complete matrix comparing all harnesses across these dimensions:

- **Skills support**: Native SKILL.md loading, trigger reliability, progressive disclosure
- **MCP support**: Server configuration, tool availability, custom servers
- **AGENTS.md support**: Passive context loading, compression format support
- **Multi-agent coordination**: Parallel execution, inter-agent communication, orchestration
- **Cost models**: Per-token pricing, subscription tiers, free tier limits
- **Offline mode**: Local model support, air-gapped operation
- **IDE integration**: VS Code, JetBrains, standalone CLI, web interface
- **Language support**: Programming language coverage, natural language support
- **Context windows**: Maximum context size, effective context utilization
- **Parallel execution**: Multiple agent instances, concurrent operations
- **State persistence**: Session checkpointing, cross-session state
- **Custom models**: Bring-your-own-model, fine-tuned model support
- **Browser automation**: Web interaction capabilities, Playwright/Puppeteer integration
- **Pricing**: Monthly costs for typical usage patterns (light/medium/heavy)

### 3. Individual Harness Deep-Dives

#### Claude Code
- **Strengths**: Production workflows, team collaboration, enterprise compliance
- **Best for**: Teams building production agent systems, enterprise environments
- **Key features**: Native Skills and AGENTS.md support, multi-agent teams, MCP ecosystem
- **Limitations**: Anthropic models only, requires API access
- **Cost profile**: Token-based pricing with Max subscription option
- **Integration**: VS Code extension, CLI, web interface

#### Kilo Code
- **Strengths**: Research needed -- limited public information available
- **Best for**: To be determined based on research
- **Key features**: To be documented
- **Limitations**: To be documented
- **Cost profile**: To be documented
- **Note**: Mark sections requiring additional research with `[RESEARCH NEEDED]` tags

#### OpenClaw
- **Strengths**: Open-source experimentation, custom model integration, Chinese language workflows
- **Best for**: Teams needing custom model support, open-source advocates, Chinese language projects
- **Key features**: Multi-model support, open-source, extensible architecture
- **Limitations**: Smaller ecosystem, less enterprise support
- **Cost profile**: Self-hosted (infrastructure costs only) or hosted options
- **Integration**: CLI-based, extensible

#### Cursor
- **Strengths**: Individual developers, IDE-native workflows, rapid prototyping
- **Best for**: Solo developers, quick iteration, code-focused workflows
- **Key features**: Deep IDE integration, fast completions, multi-model support
- **Limitations**: Less suited for multi-agent orchestration, IDE-dependent
- **Cost profile**: Subscription-based with usage limits
- **Integration**: Custom IDE (VS Code fork)

#### Windsurf
- **Strengths**: Research needed -- emerging platform
- **Best for**: To be determined based on research
- **Key features**: To be documented
- **Limitations**: To be documented
- **Cost profile**: To be documented
- **Note**: Mark sections requiring additional research with `[RESEARCH NEEDED]` tags

### 4. Cost Model Comparisons

Typical usage pattern cost projections:

| Usage Pattern | Claude Code | Cursor | OpenClaw | Notes |
|--------------|-------------|--------|----------|-------|
| Light (1hr/day, single agent) | $X/mo | $X/mo | $X/mo | Individual developer |
| Medium (4hr/day, 2-3 agents) | $X/mo | $X/mo | $X/mo | Small team |
| Heavy (8hr/day, 5+ agents) | $X/mo | $X/mo | $X/mo | Production workflow |
| Software Factory (24/7 swarm) | $X/mo | N/A | $X/mo | StrongDM-style |

Include calculation methodology showing:
- Tokens per hour by task type
- Model cost per million tokens
- Overhead factors (retries, context loading, coordination)

### 5. Migration Strategies Between Harnesses

Step-by-step migration guides for common paths:

#### Claude Code to Cursor
- What transfers directly (AGENTS.md files, skill concepts)
- What needs adaptation (orchestration patterns, MCP configs)
- What is lost (multi-agent coordination, some MCP servers)
- Migration checklist with estimated effort

#### Claude Code to OpenClaw
- Model compatibility considerations
- Configuration format differences
- Custom model integration steps
- Migration checklist with estimated effort

#### Cursor to Claude Code
- Upgrading from single-agent to multi-agent
- Importing existing configurations
- Leveraging new capabilities (Skills, MCP)
- Migration checklist with estimated effort

#### General Migration Framework
- Inventory current configurations
- Identify harness-specific vs portable components
- Create abstraction layer for portable configs
- Test and validate in target harness

### 6. Harness-Agnostic Patterns for Portability

Design patterns that work across harnesses:
- **Portable AGENTS.md format**: Subset of features supported everywhere
- **Skill abstraction**: Writing skills that can be adapted to any harness
- **Configuration layering**: Base config (portable) + harness overlay (specific)
- **File-based coordination**: Patterns that don't depend on harness-specific APIs
- **Testing portability**: Validating templates work across harnesses

### 7. Selection Decision Tree

Flowchart-style decision tree:

```
START: What is your primary use case?
├── Multi-agent team workflows?
│   ├── Enterprise compliance needed? → Claude Code
│   └── Open-source/custom models? → OpenClaw
├── Individual developer productivity?
│   ├── IDE-native experience? → Cursor
│   └── CLI/terminal workflow? → Claude Code
├── Research/experimentation?
│   ├── Custom models required? → OpenClaw
│   └── Standard models sufficient? → Claude Code or Cursor
└── Budget is primary constraint?
    ├── Self-hosting possible? → OpenClaw
    └── Managed service preferred? → Cursor (subscription) or Claude Code (pay-per-use)
```

### 8. Benchmark Performance Data

Where available, include:
- Task completion rates by harness
- Token efficiency comparisons
- Latency measurements
- Skill trigger reliability by harness
- Multi-agent coordination performance

**Note**: Mark benchmarks as `[SELF-MEASURED]`, `[VENDOR-REPORTED]`, or `[COMMUNITY-REPORTED]` for transparency.

## Writing Guidelines

- Be objective and fair in comparisons; acknowledge uncertainty with `[RESEARCH NEEDED]` tags
- Include dates for all pricing and feature data (these change rapidly)
- Provide concrete migration checklists, not vague guidance
- Use actual dollar amounts where possible, ranges where not
- Reference official documentation for each harness
- Update cadence recommendation: quarterly review of all data

## Dependencies

- Research into Kilo Code and Windsurf capabilities (mark as `[RESEARCH NEEDED]` until complete)
- Current pricing data for all harnesses (include retrieval date)
- Benchmark data collection (mark source and methodology)

## Cross-References

- **Strategies Layer**: `specs/03-strategies-layer/SPEC.md`
- **Decision Framework**: `specs/03-strategies-layer/guides/decision-framework/SPEC.md` (complementary guide)
- **Model Selection**: `specs/03-strategies-layer/guides/model-selection/SPEC.md` (model choices within harnesses)
- **Deployment Guide**: `specs/03-strategies-layer/guides/deployment/SPEC.md` (deploying in chosen harness)
