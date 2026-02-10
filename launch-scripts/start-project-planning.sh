#!/usr/bin/env bash
# Agent Foundry — Launch Project Planning Team
# Multi-team orchestration, SAFe, Agile, Scrum
# Agents: 7 | Cost: ~$50-80 | Duration: ~1.5 hours
exec "$(dirname "$0")/start-team.sh" "project-planning" "${1:-}"
