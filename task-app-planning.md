# 🚀 Project: AI Task Management App - "Chronos"

*Planning Document v1.0*
*Created: 2026-03-10*
*Status: RESEARCH COMPLETE - AWAITING APPROVAL*

---

## Executive Summary

**Project Goal:** Build the ultimate AI-powered task management application that surpasses Motion and Akiflow with groundbreaking UI/UX, native iPhone/Mac apps, and unparalleled automation.

**Current Market Gap:**
- Motion: All-in-one but expensive, overwhelming features, lacks native Mac/iPhone
- Akiflow: Good time-blocking but limited AI, no native apps
- Neither delivers the "Apple-designed" experience users crave

**Our Opportunity:** Combine the best of both + native apps + Apple-level UX + aggressive AI automation

---

## 📊 Competitive Analysis

### Motion (usemotion.com)

**Strengths:**
- ✅ AI Task Planner - auto-prioritizes urgent/important
- ✅ AI Project Manager - generates projects in seconds
- ✅ AI Meeting Notetaker - transcribes, summaries, action items
- ✅ AI Calendar Assistant - auto-schedules your day
- ✅ AI Docs - creates tasks from notes automatically
- ✅ Integrations: Google Meet, Gmail, Outlook, Siri, HubSpot, Salesforce
- ✅ SOC 2 Type 2 security

**Weaknesses:**
- ❌ No native Mac app (web-only)
- ❌ No native iPhone app
- ❌ Expensive ($20-30+/month)
- ❌ Feature overload - can feel overwhelming
- ❌ UI feels "enterprisey" not premium consumer

### Akiflow (akiflow.com)

**Strengths:**
- ✅ Excellent time-blocking UX
- ✅ Natural language task entry
- ✅ Command bar for quick actions
- ✅ Daily rituals (planning/shutdown)
- ✅ Focus Mode
- ✅ Stats and analytics
- ✅ Mobile app (iOS)
- ✅ Reasonable pricing (~$15/month)

**Weaknesses:**
- ❌ Limited AI features (mostly calendar sync)
- ❌ No native Mac app
- ❌ No real AI prioritization
- ❌ Basic automation
- ❌ No project management features

---

## 🎯 Target User Profile

**Primary:** Aaron Maziarz
- Tech-savvy power user
- Currently using Akiflow
- Wants to leave Akiflow for something better
- Values: Clean UI, automation, native apps, Apple-quality design

