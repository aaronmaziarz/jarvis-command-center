---
name: dashboard-action-wiring
description: Connects dashboard controls (spawn buttons, model selectors) to real OpenClaw agent spawning. Use when: (1) wiring dashboard spawn buttons to sessions_spawn, (2) connecting model selector to actual model selection, (3) validating end-to-end dashboard functionality.
---

# Dashboard Action Wiring

Connect dashboard UI to actual OpenClaw functionality.

## Current Dashboard State

- Spawn buttons exist but may not trigger real agents
- Model selector shows options but may not apply
- Agent cards show static data, not real-time status

## Wiring Checklist

### 1. Agent Spawning

```javascript
// In dashboard.html, wire button to:
await fetch('/api/spawn', {
  method: 'POST',
  body: JSON.stringify({ 
    agentId: 'researcher',
    task: userTask 
  })
})
```

### 2. Status Polling

Ensure `/status.json` updates reflect actual agent state:
- Query active sessions
- Update status.json periodically
- Dashboard polls status.json

### 3. Model Selection

Pass selected model to spawn:
```javascript
model: document.getElementById('model-select').value
```

### 4. Test End-to-End

1. Click spawn button
2. Verify agent spawned: `openclaw sessions list`
3. Check status.json updated
4. Verify dashboard reflects new state

## Files to Modify

- `/workspace/dashboard.html` - UI wiring
- `/workspace/status.json` - status generation
- Cron job for status updates

## Validation

After wiring, test:
1. Spawn an agent from dashboard
2. Verify it appears in `openclaw sessions list`
3. Check dashboard updates within poll interval
4. Confirm completion status returns correctly
