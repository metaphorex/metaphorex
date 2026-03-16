# Schema Migration Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Migrate 445 catalog entries to the new 5-kind schema, update the validator, CONTRIBUTING.md, and agent skill — shipping as a single PR.

**Architecture:** Regex-based migration script (preserves exact file formatting), then validator rewrite to enforce the new rules. Phase 1 enforces kinds/fields; Phase 2 (later PR) enforces `transfers`/`limits` min counts after content enrichment.

**Tech Stack:** Python 3.11+, python-frontmatter (PEP 723 inline deps), uv

---

### Task 1: Create the migration script skeleton

**Files:**
- Create: `scripts/migrate_schema_v2.py`

**Step 1: Write the script with PEP 723 header and CLI**

```python
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-frontmatter>=1.1.0",
# ]
# ///
"""Migrate Metaphorex catalog to v2 schema.

One-shot migration: renames kinds, replaces target_frame with applies_to,
renames body section headings. Idempotent — safe to re-run.

Usage:
    uv run scripts/migrate_schema_v2.py              # migrate all entries
    uv run scripts/migrate_schema_v2.py --dry-run     # show changes without writing
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import frontmatter

ROOT = Path(__file__).resolve().parent.parent
MAPPINGS_DIR = ROOT / "catalog" / "mappings"


def migrate_frontmatter(meta: dict) -> tuple[dict, list[str]]:
    """Apply frontmatter transforms. Returns (new_meta, list_of_changes)."""
    changes: list[str] = []

    # Kind renames
    kind = meta.get("kind")
    if kind == "conceptual-metaphor":
        meta["kind"] = "metaphor"
        changes.append("kind: conceptual-metaphor → metaphor")
    elif kind == "dead-metaphor":
        meta["kind"] = "metaphor"
        meta["dead"] = True
        changes.append("kind: dead-metaphor → metaphor + dead: true")
    elif kind == "cross-field-mapping":
        meta["kind"] = "metaphor"
        changes.append("kind: cross-field-mapping → metaphor")

    # target_frame → applies_to
    if "target_frame" in meta:
        target = meta.pop("target_frame")
        meta["applies_to"] = [target]
        changes.append(f"target_frame: {target} → applies_to: [{target}]")

    return meta, changes


def migrate_body(content: str) -> tuple[str, list[str]]:
    """Rename body section headings. Returns (new_content, list_of_changes)."""
    changes: list[str] = []

    renames = {
        "## What It Brings": "## Transfers",
        "## Where It Breaks": "## Limits",
    }

    for old, new in renames.items():
        if old in content:
            content = content.replace(old, new, 1)
            changes.append(f"section: {old} → {new}")

    return content, changes


def migrate_file(path: Path, dry_run: bool = False) -> list[str]:
    """Migrate a single file. Returns list of changes made."""
    post = frontmatter.load(path)

    meta, fm_changes = migrate_frontmatter(post.metadata)
    post.metadata = meta

    content, body_changes = migrate_body(post.content)
    post.content = content

    all_changes = fm_changes + body_changes
    if all_changes and not dry_run:
        path.write_text(frontmatter.dumps(post) + "\n")

    return all_changes


def main() -> None:
    dry_run = "--dry-run" in sys.argv

    migrated = 0
    skipped = 0
    total_changes: list[str] = []

    for path in sorted(MAPPINGS_DIR.glob("*.md")):
        changes = migrate_file(path, dry_run=dry_run)
        if changes:
            migrated += 1
            prefix = "[DRY RUN] " if dry_run else ""
            print(f"{prefix}{path.name}:")
            for c in changes:
                print(f"  - {c}")
            total_changes.extend(changes)
        else:
            skipped += 1

    verb = "would migrate" if dry_run else "migrated"
    print(f"\n{verb} {migrated} entries, skipped {skipped} (already current)")
    print(f"total changes: {len(total_changes)}")


if __name__ == "__main__":
    main()
```

**Step 2: Run dry-run to verify**

Run: `uv run scripts/migrate_schema_v2.py --dry-run`
Expected: output showing ~445 entries with kind renames, target_frame → applies_to, and section renames. Zero errors.

**Step 3: Verify round-trip fidelity on one file**

