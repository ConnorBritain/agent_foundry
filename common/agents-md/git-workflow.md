# Git Workflow — Compressed AGENTS.md Knowledge

## Quick Reference
| Area | Key Concepts |
|---|---|
| Branching | trunk-based, GitHub Flow, feature branches, release branches |
| Commits | Conventional Commits, atomic commits, message format |
| PR Workflow | Draft PRs, review process, merge strategies, templates |
| CI/CD | GitHub Actions, pre-commit hooks, automated checks |
| Collaboration | Code owners, branch protection, merge queue |
| Recovery | Revert, cherry-pick, bisect, reflog |

## Branching Strategies
### GitHub Flow (Recommended for most teams)
```
main (always deployable)
  └── feature/add-user-auth (short-lived branch)
       └── PR → review → merge to main → deploy
```

| Rule | Detail |
|---|---|
| main is sacred | Always deployable, never commit directly |
| Feature branches | Branch from main, merge back to main |
| Short-lived | Days, not weeks — smaller PRs merge faster |
| Delete after merge | Clean up remote branches post-merge |

### Trunk-Based Development
```
main (deploy continuously)
  └── short-lived branches (< 1 day) or direct commits with feature flags
```

### Release Branches (For versioned software)
```
main → develop → feature branches
          └── release/1.2.0 → hotfix → tag → merge back
```

## Branch Naming Conventions
| Pattern | Example |
|---|---|
| feature/{ticket}-{desc} | feature/AUTH-123-add-oauth |
| fix/{ticket}-{desc} | fix/BUG-456-null-pointer |
| chore/{desc} | chore/update-dependencies |
| docs/{desc} | docs/api-reference |
| refactor/{desc} | refactor/extract-auth-module |
| release/{version} | release/1.2.0 |
| hotfix/{desc} | hotfix/critical-auth-bypass |

## Conventional Commits
```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Types
| Type | When to Use |
|---|---|
| feat | New feature (triggers MINOR version bump) |
| fix | Bug fix (triggers PATCH version bump) |
| docs | Documentation only |
| style | Formatting, missing semicolons (no code change) |
| refactor | Code change that neither fixes nor adds feature |
| perf | Performance improvement |
| test | Adding or correcting tests |
| build | Build system or external dependencies |
| ci | CI configuration changes |
| chore | Other changes that don't modify src or test |
| revert | Reverts a previous commit |

### Breaking Changes
```
feat!: remove deprecated auth endpoint
  OR
feat(auth): add new login flow

BREAKING CHANGE: /api/v1/login removed, use /api/v2/auth instead
```

### Good Commit Messages
```
feat(auth): add OAuth2 PKCE flow for GitHub login

Implements the authorization code flow with PKCE for GitHub OAuth.
This replaces the implicit flow for improved security in SPAs.

Closes #234
```

| Rule | Example |
|---|---|
| Imperative mood | "add feature" not "added feature" |
| No period at end | "fix null check" not "fix null check." |
| Max 72 chars subject | Keep it concise |
| Body explains WHY | Not what (code shows what) |
| Reference issues | Closes #123, Fixes #456 |

## Atomic Commits
```
Each commit should:
1. Represent ONE logical change
2. Compile and pass tests independently
3. Be revertable without side effects
4. Have a clear, descriptive message

Anti-patterns:
- "WIP" commits in main branch
- "fix stuff" — meaningless messages
- Giant commits with unrelated changes
- Commits that break the build
```

## Pull Request Workflow
### PR Template
```markdown
## What
Brief description of the change.

## Why
Context and motivation.

## How
Implementation approach and key decisions.

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests pass
- [ ] Manual testing completed

## Screenshots (if UI change)

## Related
Closes #123
```

### PR Best Practices
| Practice | Detail |
|---|---|
| Small PRs | < 400 lines changed, single concern |
| Draft PRs early | Get feedback before investing heavily |
| Self-review first | Review your own diff before requesting |
| Descriptive title | Conventional commit format for PR title |
| Link issues | Connect PR to issue/ticket for traceability |
| Respond promptly | Review comments within 24 hours |
| Don't force push | After review starts, add fixup commits |
| Squash on merge | Clean history, one commit per PR in main |

### Merge Strategies
| Strategy | When |
|---|---|
| Squash and merge | Default — clean linear history, one commit per PR |
| Merge commit | Preserve full branch history (complex features) |
| Rebase and merge | Linear history, preserves individual commits |

## CI/CD with GitHub Actions
### Basic Workflow
```yaml
# .github/workflows/ci.yml
name: CI
on:
  pull_request:
    branches: [main]
  push:
    branches: [main]

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 20, cache: 'pnpm' }
      - run: pnpm install --frozen-lockfile
      - run: pnpm lint
      - run: pnpm typecheck
      - run: pnpm test -- --coverage
      - run: pnpm build
```

### Branch Protection Rules
```
Required for main branch:
- Require PR reviews (1-2 approvals)
- Require status checks to pass (CI, lint, tests)
- Require branches to be up to date
- Require linear history (squash merge)
- Restrict who can push directly
- Require signed commits (optional, high-security)
```

## Pre-commit Hooks (Husky + lint-staged)
```json
// package.json
{
  "scripts": { "prepare": "husky" },
  "lint-staged": {
    "*.{ts,tsx}": ["eslint --fix", "prettier --write"],
    "*.{json,md,yml}": ["prettier --write"]
  }
}
```

```bash
# .husky/pre-commit
pnpm lint-staged

# .husky/commit-msg
pnpm commitlint --edit $1
```

### Commitlint Config
```javascript
// commitlint.config.js
export default {
  extends: ['@commitlint/config-conventional'],
  rules: { 'scope-enum': [2, 'always', ['auth', 'api', 'ui', 'db', 'ci']] },
};
```

## Git Recovery & Debugging
| Situation | Command |
|---|---|
| Undo last commit (keep changes) | git reset --soft HEAD~1 |
| Undo staged changes | git restore --staged <file> |
| Discard working changes | git restore <file> |
| Revert a merged PR | git revert -m 1 <merge-commit-sha> |
| Cherry-pick a commit | git cherry-pick <sha> |
| Find bug introduction | git bisect start → git bisect bad → git bisect good <sha> |
| See all history including resets | git reflog |
| Stash changes | git stash push -m "description" |
| Apply stash | git stash pop (or apply to keep in stash) |

## Code Owners
```
# .github/CODEOWNERS
* @team/engineering
/src/auth/ @team/security
/src/payments/ @team/billing @lead-dev
*.sql @team/dba
/docs/ @team/docs
```

## Git Configuration
```bash
# Useful aliases
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.st status
git config --global alias.lg "log --oneline --graph --decorate -20"
git config --global alias.amend "commit --amend --no-edit"

# Auto-setup remote tracking
git config --global push.autoSetupRemote true

# Default branch
git config --global init.defaultBranch main

# Rebase on pull (avoid merge commits)
git config --global pull.rebase true
```

## Workflow Checklist
```
[ ] Branch from latest main
[ ] Write code with atomic commits (conventional format)
[ ] Self-review diff before pushing
[ ] Open PR with description, link issue
[ ] Ensure CI passes (lint, type, test, build)
[ ] Address review feedback (new commits, not force push)
[ ] Squash merge to main
[ ] Delete feature branch
[ ] Verify deployment
```
