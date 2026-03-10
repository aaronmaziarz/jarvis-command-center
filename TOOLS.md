# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific
- Command reference shortcuts

## Sub-Agent Configuration

### Active Agents
| Agent | Status | Speciality |
|-------|--------|------------|
| Researcher (🤡) | Active | Web search, content fetching |
| Coder (💻) | Active | Python, SQL, scripting |
| Writer (✍️) | Planned | Copy, docs, proposals |
| Analyst (📊) | Planned | Data processing, reporting |
| Scheduler (⏰) | Planned | Calendar, reminders |

### Spawn Command Template
```bash
sessions_spawn task="<description>" runtime="subagent" agentId="<researcher|coder>" mode="run"
```

## Budget
- **$20/month** on OpenRouter
- Current model: `openrouter/minimax/minimax-m2.5`

## TTS Configuration
- Preferred voice: Use default (system will select)
- Channel: Match the inbound channel for best delivery

## Reference
- Full command reference: `COMMANDS.md`
- Agent definitions: `memory/subagents.md`
- Command center plan: `memory/command-center-plan.md`

---

*Updated 2026-03-10*
