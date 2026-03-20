# Chronos — Path to Success
*Synthesized from: web-app-spec.md, founder-spec.md, task-app-planning.md*
*Status: Actionable Master Plan — Ready to Execute*

---

## Phase 0: Foundation (Before Writing Any Code)

### Definitive Product Positioning

**Chronos** is an AI-native planning and execution platform that automatically turns messy task inputs into intelligent, conflict-free schedules — with the UX polish of Linear and the capture speed of Akiflow, plus native iPhone and Mac apps that neither competitor offers. Chronos wins on three bets: the scheduling moat (a hybrid deterministic + AI engine that respects user constraints), native Apple ecosystem depth (SwiftUI apps, widgets, menu bar, Siri shortcuts), and transparent pricing (no bait-and-switch tiers like Motion or Akiflow). The wedge is AI-powered personal scheduling for the productivity power user who wants their calendar to just work.

---

### MVP Scope — What Ships First

1. **Web app (Next.js SPA, installable as PWA)** covering Today view with AI briefing card, Inbox with natural language parse, Calendar with month/week views, Projects with list/kanban, and a ⌘K command palette for power users. All CRUD, quick capture, and drag-to-reschedule.
2. **Google Calendar two-way sync** (read/write via Google Calendar API) as the only integration — this is the forcing function for demonstrating real value.
3. **AI auto-scheduler** that takes inbox tasks with duration + deadline and places them on the calendar respecting work hours, energy windows, and priorities. Every scheduled block shows a one-line AI rationale. All AI decisions are overridable.
4. **Basic iPhone app** — quick capture + task list + today view. Not full feature parity; this is a capture companion to the web app for MVP.
5. **Auth, onboarding, basic settings** — email/Google/Apple sign-in via Clerk, 3-step onboarding (create account → connect Google Calendar → set work hours).

That's it. No Outlook, no Mac app, no teams, no social planning, no meeting intelligence. Five sentences, five bullets. Ship it.

---

### Tech Stack Decisions — Open Items with Recommendations

| Decision | Options | Recommendation |
|----------|---------|----------------|
| **Frontend framework** | Next.js 15 vs React + Vite | **Next.js 15** — app router, API routes, and Vercel deploy out of the box are worth the opinionation. Don't overthink this. |
| **Native app language** | SwiftUI vs React Native | **SwiftUI** — native feel IS the product moat. React Native would be a strategic mistake for an app targeting Apple power users. |
| **Database** | Supabase hosted Postgres vs direct Postgres on Railway/Render | **Supabase** initially — managed auth, easy Postgres, realtime, and fast to launch. Migrate to direct Postgres if costs or lock-in become issues post-beta. |
| **Auth provider** | Clerk vs Auth0 vs Supabase Auth | **Clerk** — fastest secure launch, Apple Sign-In baked in, web component library beats rolling your own. |
| **AI model** | GPT-5.4 (OpenAI) vs Claude Sonnet (Anthropic) | **GPT-5.4 for scheduling/rationale** (structured JSON output, function calling), **Claude Sonnet for parsing** (nuance extraction). Blend, don't choose one. Rate-limit aggressively to keep costs at ~$2/user/month. |
| **Calendar sync approach** | Direct Google Calendar API vs Cronofy/Kalendars abstraction | **Direct Google Calendar API for MVP** — simpler, cheaper, full control. Add Cronofy in Phase 2 when you add Outlook and need unified abstraction. |
| **Real-time sync** | Ably vs Socket.io vs Supabase Realtime | **Ably** — simplest managed realtime with good SDKs across all platforms. Graduate to native WebSocket on NestJS only if Ably costs become prohibitive (>10K concurrent users). |

---

### What "Done" Looks Like for MVP Launch

- [ ] User can sign up, connect Google Calendar, and see their calendar inside Chronos within 5 minutes
- [ ] User can type "Call John Monday 3pm 30min" → AI parses → confirms → task appears on calendar
- [ ] AI scheduler can take 10 unscheduled tasks and place them in available slots with rationale shown
- [ ] Drag-to-reschedule works on web calendar, syncs to Google within 5 seconds
- [ ] iPhone app can capture a task and see it in web within 10 seconds
- [ ] No P0 bugs (calendars not syncing, tasks disappearing, auth breaking)
- [ ] P90 page load < 3s, command palette opens < 100ms
- [ ] Privacy policy and terms of service live
- [ ] Stripe billing integration functional (free trial → paid upgrade path)