Run: `diff <(cat catalog/mappings/bikeshedding.md) <(uv run scripts/migrate_schema_v2.py --dry-run && cat catalog/mappings/bikeshedding.md)`
Expected: files are identical (dry-run doesn't write)

**Human verification:** Skim the dry-run output. Every `conceptual-metaphor` should become `metaphor`. Every `dead-metaphor` should become `metaphor + dead: true`. Every `target_frame` should become `applies_to: [x]`. Every `## What It Brings` should become `## Transfers`. Every `## Where It Breaks` should become `## Limits`.

**Step 4: Commit**

```bash
git checkout -b schema/v2-migration
git add scripts/migrate_schema_v2.py
git commit -m "feat: add schema v2 migration script

Renames kinds (conceptual-metaphor → metaphor, dead-metaphor → metaphor + dead: true),
replaces target_frame with applies_to, renames body sections."
```

---

### Task 2: Run the migration

**Files:**
- Modify: all 445 files in `catalog/mappings/`

**Step 1: Run the migration (for real)**

Run: `uv run scripts/migrate_schema_v2.py`
Expected: `migrated 445 entries, skipped 0`

**Step 2: Spot-check diffs on representative entries**

Run: `git diff catalog/mappings/bikeshedding.md` (dead-metaphor → metaphor + dead: true)
Expected: `kind: dead-metaphor` → `kind: metaphor` + `dead: true` added, `target_frame: collaborative-work` → `applies_to: [collaborative-work]`, `## What It Brings` → `## Transfers`, `## Where It Breaks` → `## Limits`

Run: `git diff catalog/mappings/survival-of-the-fittest.md` (paradigm — should only get target_frame rename + section renames)
Expected: `target_frame: competition` → `applies_to: [competition]`, section renames, kind unchanged

Run: `git diff catalog/mappings/the-commons.md` (archetype — same as paradigm)
Expected: `target_frame: shared-resources` → `applies_to: [shared-resources]`, section renames, kind unchanged

**Step 3: Check diff stats**

Run: `git diff --stat | tail -5`
Expected: ~445 files changed. No deletions of content lines (only heading renames and frontmatter field swaps).

**Step 4: Verify idempotency**

Run: `uv run scripts/migrate_schema_v2.py`
Expected: `migrated 0 entries, skipped 445 (already current)`

**Human verification:** Run `git diff catalog/mappings/bottleneck.md` and read the full diff. Confirm body prose is identical except for the two heading renames. Confirm frontmatter changes are exactly what's expected.

**Step 5: Commit**

```bash
git add catalog/mappings/
git commit -m "chore: migrate 445 catalog entries to v2 schema

Kind renames: conceptual-metaphor → metaphor (292), dead-metaphor → metaphor + dead: true (62).
Field renames: target_frame → applies_to across all entries.
Section renames: 'What It Brings' → 'Transfers', 'Where It Breaks' → 'Limits'."
```

---

### Task 3: Update validator — constants and required fields

**Files:**
- Modify: `scripts/validate.py`

**Step 1: Update VALID_KINDS, REQUIRED_MAPPING_FIELDS, REQUIRED_MAPPING_SECTIONS**

In `scripts/validate.py`, replace the constants at the top of the file:

```python
VALID_KINDS = {
    "metaphor",
    "pattern",
    "archetype",
    "paradigm",
    "mental-model",
}

REQUIRED_MAPPING_FIELDS = {"slug", "name", "kind", "categories", "author", "created", "updated"}

# ... keep REQUIRED_FRAME_FIELDS, REQUIRED_CATEGORY_FIELDS, REQUIRED_WORK_FIELDS unchanged ...

REQUIRED_MAPPING_SECTIONS = {"Transfers", "Limits", "Expressions"}
```

Add new constants after `VALID_WORK_TYPES`:

```python
VALID_GROUNDING = {"proven", "established", "folk", "contested"}
REJECTED_FIELDS = {"target_frame", "structural_properties", "failure_conditions"}
REJECTED_KINDS = {"conceptual-metaphor", "dead-metaphor", "cross-field-mapping"}
```

**Step 2: Run the validator to see what breaks**

Run: `uv run scripts/validate.py validate`
Expected: errors about missing `source_frame` on entries where it was optional before (paradigm, archetype), because the old validator required it globally. We'll fix the validation logic in the next step.

**Step 3: Commit**

```bash
git add scripts/validate.py
git commit -m "refactor: update validator constants for v2 schema

New VALID_KINDS (5-kind taxonomy), REQUIRED_MAPPING_FIELDS (source_frame
now conditional), REQUIRED_MAPPING_SECTIONS (renamed headings)."
```

---

### Task 4: Update validator — new validation rules in validate_mapping

**Files:**
- Modify: `scripts/validate.py`

**Step 1: Rewrite the validate_mapping function**

Replace the `validate_mapping` function body with the new logic. The full function:

```python
def validate_mapping(path: Path, frame_slugs: set[str], category_slugs: set[str],
                     mapping_slugs: set[str], work_slugs: set[str],
                     errors: list[str], warnings: list[str]) -> None:
    post = frontmatter.load(path)
    meta = post.metadata
    prefix = f"catalog/mappings/{path.name}"

    # Check required fields
    for field in REQUIRED_MAPPING_FIELDS:
        if field not in meta:
            errors.append(f"{prefix}: missing required field '{field}'")

    # Slug matches filename
    if "slug" in meta and meta["slug"] != path.stem:
        errors.append(f"{prefix}: slug '{meta['slug']}' doesn't match filename '{path.stem}'")

    # Kind validation
    kind = meta.get("kind")
    if kind in REJECTED_KINDS:
        errors.append(f"{prefix}: deprecated kind '{kind}' — run migration script")
    elif kind is not None and kind not in VALID_KINDS:
        errors.append(f"{prefix}: invalid kind '{kind}' (valid: {', '.join(sorted(VALID_KINDS))})")

    # Rejected fields
    for field in REJECTED_FIELDS:
        if field in meta:
            errors.append(f"{prefix}: deprecated field '{field}' — use new schema")

    # source_frame: required for metaphor, optional for others
    if kind == "metaphor" and "source_frame" not in meta:
        errors.append(f"{prefix}: metaphor kind requires 'source_frame'")

    # source_frame reference check (when present)
    if "source_frame" in meta and meta["source_frame"] not in frame_slugs:
        errors.append(f"{prefix}: source_frame '{meta['source_frame']}' not found in frames/")

    # applies_to: forbidden for mental-model, must be list when present
    if kind == "mental-model" and "applies_to" in meta:
        errors.append(f"{prefix}: mental-model kind must not have 'applies_to'")
    if "applies_to" in meta:
        if not isinstance(meta["applies_to"], list):
            errors.append(f"{prefix}: 'applies_to' must be a list")
        else:
            for at in meta["applies_to"]:
                if at not in frame_slugs:
                    errors.append(f"{prefix}: applies_to frame '{at}' not found in frames/")

    # dead flag: metaphor only
    if meta.get("dead") and kind != "metaphor":
        errors.append(f"{prefix}: 'dead: true' only valid for metaphor kind")

    # grounding enum
    if "grounding" in meta and meta["grounding"] not in VALID_GROUNDING:
        errors.append(f"{prefix}: invalid grounding '{meta['grounding']}' (valid: {', '.join(sorted(VALID_GROUNDING))})")

    # Category references
    for cat in meta.get("categories", []):
        if cat not in category_slugs:
            errors.append(f"{prefix}: category '{cat}' not found in categories/")

    # Provenance reference
    if "provenance" in meta and meta["provenance"] not in work_slugs:
        errors.append(f"{prefix}: provenance '{meta['provenance']}' not found in works/")

    # Related references (warnings, not errors)
    for rel in meta.get("related", []):
        if rel not in mapping_slugs:
            warnings.append(f"{prefix}: related mapping '{rel}' not found in mappings/")

    # Required sections
    sections = parse_sections(post.content)
    for section in REQUIRED_MAPPING_SECTIONS:
        if section not in sections:
            errors.append(f"{prefix}: missing required section '## {section}'")
        elif not sections[section]:
            errors.append(f"{prefix}: section '## {section}' is empty")
```

**Step 2: Run the validator**

Run: `uv run scripts/validate.py validate`
Expected: `All content valid.` with zero errors and zero warnings. If any errors appear, fix them before proceeding.

**Human verification:** Run the validator. It must exit 0. If it doesn't, read the errors — they'll tell you exactly which entries have problems and what the issue is.

**Step 3: Commit**

```bash
git add scripts/validate.py
git commit -m "feat: enforce v2 schema rules in validator

Rejects deprecated kinds and fields, enforces source_frame for metaphor,
forbids applies_to on mental-model, validates grounding enum, dead flag
metaphor-only. Phase 1: transfers/limits not yet enforced."
```

---

### Task 5: Handle validation edge cases

**Files:**
- Modify: `scripts/validate.py` (potentially)
- Modify: individual catalog entries (if needed)

**Step 1: Run validator and collect any remaining errors**

Run: `uv run scripts/validate.py validate 2>&1`
Expected: zero errors. If there ARE errors, they likely fall into:

- Entries missing `source_frame` that are `kind: metaphor` — these need investigation. Were they paradigms miscategorized as conceptual-metaphor?
- `applies_to` values that don't exist as frames — expected, since `target_frame` values were already validated against frames. These should still pass since applies_to references the same frame slugs.

**Step 2: Fix any entries with errors**

If a `metaphor` entry lacks `source_frame`, investigate:
- Did the old entry have `source_frame`? (It must have — it was required.) Check `git show HEAD:catalog/mappings/<file>` to confirm.
- If the migration introduced the issue, fix the migration script and re-run.

**Step 3: Confirm zero errors**

Run: `uv run scripts/validate.py validate`
Expected: `All content valid.`

**Step 4: Commit fixes if any**

```bash
git add -A catalog/mappings/ scripts/
git commit -m "fix: resolve edge-case validation errors from migration"
```

---

### Task 6: Update CONTRIBUTING.md — schema spec

**Files:**
- Modify: `CONTRIBUTING.md`

**Step 1: Update the "What to contribute" section**

Replace the paragraph starting "Metaphorex catalogs metaphors from all domains" and the four-bullet kind list with:

```markdown
Metaphorex catalogs metaphors from all domains, not just software. Every
entry is one of five kinds:

- **Metaphors** — specific A→B mappings where the source domain illuminates
  the target (e.g., "argument is war", "data flow is fluid flow"). Includes
  dead metaphors (`dead: true`) where the source domain is forgotten but
  structurally recoverable (bottleneck, firewall, bug).
- **Patterns** — structural solutions to recurring design problems. The source
  frame is often thin or vestigial; the value is in the structural solution
  (Observer, Factory, Facade).
- **Archetypes** — narrative or character universals appearing across cultures
  and domains (The Commons, The Trickster, Ouroboros).
- **Paradigms** — philosophies or worldviews with a position, operating within
  domains. You can agree or disagree with a paradigm (DRY, Worse is Better,
  Convention over Configuration).
- **Mental models** — cross-domain cognitive moves or predictive lenses with
  no inherent domain and no inherent position. Two subtypes: cognitive moves
  (Inversion, Second-Order Thinking) and predictive laws (Conway's Law,
  Goodhart's Law).
```

**Step 2: Update the editorial guide section headings**

Replace references to `What It Brings` and `Where It Breaks` with `Transfers` and `Limits` throughout the editorial guide. Specifically:

- The paragraph starting "**What It Brings** — the structural parallels" → rename heading and update description
- The paragraph starting "**Where It Breaks** — the failure modes" → rename heading and update description
- The quality bar checklist items referencing these sections
- The structured list format examples

Updated section descriptions:

```markdown
**Transfers** — the structural parallels between source and target.
Not "this is interesting" but "here is how the source domain's structure
maps onto the target domain, and what that mapping makes visible." Lead
with the core structural insight, then enumerate specific parallels as
labeled list items. Each parallel should name what the source contributes
that the target domain lacks on its own.

**Limits** — the failure modes of the mapping. Where does the
metaphor mislead, obscure, or import false assumptions? This section earns
its keep. Every metaphor has blind spots; a catalog entry that doesn't name
them is marketing, not analysis. Be specific: name the structural mismatch,
explain what it hides, give an example of the real-world consequence.
```

Updated quality bar items:

```markdown
- [ ] **"Transfers" names structural parallels, not vibes.**
- [ ] **"Limits" is substantive and specific.**
```

Updated structured list format:

```markdown
**Transfers** (key structural parallels):

**Limits** (failure modes):
```

**Step 3: Add new schema fields to the frontmatter example**

Find the entry frontmatter example in CONTRIBUTING.md (in the "Entry frontmatter" subsection) and add a note about new fields:

```markdown
### Mapping frontmatter

```yaml
slug: argument-is-war          # must match filename
name: Argument Is War
kind: metaphor                 # metaphor | pattern | archetype | paradigm | mental-model
source_frame: war              # required for metaphor; optional for others
applies_to: [argumentation]    # optional; absent for mental-model
categories: [cognitive-linguistics]
author: lakoff-johnson
contributors: []
related: []
created: 2026-03-07
updated: 2026-03-10
grounding: folk                # proven | established | folk | contested (default: folk, may omit)
dead: true                     # optional, metaphor kind only
```

**Step 4: Add kind decision table**

After the kind descriptions, add:

```markdown
### Kind decision criteria

| The item... | Kind |
|------------|------|
| Maps one domain onto another | `metaphor` |
| Term whose origin is forgotten but structure is recoverable | `metaphor` + `dead: true` |
| Narrative or character universal | `archetype` |
| Structural solution to a recurring design problem | `pattern` |
| Philosophy or position operating within domains | `paradigm` |
| Operational rule, design principle, legal maxim | `paradigm` |
| Cross-domain cognitive move or technique | `mental-model` |
| Named empirical regularity / predictive lens | `mental-model` |
| Razor (decision rule for underdetermination) | `mental-model` |
| Cannot generate 2+ structural propositions | **Discard** — file as nugget |

### Grounding

The `grounding` field signals epistemic status. Defaults to `folk` if omitted.

| Value | Meaning |
|-------|---------|
| `proven` | Formally derived, mathematically necessary, or tautological |
| `established` | Strong empirical grounding, well-replicated, accepted consensus |
| `folk` | Practitioner tradition, limited formal testing. **Default** |
| `contested` | Real evidence on both sides, live debate |
```

**Step 5: Run validator to confirm nothing broke**

Run: `uv run scripts/validate.py validate`
Expected: `All content valid.`

**Human verification:** Read the updated CONTRIBUTING.md. Confirm the 5-kind taxonomy is clear, section names are consistent (`Transfers`/`Limits`), and the frontmatter example matches the new schema.

**Step 6: Commit**

```bash
git add CONTRIBUTING.md
git commit -m "docs: update CONTRIBUTING.md for v2 schema

5-kind taxonomy, applies_to replaces target_frame, section renames
(Transfers/Limits), grounding field, kind decision table."
```

---

### Task 7: Update CLAUDE.md

**Files:**
- Modify: `CLAUDE.md`

**Step 1: Update the Content Schema section**

Replace the frontmatter example in CLAUDE.md:

```yaml
slug: argument-is-war          # kebab-case, matches filename
name: Argument Is War           # human-readable
kind: metaphor                  # metaphor | pattern | archetype | paradigm | mental-model
source_frame: war               # required for metaphor; optional for others
applies_to: [argumentation]     # optional; absent for mental-model
categories: [cognitive-linguistics]
author: lakoff-johnson
contributors: []
related: []
created: 2026-03-07             # ISO date, set on first creation
updated: 2026-03-10             # ISO date, updated on each edit
grounding: folk                  # proven | established | folk | contested (default: folk)
```

**Step 2: Update body section names**

Replace:
```
Required body sections: **What It Brings**, **Where It Breaks**, **Expressions**.
```
With:
```
Required body sections: **Transfers**, **Limits**, **Expressions**.
```

Replace:
```
"Where It Breaks" is the most important section — never a throwaway.
```
With:
```
"Limits" is the most important section — never a throwaway.
```

**Step 3: Commit**

```bash
git add CLAUDE.md
git commit -m "docs: update CLAUDE.md for v2 schema"
```

---

### Task 8: Update agent skill — metaphorex-schema

**Files:**
- Modify: `.claude/skills/metaphorex-schema/SKILL.md`

**Step 1: Rewrite the skill to reflect v2 schema**

Replace the full content of `.claude/skills/metaphorex-schema/SKILL.md` (after the frontmatter header) with updated schema. Key changes:

- Replace frontmatter example: `target_frame` → `applies_to`, add `grounding`, add `dead`
- Replace 2×2 kind grid with 5-kind list:
  - `metaphor` — specific A→B mapping (includes dead metaphors via `dead: true`)
  - `pattern` — structural solution to recurring design problem
  - `archetype` — narrative/character universal across domains
  - `paradigm` — philosophy/worldview with a position, operating within domains
  - `mental-model` — cross-domain cognitive move or predictive lens, no inherent domain
- Replace kind decision heuristics with the decision table from CONTRIBUTING.md
- Rename body sections: `## Transfers`, `## Limits`, `## Expressions`
- Add grounding field documentation
- Add proposition-writing guidance:
  - `[source] ...` for metaphor/pattern/archetype
  - `[paradigm] ...` for paradigm
  - `[model] ...` for mental-model (cognitive)
  - `[law] ...` for mental-model (predictive)
- Add discard filter: can't generate 2+ structural propositions → file as nugget

**Step 2: Verify the skill file is syntactically valid**

Read the file back and confirm the YAML frontmatter is valid and the markdown renders correctly.

**Human verification:** Read the updated skill. Confirm the 5-kind taxonomy is clear, the frontmatter example matches the validator, and the proposition-writing guidance is actionable.

**Step 3: Commit**

```bash
git add .claude/skills/metaphorex-schema/SKILL.md
git commit -m "docs: update metaphorex-schema skill for v2 schema

5-kind taxonomy, applies_to, grounding, proposition-writing guidance,
discard filter, section renames."
```

---

### Task 9: Final validation and PR

**Files:**
- None (validation only)

**Step 1: Run full validation**

Run: `uv run scripts/validate.py validate`
Expected: `All content valid.` with exit code 0.

**Step 2: Run migration script to confirm idempotency**

Run: `uv run scripts/migrate_schema_v2.py`
Expected: `migrated 0 entries, skipped 445 (already current)`

**Step 3: Review full diff**

Run: `git diff main --stat`
Expected: ~445 catalog files + validate.py + migrate script + CONTRIBUTING.md + CLAUDE.md + skill file

Run: `git log --oneline main..HEAD`
Expected: 5-8 commits covering migration script, catalog migration, validator, docs, skill

**Step 4: Spot-check 5 random entries**

Run: `ls catalog/mappings/ | shuf | head -5 | while read f; do echo "=== $f ==="; head -20 "catalog/mappings/$f"; done`
Expected: all show `kind: metaphor` or `kind: paradigm` or `kind: archetype` (no old kind names), `applies_to: [...]` (no `target_frame`), sections named `## Transfers` and `## Limits`

**Human verification:** Open the PR diff on GitHub. Scan 3-4 entry diffs to confirm body content is preserved (only headings renamed). Confirm the validator file looks correct. Confirm CONTRIBUTING.md reads coherently.

**Step 5: Push and create PR**

```bash
git push -u origin schema/v2-migration
gh pr create --title "Schema v2: 5-kind taxonomy, applies_to, grounding" --body "$(cat <<'EOF'
## Summary

- Migrates all 445 catalog entries to v2 schema
- Renames kinds: `conceptual-metaphor` → `metaphor`, `dead-metaphor` → `metaphor` + `dead: true`
- Replaces `target_frame` with `applies_to: [x]`
- Renames body sections: "What It Brings" → "Transfers", "Where It Breaks" → "Limits"
- Updates validator to enforce new schema (Phase 1 — transfers/limits min counts deferred)
- Updates CONTRIBUTING.md, CLAUDE.md, and agent skill

## Issues

Closes #1452, closes #1453

## Test plan

- [ ] `uv run scripts/validate.py validate` passes with zero errors
- [ ] Migration script is idempotent (re-running shows 0 changes)
- [ ] Spot-check 5 random entries for correct frontmatter and section names
- [ ] Old kind names rejected by validator
- [ ] Old field names (`target_frame`) rejected by validator

🤖 Generated with [Claude Code](https://claude.com/claude-code)
EOF
)"
```
