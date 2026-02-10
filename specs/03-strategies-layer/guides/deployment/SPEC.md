# Deployment and Operations Specification

> **STATUS**: STATIC REFERENCE -- Extracted from master prompt. Never modified, only consulted.

## Purpose

Provide practical guidance for deploying agent systems from local development through production. Cover development workflows, CI/CD integration, monitoring, version control for agent configurations, team collaboration, environment management, secrets handling, and production readiness.

## Output File

`strategies/deployment.md`

## Content Structure

### 1. Local Development Workflows

#### Repository Setup
- Directory structure conventions (following Agent Template Library layout)
- Initial configuration steps
- Local dependency installation
- Environment variable setup
- First-run validation checklist

#### Development Cycle
1. **Configure**: Set up AGENTS.md, Skills, MCP servers
2. **Validate**: Run skill-validator.py, token-calculator.py
3. **Test locally**: Execute workflow with test inputs
4. **Measure**: Use cost-estimator.py to project costs
5. **Iterate**: Adjust configurations based on results
6. **Commit**: Version control agent configurations

#### Local Multi-Agent Testing
- Running multiple agent instances locally
- Using shared-state for coordination testing
- File lock manager for conflict prevention
- Communication protocol testing
- Simulating parallel execution sequentially

### 2. CI/CD Integration Patterns

#### Pre-Commit Hooks
- Skill validation (YAML frontmatter, required fields, token limits)
- AGENTS.md token budget checking (reject if over budget)
- Configuration lint (formatting, required sections)
- Secret scanning (prevent credential commits)

#### CI Pipeline Stages

**Stage 1: Validation**
```yaml
# Example CI configuration structure
validate:
  - skill-validator.py --all
  - token-calculator.py --budget-check
  - agents-md-compressor.py --validate
  - config-lint (check YAML, markdown structure)
```

**Stage 2: Dry Run Testing**
```yaml
test:
  - Run agent with test fixtures (no real API calls)
  - Validate output format and structure
  - Check token usage against budgets
  - Verify skill trigger patterns with test prompts
```

**Stage 3: Integration Testing**
```yaml
integration:
  - Run with real models (limited token budget)
  - Validate MCP server connectivity
  - Test multi-agent coordination (if applicable)
  - Measure quality metrics against baseline
```

**Stage 4: Cost Estimation**
```yaml
cost-check:
  - Project costs for production run
  - Compare against budget thresholds
  - Flag if estimated cost exceeds limits
  - Generate cost report for review
```

#### CD Pipeline Stages

**Stage 5: Staging Deployment**
- Deploy to staging environment
- Run full workflow with representative inputs
- Compare outputs to golden reference set
- Human review gate for first deployment

**Stage 6: Production Deployment**
- Blue-green deployment for agent configurations
- Canary testing (route subset of tasks to new config)
- Automated rollback on quality metric degradation
- Post-deployment monitoring period

#### GitHub Actions / GitLab CI Examples
- Provide complete workflow files for common CI systems
- Include conditional logic for different change types
- Show how to cache model responses for faster CI
- Demonstrate cost-gated approvals

### 3. Monitoring and Cost Tracking

#### Real-Time Monitoring
- Token usage dashboards (per agent, per phase, per workflow)
- Cost accumulation tracking with alerts
- Error rate monitoring and trending
- Quality metric tracking
- Session duration and status

#### Cost Tracking Infrastructure
- Per-workflow cost attribution
- Per-agent cost breakdown
- Daily/weekly/monthly cost reports
- Budget vs actual comparison
- Cost anomaly detection

#### Logging Strategy
- Structured logging format for agent operations
- Log levels: DEBUG (full context), INFO (decisions), WARN (issues), ERROR (failures)
- Log rotation and retention policies
- Centralized logging for multi-agent teams
- Log analysis for optimization insights

#### Alerting
- Budget threshold alerts (70%, 90%, 100%)
- Quality degradation alerts
- Agent failure alerts
- Stall detection alerts
- Cost anomaly alerts
- Integration with Slack/PagerDuty/email

### 4. Version Control for Agent Configurations

#### What to Version Control
- AGENTS.md files (all)
- SKILL.md files and references (all)
- MCP server configurations (all, minus secrets)
- Team specifications (TEAM_SPEC.md, ORCHESTRATION.md)
- Cost analysis documents
- Deployment guides
- Utility scripts

#### What NOT to Version Control
- Runtime state (shared-state/agent-status.json)
- Lock files (shared-state/locks/)
- Communication logs (shared-state/communication.md)
- Active session logs (logs/active/)
- Secrets and API keys (.env, credentials)
- Large binary artifacts

#### Branching Strategy
- `main`: Production-ready agent configurations
- `develop`: Integration branch for configuration changes
- `feature/[name]`: New agent configs, new skills, new teams
- `fix/[name]`: Bug fixes to existing configurations
- `experiment/[name]`: Model selection experiments, A/B tests

#### Change Management
- PR template for agent configuration changes
- Required review checklist:
  - [ ] Token budget validated
  - [ ] Skill trigger patterns tested
  - [ ] Cost impact estimated
  - [ ] Backward compatibility confirmed
  - [ ] Documentation updated
- Semantic versioning for team templates

### 5. Team Collaboration Best Practices

#### Shared Configuration Management
- Central repository for common layer (AGENTS.md templates, universal skills)
- Team-specific repositories or directories for team templates
- Clear ownership model (who maintains what)
- Contribution guidelines for new templates

