# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Manifest validator for Prospector-generated manifest.json files.

Usage:
    uv run scripts/validate_manifest.py playbooks/my-project/manifest.json
    uv run scripts/validate_manifest.py playbooks/*/manifest.json

Validates each candidate entry against Metaphorex schema rules:
- kind is one of: metaphor, pattern, archetype, paradigm, mental-model
- name is title case (not ALL-CAPS, not all-lowercase)
- source_frame != target_frame (same-domain anti-pattern)
- source is one of: archive, llm
- Required fields present: slug, name, kind, source
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

VALID_KINDS = {
    "metaphor",
    "pattern",
    "archetype",
    "paradigm",
    "mental-model",
}

REJECTED_KINDS = {"conceptual-metaphor", "dead-metaphor", "cross-field-mapping"}

VALID_SOURCES = {"archive", "llm"}

REQUIRED_CANDIDATE_FIELDS = {"slug", "name", "kind", "source"}


def validate_manifest(path: Path) -> list[str]:
    """Validate a manifest.json file. Returns a list of error strings."""
    errors: list[str] = []

    try:
        data = json.loads(path.read_text())
    except json.JSONDecodeError as e:
        return [f"{path}: invalid JSON: {e}"]

    if not isinstance(data, dict):
        return [f"{path}: top-level value must be an object"]

    candidates = data.get("candidates", [])
    if not isinstance(candidates, list):
        return [f"{path}: 'candidates' must be an array"]

    for i, c in enumerate(candidates):
        prefix = f"{path}: candidate[{i}] ({c.get('slug', '???')})"

        # Required fields
        for field in REQUIRED_CANDIDATE_FIELDS:
            if field not in c:
                errors.append(f"{prefix}: missing required field '{field}'")

        # kind validation
        kind = c.get("kind")
        if kind is not None:
            if kind in REJECTED_KINDS:
                errors.append(
                    f"{prefix}: kind '{kind}' is not valid. "
                    f"Did you mean 'metaphor'? "
                    f"Allowed: {', '.join(sorted(VALID_KINDS))}"
                )
            elif kind not in VALID_KINDS:
                errors.append(
                    f"{prefix}: kind '{kind}' is not valid. "
                    f"Allowed: {', '.join(sorted(VALID_KINDS))}"
                )

        # name validation: not ALL-CAPS
        name = c.get("name")
        if isinstance(name, str) and len(name) > 1:
            alpha_chars = [ch for ch in name if ch.isalpha()]
            if alpha_chars and all(ch.isupper() for ch in alpha_chars):
                errors.append(
                    f"{prefix}: name '{name}' is ALL-CAPS. "
                    f"Use title case (e.g. 'Argument Is War')."
                )

        # source_frame != target_frame
        sf = c.get("source_frame")
        tf = c.get("target_frame")
        if sf and tf and sf == tf:
            errors.append(
                f"{prefix}: source_frame and target_frame are identical ('{sf}'). "
                f"A mapping must cross domains."
            )

        # source validation
        source = c.get("source")
        if source is not None and source not in VALID_SOURCES:
            errors.append(
                f"{prefix}: source '{source}' is not valid. "
                f"Allowed: {', '.join(sorted(VALID_SOURCES))}"
            )

    return errors


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: uv run scripts/validate_manifest.py <manifest.json> [...]", file=sys.stderr)
        return 1

    all_errors: list[str] = []
    files_checked = 0

    for arg in sys.argv[1:]:
        path = Path(arg)
        if not path.exists():
            all_errors.append(f"{path}: file not found")
            continue
        files_checked += 1
        all_errors.extend(validate_manifest(path))

    if all_errors:
        for err in all_errors:
            print(f"ERROR: {err}", file=sys.stderr)
        print(f"\n{len(all_errors)} error(s) in {files_checked} manifest(s).", file=sys.stderr)
        return 1

    print(f"{files_checked} manifest(s) validated, 0 errors.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
