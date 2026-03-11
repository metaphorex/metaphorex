---
name: smelt
description: Run mechanical cleanup on Miner PRs — validate, normalize, fix formatting
---

Launch the Smelter to process PRs labeled `needs-smelting`.

The Smelter will:

1. Find PRs labeled `needs-smelting` (up to 2 per invocation)
2. Run validation and mechanical checks
3. Push fixup commits for any issues
4. Advance PRs to `ready-for-assay` or flag as `needs-miner-fix`

**Usage:**
- `/smelt` — process all PRs labeled `needs-smelting`
- `/smelt <pr-url>` — process a specific PR

Invoke the Smelter agent with the target (or empty for label-based discovery).
