---
project_issue: 1460
repo: metaphorex/metaphorex
source_type: corpus
status: draft
---

# Catalog Enrichment — Transfers and Limits Propositions

## Source Description

The source is the existing Metaphorex catalog (694 entries across 6 kinds:
metaphor, dead-metaphor, pattern, archetype, paradigm, and mental-model).
The goal is to add structured `transfers` and `limits` proposition lists to
each entry's frontmatter, enabling vector search over the structural
properties that make each entry distinctive.

**Current state (2026-03-17):** 288 of 694 entries already have
transfers/limits (from pilot + batches 1 and 9 of the original run). 406
entries remain. The original batches 2-8 were mined but their PRs were
closed without merging, so those entries need to be re-enriched.

## Access Method

The "source" for this enrichment project is the catalog itself. No external
archive is involved. The survey script at
`playbooks/catalog-enrichment/scripts/survey_enrichment.py` deterministically
identifies which entries lack `transfers:` and/or `limits:` in their YAML
frontmatter.

Run the survey:
```bash
uv run playbooks/catalog-enrichment/scripts/survey_enrichment.py 2>/dev/null
```

Rebuild the manifest:
```bash
uv run playbooks/catalog-enrichment/scripts/build_manifest.py 2>/dev/null \
  > playbooks/catalog-enrichment/manifest.json
```

## Extraction Strategy

**Work type:** Enrichment (not new entry creation). The Miner reads existing
entries and adds frontmatter fields without altering body text.

**Process per entry:**