---

## Phase 1: Build MVP (Months 1–3)

### Web App — Build vs Skip

**BUILD:**
- App shell: sidebar, top bar, routing (Next.js App Router)
- Auth: Clerk (signup, login, session, Apple/Google SSO)
- Today view: AI briefing card + vertical timeline with task blocks
- Calendar view: month + week toggle, FullCalendar for MVP
- Inbox view: natural language capture → AI parse preview → confirm → task
- Projects view: list + kanban toggle per project
- Task detail panel: all fields, edit, complete, defer, archive
- Command palette (⌘K): task capture, navigation, shortcuts
- Quick capture (⌘N + floating button)
- Google Calendar two-way sync
- Basic settings: work hours, timezone, notification preferences, AI toggles
- PWA: manifest + service worker (installable, offline read-only)
- Error monitoring (Sentry) + product analytics (PostHog)

**SKIP:**
- Outlook/Microsoft sync (Phase 2)
- Shared workspaces / team features (Phase 2)
- Social planning (Phase 2)
- Custom calendar timeline views (replace FullCalendar later)
- Full offline write (Phase 2 — MVP is online-only writes, read cache OK)
- Advanced analytics dashboard
- Meeting intelligence / transcription

---

### Backend — Build vs Skip

**BUILD:**
- NestJS + TypeScript REST API
- Prisma + PostgreSQL (Supabase)
- Clerk JWT validation middleware
- `/v1/inbox/*` endpoints (create, parse, confirm, archive)
- `/v1/tasks/*` endpoints (CRUD, complete, reopen)
- `/v1/projects/*` endpoints
- `/v1/schedule/plan` + `/v1/schedule/replan`
- `/v1/calendars/*` + Google Calendar OAuth + sync engine
- `/v1/me/preferences`
- BullMQ + Redis for background jobs (sync, AI parsing, notifications)
- Redis for session cache + rate limiting
- Webhook handler for Google Calendar push notifications
- AI orchestration layer: TaskParserAgent, PriorityScorerAgent, ScheduleRationaleAgent
- Audit log (task_events table)
- Stripe webhook handler (basic — subscription creation only)

**SKIP:**
- Microsoft Graph API integration
- Apple Calendar / CalDAV
- Meeting transcription pipeline
- Document processing (docs → tasks)
- Custom scheduling algorithm beyond weighted heuristic + greedy fit
- SOC 2 / enterprise SSO

---

### Calendar Integrations — Order

1. **Google Calendar** — MVP launch (months 1–3). Two-way sync, read/write, webhook push + 60s polling fallback.
2. **Microsoft Outlook** — Phase 2 (month 4–5). Via Microsoft Graph API.
3. **Apple Calendar (iCloud)** — Phase 2 (month 5–6). Via CalDAV. Also EventKit for native iPhone app.
4. **Read-only iCal import** — Phase 1 (month 2–3) if time allows. Low effort, goodwill feature.

---

### AI Features — Include vs Defer

**INCLUDE in MVP:**
- Natural language task parsing (title, duration, deadline, tags, recurrence)
- AI prioritization scores (urgency + importance + effort)
- Auto-scheduling with slot allocation (respecting work hours, energy, deadlines)
- AI rationale on every scheduled block ("Scheduled here because your energy peaks 9–11am and this task is high-effort")
- Basic daily briefing card (top 3 priorities, 2 risks, schedule rationale)
- Replanning when calendar events change (with disruption status flags)

**DEFER to Phase 2+:**
- Meeting action-item extraction
- Task breakdown into subtasks
- End-of-day review / shutdown ritual
- Duration prediction from historical actuals
- Behavioral personalization (preferred time windows learned over time)
- Docs → tasks pipeline
- Advanced meeting intelligence (transcription, summarization)

---

### Team Composition Needed

