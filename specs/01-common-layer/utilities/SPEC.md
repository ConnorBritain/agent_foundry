# Common Utilities Specification

> **STATUS**: STATIC REFERENCE -- Extracted from master prompt. Never modified, only consulted.

## Purpose

Provide 4 practical Python utility scripts that support development, validation, cost estimation, and compression for the entire Agent Foundry. These utilities are used both by template developers (building the library) and template consumers (deploying agent teams).

## Location

```
common/utilities/
├── token-calculator.py
├── skill-validator.py
├── agents-md-compressor.py
└── cost-estimator.py
```

## Shared Requirements

All 4 utilities MUST include:

### 1. CLI Interface
- Use `argparse` for command-line argument parsing
- Provide `--help` with clear descriptions and examples
- Support both positional arguments and named flags
- Return meaningful exit codes (0=success, 1=error, 2=warning)

### 2. Example Usage
- Include a `## Usage` section in docstring or companion README
- Show at least 3 example invocations covering common use cases
- Include expected output format

### 3. Integration Notes
- Document how team templates use this utility
- Describe integration points with other utilities
- List any external dependencies

### 4. Tests
- Each utility must have a corresponding test file
- Tests cover: normal operation, edge cases, error handling
- Tests can be run with `pytest` from repository root
- Test file naming: `test_[utility-name].py`

### 5. Technical Requirements
- Python 3.9+ compatibility
- Minimal external dependencies (prefer standard library)
- Type hints on all public functions
- Docstrings on all public functions and classes
- No hardcoded paths (use CLI arguments or environment variables)

---

## Utility 1: token-calculator.py

### Purpose
Calculate token usage for AGENTS.md files, skills, and team configurations. Supports multiple tokenizers and provides cost projections.

### Features

1. **Count tokens in a single file**
   ```bash
   python token-calculator.py count path/to/file.md
   # Output: 2,347 tokens (claude-3-tokenizer)
   ```

2. **Count tokens across a team configuration**
   ```bash
   python token-calculator.py team teams/code-implementation/
   # Output:
   # Agent              | AGENTS.md | Skills | Total
   # coordinator        | 1,200     | 800    | 2,000
   # impl-specialist-a  | 3,400     | 1,200  | 4,600
   # ...
   # TEAM TOTAL: 18,500 tokens
   ```

3. **Project costs based on model and token count**
   ```bash
   python token-calculator.py cost path/to/file.md --model opus-4.6
   # Output:
   # Input tokens: 2,347
   # Estimated cost per invocation: $0.035
   # Estimated cost per 100 invocations: $3.50
   ```

4. **Compare compressed vs uncompressed formats**
   ```bash
   python token-calculator.py compare original.md compressed.md
   # Output:
   # Original:   10,234 tokens
   # Compressed:  2,048 tokens
   # Savings:     8,186 tokens (80.0%)
   # Cost savings per 1000 calls: $XX.XX (opus-4.6)
   ```

### CLI Interface

```
usage: token-calculator.py [-h] {count,team,cost,compare} ...

Token calculator for Agent Foundry

positional arguments:
  {count,team,cost,compare}
    count               Count tokens in a file
    team                Count tokens across a team configuration
    cost                Project costs for a file
    compare             Compare token counts between files

optional arguments:
  -h, --help            show this help message and exit
  --tokenizer {claude,gpt,tiktoken}
                        Tokenizer to use (default: claude)
  --output {text,json,csv}
                        Output format (default: text)
```

### Model Pricing Data (to embed or reference)

```python
MODEL_PRICING = {
    "opus-4.6": {"input": 15.00, "output": 75.00},     # per 1M tokens
    "sonnet-4.5": {"input": 3.00, "output": 15.00},
    "haiku-4.5": {"input": 0.25, "output": 1.25},
}
```

Note: Pricing should be in a separate configuration file or data structure that is easy to update as prices change.

### Integration

- Used by `agents-md-compressor.py` to verify compression ratios
- Used by `cost-estimator.py` for accurate token projections
- Referenced by all team templates for budget validation
- Can be run in CI/CD to prevent token budget regressions

