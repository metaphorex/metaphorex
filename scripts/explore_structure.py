# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-frontmatter>=1.1.0",
# ]
# ///
"""Structural enrichment explorer — find emergent connections, clusters, and gaps.

Usage:
    uv run scripts/explore_structure.py surprise        # Non-obvious cross-domain matches
    uv run scripts/explore_structure.py clusters        # Structural families
    uv run scripts/explore_structure.py gaps             # Underrepresented combinations
    uv run scripts/explore_structure.py similar <slug>   # Find structural matches for an entry
    uv run scripts/explore_structure.py all              # Run all analyses, write report
"""

from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from itertools import combinations
from pathlib import Path

import frontmatter

ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = ROOT / "catalog" / "entries"


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class Entry:
    slug: str
    name: str
    kind: str
    source_frame: str
    embodied_patterns: list[str] = field(default_factory=list)
    relation_types: list[str] = field(default_factory=list)
    structure: list[str] = field(default_factory=list)
    abstraction_level: str = ""


def load_entries() -> list[Entry]:
    entries = []
    for f in sorted(ENTRIES_DIR.glob("*.md")):
        post = frontmatter.load(f)
        m = post.metadata
        if "embodied_patterns" not in m:
            continue
        struct = m.get("structure", [])
        if isinstance(struct, str):
            struct = [struct]
        entries.append(Entry(
            slug=m.get("slug", f.stem),
            name=m.get("name", f.stem),
            kind=m.get("kind", ""),
            source_frame=m.get("source_frame", ""),
            embodied_patterns=m.get("embodied_patterns", []),
            relation_types=m.get("relation_types", []),
            structure=struct,
            abstraction_level=m.get("abstraction_level", ""),
        ))
    return entries


# ---------------------------------------------------------------------------
# Similarity
# ---------------------------------------------------------------------------

# IDF-style weights: common values downweighted, rare values boosted
RELATION_WEIGHTS = {
    "cause": 0.3, "transform": 0.3,
    "prevent": 0.8, "enable": 0.8, "contain": 0.8,
    "coordinate": 1.0, "compete": 1.0, "select": 1.0, "accumulate": 1.0,
    "translate": 1.3, "decompose": 1.3, "restore": 1.3,
}

EP_WEIGHTS = {
    "force": 0.5, "path": 0.5, "container": 0.6,
    "boundary": 0.7, "matching": 0.7, "scale": 0.8,
    "flow": 0.9, "part-whole": 0.9, "link": 0.9, "balance": 0.9,
    "surface-depth": 1.0, "near-far": 1.0, "iteration": 1.0,
    "blockage": 1.0, "center-periphery": 1.1,
    "accretion": 1.2, "removal": 1.1, "splitting": 1.2,
    "merging": 1.3, "self-organization": 1.3,
    "superimposition": 1.3, "attraction": 1.5,
}


def jaccard(a: list[str], b: list[str]) -> float:
    sa, sb = set(a), set(b)
    inter = len(sa & sb)
    union = len(sa | sb)
    return inter / union if union > 0 else 0.0


def _parent(v: str) -> str:
    """Extract parent from a hierarchical value like 'cause/propagate' -> 'cause'."""
    return v.split("/")[0] if "/" in v else v


def weighted_jaccard(a: list[str], b: list[str], weights: dict[str, float]) -> float:
    sa, sb = set(a), set(b)
    all_vals = sa | sb
    inter_w = 0.0
    union_w = 0.0

    # Track which values in b have been matched (for parent-level partial credit)
    b_matched = set()

    for v in all_vals:
        w = weights.get(_parent(v), 1.0)
        union_w += w
        if v in sa and v in sb:
            # Exact match: full credit
            inter_w += w
            b_matched.add(v)
        elif v in sa and "/" in v:
            # Check for parent-level match in b (e.g., cause/propagate ~ cause/compel)
            parent = _parent(v)
            sibling = next((bv for bv in sb - b_matched if _parent(bv) == parent and bv != v), None)
            if sibling:
                inter_w += w * 0.3  # Partial credit for same parent
                b_matched.add(sibling)

    return inter_w / union_w if union_w > 0 else 0.0


def structural_sim(a: Entry, b: Entry) -> float:
    ep = weighted_jaccard(a.embodied_patterns, b.embodied_patterns, EP_WEIGHTS)
    rt = weighted_jaccard(a.relation_types, b.relation_types, RELATION_WEIGHTS)
    st = jaccard(a.structure, b.structure)
    al = 1.0 if a.abstraction_level == b.abstraction_level else 0.0
    return ep * 0.35 + rt * 0.35 + st * 0.20 + al * 0.10


# ---------------------------------------------------------------------------
# Analysis: Surprise finder
# ---------------------------------------------------------------------------

