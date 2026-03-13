---
name: skill-scaffold
description: Creates new OpenClaw skills with proper structure, SKILL.md, and documentation. Use when: (1) building a new skill from scratch, (2) following OpenClaw skill conventions, (3) packaging skills for distribution.
---

# Skill Scaffold

Template for creating new OpenClaw skills.

## Skill Structure

```
skill-name/
├── SKILL.md (required)
├── scripts/ (optional)
├── references/ (optional)
└── assets/ (optional)
```

## SKILL.md Format

```markdown
---
name: skill-name
description: Clear description of what the skill does and when to use it
---

# Skill Name

## Purpose
What this skill accomplishes

## Usage
How to invoke the skill

## Examples
Example invocations

## Notes
Any additional context
```

## Required Fields

- `name`: lowercase, hyphens only
- `description`: When to use, what it does

## Creation Steps

1. Create skill directory:
```bash
mkdir -p /workspace/skills/my-skill
```

2. Create SKILL.md with frontmatter

3. Add optional resources:
```bash
mkdir -p my-skill/scripts
mkdir -p my-skill/references
mkdir -p my-skill/assets
```

4. Test the skill by invoking it

## Skill Naming Conventions

- Lowercase only
- Hyphens for spaces: `my-awesome-skill`
- Max 64 characters
- Verb-led names preferred: `code-review`, `deploy-app`

## Description Best Practices

Include:
- What the skill does
- When to use it
- Specific triggers/contexts

Example:
```
description: Creates and manages cron jobs for scheduled tasks. Use when: 
(1) setting up periodic automation, (2) modifying existing schedules, 
(3) debugging cron issues.
```

## Validation

After creation, verify:
1. SKILL.md has valid frontmatter
2. Name matches directory
3. Description is clear and complete
4. Skill loads: `openclaw status` should list it
