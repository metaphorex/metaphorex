---
name: mine
description: Extract mappings — from a playbook, a nugget, or the next available issue
---

Launch the Miner agent to extract mapping entries.

**Usage:**
- `/mine <project-name>` — mine from an approved playbook
- `/mine <issue-url>` — mine a specific issue (nugget or sub-issue)
- `/mine` — pick the next available work (nuggets first, then archive, then vein)

The Miner handles three types of work:
- **Nuggets** — standalone one-off metaphors, no playbook needed
- **Archive sub-issues** — follows the project playbook
- **Vein sub-issues** — follows the project playbook with more judgment

When picking next, the Miner claims the issue with an `in-progress` label
before starting work.

Invoke the Miner agent with the target (or empty for pick-next).