def find_surprises(entries: list[Entry], top_n: int = 40) -> list[tuple[Entry, Entry, float]]:
    """Find entry pairs with high structural similarity but different source frames.

    Caps at 2 matches per entry to prevent one entry with a common signature
    from dominating the results. Prioritizes cross-kind matches.
    """
    surprises = []
    for i, a in enumerate(entries):
        for b in entries[i + 1:]:
            if a.source_frame == b.source_frame:
                continue
            sim = structural_sim(a, b)
            threshold = 0.45 if a.kind != b.kind else 0.50
            if sim >= threshold:
                surprises.append((a, b, sim))

    surprises.sort(key=lambda x: -x[2])

    # Cap per entry: max 2 appearances per slug to prevent signature flooding
    slug_counts: dict[str, int] = {}
    filtered = []
    for a, b, sim in surprises:
        ca = slug_counts.get(a.slug, 0)
        cb = slug_counts.get(b.slug, 0)
        if ca >= 2 or cb >= 2:
            continue
        filtered.append((a, b, sim))
        slug_counts[a.slug] = ca + 1
        slug_counts[b.slug] = cb + 1

    return filtered[:top_n]


def print_surprises(entries: list[Entry]):
    print("=" * 70)
    print("STRUCTURAL SURPRISES — Non-obvious cross-domain matches")
    print("=" * 70)
    print()

    surprises = find_surprises(entries)

    # Group by shared structural signature
    for i, (a, b, sim) in enumerate(surprises, 1):
        shared_ep = set(a.embodied_patterns) & set(b.embodied_patterns)
        shared_rt = set(a.relation_types) & set(b.relation_types)
        print(f"{i:2d}. [{sim:.2f}] {a.name} ({a.source_frame}/{a.kind})")
        print(f"           ↔ {b.name} ({b.source_frame}/{b.kind})")
        print(f"    shared: ep={sorted(shared_ep)}  rt={sorted(shared_rt)}")
        print()


# ---------------------------------------------------------------------------
# Analysis: Clusters
# ---------------------------------------------------------------------------

def find_clusters(entries: list[Entry]) -> dict[str, list[Entry]]:
    """Group entries by their dominant structural signature."""
    clusters: dict[str, list[Entry]] = defaultdict(list)
    for e in entries:
        # Create a signature from the top structural features
        sig_parts = []
        sig_parts.extend(sorted(e.embodied_patterns[:3]))
        sig_parts.append("|")
        sig_parts.extend(sorted(e.relation_types[:2]))
        sig = "+".join(sig_parts)
        clusters[sig].append(e)
    return clusters


def print_clusters(entries: list[Entry]):
    print("=" * 70)
    print("STRUCTURAL FAMILIES — Entries sharing structural skeletons")
    print("=" * 70)
    print()

    clusters = find_clusters(entries)

    # Sort by size, show the interesting ones (multi-frame clusters)
    interesting = []
    for sig, members in clusters.items():
        frames = set(m.source_frame for m in members if m.source_frame)
        kinds = set(m.kind for m in members)
        if len(frames) >= 3 and len(members) >= 4:
            interesting.append((sig, members, frames, kinds))

    interesting.sort(key=lambda x: -len(x[1]))

    for sig, members, frames, kinds in interesting[:20]:
        print(f"Family: {sig}")
        print(f"  Size: {len(members)} entries across {len(frames)} source frames, {len(kinds)} kinds")
        print(f"  Frames: {', '.join(sorted(frames)[:8])}{'...' if len(frames) > 8 else ''}")
        print(f"  Kinds: {', '.join(sorted(kinds))}")
        print(f"  Members:")
        for m in members[:6]:
            print(f"    - {m.name} ({m.source_frame}/{m.kind})")
        if len(members) > 6:
            print(f"    ... and {len(members) - 6} more")
        print()


# ---------------------------------------------------------------------------
# Analysis: Gaps
# ---------------------------------------------------------------------------

