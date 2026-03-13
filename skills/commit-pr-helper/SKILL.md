---
name: commit-pr-helper
description: Git workflow helper for reviewing changes, creating commits with good messages, pushing, and optionally creating PRs. Use when: (1) user wants to commit changes, (2) standardizing commit messages across the project, (3) full commit-push-PR workflow.
---

# Commit PR Helper

Streamline git workflows with structured commits.

## Workflow Options

### Option 1: Commit Only

```bash
# Review changes
git status
git diff

# Stage
git add -A

# Commit with message
git commit -m "Descriptive message"
```

### Option 2: Commit + Push

```bash
git add -A
git commit -m "Message"
git push origin main
```

### Option 3: Full PR Workflow

```bash
# Create branch if needed
git checkout -b feature/description

# Commit changes
git add -A
git commit -m "feat: Add new feature"

# Push and create PR
git push -u origin feature/description
gh pr create --fill
```

## Commit Message Best Practices

Format: `<type>: <description>`

Types:
- feat: New feature
- fix: Bug fix
- docs: Documentation
- style: Formatting
- refactor: Code restructuring
- test: Adding tests
- chore: Maintenance

Examples:
```
feat: Add user authentication
fix: Resolve login redirect issue
docs: Update API documentation
refactor: Simplify user service
```

## Pre-commit Checklist

- [ ] Tests pass
- [ ] No debug code
- [ ] No secrets committed
- [ ] Code follows project style

## PR Description Template

```
## What
Brief description of changes

## Why
Context and motivation

## How
Implementation approach

## Testing
How to verify the changes
```
