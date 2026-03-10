# 🤖 Jarvis Command Center - Master Plan

*Created: 2026-03-09*
*Updated: 2026-03-10*
*Owner: Aaron Maziarz*
*Status: In Progress*

---

## Vision

Transform Jarvis into an AI operations hub that:
1. **Manages a team of specialized sub-agents** for parallel task execution
2. **Provides a real-time dashboard** for full system visibility and control
3. **Operates autonomously** within defined boundaries while keeping Aaron in the loop

---

## Part 1: Agent Team Architecture

### The Squad (Sub-Agent Roles)

| Agent | Role | Specialty | Model |
|-------|------|-----------|-------|
| **Researcher** | Web search, content fetching, competitive analysis | Deep research | DeepSeek R1 ✓ |
| **Coder** | Python, SQL, scripting, automation pipelines | Code generation | Qwen2.5 Coder ✓ |
| **Writer** | Copy, docs, proposals, content drafting | Words that sound human | Planned |
| **Analyst** | Data processing, spreadsheets, reporting | Numbers & insights | Planned |
| **Scheduler** | Calendar, reminders, cron jobs | Time & deadlines | Planned |

---

## Part 2: Dashboard Features

### Implemented
- ✅ Jarvis status with live uptime
- ✅ Agent grid (Researcher, Coder active)
- ✅ Task queue / Mission Log
- ✅ System health indicators
- ✅ Quick Actions buttons
- ✅ Future Actions log (add/remove tasks)
- ✅ Real-time polling from status server

### In Progress
- 🔄 Real-time updates via polling

### Planned
- ⏳ Mobile PWA installation
- ⏳ Cloudflare tunnel for remote access

---

## Part 3: Browser Control Options

### Option 1: Chrome Extension Relay (RECOMMENDED)
- **What:** Install OpenClaw browser extension on Chrome
- **Setup:** Add extension to Chrome → Click toolbar icon to attach tab
- **Pros:** Easiest setup, works immediately
- **Cons:** Requires browser to stay open

### Option 2: Install Chromium in Docker
- **What:** Add Chromium to container via Dockerfile
- **Setup:** Modify Docker config, rebuild container
- **Pros:** Full browser automation in container
- **Cons:** Requires Docker changes, more resources

### Option 3: Browser on Host
- **What:** Connect to browser on Windows host
- **Setup:** Configure Docker to share browser process
- **Pros:** Powerful, full access
- **Cons:** Complex setup

**Chosen Path:** Option 1 (Chrome Extension Relay) - Start here

---

## Part 4: Implementation Phases

### Phase 1: Foundation ✅
- [x] Define sub-agent prompts/roles
- [x] Set up memory structure for agent tracking
- [x] Create basic status reporting
- [x] Test sub-agent spawning

### Phase 2: Dashboard v1 ✅
- [x] Build HTML/CSS dashboard
- [x] Add Jarvis status card
- [x] Add agent grid with status
- [x] Add task queue view
- [x] Deploy to GitHub Pages

### Phase 3: Real-Time Features 🔄
- [x] Status server for polling
- [x] Dashboard polls every 5 seconds
- [ ] Add browser control (see options above)

### Phase 4: Polish
- [ ] UI refinements
- [ ] Mobile PWA
- [ ] Cloudflare tunnel

---

## Budget Management

- **$20/month** allocation
- Track per-request cost
- Alert when below $5 remaining
- Default to efficient models for simple tasks

---

## Rules (From Aaron)

1. ✅ Document everything in memory folders
2. ✅ Review workspace folders for context
3. ✅ Ask permission before large/critical tasks
4. ✅ Never spend real money without asking
5. ✅ Ask before deleting unrecoverable files
6. ✅ Keep Future Actions updated on dashboard

---

## Repositories Created

| Repo | Purpose | URL |
|------|---------|-----|
| jarvis-command-center | Main dashboard and project | github.com/aaronmaziarz/jarvis-command-center |
| jarvis-journal | Daily journal entries | github.com/aaronmaziarz/jarvis-journal |
| jarvis-exchange | File exchange | github.com/aaronmaziarz/jarvis-exchange |

## Sub-Agents Active

| Agent | Model | Status |
|-------|-------|--------|
| Researcher 🤡 | DeepSeek R1 | ✅ Active |
| Coder 💻 | Qwen2.5 Coder 32B | ✅ Active |
| Frontend Dev 🎨 | Claude Sonnet 4 | ✅ Active |
| Writer ✍️ | MiniMax M2.5 | ✅ Active |
| Analyst 📊 | Qwen Plus | ✅ Active |
| Scheduler ⏰ | MiniMax M2.5 | ✅ Active |

## Daily Schedule

- **7:30 AM Arizona** - Morning brief (cron job set up)

## Current Security Status

### Audit Results (2026-03-10)
**Status:** ✅ Minor issues found

| Severity | Count |
|----------|-------|
| Critical | 0 |
| Warning | 2 |
| Info | 1 |

### Findings:
1. ⚠️ **No auth rate limiting** - gateway.bind is not loopback, no rate limit configured
2. ⚠️ **Ineffective denyCommands** - Some command entries don't work as expected
3. ℹ️ **Attack surface** - Browser control enabled, personal assistant trust model

### Recommendations:
- Add rate limiting to gateway.auth.rateLimit
- Review and fix denyCommands entries
- Consider restricting gateway.bind to localhost if not needed remotely

### Security Agent 🛡️
- Active with DeepSeek R1
- Can run: "Run security audit", "Check firewall", "Review system security"

---

## Current Future Actions

1. Complete web browser setup (Chrome extension relay)
2. Set up Cloudflare tunnel for remote dashboard access

## Latest Update (2026-03-10)

### Dashboard Overhaul Complete ✅
- Frontend Dev agent (Claude Sonnet 4) completed overhaul
- Apple 2080 aesthetic: Outfit font, enhanced glassmorphism, smooth animations
- Hero status banner, mobile-first responsive, micro-interactions
- Live at: https://aaronmaziarz.github.io/jarvis-command-center/dashboard.html

### Cron Jobs Active
- Morning Brief: 7:30 AM daily
- Dashboard Sync: Every 2 hours (8AM-8PM)

---

*This document lives in `memory/command-center-plan.md` and gets updated as we progress.*