#### Knowledge Sharing
- Template usage documentation
- Cost benchmarks and lessons learned
- Skill trigger pattern library (what works, what doesn't)
- Model selection results from A/B tests
- Post-mortem reports for failed workflows

#### Review Process
- Peer review for new Skills (focus on trigger reliability)
- Token budget review for AGENTS.md changes
- Cost impact review for team template changes
- Quality metric review after configuration changes

#### Onboarding
- Getting started guide for new team members
- Walkthrough of Agent Template Library structure
- Hands-on tutorial with simple single-agent workflow
- Escalation path for issues and questions

### 6. Environment Management

#### Environment Types
- **Local**: Developer machine, full debug access, test fixtures
- **CI/CD**: Automated pipeline, limited token budget, test data
- **Staging**: Pre-production, representative data, full monitoring
- **Production**: Live workflows, real data, cost controls, alerting

#### Environment Configuration

```
# Environment-specific overrides
environments/
├── local/
│   ├── .env.local
│   ├── model-overrides.yaml    # Use cheaper models locally
│   └── budget-limits.yaml      # Lower budgets for testing
├── ci/
│   ├── .env.ci
│   ├── model-overrides.yaml    # Test models or mocks
│   └── budget-limits.yaml      # Strict budgets
├── staging/
│   ├── .env.staging
│   ├── model-overrides.yaml    # Production models, lower volume
│   └── budget-limits.yaml      # Production-like budgets
└── production/
    ├── .env.production
    ├── model-overrides.yaml    # Full production models
    └── budget-limits.yaml      # Production budgets with alerts
```

#### Environment Parity
- Use same agent configurations across environments
- Only vary: model selection, token budgets, data sources, secrets
- Test with production-equivalent configurations in staging
- Document environment-specific differences

### 7. Secrets Handling

#### Secret Categories
- **API keys**: Model provider keys, MCP server credentials
- **Service tokens**: GitHub, Linear, Jira, Notion tokens
- **Database credentials**: Connection strings, passwords
- **Encryption keys**: For secure state storage

#### Secret Management Practices
- Never commit secrets to version control
- Use environment variables for all secrets
- Use `.env` files locally (in `.gitignore`)
- Use CI/CD secret stores for pipelines
- Use vault services (HashiCorp Vault, AWS Secrets Manager) for production
- Rotate secrets regularly
- Audit secret access

#### MCP Server Secret Configuration
- Store MCP credentials separately from server configuration
- Reference secrets by environment variable name, not value
- Document required secrets in MCP README (names, not values)
- Provide setup instructions for obtaining each credential

#### Secret Scanning
- Pre-commit hook to scan for accidental secret commits
- CI check for secrets in configuration files
- Regular audit of repository for leaked secrets
- Remediation process for leaked secrets

### 8. Production Readiness Checklist

#### Pre-Launch Checklist

```markdown
## Agent Configuration
- [ ] All AGENTS.md files validated and within token budget
- [ ] All Skills pass agentskills.io spec validation
- [ ] All MCP servers configured and connectivity tested
- [ ] Model selection documented and justified
- [ ] Token budgets set with 20% buffer
- [ ] Cost projections calculated and approved

## Quality Assurance
- [ ] Skill trigger reliability tested (>90% target)
- [ ] End-to-end workflow tested with representative inputs
- [ ] Output quality validated against acceptance criteria
- [ ] Error handling tested (what happens when models fail?)
- [ ] Recovery procedures documented and tested
- [ ] Regression test suite established

## Operations
- [ ] Monitoring dashboards deployed
- [ ] Alert thresholds configured
- [ ] Cost tracking active
- [ ] Logging configured and retention policy set
- [ ] On-call rotation established (for production teams)
- [ ] Runbook created for common issues

## Security
- [ ] All secrets in secure storage (not in code)
- [ ] Secret scanning enabled in CI/CD
- [ ] Access controls configured for agent operations
- [ ] Data handling compliant with requirements (GDPR, HIPAA if applicable)
- [ ] Audit logging enabled

## Documentation
- [ ] Deployment guide complete and tested
- [ ] Troubleshooting guide created
- [ ] Cost estimation methodology documented
- [ ] Team collaboration guidelines published
- [ ] Rollback procedure documented

## Approval
- [ ] Technical review complete
- [ ] Cost approval obtained
- [ ] Stakeholder sign-off received
- [ ] Go-live date confirmed
```

## Writing Guidelines

- Include complete, copy-paste-ready configuration examples
- Provide CI/CD workflow files for GitHub Actions and GitLab CI
- Include concrete directory structures and file layouts
- Show real-world examples of each deployment stage
- Address both single-developer and team scenarios
- Include rollback procedures for every deployment step

## Dependencies

- CI/CD platform documentation (GitHub Actions, GitLab CI)
- Secret management service documentation
- Monitoring platform integration details
- Common utility scripts from common layer

## Cross-References

- **Strategies Layer**: `specs/03-strategies-layer/SPEC.md`
- **Quality Guide**: `specs/03-strategies-layer/guides/quality/SPEC.md` (testing and validation)
- **Optimization Guide**: `specs/03-strategies-layer/guides/optimization/SPEC.md` (cost optimization)
- **Common Utilities**: `specs/01-common-layer/utilities/SPEC.md` (validator, calculator scripts)
- **Teams Layer**: `specs/02-teams-layer/SPEC.md` (team-specific deployment)
