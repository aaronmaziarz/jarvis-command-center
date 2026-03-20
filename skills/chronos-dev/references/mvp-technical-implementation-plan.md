# Chronos MVP — Technical Implementation Plan

*Architecture decisions for a bootstrapped AI-native task management platform*
*Date: 2026-03-20*
*Status: Actionable — Ready to Execute*

---

## 1. Infrastructure Architecture

### Recommendation: Split Approach (Frontend + Backend + Data)

| Layer | Recommendation | Why |
|-------|---------------|-----|
| **Frontend hosting** | **Vercel** | Zero-config Next.js deploys, preview URLs per PR, edge network, free tier generous for MVP. Not worth the complexity of Cloudflare Pages with a Next.js app. |
| **Backend hosting** | **Railway** | Nixpacks auto-detects NestJS, ephemeral disks work for BullMQ Redis, $5/month starter is fine for MVP. Migrate to AWS ECS Fargate if you hit 500+ concurrent users. Fly.io is a fine alternative but Railway's DX is better for a solo dev. |
| **Database** | **Supabase** (managed Postgres) | Auth baked in (Clerk is better for MVP auth though — see Security), instant Postgres with RLS, good free tier, daily backups. Graduate to Neon if you need branching dev databases or truly serverless Postgres. |
| **Redis** | **Railway Redis** add-on | $5/month, same provider as backend, low latency. Graduate to Upstash when you need serverless Redis with global replication. |
| **Domain + DNS** | **Cloudflare** (everything) | Registrar transfer to Cloudflare, use Cloudflare DNS. Zero cost, CDN included, Workers for edge functions later if needed. Don't split DNS providers. |
| **CDN** | **Cloudflare** (included) | Already using Cloudflare for DNS. Automatic Brotli compression, asset caching, and DDoS protection. No need for CloudFront unless you're already all-in on AWS. |

### What NOT to use and why
- **AWS EC2/ECS for MVP**: Overkill. You're managing infra that Railway handles for free.
- **Heroku**: Dead. No reason new projects start there.
- **DigitalOcean App Platform**: Fine but Railway's DX is better for Node.js apps.
- **MongoDB**: Wrong tool. Your data is highly relational (tasks, projects, recurrence, audit logs). Postgres JSONB handles the flexibility you actually need.

### ⚠️ HIGH-RISK DECISION #1: Backend Hosting Longevity
Railway is VC-backed and has changed pricing tiers multiple times. **Mitigation:** Keep Dockerfile/containerization so you can migrate to Fly.io or AWS ECS in < 1 day. Don't use Railway-specific features (persistent volumes for Redis is fine for MVP).

---

## 2. The AI Architecture

This is the core product moat. The architecture must be production-grade from day one because AI quality IS the product.

### 2.1 Data Flow: Raw Text → Structured Task

```
User Input: "Finish Q1 deck by Friday need 3hrs review with Sarah Thursday afternoon"
                    │
                    ▼
┌─────────────────────────────────────────────────────────────┐
│  NestJS Controller: POST /v1/inbox/parse                    │
│  - Input: { raw_text: string, user_id: string }             │
│  - Rate limit: 20 req/min per user (free tier)              │
│  - Queue: BullMQ job "parse-task"                           │
└─────────────────────────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────────┐
│  BullMQ Worker: TaskParserAgent                             │
│  - Prompt: versioned system prompt + user text              │
│  - Model: Claude Sonnet 4 (fast, good at extraction)        │
│  - Output: validated JSON matching TaskParseSchema          │
│  - Logging: ai_runs table with token count + latency       │
└─────────────────────────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────────┐
│  Response to client:                                        │
│  {                                                         │
│    title: "Finish Q1 deck",                                │
│    duration_minutes: 180,                                  │
│    due_at: "2026-03-21T17:00:00Z",                         │
│    subtasks_suggested: ["Prepare slides", "Review with Sarah"]│
│    ambiguity_flags: ["stakeholder_needs_confirm"],         │
│    confidence_score: 0.87                                   │
│  }                                                          │
└─────────────────────────────────────────────────────────────┘
                    │
                    ▼
User confirms → POST /v1/tasks → Scheduling Engine → task_blocks table
```

