# Digest Redesign — Design

**Date:** 2026-03-13
**Status:** Approved
**Feedback source:** `docs/plans/feedback-20260313-changelog-digest-review.md`

## Problem

The current digest script generates a single daily report that tries to serve
both operators and the public site. It fails at both: operators get no trend
data or cost breakdown, and the public sees noisy PR-centric language with
a wall of 184 slugs. Specific bugs: cost tracking returns empty (date filter),
duplicate entries across days (edits counted as adds), pipeline table shows
sub-issues instead of project-level rollups.

## Architecture Principle

GitHub is the system of record. All data is pulled from GitHub APIs or the
catalog filesystem at query time. No local state files, no append-only logs,
no external dependencies.

## Design

### Two outputs, one script

`scripts/digest.py` with two subcommands:

- **`digest.py ops [--date YYYY-MM-DD]`** — daily operator report
- **`digest.py changelog [--date YYYY-MM-DD]`** — weekly public changelog

Shared helpers handle GitHub queries and catalog counting. Each subcommand
has its own formatter.

### Output locations

| Subcommand | Output path | Schedule |
|------------|-------------|----------|
| `ops` | `docs/ops/YYYY-MM-DD.md` | Daily, 09:00 UTC |
| `changelog` | `docs/changelog/YYYY-WNN.md` | Weekly, Wednesday 06:00 UTC |

### Ops report format (daily)

```markdown
---
date: 2026-03-13
type: ops
---
# Ops Report — 2026-03-13

## At a Glance
- **+12 entries today** (vs +8 yesterday)
- **408 mappings** · 101 frames · 12 categories
- **$2.47 spent** today ($14.82 this week)

## 7-Day Activity
| Date  | Added | Cost   |
|-------|-------|--------|
| 03-13 |    12 |  $2.47 |
| 03-12 |     8 |  $1.93 |
| ...   |   ... |    ... |
| 03-07 |    13 |  $3.10 |
| **Total** | **42** | **$14.82** |

## Costs by Agent
| Agent | Model | Runs | Tokens | Cost |
|-------|-------|------|--------|------|
| miner | opus | 3 | 115,000 | $1.80 |
| ...   | ...  | ... | ...     | ...  |

## Pipeline Status
| Project | Progress | Status |
|---------|----------|--------|
| Jungian Archetypes | 6/7 (86%) | active |
| Dead Metaphors | 0/12 (0%) | pending |

## Kaizen Backlog
- #123: validator rejects valid YAML (opened 2026-03-10)

Or: "No open kaizen issues. [File one](https://github.com/metaphorex/metaphorex/issues/new?template=kaizen.yml)."
```

Key features:
- **At a Glance** section with day-over-day delta and weekly cost total
- **7-Day Activity** table showing daily counts and costs as a sparkline substitute
- **Pipeline Status** shows one row per import-project with aggregated sub-issue progress
- **Costs by Agent** aggregates stats comment data by agent/model

### Changelog format (weekly)

```markdown
---
date: 2026-03-09
type: changelog
week: 2026-W11
---
# Week 11, 2026

**42 new entries** added this week. Catalog now has **408 mappings**,
101 frames, and 12 categories.

## Highlights
- 6 Jungian archetypes (the-self, the-shadow, the-persona, ...)
- 12 dead metaphors (bankrupt, brand, capital, ...)
- 24 cognitive-linguistics-canon entries

## All New Entries
- [activation-energy](/mappings/activation-energy/)
- [agent-swarm](/mappings/agent-swarm/)
...
```

Key features:
- Human-friendly language: "added" not "merged", "entries" not "mappings merged"
- Highlights grouped by import project (derived from PR branch prefix or labels)
- Only entries first added that week (uses `--diff-filter=A`, not edit detection)
- No costs, no pipeline status, no operator internals

### Site integration

| Page | Path | Content | Nav placement |
|------|------|---------|---------------|
| Changelog | `/changelog/` | Weekly changelog entries | Main nav |
| Ops | `/ops/` | Daily ops reports | Footer link |

Astro content collections:
- `changelog` collection → `loader: glob({ pattern: "**/*.md", base: "../docs/changelog" })`
- `ops` collection → `loader: glob({ pattern: "**/*.md", base: "../docs/ops" })`

The current `digests` collection and `docs/digests/` directory are replaced.

### Bug fixes

1. **Cost tracking empty**: The `stats_from_issues()` jq query filters by
   `created_at >= since` but the GitHub API returns ISO timestamps. The string
   comparison works but the function iterates all import-project issues and
   fetches comments for each — if any API call fails silently, the whole
   section returns empty. Add error handling and debug logging.

2. **Duplicate entries across days**: `merged_prs()` uses GitHub search
   `merged:since..until` which matches PRs merged in the range. But a PR
   touching a mapping that was already added by a different PR appears again.
   Fix: use `--diff-filter=A` on the git log to detect first-add only, or
   deduplicate by checking if the mapping's `created` date falls within the
   target range.

3. **Pipeline table noise**: The current code queries sub-issues individually.
   Fix: query only issues with `import-project` label, get sub-issue counts
   via GraphQL, show one row per project.

4. **Language**: Replace "mappings merged" with "entries added" throughout.

### Workflow changes

| Workflow | Trigger | Runs |
|----------|---------|------|
| `daily-digest.yml` → `daily-ops.yml` | Daily 09:00 UTC + manual | `digest.py ops` |
| `weekly-digest.yml` → `weekly-changelog.yml` | Wednesday 06:00 UTC + manual | `digest.py changelog` |
| `deploy-site.yml` | Push to main on `docs/ops/**`, `docs/changelog/**`, `catalog/**` | Astro build |

### Migration

- Delete `docs/digests/` (daily + weekly files generated in this session)
- Create `docs/ops/` and `docs/changelog/`
- Regenerate retroactive reports for all active days
- Update `site/src/content.config.ts`: remove `digests` collection, add `changelog` and `ops`
- Update `site/src/pages/changelog.astro` to use new collection
- Create `site/src/pages/ops.astro`
- Rename workflow files
