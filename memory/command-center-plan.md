# 🤖 Jarvis Command Center - Master Plan

*Created: 2026-03-09*
*Updated: 2026-03-11 19:00 UTC*
*Owner: Aaron Maziarz*
*Status: In Progress*

---

## Vision

Transform Jarvis into an AI operations hub that:
1. Manages a team of specialized sub-agents for parallel task execution
2. Provides a real-time dashboard for visibility and control
3. Operates autonomously within defined boundaries while keeping Aaron informed

---

## Current Project Goals

1. Finish functional dashboard wiring so UI controls trigger real agent actions
2. Enable true per-agent model switching instead of cosmetic-only selectors
3. Add reliable budget/spend tracking for OpenRouter usage
4. Complete browser control setup via Chrome Extension Relay
5. Continue UI polish / office redesign work for the command center

---

## Project Status Snapshot

- **Phase 1: Foundation** — ✅ Complete
- **Phase 2: Dashboard v1** — ✅ Complete
- **Phase 3: Real-Time Features** — 🔄 In Progress
  - Polling/status server is in place
  - Browser control and action wiring still need completion
- **Phase 4: Polish** — ⏳ Not complete
  - UI refinements underway
  - Mobile/PWA and Cloudflare tunnel still pending

---

## Recent Completed Work

### Completed on 2026-03-10

- Dashboard created and deployed to GitHub Pages
- 7 sub-agents configured
- 3 GitHub repositories created
- Cron jobs configured and active
- Agent modal added with editable definitions
- Model selector dropdown added
- Thinking level control added
- Per-agent model selection UI added
- Clickable task handling added
- Repositories section added
- Mobile optimization added

### Completed on 2026-03-11

- KPI metrics updated successfully via cron at 2026-03-11 07:08 UTC
- Dashboard sync completed successfully at 2026-03-11 16:03 UTC

### Dashboard URL
- https://aaronmaziarz.github.io/jarvis-command-center/dashboard.html

---

## Tasks In Progress

- Wire dashboard buttons/actions to actual sub-agent spawning
- Make selected dashboard models apply to launched agents
- Fix OpenRouter usage/budget tracking
- Finish Chrome Extension Relay browser setup
- Continue office redesign / agent visualization improvements
- Continue Apple-style UI refinements
- Improve runtime state coverage so all configured agents are tracked consistently

---

## Agent Roster

### Configured Agents (7)
- Researcher — DeepSeek R1
- Coder — Qwen2.5 Coder 32B
- Frontend Dev — Claude Sonnet 4.6
- Security — DeepSeek R1
- Writer — MiniMax M2.5
- Analyst — Qwen Plus
- Scheduler — MiniMax M2.5

### Runtime State Tracked in `memory/agent-states.json`
- Researcher — idle
- Coder — idle
- Writer — idle
- Analyst — idle
- Scheduler — idle

### Tracking Gap
- `Frontend Dev` and `Security` are configured, but not currently represented in `memory/agent-states.json`
- No tracked agent has recorded task completions yet in the state file
- All tracked agents are currently idle as of this sync
- Daily organization review on 2026-03-13 found a few likely orphaned workspace files (`BOOTSTRAP.md`, `dashboard.html.backup`, `do_replace.py`, `new_section.txt`, `replace_agent.py`) that should be reviewed before deletion

---

## Repositories

- `jarvis-command-center` — dashboard project
- `jarvis-journal` — daily summaries / journal
- `jarvis-exchange` — file sharing

---

## Cron Jobs Active

- Morning Brief — 7:30 AM daily
- Dashboard Sync — every 2 hours (8 AM–8 PM)
- Repo Sync — every 2 hours
- KPI Update — every 15 minutes
- Daily Journal — 11 PM daily

---

## Budget Status

- **Budget:** $20/month
- **Default model behavior:** MiniMax M2.5 is still being used unless a different model is explicitly requested
- **Spend telemetry:** Not automated yet
- **Current issue:** Token stats are not being recorded, so actual spend cannot be verified automatically
- **Related follow-up:** OpenRouter usage endpoint may require different API key scope / configuration
- **Current confidence:** Budget cap is known, but live spend visibility is still missing

---

## Current Future Actions

1. Set up proper credential storage
2. Add API keys to environment / docker-compose
3. Document keys in `TOOLS.md`
4. Set up X.com/Twitter access (recommended: Grok API)
5. Enable OpenRouter API usage access for automatic spend tracking
6. Verify all dashboard features are working end-to-end
7. Complete web browser setup (Chrome Extension Relay)
8. Wire dashboard spawning with selected models
9. Enable actual sub-agent model switching
10. Set up Cloudflare tunnel for remote dashboard access
11. Complete office redesign / command center visualization
12. Add missing `Frontend Dev` and `Security` entries to runtime agent-state tracking
13. Set up Discord bot and channels for multi-agent routing

---

## Blockers / Gaps

1. **Budget tracking blocker** — spend is not automatically visible yet
2. **Dashboard action blocker** — model selector and spawn controls are not fully wired
3. **Agent tracking blocker** — runtime state file does not include all configured agents
4. **Browser blocker** — browser automation depends on Chrome Extension Relay setup (or alternate browser path)
5. **Limited daily progress logged today** — only KPI cron completion is recorded so far for 2026-03-11

---

## Other Tracked Initiative

### AI Task Management App
- Research phase was previously marked complete
- No new progress was recorded in the latest daily log
- Main active focus currently remains the Jarvis Command Center

---

## Latest Sync Summary (2026-03-14 21:00 UTC)

- Command center remains the primary active project and is still in build-out mode
- Re-read the current Future Actions list; priorities remain unchanged and still center on credential/env setup, OpenRouter usage access, browser relay setup, dashboard action wiring, true model switching, Cloudflare tunnel access, UI polish, complete agent-state tracking, and Discord bot/channel setup
- Checked `memory/agent-states.json`; all 5 tracked runtime agents (Researcher, Coder, Writer, Analyst, Scheduler) are still idle with zero task completions, zero failures, and no active task timestamps
- Runtime tracking still only covers 5 agents; `Frontend Dev` and `Security` remain configured but missing from the state file
- Checked live session/sub-agent state; no active sub-agents or ACP runs were present during this sync window, and the only visible live session was the current dashboard-sync cron run
- No newly completed implementation work or architecture change was recorded since the 19:00 UTC sync
- Cleanup candidates remain unchanged and should still be reviewed manually before deletion: `BOOTSTRAP.md`, `dashboard.html.backup`, `do_replace.py`, `new_section.txt`, `replace_agent.py`
- `MEMORY.md` still does not exist, so long-term memory consolidation remains blocked for now
- Budget remains set to $20/month, but actual spend still cannot be verified automatically because spend telemetry is not wired yet
- Main blockers remain incomplete telemetry, partial agent-state coverage, unfinished dashboard wiring, pending credential setup, and missing browser relay

---

*Sync completed: 2026-03-14 21:00 UTC*