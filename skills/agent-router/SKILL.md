---
name: agent-router
description: Routes incoming tasks to the appropriate specialized sub-agent based on task analysis. Use when: (1) user asks for research, coding, documentation, or automation tasks, (2) tasks would be better handled by a specialist agent like researcher, senior-dev, backend, frontend-dev, docs-writer, scripting, or qa-test, (3) you need to coordinate multiple specialist agents for complex workflows.
---

# Agent Router

Analyzes incoming tasks and delegates to the most appropriate registered OpenClaw agent.

## Available Agents

| Agent ID | Model | Specialty |
|----------|-------|-----------|
| brain | MiniMax M2.5 | Executive orchestration |
| senior-dev | Claude Sonnet 4 | Engineering lead, architecture |
| researcher | DeepSeek R1 | Web research, information gathering |
| project-manager | MiniMax M2.5 | Task tracking, project coordination |
| frontend-dev | Claude Sonnet 4 | UI/UX, dashboard, web interfaces |
| backend | Qwen Coder | APIs, databases, server-side |
| qa-test | Qwen Plus | Testing, quality assurance |
| scripting | Qwen Coder | Automation, scripts, pipelines |
| docs-writer | MiniMax M2.5 | Documentation, content creation |
| daily-brief | MiniMax M2.5 | Summaries, daily reports |
| cron-reporter | MiniMax M2.5 | Automation logging |
| discord-ops | MiniMax M2.5 | Discord management |

## Routing Logic

1. **Research tasks** → `researcher`
   - Web searches, information gathering, competitive analysis
2. **Coding tasks** → Determine scope:
   - Large/architectural → `senior-dev`
   - Frontend/UI → `frontend-dev`
   - Backend/API → `backend`
   - Scripts/automation → `scripting`
3. **Documentation** → `docs-writer`
4. **Testing** → `qa-test`
5. **Project management** → `project-manager`
6. **Daily summaries** → `daily-brief`
7. **Discord ops** → `discord-ops`
8. **Complex multi-agent** → Coordinate via `sessions_spawn`

## Usage

When a task matches a specialist, use `sessions_spawn` with the appropriate `agentId`. After the subagent completes, synthesize the results and present to the user.

## Example

User: "Research the latest OpenClaw features"

1. Identify as research task → spawn `researcher`
2. Researcher returns findings
3. Synthesize and present to user
