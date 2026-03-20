# Chronos Web Application — Full Specification

*Web App Spec v1.0 — Built on the Chronos Technical Plan (task-app-planning.md)*
*Date: 2026-03-20*
*Status: Ready for Implementation*

---

## 1. Web App Positioning

The web app is **not** a companion or lite version. It is a first-class product surface alongside iPhone and Mac — accessible from any browser, any OS, any device with internet. Every feature that works on native must work on web, and vice versa.

**Guiding principle:**
> *"If the native app can do it, the web app can do it. The only difference is the container."*

### Platform Tiers

| Surface | Priority | Type |
|---------|----------|------|
| **Web app** | P0 — Primary access | SPA (Single Page App), installable as PWA |
| **iPhone app** | P0 — Mobile capture | Native SwiftUI |
| **Mac app** | P1 — Power users | Native SwiftUI + AppKit |
| **Android** | P2 — future | React Native or native later |

---

## 2. Design Language

### 2.1 Aesthetic Direction
Premium, minimal, Apple-inspired. Light backgrounds with purposeful contrast. Not another dark-mode-only productivity tool. The web app should feel like it belongs next to Linear, Raycast, or Cron — clean, fast, opinionated.

**Color Palette:**
```
--bg-primary:       #FAFAFA
--bg-secondary:     #F5F5F7
--bg-surface:       #FFFFFF
--bg-elevated:      #FFFFFF
--border:           #E5E5E7
--border-subtle:    #F0F0F2

--text-primary:      #1D1D1F
--text-secondary:   #6E6E73
--text-tertiary:    #AEAEB2

--accent:           #007AFF (Apple blue — primary actions)
--accent-hover:     #0071E3
--accent-success:   #34C759
--accent-warning:   #FF9500
--accent-danger:    #FF3B30

--task-scheduled:   #5856D6 (purple)
--task-flexible:    #007AFF (blue)
--task-focus:       #FF9500 (orange)
--task-complete:    #34C759 (green)
```

**Typography:**
- Primary: SF Pro (via font-face: -apple-system, BlinkMacSystemFont)
- Fallback: Inter for non-Apple platforms
- Mono: SF Mono / JetBrains Mono (for timestamps, durations, keyboard shortcuts)
- Scale: 11px / 13px / 15px / 17px / 22px / 28px / 36px

**Spacing System:**
- Base unit: 4px
- Component padding: 8px / 12px / 16px
- Section gaps: 24px / 32px / 48px
- Max content width: 1200px
- Sidebar width: 240px (collapsible)
- Command palette width: 640px

### 2.2 Motion Philosophy
Purposeful, fast, physical. Animations communicate state changes, not decoration.

- **Micro-interactions:** 120-200ms ease-out (button press, hover, toggle)
- **Panel transitions:** 250ms ease-in-out (sidebar open/close, modal)
- **Page transitions:** 300ms ease-out (view switches, navigation)
- **Drag operations:** Real-time, no animation delay (drag task between columns)
- **Loading states:** Skeleton screens, not spinners

### 2.3 Component Standards
All UI components follow a consistent pattern:
- States: default, hover, active, disabled, loading, error
- Focus: visible outline for keyboard navigation (2px accent ring)
- Touch targets: minimum 44x44px on mobile
- Consistent border radius: 6px (inputs), 8px (cards), 12px (modals)

---

## 3. Layout Architecture

### 3.1 Shell Layout

```
┌─────────────────────────────────────────────────────┐
│ [≡] Chronos          [Search ⌘K]    [🔔] [Avatar]   │  ← Top bar (48px)
├────────────┬────────────────────────────────────────┤
│            │                                        │
│  Sidebar   │           Main Content Area            │
│  (240px)   │                                        │
│            │                                        │
│  - Today   │                                        │
│  - Inbox   │                                        │
│  - Calendar│                                        │
│  - Projects│                                        │
│  - Focus   │                                        │
│  - Review  │                                        │
│  ─────────│                                        │
│  - Settings│                                        │
│            │                                        │
└────────────┴────────────────────────────────────────┘
```

### 3.2 Responsive Breakpoints

