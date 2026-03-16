# Kaizen Feedback Loops Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Make the kaizen system visible and self-reinforcing — pitboss uses correct labels, round summaries highlight improvements, survey surfaces the kaizen backlog, and close-the-loop reporting shows the operator what changed.

**Architecture:** Five incremental changes across two files (`work.md`, `survey.py`) plus label hygiene. Each task is independently valuable and can ship alone. No new files, no new dependencies.

**Tech Stack:** Markdown (work.md), Python (survey.py), GitHub CLI (label ops)

---

### Task 1: Pitboss Kaizen Labeling Rule

**Why:** The pitboss filed 5/8 kaizen issues this session with wrong labels (`bug`, `enhancement`), making them invisible to `digest.py` kaizen_backlog(). One-line fix, immediate impact.

**Files:**
- Modify: `.claude/commands/work.md:111-131` (Phase C section)

**Step 1: Add kaizen labeling rule to work.md**

Insert after the "Stats accounting" section (after line 153), a new section:

```markdown
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
```

**Step 2: Verify the instruction is reachable**

Run: `grep -c "kaizen:pipeline" .claude/commands/work.md`
Expected: at least 2 matches (the label and the search command)

**Step 3: Commit**

```bash
git add .claude/commands/work.md
git commit -m "kaizen: add pitboss kaizen labeling rules to /work command"
```

**Human verification:** Read the new section in work.md — does it match the pattern used in `.claude/agents/miner.md` lines 154-179?

---

### Task 2: Survey Surfaces Kaizen Backlog

**Why:** The survey currently returns zero information about kaizen issues. The pitboss can't report what it can't see. Adding a `kaizen_open` field to survey output makes the backlog visible in every round's summary table.

**Files:**
- Modify: `scripts/survey.py:84-284` (survey function)
- Test: run `uv run scripts/survey.py --repo metaphorex/metaphorex` and check output

**Step 1: Write a manual test expectation**

Run the survey and confirm kaizen issues are NOT in the output:
```bash
uv run scripts/survey.py --repo metaphorex/metaphorex | python3 -c "import json,sys; d=json.load(sys.stdin); print('kaizen_open' in d)"
```
Expected: `False`

**Step 2: Add kaizen query to survey.py**

In the `survey()` function, after the existing `pr_in_progress` query (line 108), add a new concurrent query:

```python
    kaizen_issues = gh_query([
        "issue", "list", "-R", repo,
        "--label", "kaizen:pipeline,kaizen:content",
        "--state", "open",
        "--json", "number,title,labels",
        "--limit", "20",
    ])
```

Then after the existing `collect()` calls (after line 120), add:

```python
    kaizen_open = [{"number": i["number"], "title": i["title"]} for i in collect(kaizen_issues)]
```

Finally, add `"kaizen_open": kaizen_open,` to the result dict (after line 287, the `stale_in_progress` line). Do NOT add kaizen_open to `total_actionable` — kaizen issues are informational, not dispatched work.

**Step 3: Run the survey and verify kaizen appears**

```bash
uv run scripts/survey.py --repo metaphorex/metaphorex | python3 -c "import json,sys; d=json.load(sys.stdin); print(f'kaizen_open: {len(d.get(\"kaizen_open\", []))}')"
```
Expected: `kaizen_open: 8` (or current count of open kaizen issues)

**Step 4: Commit**

```bash
git add scripts/survey.py
git commit -m "feat: survey.py surfaces open kaizen issues in output"
```

**Human verification:** Run the survey — does the `kaizen_open` array contain the issues you filed this session?

---

### Task 3: Round Summary Includes Highlights Section

**Why:** Round summaries currently show only mining output ("Mined 5 issues → PR opened"). The operator has no visibility into improvements made, kaizen filed, or before/after metrics. This is the core feedback loop.

**Files:**
- Modify: `.claude/commands/work.md:111-131` (Phase C section)

**Step 1: Replace the Phase C round summary template**

Replace the existing Phase C section (lines 111-131) with:

````markdown
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
````

**Step 2: Verify the template has all three sections**

Run: `grep -c "###" .claude/commands/work.md`
Expected: at least 3 (Work, Highlights, Kaizen)

**Step 3: Commit**

```bash
git add .claude/commands/work.md
git commit -m "feat: /work round summaries now include Highlights and Kaizen sections"
```

**Human verification:** Read the new Phase C — does it describe the three-section format clearly enough that the pitboss will follow it without improvising?

---

### Task 4: Session-End Summary with Before/After Metrics

