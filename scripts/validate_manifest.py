# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Validate prospect manifest files against Metaphorex schema rules.

Usage:
    uv run scripts/validate_manifest.py playbooks/*/manifest.json
    uv run scripts/validate_manifest.py playbooks/dead-metaphors/manifest.json

Checks:
    - Required fields present (slug, name, kind, source)
    - kind is a valid entry kind
    - name is title case (not ALL-CAPS, not lowercase)
    - source is 'archive' or 'llm'
    - source_frame and target_frame are not identical
    - Category slugs reference actual files in catalog/categories/
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATEGORIES_DIR = ROOT / "catalog" / "categories"

VALID_KINDS = {
    "metaphor",
    "pattern",
    "archetype",
    "paradigm",
    "mental-model",
}

VALID_SOURCES = {"archive", "llm"}

REQUIRED_CANDIDATE_FIELDS = {"slug", "name", "kind", "source"}


def is_title_case(name: str) -> bool:
    """Check if a name is title-case (not ALL-CAPS, not all-lowercase).

    Title case means at least one uppercase letter and at least one lowercase
    letter.  ALL-CAPS strings like "TIME IS MONEY" fail.  Single-word proper
    nouns like "Grok" pass.  Lowercase strings like "time is money" fail.
    """
    has_upper = any(c.isupper() for c in name)
    has_lower = any(c.islower() for c in name)
    return has_upper and has_lower


def category_slugs() -> set[str]:
    """Return the set of valid category slugs from catalog/categories/*.md filenames."""
    return {f.stem for f in CATEGORIES_DIR.glob("*.md")}


def validate_manifest(path: Path, valid_categories: set[str]) -> list[str]:
    """Validate a single manifest file. Returns a list of error strings."""
    errors: list[str] = []
    prefix = str(path)

    try:
        data = json.loads(path.read_text())
    except json.JSONDecodeError as e:
        errors.append(f"{prefix}: invalid JSON: {e}")
        return errors

    if not isinstance(data, dict):
        errors.append(f"{prefix}: manifest must be a JSON object")
        return errors

    candidates = data.get("candidates", [])
    if not isinstance(candidates, list):
        errors.append(f"{prefix}: 'candidates' must be a list")
        return errors

    if not candidates:
        errors.append(f"{prefix}: manifest has no candidates")
        return errors

    for i, candidate in enumerate(candidates):
        slug = candidate.get("slug", f"candidate[{i}]")
        cpfx = f"{prefix}: {slug}"

        # Required fields
        for field in REQUIRED_CANDIDATE_FIELDS:
            if field not in candidate:
                errors.append(f"{cpfx}: missing required field '{field}'")

        # kind validation
        kind = candidate.get("kind")
        if kind is not None and kind not in VALID_KINDS:
            errors.append(
                f"{cpfx}: invalid kind '{kind}' "
                f"(valid: {', '.join(sorted(VALID_KINDS))})"
            )

        # name casing validation
        name = candidate.get("name")
        if name is not None and not is_title_case(name):
            if name == name.upper():
                errors.append(f"{cpfx}: name '{name}' is ALL-CAPS, use title case")
            elif name == name.lower():
                errors.append(f"{cpfx}: name '{name}' is lowercase, use title case")
            else:
                errors.append(f"{cpfx}: name '{name}' is not title case")

        # source validation
        source = candidate.get("source")
        if source is not None and source not in VALID_SOURCES:
            errors.append(
                f"{cpfx}: invalid source '{source}' "
                f"(valid: {', '.join(sorted(VALID_SOURCES))})"
            )

        # source_frame != target_frame
        source_frame = candidate.get("source_frame")
        target_frame = candidate.get("target_frame")
        if (
            source_frame is not None
            and target_frame is not None
            and source_frame == target_frame
        ):
            errors.append(
                f"{cpfx}: source_frame and target_frame are identical "
                f"('{source_frame}')"
            )

        # category slug validation
        for cat in candidate.get("categories", []):
            if cat not in valid_categories:
                errors.append(
                    f"{cpfx}: category '{cat}' "
                    f"does not exist in catalog/categories/"
                )

    return errors


def main() -> None:
    valid_cats = category_slugs()

    if len(sys.argv) < 2:
        print(__doc__.strip())
        sys.exit(1)

    paths = [Path(p) for p in sys.argv[1:]]
    all_errors: list[str] = []

    for path in paths:
        if not path.exists():
            all_errors.append(f"{path}: file not found")
            continue
        all_errors.extend(validate_manifest(path, valid_cats))

    if all_errors:
        print(f"{len(all_errors)} error(s):\n")
        for e in all_errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print(f"All {len(paths)} manifest(s) valid.")
        sys.exit(0)


if __name__ == "__main__":
    main()
