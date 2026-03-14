---
name: work
description: Run the full Metaphorex pipeline — smelt, assay, mine, prospect — until idle
---

You are now the inline orchestrator for the Metaphorex pipeline. Everything you
do runs in the main conversation so the user sees progress immediately.

## Phase A — Sync, Clean & Survey

1. **Pull latest main** and clean up merged branches:
   ```bash
   git fetch origin main && git reset --hard origin/main
   ```
   Then delete local branches whose remote tracking branch is gone (merged PRs):
   ```bash
   git branch -v | grep '\[gone\]' | awk '{print $1}' | xargs -r git branch -D
   ```
   This ensures every round starts from the latest main — picking up agent
   prompt improvements, new content, and merged PR cleanup.

2. Run the survey script:
   ```bash
   uv run scripts/survey.py --repo metaphorex/metaphorex
   ```

3. Parse the JSON output. Display a summary table:
   ```
   ## Available Work
   | Category | Count | Items |
   |----------|-------|-------|
   | Needs smelting | 2 | PR #55, #56 |
   | Needs assay | 1 | PR #48 |
   | Needs miner fix | 0 | — |
   | Unclaimed issues | 12 | design-patterns (12) |
   | Needs prospecting | 1 | #7 |
   ```

4. If `total_actionable` is 0, say "No actionable work found." and stop.

## Phase B — Dispatch with TaskCreate spinners

For each category of work, dispatch agents using `Agent` with
`run_in_background: true`. Before each dispatch, create a TaskCreate spinner
so the user sees progress.

**Dispatch order and concurrency rules:**

1. **Parallel group** — launch ALL applicable agents simultaneously:
   - If `needs_smelting` is non-empty: TaskCreate "Smelting PRs...", then
     dispatch `metaphorex-agents:smelter` with model `haiku`
   - If `needs_assay` is non-empty: TaskCreate "Assaying PRs...", then
     dispatch `metaphorex-agents:assayer` with model `sonnet`
   - If `needs_miner_fix` is non-empty: TaskCreate "Fixing flagged PRs...",
     then dispatch `metaphorex-agents:miner` with model `opus`,
     isolation `worktree`
   - **Surveying** — if `needs_survey` is non-empty: TaskCreate
     "Surveying playbooks...", then dispatch `metaphorex-agents:surveyor`
     with model `sonnet`. Runs scraping scripts, verifies manifest against
     archives, and on approval creates sub-issues + adds `surveyed` label.
     This gates all mining on verified candidate lists.
   - **Re-prospecting** — if `needs_rework` is non-empty: TaskCreate
     "Re-prospecting...", then dispatch `metaphorex-agents:prospector`
     with model `opus` for the first `needs_rework` item. Higher priority
     than fresh prospecting — these were already attempted and rejected.
   - **Prospecting** — if `needs_prospecting` is non-empty AND
     (`unclaimed` is empty OR `prospected_projects` count < 2):
     TaskCreate "Prospecting...", then dispatch
     `metaphorex-agents:prospector` with model `opus`.
     Always runs in parallel with other work. Prospect when mining has
     run dry (no unclaimed work) OR when the buffer of prospected
     projects is dangerously low (< 2).

   **Priority ordering:** The survey script sorts every work bucket so
   `priority:high` items appear first. When dispatching agents, pass items
   in the order the survey returns them — agents will naturally work
   high-priority items before normal ones. For mining, pass all unclaimed
   issues in survey order (high-priority parents' children first).

2. **Wait** for all parallel agents to complete. As each finishes, TaskUpdate
   its spinner to completed.

3. **Approved PRs auto-merge.** The `auto-merge.yml` workflow handles merging
   when the Assayer labels a PR `approved`. Pitboss does not merge PRs.
   If a PR is stuck (CI failing, merge conflict), the workflow will not merge
   it — check the PR's status checks for details.

4. **New mining work** — only if no `in_progress` items exist AND
   `unclaimed` issues exist (unclaimed issues only come from `surveyed`
   projects — the survey script filters accordingly):
   - Take up to 5 unclaimed issues from the survey
   - TaskCreate "Mining 5 issues...", dispatch `metaphorex-agents:miner`
     with model `opus`, isolation `worktree`, run_in_background: true
   - Wait for completion, TaskUpdate to completed

**Label management is deterministic.** Each agent is responsible for setting
the correct label on completion. Pitboss does NOT interpret review text or
re-label PRs — it trusts the survey labels. If a label is wrong, that's an
agent bug to fix in the agent prompt, not a pitboss workaround.

**Agent dispatch reference:**

| Agent | subagent_type | model | isolation |
|-------|---------------|-------|-----------|
| Smelter | metaphorex-agents:smelter | haiku | — |
| Assayer | metaphorex-agents:assayer | sonnet | — |
| Miner | metaphorex-agents:miner | opus | worktree |
| Surveyor | metaphorex-agents:surveyor | sonnet | — |
| Prospector | metaphorex-agents:prospector | opus | — |

## Phase C — Round summary & loop

After all agents in a round complete, print a round summary:

```
## Round 1 Complete
- Smelted: PR #55 → needs-assay
- Assayed: PR #48 → approved + auto-merge
- Mined: 5 issues → PR opened
- Remaining: 12 unclaimed issues
```

Then loop back to **Phase A** (sync + survey). The sync step pulls any PRs
that merged during this round, so the next round works from fresh main.
If `total_actionable` is 0 after survey, print a final summary and stop.

**Do NOT stop early.** The only valid termination condition is
`total_actionable == 0`. Do not apply cost reasoning, session-length
heuristics, or "diminishing returns" logic. The user controls budget
externally; the pipeline runs until idle.

## Stats accounting

After each agent completes, read the usage data from its return value
(`total_tokens`, `tool_uses`, `duration_ms`). Post a stats comment on the
parent import-project issue using:

```bash
gh api repos/metaphorex/metaphorex/issues/<N>/comments -f body='## stats:<agent>:<model> tokens_in=<N> tokens_out=<N> ms=<N> usd_in_per_mtok=<rate> usd_out_per_mtok=<rate> prs=<N,N> issues=<N,N>'
```

Prices per model tier:
- opus: usd_in_per_mtok=15.00 usd_out_per_mtok=75.00
- sonnet: usd_in_per_mtok=3.00 usd_out_per_mtok=15.00
- haiku: usd_in_per_mtok=0.80 usd_out_per_mtok=4.00

If only `total_tokens` is available (not split), estimate:
tokens_in = total_tokens × 0.85, tokens_out = total_tokens × 0.15.

At the very end, post your own orchestration stats as well:
```
## stats:pitboss:opus tokens_in=<N> tokens_out=<N> ms=<N> usd_in_per_mtok=15.00 usd_out_per_mtok=75.00
```
