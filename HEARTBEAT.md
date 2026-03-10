# HEARTBEAT.md

# Keep this file empty (or with only comments) to skip heartbeat API calls.

# Add tasks below when you want the agent to check something periodically.

---

## Daily Morning Brief (7:30 AM Arizona - Cron Job)

The morning brief runs automatically via cron job. Each morning, check:

1. **Weather in Arizona** - Use weather skill
2. **Calendar** - Check upcoming events (if available)
3. **Email** - Check for urgent items (if available)
4. **Dashboard Status** - Read Future Actions from memory/command-center-plan.md
5. **Jarvis Status** - Current state, active agents, budget remaining

### Morning Brief Template

```
☀️ Good Morning, Aaron!

Here's your daily briefing:

🌤️ Arizona Weather: [current conditions]
📅 Upcoming: [next few events]
📧 Urgent: [any important emails]
🤖 Jarvis Status: [online/agents active]
💰 Budget: [$X.XX remaining]
📋 Today's Focus: [top 3 priorities from Future Actions]
```

---

## Dashboard Sync (Every 2 Hours, 8AM-8PM Arizona)

The sync runs every 2 hours via cron job. Each sync:

1. **Read current status** from:
   - memory/command-center-plan.md (Future Actions, project status)
   - memory/agent-states.json (agent activity)
   - memory/YYYY-MM-DD.md (daily tasks completed)

2. **Compile summary**:
   - Current project goals
   - Tasks in progress
   - Completed tasks today
   - Agent status (idle/working)
   - Budget remaining
   - Any blockers

3. **Update memory**:
   - Update memory/command-center-plan.md with latest status
   - Add completed tasks to daily log

4. **Deliver sync report** to Telegram

### Sync Report Template

```
🔄 Dashboard Sync

🤖 Agents: [X active, Y idle]
💰 Budget: $[remaining]
📋 Tasks:
  - In Progress: [list]
  - Completed: [list]
  - Pending: [list]
⚠️ Blockers: [if any]
```

