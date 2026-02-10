#!/usr/bin/env bash
# Agent Foundry — Stop All Running Teams
# Kills the agent-foundry tmux session and all team sessions.

set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BOLD='\033[1m'
NC='\033[0m'

echo ""
echo -e "${BOLD}Agent Foundry — Stopping All Teams${NC}"
echo ""

if ! command -v tmux &>/dev/null; then
    echo -e "${YELLOW}[WARN]${NC} tmux not installed. No sessions to stop."
    exit 0
fi

if tmux has-session -t "agent-foundry" 2>/dev/null; then
    # List active windows before killing
    echo "  Active sessions:"
    tmux list-windows -t "agent-foundry" -F "    - #{window_name}" 2>/dev/null || true
    echo ""

    read -rp "  Stop all teams? (Y/n): " CONFIRM
    if [[ "$CONFIRM" == "n" || "$CONFIRM" == "N" ]]; then
        echo -e "${YELLOW}[WARN]${NC} Cancelled."
        exit 0
    fi

    tmux kill-session -t "agent-foundry"
    echo -e "${GREEN}[OK]${NC} All Agent Foundry sessions stopped."
else
    echo "  No active Agent Foundry sessions found."
fi

echo ""