### 2.2 AI Module Architecture

```
src/ai/
├── modules/
│   ├── task-parser/
│   │   ├── task-parser.agent.ts      # Orchestrates parse
│   │   ├── prompts/
│   │   │   ├── v1.system.md          # Versioned system prompt
│   │   │   └── v1.examples.json      # Few-shot examples
│   │   └── schemas/
│   │       └── task-parse.schema.ts  # Zod output schema
│   ├── priority-scorer/
│   │   ├── priority-scorer.agent.ts
│   │   └── schemas/
│   ├── schedule-rationale/
│   │   └── schedule-rationale.agent.ts
│   └── daily-briefing/
│       └── daily-briefing.agent.ts
├── ai.module.ts
├── ai.service.ts                      # Unified interface, retries, fallbacks
└── models.config.ts                   # Model selection + cost tracking
```

### 2.3 Scheduling Decision Logic

```
POST /v1/schedule/plan
          │
          ▼
┌──────────────────────────────────────────────────────────────┐
│  Deterministic Scheduling Engine (pure functions, no AI)    │
│  1. Fetch unscheduled tasks (status = 'todo')                │
│  2. Fetch availability map from calendar_events table        │
│  3. Generate feasible slots (respecting work hours, buffers)│
│  4. Score: urgency*0.4 + importance*0.3 + deadline*0.2 + flexibility*0.1│
│  5. Greedy best-fit: highest score → earliest feasible slot │
│  6. Reserve block in task_blocks table                       │
└──────────────────────────────────────────────────────────────┘
          │
          ▼
┌──────────────────────────────────────────────────────────────┐
│  AI Rationale Layer (only for explanation)                   │
│  - "Scheduled 9–11am because your energy peaks then         │
│     and this is a high-effort task"                          │
│  - NOT used for placement decisions                          │
└──────────────────────────────────────────────────────────────┘
```

### 2.4 Prompt Versioning Strategy

- Store prompts as `.md` files in `src/ai/modules/*/prompts/v{n}.md`
- Track active version in `ai_runs.prompt_version`
- Migration: when updating a prompt, increment version, keep old file
- A/B testing: 10% of users get new version, compare acceptance rate in PostHog

### 2.5 Cost Management ($2–4/user/month)

| Technique | Implementation | Savings |
|-----------|---------------|---------|
| **Rate limiting** | 20 parses/user/month free, 100/month Pro | Prevents abuse |
| **Model routing** | Claude Sonnet for parsing ($0.003/1K tokens), GPT-4o for rationale only | Parse is 80% of calls |
| **Caching** | Redis cache for identical input hashes (TTL: 1hr) | ~20% redundant calls |
| **Batching** | Queue parses, batch into single API call where possible | Reduces overhead |
| **Token budget** | Hard cap per user per day in Redis, reject at gateway | Predictable cost |

**Cost math at 1,000 Pro users:**
- 50 parses/user/month × 200 tokens avg = 10M tokens = ~$30/month on Claude
- 10 rationale calls/user/month × 300 tokens = 3M tokens = ~$60/month on GPT-4o
- **Total AI: ~$90/month = $0.09/user/month** — well under target

### 2.6 Fallback When AI Is Unavailable

```typescript
// ai.service.ts
async parseTask(input: string): Promise<TaskParseResult> {
  try {
    const cached = await this.redis.get(`parse:${hash(input)}`);
    if (cached) return JSON.parse(cached);
    const result = await this.callClaude(input);
    await this.redis.setex(`parse:${hash(input)}`, 3600, JSON.stringify(result));
    return result;
  } catch (error) {
    if (error.status === 429 || error.status === 503) {
      return this.ruleBasedParser.parse(input); // handles "Task X by Friday", etc.
    }
    throw error;
  }
}
```

---

## 3. Calendar Sync Architecture

### 3.1 Google Calendar OAuth Flow

```
1. User clicks "Connect Google Calendar"
2. /auth/google (NestJS) → Google Consent Screen
3. Google callback: /auth/google/callback?code=XXX
4. NestJS exchanges code for tokens
5. Encrypt refresh_token with AES-256 (see Security)
6. Store in calendar_accounts table
7. Queue BullMQ job: SyncFullCalendar
8. Queue recurring job: SyncIncremental (every 60 seconds)
9. Register Google Pub/Sub webhook for push updates
```