**Why:** At end of session, the operator should see a dashboard of what the session accomplished — not just "X PRs opened" but "factory went from stalled to producing." This is the cumulative version of per-round Highlights.

**Files:**
- Modify: `.claude/commands/work.md` (add after Phase C, before Stats accounting)

**Step 1: Add session-end summary template**

Insert before the "Stats accounting" section a new section:

````markdown
## Session-end summary

When `total_actionable` reaches 0 (or the session ends), print a final
summary covering the entire session:

```
## Session Complete

### Production
- Rounds: N
- PRs opened: N (list PR numbers)
- New mappings created: ~N
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
````

**Step 2: Verify section exists**

Run: `grep -c "Session-end summary" .claude/commands/work.md`
Expected: 1

**Step 3: Commit**

```bash
git add .claude/commands/work.md
git commit -m "feat: /work includes session-end summary with before/after metrics and kaizen status"
```

**Human verification:** Does the session-end template capture the kind of summary the operator asked for at the end of the session that prompted this work?

---

### Task 5: Friction Aggregation in Pitboss

**Why:** When 12 miners all hit the same worktree bug (#1432), one agent files it but the pitboss doesn't escalate. The operator has no idea it's systemic until they ask. The pitboss should scan agent results for repeated friction and bump priority.

**Files:**
- Modify: `.claude/commands/work.md` (add to Phase C, after agent completion)

**Step 1: Add friction aggregation instructions to Phase C**

Insert after the "Wait for all parallel agents to complete" instruction (current line 80-81):

````markdown
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
````

**Step 2: Verify the instruction is in Phase C**

Run: `grep -c "Friction aggregation" .claude/commands/work.md`
Expected: 1

**Step 3: Commit**

```bash
git add .claude/commands/work.md
git commit -m "feat: pitboss aggregates repeated agent friction and escalates kaizen priority"
```

**Human verification:** Read the friction aggregation rule — is the threshold (3+ agents) reasonable? Is the escalation action (priority:high + comment) proportionate?

---

### Task 6: Stale Claim Auto-Reclaim in Pitboss

**Why:** This session required manual reclaim of 187 stale in-progress issues. The pitboss should handle `stale_in_progress` automatically before dispatching miners, so the factory never stalls on orphaned claims again.

**Files:**
- Modify: `.claude/commands/work.md` (add to Phase B dispatch rules)

**Step 1: Add stale reclaim step to Phase B**

Insert at the beginning of Phase B (before the parallel dispatch group):

````markdown
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
````

**Step 2: Verify the instruction is in Phase B**

Run: `grep -c "Reclaim stale" .claude/commands/work.md`
Expected: 1

**Step 3: Commit**

```bash
git add .claude/commands/work.md
git commit -m "feat: pitboss auto-reclaims stale in-progress issues before mining dispatch"
```

**Human verification:** Read the reclaim step — does it match what was done manually in round 2 of this session?

---

### Task 7: Final Integration Test

**Step 1: Run the full survey and verify all new fields**

```bash
uv run scripts/survey.py --repo metaphorex/metaphorex | python3 -c "
import json, sys
d = json.load(sys.stdin)
required = ['needs_smelting', 'needs_assay', 'needs_miner_fix', 'needs_survey',
            'needs_rework', 'in_progress', 'unclaimed', 'stale_in_progress',
            'needs_prospecting', 'prospected_projects', 'kaizen_open', 'total_actionable']
for key in required:
    print(f'{key}: {len(d[key]) if isinstance(d[key], list) else d[key]}')
missing = [k for k in required if k not in d]
print(f'Missing keys: {missing or \"none\"}')
"
```
Expected: All keys present, `kaizen_open` shows current count, no missing keys.

**Step 2: Verify work.md has all new sections**

```bash
grep -n "Kaizen reporting\|Session-end summary\|Friction aggregation\|Reclaim stale\|### Highlights\|### Kaizen" .claude/commands/work.md
```
Expected: 6 matches, one for each new section/subsection.

**Step 3: Run validator to make sure nothing broke**

```bash
uv run scripts/validate.py validate
```
Expected: zero errors, zero new warnings.

**Step 4: Final commit if any cleanup needed, then push**

```bash
git push origin main
```

**Human verification:** Read through the complete `work.md` end-to-end. Does the flow make sense? Phase A surveys (including kaizen), Phase B reclaims stale + dispatches, Phase C reports Work + Highlights + Kaizen. Session-end gives the full dashboard.
