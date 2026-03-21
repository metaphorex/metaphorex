---
name: enrich
description: Run a structural enrichment sweep — tag entries with embodied_patterns, relation_types, structure, and abstraction_level
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Agent
model: sonnet
---

# Structural Enrichment Sweep

You are enriching Metaphorex catalog entries with structural tags that
enable cross-domain similarity retrieval.

## Setup

1. Invoke the `agent-identity` skill before any git/gh commands
2. Read the vocabulary doc for allowed values and annotation guidance:
   `docs/plans/2026-03-20-structural-enrichment-vocabulary.md`
3. Read the schema skill for how structural fields fit the entry schema

## Survey

Identify entries that need enrichment:

```bash
# Find entries missing embodied_patterns (the primary structural field)
for f in catalog/entries/*.md; do
  if ! grep -q "^embodied_patterns:" "$f"; then
    basename "$f" .md
  fi
done | wc -l
```

## Batch Selection

$ARGUMENTS

If no arguments provided, pick the next batch of 50 unenriched entries.
Group by kind when possible (all archetypes together, then paradigms, etc.)
to maintain annotation consistency within a batch.

If a kind or source_frame is specified (e.g., `--kind metaphor` or
`--frame mythology`), filter to that subset.

## Enrichment Process

For each entry in the batch:

1. **Read the entry** — understand transfers, limits, and body text
2. **Tag with structural fields** using the vocabulary:
   - `embodied_patterns: [val1, val2, val3]` — 2-4 values
   - `relation_types: [val1, val2, val3]` — 2-4 values
   - `structure: val` or `structure: [val1, val2]` — 1-2 values
   - `abstraction_level: val` — exactly 1 value
3. **Insert fields into frontmatter** — add after `grounding` or after
   `dead` if present, before the closing `---`. Do NOT change any
   existing fields or body text.

### Annotation Rules

- Tag the STRUCTURAL embodied patterns, not the surface domain
- Pick the 2-4 most load-bearing relations, not exhaustive ones
- `translate` = bridging two systems that can't directly talk
- `accretion` = deposits BECOME the structure (not just accumulation)
- `self-organization` = system structures itself through feedback
- `specific` = source frame requires domain expertise to understand
- Prefer fewer confident tags over many speculative ones
- When unsure, check the vocabulary doc for the distinction
  (e.g., `flow` vs `path`, `enable` vs `cause`)

### YAML format

```yaml
embodied_patterns:
  - container
  - force
  - boundary
relation_types:
  - compete
  - prevent
structure: competition
abstraction_level: generic
```

Use list format for `embodied_patterns` and `relation_types` (always
lists). Use scalar for `structure` and `abstraction_level` when single
value, list when two values for `structure`.

## Validate

After enriching the batch:

```bash
uv run scripts/validate.py validate
```

Fix any errors. The validator checks that all values are in the
controlled vocabulary.

## Commit and PR

Branch: `enrich/structural-batch-N` (where N is the batch number)

```bash
git checkout -b enrich/structural-batch-N
git add catalog/entries/
git commit -m "Enrich: structural tags batch N (M entries)"
```

Open a PR labeled `needs-smelting`:

```bash
gh pr create \
  --title "Enrich: structural tags batch N (M entries)" \
  --label needs-smelting \
  --body "Adds embodied_patterns, relation_types, structure, and abstraction_level to M entries.

Part of the structural enrichment sweep.
See: docs/plans/2026-03-20-structural-enrichment-vocabulary.md"
```

## Batch Size Guidance

- Default: 50 entries per batch
- If entries are complex (many transfers, nuanced structural choices): 30
- If entries are simple (clear single-domain metaphors): 75
- Never exceed 100 per batch — keeps PRs reviewable

## Quality Checks

Before opening the PR, spot-check 5 entries:
- Do the embodied_patterns capture structural shape, not surface domain?
- Do the relation_types reflect the load-bearing predicates in transfers?
- Is the abstraction_level correct? (Would a non-expert understand the source frame?)
- Does the structure tag match the dominant topology?