### 3.2 Two-Way Sync Reconciliation

| Event Source | Direction | Mechanism | Latency Target |
|-------------|-----------|-----------|----------------|
| User edits in Chronos | Chronos → Google | BullMQ → Google Calendar API `PUT` | < 5 seconds |
| User edits in Google | Google → Chronos | Pub/Sub webhook + 60s polling fallback | < 60 seconds |

**Conflict resolution:** Last-write-wins by `updated_at`. If `provider.updated_at > local.updated_at AND local has unsaved changes`, flag for user review.

### 3.3 What to Store Locally vs. Always Fetch

| Data | Strategy | Rationale |
|------|----------|-----------|
| Calendar metadata (name, color, id) | Local DB, refresh weekly | Rarely changes |
| Calendar events (next 30 days) | Local DB, sync continuously | Core display data |
| Calendar events (31–90 days) | Local DB, sync on demand | Memory optimization |
| Calendar events (90+ days) | Fetch fresh, don't store | Archival view only |
| Free/busy status | Always compute from local DB | No Google round-trip needed |

### 3.4 Google API Rate Limiting Compliance

- **Sync tokens**: Store per-calendar `sync_token`, use `GcalEvents.list` with `syncToken` param
- **Burst limit**: 60 req/user/second — enforced by BullMQ rate limiter
- **Webhook quota**: 100k notifications/day/org — plenty at MVP scale
- **Polling fallback**: If webhook fails 3x, switch to 60-second polling

---

## 4. Real-Time Architecture

### 4.1 WebSocket Setup with NestJS

```typescript
// schedule.gateway.ts
@WebSocketGateway({ cors: { origin: '*' } })
export class ScheduleGateway {
  @SubscribeMessage('subscribe-task')
  handleSubscribe(@MessageBody() data: { taskId: string }, @ConnectedSocket() client: Socket) {
    client.join(`task:${data.taskId}`);
    return { event: 'subscribed', data: { taskId: data.taskId } };
  }
}

// Emit from any service when task changes:
this.gateway.server.to(`task:${taskId}`).emit('task.updated', { task });
```

**Rooms/channels:**
- `user:{userId}` — personal notifications, sync status
- `task:{taskId}` — task detail changes
- `schedule:{date}` — daily schedule updates

### 4.2 Fallback to SSE

WebSockets blocked in some corporate proxies — implement SSE as fallback:
```typescript
// Client: try WebSocket first, fall back to SSE on error
const socket = new WebSocket(url);
socket.onerror = () => connectSSE(url.replace('ws', 'http') + '/events');
```

### 4.3 Self-Hosted vs. Managed Real-Time

| Option | Cost | Recommendation |
|--------|------|----------------|
| **Self-hosted (NestJS Gateway)** | $0 extra on Railway | **MVP choice** |
| **Ably** | $50+/month | Only if >10K concurrent connections |
| **Pusher** | $50+/month | Same as Ably |

**⚠️ HIGH-RISK DECISION #2: WebSocket Scaling**
Self-hosted WebSockets on Railway don't auto-scale. At 500+ connections, migrate to Ably or Fly.io with Fly Machines. **Mitigation:** Monitor in Sentry, alert at 200 connections.

---

## 5. Security Architecture

### 5.1 Clerk JWT Validation

```typescript
// clerk.middleware.ts (NestJS)
@Injectable()
export class ClerkMiddleware implements NestMiddleware {
  constructor(private clerkService: ClerkService) {}
  
  async use(req: Request, res: Response, next: NextFunction) {
    const token = req.headers.authorization?.replace('Bearer ', '');
    if (!token) return res.status(401).json({ error: 'No token' });
    try {
      const payload = await this.clerkService.verifyToken(token);
      (req as any).user = { id: payload.sub, ...payload };
      next();
    } catch {
      return res.status(401).json({ error: 'Invalid token' });
    }
  }
}
```

### 5.2 API Rate Limiting

