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
   | Needs enrichment | 3 | #1465, #1466, #1467 |
   | Unclaimed issues | 12 | design-patterns (12) |
   | Needs prospecting | 1 | #7 |
   ```

4. If `total_actionable` is 0, say "No actionable work found." and stop.

## Phase B — Dispatch with TaskCreate spinners

For each category of work, dispatch agents using `Agent` with
`run_in_background: true`. Before each dispatch, create a TaskCreate spinner
so the user sees progress.

**Dispatch order and concurrency rules:**

0. **Reclaim stale issues** — if `stale_in_progress` is non-empty, remove
   the `in-progress` label from each stale issue before dispatching miners.
   These are sub-issues that were claimed by a miner but never completed
   (no open PR references them).

   ```bash
   for num in <stale_issue_numbers>; do
     gh api "repos/metaphorex/metaphorex/issues/$num/labels/in-progress" -X DELETE --silent
   done
   ```

   Report in the round summary Highlights:
   "Reclaimed N stale in-progress issues — now available for mining"

   This step runs before miner dispatch so the reclaimed issues appear
   in the `unclaimed` bucket on the next survey.

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
   - **Enrichment** — if `needs_enrichment` is non-empty: TaskCreate
     "Enriching batch...", then dispatch `metaphorex-agents:miner` with
     model `opus`, isolation `worktree`. Pass the first
     `needs_enrichment` issue. Enrichment takes priority over new
     mining — while enrichment batches exist, skip step 6.
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

3. **Friction aggregation** — after all agents in a round complete, scan
   their result text for kaizen issue references (e.g., "#1432"). If 3+
   agents reference the same kaizen issue:
   - Add `priority:high` label if not already set:
     ```bash
     gh issue edit <N> --repo metaphorex/metaphorex --add-label "priority:high"
     ```
   - Add a comment noting the systemic impact:
     ```bash
     gh api repos/metaphorex/metaphorex/issues/<N>/comments \
       -f body="Systemic: hit by N/M agents in round R. Escalating to priority:high."
     ```
   - Include in the round summary Kaizen section:
     "Escalated: #1432 (worktree confusion) — hit by 5/5 miners this round"

4. **Approved PRs auto-merge.** The `auto-merge.yml` workflow handles merging
   when the Assayer labels a PR `approved`. Pitboss does not merge PRs.
   If a PR is stuck (CI failing, merge conflict), the workflow will not merge
   it — check the PR's status checks for details.

5. **New mining work** — only if:
   - No `in_progress` items exist AND
   - `unclaimed` issues exist AND
   - `needs_enrichment` is empty (enrichment takes priority over mining)
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

After all agents in a round complete, print a round summary with three
sections: Work, Highlights, and Kaizen.

```
## Round N Complete

### Work
- Smelted: PR #55 → needs-assay
- Assayed: PR #48 → approved + auto-merge
- Mined: 5 issues → PR #123 opened
- Remaining: 12 unclaimed issues

### Highlights
- (any bugs fixed and pushed to main this round)
- (any stale issues reclaimed, with before/after counts)
- (any structural improvements made to scripts or agent prompts)
- (if nothing notable: "Routine round, no structural changes.")

### Kaizen
- Open: N issues — #1451 (kaizen feedback loops), #1432 (worktree confusion)
- Filed this round: #1449 (missing playbook details)
- Resolved this round: #1369, #1370, #1371 (survey.py fixes → commit abc123)
- (if no kaizen activity: "No kaizen activity this round.")
```

**Highlights rules:**
- Only include genuinely notable items — not every agent completing normally
- Always include before/after metrics when fixing pipeline blockages
  (e.g., "Reclaimed 187 stale issues: unclaimed went 0 → 188")
- When pushing fixes to main, name the commit and what it changes
- When closing kaizen issues, link the fix and describe the impact

**Kaizen rules:**
- Read `kaizen_open` from the survey output each round
- Show the open count + first 3 issue numbers/titles
- Track which kaizen issues were filed or resolved this round
- When resolving kaizen, always describe what the operator can expect
  to see differently in future runs

Then loop back to **Phase A** (sync + survey). The sync step pulls any PRs
that merged during this round, so the next round works from fresh main.
If `total_actionable` is 0 after survey, print a final summary and stop.

**Do NOT stop early.** The only valid termination condition is
`total_actionable == 0`. Do not apply cost reasoning, session-length
heuristics, or "diminishing returns" logic. The user controls budget
externally; the pipeline runs until idle.

## Session-end summary

When `total_actionable` reaches 0 (or the session ends), print a final
summary covering the entire session:

```
## Session Complete

### Production
- Rounds: N
- PRs opened: N (list PR numbers)
- Entries enriched: ~N
- New entries created: ~N
- Duplicates closed: N
- Projects surveyed/approved: N
- Sub-issues created: N

### Improvements Made
- (list each structural fix with before/after impact)
- Example: "Fixed survey.py (3 bugs) → unclaimed went 0 → 188"
- Example: "Reclaimed 187 stale in-progress issues"

### Kaizen Filed
- #NNNN: title (priority)
- #NNNN: title (priority)

### Kaizen Resolved
- #NNNN: title — fixed via commit/PR, impact description

### Open Kaizen Backlog
- N issues remain open (list top 5 by priority)
```

Track these metrics incrementally as the session progresses. Keep running
counters for PRs opened, mappings created, kaizen filed/resolved.

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

## Kaizen reporting

When filing improvement or friction issues during a session, always use the
kaizen label namespace — never bare `bug` or `enhancement`:

```bash
gh issue create --repo metaphorex/metaphorex \
  --label "kaizen:pipeline" \
  --title "kaizen: <short description>" \
  --body "<description>"
```

Use `kaizen:pipeline` for agent prompts, orchestration, scripts, merge flow.
Use `kaizen:content` for schema, validation, taxonomy issues.
Search for duplicates first: `gh issue list -R metaphorex/metaphorex --label kaizen:pipeline --state open`
