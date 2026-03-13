# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-frontmatter>=1.1.0",
#     "networkx>=3.2",
#     "matplotlib>=3.8",
# ]
# ///
"""Explore the Metaphorex frame-to-frame graph.

Builds a directed graph where nodes are frames and edges are mappings.
Outputs statistics and a visualization to help decide whether graph
features are worth pursuing.

Usage:
    uv run scripts/graph_explore.py                    # print stats + save PNG
    uv run scripts/graph_explore.py --output graph.svg # save as SVG
"""

from __future__ import annotations

import sys
from pathlib import Path

import frontmatter
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx

ROOT = Path(__file__).resolve().parent.parent
MAPPINGS_DIR = ROOT / "catalog" / "mappings"
FRAMES_DIR = ROOT / "catalog" / "frames"


def load_graph() -> tuple[nx.DiGraph, dict[str, str]]:
    """Build directed graph from catalog. Returns (graph, frame_slug_to_name)."""
    G = nx.DiGraph()

    # Load frame names
    frame_names = {}
    for f in FRAMES_DIR.glob("*.md"):
        post = frontmatter.load(f)
        slug = post.metadata.get("slug", f.stem)
        name = post.metadata.get("name", slug)
        frame_names[slug] = name
        G.add_node(slug, name=name)

    # Add edges from mappings
    for f in MAPPINGS_DIR.glob("*.md"):
        post = frontmatter.load(f)
        meta = post.metadata
        src = meta.get("source_frame")
        tgt = meta.get("target_frame")
        if src and tgt:
            if G.has_edge(src, tgt):
                G[src][tgt]["weight"] += 1
                G[src][tgt]["mappings"].append(meta.get("slug", f.stem))
            else:
                G.add_edge(src, tgt, weight=1, mappings=[meta.get("slug", f.stem)])

    return G, frame_names


def print_stats(G: nx.DiGraph, frame_names: dict[str, str]) -> None:
    """Print graph statistics."""
    print(f"Nodes (frames): {G.number_of_nodes()}")
    print(f"Edges (unique frame pairs): {G.number_of_edges()}")
    print(f"Total mappings as edges: {sum(d['weight'] for _, _, d in G.edges(data=True))}")

    # Degree analysis (treat as undirected for connectivity)
    U = G.to_undirected()

    print(f"\n--- Components ---")
    components = list(nx.connected_components(U))
    print(f"Connected components: {len(components)}")
    sizes = sorted([len(c) for c in components], reverse=True)
    print(f"Component sizes: {sizes}")

    if len(components) == 1 or sizes[0] > 1:
        largest = max(components, key=len)
        subgraph = U.subgraph(largest)
        try:
            diameter = nx.diameter(subgraph)
            print(f"Diameter of largest component: {diameter}")
        except nx.NetworkXError:
            print("Diameter: could not compute")

    print(f"\n--- Hub Frames (top 15 by degree) ---")
    degree_sorted = sorted(U.degree(), key=lambda x: x[1], reverse=True)[:15]
    for slug, deg in degree_sorted:
        name = frame_names.get(slug, slug)
        print(f"  {name} ({slug}): {deg} connections")

    print(f"\n--- Bridges ---")
    bridges = list(nx.bridges(U))
    if bridges:
        print(f"{len(bridges)} bridge edge(s) (removing them disconnects the graph):")
        for u, v in bridges[:10]:
            print(f"  {frame_names.get(u, u)} <-> {frame_names.get(v, v)}")
    else:
        print("No bridges (graph is 2-edge-connected)")

    # Find some interesting multi-hop paths
    print(f"\n--- Multi-Hop Paths (sample) ---")
    nodes = list(largest if len(components) > 0 else G.nodes())
    if len(nodes) >= 2:
        # Find the pair with the longest shortest path
        try:
            all_pairs = dict(nx.all_pairs_shortest_path_length(subgraph))
            max_dist = 0
            max_pair = (None, None)
            for src, dists in all_pairs.items():
                for tgt, dist in dists.items():
                    if dist > max_dist:
                        max_dist = dist
                        max_pair = (src, tgt)

            if max_pair[0]:
                path = nx.shortest_path(U, max_pair[0], max_pair[1])
                path_names = [frame_names.get(n, n) for n in path]
                print(f"  Longest shortest path ({max_dist} hops):")
                print(f"    {' → '.join(path_names)}")

            # A few more interesting paths between distant domains
            interesting_pairs = [
                ("war", "love-and-relationships"),
                ("fluid-dynamics", "economics"),
                ("horticulture", "software-abstraction"),
                ("gambling", "philosophy"),
                ("medicine", "software-programs"),
            ]
            for src, tgt in interesting_pairs:
                if src in U and tgt in U and nx.has_path(U, src, tgt):
                    path = nx.shortest_path(U, src, tgt)
                    path_names = [frame_names.get(n, n) for n in path]
                    print(f"  {frame_names.get(src, src)} → {frame_names.get(tgt, tgt)} ({len(path)-1} hops):")
                    print(f"    {' → '.join(path_names)}")
        except Exception as e:
            print(f"  Path analysis failed: {e}")


def draw_graph(G: nx.DiGraph, frame_names: dict[str, str], output: str) -> None:
    """Draw the graph and save to file."""
    U = G.to_undirected()

    fig, ax = plt.subplots(1, 1, figsize=(20, 16))

    # Node sizes by degree
    degrees = dict(U.degree())
    node_sizes = [max(degrees.get(n, 1) * 120, 80) for n in U.nodes()]

    # Layout
    pos = nx.spring_layout(U, k=2.5, iterations=80, seed=42)

    # Edge widths by weight
    edge_weights = [U[u][v].get("weight", 1) * 0.5 for u, v in U.edges()]

    nx.draw_networkx_edges(U, pos, alpha=0.2, width=edge_weights, ax=ax)
    nx.draw_networkx_nodes(U, pos, node_size=node_sizes, node_color="#36c",
                           alpha=0.7, ax=ax)

    # Labels for high-degree nodes only
    labels = {n: frame_names.get(n, n) for n in U.nodes() if degrees.get(n, 0) >= 3}
    nx.draw_networkx_labels(U, pos, labels, font_size=7, font_family="sans-serif", ax=ax)

    ax.set_title(f"Metaphorex Frame Graph — {U.number_of_nodes()} frames, {U.number_of_edges()} edges",
                 fontsize=14)
    ax.axis("off")
    plt.tight_layout()
    plt.savefig(output, dpi=150, bbox_inches="tight")
    print(f"\nGraph saved to {output}")


def main() -> None:
    output = "graph.png"
    if "--output" in sys.argv:
        idx = sys.argv.index("--output")
        if idx + 1 < len(sys.argv):
            output = sys.argv[idx + 1]

    G, frame_names = load_graph()
    print_stats(G, frame_names)
    draw_graph(G, frame_names, output)


if __name__ == "__main__":
    main()