| Endpoint | Limit | Window | Rationale |
|----------|-------|--------|-----------|
| `POST /v1/inbox/parse` | 20 (free) / 100 (Pro) | per user / month | AI cost control |
| `POST /v1/schedule/plan` | 10 | per user / minute | Compute-heavy |
| `GET /v1/calendars/events` | 60 | per user / minute | Google API proxy |
| All other endpoints | 100 | per user / minute | Standard |

Implementation: `@nestjs/throttler` with Redis store.

### 5.3 Calendar OAuth Token Encryption

```typescript
// encryption.service.ts
private readonly ALGORITHM = 'aes-256-gcm';
encryptToken(token: string): string {
  const iv = crypto.randomBytes(16);
  const key = Buffer.from(process.env.TOKEN_ENCRYPTION_KEY!, 'hex'); // 32 bytes
  const cipher = crypto.createCipheriv(this.ALGORITHM, key, iv);
  const encrypted = Buffer.concat([cipher.update(token, 'utf8'), cipher.final()]);
  const authTag = cipher.getAuthTag();
  return Buffer.concat([iv, authTag, encrypted]).toString('base64');
}
```

**Storage:** `calendar_accounts.refresh_token_encrypted` — never store raw tokens.

### 5.4 Secrets Management

| Option | Cost | Recommendation |
|--------|------|----------------|
| **Doppler** | Free up to 3 projects | **MVP choice** — best DX, GitHub Actions + Railway integration |
| **AWS Secrets Manager** | $0.05K/month | Overkill unless all-in on AWS |
| **.env files** | Free | Fine for local dev, bad for production |

---

## 6. CI/CD Pipeline

### 6.1 GitHub Actions Workflow

```yaml
# .github/workflows/ci.yml
name: CI/CD
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4 with: { node-version: '22' }
      - run: npm ci && npm run lint && npm run test && npm run test:e2e

  build-frontend:
    needs: test
    if: github.event == 'push'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci && npm run build working-directory: ./frontend
      - uses: vercel-action@v5 with: { vercel-token: ${{ secrets.VERCEL_TOKEN }}, vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}, vercel-project-id: ${{ secrets.VERCEL_PROJECT_ID }}, vercel-args: '--prod' }

  build-backend:
    needs: test
    if: github.event == 'push'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: docker build -t chronos-backend:${{ github.sha }} . && docker push registry.railway.app/chronos/backend:${{ github.sha }}
      - uses: railway/action@v1 with: { token: ${{ secrets.RAILWAY_TOKEN }} }
```

### 6.2 Branch Strategy: Trunk-Based

```
main (always deployable)
  └── feature/task-parser-v2 (1-2 days max, then merge)
  └── fix/calendar-sync-bug (hours to days, then merge)
```

Simpler than Gitflow, forces small PRs, faster iteration. Vercel preview deploys on every PR.

### 6.3 Preview Environments

| For | How | Cost |
|-----|-----|------|
| Frontend (Next.js) | Vercel auto-preview on PR | Free |
| Backend (NestJS) | Railway ephemeral deploy on PR | ~$0.10/hour |

**MVP approach:** No dedicated backend preview. Vercel preview points to staging Railway backend.

### 6.4 Backend Deployment Strategy

**Rolling deployment** on Railway. Zero-downtime by default — Railway waits for health check before cutting over.
- Health check: `GET /health` returns `{ status: 'ok', timestamp }`

### 6.5 Database Migrations in CI/CD

```yaml
# After docker push, before deploy:
- name: Run migrations
  run: npx prisma migrate deploy
  env:
    DATABASE_URL: ${{ secrets.PROD_DATABASE_URL }}
```

**Critical rules:**
1. Migrations must be backwards-compatible
2. New columns must have defaults or be nullable
3. Never run `migrate reset` in production
4. Test on staging first

---

## 7. Observability

### 7.1 Sentry — Full Setup

```typescript
// main.ts
import * as Sentry from '@sentry/nestjs';
Sentry.init({
  dsn: process.env.SENTRY_DSN,
  tracesSampleRate: 0.1, // 10% for cost control
  environment: process.env.NODE_ENV,
  release: process.env.GIT_SHA,
});
```

