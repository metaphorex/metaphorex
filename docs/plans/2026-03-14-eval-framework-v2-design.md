# Eval Framework v2 — Fair Prompts, Scoring Pipeline, Snapshot Versioning

**Date:** 2026-03-14
**Status:** Draft
**Repo:** `metaphorex/eval` (at `/Users/fshot/code/fshot/metaphorex/eval`)
**Supersedes:** Tasks 8-10 of `2026-03-14-eval-framework-impl.md`

## Context

Tasks 1-7 of the original eval framework plan are implemented (21 tests
passing, lint clean). During review we identified four problems that must be
fixed before burning eval tokens:

1. **Unfair prompt design** — baseline gets no metaphor encouragement while
   m4x condition gets extra framing. Confounds the variable.
2. **Scoring pipeline not wired** — runner saves raw responses, report shows
   response lengths, no scoring step in between.
3. **Snapshots are ad-hoc** — generated locally, gitignored, not pinned. No
   reproducibility.
4. **Prompt sensitivity unknown** — slight wording changes might swing results.
   Need systematic prompt variant testing.

## Task dependency graph

```
A (Prompt redesign) ──┐
B (Scoring pipeline) ──┼──> E (First real eval run)
C (Snapshot releases) ──┤
D (promptfoo setup) ────┘
                        F (HuggingFace prep) — after C, independent
```

A, B, C, D are independent and can be developed in parallel. E requires all
four. F requires only C.

