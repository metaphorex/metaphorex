# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Validate prospect manifest files against Metaphorex schema rules.

Usage:
    uv run scripts/validate_manifest.py playbooks/*/manifest.json
    uv run scripts/validate_manifest.py playbooks/dead-metaphors/manifest.json
    uv run scripts/validate_manifest.py --verify-urls playbooks/*/manifest.json
    uv run scripts/validate_manifest.py playbooks/  # all manifests under dir

Checks:
    - Required fields present (slug, name, kind, source)
    - kind is a valid entry kind
    - name is title case (not ALL-CAPS, not lowercase)
    - source is 'archive' or 'llm'
    - source_frame and target_frame are not identical
    - Category slugs reference actual files in catalog/categories/
    - archive_url pages contain the candidate name (--verify-urls)
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
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


# ---------------------------------------------------------------------------
# archive_url verification helpers
# ---------------------------------------------------------------------------


def slug_keywords(slug: str) -> list[str]:
    """Extract meaningful keywords from a slug for page matching.

    Returns individual words from the slug, filtering out very short ones
    that would cause false positives.
    """
    parts = slug.split("-")
    # Keep words 3+ chars to avoid matching noise like "a", "is", "of"
    return [w for w in parts if len(w) >= 3]


def name_on_page(name: str, slug: str, page_text: str) -> bool:
    """Check if a candidate name or slug keyword appears on a page.

    Case-insensitive. Returns True if the full name OR at least half of
    the slug keywords appear on the page.
    """
    text_lower = page_text.lower()

    # Check full name (case-insensitive)
    if name.lower() in text_lower:
        return True

    # Check slug keywords — require at least half to match
    keywords = slug_keywords(slug)
    if not keywords:
        return True  # No meaningful keywords to check
    matches = sum(1 for kw in keywords if kw.lower() in text_lower)
    return matches >= max(1, len(keywords) // 2)


def fetch_page(url: str, timeout: int = 15) -> str | None:
    """Fetch a URL and return text content, or None on failure."""
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "metaphorex-manifest-validator/1.0"},
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read()
            # Try UTF-8 first, fall back to latin-1
            try:
                return data.decode("utf-8")
            except UnicodeDecodeError:
                return data.decode("latin-1")
    except (urllib.error.URLError, urllib.error.HTTPError, OSError) as exc:
        print(f"  FETCH-ERROR: {url} -- {exc}", file=sys.stderr)
        return None


# ---------------------------------------------------------------------------
# Core validation
# ---------------------------------------------------------------------------


def find_manifests(paths: list[Path]) -> list[Path]:
    """Resolve CLI args to manifest.json file paths."""
    result: list[Path] = []
    for path in paths:
        if path.is_dir():
            result.extend(sorted(path.rglob("manifest.json")))
        elif path.is_file() and path.name.endswith(".json"):
            result.append(path)
        else:
            print(f"SKIP: {path} is not a JSON file or directory", file=sys.stderr)
    return result


def validate_manifest(
    path: Path,
    valid_categories: set[str],
    *,
    verify_urls: bool = False,
) -> list[str]:
    """Validate a single manifest file. Returns a list of error/warning strings."""
    errors: list[str] = []
    warnings: list[str] = []
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

    slugs_seen: set[str] = set()
    for i, candidate in enumerate(candidates):
        slug = candidate.get("slug", f"candidate[{i}]")
        cpfx = f"{prefix}: {slug}"

        # Required fields
        for field in REQUIRED_CANDIDATE_FIELDS:
            if field not in candidate:
                errors.append(f"{cpfx}: missing required field '{field}'")

        # Duplicate slug check
        if "slug" in candidate:
            if candidate["slug"] in slugs_seen:
                warnings.append(f"{cpfx}: duplicate slug '{candidate['slug']}'")
            slugs_seen.add(candidate["slug"])

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

    # URL verification (only with --verify-urls)
    if verify_urls:
        page_cache: dict[str, str | None] = {}

        for candidate in candidates:
            cand_url = candidate.get("archive_url")
            if not cand_url:
                continue

            name = candidate.get("name", "")
            slug = candidate.get("slug", "")
            label = name or slug

            if cand_url not in page_cache:
                print(f"  Fetching {cand_url} ...", file=sys.stderr)
                page_cache[cand_url] = fetch_page(cand_url)

            page_text = page_cache[cand_url]
            if page_text is None:
                warnings.append(
                    f"{prefix}: candidate '{label}' -- "
                    f"could not fetch archive_url {cand_url}"
                )
                continue

            if not name_on_page(name, slug, page_text):
                warnings.append(
                    f"{prefix}: candidate '{label}' not found at "
                    f"archive_url {cand_url} -- possible URL/content mismatch"
                )

    return errors + warnings


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate prospect manifest files against Metaphorex schema rules",
    )
    parser.add_argument(
        "paths",
        nargs="+",
        type=Path,
        help="Manifest JSON files or directories containing them",
    )
    parser.add_argument(
        "--verify-urls",
        action="store_true",
        default=False,
        help="Fetch archive_url values and verify candidate names appear on the page",
    )
    args = parser.parse_args()

    valid_cats = category_slugs()
    manifests = find_manifests(args.paths)
    if not manifests:
        print("No manifest files found.", file=sys.stderr)
        sys.exit(1)

    all_errors: list[str] = []
    for mf in manifests:
        print(f"Validating {mf} ...", file=sys.stderr)
        all_errors.extend(
            validate_manifest(mf, valid_cats, verify_urls=args.verify_urls)
        )

    if all_errors:
        print(f"\n{len(all_errors)} issue(s):\n")
        for e in all_errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print(f"\nAll {len(manifests)} manifest(s) valid.")
        sys.exit(0)


if __name__ == "__main__":
    main()