| Breakpoint | Width | Layout |
|-----------|-------|--------|
| Mobile | < 640px | Bottom tab nav, full-width views |
| Tablet | 640-1024px | Collapsible sidebar, 2-column where needed |
| Desktop | > 1024px | Full sidebar, multi-column layouts |
| Wide | > 1440px | Expanded sidebar, max-width containers |

### 3.3 View Structure

**Today View** (default landing)
- Top: AI briefing card (top 3 priorities, risks, schedule rationale)
- Middle: Vertical timeline with task blocks
- Right panel (desktop): Task detail / quick capture

**Calendar View**
- Month / Week / Day / Agenda toggles
- Unified timeline for all connected calendars
- Task blocks overlaid on availability
- Drag-to-reschedule with snap-to-grid

**Inbox View**
- Natural language captures awaiting confirmation
- AI-suggested parse with confidence indicators
- Bulk actions: confirm all, archive, edit

**Projects View**
- Project list with progress indicators
- Kanban or list toggle per project
- Subtask hierarchy with dependency visualization

**Focus View**
- Active focus block display (full-screen capable)
- Timer integration
- Minimal distractions mode

**Review View** (end of day)
- Completed tasks summary
- Rescheduling suggestions for tomorrow
- AI daily journal entry

---

## 4. Feature Specification

### 4.1 Command Palette (⌘K)

The command palette is the primary interaction pattern for power users on web. It must be fast (<100ms to open), keyboard-first, and capable of anything.

**Capabilities:**
- Quick task capture (enter → parses and creates task)
- Navigation (type view name → jump)
- Task search and action (search task → defer, complete, edit)
- Calendar shortcuts ("block 3pm tomorrow for 1 hour")
- Settings shortcuts (toggle dark mode, change work hours)
- Integrations (connect calendar, invite user)

**Interaction:**
- `⌘K` or `/` to open
- Fuzzy search across all actions
- Recent actions shown by default
- Arrow keys to navigate, Enter to select, Esc to close
- Mouse click on any item to select

**Example entries:**
```
> "Finish Q1 report by Friday need 3 hours"
> /calendar
> "schedule dentist appointment"
> @Sarah tasks
> block 2pm-4pm deep work
```

### 4.2 Quick Capture

**Global quick capture:** floating button (bottom-right) + `⌘N` shortcut + browser extension.

**Flow:**
1. User enters natural language text
2. Real-time parse preview shows as they type
3. AI extracts: title, duration, deadline, project, tags
4. User confirms or edits inline
5. Task created with one Enter keystroke

**Input parsing examples:**
| Input | Parsed |
|-------|--------|
| "Call John Monday 3pm 30min" | title: Call John, Monday 3pm, 30min |
| "Finish deck by Friday needs 3 hours review with Sarah Thursday afternoon" | title: Finish deck, Friday EOD, 3hrs, review Thursday PM |
| "Gym every weekday 7am" | title: Gym, weekdays 7am, recurring |

### 4.3 Calendar Integration

**Supported at launch:**
- Google Calendar (read/write via Google Calendar API)
- Microsoft Outlook (read/write via Microsoft Graph API)

**Web-specific calendar features:**
- Drag-to-create events directly on calendar grid
- Drag-to-reschedule tasks with live calendar update
- Conflict detection with visual warnings
- Availability overlay showing free/busy across all connected calendars
- Subscribe-only calendar feeds (read-only iCal import)

**Two-way sync behavior:**
- Changes in Chronos push to Google/Outlook within 5 seconds
- Changes in Google/Outlook reflect in Chronos via webhook + 60-second polling
- Conflict UI if same event edited in both places simultaneously

### 4.4 Task Management

**Task fields (all accessible, most auto-populated by AI):**
- Title (required)
- Description (optional, markdown supported)
- Status: Inbox → Todo → Scheduled → In Progress → Blocked → Done → Archived
- Duration estimate (minutes)
- Due date / deadline
- Earliest start date
- Priority (1-5 manual, AI score overlay)
- Energy level required (low / medium / high)
- Scheduling flexibility (fixed / flexible / someday)
- Project membership
- Tags
- Recurrence rule (RRULE format)
- Focus block required (boolean — forces 45/60/90min uninterrupted window)
- Preferred time windows

