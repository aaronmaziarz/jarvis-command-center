# 🤖 Jarvis Command Center - Master Plan

*Created: 2026-03-09*
*Owner: Aaron Maziarz*
*Status: Planning*

---

## Vision

Transform Jarvis into an AI operations hub that:
1. **Manages a team of specialized sub-agents** for parallel task execution
2. **Provides a real-time dashboard** for full system visibility and control
3. **Operates autonomously** within defined boundaries while keeping Aaron in the loop

---

## Part 1: Agent Team Architecture

### The Squad (Sub-Agent Roles)

| Agent | Role | Specialty |
|-------|------|-----------|
| **Researcher** | Web search, content fetching, competitive analysis | Info gathering at speed |
| **Coder** | Python, SQL, scripting, automation pipelines | Building & debugging |
| **Writer** | Copy, docs, proposals, content drafting | Words that sound human |
| **Analyst** | Data processing, spreadsheets, reporting | Numbers & insights |
| **Scheduler** | Calendar, reminders, cron jobs | Time & deadlines |

### How It Works

- **Me (Jarvis)** = The manager/brain
  - I receive your request
  - I delegate to the right sub-agent(s)
  - I synthesize results and present to you
  - I track progress across all agents

- **Sub-agents** = The workers
  - Spawned on-demand for specific tasks
  - Each has a clear role and context
  - Report back to me with results

- **You** = The CEO
  - Give high-level commands
  - Approve big moves
  - Override anytime

---

## Part 2: Dashboard Design

### UI/UX Principles
- **Dark mode** (tech aesthetic, easy on eyes)
- **Card-based layout** (modular, scannable)
- **Status colors**: Green = good, Yellow = working, Red = blocked
- **Real-time updates** (auto-refresh, no manual reload)
- **Mobile-first** (works on phone, great on desktop)

### Dashboard Sections

#### 1. 🧠 Jarvis Status (Brain)
- Current mood/state
- Active context (what project/task I'm on)
- Memory usage indicator
- Model currently in use

#### 2. 👥 Agent Team Grid
- Each agent as a card:
  - Name + role icon
  - Status: idle / working / waiting / error
  - Current task (if any)
  - Tasks completed today
  - Time spent this session

#### 3. 📋 Task Queue
- Pending tasks (what you asked for)
- In-progress tasks
- Completed tasks (with timestamps)
- Failed tasks (with error summary)

#### 4. 🎯 Current Project
- Active project name
- Goals breakdown
- Next steps
- Blockers (if any)

#### 5. 📊 System Stats
- OpenRouter budget remaining
- API calls this session
- Active sub-agents count
- Uptime

#### 6. ⚡ Quick Actions
- Buttons for common ops:
  - Spawn agent
  - Check memory
  - Run health check
  - Pull latest

---

## Part 3: Implementation Phases

### Phase 1: Foundation (Week 1)
- [ ] Define sub-agent prompts/roles
- [ ] Set up memory structure for agent tracking
- [ ] Create basic status reporting (text-based)
- [ ] Test sub-agent spawning

### Phase 2: Dashboard v1 (Week 2)
- [ ] Build HTML/CSS dashboard
- [ ] Add Jarvis status card
- [ ] Add agent grid with basic status
- [ ] Add task queue view
- [ ] Deploy to canvas

### Phase 3: Real-Time Features (Week 3)
- [ ] WebSocket or polling for live updates
- [ ] Agent activity logging
- [ ] Budget tracking
- [ ] Task history persistence

### Phase 4: Polish (Week 4)
- [ ] UI refinements (animations, hover states)
- [ ] Mobile optimization
- [ ] Add quick action buttons
- [ ] Error handling & edge cases

---

## Budget Management

- **$20/month** allocation
- Track per-request cost
- Alert when below $5 remaining
- Default to efficient models for simple tasks
- Ask before using premium models

---

## Rules (From Aaron)

1. ✅ Document everything in memory folders
2. ✅ Review workspace folders for context
3. ✅ Ask permission before large/critical tasks
4. ✅ Never spend real money without asking
5. ✅ Ask before deleting unrecoverable files

---

## Next Steps

1. **Approve this plan** (or suggest changes)
2. **Decide which sub-agents to prioritize first**
3. **Pick dashboard features for v1**
4. Let's build 🔧

---

*This document lives in `memory/command-center-plan.md` and gets updated as we progress.*