### Tests

```
tests/
└── test_token_calculator.py
    ├── test_count_single_file()
    ├── test_count_empty_file()
    ├── test_count_large_file()
    ├── test_team_directory_scan()
    ├── test_cost_projection_accuracy()
    ├── test_compare_formats()
    ├── test_different_tokenizers()
    ├── test_json_output()
    ├── test_csv_output()
    └── test_invalid_file_path()
```

---

## Utility 2: skill-validator.py

### Purpose
Validate SKILL.md files against the agentskills.io specification. Ensures all skills in the library meet the required format and quality standards.

### Validation Rules

1. **YAML frontmatter structure**
   - Frontmatter exists (delimited by `---`)
   - YAML is parseable
   - No syntax errors

2. **Required fields**
   - `name`: present, string
   - `description`: present, string

3. **Name format**
   - Lowercase only
   - Hyphens for word separation
   - Maximum 64 characters
   - No special characters beyond hyphens
   - Pattern: `^[a-z][a-z0-9-]{0,63}$`

4. **Description length**
   - Maximum 1024 characters
   - Minimum 50 characters (to ensure meaningful description)

5. **File references exist**
   - All paths referenced in `references/` section resolve to actual files
   - All paths referenced in `scripts/` section resolve to actual files
   - Relative paths are resolved from the SKILL.md file location

6. **No deeply nested references**
   - References can point to files, but those files cannot reference other files
   - Maximum 1 level of indirection

7. **Token budget accuracy** (optional, requires token-calculator.py)
   - If `token_budget` is specified in metadata, validate it is within 10% of actual measured tokens

### CLI Interface

```
usage: skill-validator.py [-h] [--strict] [--fix] path

Validate SKILL.md files against agentskills.io specification

positional arguments:
  path                  Path to SKILL.md file or directory containing skills

optional arguments:
  -h, --help            show this help message and exit
  --strict              Enable strict mode (warnings become errors)
  --fix                 Attempt to auto-fix minor issues
  --check-tokens        Also validate token budget accuracy (requires token-calculator.py)
  --output {text,json}  Output format (default: text)
```

### Example Usage

```bash
# Validate a single skill
python skill-validator.py common/skills/file-search/SKILL.md
# Output:
# PASS: file-search/SKILL.md
#   - name: valid (file-search)
#   - description: valid (234 chars)
#   - frontmatter: valid YAML
#   - references: 2/2 files found
#   - scripts: 1/1 files found

# Validate all skills in directory
python skill-validator.py common/skills/
# Output:
# Validating 10 skills...
# PASS: file-search (7/7 checks)
# PASS: file-transform (7/7 checks)
# FAIL: web-research (6/7 checks)
#   - ERROR: references/missing-file.md does not exist
# ...
# Results: 9/10 passed, 1/10 failed

# Strict mode (warnings become errors)
python skill-validator.py common/skills/ --strict
```

### Validation Output Format

```json
{
  "skill": "file-search",
  "path": "common/skills/file-search/SKILL.md",
  "status": "PASS",
  "checks": {
    "frontmatter_exists": {"status": "pass"},
    "frontmatter_valid_yaml": {"status": "pass"},
    "name_present": {"status": "pass"},
    "name_format": {"status": "pass", "value": "file-search"},
    "description_present": {"status": "pass"},
    "description_length": {"status": "pass", "value": 234},
    "references_exist": {"status": "pass", "found": 2, "total": 2},
    "scripts_exist": {"status": "pass", "found": 1, "total": 1}
  },
  "warnings": [],
  "errors": []
}
```

### Integration

- Run in CI/CD to prevent invalid skills from being merged
- Referenced by skill authors during development
- Used by `cost-estimator.py` to verify skill metadata
- Can validate team-specific skills as well as common skills

### Tests

```
tests/
└── test_skill_validator.py
    ├── test_valid_skill()
    ├── test_missing_frontmatter()
    ├── test_invalid_yaml()
    ├── test_missing_name()
    ├── test_name_too_long()
    ├── test_name_invalid_chars()
    ├── test_description_too_long()
    ├── test_description_too_short()
    ├── test_missing_file_reference()
    ├── test_nested_references()
    ├── test_directory_scan()
    ├── test_strict_mode()
    ├── test_json_output()
    └── test_fix_mode()
```

