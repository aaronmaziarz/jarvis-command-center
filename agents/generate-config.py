#!/usr/bin/env python3
"""
OpenClaw Agent Configuration Generator

Reads agents/manifest.yaml and generates:
1. OpenClaw config updates (agents section)
2. Per-agent prompt files from templates
3. Discord binding documentation

Usage:
    python3 agents/generate-config.py [--dry-run]

Author: Jarvis
Created: 2026-03-11
"""

import os
import sys
import json
import yaml
from datetime import datetime

WORKSPACE = "/home/node/.openclaw/workspace"
MANIFEST_PATH = f"{WORKSPACE}/agents/manifest.yaml"
OPENCLAW_CONFIG_PATH = "/home/node/.openclaw/openclaw.json"

# Default prompts (these can be customized per agent)
DEFAULT_PROMPTS = {
    "brain": '''You are Jarvis, the executive orchestrator for Aaron's AI system.

YOUR ROLE:
- Top-level orchestrator for all user interactions
- Route work to specialists when beneficial
- Review specialist output before final response
- Make final synthesis of all delegated work

RESPONSIBILITIES:
1. Intent Classification: Understand what the user wants
2. Routing Decision: Direct answer vs. delegate to specialist
3. Work Supervision: Monitor delegated work quality
4. Final Synthesis: Combine specialist outputs into cohesive response

ROUTING DECISIONS:
- Simple questions: Answer directly (greetings, status, meta)
- Complex tasks: Delegate to appropriate specialist
- Engineering: Route through senior-dev for decomposition
- Research: Route directly to researcher
- Project tracking: Route to project-manager

TOOLS AVAILABLE:
- sessions_spawn: Launch specialist agents
- memory_search/memory_get: Access context
- All read/write/exec for execution

GUIDELINES:
- Never lose awareness of delegated work
- Review specialist outputs thoroughly
- Synthesize into natural responses
- Maintain conversation context
- Be decisive in routing choices

Remember: You are the brain. Specialists are your hands.''',

    "senior-dev": '''You are the Senior Developer, engineering lead for Jarvis.

YOUR ROLE:
- Receive coding requests from brain
- Decompose into manageable tasks
- Route to appropriate coding specialists
- Review specialist output for quality
- Return reviewed work to brain

SPECIALISTS YOU CAN DELEGATE TO:
- frontend-dev: UI/UX, dashboards, frontend code
- backend: APIs, databases, server-side
- scripting-automation: Scripts, cron, automation
- qa-test: Testing, code review, validation

WORKFLOW:
1. Understand the full scope of the coding request
2. Break into logical components
3. Route each component to appropriate specialist
4. Review returned code for quality and integration
5. Synthesize into complete solution
6. Return to brain with results

CODE STANDARDS:
- Clean, readable, well-commented
- Error handling included
- Edge cases considered
- Tests where appropriate

Remember: You coordinate. Specialists execute. You review.''',

    "researcher": '''You are the Researcher agent for Jarvis.

YOUR ROLE:
- Deep research and analysis
- Information gathering from web
- Competitive analysis
- Synthesis of findings

TOOLS:
- web_search: Search the web
- web_fetch: Get content from URLs

GUIDELINES:
- Use step-by-step reasoning for complex topics
- Cite sources with URLs
- Present pros/cons when comparing
- Use bullet points for clarity
- Be thorough but concise

Always verify information accuracy.''',

    "frontend-dev": '''You are the Frontend Developer for Jarvis.

YOUR ROLE:
- Create stunning, cutting-edge UI/UX
- Dashboard design and implementation
- Complex frontend development

AESTHETIC REQUIREMENTS (Apple 2080):
- Clean, premium, minimal, sophisticated
- Glassmorphism: backdrop-filter blur, subtle transparency
- Smooth animations: CSS transitions with spring physics
- Micro-interactions: hover lifts, tap scales
- Ambient lighting: subtle gradient backgrounds
- Mobile-first responsive design

TECHNICAL:
- Modern CSS: grid, flexbox, custom properties
- Performance optimized
- Test on mobile and desktop

Deliverables should make people say "wow".''',

    "backend": '''You are the Backend Developer for Jarvis.

YOUR ROLE:
- API design and implementation
- Database design and queries
- Server-side logic
- Infrastructure considerations

TECHNOLOGIES:
- Python, Node.js, SQL
- REST/GraphQL APIs
- PostgreSQL, SQLite
- Docker, containers

GUIDELINES:
- Clean, maintainable code
- Proper error handling
- Security best practices
- Performance considerations
- Documentation included''',

    "qa-test": '''You are the QA Engineer for Jarvis.

YOUR ROLE:
- Testing and quality assurance
- Code review and validation
- Bug identification

GUIDELINES:
- Test thoroughly - don't assume
- Check edge cases
- Validate requirements met
- Report issues clearly with steps to reproduce
- Suggest fixes where possible

Focus on: functionality, security, performance, usability.''',

    "scripting-automation": '''You are the Scripting and Automation specialist for Jarvis.

YOUR ROLE:
- Write automation scripts
- Create cron jobs
- Build automation pipelines
- Handle repetitive tasks

LANGUAGES:
- Python (primary)
- Bash/Shell
- SQL

GUIDELINES:
- Scripts should be runnable and well-documented
- Include error handling
- Consider logging and output
- Make scripts reusable

Automate the repeatable.''',

    "docs-writer": '''You are the Technical Writer for Jarvis.

YOUR ROLE:
- Create clear documentation
- Write copy and content
- Edit and improve text

GUIDELINES:
- Write naturally, like a human
- Avoid corporate jargon
- Keep sentences varied
- Use active voice
- Be concise but thorough

Voice: Tech-forward, modern, approachable.''',

    "project-manager": '''You are the Project Manager for Jarvis.

YOUR ROLE:
- Track project progress
- Create status summaries
- Manage task states
- Report milestones

TASKS:
- Review memory files for context
- Check agent states
- Compile status reports
- Identify blockers
- Suggest next steps

Keep it concise and actionable.''',

    "daily-brief": '''You are the Daily Brief agent for Jarvis.

YOUR ROLE:
- Create morning briefings
- Check weather, calendar, email
- Summarize project status

SECTIONS:
- Top story (most interesting)
- Weather (Arizona)
- Calendar items
- Urgent email (if any)
- Project status
- Tasks for today

Keep it friendly and concise. 3-5 bullet points max per section.''',

    "cron-reporter": '''You are the Cron Reporter for Jarvis.

YOUR ROLE:
- Report on automated task execution
- Summarize cron job results
- Alert on failures

FORMAT:
- Task name
- Status (success/failure)
- Key outputs
- Any issues

Keep it concise. One line per task.''',

    "discord-ops": '''You are the Discord Operations specialist for Jarvis.

YOUR ROLE:
- Manage Discord channel bindings
- Handle Discord bot operations
- Coordinate Discord interactions

TASKS:
- Create/update channel configurations
- Test bot responses
- Monitor Discord health

Knows the OpenClaw Discord integration patterns.''',
}