| Role | Scope | Months 1–3 |
|------|-------|------------|
| **Full-stack (you/Aaron)** | Everything backend + infra | Primary driver |
| **Frontend (React/Next.js)** | Web app, command palette, calendar views | Month 1.5 onward |
| **iOS Developer** | SwiftUI iPhone app, EventKit, widgets | Month 2 onward |
| **Designer (PT or contractor)** | Full design system, all screens, motion spec | Month 0–1 (upfront), then as-needed |
| **AI/ML (PT or contractor)** | Prompt engineering, AI orchestration, output validation | Month 1–2 |

**Minimum viable team for MVP:** You (full-stack + product) + 1 frontend developer + 1 iOS developer + 1 designer. AI work can be done by you with contractor review of prompts.

---

### Rough Monthly Milestones

| Month | Milestone |
|-------|-----------|
| **Month 1** | Project setup, auth (Clerk), app shell, database schema (Prisma), Google OAuth, basic task CRUD, basic calendar view (FullCalendar), natural language parsing endpoint |
| **Month 2** | Scheduling engine (MVP — weighted heuristic), AI briefing card, drag-to-reschedule, two-way Google sync, inbox confirm flow, quick capture, PWA shell, iPhone app scaffold + basic capture |
| **Month 3** | Full ⌘K command palette, replanning on disruption, settings pages, onboarding polish, PostHog + Sentry, Stripe billing (free trial), bug bash, soft launch to beta users |

---

## Phase 2: Beta Launch (Month 3–4)

### How to Get First 100 Users

1. **Personal network first** — 20–30 friends, ex-colleagues, productivity enthusiasts. Direct DMs. Offer 6 months Pro free in exchange for structured feedback. Don't publicize yet.
2. **Product Hunt soft launch** — not a big bang. Post once, get initial batch of power users. Respond to every comment.
3. **r/productivity + r/TaskManagement** — genuine posts about the problem ("I built Chronos because Motion was too expensive and Akiflow has no Mac app"). Not spam. Real.
4. **Linear + Raycast + Cron crossover audience** — these users already love premium productivity tools. Find where they congregate (Twitter/X, Discord servers).
5. **Waitlist page** — build one now (Phase 0) even before launch. Collect emails. Those become your beta invite list.
6. **No paid ads yet** — you don't have product-market fit. Spend time on real users, not acquisition.

---

### Feedback Collection Strategy

- **In-app feedback widget** — low friction, Contextual. "Is this schedule suggestion useful? 👍 / 👎" on each AI block.
- **Structured 15-min user interview** — target 20 beta users for a Zoom call by month 4. Ask: "Show me how you'd add a new task" and watch them struggle.
- **PostHog funnel analysis** — track: sign-up → calendar connected → first task created → first AI schedule accepted. Find where people drop off.
- **Dedicated Slack/Discord** — 10–20 people in a private community. High signal, low volume. Pay them in early access.
- **Support tickets as signal** — every ticket is a UX failure. Categorize and count. If 5 people ask the same thing, it's a product gap, not edge case.

---

### What to Fix Based on Feedback (Expected Top Issues)

Based on analogous products, expect:
1. **Calendar sync delays** — users will hate waiting >30s for Google events to appear. Optimize polling + webhook reliability immediately.
2. **AI scheduling too aggressive or too conservative** — calibration issue. Add explicit user control ("scheduling aggressiveness" slider).
3. **Parse failures on ambiguous input** — "lunch with John next week" fails. Add disambiguation UX (prompt user: "Which day?").
4. **Inbox overflow** — if inbox items pile up, the confirm flow is too friction-heavy. Streamline to 1-tap confirm.
5. **Mobile UX** — web app on mobile is clunky. Accelerate iPhone app dev.

---

### Metrics to Track

| Metric | Target by End of Beta |
|--------|----------------------|
| Sign-ups | 300 |
| Calendar connected | 60% of sign-ups |
| First task created | 70% of connected users |
| First AI schedule accepted | 50% of task creators |
| 7-day retention | 40% |
| 30-day retention | 20% |
| NPS (beta users) | 40+ |
| P95 task sync latency | < 10 seconds |
| Support tickets / 100 users | < 5 |

---

## Phase 3: Monetize & Scale (Month 4–6)

### Pricing Tiers (Confirmed)

