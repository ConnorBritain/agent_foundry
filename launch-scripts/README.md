# Launch Scripts

Scripts for starting Sforza team sessions.

## Quick Start

```bash
# Launch a single team
./launch-scripts/start-c-suite.sh projects/my-startup

# Launch multiple teams in parallel (requires tmux)
./launch-scripts/start-all-parallel.sh projects/my-startup c-suite research-deep-dive content-creation

# Stop all running teams
./launch-scripts/stop-all.sh
```

## Available Scripts

| Script | Team | Cost | Duration |
|--------|------|------|----------|
| `start-c-suite.sh` | C-Suite (strategy, financials) | ~$150-200 | ~3-4 hours |
| `start-web-app-development.sh` | Web App Development | ~$105 | ~2.75 hours |
| `start-sales-marketing.sh` | Sales & Marketing | ~$80-120 | ~2-3 hours |
| `start-recruitment-hr.sh` | Recruitment & HR | ~$70-100 | ~2-2.5 hours |
| `start-content-creation.sh` | Content Creation | ~$60-80 | ~2 hours |
| `start-code-implementation.sh` | Code Implementation | ~$40-60 | ~1 hour |
| `start-project-planning.sh` | Project Planning | ~$50-80 | ~1.5 hours |
| `start-research-deep-dive.sh` | Research (Deep Dive) | ~$80-120 | ~2-3 hours |
| `start-all-parallel.sh` | Multiple teams (tmux) | Varies | Varies |
| `stop-all.sh` | Stop all teams | — | — |

## Usage

All team scripts follow the same pattern:

```bash
./launch-scripts/start-<team>.sh <project-directory>
```

The generic launcher can also be used directly:

```bash
./launch-scripts/start-team.sh <team-name> <project-directory>
```

## How It Works

Each launch script:

1. Validates the team template exists in `teams/<team-name>/`
2. Creates a team workspace directory in your project
3. Creates an artifacts directory in `shared-workspace/artifacts/<team>/`
4. Builds a prompt with the team spec and project charter
5. Launches Claude Code with the prompt (or saves it for manual use)

## Parallel Execution

`start-all-parallel.sh` requires [tmux](https://github.com/tmux/tmux):

```bash
# Install tmux
brew install tmux      # macOS
apt install tmux       # Ubuntu/Debian
```

It creates a tmux session with one window per team plus a monitoring window.

## Without Claude Code CLI

If you don't have the Claude Code CLI installed, the scripts will save the launch prompt to `.launch-prompt.md` in the team workspace. Copy and paste it into Claude Code (web or IDE).
