# Content Enrichment Pipeline — Implementation Plan

**Date:** 2026-03-15
**Status:** Draft
**Author:** fshot + Claude

---

## Goal

Add structured `transfers` and `limits` proposition lists to every catalog entry's YAML frontmatter (~445 entries). Each proposition is embedded individually for vector search by structural similarity. This is modeled as an import project where the "source" is the existing catalog.

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                   Parent Issue                               │
│   "Content enrichment: add transfers + limits to all entries"│
└──────────┬──────────────────────────────────────────────────┘
           │
           ├── Batch sub-issue 1 (pilot, 20 entries)
           ├── Batch sub-issue 2 (50 entries)
           ├── Batch sub-issue 3 (50 entries)
           │   ...
           └── Batch sub-issue N
```

**Playbook:** `playbooks/catalog-enrichment/playbook.md`
**Label flow:** `needs-enrichment` → `enriching` → `needs-smelting` → `needs-assay` → `approved` → auto-merge

## Tech Stack

- Python scripts (PEP 723 inline deps, `uv run`)
- GitHub Issues + Labels (orchestration)
- Claude Code agents (Miner, Smelter, Assayer)
- Existing validator (`scripts/validate.py`)

---

## 1. Proposition Schema

### Form by kind

| Kind | Prefix | Example |
|------|--------|---------|
| `metaphor` | `[source]` | `[war] has winners and losers determined by strategy and force` |
| `pattern` | `[source]` | `[observer] decouples state changes from notification of dependents` |
| `archetype` | `[source]` | `[trickster] violates rules to reveal their arbitrariness` |
| `paradigm` | `[paradigm]` | `[paradigm] explanatory power trumps predictive accuracy` |
| `mental-model` (cognitive) | `[model]` | `[model] agents overweight losses relative to equivalent gains` |
| `mental-model` (predictive) | `[law]` | `[law] work expands to fill the time available for its completion` |

### Quality criteria

Every proposition must satisfy three tests:

1. **Independently true of source domain.** The proposition is a genuine structural fact about the source, not a restatement of the mapping itself.
2. **Non-trivially false of 2+ similar domains (discrimination test).** If you swap in a topically adjacent but structurally different domain, the proposition becomes false. This is what makes the proposition useful for distinguishing entries.
3. **Relational, not attributive.** Describes a relationship or process, not a static attribute. "X is complex" fails. "X propagates failures upstream" passes.

### Min counts

| Kind | Min transfers | Min limits |
|------|--------------|------------|
| `metaphor` | 3 | 2 |
| `pattern` | 3 | 2 |
| `archetype` | 3 | 2 |
| `paradigm` | 2 | 2 |
| `mental-model` | 2 | 2 |

### Good vs bad propositions

**BAD propositions (and why):**

- `[source] involves flow` — also true of rivers, blood, traffic, electricity (fails discrimination)
- `[source] is complex` — attributive, not relational (fails relational check)
- `[source] maps onto the target in interesting ways` — restates the mapping itself (fails independence)
- `[source] has structure` — vacuously true of everything (fails discrimination)

**GOOD propositions (and why):**

- `[source] blockage at any stage propagates upstream` — false of rivers (flow around), traffic (propagates but differently), electricity (fails open or short)
- `[source] participants escalate commitment based on sunk investment` — specific relational structure, false of games (can forfeit), commerce (can cut losses)
- `[source] victory requires both strategy and execution under pressure` — false of puzzles (no opponent), false of voting (no execution phase)

---

## 2. Label Mechanism

### New labels

| Label | Color | Description |
|-------|-------|-------------|
| `needs-enrichment` | `#d4c5f9` | Batch sub-issue ready for Miner to enrich |
| `enriching` | `#bfd4f2` | Miner has claimed this batch |

### State transitions

```
                 ┌──────────────────┐
                 │ needs-enrichment │  (set on batch sub-issue creation)
                 └────────┬─────────┘
                          │  Miner claims
                          ▼
                 ┌──────────────────┐
                 │    enriching     │  (Miner working)
                 └────────┬─────────┘
                          │  Miner opens PR, removes enriching
                          ▼
                 ┌──────────────────┐
                 │ needs-smelting   │  (standard pipeline)
                 └────────┬─────────┘
                          │  Smelter validates
                          ▼
                 ┌──────────────────┐
                 │   needs-assay    │
                 └────────┬─────────┘
                          │  Assayer reviews
                          ▼
                 ┌──────────────────┐
                 │    approved      │  → auto-merge
                 └──────────────────┘
```

---

## 3. Agent Updates

### 3a. Miner — enrichment work type

