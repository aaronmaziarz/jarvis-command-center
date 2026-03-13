---
name: browser-relay-setup
description: Guided setup for Chrome Extension Relay browser automation. Use when: (1) configuring browser automation for the first time, (2) attaching existing Chrome tabs for relay control, (3) troubleshooting browser automation issues.
---

# Browser Relay Setup

Configure Chrome Extension Relay for browser automation.

## Prerequisites

- Chrome browser installed
- OpenClaw browser relay extension

## Step 1: Install Extension

1. Download from Chrome Web Store (search "OpenClaw Browser Relay")
2. Or sideload: openclaw browser install

## Step 2: Enable Extension

1. Open Chrome → Extensions (chrome://extensions/)
2. Enable OpenClaw Browser Relay
3. Enable "Developer mode" if needed

## Step 3: Attach Tab

1. Navigate to the page you want to control
2. Click the OpenClaw extension icon in toolbar
3. Badge should show "ON" when attached

## Step 4: Verify Connection

```bash
openclaw browser status
# Should show attached tabs
```

## Usage

```python
# Attach to existing tab
browser(action="snapshot", profile="chrome")
```

## Troubleshooting

- Badge shows "OFF": Click to attach
- Tab not found: Navigate in Chrome first
- Permission denied: Check extension permissions

## Alternative: Headless

For server environments, use:
```bash
openclaw browser start --profile openclaw
```
