---
name: prospect
description: Research a source and build an extraction playbook for Metaphorex
---

Launch the Prospector agent to research an import source and produce a
playbook, extraction scripts, and sub-issues.

**Usage:**
- `/prospect <issue-url>` — prospect a specific import-project issue
- `/prospect` — pick the next unprospected import-project issue

The Prospector handles both `archive` (finite) and `vein` (ongoing) projects.
It is not involved in `nugget` issues.

Invoke the Prospector agent with the issue URL (or empty for pick-next).