**What to capture:** Unhandled exceptions, AI parsing failures, calendar sync failures, JWT validation failures.
**What NOT to capture:** Expected validation errors (400s from Zod), rate limit hits.

### 7.2 Structured Logging

```typescript
logger.log({ event: 'task.created', taskId: task.id, userId: user.id, duration_ms: 12 }, 'Task created');
logger.warn({ event: 'ai.parse.low_confidence', userId: user.id, confidence: 0.3 }, 'Low confidence parse');
logger.error({ event: 'calendar.sync.failed', calendarId: id, error: error.message }, 'Sync failed');
```

- `ERROR`: Unexpected failures (alert-worthy)
- `WARN`: Expected failures, degraded behavior (review daily)
- `LOG`: Business events (for analytics)
- `DEBUG`: Verbose dev info (off in production)

### 7.3 PostHog — Critical Events to Track

| Event | Properties | Why |
|-------|-----------|-----|
| `task_created` | source: 'quick_add' \| 'inbox_confirm' \| 'calendar' | Where users add tasks |
| `inbox_item_confirmed` | parse_confidence, time_to_confirm_ms | AI parse quality |
| `schedule_accepted` | tasks_scheduled, ai_rationale_shown | Auto-scheduling usefulness |
| `calendar_connected` | provider: 'google' \| 'outlook' | Acquisition funnel |
| `ai_parse_failed` | fallback_used: boolean | AI reliability signal |
| `upgrade_cta_clicked` | plan: 'pro' \| 'pro_plus' | Conversion funnel |

### 7.4 Uptime Monitoring

| Check | Service | Interval | Alert |
|-------|---------|---------|-------|
| Frontend | Vercel built-in | Continuous | Email if down |
| Backend health | UptimeRobot | 5 min | Email + SMS if down |
| Google OAuth callback | UptimeRobot | 5 min | Email if down |

**Status page:** Use `statuspage.io` ($6/month) or free `uptime.kuma.is`. Public page builds trust during beta.

### 7.5 Alerting

| Alert | When | How |
|-------|-----|-----|
| P0: Backend down | 1 failed health check | SMS |
| P0: DB connection lost | Railway alert | Email + SMS |
| P1: Error rate > 5% in 5 min | Sentry alert | Email |
| P1: AI parse failure > 20% | Custom Sentry alert | Email |

**No PagerDuty until $5K+/month ARR.** Email alerts are fine for MVP.

---

## 8. MVP Scope Boundaries

### What NOT to Build in MVP

| Feature | Why Not MVP | When |
|---------|------------|------|
| Microsoft Outlook sync | Complex OAuth + Graph API | Phase 2 |
| Apple Calendar / CalDAV | Different sync model entirely | Phase 2 |
| Shared workspaces / teams | Product complexity explosion | Phase 3 |
| Meeting transcription | Whisper API cost + UX complexity | Phase 2+ |
| Task breakdown into subtasks | MVP parse quality insufficient | Post-beta |
| Mac native app | Hire dedicated iOS dev first | Phase 3 |
| Android app | Wrong audience for MVP | Never |
| Offline write (web) | Service worker + sync logic is weeks of work | Phase 2 |
| Advanced analytics dashboard | PostHog dashboards are enough | Phase 2+ |
| SOC 2 / enterprise SSO | Only needed with enterprise demand | Phase 4+ |

### What to Stub/Mock vs. Real

| Component | MVP Approach | Rationale |
|-----------|-------------|-----------|
| Google Calendar sync | **Real** | Core value prop |
| AI parsing | **Real** | Core value prop |
| AI scheduling rationale | **Real** | Core value prop |
| AI auto-scheduling algorithm | **MVP deterministic** | Hybrid engine is Phase 2 |
| Stripe billing | **Real** | $15 Pro pricing needs to work at launch |
| Push notifications | **Stub (log only)** | Web push setup is complex, email-only for MVP |
| Apple Sign-In | **Real** | Required for iPhone app users |

### Third-Party Services: Build vs. Buy