The Miner currently creates new files. For enrichment, it reads existing entries and adds frontmatter.

**Behavior when processing a `needs-enrichment` issue:**

1. Read the batch manifest (list of entry slugs in the sub-issue body)
2. For each entry:
   a. Read the existing file from `catalog/mappings/<slug>.md`
   b. Parse the existing body sections (`## Transfers`, `## Limits`, `## Expressions`)
   c. Generate `transfers:` and `limits:` YAML lists based on body content and source domain knowledge
   d. Use the correct proposition prefix based on `kind`
   e. Insert the lists into the frontmatter, after `categories` and before `author`
3. Open one PR per batch sub-issue, linking to it
4. Remove `enriching` label, add `needs-smelting` label

**Key constraint:** The Miner must not alter existing body text. It only adds frontmatter fields.

### 3b. Smelter — mechanical validation of propositions

Add enrichment checks to Smelter's validation pass:

- `transfers` field exists and is a YAML list
- `limits` field exists and is a YAML list
- Transfer count meets minimum for the entry's kind
- Limit count meets minimum (2 for all kinds)
- Each proposition starts with the correct prefix for its kind
- No duplicate propositions within an entry
- No empty strings in lists

These are purely mechanical — the Smelter makes no judgment about content quality.

### 3c. Assayer — enrichment quality review

Add enrichment-specific quality checks:

| Check | Method | Fail action |
|-------|--------|-------------|
| Discrimination test | For each transfer, name 2 similar-but-different domains where it's false | Request changes with counter-examples |
| Relational check | Verify proposition describes relationship/process, not attribute | Flag attributive propositions |
| Form check | Prefix matches kind | Flag mismatches |
| Coverage check | Do propositions collectively capture the relational structure? | Flag gaps |
| Redundancy check | Are any propositions near-duplicates? | Flag for consolidation |

**Phase A (pilot):** Assayer reviews every proposition in every entry.
**Phase B (scale):** Assayer spot-checks 5 entries per batch of 50.

---

## 4. Phasing

### Phase A — Pilot (20 entries)

**Goal:** Prove the enrichment pipeline and calibrate the playbook.

- Select 20 entries covering all 5 kinds (at least 2 per kind, rest weighted toward metaphor)
- Prefer entries with strong existing body sections (good raw material)
- One batch sub-issue, one PR
- Full Assayer review of all 20
- Human reviews all 20 to calibrate proposition quality
- Iterate playbook based on findings

**Entry selection criteria:**
- At least 4 metaphors, 4 patterns, 4 archetypes, 4 paradigms, 4 mental-models
- Mix of "easy" (clear source domain) and "hard" (abstract source domain)
- Include at least 2 entries where the Transfers section is thin (stress test)

**Exit criteria:**
- All 20 entries pass Smelter validation
- Assayer approves all 20
- Human confirms proposition quality is sufficient for embedding
- Playbook updated with any lessons learned

### Phase B — Scale (~425 remaining entries)

**Goal:** Enrich all remaining entries at higher throughput.

- Batch by kind, ~50 entries per batch
- ~9 batch sub-issues
- Assayer spot-checks 5 per batch (10% sample)
- If spot-check fails >1 entry, escalate to full review of that batch

**Batching order:**
1. Metaphors (largest group, most practiced by Phase A)
2. Patterns
3. Archetypes
4. Paradigms
5. Mental-models

**Exit criteria:**
- All entries have `transfers` and `limits` in frontmatter
- Zero Smelter validation failures
- Spot-check pass rate ≥ 90% per batch

### Phase C — Enable strict validation

**Goal:** Make transfers/limits mandatory going forward.

- Update `scripts/validate.py` to enforce min counts
- Run validator against full catalog
- Fix any entries that fail (should be zero if Phase B completed)
- Merge validator update

---

## 5. Implementation Tasks

### Task 0: Terminology rename — "mappings" → "entries"

**What:** The term "mapping" no longer fits the full 5-kind taxonomy. A mental
model doesn't "map" anything; a razor doesn't have a source→target transfer.
Rename the user-facing term from "mapping" to "entry" across all prose,
agent prompts, skill files, CONTRIBUTING.md, CLAUDE.md, and the site.

The `catalog/mappings/` directory stays as-is (renaming it would break every
agent, script, and link). The frontmatter field names stay. Only the
*conceptual term* used in prose, agent instructions, and UI changes.

