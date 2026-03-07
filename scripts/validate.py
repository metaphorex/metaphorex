# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-frontmatter>=1.1.0",
# ]
# ///
"""Metaphorex content validator and extractor.

Usage:
    uv run scripts/validate.py validate          # validate all content
    uv run scripts/validate.py validate catalog/mappings/ # validate specific dir
    uv run scripts/validate.py extract            # emit JSON to stdout
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import frontmatter

ROOT = Path(__file__).resolve().parent.parent
CATALOG_DIR = ROOT / "catalog"
MAPPINGS_DIR = CATALOG_DIR / "mappings"
FRAMES_DIR = CATALOG_DIR / "frames"
CATEGORIES_DIR = CATALOG_DIR / "categories"

VALID_KINDS = {
    "conceptual-metaphor",
    "design-pattern",
    "archetype",
    "cross-field-mapping",
    "dead-metaphor",
    "paradigm",
}

REQUIRED_MAPPING_FIELDS = {"slug", "name", "kind", "source_frame", "target_frame", "categories", "author"}
REQUIRED_FRAME_FIELDS = {"slug", "name", "roles"}
REQUIRED_CATEGORY_FIELDS = {"slug", "name"}

REQUIRED_MAPPING_SECTIONS = {"What It Brings", "Where It Breaks", "Expressions"}


def slugs_in(directory: Path) -> set[str]:
    """Collect all slugs from frontmatter in a directory."""
    slugs = set()
    for f in directory.glob("*.md"):
        post = frontmatter.load(f)
        if "slug" in post.metadata:
            slugs.add(post.metadata["slug"])
    return slugs


def slug_files(directory: Path) -> dict[str, Path]:
    """Map slugs to their file paths."""
    result = {}
    for f in directory.glob("*.md"):
        post = frontmatter.load(f)
        if "slug" in post.metadata:
            result[post.metadata["slug"]] = f
    return result


def parse_sections(content: str) -> dict[str, str]:
    """Parse markdown body into {heading: content} dict."""
    sections: dict[str, str] = {}
    current_heading = None
    current_lines: list[str] = []

    for line in content.split("\n"):
        m = re.match(r"^## (.+)$", line)
        if m:
            if current_heading:
                sections[current_heading] = "\n".join(current_lines).strip()
            current_heading = m.group(1).strip()
            current_lines = []
        elif current_heading is not None:
            current_lines.append(line)

    if current_heading:
        sections[current_heading] = "\n".join(current_lines).strip()

    return sections


def validate_mapping(path: Path, frame_slugs: set[str], category_slugs: set[str],
                     mapping_slugs: set[str], errors: list[str], warnings: list[str]) -> None:
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
    if "kind" in meta and meta["kind"] not in VALID_KINDS:
        errors.append(f"{prefix}: invalid kind '{meta['kind']}' (valid: {', '.join(sorted(VALID_KINDS))})")

    # Frame references
    if "source_frame" in meta and meta["source_frame"] not in frame_slugs:
        errors.append(f"{prefix}: source_frame '{meta['source_frame']}' not found in frames/")
    if "target_frame" in meta and meta["target_frame"] not in frame_slugs:
        errors.append(f"{prefix}: target_frame '{meta['target_frame']}' not found in frames/")

    # Category references
    for cat in meta.get("categories", []):
        if cat not in category_slugs:
            errors.append(f"{prefix}: category '{cat}' not found in categories/")

    # Related references (warnings, not errors — graph grows outward)
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


def validate_frame(path: Path, frame_slugs: set[str], errors: list[str], warnings: list[str]) -> None:
    post = frontmatter.load(path)
    meta = post.metadata
    prefix = f"catalog/frames/{path.name}"

    for field in REQUIRED_FRAME_FIELDS:
        if field not in meta:
            errors.append(f"{prefix}: missing required field '{field}'")

    if "slug" in meta and meta["slug"] != path.stem:
        errors.append(f"{prefix}: slug '{meta['slug']}' doesn't match filename '{path.stem}'")

    # broader/related are aspirational links — warn, don't error
    if "broader" in meta and meta["broader"] not in frame_slugs:
        warnings.append(f"{prefix}: broader frame '{meta['broader']}' not found in frames/")

    for rel in meta.get("related", []):
        if rel not in frame_slugs:
            warnings.append(f"{prefix}: related frame '{rel}' not found in frames/")


def validate_category(path: Path, category_slugs: set[str], errors: list[str], warnings: list[str]) -> None:
    post = frontmatter.load(path)
    meta = post.metadata
    prefix = f"catalog/categories/{path.name}"

    for field in REQUIRED_CATEGORY_FIELDS:
        if field not in meta:
            errors.append(f"{prefix}: missing required field '{field}'")

    if "slug" in meta and meta["slug"] != path.stem:
        errors.append(f"{prefix}: slug '{meta['slug']}' doesn't match filename '{path.stem}'")

    # broader/related are aspirational links — warn, don't error
    if "broader" in meta and meta["broader"] not in category_slugs:
        warnings.append(f"{prefix}: broader category '{meta['broader']}' not found in categories/")

    for rel in meta.get("related", []):
        if rel not in category_slugs:
            warnings.append(f"{prefix}: related category '{rel}' not found in categories/")


def validate(target: str | None = None) -> tuple[list[str], list[str]]:
    frame_slugs = slugs_in(FRAMES_DIR)
    category_slugs = slugs_in(CATEGORIES_DIR)
    mapping_slugs = slugs_in(MAPPINGS_DIR)
    errors: list[str] = []
    warnings: list[str] = []

    dirs_to_check = {"mappings", "frames", "categories"}
    if target:
        # Accept both "mappings" and "catalog/mappings"
        normalized = target.rstrip("/").removeprefix("catalog/")
        dirs_to_check = {normalized}

    if "frames" in dirs_to_check:
        for f in sorted(FRAMES_DIR.glob("*.md")):
            validate_frame(f, frame_slugs, errors, warnings)

    if "categories" in dirs_to_check:
        for f in sorted(CATEGORIES_DIR.glob("*.md")):
            validate_category(f, category_slugs, errors, warnings)

    if "mappings" in dirs_to_check:
        for f in sorted(MAPPINGS_DIR.glob("*.md")):
            validate_mapping(f, frame_slugs, category_slugs, mapping_slugs, errors, warnings)

    return errors, warnings


def extract() -> list[dict]:
    results = []
    for f in sorted(MAPPINGS_DIR.glob("*.md")):
        post = frontmatter.load(f)
        sections = parse_sections(post.content)
        results.append({
            **post.metadata,
            "sections": sections,
        })
    return results


def main() -> None:
    if len(sys.argv) < 2 or sys.argv[1] not in ("validate", "extract"):
        print(__doc__.strip())
        sys.exit(1)

    command = sys.argv[1]

    if command == "validate":
        target = sys.argv[2] if len(sys.argv) > 2 else None
        errors, warnings = validate(target)
        if warnings:
            print(f"{len(warnings)} warning(s) (dangling references, non-blocking):\n")
            for w in warnings:
                print(f"  ~ {w}")
            print()
        if errors:
            print(f"{len(errors)} error(s):\n")
            for e in errors:
                print(f"  - {e}")
            sys.exit(1)
        else:
            print("All content valid.")
            sys.exit(0)

    elif command == "extract":
        data = extract()
        json.dump(data, sys.stdout, indent=2)
        print()


if __name__ == "__main__":
    main()
