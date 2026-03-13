---
name: code-review-sweep
description: Structured post-change review for correctness, edge cases, missing tests, regressions, and risky patterns. Use when: (1) reviewing code changes before calling them done, (2) catching potential bugs or issues, (3) verifying test coverage.
---

# Code Review Sweep

Systematic code review for quality assurance.

## Review Checklist

### 1. Correctness
- Does the code do what it's supposed to?
- Are edge cases handled?
- Are there any obvious bugs?

### 2. Security
- Any injection vulnerabilities?
- Secrets properly handled?
- Input validation present?

### 3. Performance
- Any obvious inefficiencies?
- N+1 query patterns?
- Unnecessary allocations?

### 4. Testing
- Are there tests?
- Do tests cover edge cases?
- Any missing test scenarios?

### 5. Code Quality
- Consistent style with codebase?
- Clear variable/function names?
- Appropriate abstractions?

### 6. Documentation
- Comments where needed?
- API docs updated?
- README if public API?

### 7. Error Handling
- Errors handled gracefully?
- Proper error messages?
- Logging where appropriate?

## Review Output Format

```
## Review Summary
✓ Passed / ⚠ Issues Found / ✗ Blocking

### Issues
1. [Severity] Description
   - File:line
   - Suggestion

### Recommendations
- Optional improvements

### Test Coverage
- Current: X%
- Recommended additions
```

## Common Patterns to Catch

- TODO comments that should be resolved
- Hardcoded values that should be config
- Missing null checks
- Silent failures
- Inconsistent error handling