**Recommended order:** D first (informs A's wording), then A+B+C in parallel,
then E, then F.

---

## Task A: Redesign prompts for fair 4-condition experiment

**Problem:** Baseline and m4x conditions get different levels of metaphor
encouragement. The only variable should be what data accompanies the prompt.

### New design — 4 conditions, shared encouragement

| Condition | Encouragement | Data provided |
|-----------|--------------|---------------|
| `baseline` | Shared | None |
| `frames_only` | Shared | ~20 source domain names (kitchen, military, theater...) |
| `m4x_pairs` | Shared | Compact catalog: name + source→target for all 408 |
| `m4x_full` | Shared | Full catalog: What It Brings + Where It Breaks + Expressions |

**Key: the `SHARED_ENCOURAGEMENT` must NOT mention "knowledge graph" or
"catalog"** — that would prime non-baseline conditions differently.

### What each comparison isolates

- A vs B: Does having a menu of source domains help?
- B vs C: Does structured source→target mapping help beyond a bare list?
- C vs D: Does "Where It Breaks" analysis improve the "Potential Mislead"
  quality?

### Draft shared encouragement

> You are a software architect naming components for a new system. Good
> component names use a consistent metaphorical frame — all names come from
> the same source domain (e.g., all from cooking, all from military command,
> all from theater). This makes the system easier to understand and
> communicate about.
>
> {system_desc}
>
> Name exactly 10 components. For each, provide:
> 1. The name (drawn from your chosen metaphorical frame)
> 2. Which component role it fulfills
> 3. Why this name fits that role
> 4. What the name might mislead someone about
>
> Output as a numbered list: Name | Role | Why This Name | Potential Mislead

For conditions B/C/D, prepend a neutral data preamble:

> Here is reference material on metaphorical source domains:
>
> {data_block}
>
> ---

---

## Task B: Wire the scoring pipeline

**Problem:** No step reads raw results → calls scorers → writes scored output.
Report can't show scores.

### New file: `scoring/score.py` — Scoring orchestrator

```
uv run python -m scoring.score --results results/naming/run-*.json
```

- Reads raw result JSON files
- For each non-dry-run response:
  - Calls `score_frame_consistency(response)` → `consistency_ratio`
  - Calls `score_structural_fidelity(response, system_desc)` → `fidelity`,
    `mislead_quality`
  - Looks up `system_desc` from `SCENARIOS` by matching `result["scenario"]`
- Writes `results/scored/scored-{timestamp}.json` — same shape as raw but with
  added `scores` dict
- Shares a single Anthropic client across all calls
- `--dry-run` flag skips API calls, writes `scores: null`

### Report updates

- Summary table shows scores (consistency, fidelity, mislead) instead of
  response lengths
- Per-condition averages across models and scenarios
- Raw response appendix controlled by `--include-responses` flag

---

## Task C: Snapshot versioning with CalVer releases

**Problem:** Snapshots are ad-hoc and gitignored. Need reproducible, versioned
snapshots tied to content repo releases.

### CalVer scheme

`YYYY.MM.DD` with `.N` suffix for same-day releases (e.g., `2026.03.14`,
`2026.03.14.1`).

### In content repo

1. **New script: `scripts/release.py`** (PEP 723 inline-deps):
   - Generates CalVer tag from today's date
   - Checks existing tags for same-day collisions, appends `.N` if needed
   - Runs `validate.py extract` to produce snapshot JSON
   - Diffs against last release — skips if no catalog changes
   - Creates GitHub Release via `gh release create {tag}` with snapshot
     attached as `metaphorex-{tag}.json`
   - `--dry-run` flag

2. **New workflow: `.github/workflows/release.yml`** — triggered by
   `workflow_run` completion of `deploy-site.yml`:
   - Runs `uv run scripts/release.py`
   - Separate from deploy (clean separation of concerns)
   - Needs `contents: write` permission
   - Ties releases to the existing "publish" concept: daily cron + manual
     dispatch

### In eval repo

3. **`data/snapshot.py`** — add `fetch_snapshot(version, repo)`:
   - Uses `gh release download` to fetch specific release assets
   - `version=None` fetches latest

4. **`evals/naming/run.py`** — add `--snapshot-version` arg, mutually
   exclusive with `--snapshot` path.

---

## Task D: promptfoo for prompt sensitivity testing

**Problem:** We don't know if minor prompt wording changes swing results. Need
to calibrate before the real eval.

**Approach:** promptfoo runs standalone via `npx` — not a Python dependency.
Config lives in the eval repo. Run it to test 2-3 prompt variants against 1-2
cheap models on 1 scenario, then pick the most stable wording for Task A.

### Files

| File | Purpose |
|------|---------|
| `promptfoo/promptfooconfig.yaml` | OpenRouter providers, prompt files, test cases |
| `promptfoo/prompts/v1.txt` | Primary encouragement wording |
| `promptfoo/prompts/v2.txt` | Variant: "frame" vs "domain" |
| `promptfoo/prompts/v3.txt` | Variant: instruction ordering |
| `promptfoo/README.md` | Install, run, interpret |

### Usage

```bash
npx promptfoo@latest eval --config promptfoo/promptfooconfig.yaml
npx promptfoo@latest view
```

---

## Task E: First real eval run

**Depends on:** A, B, C, D all complete.

1. Create release in content repo: `uv run scripts/release.py`
2. Fetch snapshot in eval repo: `--snapshot-version YYYY.MM.DD`
3. Run eval: 4 conditions × 3 scenarios × 5 models = 60 API calls (~$1)
4. Score results: 60 responses × 2 scorers = 120 Haiku calls (~$0.12)
5. Generate report with comparison tables
6. Review and commit scored results

---

## Task F: HuggingFace dataset prep (NO PUSH)

**Depends on:** C.

Build push script (`data/huggingface/push.py`) and dataset card
(`data/huggingface/README.md`) but do **not** push. User sets up HF
account/org/token manually, then runs the script when ready.

---

## Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| 4 conditions vs 2 | 4 | Isolates data quality from encouragement effect |
| promptfoo for prompt testing | Yes | Systematic variant testing before committing |
| CalVer releases | Tied to deploy-site | Matches existing "publish" cadence |
| Same-day disambiguation | `.N` suffix | Simple, human-readable |
| Release workflow | Separate from deploy | Clean separation, different permissions |
| promptfoo as npx | Not a Python dep | Different toolchain, runs independently |
