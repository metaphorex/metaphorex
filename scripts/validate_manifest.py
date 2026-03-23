# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Validate prospect manifest files against Metaphorex schema rules.

Usage:
    uv run scripts/validate_manifest.py playbooks/my-project/manifest.json
    uv run scripts/validate_manifest.py playbooks/*/manifest.json

Exits non-zero if any validation errors are found.
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

VALID_SOURCES = {"archive", "llm"}

REQUIRED_CANDIDATE_FIELDS = {"slug", "name", "kind", "source"}


def is_title_case(name: str) -> bool:
    """Check that a name is title case -- not ALL-CAPS or all-lowercase.

    Title case means each word starts with an uppercase letter. We allow
    short words (a, an, the, is, of, etc.) to be lowercase, and we allow
    single-letter words. ALL-CAPS strings with 2+ alpha chars fail.
    """
    if not name or not name.strip():
        return False
    # ALL-CAPS check: if every alpha char is uppercase and there are 2+ alpha
    alpha_chars = [c for c in name if c.isalpha()]
    if len(alpha_chars) >= 2 and all(c.isupper() for c in alpha_chars):
        return False
    # All-lowercase check: if every alpha char is lowercase
    if len(alpha_chars) >= 2 and all(c.islower() for c in alpha_chars):
        return False
    return True


def validate_candidate(candidate: dict, index: int) -> list[str]:
    """Validate a single candidate entry. Returns list of error messages."""
    errors = []
    prefix = f"candidate[{index}]"

    slug = candidate.get("slug", "<unknown>")
    if slug != "<unknown>":
        prefix = f"candidate '{slug}'"

    # Required fields
    missing = REQUIRED_CANDIDATE_FIELDS - set(candidate.keys())
    if missing:
        errors.append(f"{prefix}: missing required fields: {sorted(missing)}")

    # kind validation
    kind = candidate.get("kind")
    if kind is not None and kind not in VALID_KINDS:
        errors.append(
            f"{prefix}: invalid kind '{kind}' "
            f"(must be one of: {', '.join(sorted(VALID_KINDS))})"
        )

    # name validation (title case)
    name = candidate.get("name")
    if name is not None and not is_title_case(name):
        errors.append(
            f"{prefix}: name '{name}' is not title case"
        )

    # source validation
    source = candidate.get("source")
    if source is not None and source not in VALID_SOURCES:
        errors.append(
            f"{prefix}: invalid source '{source}' "
            f"(must be one of: {', '.join(sorted(VALID_SOURCES))})"
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
            f"{prefix}: source_frame and target_frame are identical "
            f"('{source_frame}')"
        )

    return errors


def validate_manifest(path: Path) -> list[str]:
    """Validate a manifest file. Returns list of error messages."""
    errors = []

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"{path}: invalid JSON: {exc}"]

    if not isinstance(data, dict):
        return [f"{path}: expected a JSON object at top level"]

    candidates = data.get("candidates")
    if candidates is None:
        return [f"{path}: missing 'candidates' array"]

    if not isinstance(candidates, list):
        return [f"{path}: 'candidates' must be an array"]

    for i, candidate in enumerate(candidates):
        if not isinstance(candidate, dict):
            errors.append(f"{path}: candidate[{i}] is not an object")
            continue
        for err in validate_candidate(candidate, i):
            errors.append(f"{path}: {err}")

    return errors


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: uv run scripts/validate_manifest.py <manifest.json> ...", file=sys.stderr)
        return 2

    paths = [Path(arg) for arg in sys.argv[1:]]
    total_errors = 0

    for path in paths:
        if not path.exists():
            print(f"ERROR: {path} does not exist", file=sys.stderr)
            total_errors += 1
            continue

        errors = validate_manifest(path)
        for err in errors:
            print(f"  ERROR: {err}", file=sys.stderr)
        total_errors += len(errors)

    if total_errors == 0:
        print(f"OK: {len(paths)} manifest(s) validated, 0 errors")
        return 0
    else:
        print(f"\nFAILED: {total_errors} error(s) in {len(paths)} manifest(s)", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