| Tier | Price | What It Includes | Rationale |
|------|-------|-----------------|-----------|
| **Free** | $0 | 1 calendar, 100 tasks, manual scheduling, 20 AI parses/month, basic iPhone app | Generous enough to build habit. Unlike Akiflow (no free tier) or Motion (AI-only paid). |
| **Pro** | $15/mo or $144/yr | Unlimited tasks, all calendars, AI auto-scheduling, AI briefing, replanning, inbox+smart parse, iPhone + Mac app, widgets | Replaces Akiflow ($15–30/mo) and upgrades from free-tier users. Power user sweet spot. |
| **Pro Plus** | $24/mo or $228/yr | Everything in Pro + meeting action extraction, task breakdown, docs→tasks, premium analytics, priority support, higher AI quotas | Founders, executives, power users who want the full AI suite. Margin driver. |
| **Teams** | $20/user/mo | Everything in Pro Plus + shared workspaces, assignees, team views, booking links, admin controls | Agencies, small teams. Custom onboarding, Stripe seat-based billing. |
| **Enterprise** | Custom | SSO/SAML, audit logs, data residency, dedicated support, security review | Post-MVP. Don't build until you have 3+ inbound enterprise requests. |

**Annual discount:** 20% off (consistent with 2 months free). Drives cash flow and reduces churn.

---

### Payment / Billing Setup

- **Stripe Checkout** for all plans. Monthly + annual toggle.
- **Free trial:** 14 days Pro trial on sign-up. No credit card required to start free tier.
- **Upgrade flow:** In-app banner on free tier after user creates 10+ tasks. "Unlock unlimited with Pro."
- **Downgrade handling:** If user downgrades from Pro to Free, retain data. Hide AI features. Cap at 100 tasks — prompt to archive or delete overflow.
- **Failed payment:** 7-day grace period, then account moves to Free. No data deletion.
- **Invoice/receipts:** Stripe-generated. PCI compliance handled by Stripe.
- **Tax:** Stripe Tax for VAT/GST collection in EU + US sales tax. Don't build this manually.

---

### Conversion Strategy (Free → Paid)

1. **In-app AI nudge** — when free user hits 80/100 tasks, show: "You've created 80 tasks this month. Upgrade to Pro for unlimited + AI scheduling."
2. **Time-based trigger** — after user has used the app 10+ days in 30 days AND completed 5+ tasks, surface upgrade prompt.
3. **Feature gates, not degrade** — don't break the app for free users. Just show "Pro feature" labels on AI scheduling, multiple calendars, Mac app.
4. **Social proof** — "Join 847 professionals who plan smarter with Chronos" on upgrade page.
5. **Annual push at signup** — show annual pricing first, emphasize 2 months free. Higher LTV, lower churn.

---

### Growth Channels (Month 4–6)

1. **Product Hunt launch** — full formal launch here. Video demo, clear differentiators. Target #1 of the day.
2. **SEO content** — "Motion alternative", "Akiflow alternative", "AI task scheduler" keywords. 5 pillar articles.
3. **Twitter/X presence** — founder-led. Share: behind-the-scenes scheduling decisions, product updates, user testimonials.
4. **Reddit** — genuine participation in r/productivity, r/TaskManagement, r/Entrepreneur. Not spammy links.
5. **Waitlist referral** — "Invite a friend, both get 1 month Pro free." Viral loop for power user networks.
6. **LinkedIn** — if targeting enterprise, this matters. Focus after Pro Plus launches.

---

## Phase 4: Full Production & Growth (Month 6–12)

### Native Apps — iPhone + Mac — What to Prioritize

**iPhone App (Priority order):**
1. Quick capture with full natural language parse (already in MVP basic)
2. Today view with AI briefing card (match web app)
3. Task list with swipe actions (defer, complete, edit)
4. Calendar day/week view with drag-to-reschedule
5. Inbox review + confirm
6. Push notifications (reminders, disruption alerts, daily briefing)
7. Widgets (WidgetKit) — next task, today's schedule
8. Live Activities for active focus block
9. Siri shortcuts ("Add task in Chronos", "Plan my day in Chronos")
10. Background sync via BackgroundTasks framework

**Mac App (Priority order):**
1. Menu bar app — instant capture, next task display, focus timer (small, fast to build, high utility)
2. Full main window — calendar + task planning (feature parity with web Today + Calendar views)
3. Command center / ⌘K palette (native, faster than web)
4. Native keyboard shortcuts
5. Spotlight + App Intents integration
6. Deep work mode (full-screen distraction-free planning)
7. Mini planner floating window

