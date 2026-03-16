# MEMORY.md

## Ongoing Projects
- Jarvis command center/dashboard work remains in planning and setup mode, with recurring priorities around credential/env setup, OpenRouter usage access, browser relay setup, dashboard action wiring, true per-agent model switching, Cloudflare tunnel access, UI polish, full runtime state coverage, and Discord bot/channel setup.

## Current Operational State
- Runtime agent tracking currently covers 5 agents (Researcher, Coder, Writer, Analyst, Scheduler), all recently observed idle with zero task completions and zero failures.
- Runtime state coverage is incomplete: configured agents `Frontend Dev` and `Security` are still missing from `memory/agent-states.json`.
- Spend telemetry is not yet wired, so the configured $20/month budget cannot be automatically verified.

## Maintenance Notes
- Repeated dashboard syncs through 2026-03-16 found no newly completed implementation work, no active/recent sub-agent or ACP sessions beyond cron runs, and no architecture changes.
- Cleanup candidates still pending manual review: `BOOTSTRAP.md`, `dashboard.html.backup`, `do_replace.py`, `new_section.txt`, `replace_agent.py`.
- `BOOTSTRAP.md` is still present even though onboarding appears complete, so it remains the strongest orphaned-file candidate.
