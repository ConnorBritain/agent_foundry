#!/usr/bin/env bash
# Sforza — Stop All Running Teams
# Kills the sforza tmux session and all team sessions.

set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BOLD='\033[1m'
NC='\033[0m'

echo ""
echo -e "${BOLD}Sforza — Stopping All Teams${NC}"
echo ""

if ! command -v tmux &>/dev/null; then
    echo -e "${YELLOW}[WARN]${NC} tmux not installed. No sessions to stop."
    exit 0
fi

if tmux has-session -t "sforza" 2>/dev/null; then
    # List active windows before killing
    echo "  Active sessions:"
    tmux list-windows -t "sforza" -F "    - #{window_name}" 2>/dev/null || true
    echo ""

    read -rp "  Stop all teams? (Y/n): " CONFIRM
    if [[ "$CONFIRM" == "n" || "$CONFIRM" == "N" ]]; then
        echo -e "${YELLOW}[WARN]${NC} Cancelled."
        exit 0
    fi

    tmux kill-session -t "sforza"
    echo -e "${GREEN}[OK]${NC} All Sforza sessions stopped."
else
    echo "  No active Sforza sessions found."
fi

echo ""