1. Read the existing file from `catalog/entries/<slug>.md`
2. Read the body sections (## What It Brings, ## Where It Breaks) for context
3. Generate `transfers:` and `limits:` YAML lists following the proposition-writing
   guidance below
4. Insert the new fields into the existing frontmatter block
5. Do NOT alter existing body text -- frontmatter additions only

**Batch processing:** Each batch sub-issue lists entry slugs. Process all slugs
in a single PR. Batches are ~50 entries each, grouped by kind.

**Batch composition (406 entries, 9 batches):**

| Batch | Size | Kinds |
|-------|------|-------|
| 1 | 50 | archetype (2), dead-metaphor (6), mental-model (27), metaphor (15) |
| 2 | 50 | metaphor (50) |
| 3 | 50 | metaphor (50) |
| 4 | 50 | metaphor (50) |
| 5 | 50 | metaphor (50) |
| 6 | 50 | metaphor (50) |
| 7 | 50 | metaphor (50) |
| 8 | 50 | metaphor (50) |
| 9 | 6 | metaphor (6) |

## Schema Mapping

Enrichment adds two fields to existing frontmatter:

| Field | Type | Description |
|-------|------|-------------|
| `transfers` | list[str] | Propositions describing what structural properties transfer from the source frame |
| `limits` | list[str] | Propositions describing where the mapping breaks down or misleads |

These fields are inserted at the end of the frontmatter block, after `updated`
and before the closing `---`.

## Proposition-Writing Guidance

### Form by Kind

| Kind | Prefix | Example |
|------|--------|---------|
| `metaphor` | `[source]` | `[source] blockage at any stage propagates upstream` |
| `dead-metaphor` | `[source]` | `[source] the original nautical sense of keeping a ship steady persists in the abstract meaning` |
| `pattern` | `[source]` | `[source] decouples state changes from notification` |
| `archetype` | `[source]` | `[source] the trickster violates rules to reveal arbitrariness` |
| `paradigm` | `[paradigm]` | `[paradigm] simplicity is preferred over correctness` |
| `mental-model` (cognitive) | `[model]` | `[model] reframes by asking what guarantees failure` |
| `mental-model` (predictive) | `[law]` | `[law] predicts systems mirror org structure` |

### Three Quality Tests

Every proposition must pass all three tests. No exceptions.

1. **Independence:** Genuinely true of the source domain, not a restatement
   of the mapping relationship itself. The proposition should hold even if
   you have never heard of the target domain.

2. **Discrimination:** Non-trivially false of 2+ topically-similar but
   structurally-different domains. This is the critical test. If the
   proposition is true of everything in the same neighborhood, it carries
   no signal for vector search.

3. **Relational:** Describes a relationship or process, not a static
   attribute. "[source] connects X to Y" passes. "[source] is large" fails.

### Minimum Counts

| Kind | Min transfers | Min limits |
|------|--------------|------------|
| `metaphor`, `dead-metaphor`, `pattern`, `archetype` | 3 | 2 |
| `paradigm`, `mental-model` | 2 | 2 |

## Good vs Bad Examples

### BAD -- Do Not Write These

- `[source] involves flow` -- also true of rivers, blood, traffic (fails
  discrimination). Too vague to distinguish this entry from dozens of
  others.

- `[source] is complex` -- attributive, not relational (fails relational
  check). Describes a static property, not a structural relationship.

- `[source] maps onto the target in interesting ways` -- restates the
  mapping relationship itself (fails independence). This is true of every
  entry in the catalog by definition.

- `[source] has structure` -- vacuously true of everything (fails
  discrimination). Carries zero signal for vector search.

### GOOD -- These Pass All Three Tests

- `[source] blockage at any stage propagates upstream` -- false of rivers
  (flow around obstacles), traffic (congestion stays local), electricity
  (open/short). Discriminates plumbing-family metaphors sharply.

- `[source] participants escalate commitment based on sunk investment` --
  false of games (can forfeit), commerce (can cut losses at any time).
  Captures a specific structural dynamic.

- `[source] victory requires both strategy and execution under pressure` --
  false of puzzles (no opponent), voting (no execution phase). Distinguishes
  competitive-conflict metaphors from other goal-pursuit frames.

- `[law] predicts that when a measure becomes a target, it ceases to be a
  good measure` -- specific, testable, distinguishes from related effects
  like regression to the mean or survivorship bias.

## Frontmatter Insertion Format

Insert after existing frontmatter fields, before the closing `---`:

```yaml
transfers:
  - "[source] first proposition here"
  - "[source] second proposition here"
  - "[source] third proposition here"
limits:
  - "[source] breaks when first condition"
  - "[source] misleads when second condition"
```

The `transfers` and `limits` fields go at the end of the frontmatter block,
after `updated` and before the `---` that closes the YAML. Preserve all
existing fields exactly as they are.

**YAML quoting:** All propositions must be double-quoted strings in the YAML
list. This prevents issues with colons, apostrophes, and other special
characters in proposition text.

## Git Workflow

- Branch: `enrich/<batch-number>`
- PR title: `Enrich: batch N (M entries)`
- PR body: list all enriched slugs, link to batch sub-issue
- Commit with: `Co-Authored-By: metaphorex-miner <miner@metaphorex.org>`

## Gotchas

1. **Do NOT alter body text** -- only add frontmatter fields. The body
   sections (What It Brings, Where It Breaks, Expressions) are the source
   material you read, not the output you write.

2. **Do NOT add `grounding`** -- that is a separate audit step with its own
   process. This playbook covers `transfers` and `limits` only.

3. **Skip entries that already have propositions.** If an entry already has
   `transfers:` or `limits:` in its frontmatter, skip it entirely.

4. **Flag thin entries instead of forcing bad propositions.** If an entry's
   body sections are too thin to generate propositions that pass all three
   quality tests, do not guess. Instead, flag the slug in a comment on the
   batch sub-issue with a brief explanation of what is missing.

5. **Run validation after each batch:**
   ```bash
   uv run scripts/validate.py validate
   ```
   Zero errors required before opening the PR.

6. **YAML quoting for propositions.** Propositions frequently contain colons,
   apostrophes, and other characters that break unquoted YAML strings. Always
   use double-quoted strings in the `transfers:` and `limits:` lists.

7. **dead-metaphor kind.** 6 entries use the `dead-metaphor` kind. These
   follow the same `[source]` prefix convention as regular metaphors but
   the propositions should emphasize the etymological relationship between
   the literal origin and the current abstract usage.

8. **Sub-issue cap.** With 9 batches needed plus the existing sub-issues,
   we remain well under GitHub's 100 sub-issue limit.
