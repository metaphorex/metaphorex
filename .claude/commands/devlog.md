---
description: Generate a weekly devlog entry from session logs, git history, and ops data
argument-hint: [YYYY-WNN]
---

# Devlog

Use the `devlog` skill to generate a weekly development log entry.

Target week (if provided): $ARGUMENTS

If no week was provided, default to the most recent completed week.

Follow the devlog skill's three-phase workflow:
1. Extract week context using the week-extractor agent
2. Present summary and ask for corrections/additions
3. Synthesize the devlog draft to docs/devlog/
