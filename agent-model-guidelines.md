# 🤖 Jarvis Agent Model Guidelines

*Created: 2026-03-10*
*Purpose: When to use which model/agent*

---

## Model Tiers

### 🟢 Fast & Efficient (Default)
| Model | Use For | Cost |
|-------|---------|------|
| MiniMax M2.5 | Simple tasks, scheduling, writing | ~$0.20/1M |
| Qwen Plus | Data analysis, medium complexity | ~$0.40/1M |

### 🟡 High Quality
| Model | Use For | Cost |
|-------|---------|------|
| Claude Sonnet 4 | UI/UX, complex frontend, planning | ~$3/1M |
| GPT-4o | General high-quality tasks | ~$2.5/1M |

### 🔴 Premium (Use Sparingly)
| Model | Use For | Cost |
|-------|---------|------|
| **GPT-5.4 Pro** | Deep planning, complex architecture, breakthrough ideas | ~$10/1M |
| Claude Opus 4.6 | Deep reasoning, complex analysis | ~$15/1M |

---

## When to Use What

### Use Default Models (MiniMax, Qwen):
- ✅ Simple Q&A
- ✅ Routine tasks
- ✅ Scheduling
- ✅ Basic writing
- ✅ Status checks

### Use High Quality (Claude Sonnet, GPT-4o):
- ✅ Complex coding
- ✅ UI/UX work
- ✅ Analysis
- ✅ Documents

### Use Premium (GPT-5.4 Pro, Opus):
- ✅ **Major project planning** (like Chronos)
- ✅ Complex architecture decisions
- ✅ Strategic decisions
- ✅ When you need the best output
- ❌ NOT for simple tasks

---

## Agent Specializations

| Agent | Model | Best For |
|-------|-------|----------|
| 🤡 Researcher | DeepSeek R1 | Web research, info gathering |
| 💻 Coder | Qwen2.5 Coder | Python, SQL, scripts |
| 🎨 Frontend Dev | Claude Sonnet 4.6 | UI/UX, dashboard design |
| 🛡️ Security | DeepSeek R1 | Audits, hardening |
| ✍️ Writer | MiniMax M2.5 | Copy, docs |
| 📊 Analyst | Qwen Plus | Data, reports |
| ⏰ Scheduler | MiniMax M2.5 | Reminders, calendar |
| 🗂️ Organization | MiniMax M2.5 | File management |

---

## Budget Rules

- **Monthly Budget:** $20
- **Premium models:** Use only when value justifies cost
- **Default to efficient:** Unless quality is critical

**Example:**
- Simple status check: MiniMax ($0.001)
- Chronos planning: GPT-5.4 Pro ($0.50)
- Dashboard UI: Claude Sonnet ($0.10)

---

## How to Spawn with Specific Model

```javascript
// GPT-5.4 Pro for planning
sessions_spawn({
  model: "openrouter/openai/gpt-5.4-pro",
  task: "Plan the Chronos architecture...",
  mode: "run"
})

// Claude Sonnet for UI
sessions_spawn({
  model: "openrouter/anthropic/claude-sonnet-4-20250514", 
  task: "Design the dashboard UI...",
  mode: "run"
})
```

---

*This lives in jarvis-exchange/agent-model-guidelines.md*