---

## Utility 3: agents-md-compressor.py

### Purpose
Compress documentation into pipe-delimited AGENTS.md format. Estimates token savings and validates retrieval paths.

### Features

1. **Scan directory of docs and generate compressed index**
   ```bash
   python agents-md-compressor.py compress ./docs/ --output framework-nextjs.md
   # Output:
   # Scanned: 45 files in ./docs/
   # Generated: framework-nextjs.md
   # Original tokens: 10,234
   # Compressed tokens: 2,048
   # Savings: 80.0%
   ```

2. **Estimate token savings**
   ```bash
   python agents-md-compressor.py estimate ./docs/
   # Output:
   # Current size: 10,234 tokens
   # Estimated compressed: 2,000-2,500 tokens
   # Estimated savings: 75-80%
   ```

3. **Validate retrieval paths in compressed file**
   ```bash
   python agents-md-compressor.py validate framework-nextjs.md --root ./docs/
   # Output:
   # Checking 45 file references...
   # PASS: All references resolve correctly
   ```

4. **Decompress back to full docs (for verification)**
   ```bash
   python agents-md-compressor.py decompress framework-nextjs.md --output ./expanded/
   # Output:
   # Expanded 45 references to ./expanded/
   ```

5. **Support for different doc structures**
   ```bash
   # API reference style
   python agents-md-compressor.py compress ./api-docs/ --style api-reference

   # Prose guide style
   python agents-md-compressor.py compress ./guides/ --style prose

   # Code example style
   python agents-md-compressor.py compress ./examples/ --style code-examples
   ```

### Compression Styles

#### api-reference
```
|GET /api/users(limit:n,offset:n)->User[]
|POST /api/users{name:s,email:s}->User
|GET /api/users/:id->User|404
|PUT /api/users/:id{name?:s,email?:s}->User|404
|DELETE /api/users/:id->204|404
```

#### prose
```
|RULE: Always use server components for data fetching
|RULE: Client components only for interactivity
|PREFER: Static generation over SSR when possible
|AVOID: useEffect for data fetching in client components
|NOTE: Suspense boundaries required for streaming
```

#### code-examples
```
|EXAMPLE: server-action-form -> references/server-action-form.tsx
|EXAMPLE: api-route-handler -> references/api-route-handler.ts
|EXAMPLE: middleware-auth -> references/middleware-auth.ts
|PATTERN: data-fetching -> references/patterns/data-fetching.tsx
```

### CLI Interface

```
usage: agents-md-compressor.py [-h] {compress,estimate,validate,decompress} ...

Compress documentation into AGENTS.md pipe-delimited format

positional arguments:
  {compress,estimate,validate,decompress}
    compress            Compress docs directory into AGENTS.md format
    estimate            Estimate token savings without compressing
    validate            Validate file references in compressed AGENTS.md
    decompress          Expand compressed AGENTS.md back to full docs

optional arguments:
  -h, --help            show this help message and exit
  --style {api-reference,prose,code-examples,auto}
                        Compression style (default: auto)
  --output PATH         Output file or directory
  --root PATH           Root directory for reference resolution
  --include-header      Include template header block
```

### Integration

- Used to create all templates in `common/agents-md/`
- Referenced by `token-calculator.py` for savings verification
- Can be run in CI/CD to regenerate compressed templates when source docs change
- Decompression mode useful for template consumers who want to inspect full docs

### Tests

```
tests/
└── test_agents_md_compressor.py
    ├── test_compress_api_reference()
    ├── test_compress_prose()
    ├── test_compress_code_examples()
    ├── test_auto_style_detection()
    ├── test_estimate_savings()
    ├── test_validate_references_pass()
    ├── test_validate_references_fail()
    ├── test_decompress_roundtrip()
    ├── test_compression_ratio_target()
    ├── test_empty_directory()
    ├── test_nested_directory_structure()
    └── test_output_formats()
```