**Secondary:** Professionals who want:
- AI-powered scheduling (like Motion's auto-schedule)
- Time-blocking (like Akiflow)
- Native Mac + iPhone apps
- Premium Apple-level UX
- Full user control with AI assistance
- Privacy-focused

---

## 🏗️ Product Requirements

### Phase 1: Core Platform

#### 1.1 Task Management
- [ ] Create tasks with natural language ("Call John Monday 3pm for 1 hour")
- [ ] Task fields: title, description, duration, priority, deadline, recurrence, status, tags, project
- [ ] Smart prioritization (AI analyzes urgency, importance, deadlines)
- [ ] Task locking to specific calendars
- [ ] Recurring tasks (daily, weekly, monthly, yearly, custom)
- [ ] Task history / audit log
- [ ] Bulk actions

#### 1.2 Calendar Integration
- [ ] Google Calendar sync (two-way)
- [ ] Outlook Calendar sync (two-way)
- [ ] Apple Calendar sync (iCloud)
- [ ] Multiple calendar support
- [ ] Calendar conflict detection
- [ ] Unified calendar view
- [ ] Event creation with details

#### 1.3 Time Blocking
- [ ] Drag & drop time slots
- [ ] Time slot customization (color, project, recurrence)
- [ ] Focus blocks
- [ ] Focus Mode (distraction-free)
- [ ] Automatic schedule optimization

#### 1.4 AI Core Engine
- [ ] **Auto-Scheduler:** Analyze tasks, deadlines, preferences → create optimal schedule
- [ ] **Smart Prioritization:** AI scores tasks based on urgency, importance, context
- [ ] **Re-planning:** Automatically re-plan when meetings run late or priorities shift
- [ ] **Deadline Awareness:** Distinguish "do date" from "due date"
- [ ] **Context Awareness:** Knows your meetings, energy levels, work patterns
- [ ] **Learning:** Improves suggestions based on your behavior

### Phase 2: Collaboration & Communication

#### 2.1 Meeting Integration
- [ ] Zoom integration
- [ ] Google Meet integration
- [ ] Microsoft Teams integration
- [ ] Meeting notetaker (AI transcription)
- [ ] Action item extraction
- [ ] Auto-follow-up drafts

#### 2.2 Team Features
- [ ] Shared calendars
- [ ] Team availability
- [ ] Booking links
- [ ] Team billing

### Phase 3: Documents & Workflows

#### 3.1 Docs
- [ ] Rich text docs
- [ ] AI drafting assistant
- [ ] Auto-create tasks from notes
- [ ] Wiki/project docs

#### 3.2 Workflows
- [ ] Visual workflow builder
- [ ] SOP → workflow conversion
- [ ] Automated sequences

---

## 📱 Native Apps (CRITICAL FEATURE)

### iPhone App
- [ ] Native Swift/SwiftUI
- [ ] Calendar view (day, week, month)
- [ ] Task creation (natural language)
- [ ] Push notifications
- [ ] Widgets
- [ ] Siri integration
- [ ] Focus Mode
- [ ] Offline support

### Mac App
- [ ] Native Swift/SwiftUI + AppKit
- [ ] Menu bar companion (quick tasks)
- [ ] Calendar widget
- [ ] Native notifications
- [ ] Spotlight integration
- [ ] Keyboard-first navigation
- [ ] Drag & drop support
- [ ] Handoff with iPhone

---

## 🎨 UI/UX Requirements ("Apple-2080" Vision)

### Design Principles
1. **Glassmorphism** - Frosted glass effects, subtle blur
2. **Spatial Depth** - Layered interface with depth
3. **Fluid Animations** - 60fps, spring physics, micro-interactions
4. **Dark Mode First** - OLED blacks, accent colors
5. **Typography** - SF Pro, clear hierarchy
6. **Minimal Chrome** - Content over controls

### Color Palette
- **Background:** #000000 (OLED black)
- **Surface:** rgba(255,255,255,0.08) (glass)
- **Primary:** #2997ff (Apple blue)
- **Accent:** #bf5af2 (purple), #30d158 (green)
- **Text Primary:** #ffffff
- **Text Secondary:** rgba(255,255,255,0.6)

### Key UI Components
- [ ] Floating command bar (⌘K style)
- [ ] Collapsible sidebar
- [ ] Calendar with fluid transitions
- [ ] Task cards with gesture support
- [ ] Smart notification center
- [ ] Focus mode overlay

---

## 🔧 Technical Architecture

### Stack
- **Frontend (Web):** React + TypeScript + Vite
- **Mobile:** Swift/SwiftUI (iOS), SwiftUI (Mac)
- **Backend:** Node.js + Supabase (or Firebase)
- **AI:** OpenAI GPT-5 + Claude for reasoning
- **Calendar API:** Google Calendar API, Microsoft Graph API
- **Real-time:** WebSocket + Supabase Realtime

### Data Model
```
User
├── CalendarAccounts (Google, Outlook, iCloud)
├── Tasks
│   ├── title, description, duration
│   ├── priority (AI-calculated)
│   ├── deadline, doDate
│   ├── recurrence, status, tags
│   └── timeSlots
├── Projects
├── Documents
├── Meetings
└── TeamSettings
```

### Security
- [ ] SOC 2 Type 2 equivalent
- [ ] End-to-end encryption for sensitive data
- [ ] OAuth for calendar integrations
- [ ] GDPR compliant

---

## 💰 Pricing Model (Post-MVP)

| Tier | Price | Features |
|------|-------|----------|
| Free | $0 | Basic tasks, 1 calendar, manual scheduling |
| Pro | $12/mo | AI scheduling, all calendars, docs |
| Team | $25/user | Team features, shared calendars |
| Enterprise | Custom | SSO, advanced security, dedicated support |

*Note: Free tier competitive with Akiflow, Pro with Motion but better*

---

## 📋 Development Phases

### Phase 1: MVP (3-4 months)
- [ ] Core task management
- [ ] Google Calendar sync
- [ ] AI auto-scheduler (basic)
- [ ] Web app (responsive)
- [ ] iPhone app (basic)

### Phase 2: Polish (2 months)
- [ ] Mac app
- [ ] More integrations
- [ ] AI improvements
- [ ] Performance optimization

### Phase 3: Scale (ongoing)
- [ ] Team features
- [ ] Advanced AI
- [ ] Enterprise features

---

## 🤔 Questions for Aaron

1. **Budget:** What's the development budget? (Native apps significantly increase cost)
2. **Timeline:** When do you want to launch?
3. **Priorities:** What's most important - speed to market or feature completeness?
4. **Platforms:** iPhone + Mac only, or Android + Windows too?
5. **Monetization:** One-time purchase or subscription?
6. **Existing integrations:** What other tools must it connect to? (Make, Monday, etc.)

---

## ✅ Next Steps

**Waiting on Aaron's approval before:**
1. Creating detailed technical spec
2. Architecture diagrams
3. UI/UX wireframes
4. Development timeline
5. Cost estimation

---

*This document lives in jarvis-exchange/task-app-planning.md*
*Use this for planning only - no development until approved*