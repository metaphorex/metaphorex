# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-frontmatter>=1.1.0",
# ]
# ///
"""Backfill provenance field on existing mappings.

Usage:
    uv run scripts/backfill_provenance.py          # dry run
    uv run scripts/backfill_provenance.py --apply  # write changes
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import frontmatter

ROOT = Path(__file__).resolve().parent.parent
MAPPINGS_DIR = ROOT / "catalog" / "mappings"
PLAYBOOKS_DIR = ROOT / "playbooks"

# Map: playbook slug -> provenance work slug(s)
# Most playbooks map 1:1 to a work. Some need splitting.
PLAYBOOK_TO_PROVENANCE: dict[str, str] = {
    "lakoff-johnson-mwlb": "lakoff-johnson-mwlb",
    "hacker-laws": "hacker-laws",
    "munger-mental-models": "munger-poor-charlies-almanack",
    "cognitive-linguistics-canon": "osaka-master-metaphor-list",
    # design-patterns has no manifest, skip for now
    # sw-eng-vernacular is community-sourced, no single work
    # unix-c-metaphors is community-sourced, no single work
    # dead-metaphors is community-sourced, no single work
    # active-ai-metaphors is a vein, no attribution
}

# Jungian archetypes need per-mapping attribution
JUNGIAN_PROVENANCE: dict[str, str] = {
    "the-self": "jung-aion",
    "the-shadow": "jung-aion",
    "the-anima-animus": "jung-aion",
    "the-persona": "jung-two-essays",
    "the-hero": "jung-symbols-of-transformation",
    "the-great-mother": "jung-archetypes-collective-unconscious",
    "the-wise-old-man": "jung-archetypes-collective-unconscious",
    "the-divine-child": "jung-archetypes-collective-unconscious",
    "the-maiden": "jung-archetypes-collective-unconscious",
    "the-senex": "jung-archetypes-collective-unconscious",
    "the-shapeshifter": "jung-archetypes-collective-unconscious",
}


def load_manifest_slugs(playbook_slug: str) -> set[str]:
    """Load candidate slugs from a playbook's manifest.json."""
    manifest_path = PLAYBOOKS_DIR / playbook_slug / "manifest.json"
    if not manifest_path.exists():
        return set()
    data = json.loads(manifest_path.read_text())
    # Manifests are dicts with a "candidates" array
    candidates = data.get("candidates", []) if isinstance(data, dict) else data
    return {entry["slug"] for entry in candidates if "slug" in entry}


def main() -> None:
    apply = "--apply" in sys.argv
    updated = 0
    skipped = 0

    # Build slug -> provenance mapping
    slug_to_provenance: dict[str, str] = {}

    # From playbook manifests
    for playbook_slug, work_slug in PLAYBOOK_TO_PROVENANCE.items():
        manifest_slugs = load_manifest_slugs(playbook_slug)
        for s in manifest_slugs:
            slug_to_provenance[s] = work_slug

    # Jungian overrides
    slug_to_provenance.update(JUNGIAN_PROVENANCE)

    # Process all mappings
    for path in sorted(MAPPINGS_DIR.glob("*.md")):
        post = frontmatter.load(path)
        slug = post.metadata.get("slug", path.stem)

        if "provenance" in post.metadata:
            skipped += 1
            continue

        if slug not in slug_to_provenance:
            continue

        work_slug = slug_to_provenance[slug]
        print(f"  {slug} -> {work_slug}")

        if apply:
            post.metadata["provenance"] = work_slug
            path.write_text(frontmatter.dumps(post) + "\n")

        updated += 1

    mode = "updated" if apply else "would update"
    print(f"\n{mode} {updated} mappings, skipped {skipped} (already set)")


if __name__ == "__main__":
    main()
