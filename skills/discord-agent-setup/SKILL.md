---
name: discord-agent-setup
description: Guides through Discord bot setup, channel creation, and agent binding for multi-agent routing. Use when: (1) setting up Discord as a new channel, (2) creating dedicated channels for each specialist agent, (3) configuring openclaw agents bind for channel-to-agent routing.
---

# Discord Agent Setup

Step-by-step guide for configuring Discord with OpenClaw multi-agent routing.

## Prerequisites

1. Discord Developer Portal access
2. Bot token from BotFather
3. OpenClaw gateway running

## Step 1: Create Discord Bot

1. Go to https://discord.com/developers/applications
2. Create new application
3. Go to Bot section → Create Bot
4. Copy the bot token
5. Enable Message Content Intent in Bot settings

## Step 2: Add Bot to Server

1. Generate invite URL with permissions:
   - Send Messages
   - Read Message History
   - Manage Channels (for auto-creation)
2. Invite the bot to your server

## Step 3: Configure OpenClaw

```bash
openclaw channels login --channel discord --token YOUR_BOT_TOKEN
```

## Step 4: Create Channel Structure

Recommended channels:
- #brain - Main orchestrator
- #engineering - senior-dev, backend, frontend-dev
- #research - researcher
- #docs - docs-writer
- #automation - scripting, cron-reporter
- #general - Catch-all

## Step 5: Bind Agents to Channels

```bash
openclaw agents bind --agent brain --bind discord:brain
openclaw agents bind --agent researcher --bind discord:research
openclaw agents bind --agent senior-dev --bind discord:engineering
# etc.
```

## Verification

```bash
openclaw agents bindings
openclaw channels status --probe
```
