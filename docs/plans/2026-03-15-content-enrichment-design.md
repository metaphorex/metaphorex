# Content enrichment design
## Transfers, limits, grounding, and kind reclassification

**Issues**: #1454 (content enrichment), #1455 (grounding audit)
**Parent**: #899 (schema overhaul)
**Prereqs**: #1452 + #1453 (validator + migration must land first)

---

## Overview

After the schema migration renames fields and kinds, every entry still
needs structured propositions (`transfers` and `limits`) added to its
frontmatter. This is the work that makes vector search possible.

Three passes, run sequentially:

1. **Kind reclassification audit** — move entries between kinds where needed
2. **Opus content pass** — generate `transfers` + `limits` for all entries
3. **Grounding audit** — set `grounding` on non-folk entries

---

## 1. Kind reclassification audit

### Paradigm → mental-model candidates

Review all 51 current `paradigm` entries. Some may actually be
`mental-model` (cross-domain cognitive move, no inherent position).

**Decision rule**: Does the entry take a position you can agree or
disagree with? If yes → `paradigm`. If it's a lens or technique with
no inherent domain → `mental-model`.

Examples that likely stay `paradigm`:
- worse-is-better (has a position: simplicity over correctness)
- survival-of-the-fittest (has a real source_frame in biology)
- convention-over-configuration (prescriptive)

Examples that might become `mental-model`:
- Entries about named laws (Conway's Law, Goodhart's Law) — if they exist
- Entries about razors or decision heuristics
- Entries about cognitive techniques (inversion, second-order thinking)

**Note**: Most of these entries don't exist yet. This audit is primarily
about the 51 existing paradigm entries. The Miner handles new entries
with correct kinds going forward.

### Source frame audit for paradigms

For each `paradigm` entry:
- Does `source_frame` represent a genuine metaphorical source domain?
  - Yes (survival-of-the-fittest → natural-selection): keep it
  - No (forced/artificial frame to satisfy old validator): remove it

After migration, `source_frame` is optional for paradigms, so removing
artificial frames is now possible.

### Dead metaphor verification

All 62 entries migrated from `dead-metaphor` to `metaphor` + `dead: true`.
Quick scan to confirm `dead` classification is correct:
- Would a newcomer need the original source domain explained? → `dead: true`
- Is the source domain still actively referenced? → remove `dead: true`

### Process

- One pass, one PR
- Changes are kind reclassification + source_frame removal only
- No content changes (propositions added in next pass)
- Human review required (these are editorial judgments)

---

## 2. Opus content pass: transfers + limits

### What gets generated

For each of the ~445 entries, generate and add to frontmatter:

```yaml
transfers:
  - "[source] moves items in one direction only"
  - "[source] has discrete stages that transform items sequentially"
  - "[source] throughput is bounded by the slowest stage"

limits:
  - "[source] assumes items are independent; feedback loops break the model"
  - "[source] assumes clear stage boundaries"
```

### Proposition form by kind

| Kind | Prefix | Example |
|------|--------|---------|
| `metaphor` | `[source]` | `[source] blockage propagates upstream` |
| `pattern` | `[source]` | `[source] decouples producers from consumers` |
| `archetype` | `[source]` | `[source] the hero departs the known world` |
| `paradigm` | `[paradigm]` | `[paradigm] simplicity is preferred over correctness` |
| `mental-model` (cognitive) | `[model]` | `[model] reframes by asking what guarantees failure` |
| `mental-model` (predictive) | `[law]` | `[law] predicts systems mirror org structure` |

### Minimum counts

| Kind | Min transfers | Min limits |
|------|--------------|------------|
| `metaphor`, `pattern`, `archetype` | 3 | 2 |
| `paradigm`, `mental-model` | 2 | 2 |

### Generation prompt

```
You are building a structured metaphor knowledge base optimized for
structural similarity search.

ENTRY:
{full_entry_text including frontmatter and body}

Generate two lists:

transfers: 4-8 propositions in "[source] ..." form (or "[paradigm]",
"[model]", "[law]" as appropriate to the kind).

Each proposition must be:
- Independently true of the source domain
- Non-trivially false of at least two topically-similar but
  structurally-different domains (name those domains in a comment
  after the proposition to show your work)
- Relational, not attributive: "[source] connects X to Y via Z",
  not "[source] is large"

limits: 2-5 propositions in "[source] breaks when ..." or
"[source] misleads when ..." form.

Flag low confidence with a # low-confidence comment.
Output YAML only.
```

### Quality gate

Before scaling past 20 entries:

**Discrimination test**: For each `transfers` proposition, ask:
"Is this also true of three topically similar but structurally different
domains?" If yes → proposition is not discriminating enough → revise.

