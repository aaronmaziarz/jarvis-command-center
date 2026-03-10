# HEARTBEAT.md

# Keep this file empty (or with only comments) to skip heartbeat API calls.

# Add tasks below when you want the agent to check something periodically.

---

## Daily Morning Brief (7:30 AM Arizona - Cron Job)

The morning brief runs automatically via cron job. Each morning, check:

1. **Weather in Arizona** - Use weather skill
2. **Calendar** - Check upcoming events (if available)
3. **Email** - Check for urgent items (if available)
4. **Dashboard Status** - Read Future Actions from dashboard
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

