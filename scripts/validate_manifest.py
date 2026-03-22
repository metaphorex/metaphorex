# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Manifest validator for Metaphorex prospect manifests.

Validates manifest.json files in playbooks/ against schema rules:
- kind must be one of: metaphor, pattern, archetype, paradigm, mental-model
- name must be title-case (not ALL-CAPS or all-lowercase)
- source_frame must differ from target_frame
- source must be one of: archive, llm

Usage:
    uv run scripts/validate_manifest.py                          # all manifests
    uv run scripts/validate_manifest.py playbooks/foo/manifest.json  # one file
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

VALID_KINDS = {"metaphor", "pattern", "archetype", "paradigm", "mental-model"}
VALID_SOURCES = {"archive", "llm"}


def is_all_caps(name: str) -> bool:
    """Return True if the name is ALL-CAPS (ignoring non-alpha chars)."""
    alpha = [c for c in name if c.isalpha()]
    return len(alpha) > 0 and all(c.isupper() for c in alpha)


def is_all_lower(name: str) -> bool:
    """Return True if the name is all-lowercase (ignoring non-alpha chars)."""
    alpha = [c for c in name if c.isalpha()]
    return len(alpha) > 0 and all(c.islower() for c in alpha)


def validate_manifest(path: Path) -> list[str]:
    """Validate a single manifest file. Returns list of error messages."""
    errors: list[str] = []

    try:
        data = json.loads(path.read_text())
    except json.JSONDecodeError as e:
        return [f"{path}: invalid JSON: {e}"]

    candidates = data.get("candidates", [])
    if not isinstance(candidates, list):
        return [f"{path}: 'candidates' is not a list"]

    for i, candidate in enumerate(candidates):
        slug = candidate.get("slug", f"<candidate {i}>")
        prefix = f"{path}: {slug}"

        # Validate kind
        kind = candidate.get("kind")
        if kind and kind not in VALID_KINDS:
            errors.append(
                f"{prefix}: invalid kind '{kind}' "
                f"(must be one of: {', '.join(sorted(VALID_KINDS))})"
            )

        # Validate name is title-case (not ALL-CAPS or all-lowercase)
        name = candidate.get("name", "")
        if is_all_caps(name):
            errors.append(f"{prefix}: name '{name}' is ALL-CAPS (use title case)")
        elif is_all_lower(name):
            errors.append(
                f"{prefix}: name '{name}' is all-lowercase (use title case)"
            )

        # Validate source_frame != target_frame
        source_frame = candidate.get("source_frame", "")
        target_frame = candidate.get("target_frame", "")
        if source_frame and target_frame and source_frame == target_frame:
            errors.append(
                f"{prefix}: source_frame '{source_frame}' "
                f"equals target_frame (same-domain mapping)"
            )

        # Validate source
        source = candidate.get("source")
        if source and source not in VALID_SOURCES:
            errors.append(
                f"{prefix}: invalid source '{source}' "
                f"(must be one of: {', '.join(sorted(VALID_SOURCES))})"
            )

    return errors


def main() -> int:
    args = sys.argv[1:]

    if args:
        paths = [Path(a) for a in args]
    else:
        paths = sorted((ROOT / "playbooks").glob("*/manifest.json"))

    if not paths:
        print("No manifest files found.")
        return 1

    total_errors: list[str] = []
    files_checked = 0

    for path in paths:
        if not path.exists():
            total_errors.append(f"{path}: file not found")
            continue
        files_checked += 1
        errors = validate_manifest(path)
        total_errors.extend(errors)

    for error in total_errors:
        print(f"ERROR: {error}", file=sys.stderr)

    if total_errors:
        print(
            f"\n{len(total_errors)} error(s) in {files_checked} manifest(s).",
            file=sys.stderr,
        )
        return 1
    else:
        print(f"OK: {files_checked} manifest(s) validated, no errors.")
        return 0


if __name__ == "__main__":
    sys.exit(main())