Example:
- BAD: `[source] involves flow` — also true of RIVER, BLOOD, TRAFFIC
- GOOD: `[source] blockage at any stage propagates upstream` — false of
  rivers (don't back up), false of traffic (blocks locally, not upstream)

**Coverage test**: Do the propositions collectively capture the *relational
structure* that makes this entry useful as a reasoning tool? If someone
searches for a structural pattern, would these propositions surface this
entry for the right queries?

### Execution plan

```
Phase A — Pilot (20 entries)
  - Select 20 entries: 8 metaphor, 4 dead-metaphor, 4 paradigm,
    2 archetype, 2 edge cases
  - Generate transfers + limits via Opus
  - Human review of all 20
  - Run discrimination test on all transfers propositions
  - Iterate prompt if quality is insufficient

Phase B — Scale (remaining ~425 entries)
  - Batch by kind (metaphors first, then paradigms, then archetypes)
  - 50 entries per batch, human spot-check 5 per batch
  - Validator enforces min counts after each batch merges

Phase C — Enable strict validation
  - Flip validator to enforce transfers/limits min counts
  - Fix any entries that fail
```

### Script design

`scripts/enrich_propositions.py` — PEP 723 inline deps

```python
# Key behaviors:
# - Reads each mapping, checks if transfers/limits already present
# - If absent: calls Opus API with the generation prompt
# - Inserts generated propositions into frontmatter
# - Writes back to file
# - Tracks costs in structured output (model, tokens, cost per entry)
# - --batch N: process N entries then stop
# - --kind X: only process entries of kind X
# - --slug X: process single entry
# - --dry-run: print generated propositions without writing
# - --pilot: process 20 pre-selected entries only
```

### Where propositions go

**Frontmatter** (structured, for vector search):
```yaml
transfers:
  - "[source] ..."
limits:
  - "[source] ..."
```

**Body sections** (prose, for human reading):
```markdown
## Transfers

A committee that must approve a nuclear power plant spends most of its
time debating the color of the bike shed...

## Limits

Breaks when the trivial item genuinely is the most important...
```

The frontmatter lists are the embedding targets. The body sections are
the human-readable narrative. Both exist. The enrichment pass adds the
frontmatter lists; the body sections are already written (just renamed
from "What It Brings" / "Where It Breaks").

---

## 3. Grounding audit

### Scope

Most entries will have no `grounding` field (validator defaults to `folk`).
Only entries where the default is wrong need the field set.

### Process

1. Scan all entries
2. For entries that are clearly `proven`, `established`, or `contested` — add field
3. Leave all others alone (implicit `folk`)

### Known targets from import projects

| Entry | Grounding | Reason |
|-------|-----------|--------|
| Amdahl's Law | `proven` | Pure mathematics |
| CAP Theorem | `proven` | Formal proof |
| Conway's Law | `established` | Well-studied |
| Goodhart's Law | `established` | Well-observed |
| Loss Aversion | `established` | Hundreds of replications |
| Broken Windows Theory | `contested` | Evidence cuts both ways |
| Dunning-Kruger Effect | `contested` | Methodology disputed |
| Gall's Law | `contested` | Unfalsifiable |
| The Lindy Effect | `contested` | Not rigorously tested |

Most of these don't exist in the catalog yet. The grounding audit runs on
whatever exists after the content enrichment pass, and the Miner sets
grounding on new entries going forward.

### Decision criteria

- **proven**: Can you derive it from axioms or prove it formally? Not an
  empirical claim at all?
- **established**: Would a review paper cite strong evidence? Is the
  consensus clear in the relevant field?
- **contested**: Are there published critiques with substance? Is the
  debate ongoing in the relevant field?
- **folk**: Everything else. The safe default. When in doubt, omit.

### Execution

- One pass, one PR
- Can run in parallel with content enrichment (different fields)
- Human review required (editorial judgments about epistemics)

---

## 4. Agent guidance for ongoing content

After the enrichment pass, agents need updated guidance for new entries.

### Miner changes

When creating new entries:
- Generate `transfers` and `limits` as part of entry creation (not a
  separate pass)
- Use correct proposition form based on kind
- Set `grounding` when clearly non-folk
- Use `applies_to: [x]` instead of `target_frame: x`
- Apply discard filter: if can't generate 2+ transfers, file as nugget

### Assayer changes

When reviewing entries:
- Check proposition quality (discriminating, relational, correct form)
- Verify kind classification (especially paradigm vs mental-model)
- Verify grounding is appropriate
- Flag entries that might need different kind

### Discard filter (all playbooks)

An item is discarded if:
1. Cannot generate 2+ relational propositions that transfer beyond origin domain
2. No structural content (just a fact or definition)
3. Purely evaluative with no structural claim
4. Duplicate of existing entry

Discarded items → `nugget` issues, not silently dropped.

---

## 5. Sequencing summary

```
Week 1:
  #1453 Migration script (rename kinds + fields)     ─┐
  #1452 Validator update (new rules, Phase 1)          ├─ Single PR
  CONTRIBUTING.md + agent skill updates               ─┘

Week 2:
  Kind reclassification audit (paradigm review)       ── PR
  Grounding audit (set non-folk entries)              ── PR (parallel)

Week 2-3:
  #1454 Content enrichment Phase A (pilot 20 entries) ── PR
  Review + iterate prompt

Week 3-4:
  #1454 Content enrichment Phase B (remaining ~425)   ── Multiple PRs
  Enable strict validation (Phase 2)                  ── PR

Future:
  #1456 Embeddings pipeline (needs transfers/limits populated)
```

---

## 6. Success criteria

- [ ] All entries have valid kinds from the 5-kind taxonomy
- [ ] All metaphor entries have `source_frame`
- [ ] No entries have `target_frame` (replaced by `applies_to`)
- [ ] All entries have `transfers` (min 3 or min 2 depending on kind)
- [ ] All entries have `limits` (min 2)
- [ ] Non-folk entries have explicit `grounding`
- [ ] `mental-model` entries have no `applies_to`
- [ ] `dead: true` only on metaphor entries
- [ ] Validator passes with zero errors in strict mode
- [ ] Agent skills updated for ongoing content creation