def find_gaps(entries: list[Entry]):
    """Identify underrepresented structural combinations."""
    print("=" * 70)
    print("STRUCTURAL GAPS — Underrepresented patterns and combinations")
    print("=" * 70)
    print()

    # 1. Rare embodied patterns
    ep_counts = Counter()
    for e in entries:
        for v in e.embodied_patterns:
            ep_counts[v] += 1

    print("Rare embodied patterns (bottom 5):")
    for v, c in ep_counts.most_common()[-5:]:
        pct = c / len(entries) * 100
        print(f"  {v:25s} {c:4d} ({pct:.1f}%)")
    print()

    # 2. Rare relation types
    rt_counts = Counter()
    for e in entries:
        for v in e.relation_types:
            rt_counts[v] += 1

    print("Rare relation types (bottom 5):")
    for v, c in rt_counts.most_common()[-5:]:
        pct = c / len(entries) * 100
        print(f"  {v:25s} {c:4d} ({pct:.1f}%)")
    print()

    # 3. Underrepresented structure types
    st_counts = Counter()
    for e in entries:
        for v in e.structure:
            st_counts[v] += 1

    print("Structure distribution:")
    for v, c in st_counts.most_common():
        bar = "█" * (c // 5)
        print(f"  {v:20s} {c:4d} {bar}")
    print()

    # 4. EP × RT combinations that are rare but structurally interesting
    ep_rt_combos = Counter()
    for e in entries:
        for ep in e.embodied_patterns:
            for rt in e.relation_types:
                ep_rt_combos[(ep, rt)] += 1

    # Find combos that SHOULD exist but barely do
    expected_interesting = [
        ("self-organization", "coordinate"),
        ("self-organization", "transform"),
        ("accretion", "transform"),
        ("attraction", "cause"),
        ("attraction", "enable"),
        ("superimposition", "transform"),
        ("merging", "translate"),
        ("splitting", "decompose"),
        ("iteration", "restore"),
        ("blockage", "translate"),
    ]

    print("Structurally interesting but rare EP×RT combos:")
    for ep, rt in expected_interesting:
        c = ep_rt_combos.get((ep, rt), 0)
        status = "GAP" if c <= 2 else f"{c}"
        print(f"  {ep:20s} × {rt:15s} → {status}")
    print()

    # 5. Cross-kind coverage gaps
    kind_ep = defaultdict(Counter)
    for e in entries:
        for v in e.embodied_patterns:
            kind_ep[e.kind][v] += 1

    print("Embodied patterns underrepresented by kind:")
    all_eps = set(ep_counts.keys())
    for kind in sorted(kind_ep.keys()):
        missing = []
        for ep in all_eps:
            if kind_ep[kind][ep] <= 1:
                missing.append(ep)
        if missing:
            print(f"  {kind}: few/no entries with {', '.join(sorted(missing)[:5])}{'...' if len(missing) > 5 else ''}")
    print()

    # 6. Source frames with low structural diversity
    frame_eps = defaultdict(set)
    for e in entries:
        if e.source_frame:
            frame_eps[e.source_frame].update(e.embodied_patterns)

    print("Source frames with narrow structural range (< 6 distinct patterns):")
    for frame, eps in sorted(frame_eps.items()):
        if len(eps) < 6 and frame:
            count = sum(1 for e in entries if e.source_frame == frame)
            if count >= 5:  # Only show frames with enough entries to care
                print(f"  {frame:30s} {count:3d} entries, {len(eps)} patterns: {', '.join(sorted(eps))}")
    print()

    # 7. Emergence is rare — what entries have it?
    print("Entries with structure=emergence (rare, high-value):")
    emergence = [e for e in entries if "emergence" in e.structure]
    for e in emergence:
        print(f"  {e.name:50s} ({e.source_frame}/{e.kind})")
    print(f"  Total: {len(emergence)}")
    print()

    # 8. Entries with 'translate' relation (high-value for retrieval)
    translate_entries = [e for e in entries if "translate" in e.relation_types]
    print(f"Entries with translate relation: {len(translate_entries)}")
    frame_translate = Counter(e.source_frame for e in translate_entries)
    for frame, c in frame_translate.most_common(10):
        print(f"  {frame:30s} {c}")
    print()


# ---------------------------------------------------------------------------
# Analysis: Similar entries
# ---------------------------------------------------------------------------

def find_similar(entries: list[Entry], target_slug: str, top_n: int = 15):
    target = next((e for e in entries if e.slug == target_slug), None)
    if not target:
        print(f"Entry '{target_slug}' not found or not enriched.")
        return

    print(f"Structural matches for: {target.name}")
    print(f"  kind: {target.kind}, frame: {target.source_frame}")
    print(f"  ep: {target.embodied_patterns}")
    print(f"  rt: {target.relation_types}")
    print(f"  st: {target.structure}")
    print(f"  al: {target.abstraction_level}")
    print()

    scored = []
    for e in entries:
        if e.slug == target_slug:
            continue
        sim = structural_sim(target, e)
        scored.append((e, sim))

    scored.sort(key=lambda x: -x[1])

    # Separate same-frame and cross-frame
    print("Cross-domain matches (different source frame):")
    cross = [(e, s) for e, s in scored if e.source_frame != target.source_frame]
    for e, sim in cross[:top_n]:
        shared_ep = sorted(set(target.embodied_patterns) & set(e.embodied_patterns))
        shared_rt = sorted(set(target.relation_types) & set(e.relation_types))
        print(f"  [{sim:.2f}] {e.name:45s} ({e.source_frame}/{e.kind})")
        print(f"         shared: ep={shared_ep} rt={shared_rt}")

    print()
    print("Same-domain matches (same source frame):")
    same = [(e, s) for e, s in scored if e.source_frame == target.source_frame]
    for e, sim in same[:5]:
        print(f"  [{sim:.2f}] {e.name:45s} ({e.kind})")


# ---------------------------------------------------------------------------
# Full report
# ---------------------------------------------------------------------------

def write_report(entries: list[Entry]):
    report_path = ROOT / "docs" / "evals" / "structural-exploration-report.md"

    lines = []
    lines.append("# Structural Exploration Report\n")
    lines.append(f"**Entries analyzed:** {len(entries)}\n")

    # Tag distribution summary
    ep_counts = Counter()
    rt_counts = Counter()
    st_counts = Counter()
    for e in entries:
        for v in e.embodied_patterns: ep_counts[v] += 1
        for v in e.relation_types: rt_counts[v] += 1
        for v in e.structure: st_counts[v] += 1

    lines.append("\n## Tag Distribution\n")
    lines.append("### Embodied Patterns\n")
    lines.append("| Pattern | Count | % |\n|---|---|---|\n")
    for v, c in ep_counts.most_common():
        lines.append(f"| {v} | {c} | {c*100//len(entries)}% |\n")

    lines.append("\n### Relation Types\n")
    lines.append("| Type | Count | % |\n|---|---|---|\n")
    for v, c in rt_counts.most_common():
        lines.append(f"| {v} | {c} | {c*100//len(entries)}% |\n")

    lines.append("\n### Structure\n")
    lines.append("| Structure | Count | % |\n|---|---|---|\n")
    for v, c in st_counts.most_common():
        lines.append(f"| {v} | {c} | {c*100//len(entries)}% |\n")

    # Surprises
    lines.append("\n## Top Structural Surprises\n")
    lines.append("Entry pairs with high structural similarity across different domains.\n\n")
    surprises = find_surprises(entries, top_n=30)
    lines.append("| # | Sim | Entry A | Frame A | Entry B | Frame B | Shared Patterns | Shared Relations |\n")
    lines.append("|---|-----|---------|---------|---------|---------|-----------------|------------------|\n")
    for i, (a, b, sim) in enumerate(surprises, 1):
        sep = sorted(set(a.embodied_patterns) & set(b.embodied_patterns))
        srt = sorted(set(a.relation_types) & set(b.relation_types))
        lines.append(f"| {i} | {sim:.2f} | {a.name} | {a.source_frame} | {b.name} | {b.source_frame} | {', '.join(sep)} | {', '.join(srt)} |\n")

    # Gaps
    lines.append("\n## Structural Gaps\n")
    lines.append("Areas where the catalog could benefit from new entries.\n\n")

    # Rare patterns
    lines.append("### Rare Embodied Patterns\n")
    lines.append("| Pattern | Count | Suggestion |\n|---|---|---|\n")
    for v, c in ep_counts.most_common()[-6:]:
        suggestion = {
            "attraction": "Metaphors about pull, gravity, magnetism, desire",
            "superimposition": "Layering, palimpsest, protocol stacks, geological strata",
            "merging": "Fusion, synthesis, cultural assimilation, merge conflicts",
            "self-organization": "Emergent order, stigmergy, market self-regulation",
            "accretion": "Coral reef, common law, trail-making, sedimentation",
            "splitting": "Fork, schism, cell division, branching",
        }.get(v, "")
        lines.append(f"| {v} | {c} | {suggestion} |\n")

    # Rare structures
    lines.append("\n### Rare Structures\n")
    lines.append("| Structure | Count | Suggestion |\n|---|---|---|\n")
    for v, c in st_counts.most_common()[-4:]:
        suggestion = {
            "emergence": "Flocking, market pricing, Wikipedia, open-source governance",
            "growth": "Compound interest, viral spread, cancer, population dynamics",
            "equilibrium": "Homeostasis, market clearing, thermostat, predator-prey balance",
            "competition": "Arms race, auction, tournament, natural selection",
        }.get(v, "")
        lines.append(f"| {v} | {c} | {suggestion} |\n")

    report_path.write_text("".join(lines))
    print(f"Report written to {report_path}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1]
    entries = load_entries()
    print(f"Loaded {len(entries)} enriched entries\n")

    if cmd == "surprise":
        print_surprises(entries)
    elif cmd == "clusters":
        print_clusters(entries)
    elif cmd == "gaps":
        find_gaps(entries)
    elif cmd == "similar" and len(sys.argv) >= 3:
        find_similar(entries, sys.argv[2])
    elif cmd == "all":
        print_surprises(entries)
        print()
        print_clusters(entries)
        print()
        find_gaps(entries)
        write_report(entries)
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
