# Progressive enrichment pattern

## The pattern

A repeatable process for adding new optional fields to the catalog
without halting normal operations. Each enrichment follows the same
lifecycle: design → validate → integrate → sweep → harden → exploit.

This document defines the pattern. Individual enrichment passes
(structural tags, sameAs URIs, abstract roles on frames) each get
their own vocabulary doc but follow this lifecycle.

---

## Lifecycle phases

### Phase 1: Design

Define the new fields and their controlled vocabularies.

**Artifacts produced:**
- Vocabulary doc (`docs/plans/<date>-<enrichment>-vocabulary.md`)
  with values, definitions, annotation guidance, and examples
- All fields are OPTIONAL — additive, never breaking

**Gate:** Vocabulary doc reviewed and approved.

### Phase 2: Validate

Prove the enrichment has measurable value on a small sample.

**Process:**
1. Tag 50-100 entries by hand or agent
2. Build eval set with analogy triples or other test cases
3. Run eval harness
4. Go/no-go decision based on metrics

**Artifacts produced:**
- Eval set (`docs/evals/<enrichment>-eval-set.yaml`)
- Eval script (`scripts/eval-<enrichment>.ts`)
- Eval report (`docs/evals/<date>-<enrichment>-report.md`)

**Gate:** Eval demonstrates measurable improvement over baseline.

### Phase 3: Integrate

Teach the pipeline so new content arrives enriched automatically.

**Changes:**
1. **Schema skill** — add new fields to the canonical schema reference
2. **Miner agent** — include enrichment in the entry creation workflow
3. **Assayer agent** — include enrichment quality in the review checklist
4. **Validator** — recognize new fields, validate values against
   vocabulary, do NOT require them

**Model selection:** Different enrichments may need different cognitive
levels. Structural tagging (embodied_patterns, relation_types) requires
understanding of metaphor theory — use Sonnet or Opus. Simple field
additions (sameAs URIs, wikidata IDs) can use Haiku.

**Gate:** A new entry created by the Miner arrives with correct
enrichment fields. The Assayer reviews them as part of normal QA.

### Phase 4: Sweep

Enrich the backlog of existing entries.

**Process:**
1. Survey script identifies unenriched entries
2. Batch into groups of 50-100 (grouped by kind or source frame)
3. Sweep agent processes each batch:
   - Read entry → read vocabulary → tag → validate → PR
4. Each batch is a short-lived branch, immediately merged
5. Tracking issue with checklist tracks progress

**Operational constraints:**
- Normal mining/prospecting/assaying continues uninterrupted
- Sweep PRs go through the same review pipeline (smelter → assayer)
- Sweep agent uses the model specified for this enrichment type
- Validator must pass (zero errors) before merge

**Gate:** Survey script reports 0 unenriched entries.

### Phase 5: Harden

Tighten enforcement after the sweep completes.

**Changes:**
1. Validator graduates from "recognize" to "warn on missing"
2. Miner PRs that forget enrichment fields get flagged
3. Eval suite runs as regression gate on new entries
4. Old entries grandfathered only until next touch

**Gate:** Validator enforces the field; no new entries merge without it.

### Phase 6: Exploit

Build features on the enriched data.

**Examples:**
- Search strategies (faceted, blended, text-only)
- API filters and facets
- Site UI (browse by structure, by embodied pattern)
- New eval suites that measure retrieval quality
- Cross-kind navigation (explanation stacks)

---

## Enrichment registry

Track all enrichment passes in one place.

| Enrichment | Fields | Model | Phase | Vocabulary doc | Tracking issue |
|---|---|---|---|---|---|
| Transfers & limits | `transfers[]`, `limits[]` | Sonnet | Phase 4 (sweeping) | enrichment-pipeline-design.md | — |
| Structural tags | `embodied_patterns[]`, `relation_types[]`, `structure`, `abstraction_level` | Sonnet | Phase 3 (integrating) | structural-enrichment-vocabulary.md | TBD |
| Abstract roles | `abstract_roles{}` (frames) | Sonnet | Phase 1 (designed) | structural-enrichment-vocabulary.md | — |
| Semantic web links | `sameAs[]` | Haiku | Phase 1 (designed) | TBD | — |

---

## Sweep agent design

The sweep agent is a lightweight, single-purpose agent that processes
batches of entries for a specific enrichment type.

### Interface

```
/enrich [--enrichment structural] [--batch-size 50] [--kind metaphor] [--dry-run]
```

When invoked without arguments, picks the next unenriched batch.

### Workflow

1. **Survey:** Identify entries missing the enrichment fields
2. **Batch:** Group into batches of N (default 50), optionally filtered by kind
3. **Tag:** For each entry in the batch:
   a. Read the entry markdown
   b. Read the vocabulary doc for allowed values
   c. Generate tags (using the model appropriate for this enrichment)
   d. Validate tags against vocabulary
   e. Insert fields into frontmatter (preserving all existing content)
4. **Validate:** Run `uv run scripts/validate.py validate`
5. **PR:** Open PR with the batch, labeled `needs-smelting`
6. **Track:** Update tracking issue checklist

### Safety constraints

- NEVER modify body text — enrichment is frontmatter-only
- NEVER remove or change existing frontmatter fields
- ALWAYS run validator before opening PR
- ALWAYS use the vocabulary doc as the source of truth for allowed values
- Skip entries that already have the enrichment fields (idempotent)

### Model selection by enrichment type

| Enrichment | Recommended model | Why |
|---|---|---|
| Structural tags | Sonnet | Requires understanding metaphor structure, embodied cognition theory |
| Transfers & limits | Sonnet | Requires generating novel propositions about source/target mappings |
| Abstract roles | Sonnet | Requires mapping frame-specific roles to abstract types |
| sameAs URIs | Haiku | Lookup task — match names to Wikidata/FrameNet IDs |
| Grounding audit | Opus | Requires domain expertise to judge proven/established/contested |

---

## Zero-outage guarantee

The markdown-first architecture makes this possible:

1. **All enrichment fields are optional.** An entry without
   `embodied_patterns` is still a valid entry. The validator doesn't
   reject it. The search system falls back to text-only.

2. **The validator is the gatekeeper of transitions.** It moves through
   states: ignore → recognize → warn → require. At each state, the
   catalog remains valid.

3. **Enrichment PRs merge into main continuously.** There is no
   "enrichment branch" that diverges. Each batch is a small PR that
   merges immediately, like any other content PR.

4. **Search degrades gracefully.** The search system checks whether
   enrichment fields exist and uses them when present:
   ```
   if entry has embodied_patterns → use faceted + text (blended)
   else → use text-only (baseline)
   ```
   As more entries get enriched, search quality improves gradually
   across the catalog, not all-at-once.

5. **Normal operations never pause.** Miners mine, prospectors prospect,
   assayers assay. The sweep agent runs alongside them. Merge conflicts
   are rare because enrichment only adds frontmatter fields, and normal
   operations typically add new entries (different files).