| Component | Buy/Use | Build |
|-----------|---------|-------|
| Auth | **Clerk** | — |
| Database | **Supabase Postgres** | — |
| Billing | **Stripe** | — |
| Analytics | **PostHog** | — |
| Error monitoring | **Sentry** | — |
| Email | **Resend** | — |
| Scheduling engine | — | **Build** (the moat) |
| AI orchestration | — | **Build** (APIs) |
| Calendar sync logic | — | **Build** (Google Calendar API) |
| Realtime (WebSocket) | — | **Build** (NestJS gateway) |

### Offline Behavior in MVP

**Skip offline write for MVP:**
- ✅ Service worker caches app shell
- ✅ Cached calendar data shows offline
- ❌ User cannot create tasks offline
- ❌ No background sync queue

Saves 2-3 weeks. Beta users are online 99% of the time.

---

## 9. Development Workflow

### 9.1 Repo Structure: Monorepo

```
chronos/
├── apps/
│   ├── web/                    # Next.js frontend
│   │   ├── app/               # App Router pages
│   │   ├── components/        # React components
│   │   └── package.json
│   └── api/                   # NestJS backend
│       ├── src/modules/        # Feature modules
│       ├── src/ai/            # AI orchestration
│       └── package.json
├── packages/
│   ├── shared-types/          # Shared TypeScript interfaces
│   └── database/              # Prisma schema + migrations
├── docker-compose.yml          # Local dev stack
├── turbo.json                 # Turborepo config
└── package.json                # Root workspace
```

**Why monorepo:** Single PR can touch frontend and backend. Shared types prevent drift. Easier CI/CD.

### 9.2 Local Development Setup

```yaml
# docker-compose.yml
services:
  postgres:
    image: postgres:16
    environment:
      POSTGRES_DB: chronos_dev
      POSTGRES_PASSWORD: dev_password
    ports: ["5432:5432"]
    volumes:
      - postgres_data:/var/lib/postgresql/data
  redis:
    image: redis:7-alpine
    ports: ["6379:6379"]
    volumes:
      - redis_data:/data
```

```bash
# Setup (run once)
git clone git@github.com:getchronos/chronos.git
cd chronos
npm install
cp apps/api/.env.example apps/api/.env   # fill in API keys
cp apps/web/.env.example apps/web/.env
npx docker-compose up -d
npx prisma migrate dev
npx prisma generate
npm run dev  # starts frontend (3000) + backend (3001)
```

### 9.3 Environment Variables

```
# apps/api/.env.example
DATABASE_URL=postgresql://postgres:dev_password@localhost:5432/chronos_dev
REDIS_URL=redis://localhost:6379
CLERK_SECRET_KEY=sk_test_xxx
OPENAI_API_KEY=sk-xxx
ANTHROPIC_API_KEY=sk-ant-xxx
GOOGLE_CLIENT_ID=xxx.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=xxx
STRIPE_SECRET_KEY=sk_test_xxx
SENTRY_DSN=https://xxx@sentry.io/xxx
TOKEN_ENCRYPTION_KEY=xxx  # 32-byte hex
```

**Strategy:** Doppler syncs to GitHub Actions + Railway. Local `.env` is gitignored.

---

## 10. Month-by-Month Technical Milestones

### Month 1: Core Loop End-to-End

**Goal:** User can sign up, connect Google Calendar, and create + see a task on a calendar.

| Week | Deliverable | Details |
|------|-------------|---------|
| 1 | Project setup | Monorepo, CI/CD, Docker Compose, Prisma schema |
| 2 | Auth | Clerk integration, JWT validation in NestJS |
| 3 | Task CRUD + Google OAuth | Create/list tasks, connect Google Calendar |
| 4 | Calendar view | FullCalendar display, basic task blocks |

**Definition of done:** User can create a task and see it on a calendar view with Google events.

### Month 2: AI Features + Polish

**Goal:** Natural language capture works reliably and AI schedules tasks automatically.

| Week | Deliverable | Details |
|------|-------------|---------|
| 5 | AI parsing | Claude Sonnet integration, parse endpoint, Zod validation, rule-based fallback |
| 6 | AI auto-scheduling | Deterministic scheduling engine, task block creation, rationale generation |
| 7 | Quick capture flow | ⌘K palette, real-time parse preview, inbox confirm |
| 8 | Replanning | Calendar change detection, disrupted block flagging, replan trigger |

