#!/usr/bin/env bash
# Agent Foundry — Launch Content Creation Team
# Research-backed content with brand voice matching
# Agents: 7 | Cost: ~$60-80 | Duration: ~2 hours
exec "$(dirname "$0")/start-team.sh" "content-creation" "${1:-}"