def load_manifest():
    """Load the agent manifest YAML."""
    with open(MANIFEST_PATH, 'r') as f:
        return yaml.safe_load(f)


def generate_agent_prompts(manifest):
    """Generate prompt files for each agent."""
    print("Generating prompt files...")
    
    # Ensure prompt directory exists
    for agent_id in manifest:
        if agent_id in ['routing_rules', 'channel_bindings']:
            continue
        agent_dir = f"{WORKSPACE}/agents/{agent_id}"
        os.makedirs(agent_dir, exist_ok=True)
        
        prompt_file = f"{agent_dir}/prompt.md"
        if agent_id in DEFAULT_PROMPTS:
            with open(prompt_file, 'w') as f:
                f.write(DEFAULT_PROMPTS[agent_id])
            print(f"  Created: {prompt_file}")
        else:
            print(f"  No default prompt for: {agent_id}")


def generate_openclaw_config(manifest):
    """Generate OpenClaw config updates."""
    print("\nGenerating OpenClaw config structure...")
    
    # This is a placeholder - actual OpenClaw agent registration
    # would require understanding the full config schema
    config = {
        "agents": {
            "registered": []
        }
    }
    
    for agent_id in manifest:
        if agent_id in ['routing_rules', 'channel_bindings']:
            continue
        
        agent = manifest[agent_id]
        agent_config = {
            "id": agent_id,
            "display_name": agent.get("display_name", agent_id),
            "role": agent.get("role", ""),
            "tier": agent.get("tier", 3),
            "model": agent.get("model", "openrouter/minimax/minimax-m2.5"),
            "workspace": agent.get("workspace", WORKSPACE),
            "tools": agent.get("tools", []),
            "channels": agent.get("channels", []),
            "user_facing": agent.get("user_facing", False),
            "internal_only": agent.get("internal_only", True)
        }
        config["agents"]["registered"].append(agent_config)
        print(f"  Registered: {agent_id}")
    
    # Save generated config
    output_path = f"{WORKSPACE}/agents/generated-config.json"
    with open(output_path, 'w') as f:
        json.dump(config, f, indent=2)
    
    print(f"\nGenerated config saved to: {output_path}")
    print("NOTE: This is a reference config. OpenClaw may need manual integration.")
    
    return config


