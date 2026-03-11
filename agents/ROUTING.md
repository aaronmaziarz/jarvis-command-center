# Agent Routing Guide

## Overview
All user requests flow through the Brain, which decides:
- Answer directly (simple questions)
- Delegate to domain lead (complex tasks)
- Delegate to specialist (specific work)

## Routing Decision Tree

```
User Request → Brain
     │
     ├─ Simple? → Yes → Answer directly
     │
     └─ Complex?
           │
           ├─ Research → Researcher
           ├─ Engineering → Senior-Dev → Specialist
           └─ Other → Project Manager
```

## Task Type Routing

| Task | Route To |
|------|----------|
| Greeting, status | Brain (direct) |
| Code, build, debug | senior-dev → specialist |
| Research, find | researcher |
| Project tracking | project-manager |
| Documentation | docs-writer |

## Agent Tiers

- **Tier 1 (Brain)**: Executive - orchestrator
- **Tier 2 (Leads)**: senior-dev, researcher, project-manager  
- **Tier 3 (Specialists)**: frontend-dev, backend, qa-test, etc.

## Failure Handling

1. Specialist fails → domain lead
2. Lead fails → brain
3. Brain attempts direct answer
