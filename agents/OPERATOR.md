# OpenClaw Agent System - Operator Guide

## Quick Reference

### View All Agents
`agents/manifest.json`

### Modify Agent Prompt
1. Edit: `agents/<agent_id>/prompt.md`
2. Restart gateway

### Change Agent Model  
Edit `agents/manifest.json` → change `model` field

## Agent Definitions

| Agent | Role | Tier | Model |
|-------|------|------|-------|
| brain | Executive Orchestrator | 1 | minimax-m2.5 |
| senior-dev | Engineering Lead | 2 | claude-sonnet-4 |
| researcher | Research Lead | 2 | deepseek-r1 |
| frontend-dev | UI/UX | 3 | claude-sonnet-4 |
| backend | Backend | 3 | qwen-coder |
| qa-test | Testing | 3 | qwen-plus |
| scripting-automation | Automation | 3 | qwen-coder |
| docs-writer | Documentation | 3 | minimax-m2.5 |
| project-manager | Project Tracking | 2 | minimax-m2.5 |
| daily-brief | Daily Summaries | 3 | minimax-m2.5 |
| cron-reporter | Automation Logs | 3 | minimax-m2.5 |
| discord-ops | Discord Ops | 3 | minimax-m2.5 |

## Discord Channel Setup

To enable Discord channels:
1. Create channels in Discord
2. Get channel IDs (Developer Mode → right-click → Copy ID)
3. Update `manifest.json` with channel IDs
4. Configure Discord bot in OpenClaw

## Troubleshooting

**Agent not responding:**
- Check manifest.json registration
- Verify model is valid
- Check workspace permissions

**Delegation not working:**
- Verify routing rules
- Check brain can spawn agents

---

Generated: 2026-03-11T18:23:29.747501