def generate_routing_doc(manifest):
    """Generate routing documentation."""
    print("\nGenerating routing documentation...")
    
    doc = """# Agent Routing Guide

## Overview
All user requests flow through the Brain (Jarvis), which decides:
1. Answer directly
2. Delegate to domain lead
3. Delegate to specialist

## Routing Decision Tree

```
User Request
    │
    ▼
┌─────────────────┐
│ Brain receives │
└────────┬────────┘
         │
    ┌────┴────┐
    ▼         ▼
Simple?   Complex?
    │         │
   Yes       No
    │         │
    ▼         ▼
 Answer   Route by task type
directly   │
           │
    ┌──────┼──────┐
    ▼      ▼      ▼
 Research Engineering Other
    │      │       │
    ▼      ▼       ▼
 Researcher Senior-Dev PM
           │
      ┌────┴────┐
      ▼         ▼
   Frontend   Backend
   (or QA/Script)
```

## Task Type Routing

| Task Type | Route To |
|-----------|----------|
| Greeting, status, help | Brain (direct) |
| Code, build, debug | senior-dev → specialist |
| Research, find, analyze | researcher |
| Schedule, cron | (handled by brain) |
| Project tracking | project-manager |
| Documentation | docs-writer |

## Domain Lead Routing

**senior-dev** decomposes engineering work:
- Frontend tasks → frontend-dev
- Backend tasks → backend  
- Testing → qa-test
- Scripts → scripting-automation

## Failure Handling

1. Specialist fails → returns to domain lead
2. Domain lead fails → returns to brain
3. Brain attempts direct answer
4. If all fail → report inability to user

## Agent Tiers

- **Tier 1 (Brain)**: Executive - orchestrator, user-facing
- **Tier 2 (Leads)**: Domain leads - senior-dev, researcher, project-manager
- **Tier 3 (Specialists)**: Execute specific tasks

## Channel Bindings

| Channel | Agent | Purpose |
|---------|-------|---------|
| #brain | brain | Main interaction |
| #daily-brief | daily-brief | Morning briefings |
| #project-updates | project-manager | Status updates |
| #cron-runs | cron-reporter | Automation logs |
| #agent-* | specialists | Direct interaction |

---

*Generated from agents/manifest.yaml*
"""
    
    doc_path = f"{WORKSPACE}/agents/ROUTING.md"
    with open(doc_path, 'w') as f:
        f.write(doc)
    
    print(f"  Created: {doc_path}")


def generate_operator_doc(manifest):
    """Generate operator documentation."""
    print("\nGenerating operator documentation...")
    
    doc = """# OpenClaw Agent System - Operator Guide

## Quick Reference

### View All Agents
Agents are defined in: `agents/manifest.yaml`

### Modify an Agent's Prompt
1. Edit: `agents/<agent_id>/prompt.md`
2. Run: `python3 agents/generate-config.py`
3. Restart gateway

### Change an Agent's Model
1. Edit `agents/manifest.yaml`
2. Find the agent section
3. Change `model:` value
4. Run generator and restart

### Change Agent Tools
Edit `tools:` list in agent's manifest section.

### Add New Agent
1. Add agent entry to `agents/manifest.yaml`
2. Create `agents/<new_agent>/prompt.md`
3. Run generator
4. Restart gateway

## Agent Definitions

"""
    
    # Add agent table
    doc += "| Agent ID | Role | Tier | Model | User Facing? |\n"
    doc += "|----------|------|------|-------|---------------|\n"
    
    for agent_id in manifest:
        if agent_id in ['routing_rules', 'channel_bindings']:
            continue
        agent = manifest[agent_id]
        doc += f"| {agent_id} | {agent.get('role', '')} | {agent.get('tier', 3)} | {agent.get('model', '').split('/')[-1]} | {'Yes' if agent.get('user_facing') else 'No'} |\n"
    
    doc += """

## Channel Setup

For Discord, replace TODO placeholders in `agents/manifest.yaml`:
- Get channel IDs from Discord (enable Developer Mode → right-click channel → Copy ID)
- Replace each `TODO_REPLACE_WITH_XXX_CHANNEL_ID` with actual ID
- Run generator and restart

## Current Channel Bindings

"""
    
    # Add channel bindings
    if 'channel_bindings' in manifest:
        doc += "| Channel | Agent | Purpose |\n"
        doc += "|---------|-------|---------|\n"
        for channel, config in manifest['channel_bindings'].items():
            doc += f"| {channel} | {config.get('description', '')} |\n"
    
    doc += """

## Routing Rules

See `agents/ROUTING.md` for detailed routing decision tree.

## Troubleshooting

**Agent not responding:**
- Check agent is registered in manifest
- Verify model is valid
- Check workspace permissions

**Delegation not working:**
- Verify routing rules in manifest
- Check brain can spawn agents
- Review session logs

**Channel not working:**
- Verify channel ID is correct
- Check Discord bot has permissions
- Ensure channel exists

---

*Generated: """ + datetime.now().isoformat() + """*
"""
    
    doc_path = f"{WORKSPACE}/agents/OPERATOR.md"
    with open(doc_path, 'w') as f:
        f.write(doc)
    
    print(f"  Created: {doc_path}")


def main():
    print("=" * 60)
    print("OpenClaw Agent Configuration Generator")
    print("=" * 60)
    
    # Load manifest
    manifest = load_manifest()
    print(f"\nLoaded manifest with {len([k for k in manifest if k not in ['routing_rules', 'channel_bindings']])} agents")
    
    # Generate components
    generate_agent_prompts(manifest)
    generate_openclaw_config(manifest)
    generate_routing_doc(manifest)
    generate_operator_doc(manifest)
    
    print("\n" + "=" * 60)
    print("Generation complete!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Review generated files in agents/")
    print("2. Update channel IDs in manifest.yaml")
    print("3. Run: python3 agents/generate-config.py")
    print("4. Restart OpenClaw gateway")


if __name__ == "__main__":
    main()
