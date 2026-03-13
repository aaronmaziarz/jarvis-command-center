---
name: openrouter-spend-audit
description: Validates OpenRouter API access, retrieves usage statistics, and compares against budget targets. Use when: (1) checking current spend against the $20/month budget, (2) verifying API key is valid and has access to usage endpoints, (3) updating dashboard with real spend data.
---

# OpenRouter Spend Audit

Monitor and track OpenRouter API spending.

## Budget Target

- Monthly limit: $20 USD
- Default model: MiniMax M2.5 (efficient)
- Premium models: Claude Sonnet 4, DeepSeek R1

## Step 1: Validate API Key

Check auth profiles:
```bash
cat ~/.openclaw/agents/main/agent/auth-profiles.json
```

Verify key format: `sk-or-v1-...`

## Step 2: Check Usage

OpenRouter provides usage via their API:
```
GET https://openrouter.ai/api/v1/auth
```

Or check via dashboard: https://openrouter.ai/accounts

## Step 3: Update Status

Write current status to memory:
- Total spent this billing cycle
- Days remaining
- Average daily spend
- Projection at current rate

## Step 4: Recommendations

If approaching budget:
- Switch to more efficient models
- Reduce session complexity
- Use shorter context windows

## Output Format

```
Budget Status:
- Spent: $X.XX / $20.00
- Days remaining: X
- Daily average: $X.XX
- Projection: $X.XX (X% of budget)
```