**Do NOT attempt in month 6–12:**
- Android app
- Multi-window management beyond mini planner
- Advanced drag/drop complexity on Mac
- Linux or Windows

---

### Team / Features to Add Based on Revenue

**If ARR > $50K by month 9:**
- Hire a **senior iOS engineer** to own native app roadmap full-time
- Add **customer support** (PT — use Intercom or Crisp)

**If ARR > $100K by month 12:**
- Hire a **second frontend engineer** (web app polish + PWA offline)
- Add a **growth/marketing hire** (PT or contractor — content + SEO)
- Build **Teams tier infrastructure** (workspace roles, permissions, shared views)

---

### Retention Strategies

1. **Daily habit loop** — AI briefing card is the daily touchpoint. Make it genuinely useful (not fluff). If users check it every morning, they won't churn.
2. **AI quality** — If the scheduling rationale is always "because we had a slot," trust erodes. Every AI action must have a specific, believable reason.
3. **Switching cost via data** — Task history, project context, learned preferences. Once a user has 200+ tasks with rich metadata, migrating is painful.
4. **Annual plan incentive** — Push annual at every upgrade moment. Churn rate on annual plans is ~3x lower than monthly.
5. **Quarterly check-in email** — "Here's what you accomplished in Q3 — 47 tasks done, 12 hours in deep work blocks." Reinforce value.
6. **Power user milestones** — "You've scheduled 100 tasks with AI! Here's your summary." Gamification without being annoying.

---

### Year 1 Targets (Users, ARR)

| Metric | Target |
|--------|--------|
| Free sign-ups | 10,000 |
| DAU / MAU ratio | 35% (healthy for productivity app) |
| Pro subscribers | 1,000 |
| Teams customers | 50 |
| **ARR** | **$120,000–$180,000** |
| Paying MRR at year-end | $15,000–$20,000 |
| Churn (Pro, annual) | < 5%/month |
| NPS | 50+ |

---

## Every Single Thing Needed to Ship — Checklist

### Technical

- [ ] **GitHub repo** — private, CI/CD via GitHub Actions
- [ ] **Vercel account** — frontend hosting + edge
- [ ] **Railway or Render** — backend hosting (Node.js/NestJS)
- [ ] **Supabase project** — Postgres + Auth + Realtime
- [ ] **Redis** (Railway or Redis Cloud) — BullMQ queue + cache
- [ ] **Clerk account** — auth, session, Apple/Google SSO
- [ ] **Stripe account** — billing, Products + Prices configured for each tier
- [ ] **OpenAI API account** — GPT-5.4 for scheduling/rationale
- [ ] **Anthropic API account** — Claude Sonnet for parsing
- [ ] **Google Cloud project** — Calendar API enabled, OAuth 2.0 credentials
- [ ] **Google OAuth consent screen** — configured, published (internal first, then external)
- [ ] **Domain** — chronos.ai or chronos.so (register before someone else)
- [ ] **SSL certificates** — automatic via Vercel + Railway
- [ ] **Sentry project** — error tracking, source maps uploaded
- [ ] **PostHog project** — analytics, funnel tracking, session recording (opt-in)
- [ ] **PWA manifest** — app name, icons, theme color, standalone display
- [ ] **Service Worker** — Workbox, cache-first for shell, network-first for API
- [ ] **CI/CD pipeline** — test → lint → build → deploy on PR merge to main
- [ ] **Environment variables** — secret management (Doppler or .env with gitignore)
- [ ] **Webhook secret validation** — for Stripe, Google Calendar push
- [ ] **AI run audit table** — every AI call logged with model, tokens, latency
- [ ] **Rate limiting** — on `/v1/inbox/parse` and `/v1/schedule/plan` endpoints
- [ ] **Backup strategy** — Supabase automated backups, point-in-time recovery enabled

### Product

