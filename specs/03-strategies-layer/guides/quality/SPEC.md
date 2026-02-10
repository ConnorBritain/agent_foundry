# Quality and Reliability Specification

> **STATUS**: STATIC REFERENCE -- Extracted from master prompt. Never modified, only consulted.

## Purpose

Provide comprehensive guidance for testing, validating, and measuring quality in agent workflows. Address the critical skill trigger reliability problem (56% non-trigger rate), establish quality metrics and KPIs, and provide debugging strategies for agent systems.

## Output File

`strategies/quality.md`

## Content Structure

### 1. Testing Agent Workflows

#### Unit Testing

**What to Unit Test**:
- Individual skill trigger patterns (does the skill activate for expected inputs?)
- AGENTS.md token budget compliance (does it stay within limits?)
- Skill output format validation (does output match expected schema?)
- Configuration validation (are all required fields present?)
- Utility script correctness (token calculator, cost estimator accuracy)

**Unit Test Patterns**:

```python
# Example: Skill trigger test
def test_skill_triggers():
    """Test that skill triggers for expected input patterns."""
    trigger_inputs = [
        "find files matching *.py",
        "search codebase for authentication",
        "locate implementation of UserService",
    ]
    non_trigger_inputs = [
        "explain what this code does",
        "write a function to sort a list",
        "what is the weather today",
    ]
    for input in trigger_inputs:
        assert skill_should_trigger(input), f"Should trigger for: {input}"
    for input in non_trigger_inputs:
        assert not skill_should_trigger(input), f"Should NOT trigger for: {input}"
```

**Unit Test Coverage Targets**:
- Skill trigger patterns: 100% of documented patterns tested
- AGENTS.md validation: All token budget constraints
- Configuration schemas: All required fields
- Utility functions: >80% line coverage

#### Integration Testing

**What to Integration Test**:
- Skill execution end-to-end (trigger -> execution -> output)
- Multi-agent handoff (Agent A output becomes Agent B input)
- MCP server connectivity and data flow
- File lock manager coordination
- Checkpoint save/load/resume cycle

**Integration Test Patterns**:
- **Handoff tests**: Verify structured output from Agent A parses correctly as input for Agent B
- **Coordination tests**: Verify file locks prevent write conflicts
- **State tests**: Verify checkpoint resume produces identical behavior to continuous run
- **MCP tests**: Verify tool calls return expected data formats

**Integration Test Infrastructure**:
- Test fixtures with representative data
- Mock MCP servers for isolated testing
- Recorded model responses for deterministic tests
- Test token budgets (limited, to catch budget overruns early)

#### End-to-End Testing

**What to E2E Test**:
- Complete team workflows from input to deliverables
- Multi-phase execution with all coordination
- Error recovery and resumption
- Cost tracking accuracy (estimated vs actual)

**E2E Test Approach**:
1. Define representative workflow scenarios
2. Create golden reference outputs (human-validated)
3. Run workflow with test inputs
4. Compare outputs to golden references (semantic similarity, not exact match)
5. Validate cost within budget
6. Validate quality metrics meet thresholds

**E2E Test Cadence**:
- Full E2E: Before major configuration changes
- Smoke tests: After any configuration change
- Regression suite: Weekly automated run
- Golden reference refresh: Monthly review

### 2. Validation and Error Handling Patterns

#### Input Validation
- Validate user inputs before starting workflow
- Check for required fields, format compliance, reasonable length
- Provide clear error messages for invalid inputs
- Validate against configuration schema

#### Output Validation
- Check output format matches expected schema
- Validate output completeness (all required sections present)
- Check output quality metrics (if automated measurement possible)
- Flag outputs below quality threshold for human review

#### Error Categories and Handling

| Error Category | Examples | Handling Pattern |
|---------------|----------|-----------------|
| Transient | API timeout, rate limit, network error | Retry with exponential backoff (max 3) |
| Input | Invalid format, missing data, out of scope | Validate early, clear error message, request correction |
| Quality | Output below threshold, incomplete output | Retry with stronger model or adjusted prompt |
| Resource | Token budget exceeded, disk full | Checkpoint, notify user, request decision |
| Configuration | Missing skill, invalid AGENTS.md, broken MCP | Fail fast, clear diagnostic message |
| Coordination | Lock conflict, agent failure, stale state | Coordinator-level recovery protocol |

