# Observability, Kaizen & Auto-Merge Design

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Make pipeline costs, content growth, and improvement opportunities
visible to humans on a daily/weekly cadence — and eliminate stacked-diff
friction by auto-merging approved content PRs.

**Architecture:** GitHub-native. Digests are markdown files committed to the
repo. Cost and activity data is queried from GitHub issue comments and PR
metadata at generation time. The site renders digest data at build time.
No external database.

**Tech Stack:** Python scripts (PEP 723 inline deps), GitHub Actions
workflows, Astro pages, existing `stats.py` infrastructure.

---

## Context

### What exists today

| Component | Status |
|-----------|--------|
| `## stats:` comment format | Working — agents post structured cost data on issues |
| `scripts/stats.py` | Working — `emit`, `summary`, `validate` subcommands |
| `project-summary.yml` | Working — auto-posts cost rollup when import-project closes |
| `kaizen:pipeline` / `kaizen:content` labels | Created but underused (1 open issue) |
| Stacked-diff merging | Manual — pitboss does `gh pr merge --squash --auto` sequentially |
| Site deploy | Nightly at 04:00 UTC via `deploy-site.yml` |

### What's missing

1. **Daily visibility** — no summary of yesterday's activity, costs, or growth
2. **Weekly review artifact** — no aggregated report for human review
3. **Kaizen channel** — agents have no way to report friction
4. **Auto-merge** — approved content PRs still require manual merge + rebase
5. **Content timestamps** — `created`/`updated` fields (issue #944) needed for
   "recently added" on site and in digests
6. **Issue navigation** — 128+ open issues in a flat list mixing content,
   dev, and community work
7. **Build-in-public pages** — no changelog or stats page on metaphorex.org

### Timing chain (working back from LinkedIn)

LinkedIn engagement peaks Tuesday–Thursday 10–11 AM ET. Target: **Wednesday
10:00 AM ET** for weekly post.

| Time (ET) | Time (UTC) | Event |
|-----------|------------|-------|
| Daily 5:00 AM | 09:00 UTC | Daily digest generates |
| Wed 2:00 AM | 06:00 UTC | Weekly digest generates |
| Wed 6:00 AM | 10:00 UTC | Human reviews weekly digest |
| Wed 10:00 AM | 14:00 UTC | LinkedIn post goes live (manual) |

---

## Design

### Task 1: Auto-merge on `approved` label

**Problem:** Content PRs are additive and independent, but the current merge
flow creates artificial serial dependencies. Each merge triggers rebase
conflicts in the next PR. The pitboss spends more time rebasing than mining.

**Solution:** A GitHub Action that auto-merges content PRs when labeled
`approved`, gated only by CI (validator must pass).

**File:** `.github/workflows/auto-merge.yml`

**Trigger:** `pull_request` event, type `labeled`, label `approved`

**Logic:**
1. Verify the PR only touches `catalog/` files (content-only gate)
2. Enable auto-merge: `gh pr merge $PR --squash --auto`
3. GitHub handles the rest — waits for CI, then merges

**Scope guard:** PRs touching `.claude/`, `scripts/`, `site/`, `.github/`,
or any non-catalog path are NOT auto-merged. Those still require human review.

**Impact on pitboss (`work.md`):** Remove the Phase C "Merge approved PRs"
block. The workflow replaces it. Pitboss no longer needs to rebase, update
branches, or handle merge conflicts for content PRs.

**Human editorial model:** Post-merge. Rollbacks via `git revert`, polish via
direct PRs to main. Kaizen issues for systemic quality problems.

#### Acceptance criteria

- [ ] Open a test PR adding a dummy mapping, label it `approved`, verify it
  auto-merges after validator CI passes
- [ ] Open a test PR touching `scripts/` AND `catalog/`, label it `approved`,
  verify it does NOT auto-merge (scope guard works)
- [ ] Run `/work` and verify pitboss no longer attempts manual merge steps

### Task 2: `created`/`updated` frontmatter fields + backfill

**Problem:** The site's "Latest Entries" sorts by filesystem mtime, which
breaks on fresh clones. Issue #944 tracks this.

**Solution:** Add `created` and `updated` ISO 8601 date fields to all content
frontmatter. Backfill from git history.

**Files:**
- `scripts/backfill_dates.py` — new script
- `scripts/validate.py` — add `created`/`updated` to required fields
- `site/src/content.config.ts` — add fields to Zod schema
- `site/src/pages/index.astro` — sort by `created` instead of mtime
- `CLAUDE.md` — document the new fields in Content Schema section
- Agent prompts (miner, smelter) — instruct agents to set these fields

**Backfill logic:**
```python
# created: date of first commit that added this file
git log --follow --diff-filter=A --format=%aI -- <file> | tail -1

# updated: date of most recent commit that modified this file
git log -1 --format=%aI -- <file>
```

Use date-only format (`2026-03-10`), not full ISO 8601 with time. Simpler,
sufficient for our purposes, and friendlier in frontmatter.

**Frontmatter result:**
```yaml
slug: argument-is-war
name: "Argument Is War"
kind: conceptual-metaphor
created: 2026-03-07
updated: 2026-03-10
# ... rest of fields
```

**Validator change:** `created` required, `updated` required. Both must be
valid ISO date strings (`YYYY-MM-DD`).

**Astro schema change:**
```typescript
created: z.coerce.date(),
updated: z.coerce.date(),
```

**Agent prompt changes:**
- Miner: set `created` to today's date, `updated` to today's date
- Smelter: preserve existing `created`, update `updated` to today's date
  if content was modified

#### Acceptance criteria

- [ ] Run backfill script: every `.md` file in `catalog/` has `created` and
  `updated` fields in frontmatter
- [ ] `uv run scripts/validate.py validate` passes with zero errors
- [ ] `cd site && bun run build` succeeds
- [ ] Home page sorts by `created` date, not filesystem mtime
- [ ] Spot-check 5 entries: `created` date matches the git log date for
  initial file creation

### Task 3: Kaizen issue template + agent reporting

**Problem:** Agents encounter friction (validation quirks, GitHub API limits,
schema ambiguities) but have no structured channel to report it. Observations
die with the conversation.

**Solution:** Two parts — a GitHub issue template for filing kaizen issues,
and instructions in each agent prompt to use it.

**Files:**
- `.github/ISSUE_TEMPLATE/kaizen.yml` — new template
- `.claude/agents/miner.md` — add kaizen reporting section
- `.claude/agents/assayer.md` — add kaizen reporting section
- `.claude/agents/smelter.md` — add kaizen reporting section
- `.claude/agents/prospector.md` — add kaizen reporting section
- `.claude/commands/work.md` — add kaizen reporting to pitboss

**Template:**
```yaml
name: Kaizen — report friction or suggest improvement
description: Report pipeline friction, schema issues, or improvement ideas
labels: ["kaizen:pipeline"]
body:
  - type: dropdown
    id: area
    attributes:
      label: Area
      options:
        - pipeline (agent prompts, orchestration, merge flow)
        - content-schema (frontmatter, validation, taxonomy)
        - site (Astro, pages, search)
        - github-workflow (CI, Actions, issue templates)
        - tooling (scripts, utilities)
    validations:
      required: true
  - type: textarea
    id: observation
    attributes:
      label: What happened
      description: What friction did you hit? What workaround did you use?
      placeholder: "Validator rejected a valid mapping because..."
    validations:
      required: true
  - type: textarea
    id: suggestion
    attributes:
      label: Suggested fix
    validations:
      required: false
```

**Agent prompt addition** (appended to each agent):
```markdown
## Kaizen reporting

At the end of your run, if you encountered friction that slowed you down or
forced a workaround, file a kaizen issue:

    gh issue create -R metaphorex/metaphorex \
      --template kaizen.yml \
      --title "kaizen: <short description>" \
      --body "<what happened and suggested fix>"

Rules:
- Search open kaizen issues first — don't file duplicates
- One issue per distinct problem
- Do this at the end of your run, not mid-task
- Don't file for transient errors (network blips, rate limits)
```

#### Acceptance criteria

- [ ] Template renders correctly on GitHub: visit
  `github.com/metaphorex/metaphorex/issues/new?template=kaizen.yml`
- [ ] Manually create a kaizen issue using the template — verify labels apply
- [ ] Run `/work` and verify agents can file kaizen issues (check for new
  issues labeled `kaizen:pipeline` after a run that encounters friction)

### Task 4: GitHub Projects board

**Problem:** 128+ open issues in a flat list. Content factory tickets drown
out dev work and community contributions.

**Solution:** A GitHub Projects board with filtered views. Labels are already
good — we need views, not more labels.

**Views:**

| View | Filter | Purpose |
|------|--------|---------|
| Pipeline | `label:import-project,nugget,in-progress,needs-smelting,needs-assay` | Daily agent ops |
| Dev & Kaizen | `label:kaizen:pipeline,kaizen:content,infrastructure,agents,enhancement,bug` | Weekly human review |
| Community | `no:label OR label:good first issue,help wanted,question,editorial-feedback` | External contributors |

**Implementation:** `gh project` CLI commands. No code.

```bash
# Create project
gh project create --owner metaphorex --title "Metaphorex Ops" --format board

# Add views with filters (via GraphQL — gh project doesn't support
# view creation directly, so we use the web UI or API)
```

**Practical note:** GitHub Projects v2 view filters are easiest to configure
in the web UI after creating the project via CLI. The plan should create the
project and document the view filters for manual setup.

#### Acceptance criteria

- [ ] Project board exists at `github.com/orgs/metaphorex/projects/`
- [ ] Three views visible: Pipeline, Dev & Kaizen, Community
- [ ] Pipeline view shows only content factory issues
- [ ] Dev & Kaizen view shows kaizen and infrastructure issues
- [ ] Community view shows unlabeled / community-facing issues

### Task 5: Daily and weekly digest scripts + workflows

**Problem:** Cost data and pipeline status exist but require manual excavation
across scattered issue comments.

**Solution:** A `scripts/digest.py` script with `daily` and `weekly`
subcommands, run by GitHub Actions on schedule. Output is a markdown file
committed to `docs/digests/`.

**Files:**
- `scripts/digest.py` — new script
- `.github/workflows/daily-digest.yml` — new workflow
- `.github/workflows/weekly-digest.yml` — new workflow

**Digest data sources** (all queried via `gh` CLI at generation time):

| Data | Source | Query |
|------|--------|-------|
| New mappings merged | PRs merged to main touching `catalog/mappings/` | `gh pr list --state merged --search "merged:>YYYY-MM-DD"` |
| Costs | `## stats:` comments on import-project issues | `gh api` + `stats.py summary` |
| Open kaizen issues | Issues labeled `kaizen:*` | `gh issue list --label kaizen:pipeline,kaizen:content` |
| Pipeline status | Import projects with sub-issue completion % | `gh api graphql` sub-issue query |
| Community activity | Issues/PRs from non-bot users | `gh` queries filtered by author |

**Daily digest format** (`docs/digests/2026-03-13.md`):

```markdown
---
date: 2026-03-13
type: daily
---

# Daily Digest — 2026-03-13

## New Content
- 5 mappings merged: [list with links]
- 2 frames added
- Catalog total: 231 mappings, 73 frames, 20 categories

## Costs (last 24h)
| Agent | Model | Runs | Tokens | Cost |
|-------|-------|------|--------|------|
| miner | opus | 3 | 45,000 | $2.14 |
| assayer | sonnet | 2 | 12,000 | $0.18 |
| **Total** | | **5** | **57,000** | **$2.32** |

## Pipeline Status
| Project | Progress | Status |
|---------|----------|--------|
| cognitive-linguistics-canon | 45/62 (73%) | active |
| design-patterns-gof | 23/23 (100%) | complete |

## Kaizen Backlog
- #899: Content kaizen: where do mental models live? (open 3 days)
- #961: Validator rejects valid paradigm entries (new today)
```

**Weekly digest format** (`docs/digests/weekly/2026-W11.md`):

```markdown
---
date: 2026-03-12
type: weekly
week: 2026-W11
---

# Weekly Digest — Week 11, 2026

## Growth
- 32 new mappings (194 → 226)
- 8 new frames (63 → 71)
- 1 new category

## Costs (7-day total)
| Agent | Runs | Tokens | Cost |
|-------|------|--------|------|
| miner | 18 | 312,000 | $14.22 |
| assayer | 12 | 78,000 | $1.17 |
| smelter | 15 | 45,000 | $0.18 |
| pitboss | 4 | 89,000 | $5.01 |
| **Total** | **49** | **524,000** | **$20.58** |

## Cumulative
- Total mappings: 226
- Total cost to date: $48.73
- Cost per mapping: $0.22

## Pipeline Health
- 3 import projects active, 2 stalled (no activity 7+ days)
- 12 kaizen issues open (3 new this week)

## Community
- 0 external PRs, 2 nugget issues filed

## Highlights
[1-3 notable entries or milestones — good raw material for LinkedIn post]
```

**Workflow schedules:**
- Daily: `cron: "0 9 * * *"` (09:00 UTC = 5:00 AM ET)
- Weekly: `cron: "0 6 * * 3"` (06:00 UTC Wednesday = 2:00 AM ET)

**Workflow logic:**
1. Checkout repo
2. Run `uv run scripts/digest.py daily` (or `weekly`)
3. Script writes markdown file to `docs/digests/`
4. Commit and push to main

**Script design:** `digest.py` uses PEP 723 inline deps (same pattern as
`validate.py` and `stats.py`). It shells out to `gh` for GitHub data and
imports `stats.py` for cost parsing. Output is written directly to the
correct file path.

#### Acceptance criteria

- [ ] Run `uv run scripts/digest.py daily` locally — produces a valid
  markdown file at `docs/digests/YYYY-MM-DD.md` with real data from GitHub
- [ ] Run `uv run scripts/digest.py weekly` locally — produces a valid
  markdown file at `docs/digests/weekly/YYYY-WNN.md`
- [ ] Daily digest includes: new content count, cost table, pipeline status,
  kaizen backlog
- [ ] Weekly digest includes: growth delta, 7-day cost total, cumulative
  stats, community activity, highlights section
- [ ] Workflows trigger on schedule (verify via `gh workflow list`)
- [ ] Digest commit appears on main with correct file path

### Task 6: Site pages — changelog and stats

**Problem:** Build-in-public ethos requires publishing operational data.
Currently the site shows content but not how it grows.

**Solution:** Two new Astro pages that render from digest data and catalog
metadata.

**Files:**
- `site/src/pages/changelog.astro` — renders recent digests
- `site/src/pages/stats.astro` — corpus statistics
- `site/src/pages/index.astro` — update "Latest Entries" to use `created`
  field (already covered in Task 2, but the sorting logic change lives here)
- `site/src/content.config.ts` — add digests collection if needed, or
  read digest files directly at build time

**Changelog page (`/changelog/`):**

Shows the last 30 daily digests, rendered from `docs/digests/*.md`. Each
digest is a collapsible section with the date as header.

Implementation options:
- **Option A:** Add a `digests` content collection pointing at
  `docs/digests/` (Astro glob loader). Render with `getCollection`.
- **Option B:** Read digest files directly with `import.meta.glob` at build
  time. Simpler, no schema needed.

Recommend **Option A** — content collection gives us frontmatter parsing
and sorting for free, and we want the `date` and `type` fields.

Digest content collection config:
```typescript
const digests = defineCollection({
  loader: glob({ pattern: "*.md", base: "../../docs/digests" }),
  schema: z.object({
    date: z.coerce.date(),
    type: z.enum(["daily", "weekly"]),
    week: z.string().optional(),
  }),
});
```

**Stats page (`/stats/`):**

Computed at build time from the catalog collections:
- Total mappings, frames, categories
- Breakdown by kind (conceptual-metaphor: N, design-pattern: N, ...)
- Breakdown by category
- Top frames (most-referenced source and target frames)
- Growth chart data (from digest `date` + counts, rendered as a simple
  HTML table — no JS charting library needed for v1)

**Deploy trigger update:** `deploy-site.yml` should also trigger on pushes
to `docs/digests/` so the site rebuilds when a new digest is committed.

Add to the `on:` block:
```yaml
on:
  schedule:
    - cron: "0 4 * * *"
  push:
    branches: [main]
    paths: ["docs/digests/**"]
  workflow_dispatch: {}
```

#### Acceptance criteria

- [ ] `/changelog/` page renders on local dev server (`bun run dev`)
- [ ] Shows at least the most recent daily digest with correct formatting
- [ ] `/stats/` page renders with correct corpus counts
- [ ] Stats page shows breakdown by kind and by category
- [ ] `bun run build` succeeds with the new pages
- [ ] Site deploy triggers when a digest file is pushed (verify workflow run)

---

## Implementation Order

```
┌─────────────────────────────────────────┐
│ Parallel group (no dependencies)        │
│                                         │
│  Task 1: Auto-merge workflow            │
│  Task 2: created/updated backfill       │
│  Task 3: Kaizen template + agents       │
│  Task 4: GitHub Projects board          │
│                                         │
└─────────────┬───────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────┐
│ Task 5: Daily/weekly digest             │
│ (needs Tasks 2+3 for datetime fields    │
│  and kaizen issues to report on)        │
└─────────────┬───────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────┐
│ Task 6: Site changelog + stats pages    │
│ (needs Task 2 for dates, Task 5 for    │
│  digest files to render)               │
└─────────────────────────────────────────┘
```

Tasks 1–4 are fully independent. Dispatch as parallel agents.
Task 5 depends on 2 and 3. Task 6 depends on 2 and 5.

---

## Risks and mitigations

| Risk | Mitigation |
|------|------------|
| Auto-merge lands broken content | Validator CI is the gate. If validator has gaps, fix the validator (kaizen issue). Human rollback via `git revert` is fast. |
| Digest script fails silently | Workflow posts a GitHub Actions failure notification. Script exits non-zero on any `gh` query failure. |
| Kaizen issue spam from agents | "Search before filing" instruction + human triage in weekly review. Can add rate limit later if needed. |
| Backfill script gets wrong dates | Spot-check acceptance criteria (5 entries). Git history is authoritative — `--follow` handles renames. |
| Projects board goes stale | Auto-add rules: new issues auto-added to project. Views filter by label, so label discipline (already good) keeps views accurate. |