---

## Utility 4: cost-estimator.py

### Purpose
Estimate costs for agent teams and workflows. Takes team configurations and workflow descriptions as input, produces token projections per phase, total cost, model comparison, and sensitivity analysis.

### Features

1. **Token projections per phase**
   ```bash
   python cost-estimator.py estimate teams/code-implementation/
   # Output:
   # Phase                 | Tokens    | Model       | Cost
   # Planning              | 30,000    | sonnet-4.5  | $0.09
   # Implementation (x2)   | 300,000   | opus-4.6    | $4.50
   # Code Review           | 80,000    | opus-4.6    | $1.20
   # Testing               | 60,000    | sonnet-4.5  | $0.18
   # Documentation         | 20,000    | haiku-4.5   | $0.01
   # -------------------------------------------------
   # TOTAL                 | 490,000   | mixed       | $5.98
   ```

2. **Model comparison**
   ```bash
   python cost-estimator.py compare teams/code-implementation/
   # Output:
   # Configuration          | Total Cost | Quality Est.
   # All Opus 4.6           | $7.35      | Highest
   # Mixed (default)        | $5.98      | High
   # All Sonnet 4.5         | $1.47      | Medium
   # All Haiku 4.5          | $0.12      | Basic
   # Language-optimized     | $5.50      | High
   ```

3. **Sensitivity analysis**
   ```bash
   python cost-estimator.py sensitivity teams/code-implementation/
   # Output:
   # Scenario               | Token Delta | Cost Impact
   # Base case              | 0%          | $5.98
   # +20% tokens            | +98,000     | $7.18
   # +50% tokens            | +245,000    | $8.97
   # -20% tokens            | -98,000     | $4.78
   # Parallel doubled       | +300,000    | $9.48
   # All phases sequential  | +100,000    | $7.48
   ```

4. **Workflow cost estimation**
   ```bash
   python cost-estimator.py workflow --phases "research:40K:sonnet,draft:60K:sonnet,review:50K:opus"
   # Output:
   # Phase   | Tokens  | Model      | Input Cost | Output Est. | Total
   # research| 40,000  | sonnet-4.5 | $0.12      | $0.30       | $0.42
   # draft   | 60,000  | sonnet-4.5 | $0.18      | $0.45       | $0.63
   # review  | 50,000  | opus-4.6   | $0.75      | $1.88       | $2.63
   # --------------------------------------------------------
   # TOTAL   | 150,000 | mixed      | $1.05      | $2.63       | $3.68
   ```

### CLI Interface

```
usage: cost-estimator.py [-h] {estimate,compare,sensitivity,workflow} ...

Cost estimator for agent teams and workflows

positional arguments:
  {estimate,compare,sensitivity,workflow}
    estimate            Estimate costs for a team configuration
    compare             Compare costs across model configurations
    sensitivity         Run sensitivity analysis on cost estimates
    workflow            Estimate costs for custom workflow phases

optional arguments:
  -h, --help            show this help message and exit
  --output {text,json,csv}
                        Output format (default: text)
  --include-output-tokens
                        Include estimated output tokens (default: input only)
  --output-ratio FLOAT  Ratio of output to input tokens (default: 2.5)
```

### Team Configuration Format

The cost estimator reads team configuration from team directories. Expected structure:

```yaml
# In TEAM_SPEC.md or cost-analysis.md, parseable section:
## Token Budget
- Planning phase: ~30K tokens (Coordinator, sonnet-4.5)
- Implementation phase: ~150K tokens per specialist (opus-4.6)
- Review phase: ~80K tokens (Code Reviewer, opus-4.6)
- Testing phase: ~60K tokens (Test Engineer, sonnet-4.5)
- Documentation phase: ~20K tokens (Documentation Writer, haiku-4.5)
```

Alternatively, a structured `cost-config.yaml` in the team directory:

```yaml
phases:
  - name: planning
    tokens: 30000
    model: sonnet-4.5
    agents: [coordinator]
    parallel: false
  - name: implementation
    tokens: 150000
    model: opus-4.6
    agents: [impl-specialist-a, impl-specialist-b]
    parallel: true
  - name: review
    tokens: 80000
    model: opus-4.6
    agents: [code-reviewer]
    parallel: false
  - name: testing
    tokens: 60000
    model: sonnet-4.5
    agents: [test-engineer]
    parallel: true  # parallel with documentation
  - name: documentation
    tokens: 20000
    model: haiku-4.5
    agents: [documentation-writer]
    parallel: true  # parallel with testing
```

### Cost Formula

```
Phase Cost = (input_tokens * model_input_price / 1_000_000) +
             (estimated_output_tokens * model_output_price / 1_000_000)

Total Cost = sum(Phase Costs)

Sensitivity = Total Cost * (1 + sensitivity_factor)
```

**Default output token estimation**: output_tokens = input_tokens * 2.5 (configurable)

### Integration

- References `token-calculator.py` for accurate token counts
- Reads team configurations from `teams/*/TEAM_SPEC.md` or `teams/*/cost-config.yaml`
- Output can be embedded in team `cost-analysis.md` files
- Can be integrated into CI/CD to track cost trends over time

### Tests

```
tests/
└── test_cost_estimator.py
    ├── test_estimate_single_phase()
    ├── test_estimate_full_team()
    ├── test_compare_all_models()
    ├── test_sensitivity_positive()
    ├── test_sensitivity_negative()
    ├── test_custom_workflow()
    ├── test_parallel_phase_costing()
    ├── test_output_token_ratio()
    ├── test_json_output()
    ├── test_csv_output()
    ├── test_missing_team_config()
    └── test_pricing_data_accuracy()
```

---

## Additional Orchestration Utilities

These utilities are referenced in the master prompt for multi-agent coordination. They live in `common/utilities/` alongside the 4 primary utilities but serve a different purpose (runtime coordination vs development tooling).

### file-lock-manager.py (Already specified in master prompt)
- Purpose: Prevent write conflicts during parallel agent workflows
- Functions: `acquire_lock()`, `release_lock()`, `check_lock()`
- Lock file: `shared-state/file-ownership.json`
- Lock duration: 30 minutes (configurable)
- CLI: `python file-lock-manager.py <acquire|release|check> <file_path> [agent_name] [reason]`

### status-updater.py (Already specified in master prompt)
- Purpose: Agents update their status in shared state
- Function: `update_status(agent_name, status, task, progress, blocked_by)`
- Status file: `shared-state/agent-status.json`
- Status values: active, awaiting, offline
- CLI: `python status-updater.py <agent_name> <status> <task> <progress> [blocked_by]`

These two orchestration utilities are fully specified in the master prompt with complete implementation code. They should be implemented as-is.

## Dependency Graph

```
token-calculator.py  <-- standalone, no dependencies
        ^
        |
skill-validator.py   <-- optionally uses token-calculator for budget validation
        |
agents-md-compressor.py  <-- uses token-calculator for savings verification
        |
cost-estimator.py    <-- uses token-calculator for accurate counts
```

## External Dependencies

Minimize external dependencies. Acceptable packages:

- **Required**: None (standard library only for core functionality)
- **Optional**:
  - `tiktoken` (for GPT tokenizer support in token-calculator.py)
  - `anthropic` (for Claude tokenizer support in token-calculator.py)
  - `pyyaml` (for YAML parsing in skill-validator.py -- or use built-in `json` with YAML subset)
  - `pytest` (for running tests)

If external packages are used, include a `requirements.txt`:
```
tiktoken>=0.5.0
pyyaml>=6.0
pytest>=7.0
```

## Cross-References

- **Implementation location**: `common/utilities/`
- **Orchestration utilities**: `common/utilities/file-lock-manager.py`, `common/utilities/status-updater.py`
- **Consumer**: All team templates, CI/CD pipelines, template developers
- **Parent spec**: `specs/01-common-layer/SPEC.md`
- **Master prompt**: `specs/MASTER_PROMPT.md` (Section: 1D - Common Utilities)
- **Test location**: `tests/` (repository root) or `common/utilities/tests/`