#### Error Handling Best Practices
- Fail fast for configuration errors (don't waste tokens)
- Retry transparently for transient errors (user doesn't need to know)
- Escalate quality errors (let user decide: accept, retry, or abort)
- Always checkpoint before risky operations
- Log all errors with full context for debugging
- Include recovery instructions in error messages

### 3. Improving Skill Trigger Reliability (Addressing the 56% Problem)

#### The Problem

Vercel eval study findings:
- Skills failed to trigger in 56% of cases without explicit instructions
- Even with explicit instructions, trigger rate was only 79% (vs 100% for AGENTS.md)
- Instruction wording is fragile (small changes cause big behavioral shifts)

#### Root Causes
1. **Vague trigger descriptions**: "Helps with code" doesn't distinguish from general coding ability
2. **Single trigger pattern**: Only one way to invoke the skill
3. **Missing boundaries**: Skill description doesn't say when NOT to use it
4. **No examples**: Agent doesn't see concrete examples of trigger scenarios
5. **Competing skills**: Multiple skills with overlapping descriptions

#### Solution: Multi-Pattern Trigger Design

**Template for High-Reliability Skill Triggers**:

```yaml
---
name: code-review
description: >
  Review code changes for quality, security, and style adherence.
  USE THIS SKILL when the user asks to review code, check for issues,
  audit code quality, or validate changes against team standards.
  DO NOT USE for writing new code, explaining code, or refactoring.

# Trigger patterns (test each individually)
trigger_patterns:
  - "review this code"
  - "check for issues in"
  - "audit code quality"
  - "validate changes against"
  - "find bugs in this"

# Anti-patterns (should NOT trigger)
anti_patterns:
  - "write a function"
  - "explain this code"
  - "refactor this"
  - "optimize performance"
---
```

#### The 5-Pattern Trigger Reliability Framework

1. **Action verb trigger**: "Review this code for issues"
2. **Question trigger**: "Are there any problems with this code?"
3. **Imperative trigger**: "Check the code quality of this PR"
4. **Contextual trigger**: "I just committed changes and need a quality check"
5. **Negative trigger**: "Make sure this code doesn't have security vulnerabilities"

#### Trigger Testing Protocol

For each skill:
1. Write 10 positive trigger inputs (should activate)
2. Write 10 negative trigger inputs (should NOT activate)
3. Write 5 edge case inputs (ambiguous, could go either way)
4. Test all 25 inputs against the skill description
5. Calculate trigger accuracy: (correct_triggers + correct_non_triggers) / total
6. Target: >90% accuracy
7. If below target: revise description, add patterns, clarify boundaries

#### Explicit Instruction Pattern

When skills must be highly reliable, embed explicit instructions in AGENTS.md:

```markdown
## Available Skills

When the user asks you to review code, ALWAYS use the `code-review` skill.
When the user asks you to generate tests, ALWAYS use the `test-generator` skill.
When the user asks you to search files, ALWAYS use the `file-search` skill.

Do NOT use skills for general conversation or tasks not matching the above patterns.
```

This pattern increases trigger reliability from 44% to 79% (Vercel eval data).

### 4. Output Quality Measurement and Validation

#### Quality Dimensions

| Dimension | Measurement | Automated? | Target |
|-----------|-------------|-----------|--------|
| Correctness | Factual accuracy, code compiles, tests pass | Partially | >95% |
| Completeness | All required sections/features present | Yes | 100% |
| Consistency | Follows style guide, consistent terminology | Yes | >90% |
| Clarity | Readability score, structure quality | Partially | Score >7/10 |
| Relevance | Addresses the actual task, not tangential | No | >90% |
| Efficiency | Token usage vs output value | Yes | Within budget |

#### Automated Quality Checks

**Code Output Quality**:
- Syntax validation (does it parse?)
- Linting (does it follow style rules?)
- Type checking (for typed languages)
- Test execution (do generated tests pass?)
- Security scanning (no obvious vulnerabilities?)

**Documentation Output Quality**:
- Structure validation (required sections present)
- Link checking (no broken links)
- Spell checking
- Readability score (Flesch-Kincaid or similar)
- Token count (within budget)

**Research Output Quality**:
- Citation validation (do cited sources exist?)
- Claim verification (can claims be traced to sources?)
- Methodology adherence (follows stated research design)
- Completeness check (all research questions addressed)

#### Human Quality Review

When automated checks pass, sample for human review:
- Review rate: 10-20% of outputs
- Focus on: nuanced quality (creativity, insight, practical value)
- Use rubric with consistent scoring criteria
- Track inter-rater reliability
- Calibrate rubric quarterly

### 5. Regression Testing for Agent Changes

#### What Triggers Regression Testing
- AGENTS.md content changes
- Skill description or instruction changes
- Model version updates
- Prompt template changes
- MCP server configuration changes
- Utility script changes

#### Regression Test Suite

**Golden Test Set**:
- 20-50 representative inputs per team template
- Expected outputs (human-validated)
- Quality metric baselines for each input
- Categorized by difficulty (easy, medium, hard)

**Regression Test Process**:
1. Run golden test set with modified configuration
2. Compare outputs to baseline (semantic similarity threshold: >0.85)
3. Calculate quality metrics and compare to baseline
4. Flag regressions (quality drop >5% on any dimension)
5. Investigate flagged regressions
6. Accept (if intentional/acceptable) or fix (if unintentional)

**Regression Prevention**:
- PR checks include regression test run
- Quality metric tracking over time (trend analysis)
- Alert on sustained quality decline (3+ consecutive drops)
- Rollback capability for configuration changes

### 6. Quality Metrics and KPIs

#### Primary KPIs

| KPI | Definition | Target | Measurement |
|-----|-----------|--------|-------------|
| Task Completion Rate | % of tasks completed without human intervention | >85% | Automated tracking |
| Output Quality Score | Average quality score across dimensions | >8/10 | Automated + human |
| Skill Trigger Accuracy | % of correct trigger/non-trigger decisions | >90% | Trigger test suite |
| Cost Efficiency | Deliverable value / token cost | Improving trend | Monthly calculation |
| Error Recovery Rate | % of errors recovered without user intervention | >70% | Error log analysis |
| Regression Rate | % of changes causing quality regression | <10% | Regression test suite |

#### Secondary Metrics

| Metric | Purpose | Frequency |
|--------|---------|-----------|
| Token usage per task | Efficiency tracking | Per task |
| Retry rate | Error frequency | Per session |
| Context window utilization | Capacity planning | Per session |
| Checkpoint frequency | Stability indicator | Per session |
| User intervention rate | Autonomy measurement | Per workflow |
| Time to completion | Performance tracking | Per workflow |

#### Quality Dashboard Template

```markdown
## Quality Report: [Team/Workflow Name]
Period: [date range]

### Primary KPIs
| KPI | Current | Target | Trend |
|-----|---------|--------|-------|
| Task Completion Rate | X% | 85% | [up/down/stable] |
| Output Quality Score | X/10 | 8/10 | [up/down/stable] |
| Skill Trigger Accuracy | X% | 90% | [up/down/stable] |
| Cost Efficiency | $X/deliverable | Improving | [up/down/stable] |
| Error Recovery Rate | X% | 70% | [up/down/stable] |

### Issues This Period
- [Issue 1]: [Impact] [Resolution]
- [Issue 2]: [Impact] [Resolution]

### Optimization Actions Taken
- [Action 1]: [Result]

### Recommendations
- [Recommendation 1]
```

### 7. Debugging Strategies

#### Common Failure Modes

| Failure Mode | Symptoms | Root Cause | Fix |
|-------------|----------|------------|-----|
| Skill not triggering | Task completed without skill, lower quality output | Vague trigger description | Apply 5-pattern framework |
| Wrong skill triggered | Incorrect workflow applied, unexpected output | Overlapping skill descriptions | Add explicit boundaries, anti-patterns |
| Context overflow | Truncated output, missing information, errors | AGENTS.md + skills exceed window | Compress AGENTS.md, reduce skill count |
| Quality degradation | Declining output quality over long sessions | Context pollution, token exhaustion | Checkpoint and restart, summarize context |
| Coordination failure | Agents producing conflicting output | Missing coordination protocol | Add file locks, structured handoffs |
| Cost overrun | Budget exceeded before completion | Under-estimated complexity | Add cost checkpoints, use cost-estimator.py |

#### Debugging Workflow

1. **Identify**: What specific behavior is wrong?
2. **Isolate**: Is the problem in one agent, one skill, or coordination?
3. **Reproduce**: Can the problem be reproduced with same inputs?
4. **Diagnose**: Check logs for error messages, token usage, model responses
5. **Hypothesize**: What is the most likely root cause?
6. **Test**: Apply fix to isolated test case
7. **Validate**: Run regression tests to confirm fix doesn't break other things
8. **Deploy**: Roll out fix with monitoring

#### Debug Logging

Enable verbose logging for debugging:

```python
# Debug log structure
{
    "timestamp": "ISO8601",
    "agent": "agent_name",
    "operation": "skill_trigger|model_call|file_write|coordination",
    "input_tokens": 0,
    "output_tokens": 0,
    "model": "opus|sonnet|haiku",
    "skill_triggered": "skill_name or null",
    "success": true,
    "error": "null or error message",
    "duration_ms": 0,
    "context_window_usage": 0.0,
    "notes": "any relevant context"
}
```

#### Debugging Checklist

```markdown
## Agent Debugging Checklist

### Configuration
- [ ] AGENTS.md within token budget? (run token-calculator.py)
- [ ] Skills pass validation? (run skill-validator.py)
- [ ] MCP servers connected and responding?
- [ ] Model configured correctly for role?
- [ ] Environment variables set?

### Skill Triggers
- [ ] Skill trigger description clear and specific?
- [ ] Multiple trigger patterns defined?
- [ ] Anti-patterns defined (when NOT to trigger)?
- [ ] Explicit skill instructions in AGENTS.md?
- [ ] No overlapping skills with ambiguous boundaries?

### Context
- [ ] Context window not overflowing?
- [ ] AGENTS.md compression ratio adequate?
- [ ] Reference files accessible?
- [ ] No stale cached context?

### Coordination (multi-agent)
- [ ] File locks working correctly?
- [ ] Communication protocol followed?
- [ ] Handoff documents structured correctly?
- [ ] No circular dependencies between agents?

### Quality
- [ ] Output format matches expected schema?
- [ ] Quality metrics above threshold?
- [ ] No regression from recent changes?
- [ ] Human review sample satisfactory?
```

## Writing Guidelines

- Include working test code examples that can be adapted
- Provide concrete thresholds and targets (not vague "improve quality")
- Address the 56% trigger problem as a first-class concern
- Include both automated and human quality measurement
- Provide templates for quality reports and debugging checklists
- Reference Vercel eval data as the empirical foundation

## Dependencies

- Vercel eval study data (trigger reliability numbers)
- Agent Skills Specification (validation rules)
- Common utility scripts (validators, calculators)
- Team template specifications (for team-specific quality criteria)

## Cross-References

- **Strategies Layer**: `specs/03-strategies-layer/SPEC.md`
- **Decision Framework**: `specs/03-strategies-layer/guides/decision-framework/SPEC.md` (AGENTS.md vs Skills reliability)
- **Optimization Guide**: `specs/03-strategies-layer/guides/optimization/SPEC.md` (efficiency metrics)
- **Deployment Guide**: `specs/03-strategies-layer/guides/deployment/SPEC.md` (CI/CD quality gates)
- **Common Skills**: `specs/01-common-layer/skills/SPEC.md` (skill design patterns)
- **Research Foundation**:
  - Vercel AGENTS.md eval study: https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals
  - Agent Skills Specification: https://agentskills.io/specification