**Who:** Human (mechanical find-and-replace + editorial review)
**Files:**
- `CONTRIBUTING.md` — replace "mapping" / "mappings" with "entry" / "entries" in prose
- `CLAUDE.md` — same
- `.claude/skills/metaphorex-schema/SKILL.md` — same
- `.claude/agents/miner.md` — same
- `.claude/agents/assayer.md` — same
- `.claude/agents/smelter.md` — same
- `.claude/agents/prospector.md` — same
- `.claude/agents/surveyor.md` — same
- `site/` — any user-facing copy

**Caution:** Don't rename:
- `catalog/mappings/` directory
- Frontmatter field names (`mapping_slugs`, etc.)
- The `validate_mapping()` function name in `validate.py`
- The term "mapping" when it refers to the *conceptual metaphor relationship*
  (source→target mapping), not the content type

**Acceptance criteria:**
- grep for `\bmapping\b` in prose files returns only structural/relational uses
- Agent prompts say "entry" / "entries" when referring to catalog content
- `catalog/mappings/` directory unchanged

### Task 1: Create enrichment labels

**What:** Add `needs-enrichment` and `enriching` labels to the repo.
**Who:** Human (one-time setup)
**Files:** None (GitHub UI or `gh label create`)
**Acceptance criteria:**
- `gh label list` shows both labels with correct colors

### Task 2: Create parent issue

**What:** Create the parent issue for the enrichment project.
**Who:** Human or Prospector
**Files:** None (GitHub issue)
**Acceptance criteria:**
- Issue exists with title "Content enrichment: add transfers + limits to all entries"
- Body contains project overview, links to playbook, phasing summary
- Labels: `import-project`

### Task 3: Write enrichment playbook

**What:** Create the playbook that guides the Miner through enrichment work.
**Who:** Prospector
**Files:** `playbooks/catalog-enrichment/playbook.md`
**Acceptance criteria:**
- Contains proposition-writing guidance with forms by kind
- Contains quality rubric (discrimination test, relational check, coverage)
- Contains min counts table
- Contains good vs bad examples (at least 3 of each)
- Contains batch processing instructions
- Contains frontmatter insertion format specification

### Task 4: Update survey.py to detect needs-enrichment

**What:** Add `needs-enrichment` to the set of labels that `survey.py` detects, so the `/work` pipeline can dispatch Miners for enrichment alongside regular mining.
**Who:** Human or Smelter
**Files:** `scripts/survey.py`
**Acceptance criteria:**
- `needs-enrichment` issues appear in survey output
- `/work` command can find and dispatch enrichment work
- No regression in existing label detection

### Task 5: Update Miner for enrichment work type

**What:** Add enrichment mode to the Miner agent's capabilities.
**Who:** Human
**Files:**
- `.claude/agents/miner.md` (agent instructions)
- `.claude/commands/mine.md` (if dispatch logic needs updating)
**Acceptance criteria:**
- Miner can distinguish enrichment sub-issues from regular mining sub-issues (by label or issue body)
- Miner reads existing entry, generates propositions, inserts into frontmatter
- Miner uses correct prefix per kind
- Miner does not alter existing body text
- Miner opens PR linked to batch sub-issue

### Task 6: Update Smelter for proposition validation

**What:** Add mechanical proposition checks to Smelter's validation pass.
**Who:** Human
**Files:**
- `.claude/agents/smelter.md` (agent instructions)
- `scripts/validate.py` (add proposition format checks, gated behind a flag or as warnings until Phase C)
**Acceptance criteria:**
- Smelter checks: field existence, list format, min counts, prefix correctness, no duplicates
- Checks run as warnings (not errors) until Phase C
- No regression in existing validation

### Task 7: Update Assayer for enrichment quality review

**What:** Add enrichment-specific quality checks to Assayer's review process.
**Who:** Human
**Files:** `.claude/agents/assayer.md` (agent instructions)
**Acceptance criteria:**
- Assayer applies discrimination test, relational check, form check, coverage check
- Assayer knows to do full review in Phase A, spot-check in Phase B
- Review comments cite specific failing propositions with suggested fixes

### Task 8: Create pilot batch sub-issue

**What:** Select 20 entries and create the first batch sub-issue.
**Who:** Prospector
**Files:** None (GitHub issue)
**Acceptance criteria:**
- Sub-issue lists 20 slugs (at least 4 per kind)
- Sub-issue is a sub-issue of the parent enrichment issue
- Labeled `needs-enrichment`
- Entry selection covers easy and hard cases

### Task 9: Execute pilot batch

**What:** Miner enriches 20 entries, Smelter validates, Assayer reviews.
**Who:** Miner → Smelter → Assayer → Human
**Files:** 20 files in `catalog/mappings/`
**Acceptance criteria:**
- All 20 entries have `transfers` and `limits` in frontmatter
- Smelter passes all mechanical checks
- Assayer approves all 20
- Human reviews and confirms quality

