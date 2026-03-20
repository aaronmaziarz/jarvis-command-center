---
name: chronos-dev
description: Development guide for Chronos — an AI-native task management platform positioned between Motion and Akiflow. Use when (1) building or implementing Chronos features, (2) making technical decisions about architecture, stack, or infrastructure, (3) planning new features or phases, (4) reviewing code or specs for Chronos, (5) answering questions about Chronos product direction, MVP scope, AI architecture, calendar sync, or monetization. Triggers on any request involving Chronos development, planning, or technical review.
---

# chronos-dev

Development skill for **Chronos** — AI-native task management + planning platform.

## Core Docs (read first)

All specs live in `references/`. Load the relevant file based on the request:

| File | When to load |
|------|-------------|
| `references/path-to-success.md` | Business decisions — pricing, go-to-market, team, Phase 0-4 roadmap, oversight responsibilities |
| `references/mvp-technical-implementation-plan.md` | Technical architecture — infra, AI, calendar sync, WebSocket, security, CI/CD, costs |
| `references/web-app-spec.md` | Web app UX — layout, components, keyboard shortcuts, views, PWA requirements |
| `references/founder-spec.md` | Product context — problem statement, competitive positioning, MVP features |

## Quick Reference

### What is Chronos?

AI-native planning platform that automatically turns task inputs into intelligent, conflict-free schedules. Wedge: **AI scheduling + native Apple apps + transparent pricing**.

- **vs Motion**: Better UX, cheaper, native iPhone/Mac
- **vs Akiflow**: Native apps, AI scheduling, free tier

### MVP Scope (5 bullets — don't expand)

1. Web app (Next.js PWA): Today + Inbox + Calendar + Projects + ⌘K command palette
2. Google Calendar two-way sync (only integration for MVP)
3. AI auto-scheduler with per-block rationale
4. Basic iPhone app (capture companion, not full parity)
5. Auth via Clerk + 3-step onboarding

**Skip**: Outlook, Mac app, teams, social planning, meeting intelligence, offline write

### Tech Stack

```
Frontend:   Next.js 15 + TypeScript + Tailwind + shadcn/ui + Zustand + TanStack Query
Backend:    NestJS + TypeScript + Prisma + PostgreSQL (Supabase)
Queue:      BullMQ + Redis (Upstash)
AI:         Claude Sonnet (parsing) + GPT-4o (scheduling rationale)
Auth:       Clerk
Calendar:   Direct Google Calendar API (no Cronofy)
Realtime:   NestJS WebSocket gateway → Ably at 500+ connections
Infra:      Vercel (frontend) + Railway (backend) + Cloudflare (DNS/CDN)
```

### Infrastructure Costs

| Users | Est. Monthly |
|-------|-------------|
| 10 | ~$40-50 |
| 100 | ~$100-150 |
| 1,000 | ~$300-400 |

AI is the dominant cost driver (~$1.26/user/mo at scale).

### 5 Highest-Risk Technical Decisions

1. **Scheduling engine**: Hybrid deterministic + AI assist. Never pure LLM. Deterministic enforces constraints; AI suggests and explains.
2. **Google Calendar OAuth**: Direct API, Pub/Sub webhooks + 60s polling fallback. Token refresh must be bulletproof.
3. **AI cost controls**: Rate limit parse to 30/day, cache aggressively, confidence threshold fallback to rules-based parser.
4. **WebSocket scaling**: 1 connection per user. Fallback chain: WS → SSE → 5s polling.
5. **DB migrations**: Add-only policy. Never rename/delete columns in MVP. Use `CREATE INDEX CONCURRENTLY`.

### AI Cost Controls (mandatory)

```
Rate limits per user per day:
  - /v1/inbox/parse:  30 calls
  - /v1/schedule/plan: 60 calls
  - /v1/daily-briefing: 30 calls

Cache: parse results cached by text hash, TTL 24h
Fallback: if parse confidence > 0.85, skip AI, use rules engine
Budget mode: if exceeded, disable auto-scheduling, show manual UI only
Alert thresholds: green <$100/mo | yellow $100-200 | red >$200
```

### Domain

Register `chronos.ai` or `chronos.so` **before building**. Cloudflare for DNS.

## When Working on Features

Before implementing any feature, check:
1. Is it in the MVP scope? (path-to-success.md Phase 1)
2. Does it require new infrastructure? (mvp-technical-implementation-plan.md Section 1)
3. Does it affect the AI architecture? (mvp-technical-implementation-plan.md Section 2)
4. Does it touch calendar sync? (mvp-technical-implementation-plan.md Section 3)

If the answer to any is "I don't know," load the relevant reference file first.

## Conventions

- Branch strategy: trunk-based (`main` → feature branch → PR → merge to main)
- Commits: conventional commits (`feat:`, `fix:`, `docs:`, `chore:`)
- Error codes: `AUTH_*`, `CAL_*`, `TASK_*`, `AI_*`, `SCHEDULE_*`, `INFRA_*`
- Migration policy: add-only columns, never rename/delete in MVP
- AI prompts: version-controlled in `backend/src/ai/prompts/`, one file per agent
- API errors: `{ code: string, message: string, details?: object }`

## Access & Oversight

- Production infra: **Aaron only**
- Stripe / Supabase admin: **Aaron only**
- GitHub: Aaron + developers (full access)
- Sentry / PostHog: Aaron + developers (read-only)
- Weekly: AI cost review (OpenAI + Anthropic dashboards)