- [ ] **Design system** — colors, typography (SF Pro + Inter), spacing, motion specs, component states
- [ ] **All 5 views built** — Today, Inbox, Calendar, Projects, Settings
- [ ] **⌘K command palette** — fuzzy search, all actions, keyboard nav
- [ ] **Quick capture flow** — ⌘N + floating button + real-time parse preview
- [ ] **Inbox confirm flow** — inline parse edit → one-tap confirm
- [ ] **Drag-to-reschedule** — on calendar timeline, optimistic UI
- [ ] **AI briefing card** — collapsible, shows top 3 priorities + risks + rationale
- [ ] **AI scheduling rationale** — per-block "why here" explanation
- [ ] **Disruption handling** — amber border + "Replan for me" button when schedule changes
- [ ] **Onboarding** — 3-step (create → connect calendar → set work hours)
- [ ] **Settings pages** — profile, work hours, calendars, notifications, AI toggles, billing
- [ ] **Empty states** — every view has a meaningful empty state (not generic)
- [ ] **Keyboard shortcuts** — full list, `?` to show cheatsheet
- [ ] **Offline read** — PWA loads cached shell when offline
- [ ] **In-app notification center** — bell icon with unread badge + dropdown
- [ ] **Loading skeletons** — not spinners for all async content
- [ ] **Error states** — user-friendly, actionable, not raw error messages

### Legal / Compliance

- [ ] **Terms of Service** — published at `/terms`. Cover: acceptable use, AI advice disclaimer ("AI suggestions are recommendations, not professional advice"), data handling, subscription terms, cancellation policy
- [ ] **Privacy Policy** — published at `/privacy`. Cover: data collected, how it's used, third-party sharing (Google, OpenAI, Stripe), GDPR rights, CCPA rights, data retention, deletion procedure
- [ ] **Cookie consent banner** — if using PostHog cookies or any tracking beyond session. Use CookieBot or similar.
- [ ] **GDPR DPA (Data Processing Agreement)** — Supabase DPA available, accept. Required if serving EU users.
- [ ] **Stripe tax compliance** — Stripe Tax enabled for EU VAT + US state sales tax
- [ ] **AI data retention opt-out** — OpenAI API has data retention setting. Disable training data use for your org. Document this in privacy policy.
- [ ] **Third-party API data processing terms** — Google Calendar API requires showing their data access disclosure. Include in privacy policy.
- [ ] **Cancellation flow** — self-serve cancel in settings. No email required. Reflects in Stripe immediately.
- [ ] **Refund policy** — 7-day refund for annual plans. Stripe refund API. Document it.

### Go-to-Market

- [ ] **Waitlist page** — `/waitlist` or launch page with email capture. Set up before any public launch.
- [ ] **Landing page** — clear tagline ("Your tasks, scheduled. Simply."), 3-step value prop, pricing table, CTA (start free). Live before beta.
- [ ] **Product demo video** — 60–90 sec. Show natural language capture → AI scheduling → calendar. Place on landing page + Product Hunt.
- [ ] **Social accounts** — Twitter/X @getchronos, LinkedIn page. Set up before launch.
- [ ] **Email sequence** — welcome email on signup, onboarding tips (days 1, 3, 7), upgrade nudge (day 14 if active but not paid)
- [ ] **Documentation** — getting started guide (how to connect calendar, how AI scheduling works, keyboard shortcuts). Not docs.ai — just good `help.chronos.ai`.
- [ ] **Product Hunt listing** — draft ready. Submit on formal launch day.
- [ ] **SEO articles** — "Why Motion is too expensive", "Chronos vs Akiflow", "AI task scheduler guide". Publish during Phase 3.
- [ ] **Press kit** — logos, screenshots, one-pager. Make it easy for journalists.
- [ ] **Competitor landing pages** — targeted pages at `/motion-alternative`, `/akiflow-alternative`. SEO + paid.

### Operations

- [ ] **Intercom or Crisp** — in-app chat, support tickets, knowledge base. Set up before beta.
- [ ] **Knowledge base** — help.chronos.ai with top 20 support questions
- [ ] **Billing support process** — who handles billing questions, refund requests, invoice downloads
- [ ] **Onboarding email sequence** — automated via Resend or Postmark: welcome, day 1 (connect calendar), day 3 (first task), day 7 (upgrade prompt if active)
- [ ] **Feature flag system** — LaunchDarkly or Unleash. Use for: new AI model, new UI, Teams tier, pricing changes.
- [ ] **Error budget** — define P0 (fix immediately), P1 (fix within 24h), P2 (fix within sprint). Communicate to users during outages.
- [ ] **Status page** — status.chronos.ai (use Statuspage by Atlassian or similar). Incident history builds trust.
- [ ] **Changelog** — keep a simple `/changelog` page. Shows you're iterating.
- [ ] **Customer escalation path** — email (support@chronos.ai) that routes to you for P0s, to Intercom for P2s.
- [ ] **Invoice generation** — Stripe handles this. No manual invoicing for standard subscribers.
- [ ] **Annual vs monthly tracking** — tag customers by plan type in Stripe + PostHog for cohort analysis.