**Task actions:**
- Complete (checkbox, keyboard shortcut `d`)
- Defer → choose new date/time
- Reschedule → drag on calendar or date picker
- Break down → AI subtask generation
- Set priority → 1-5 scale
- Move to project
- Add dependency
- Archive

### 4.5 AI Planning Engine (Web Interface)

**AI Briefing Card (Today view, top):**
```
┌─────────────────────────────────────────────────────┐
│ ☀️ Good morning, Aaron. Here's your plan.            │
│                                                     │
│ 🎯 Top 3 priorities today:                          │
│   1. Finish Q1 deck (due today, 3hrs, high risk)   │
│   2. Review Sarah's changes (follow-up, 45min)     │
│   3. Gym + prep (hard deadline tomorrow AM)        │
│                                                     │
│ ⚠️ 2 schedule risks:                               │
│   - Q1 deck needs 3hrs but only 2.5hrs free        │
│   - Meeting at 2pm pushed focus block to 3:30pm   │
│                                                     │
│ 💡 Suggestion: Split deck into 2hr + 1hr blocks    │
└─────────────────────────────────────────────────────┘
```

**AI Explanations:**
- Every AI-scheduled block shows why: "Scheduled here because your energy peaks at 9-11am and this task is high-effort"
- Hover or click to see reasoning, adjust manually if desired
- All AI decisions are overridable with full user control

**Replanning interface:**
- When a meeting changes, affected tasks highlight with amber border
- Toast notification: "Schedule updated — 2 tasks need replanning"
- One-click "Replan for me" or manual drag to fix

### 4.6 Notifications & Reminders

**Web push notifications (via Service Worker + Web Push API):**
- Daily briefing at configured time (e.g., 8:00 AM)
- Task reminder before block starts (configurable: 5/10/15/30 min)
- Schedule disruption alerts ("Meeting moved — tap to see impact")
- AI daily review prompt (end of day, configurable)

**In-app notification center:**
- Bell icon in top bar with unread count badge
- Notification types: reminders, schedule changes, AI suggestions, teammate activity
- Grouped by time (today, yesterday, earlier)

### 4.7 Real-Time Collaboration

**Shared workspaces (Phase 2+):**
- Multiple users per workspace
- Visible task assignments
- Shared calendar views
- @mentions in task comments
- Activity feed for workspace changes

**Presence indicators:**
- Green dot = active on web / native app
- Show who's viewing a shared task
- Typing indicators in comments

**Permissions model:**
- Owner: full control + billing
- Admin: manage members + all tasks
- Member: create/edit own tasks + view assigned
- Viewer: read-only access

### 4.8 Settings & Preferences

**User preferences:**
- Work hours (start / end)
- Time zone (auto-detect + manual override)
- Working days (which days of week)
- Default task duration
- Focus block default length (45/60/90 min)
- Notification preferences (toggle each type)
- Theme (light / dark / system)

**Calendar settings:**
- Connected accounts list
- Per-calendar visibility toggles
- Sync frequency (real-time / 5min / 15min / manual)
- Default event duration
- Buffer time between events (0 / 5 / 10 / 15 min)

**AI settings:**
- AI auto-schedule: on/off
- AI confidence threshold for auto-action (low / medium / high)
- Show AI reasoning: always / when changed / never
- Daily briefing time
- End-of-day review: on/off

---

## 5. Technical Architecture

### 5.1 Stack (from Technical Plan, confirmed for web)

```
Frontend:
  - Framework: Next.js 15 (App Router)
  - Language: TypeScript (strict mode)
  - UI: React + Tailwind CSS + shadcn/ui primitives
  - State: Zustand (client state) + TanStack Query (server state)
  - Calendar UI: FullCalendar (MVP), custom timeline views (later)
  - Command Bar: cmdk
  - Forms: React Hook Form + Zod
  - Auth: Clerk (fastest secure launch)
  - Real-time: WebSockets via Socket.io or Ably

Backend (shared with native):
  - Runtime: Node.js + NestJS
  - Database: PostgreSQL 16 via Supabase or direct Postgres
  - ORM: Prisma
  - Cache/Queue: Redis + BullMQ
  - Auth: Clerk (JWT validation on backend)
  - Realtime: Ably or native WebSocket via NestJS gateway

Infrastructure:
  - Hosting: Vercel (frontend) + Railway/Render (backend)
  - CDN: Cloudflare (global edge)
  - Monitoring: Sentry (errors) + PostHog (analytics)
  - CI/CD: GitHub Actions
```

