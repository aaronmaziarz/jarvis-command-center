# 📋 Jarvis Command Reference

_Comprehensive command structure for the Jarvis AI assistant_

---

## OpenClaw Core Commands

### Gateway Management
| Command | Description |
|---------|-------------|
| `openclaw gateway start` | Start the OpenClaw gateway daemon |
| `openclaw gateway stop` | Stop the gateway daemon |
| `openclaw gateway restart` | Restart the gateway |
| `openclaw gateway status` | Check gateway status |

### Session Management
| Command | Description |
|---------|-------------|
| `openclaw sessions list` | List active sessions |
| `openclaw sessions history <session>` | Get session history |
| `openclaw sessions send <session> <message>` | Send to another session |

### Agent Management
| Command | Description |
|---------|-------------|
| `openclaw agents list` | List available sub-agents |
| `openclaw subagents spawn` | Spawn a sub-agent |
| `openclaw subagents kill` | Terminate sub-agent |

### Cron & Scheduling
| Command | Description |
|---------|-------------|
| `openclaw cron status` | Check cron scheduler status |
| `openclaw cron list` | List scheduled jobs |
| `openclaw cron add` | Add a new cron job |
| `openclaw cron remove <jobId>` | Remove a cron job |
| `openclaw cron run <jobId>` | Run a job immediately |
| `openclaw cron wake` | Send wake event |

### Configuration
| Command | Description |
|---------|-------------|
| `openclaw config get` | Get current config |
| `openclaw config apply` | Apply new config |
| `openclaw config patch` | Patch config |

### System & Diagnostics
| Command | Description |
|---------|-------------|
| `openclaw status` | Full system status |
| `openclaw health` | Health check |
| `openclaw logs` | View logs |
| `openclaw doctor` | Run diagnostics |
| `openclaw update run` | Run updates |

---

## Jarvis-Specific Commands

### Agent Team (Sub-Agents)
| Agent | Role | Trigger |
|-------|------|---------|
| **Researcher** 🤡 | Web search, content fetching, competitive analysis | "Research X", "Find info on Y" |
| **Coder** 💻 | Python, SQL, scripting, automation, debugging | "Write script for X", "Debug this" |
| **Writer** ✍️ | Copy, docs, proposals, content drafting | "Write copy for X", "Draft proposal" |
| **Analyst** 📊 | Data processing, spreadsheets, reporting | "Analyze this data", "Build report" |
| **Scheduler** ⏰ | Calendar, reminders, cron jobs | "Set reminder", "Check calendar" |

### Spawning Sub-Agents
```
sessions_spawn with:
- task: <description>
- runtime: "subagent" | "acp"
- agentId: <agent-name>
- mode: "run" | "session"
```

### Heartbeat Commands
- Check `HEARTBEAT.md` for periodic tasks
- Respond with `HEARTBEAT_OK` when nothing needed

### Memory Commands
- `memory_search` - Search long-term and daily memory
- `memory_get` - Get specific memory file contents
- Write to `memory/YYYY-MM-DD.md` for daily logs
- Update `MEMORY.md` for curated long-term memory

---

## Available Tools (API-Level)

### File Operations
- `read` - Read file contents
- `write` - Create or overwrite files
- `edit` - Make surgical edits to files

### Execution
- `exec` - Run shell commands
- `process` - Manage background exec sessions

### Web & Browser
- `web_search` - Search the web (Brave/Perplexity)
- `web_fetch` - Fetch and extract content from URLs
- `browser` - Control web browser automation

### Communication
- `message` - Send messages via channels (Telegram, Discord, Signal, WhatsApp, etc.)
- `tts` - Text-to-speech conversion

### System
- `cron` - Manage scheduled jobs and wake events
- `gateway` - Gateway restart, config, updates
- `session_status` - Get session usage stats
- `sessions_spawn` - Spawn isolated sub-agents or ACP sessions

### Paired Nodes
- `nodes` - Control paired devices (camera, location, notifications, etc.)

---

## Skill Commands

### Available Skills
| Skill | Purpose |
|-------|---------|
| **healthcheck** | Security hardening, firewall, SSH hardening, risk assessment |
| **skill-creator** | Create/update AgentSkills |
| **weather** | Get current weather and forecasts |

### Using Skills
- Read `SKILL.md` when task matches skill description
- Follow skill-specific instructions for that task type

---

## Messaging Surfaces

### Supported Channels
- Telegram
- Discord
- WhatsApp
- Signal
- IRC
- Google Chat
- Slack
- iMessage
- Line
- Webchat

### Message Actions
- `send` - Send message
- `react` - Add reaction
- `poll` - Create polls
- `edit` - Edit message
- `delete` - Delete message

---

## Budget Management

- **$20/month** allocated for API usage
- Track via `session_status`
- Alert when below $5 remaining
- Default to efficient models for simple tasks

---

## File Locations

| Purpose | File |
|---------|------|
| Identity | `IDENTITY.md` |
| User info | `USER.md` |
| Soul/Persona | `SOUL.md` |
| Tools setup | `TOOLS.md` |
| Agent definitions | `memory/subagents.md` |
| Command center plan | `memory/command-center-plan.md` |
| Daily logs | `memory/YYYY-MM-DD.md` |
| Long-term memory | `MEMORY.md` |

---

*This file auto-generated from workspace exploration*