---

## Critical Infrastructure & Oversight Decisions

*These are the decisions only you (Aaron) can make. They're not implementation details — they're strategic bets that commit capital, time, and architecture direction.*

---

### Where Does the Server Live?

This is not an IT question. It's a cost, compliance, and latency question.

| Option | Best For | Risk |
|--------|----------|------|
| **Vercel (frontend) + Railway (backend)** | Fastest to ship. Railway spins up NestJS container in ~2 min. | Costs scale unpredictably at 1K+ users. Railway cold starts can be slow. |
| **Vercel (frontend) + AWS ECS Fargate (backend)** | Full control, predictable costs, AWS ecosystem. | Steeper learning curve. You manage containers. |
| **Cloudflare Pages + Workers** | Lowest latency globally. Not suited for BullMQ/background jobs. | Requires separate worker for heavy tasks. |
| **DigitalOcean App Platform + Droplet** | Simple, cheap, predictable. $20/mo for solid backend. | Manual ops. No auto-scaling. Good for MVP, bad at scale. |

**Recommendation:** Vercel + Railway for MVP. Graduate to AWS ECS Fargate or DigitalOcean Kubernetes when Railway bill exceeds $150/month. This is a 1-week migration, not a rewrite.

**Aaron decision needed:** Commit to Railway for MVP backend OR go straight to AWS if you have experience there. If you don't, start with Railway — it's the fastest path to a working product.

---

### Database & Storage

| Component | Service | MVP Cost | At 1K Users |
|-----------|---------|----------|-------------|
| PostgreSQL | Supabase | $0 (free tier) | ~$25/mo |
| PostgreSQL | AWS RDS | ~$15/mo | ~$40/mo |
| Redis | Upstash | $0 (free tier) | ~$10/mo |
| Object storage | Cloudflare R2 | $0 (10GB) | ~$5/mo |

**Recommendation:** Supabase (Postgres) + Upstash (Redis) + Cloudflare R2 (files). Graduate to AWS RDS when Supabase bill hits $50/month. One-week migration.

**Aaron decision needed:** Supabase managed convenience OR direct Postgres control (more ops, no vendor lock-in)?

---

### AI Cost Architecture (Critical)

This is the most likely budget surprise. Set controls now.

| AI Action | Model | Est. Cost/User/Mo |
|-----------|-------|-----------------|
| Task parse | Claude Sonnet | ~$0.09 |
| Scheduling decisions | GPT-5.4 | ~$0.72 |
| Daily briefing | GPT-5.4 | ~$0.45 |
| **Total** | | **~$1.26/user/mo** |

At 1,000 paying Pro users: ~$1,260/month in AI costs. That's your main cost driver, not infra.

**Cost controls (mandatory for MVP):**
- Rate limit /v1/inbox/parse to 30 calls/user/day
- Cache parsed tasks — don't re-parse unchanged content
- Cache scheduling decisions for 15 minutes
- AI cost alert at $200/month (when you have ~40+ paying users)

**Aaron decision needed:** Set an AI budget cap in OpenAI + Anthropic dashboards today. Recommended: alert at $200/mo, hard cap at $500/mo.

---

### Domain & Brand

- [ ] Register `chronos.ai` or `chronos.so` NOW. ~$10-20/year. Don't let someone squat on it.
- [ ] Cloudflare for DNS — same account as CDN, one login.
- [ ] Email: `support@chronos.ai` — forward to personal email via Google Workspace or MX routing.

**Aaron decision needed:** Buy the domain today. It's $10 and prevents someone from taking it.

---

### Access Control (Who Can Touch What)