### 5.2 PWA Requirements

The web app must be installable and usable offline as a Progressive Web App.

**Required PWA features:**
- `manifest.json` with app name, icons, theme color, display mode (`standalone`)
- Service Worker with Workbox for caching strategies:
  - App shell: cache-first (HTML, CSS, JS, fonts)
  - API calls: network-first with offline fallback
  - Static assets: cache-first with versioning
- Offline page when network unavailable
- Background sync for task actions taken offline

**Install prompt:**
- Browser install banner (custom, not default browser prompt)
- "Install app" in user settings

### 5.3 Performance Targets

| Metric | Target |
|--------|--------|
| First Contentful Paint | < 1.2s |
| Largest Contentful Paint | < 2.0s |
| Time to Interactive | < 3.0s |
| Command palette open | < 100ms |
| Calendar drag response | < 16ms (60fps) |
| Search results | < 200ms |

**Strategies:**
- Route-based code splitting (Next.js automatic)
- Lazy load FullCalendar and heavy views
- Optimistic UI updates for all actions
- Debounced API calls (300ms for search, instant for task actions)
- Preload next likely view (e.g., load today view calendar data on app load)

### 5.4 Security

- All API calls over HTTPS
- JWT validation on every request (Clerk)
- CSRF protection on all mutations
- Content Security Policy (CSP) headers
- Rate limiting on auth and capture endpoints
- Input sanitization on all user content
- No sensitive data in URL parameters or localStorage (tokens in httpOnly cookies only)

---

## 6. Page-by-Page Breakdown

### 6.1 Today Page (`/today`)

**Sections:**
1. **AI Briefing Card** — full width, collapsible
2. **Timeline** — vertical, hour-by-hour, scroll to current time on load
3. **Task Cards** — positioned on timeline at scheduled time
4. **Right Panel** — task detail, quick capture (desktop only, collapsible)

**Interactions:**
- Click task → opens detail panel
- Drag task → reschedule on timeline
- Click empty slot → create task at that time
- Click AI briefing → expand with full rationale
- Swipe task (mobile) → quick actions (complete, defer, edit)

### 6.2 Inbox Page (`/inbox`)

**Layout:** Single-column list, filterable by source

**Item states:**
- Unprocessed (amber left border)
- AI-parsed (shows extracted fields inline)
- Confirmed (blue left border)
- Archived (grey, dismissed)

**Interactions:**
- Click item → expand inline parse preview + edit fields
- "Confirm" button → creates task
- "Edit" → opens full edit form
- Bulk select + confirm/archive

### 6.3 Calendar Page (`/calendar`)

**Views:** Month / Week / Day / Agenda (toggle in top right)

**Timeline elements:**
- Calendar events from connected providers (read from sync)
- Task blocks (created in Chronos)
- Free/busy overlays

**Interactions:**
- Click + drag on empty slot → create task block
- Drag task block → reschedule
- Resize task block → change duration
- Double-click task → open detail
- Click event → show provider event details (read-only)

### 6.4 Projects Page (`/projects`)

**Layout:** Left: project list (filterable/searchable). Right: selected project view.

**Project view modes:**
- List view (tasks as rows)
- Kanban view (columns by status)
- Board view (grouped by tag or assignee)

**Project header:**
- Name, color, description
- Progress bar (% tasks complete)
- Due date (hard deadline)
- Member avatars (if team)

### 6.5 Settings Pages

- `/settings/profile` — name, email, avatar, timezone
- `/settings/work-hours` — hours, days, default duration
- `/settings/calendars` — connected accounts, visibility, sync
- `/settings/notifications` — push + email preferences
- `/settings/ai` — AI behavior toggles
- `/settings/billing` — plan, invoices, upgrade

### 6.6 Auth Pages

- `/login` — Clerk-powered (email, Google, Apple, Microsoft SSO)
- `/signup` — Same options
- `/onboarding` — Connect first calendar, set work hours, import existing tasks

---

## 7. Component Inventory

### Core Components

