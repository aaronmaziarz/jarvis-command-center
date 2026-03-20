# Chronos - Founder Spec

*The AI Task Management App That Puts Users First*

**Version:** 1.0  
**Date:** 2026-03-11  
**Status:** Draft - Ready for Review

---

## The Problem

Current task management apps force a choice:

| App | What's Wrong |
|-----|-------------|
| **Motion** | Expensive, feature-bloated, pushes unwanted AI, removed free features |
| **Akiflow** | No native Mac app, limited AI, removed free tier |
| **Everything Else** | Manual scheduling only - no AI help |

Users just want their tasks scheduled. They're tired of:
- 🤖 AI features they didn't ask for
- 💰 Hidden price increases
- 📱 Missing native apps (Mac/iPhone)
- 📚 Steep learning curves
- 😤 Being forced to upgrade

---

## Our Solution: Chronos

**Slogan:** "Your tasks, scheduled. Simply."

Chronos is an AI-powered task management app that:
1. **Schedules automatically** - But gives you full control
2. **Has native apps** - Mac + iPhone (not just web)
3. **Transparent pricing** - No hidden changes
4. **Optional AI** - AI assists, doesn't override
5. **Social planning** - Plan with friends (unique!)

---

## Market Opportunity

### The Problem We Solve
- **Motion users** are looking for alternatives (see: Reddit threads titled "ditching Motion")
- **Akiflow users** want native apps and more AI
- **Nobody** has social planning + flexible event types

### Target Users
1. **Productivity power users** - Want AI scheduling without bloat
2. **Professionals** - Need native Mac + iPhone apps
3. **Teams** - Want to coordinate schedules with colleagues
4. **Casual users** - Need a generous free tier

### Market Size
- Task management: $4.5B market (2024)
- AI productivity tools: Growing 25% annually
- Motion costs $20-30/mo - users are unhappy paying more for less

---

## Key Features (MVP)

### Core (Must Have)
1. **AI Auto-Scheduler**
   - Add tasks with duration + deadline
   - AI automatically schedules on calendar
   - Respects work hours and preferences

2. **Calendar Integration**
   - Google Calendar (two-way sync)
   - Outlook Calendar
   - Apple iCloud/Calendar

3. **Flexible Event Types**
   - **Scheduled** - Fixed, cannot move
   - **Flexible** - Can move, prefer not to
   - **Task** - AI can reschedule freely

4. **Task Management**
   - Natural language entry ("Call John Monday 3pm")
   - Recurring tasks
   - Projects/categories
   - Tags and priorities

### Differentiators
5. **Social Planning** (Unique!)
   - Invite friends to plan something
   - See if friend's free (without details)
   - Friend receives inbox request
   - They can accept/adjust/suggest alternative

6. **Smart Inbox**
   - Tasks from integrations land here
   - AI suggests optimal schedule time
   - One-click approve or adjust

7. **User Controls**
   - Work hours (when AI can schedule)
   - Hard vs soft deadlines
   - Focus time protection
   - Maximum tasks per day
   - Buffer time between events

### Native Apps (Critical)
8. **iPhone App** - Native Swift/SwiftUI
9. **Mac App** - Native Swift/SwiftUI + AppKit

---

## Product Vision

### Phase 1: MVP (3-4 months)
- [ ] **Web app** (full Chronos web spec — see `chronos/specs/web-app-spec.md`)
  - Command palette, quick capture, today/calendar/inbox/projects views
  - Task CRUD with natural language parse
  - Google Calendar sync (two-way)
  - AI auto-scheduling + briefing card
  - PWA installable, offline-capable
- [ ] Core task management (via web app)
- [ ] Google Calendar sync
- [ ] Basic AI auto-scheduler
- [ ] iPhone app (basic capture + task list)

### Phase 2: Polish (2 months)
- [ ] More calendar integrations
- [ ] Mac app
- [ ] Social planning (beta)
- [ ] Smart inbox

### Phase 3: Scale
- [ ] Team features
- [ ] Enterprise SSO
- [ ] Advanced analytics

---

## Pricing Strategy

| Tier | Price | Features |
|------|-------|----------|
| **Free** | $0 | 50 tasks, 1 calendar, manual scheduling |
| **Pro** | $12/mo | Unlimited tasks, all calendars, AI scheduling, smart inbox |
| **Team** | $25/user | Shared calendars, team features, booking links |
| **Enterprise** | Custom | SSO, dedicated support, advanced security |

**Philosophy:**
- Generous free tier (unlike Akiflow who removed theirs)
- Transparent pricing (unlike Motion who hides increases)
- No forced upgrades (unlike Motion's "AI Pro")

---

## Competitive Advantages

| Feature | Motion | Akiflow | Chronos |
|---------|--------|---------|---------|
| Auto-schedule | ✅ (paid) | ❌ | ✅ (free+) |
| Native Mac | ❌ | ❌ | ✅ |
| Native iPhone | ❌ | ✅ | ✅ |
| Social planning | ❌ | ❌ | ✅ |
| Transparent pricing | ❌ | ❌ | ✅ |
| Flexible events | ❌ | ❌ | ✅ |
| Free tier | ❌ | ❌ | ✅ |

---

## Technical Stack

### Frontend
- **Web:** React + TypeScript + Vite
- **iPhone:** Swift/SwiftUI
- **Mac:** Swift/SwiftUI + AppKit

### Backend
- **API:** Node.js + Express
- **Database:** Supabase (PostgreSQL)
- **Real-time:** Supabase Realtime

### AI
- **Scheduling:** GPT-5.4 + Claude for reasoning
- **Tasks:** Efficient models (MiniMax, Qwen)

### Integrations
- Google Calendar API
- Microsoft Graph API (Outlook)
- Apple Calendar (via CalDAV)

---

## Success Metrics

### Year 1 Targets
- **10,000** free users
- **1,000** Pro subscribers
- **500** Team customers
- **$120K** ARR

### Key Indicators
- Daily active users (DAU)
- Tasks scheduled via AI
- User retention (monthly)
- Net Promoter Score (NPS)
- Support ticket volume

---

## Risks & Mitigation

| Risk | Mitigation |
|------|------------|
| AI scheduling not good enough | Start simple, iterate based on feedback |
| No market fit | Run user interviews, beta program |
| Competition | Focus on where others fail (native apps, social) |
| Pricing pressure | Value-based pricing, not race to bottom |

---

## Next Steps

1. **Approve this spec** - Confirm direction
2. **Create engineering PRD** - Technical breakdown
3. **Set up development environment** - Repo, tools
4. **Build MVP** - Start with core scheduling + calendar
5. **Beta launch** - 100 users for feedback
6. **Iterate** - Based on real usage

---

## Appendix

### Research Sources
- `chronos/research/competitive-feedback.md` - Motion & Akiflow user complaints
- `chronos/planning/chronos-plan-v2.md` - Detailed technical plan

### Team Needs
- iOS Developer (Swift/SwiftUI)
- Full-stack Developer (Node.js + React)
- Designer (Apple-quality UX)

---

*This is a living document. Update as we learn more.*

**Questions?** Let's discuss before moving to engineering.