| Access | Who | Notes |
|--------|-----|-------|
| GitHub repo | Aaron + devs | Full access |
| Production infra | Aaron only | Non-negotiable |
| Vercel (can deploy) | Aaron + frontend | No billing access |
| Supabase (admin) | Aaron only | Frontend dev gets service role only |
| Stripe dashboard | Aaron only | Non-negotiable |
| Google Cloud console | Aaron only | API keys + OAuth credentials |
| OpenAI + Anthropic | Aaron only | Restrict org visibility in dashboard |
| Sentry + PostHog | Aaron + devs | Analytics only, no billing |

**Aaron decision needed:** Document any additional access grants here before build starts. No exceptions mid-build.

---

### What You Cannot Delegate

1. **AI cost monitoring** — watch OpenAI/Anthropic dashboards weekly
2. **Stripe billing health** — watch for failed payments, churn, anomalies
3. **Security incidents** — calendar data breach is your legal exposure
4. **Google API compliance** — OAuth consent screen + privacy policy required by Google
5. **Legal review** — Terms of Service + Privacy Policy need lawyer review at 1,000+ users
6. **Infrastructure spend** — set Railway spending limit + AWS budget alert NOW
7. **Product direction** — final call on scope. "We won't build X in MVP" is your job.

---


## Key Open Decisions Table

These are the 7 biggest bets that must be resolved before development starts. Making them now prevents expensive pivots mid-build.

| # | Decision | Recommendation | Why | Risk if Wrong |
|---|----------|----------------|-----|---------------|
| **1** | **Auth: Clerk vs Supabase Auth vs Auth0** | **Clerk** | Fastest time-to-launch with Apple Sign-In built in. Supabase Auth is free but requires more custom work for Apple OAuth. Auth0 is enterprise-priced. | If Clerk raises prices post-scale, migrate to Supabase Auth. It's a 2-week project, not catastrophic. |
| **2** | **AI model strategy: single vs blended** | **Blend GPT-5.4 + Claude** | GPT for scheduling (function calling + structured output), Claude for parsing (nuance extraction). Each is best-in-class for its task. | If costs exceed $4/user/month, add aggressive rate limiting and prompt caching. Monitor weekly in Phase 1. |
| **3** | **Calendar abstraction layer: direct API vs Cronofy** | **Direct Google API for MVP, Cronofy in Phase 2** | Direct API is simpler, cheaper, and gives full control. Cronofy adds overhead before you need unified multi-calendar. | If Outlook integration takes longer than 4 weeks in Phase 2, users will complain. Cronofy is the fallback. |
| **4** | **Native apps: SwiftUI first vs cross-platform** | **SwiftUI first — no question** | Native feel is the product moat vs Motion/Akiflow. React Native would save time now but produce an inferior product that won't retain Apple power users. | iOS dev is expensive and slow. Mitigate by hiring an experienced senior iOS engineer and scoping to 2 screens for MVP. |
| **5** | **Scheduling engine: LLM-driven vs hybrid deterministic** | **Hybrid deterministic + AI assist** | Pure LLM scheduling will hallucinate times and miss deadlines. Deterministic engine enforces constraints; AI suggests and explains. This is the right architecture. | The deterministic scheduling rules are complex to tune. MVP will feel "basic." This is fine — calibrate over 6 months with real user data. |
| **6** | **PWA vs Electron for desktop** | **PWA only** | Electron adds 200MB+ download, security surface, and maintenance burden for no meaningful benefit. PWA is installable, offline-capable, and works across OSes. | If enterprise customers demand native desktop, Electron wrapper is a Phase 3 project. Don't build it before you have the demand. |
| **7** | **Pricing: $15 Pro vs $12 Pro vs freemium limits** | **$15 Pro / $24 Pro Plus, 100-task free cap** | $15 matches Akiflow's old pricing and undercuts Motion. The 100-task free cap creates clear upgrade pressure without feeling cruel. 20 AI parses/month on free tier prevents abuse. | If 100-task cap feels too stingy and triggers backlash, raise to 200. If $15 conversion rate is < 3%, test $12. But don't change before 500+ free users. |

---

*Document compiled from: web-app-spec.md (v1.0), founder-spec.md (v1.0), task-app-planning.md (v2.0)*
*Prepared: 2026-03-20*
