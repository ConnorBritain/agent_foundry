---
skill_name: "quality-check"
version: "1.0.0"
description: "Validate output quality against acceptance criteria before publishing"
author: "Sforza"
triggers:
  - "before publishing any artifact"
  - "at phase completion"
  - "when user requests quality review"
---

# Quality Check Skill

## Purpose

Ensure all agent outputs meet quality standards before being published to the shared workspace or delivered to the user.

## Quality Dimensions

### 1. Completeness
- Does the output address all requirements from the project charter?
- Are there gaps or placeholder content that needs filling?
- Are all sections present as specified?

### 2. Accuracy
- Are facts verifiable and correctly sourced?
- Are financial calculations correct (spot-check formulas)?
- Are technical claims accurate (API endpoints exist, libraries are current)?

### 3. Consistency
- Does terminology match across all team deliverables?
- Are brand voice and tone consistent?
- Do numbers agree between related documents (e.g., financial model and business plan)?

### 4. Actionability
- Can the user act on this output immediately?
- Are next steps clearly defined?
- Are dependencies on other deliverables identified?

### 5. Professional Quality
- Is the writing clear and free of errors?
- Is formatting consistent (headings, lists, tables)?
- Would this be presentable to investors, clients, or stakeholders?

## Pre-Publish Checklist

Before moving any artifact to `shared-workspace/artifacts/`:

```
[ ] Content is complete — no TODOs, placeholders, or [FILL IN] markers
[ ] Facts are verified — claims are sourced or clearly marked as estimates
[ ] Numbers check out — calculations spot-checked, totals agree
[ ] Formatting is clean — consistent headings, proper markdown
[ ] No AI artifacts — removed "As an AI...", "I'd be happy to...", etc.
[ ] Brand voice matches — consistent with charter and positioning
[ ] Dependencies noted — references to other team outputs are accurate
[ ] Version labeled — file uses proper version suffix
```

## Scenario-Based Validation (StrongDM Pattern)

For critical deliverables, validate against scenarios:

1. **Define test scenarios** specific to the deliverable type
2. **Run the deliverable through each scenario** to check if it handles the case
3. **Score pass/fail** per scenario
4. **Iterate** on any failures before publishing

### Example: Business Plan Validation

| Scenario | Check | Pass? |
|----------|-------|-------|
| Investor reads exec summary | Clear value prop in first paragraph? | |
| CFO reviews financials | Revenue model internally consistent? | |
| Competitor finds the plan | No confidential data exposed? | |
| User pivots market segment | Plan sections are modular enough to update? | |

## Quality Scoring

Rate each deliverable on a 1-5 scale:

| Score | Meaning | Action |
|-------|---------|--------|
| 5 | Exceptional — exceeds requirements | Publish immediately |
| 4 | Strong — meets all requirements | Publish |
| 3 | Adequate — meets most requirements | Minor revisions, then publish |
| 2 | Below standard — significant gaps | Major revision needed |
| 1 | Unacceptable — does not meet requirements | Redo from scratch |

**Minimum publish threshold**: 3 (adequate)
**Target**: 4 (strong)

## Reporting Quality Issues

If a deliverable scores below 3:

1. Document specific issues found
2. Estimate effort to fix (minor revision vs major redo)
3. Report to coordinator with recommendation
4. Do NOT publish substandard work — iterate first
