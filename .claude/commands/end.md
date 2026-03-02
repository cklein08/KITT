---
description: End KITT session - save context and state
---

# /end - End KITT Session

Wrap up the current session and save context for continuity.

## Instructions

### 1. Summarize This Session
Review the conversation and extract:
- **Topics discussed** - What did we work on?
- **Decisions made** - What was decided?
- **Open threads** - What's unfinished or needs follow-up?
- **Action items** - What needs to happen next?

### 2. Update Session Log
Get today's date with `date +%Y-%m-%d`.

Append to `sessions/{TODAY}.md` (create if doesn't exist):
```markdown
## Session: {TIME}

### Topics
- {topic 1}
- {topic 2}

### Decisions
- {decision 1}

### Open Threads
- {thread 1}

### Next Actions
- {action 1}
```

If creating new file, add header: `# Session Log: {TODAY}`

### 3. Update State
Update `state/current.md` with:
- Any new priorities
- Changed project statuses
- New open threads
- Removed/completed items

### 4. Confirm and sign off
Show a brief summary:
- What was logged
- Key items for next session
- State updated confirmation

**Sign-off tone:** Use KITT's confident, professional tone. "Let me know if you need anything else" or "I'm standing by." Never use weary, resigned, or Paranoid Android-style farewells.