| Component | States | Notes |
|-----------|--------|-------|
| `TaskCard` | default, hover, dragging, selected, completing, blocked | Drag handle on left |
| `TaskBlock` | scheduled, flexible, focus, complete, overdue, disrupted | Calendar timeline view |
| `InboxItem` | unprocessed, parsed, editing, confirming, archived | Inline parse preview |
| `AIBriefingCard` | loading, ready, expanded, dismissed | Collapsible top of Today |
| `CommandPalette` | closed, open, searching, loading-results | `⌘K` global |
| `QuickCapture` | idle, typing, parsing, preview, confirming | Floating + `⌘N` |
| `CalendarGrid` | month, week, day, agenda views | FullCalendar + custom |
| `ProjectList` | loading, empty, populated | Sidebar project nav |
| `NotificationBell` | unread-count, dropdown-open | Top bar right |
| `SettingsPanel` | section tabs, form states | Slide-in or `/settings` |
| `Modal` | closed, open, loading, error | Centered overlay |
| `Toast` | info, success, warning, error | Bottom-right stack |
| `EmptyState` | no-tasks, no-projects, no-calendar, offline | Contextual illustrations |

---

## 8. Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `⌘K` | Open command palette |
| `⌘N` | Quick capture |
| `⌘/ ` | Focus search |
| `j / ↓` | Next item |
| `k / ↑` | Previous item |
| `Enter` | Open selected |
| `d` | Complete selected task |
| `e` | Edit selected task |
| `←` / `h` | Previous day/week |
| `→` / `l` | Next day/week |
| `t` | Go to Today |
| `c` | Go to Calendar |
| `i` | Go to Inbox |
| `,` | Open Settings |
| `?` | Show all shortcuts |
| `Esc` | Close modal / deselect |

---

## 9. Implementation Phases

### Phase 1: Web Core (MVP)
- [ ] Project setup: Next.js 15, TypeScript, Tailwind, shadcn/ui
- [ ] Auth: Clerk integration (signup, login, session)
- [ ] App shell: sidebar, top bar, routing
- [ ] Task CRUD: create, read, update, delete, complete
- [ ] Basic calendar view: month + week
- [ ] Quick capture with basic parse
- [ ] Google Calendar sync (read)
- [ ] Today view with timeline
- [ ] Settings pages: profile, work hours, calendars
- [ ] PWA: manifest + service worker basic
- [ ] Notifications: in-app only

### Phase 2: AI + Polish
- [ ] AI briefing card
- [ ] AI auto-scheduling
- [ ] Natural language parse (full)
- [ ] Task reschedule drag-and-drop
- [ ] Real-time replanning
- [ ] Full AI explanations per block
- [ ] Push notifications
- [ ] Performance optimization (LCP < 2s)
- [ ] Command palette (full)
- [ ] Inbox with AI parse + confirm

### Phase 3: Collaboration
- [ ] Shared workspaces
- [ ] Team member management
- [ ] Task assignments
- [ ] Activity feed
- [ ] @mentions
- [ ] Presence indicators
- [ ] Permission model

### Phase 4: Scale
- [ ] Microsoft Outlook sync
- [ ] Offline PWA (full)
- [ ] Keyboard shortcut cheatsheet overlay
- [ ] Mobile responsive polish
- [ ] Analytics dashboard
- [ ] Billing + Stripe integration

---

## 10. Open Questions / Decisions Needed

1. **Google Calendar sync approach:** Direct Google Calendar API or Cronofy/Kalendars abstraction layer?
2. **Offline write strategy:** Queue writes locally, sync on reconnect — or restrict web to online-only for MVP?
3. **Real-time sync:** Ably vs. Socket.io vs. Supabase Realtime — which for task/calendar updates?
4. **AI model:** OpenAI (GPT-5.4) vs. Anthropic (Claude Sonnet) for planning engine? Cost/quality tradeoff?
5. **Auth provider:** Clerk vs. Auth0 vs. Supabase Auth — tradeoffs on native + web + Apple Sign-In support?
6. **PWA vs. Electron:** Stick with PWA or build Electron wrapper for desktop download?

---

*Built on: `jarvis-exchange/chronos/task-app-planning.md` (technical plan v2.0)*