### Task 10: Iterate playbook based on pilot

**What:** Update playbook with lessons from pilot review.
**Who:** Human or Prospector
**Files:** `playbooks/catalog-enrichment/playbook.md`
**Acceptance criteria:**
- Any quality issues found in pilot are addressed in updated guidance
- New examples added if recurring mistakes were found

### Task 11: Create scale batch sub-issues

**What:** Create ~9 batch sub-issues for remaining entries.
**Who:** Prospector (scripted)
**Files:** None (GitHub issues)
**Acceptance criteria:**
- All remaining entries assigned to a batch
- Batches grouped by kind, ~50 per batch
- All sub-issues labeled `needs-enrichment`
- All sub-issues linked to parent issue

### Task 12: Execute scale batches

**What:** Miner enriches all remaining entries across batches.
**Who:** Miner → Smelter → Assayer
**Files:** ~425 files in `catalog/mappings/`
**Acceptance criteria:**
- All entries have `transfers` and `limits`
- Smelter passes all batches
- Assayer spot-check pass rate ≥ 90% per batch

### Task 13: Enable strict validation

**What:** Flip validator to enforce transfers/limits min counts as errors.
**Who:** Human
**Files:** `scripts/validate.py`
**Acceptance criteria:**
- `uv run scripts/validate.py validate` enforces min counts
- Full catalog passes with zero errors
- Any failures are fixed before merge

---

## 6. Sequencing

```
Task 1 ─── Create labels ──────────────────────────────────┐
Task 2 ─── Create parent issue ────────────────────────────┤
Task 3 ─── Write playbook ────────────────────────────────┤
                                                            │
Task 4 ─── Update survey.py ──────────────────┐            │
Task 5 ─── Update Miner ─────────────────────┤            │
Task 6 ─── Update Smelter ───────────────────┤            │
Task 7 ─── Update Assayer ───────────────────┤            │
                                               │            │
                                               ▼            ▼
Task 8 ─── Create pilot batch ──────────────────────────────┤
                                                            │
Task 9 ─── Execute pilot ─────────────────────────────────┤
                                                            │
Task 10 ── Iterate playbook ──────────────────────────────┤
                                                            │
Task 11 ── Create scale batches ──────────────────────────┤
                                                            │
Task 12 ── Execute scale batches ─────────────────────────┤
                                                            │
Task 13 ── Enable strict validation ──────────────────────┘
```

**Parallelism:** Tasks 1–3 can run in parallel. Tasks 4–7 can run in parallel. Tasks 8–13 are sequential.

**Critical path:** Task 3 (playbook) → Task 9 (pilot) → Task 10 (iterate) → Task 12 (scale). The playbook quality determines everything downstream.

---

## 7. Risk Mitigation

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Propositions are too generic (fail discrimination) | High | Medium | Playbook has explicit bad examples; pilot catches this early |
| Miner generates attributive instead of relational propositions | Medium | Medium | Playbook emphasizes relational form; Assayer has explicit check |
| Wrong prefix for kind | Low | Low | Smelter catches mechanically |
| Body sections too thin to generate good propositions | Medium | High | Miner uses domain knowledge, not just body text; flag entries needing body enrichment first |
| Pilot reveals fundamental playbook problems | Medium | Medium | That's the point of the pilot; iterate before scale |
| Scale batches overwhelm review capacity | Low | Medium | Spot-check model (5 per 50) keeps review tractable |
| Frontmatter insertion corrupts existing content | Low | High | Smelter validates full file after insertion; PR diff review catches corruption |
| Embedding quality insufficient despite good propositions | Medium | Medium | Out of scope for this plan; separate evaluation after enrichment completes |

---

## 8. Out of Scope

- **Embedding pipeline** — how propositions get embedded is a separate concern
- **Vector search API** — consuming the embeddings is downstream
- **Body section rewriting** — this plan adds frontmatter only; body improvements are separate
- **New entry creation** — this plan enriches existing entries only
- **Frame/category enrichment** — only mappings get transfers/limits

---

## 9. Success Metrics

| Metric | Target |
|--------|--------|
| Entries with transfers + limits | 100% of catalog |
| Smelter validation pass rate | 100% |
| Assayer spot-check pass rate | ≥ 90% per batch |
| Pilot human review pass rate | ≥ 80% (iterate if lower) |
| Time to complete pilot | ≤ 1 day |
| Time to complete all batches | ≤ 1 week |
| Validator enforcing min counts | Enabled, zero failures |
