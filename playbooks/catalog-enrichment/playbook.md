---
project_issue: 1460
repo: metaphorex/metaphorex
source_type: corpus
status: approved
---

# Catalog Enrichment — Transfers and Limits Propositions

## Source Description

The source is the existing Metaphorex catalog (~445 entries across 5 kinds:
conceptual-metaphor, design-pattern, archetype, paradigm, and cross-field-mapping).
The goal is to add structured `transfers` and `limits` proposition lists to each
entry's frontmatter, enabling vector search over the structural properties that
make each mapping distinctive.

## Extraction Strategy

**Work type:** Enrichment (not new entry creation). The Miner reads existing
entries and adds frontmatter fields without altering body text.

**Process per entry:**

1. Read the existing file from `catalog/mappings/<slug>.md`
2. Read the body sections (## What It Brings, ## Where It Breaks) for context
3. Generate `transfers:` and `limits:` YAML lists following the proposition-writing
   guidance below
4. Insert the new fields into the existing frontmatter block
5. Do NOT alter existing body text — frontmatter additions only

**Batch processing:** Each batch sub-issue lists entry slugs. Process all slugs
in a single PR.

## Proposition-Writing Guidance

### Form by Kind

| Kind | Prefix | Example |
|------|--------|---------|
| `metaphor` | `[source]` | `[source] blockage at any stage propagates upstream` |
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
| `metaphor`, `pattern`, `archetype` | 3 | 2 |
| `paradigm`, `mental-model` | 2 | 2 |

## Good vs Bad Examples

### BAD — Do Not Write These

- `[source] involves flow` — also true of rivers, blood, traffic (fails
  discrimination). Too vague to distinguish this mapping from dozens of
  others.

- `[source] is complex` — attributive, not relational (fails relational
  check). Describes a static property, not a structural relationship.

- `[source] maps onto the target in interesting ways` — restates the
  mapping relationship itself (fails independence). This is true of every
  entry in the catalog by definition.

- `[source] has structure` — vacuously true of everything (fails
  discrimination). Carries zero signal for vector search.

### GOOD — These Pass All Three Tests

- `[source] blockage at any stage propagates upstream` — false of rivers
  (flow around obstacles), traffic (congestion stays local), electricity
  (open/short). Discriminates plumbing-family metaphors sharply.

- `[source] participants escalate commitment based on sunk investment` —
  false of games (can forfeit), commerce (can cut losses at any time).
  Captures a specific structural dynamic.

- `[source] victory requires both strategy and execution under pressure` —
  false of puzzles (no opponent), voting (no execution phase). Distinguishes
  competitive-conflict metaphors from other goal-pursuit frames.

- `[law] predicts that when a measure becomes a target, it ceases to be a
  good measure` — specific, testable, distinguishes from related effects
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

## Git Workflow

- Branch: `enrich/<batch-number>`
- PR title: `Enrich: batch N (M entries)`
- PR body: list all enriched slugs, link to batch sub-issue
- Commit with: `Co-Authored-By: metaphorex-miner <miner@metaphorex.org>`

## Gotchas

1. **Do NOT alter body text** — only add frontmatter fields. The body
   sections (What It Brings, Where It Breaks, Expressions) are the source
   material you read, not the output you write.

2. **Do NOT add `grounding`** — that is a separate audit step with its own
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
