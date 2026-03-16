# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-frontmatter>=1.1.0",
# ]
# ///
"""Create a CalVer release with a catalog snapshot attached.

Usage:
    uv run scripts/release.py              # create release
    uv run scripts/release.py --dry-run    # show what would happen
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _get_calver_tag() -> str:
    """Generate CalVer tag (YYYY.MM.DD), appending .N for same-day collisions."""
    today = date.today().strftime("%Y.%m.%d")

    # Check existing tags
    result = subprocess.run(
        ["git", "tag", "--list", f"{today}*"],
        cwd=ROOT, capture_output=True, text=True, check=True,
    )
    existing = [t.strip() for t in result.stdout.strip().split("\n") if t.strip()]

    if not existing:
        return today

    # Find highest suffix
    max_suffix = 0
    for tag in existing:
        if tag == today:
            max_suffix = max(max_suffix, 0)
        elif tag.startswith(today + "."):
            try:
                suffix = int(tag.split(".")[-1])
                max_suffix = max(max_suffix, suffix)
            except ValueError:
                continue
    return f"{today}.{max_suffix + 1}"


def _extract_snapshot() -> str:
    """Run validate.py extract to produce snapshot JSON."""
    result = subprocess.run(
        ["uv", "run", "scripts/validate.py", "extract"],
        cwd=ROOT, capture_output=True, text=True, check=True,
    )
    return result.stdout


def _get_last_release_snapshot() -> str | None:
    """Download and return the snapshot from the latest release, or None."""
    try:
        result = subprocess.run(
            ["gh", "release", "view", "--json", "tagName", "-q", ".tagName"],
            cwd=ROOT, capture_output=True, text=True, check=True,
        )
        last_tag = result.stdout.strip()
        if not last_tag:
            return None

        with tempfile.TemporaryDirectory() as tmpdir:
            subprocess.run(
                ["gh", "release", "download", last_tag, "--pattern", "metaphorex-*.json", "--dir", tmpdir],
                cwd=ROOT, capture_output=True, text=True, check=True,
            )
            files = list(Path(tmpdir).glob("metaphorex-*.json"))
            if files:
                return files[0].read_text()
    except subprocess.CalledProcessError:
        pass
    return None


def _snapshots_differ(current: str, previous: str | None) -> bool:
    """Compare snapshots by content (ignoring whitespace differences)."""
    if previous is None:
        return True
    try:
        current_data = json.loads(current)
        previous_data = json.loads(previous)
        return current_data != previous_data
    except json.JSONDecodeError:
        return True


def main():
    parser = argparse.ArgumentParser(description="Create a CalVer release with catalog snapshot")
    parser.add_argument("--dry-run", action="store_true", help="Show what would happen without creating release")
    args = parser.parse_args()

    tag = _get_calver_tag()
    print(f"Release tag: {tag}")

    print("Extracting snapshot...")
    snapshot = _extract_snapshot()
    snapshot_data = json.loads(snapshot)
    print(f"Snapshot contains {len(snapshot_data)} entries")

    print("Checking for changes since last release...")
    last_snapshot = _get_last_release_snapshot()
    if not _snapshots_differ(snapshot, last_snapshot):
        print("No catalog changes since last release. Skipping.")
        return

    if args.dry_run:
        print(f"[DRY RUN] Would create release {tag} with {len(snapshot_data)} entries")
        return

    # Write snapshot to temp file and create release
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".json", prefix=f"metaphorex-{tag}", delete=False,
    ) as f:
        f.write(json.dumps(snapshot_data, indent=2))
        snapshot_path = f.name

    # Rename to canonical name
    canonical = Path(snapshot_path).parent / f"metaphorex-{tag}.json"
    Path(snapshot_path).rename(canonical)

    try:
        subprocess.run(
            [
                "gh", "release", "create", tag,
                "--title", f"Catalog snapshot {tag}",
                "--notes", f"Automated catalog snapshot with {len(snapshot_data)} entries.",
                str(canonical),
            ],
            cwd=ROOT, check=True,
        )
        print(f"Release {tag} created with snapshot attached")
    except subprocess.CalledProcessError as e:
        print(f"Failed to create release: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        canonical.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
