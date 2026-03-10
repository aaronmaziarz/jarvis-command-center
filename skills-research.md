# 🤖 Jarvis Skills & Tools Research

*Compiled: 2026-03-10*
*Purpose: Document all available capabilities*

---

## 📦 Bundled Skills (No Install Needed)

| Category | Skill | What It Does | Status |
|----------|-------|--------------|--------|
| **Developer Productivity** | `coding-agent` | Delegate coding to Codex/Claude Code agents | ✅ Ready |
| | `github` | GitHub: issues, PRs, CI runs, code review | ✅ Ready |
| | `tmux` | Remote-control tmux sessions | ✅ Ready |
| | `session-logs` | Search/analyze session logs | ✅ Ready |
| | `model-usage` | Per-model cost tracking (macOS) | ⚠️ Limited |
| **System Management** | `healthcheck` | Security hardening & audits | ✅ Ready |
| **Research & Data** | `summarize` | Summarize URLs, files, YouTube | ✅ Ready |
| | `blogwatcher` | Monitor blogs & RSS feeds | ✅ Ready |
| **Automation** | `skill-creator` | Create/update AgentSkills | ✅ Ready |
| **Security** | `1password` | 1Password CLI for secrets | ⚠️ CLI needed |
| **Communication** | `slack` | Slack: react, pin, send messages | ✅ Ready |
| | `discord` | Discord messaging | ✅ Ready |
| **Note-Taking** | `obsidian` | Obsidian vault via CLI | ⚠️ CLI needed |
| | `notion` | Notion API for pages/databases | ⚠️ Token needed |
| | `apple-notes` | Apple Notes integration | ⚠️ macOS only |
| | `bear-notes` | Bear notes integration | ⚠️ macOS only |
| **Productivity** | `trello` | Trello board management | ✅ Ready |
| | `things-mac` | Things.app task management | ⚠️ macOS only |
| | `gh-issues` | GitHub issues management | ✅ Ready |
| **Media** | `spotify-player` | Spotify playback control | ⚠️ API key needed |
| | `sag` | ElevenLabs TTS for voice | ⚠️ API key needed |
| | `sherpa-onnx-tts` | Offline TTS | ✅ Ready |
| | `video-frames` | Extract frames from videos | ✅ Ready |
| | `songsee` | Song identification | ✅ Ready |
| **Smart Home** | `openhue` | Philips Hue control | ✅ Ready |
| | `sonoscli` | Sonos speaker control | ✅ Ready |

---

## 🔧 Recommended to Add (Install)

| Skill | Command | Purpose |
|-------|---------|---------|
| `notion` | `clawhub install notion` | Connect to Monday CRM |
| `1password` | `brew install 1password-cli` then enable | Secrets management |
| `wacli` | `clawhub install wacli` | WhatsApp automation |

---

## 🧠 Tools Available (Built-in)

### Core Tools
- `web_search` - Web search via Perplexity
- `web_fetch` - Fetch URL content
- `exec` - Run shell commands
- `read/write/edit` - File operations
- `sessions_spawn` - Spawn sub-agents
- `browser` - Browser automation (via relay)
- `canvas` - UI rendering

### API Access
- OpenRouter: 30+ models available
- GitHub: Full API access
- OpenClaw: Cron, healthcheck, sessions

---

## ⚠️ What's Needed From Aaron

| Item | Status | Action Needed |
|------|--------|---------------|
| Codex CLI | Not installed | Run on PC: `npm install -g @openai/codex` |
| OpenRouter key | Works for calls | Usage API needs different scope |
| 1Password CLI | Not installed | `brew install 1password-cli` |
| Obsidian CLI | Not installed | `brew install obsidian-cli` |

---

## 💡 Suggestions for Expansion

1. **Enable Notion** - Connect to your Monday CRM workflows
2. **Add WhatsApp** - wacli for WhatsApp automation
3. **Setup 1Password** - Better secrets management

---

*This document lives in jarvis-exchange/skills-research.md*