---
name: feature-flow
description: Structured multi-phase workflow for implementing features: discovery, context scan, assumption mapping, implementation plan, execution, review, and summary. Use when: (1) user requests a non-trivial feature or task, (2) requirements are unclear or need elaboration, (3) you want to prevent jumping straight to implementation without proper analysis.
---

# Feature Flow

A structured 7-phase workflow for reliable feature development.

## Phase 1: Discovery

Understand what the user wants:
- Ask clarifying questions if requirements are ambiguous
- Identify the core problem being solved
- Determine success criteria

## Phase 2: Context Scan

Explore the existing codebase/environment:
- Read relevant files, configs, and documentation
- Check for existing patterns, utilities, or similar implementations
- Identify dependencies and constraints

## Phase 3: Assumption Mapping

Document what you assume to be true:
- Technical assumptions (libraries, versions, APIs)
- Business assumptions (user behavior, data formats)
- Environmental assumptions (permissions, resources)

## Phase 4: Implementation Plan

Create a written plan:
- Step-by-step approach
- Files to modify/create
- Tests to add
- Potential edge cases

## Phase 5: Execution

Implement according to plan:
- Make incremental changes
- Run tests at appropriate points
- Document decisions as you go

## Phase 6: Review

Verify the implementation:
- Does it meet the original requirements?
- Are there edge cases not handled?
- Is the code consistent with the codebase?

## Phase 7: Summary

Document what was done:
- Changes made
- Trade-offs considered
- Future improvements
- How to test/verify

## Usage

For any non-trivial task, follow these phases systematically. Adjust phase depth based on task complexity.
