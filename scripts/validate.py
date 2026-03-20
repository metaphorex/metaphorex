# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-frontmatter>=1.1.0",
# ]
# ///
"""Metaphorex content validator and extractor.

Usage:
    uv run scripts/validate.py validate              # validate all content
    uv run scripts/validate.py validate catalog/entries/ # validate specific dir
    uv run scripts/validate.py validate-manifests     # validate playbook manifests
    uv run scripts/validate.py extract                # emit JSON to stdout
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import frontmatter

ROOT = Path(__file__).resolve().parent.parent
CATALOG_DIR = ROOT / "catalog"
ENTRIES_DIR = CATALOG_DIR / "entries"
FRAMES_DIR = CATALOG_DIR / "frames"
CATEGORIES_DIR = CATALOG_DIR / "categories"
WORKS_DIR = CATALOG_DIR / "works"
PLAYBOOKS_DIR = ROOT / "playbooks"

VALID_KINDS = {
    "metaphor",
    "pattern",
    "archetype",
    "paradigm",
    "mental-model",
}

REQUIRED_MAPPING_FIELDS = {"slug", "name", "kind", "categories", "author", "created", "updated"}
REQUIRED_FRAME_FIELDS = {"slug", "name", "roles", "created", "updated"}
REQUIRED_CATEGORY_FIELDS = {"slug", "name", "created", "updated"}
REQUIRED_WORK_FIELDS = {"slug", "name", "type", "authors", "year", "created", "updated"}

VALID_WORK_TYPES = {"book", "paper", "collection", "repository", "talk", "post"}

VALID_GROUNDING = {"proven", "established", "folk", "contested"}
REJECTED_FIELDS = {"target_frame", "structural_properties", "failure_conditions"}
REJECTED_KINDS = {"conceptual-metaphor", "dead-metaphor", "cross-field-mapping"}

REQUIRED_MAPPING_SECTIONS = {"Transfers", "Limits", "Expressions"}

# Legacy headings that should be replaced with canonical names
DEPRECATED_HEADINGS = {
    "Where It Breaks": "Limits",
    "What It Brings": "Transfers",
    "What It Enables": "Expressions",
}


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


def validate_work(path: Path, work_slugs: set[str], errors: list[str], warnings: list[str]) -> None:
    post = frontmatter.load(path)
    meta = post.metadata
    prefix = f"catalog/works/{path.name}"

    for field in REQUIRED_WORK_FIELDS:
        if field not in meta:
            errors.append(f"{prefix}: missing required field '{field}'")

    if "slug" in meta and meta["slug"] != path.stem:
        errors.append(f"{prefix}: slug '{meta['slug']}' doesn't match filename '{path.stem}'")

    if "type" in meta and meta["type"] not in VALID_WORK_TYPES:
        errors.append(f"{prefix}: invalid type '{meta['type']}' (valid: {', '.join(sorted(VALID_WORK_TYPES))})")

    for rel in meta.get("related", []):
        if rel not in work_slugs:
            warnings.append(f"{prefix}: related work '{rel}' not found in works/")


def validate_entry(path: Path, frame_slugs: set[str], category_slugs: set[str],
                   entry_slugs: set[str], work_slugs: set[str],
                   errors: list[str], warnings: list[str]) -> None:
    post = frontmatter.load(path)
    meta = post.metadata
    prefix = f"catalog/entries/{path.name}"

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

    # Circular mapping: source_frame should not appear in applies_to
    source = meta.get("source_frame")
    applies = meta.get("applies_to", [])
    if source and isinstance(applies, list) and source in applies:
        warnings.append(f"{prefix}: circular mapping — source_frame '{source}' also appears in applies_to")

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
        if rel not in entry_slugs:
            warnings.append(f"{prefix}: related entry '{rel}' not found in entries/")

    # Required sections
    sections = parse_sections(post.content)
    for section in REQUIRED_MAPPING_SECTIONS:
        if section not in sections:
            errors.append(f"{prefix}: missing required section '## {section}'")
        elif not sections[section]:
            errors.append(f"{prefix}: section '## {section}' is empty")

    # Duplicate section check — parse_sections silently overwrites duplicates,
    # so count headings directly from the raw markdown body
    heading_counts: dict[str, int] = {}
    for line in post.content.split("\n"):
        m = re.match(r"^## (.+)$", line)
        if m:
            h = m.group(1).strip()
            heading_counts[h] = heading_counts.get(h, 0) + 1
    for section in REQUIRED_MAPPING_SECTIONS:
        count = heading_counts.get(section, 0)
        if count > 1:
            errors.append(f"{prefix}: duplicate section '## {section}' appears {count} times")

    # Deprecated heading check
    for heading, replacement in DEPRECATED_HEADINGS.items():
        if heading in heading_counts:
            errors.append(f"{prefix}: deprecated section '## {heading}' — use '## {replacement}'")

    # Frontmatter-body alignment: enrichment fields must have matching body sections
    for field, heading in (("transfers", "Transfers"), ("limits", "Limits")):
        if field in meta:
            if heading not in sections:
                warnings.append(f"{prefix}: frontmatter has '{field}' but body ## {heading} section is missing")
            elif not sections[heading]:
                warnings.append(f"{prefix}: frontmatter has '{field}' but body ## {heading} section is empty")


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
    entry_slugs = slugs_in(ENTRIES_DIR)
    work_slugs = slugs_in(WORKS_DIR) if WORKS_DIR.exists() else set()
    errors: list[str] = []
    warnings: list[str] = []

    dirs_to_check = {"entries", "frames", "categories", "works"}
    if target:
        # Accept both "entries" and "catalog/entries"
        normalized = target.rstrip("/").removeprefix("catalog/")
        dirs_to_check = {normalized}

    if "works" in dirs_to_check and WORKS_DIR.exists():
        for f in sorted(WORKS_DIR.glob("*.md")):
            validate_work(f, work_slugs, errors, warnings)

    if "frames" in dirs_to_check:
        for f in sorted(FRAMES_DIR.glob("*.md")):
            validate_frame(f, frame_slugs, errors, warnings)

    if "categories" in dirs_to_check:
        for f in sorted(CATEGORIES_DIR.glob("*.md")):
            validate_category(f, category_slugs, errors, warnings)

    if "entries" in dirs_to_check:
        for f in sorted(ENTRIES_DIR.glob("*.md")):
            validate_entry(f, frame_slugs, category_slugs, entry_slugs, work_slugs, errors, warnings)

    return errors, warnings


def category_slugs_from_files() -> set[str]:
    """Collect category slugs from filenames in catalog/categories/."""
    slugs = set()
    if CATEGORIES_DIR.exists():
        for f in CATEGORIES_DIR.glob("*.md"):
            slugs.add(f.stem)
    return slugs


def validate_manifests() -> tuple[list[str], list[str]]:
    """Validate playbook manifest.json files against catalog categories."""
    errors: list[str] = []
    warnings: list[str] = []
    cat_slugs = category_slugs_from_files()

    if not PLAYBOOKS_DIR.exists():
        return errors, warnings

    for manifest_path in sorted(PLAYBOOKS_DIR.glob("*/manifest.json")):
        prefix = str(manifest_path.relative_to(ROOT))
        try:
            data = json.loads(manifest_path.read_text())
        except (json.JSONDecodeError, OSError) as exc:
            errors.append(f"{prefix}: failed to parse manifest: {exc}")
            continue

        for candidate in data.get("candidates", []):
            slug = candidate.get("slug", "<unknown>")
            for cat in candidate.get("categories", []):
                if cat not in cat_slugs:
                    errors.append(
                        f"{prefix}: candidate '{slug}' references "
                        f"unknown category '{cat}'"
                    )

    return errors, warnings


def extract() -> list[dict]:
    results = []
    for f in sorted(ENTRIES_DIR.glob("*.md")):
        post = frontmatter.load(f)
        sections = parse_sections(post.content)
        results.append({
            **post.metadata,
            "sections": sections,
        })
    return results


def main() -> None:
    if len(sys.argv) < 2 or sys.argv[1] not in ("validate", "validate-manifests", "extract"):
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

    elif command == "validate-manifests":
        errors, warnings = validate_manifests()
        if warnings:
            print(f"{len(warnings)} warning(s):\n")
            for w in warnings:
                print(f"  ~ {w}")
            print()
        if errors:
            print(f"{len(errors)} manifest error(s):\n")
            for e in errors:
                print(f"  - {e}")
            sys.exit(1)
        else:
            print("All manifests valid.")
            sys.exit(0)

    elif command == "extract":
        data = extract()
        json.dump(data, sys.stdout, indent=2)
        print()


if __name__ == "__main__":
    main()
