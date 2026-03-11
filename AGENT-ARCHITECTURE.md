# 🤖 OpenClaw Multi-Agent Architecture

*Status: Implemented 2026-03-11*
*Config Repo: aaronmaziarz/openclaw-agent-configuration*

---

## Summary

I've implemented a production-grade multi-agent architecture with:

### What Was Built

1. **12 Registered Agents** in a tiered system:
   - **Tier 1 (Executive)**: brain - the main orchestrator
   - **Tier 2 (Domain Leads)**: senior-dev, researcher, project-manager
   - **Tier 3 (Specialists)**: frontend-dev, backend, qa-test, scripting-automation, docs-writer, daily-brief, cron-reporter, discord-ops

2. **Maintainable Agent Management**:
   - Single source of truth: `agents/manifest.json`
   - Per-agent prompt files: `agents/<agent_id>/prompt.md`
   - Generator script: `agents/generate-config.py`

3. **Routing Architecture**:
   - Brain is always the intake point
   - Brain decides: direct answer vs. delegate
   - Domain leads decompose work for specialists
   - Clear routing rules documented in `agents/ROUTING.md`

4. **Discord Channel Structure** (ready for setup):
   - #brain - Main interaction
   - #daily-brief - Morning briefings  
   - #project-updates - Status updates
   - #cron-runs - Automation logs
   - #agent-* - Direct specialist interaction

5. **Documentation**:
   - `agents/OPERATOR.md` - How to manage agents
   - `agents/ROUTING.md` - How routing works

---

## Architecture Diagram

```
                    ┌─────────────┐
                    │   USER      │
                    └──────┬──────┘
                           │
                           ▼
                 ┌─────────────────┐
                 │  BRAIN (Tier 1) │ ← Top-level orchestrator
                 │   Jarvis        │
                 └────────┬────────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
  ┌──────────┐     ┌────────────┐    ┌─────────────┐
  │Researcher│     │ Senior-Dev │    │ Project Mgr │
  │ (Tier 2) │     │ (Tier 2)   │    │  (Tier 2)   │
  └──────────┘     └─────┬──────┘    └─────────────┘
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
  ┌──────────┐    ┌──────────┐    ┌────────────┐
  │Frontend  │    │ Backend  │    │  QA/Test   │
  │  Dev     │    │          │    │            │
  └──────────┘    └──────────┘    └────────────┘
        │                │                │
        └────────────────┼────────────────┘
                         ▼
                  ┌──────────────┐
                  │   Review     │
                  │   to Brain   │
                  └──────────────┘
```

---

## Agent Definitions

| Agent ID | Role | Tier | Model | Purpose |
|----------|------|------|-------|---------|
| brain | Executive Orchestrator | 1 | MiniMax M2.5 | Main interface, routing |
| senior-dev | Engineering Lead | 2 | Claude Sonnet 4 | Code decomposition |
| researcher | Research Lead | 2 | DeepSeek R1 | Deep research |
| project-manager | Project Tracking | 2 | MiniMax M2.5 | Status summaries |
| frontend-dev | UI/UX Specialist | 3 | Claude Sonnet 4 | Dashboards, UI |
| backend | Backend/Systems | 3 | Qwen Coder | APIs, databases |
| qa-test | Testing/QA | 3 | Qwen Plus | Code review, testing |
| scripting-automation | Automation | 3 | Qwen Coder | Scripts, cron |
| docs-writer | Documentation | 3 | MiniMax M2.5 | Copy, docs |
| daily-brief | Daily Summaries | 3 | MiniMax M2.5 | Morning briefings |
| cron-reporter | Automation Logs | 3 | MiniMax M2.5 | Cron reporting |
| discord-ops | Discord Ops | 3 | MiniMax M2.5 | Discord management |

---

## Routing Rules

### When Brain Answers Directly
- Greetings
- Status checks
- Simple questions
- Help requests
- Meta questions about Jarvis

### When Brain Delegates
- **Engineering tasks** → senior-dev → specialist(s) → review → brain
- **Research tasks** → researcher → brain
- **Project tracking** → project-manager → brain

### Failure Handling
1. Specialist fails → domain lead retries
2. Lead fails → brain attempts direct answer
3. All fail → report inability

---

## Configuration Files

| File | Purpose |
|------|---------|
| `manifest.json` | Single source of truth for all agents |
| `manifest.yaml` | YAML version (for future tools) |
| `generate-config.py` | Config generator script |
| `ROUTING.md` | Detailed routing decisions |
| `OPERATOR.md` | How to manage the system |

---

## Discord Channel Setup (Manual Step Required)

The Discord channels need to be created and IDs captured:

1. Create channels in Discord (enable Developer Mode first)
2. Right-click each channel → Copy ID
3. Update `manifest.json` channel_bindings section
4. Restart gateway

Channel recommendations:
- #brain - Main interactions
- #daily-brief - Daily briefings  
- #project-updates - Milestones
- #cron-runs - Automation logs
- #agent-senior-dev - Direct to Senior Dev
- #agent-frontend-dev - Direct to Frontend
- #agent-backend - Direct to Backend
- #agent-researcher - Direct to Researcher

---

## Manual Setup Steps Required

1. **Discord Setup** (if using Discord):
   - Create Discord server with recommended channels
   - Enable Developer Mode in Discord settings
   - Copy channel IDs
   - Add Discord bot to server
   - Update manifest.json with channel IDs
   - Add Discord config to OpenClaw

2. **Test Routing**:
   - Try a simple task (should answer directly)
   - Try a coding task (should route to senior-dev)
   - Try a research task (should route to researcher)

---

## Known Limitations

1. **Agent Registration**: OpenClaw doesn't have a native "register agent" API - these are logical agents defined in config. The routing uses sessions_spawn to launch them.

2. **Channel Bindings**: Discord channel bindings need manual ID capture.

3. **Persistence**: Agent state is tracked in memory files, not in OpenClaw's native state.

---

## Next Steps

1. Set up Discord channels (if desired)
2. Test the routing flow
3. Customize prompts in `agents/<agent_id>/prompt.md`
4. Add more specialists as needed

---

*Config repo: https://github.com/aaronmaziarz/openclaw-agent-configuration*
