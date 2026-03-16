# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-frontmatter>=1.1.0",
# ]
# ///
"""Reclassify paradigm entries to mental-model or metaphor where appropriate.

Usage:
    uv run scripts/reclassify_paradigms.py              # apply changes
    uv run scripts/reclassify_paradigms.py --dry-run    # preview changes
"""

from __future__ import annotations

import sys
from pathlib import Path

import frontmatter

ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = ROOT / "catalog" / "entries"

# slug -> new kind (only entries that change)
RECLASSIFY: dict[str, str] = {
    # Cognitive moves
    "inversion": "mental-model",
    "second-order-thinking": "mental-model",
    "first-principles-thinking": "mental-model",
    "checklist-approach": "mental-model",
    "scenario-analysis": "mental-model",
    "two-track-analysis": "mental-model",
    "bayesian-updating": "mental-model",
    "falsification": "mental-model",
    # Predictive lenses / empirical regularities
    "regression-to-the-mean": "mental-model",
    "network-effects": "mental-model",
    "compounding": "mental-model",
    "power-laws": "mental-model",
    "nonlinearity": "mental-model",
    "feedback-loops": "mental-model",
    "activation-energy": "mental-model",
    "critical-mass": "mental-model",
    "catalysts": "mental-model",
    "red-queen-effect": "mental-model",
    "social-proof": "mental-model",
    "reciprocity": "mental-model",
    "lollapalooza-effect": "mental-model",
    "incentive-caused-bias": "mental-model",
    "information-asymmetry": "mental-model",
    "principal-agent-problem": "mental-model",
    "opportunity-cost": "mental-model",
    "comparative-advantage": "mental-model",
    "leverage": "mental-model",
    "margin-of-safety": "mental-model",
    "mr-market": "mental-model",
    "man-with-a-hammer": "mental-model",
    "redundancy": "mental-model",
    "system-resilience-vs-fragility": "mental-model",
    "scale-economies": "mental-model",
    "switching-costs": "mental-model",
    "niche-specialization": "mental-model",
    "economic-moats": "mental-model",
    "the-map-is-not-the-territory": "mental-model",
    # Razors
    "hanlons-razor": "mental-model",
    "occams-razor": "mental-model",
    # Named frameworks / meta-models
    "circle-of-competence": "mental-model",
    "latticework-of-mental-models": "mental-model",
    # Genuine A->B metaphor systems
    "the-conduit-metaphor": "metaphor",
    "event-structure": "metaphor",
}

# Slugs whose source_frame is artificial (the frame IS the native domain,
# not a metaphorical source). Remove source_frame for these.
REMOVE_SOURCE_FRAME: set[str] = {
    "comparative-advantage",    # source_frame: economics (IS economics)
    "compounding",              # source_frame: economics (IS economics)
    "falsification",            # source_frame: intellectual-inquiry (IS the domain)
    "incentive-caused-bias",    # source_frame: economics (IS economics)
    "information-asymmetry",    # source_frame: economics (IS economics)
    "opportunity-cost",         # source_frame: economics (IS economics)
    "principal-agent-problem",  # source_frame: economics (IS economics)
}


def main() -> None:
    dry_run = "--dry-run" in sys.argv

    if dry_run:
        print("DRY RUN — no files will be modified\n")

    changes = 0

    for slug, new_kind in sorted(RECLASSIFY.items()):
        path = ENTRIES_DIR / f"{slug}.md"
        if not path.exists():
            print(f"  SKIP {slug}: file not found")
            continue

        post = frontmatter.load(path)
        meta = post.metadata
        old_kind = meta.get("kind")
        modified = False
        actions: list[str] = []

        # 1. Reclassify kind
        if old_kind != new_kind:
            actions.append(f"kind: {old_kind} -> {new_kind}")
            if not dry_run:
                meta["kind"] = new_kind
            modified = True

        # 2. Remove artificial source_frame
        if slug in REMOVE_SOURCE_FRAME and "source_frame" in meta:
            actions.append(f"remove source_frame: {meta['source_frame']}")
            if not dry_run:
                del meta["source_frame"]
            modified = True

        # 3. Remove applies_to for mental-model entries (validator forbids it)
        if new_kind == "mental-model" and "applies_to" in meta:
            actions.append(f"remove applies_to: {meta['applies_to']}")
            if not dry_run:
                del meta["applies_to"]
            modified = True

        if modified:
            changes += 1
            print(f"  {'WOULD ' if dry_run else ''}UPDATE {slug}: {'; '.join(actions)}")
            if not dry_run:
                frontmatter.dump(post, path)

    print(f"\n{'Would change' if dry_run else 'Changed'} {changes} file(s).")


if __name__ == "__main__":
    main()
