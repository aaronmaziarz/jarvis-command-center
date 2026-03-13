---
name: agent-state-sync
description: Ensures all configured agents are consistently represented across manifest, runtime state, dashboard status, and reporting. Use when: (1) fixing mismatch between defined agents and visible agents, (2) adding new agents to all tracking systems, (3) auditing agent coverage.
---

# Agent State Sync

Maintain consistency across all agent state sources.

## Agent Data Sources

1. **Manifest**: `agents/manifest.json` - defines all agents
2. **Runtime State**: `memory/agent-states.json` - current status
3. **Dashboard**: `status.json` - UI display
4. **OpenClaw Config**: `openclaw.json` - registered agents

## Sync Process

### 1. Read Manifest

```bash
cat agents/manifest.json | jq 'keys'
```

### 2. Read Runtime State

```bash
cat memory/agent-states.json | jq 'keys'
```

### 3. Compare and Identify Gaps

- Which agents are in manifest but not in runtime state?
- Which are in runtime but not dashboard?
- Which are in OpenClaw but not manifest?

### 4. Add Missing Entries

For each missing agent, add to each data source with:
- status: "idle"
- tasks_completed: 0
- tasks_failed: 0
- current_task: null

### 5. Verify All Sources Match

All should contain the same agent IDs.

## Common Issues

- Frontend Dev and Security missing from runtime tracking
- Dashboard shows only 5 agents instead of 12
- OpenClaw registered but not in manifest

## Verification Command

```bash
# Should show all 12+ agents
openclaw agents list
```
