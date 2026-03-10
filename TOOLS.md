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
| Agent | Status | Model | Speciality |
|-------|--------|-------|------------|
| Researcher (🤡) | Active | DeepSeek R1 | Web search, content fetching |
| Coder (💻) | Active | Qwen2.5 Coder 32B | Python, SQL, scripting |
| Writer (✍️) | Planned | MiniMax M2.5 | Copy, docs, proposals |
| Analyst (📊) | Planned | Qwen Plus | Data processing, reporting |
| Scheduler (⏰) | Planned | MiniMax M2.5 | Calendar, reminders |

### Spawn Command Template
```bash
sessions_spawn task="<description>" runtime="subagent" agentId="<researcher|coder>" mode="run"
```

## Browser Control

### Current Status
- No Chromium installed in container
- Using web_search/web_fetch for research
- Full browser automation requires Chrome extension relay

### Setup: Chrome Extension Relay (Recommended)
1. Install OpenClaw Chrome extension on your Windows Chrome
2. Open Chrome and click the OpenClaw toolbar icon on any tab
3. Badge shows "ON" when connected
4. Use `browser` tool with `profile="chrome"` to control

### Alternative: Install in Docker
- Would require modifying Dockerfile or privileged mode
- Lower priority - focus on extension relay first

## Dashboard URLs
- **GitHub Pages:** https://aaronmaziarz.github.io/jarvis-command-center/dashboard.html
- **Local (when on same network):** http://<PC-IP>:18790/status.json

## Budget
- **$20/month** on OpenRouter
- Current default model: `minimax-m2.5`
- Researcher: `deepseek-r1` (~$0.07/1M tokens)
- Coder: `qwen2.5-coder-32b-instruct` (~$0.20/1M tokens)

## TTS Configuration
- Preferred voice: Use default (system will select)
- Channel: Match the inbound channel for best delivery

## Reference
- Full command reference: `COMMANDS.md`
- Agent definitions: `memory/subagents.md`
- Command center plan: `memory/command-center-plan.md`
- Future Actions: Check dashboard

---

*Updated 2026-03-10*