**Definition of done:** User types "Finish deck by Friday need 3 hours" → AI parses → user confirms → task appears scheduled with AI rationale.

### Month 3: Shippable MVP

**Goal:** Everything needed for beta with real users, no P0 bugs.

| Week | Deliverable | Details |
|------|-------------|---------|
| 9 | Today view + briefing | AI briefing card, vertical timeline, task detail panel |
| 10 | Drag-to-reschedule + sync | Drag on calendar, push to Google Calendar, webhook receiver |
| 11 | PWA + observability | Service worker, PostHog, Sentry, Stripe (free trial) |
| 12 | Bug bash + beta launch | Fix P0 bugs, onboarding polish, invite first 20 beta users |

**Definition of done:** First 20 beta users complete full flow (signup → connect → NLP create → AI schedule → sync to Google). No data loss, no auth bugs, sync < 10s.

### How to Verify MVP Before Beta

1. **Smoke test script:** Automated full user flow runs in CI on every PR
2. **Load test:** 10 concurrent users with k6 — p95 < 500ms
3. **AI quality gate:** `ai_parse_failed` rate in PostHog > 10% = don't ship
4. **Dogfood:** Use it yourself for 2 weeks first. Every bug you hit is a P0.

---

## 11. Tech Stack Summary

### Definitive Component → Service Table

| Component | Service | MVP Cost |
|-----------|--------|----------|
| Frontend framework | Next.js 15 | — |
| Frontend hosting | **Vercel** | Free (Hobby) |
| Backend framework | NestJS + TypeScript | — |
| Backend hosting | **Railway** | $5/mo (starter) |
| Database | **Supabase** (Postgres 16) | Free (tier 2) |
| Redis | **Railway Redis** | $5/mo |
| Auth | **Clerk** | Free (up to 10K MAU) |
| AI — parsing | **Claude Sonnet 4** (Anthropic) | ~$10/mo at MVP |
| AI — rationale | **GPT-4o** (OpenAI) | ~$20/mo at MVP |
| Calendar API | **Google Calendar API** | Free |
| Billing | **Stripe** | 2.9% + 30¢ |
| Analytics | **PostHog** | Free |
| Error monitoring | **Sentry** | Free (5K events/mo) |
| Email | **Resend** | Free (3K/month) |
| Secrets | **Doppler** | Free (3 seats) |
| DNS + CDN | **Cloudflare** | Free |
| Domain | **Cloudflare Registrar** | $12/yr |

### Monthly Infrastructure Cost

| Scale | Total | Breakdown |
|-------|-------|----------|
| **10 users (beta)** | **~$40–50/month** | Railway ($5) + Redis ($5) + Supabase (free) + Vercel (free) + AI ($5) |
| **100 users** | **~$100–150/month** | Railway ($15) + Redis ($10) + Supabase ($25) + Vercel (free) + AI ($50) + Doppler ($3) |
| **1,000 users** | **~$300–400/month** | Railway ($50) + Redis ($20) + Supabase ($75) + Vercel Pro ($20) + AI ($150) + Doppler ($5) |

---

## ⚠️ Top 5 Highest-Risk Technical Decisions

| # | Decision | Risk | Mitigation |
|---|----------|------|------------|
| **1** | Railway for backend hosting | VC-backed pricing volatility, potential migration needed | Keep Dockerfile, migrate to Fly.io in < 1 day |
| **2** | Self-hosted WebSockets | No auto-scaling on Railway, painful at 500+ connections | Monitor with Sentry, alert at 200, migrate to Ably if needed |
| **3** | Direct Google Calendar API (no Cronofy) | Complexity of handling all edge cases yourself | Build solid sync reconciliation logic, comprehensive error handling |
| **4** | Hybrid deterministic + AI scheduling | MVP deterministic engine may feel "basic" | Ship anyway, calibrate over 6 months with real user data |
| **5** | Skip offline write in MVP | Beta users will complain | Be transparent in beta, prioritize Phase 2 |

---

*Document created from: path-to-success.md, web-app-spec.md, task-app-planning.md*
