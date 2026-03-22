// scripts/build-neighbors.ts
// Build-time computation of structural neighbors for each entry.
// Outputs site/src/data/neighbors.json — consumed by entry pages at build time.
//
// Usage: bun run scripts/build-neighbors.ts

import { resolve } from "node:path";
import { writeFileSync, mkdirSync } from "node:fs";
import { readCatalog, type CatalogEntry } from "./lib/catalog.ts";

const ROOT = resolve(import.meta.dirname!, "..");
const OUT_DIR = resolve(ROOT, "site/src/data");
const OUT_PATH = resolve(OUT_DIR, "neighbors.json");

// ---------------------------------------------------------------------------
// IDF-style weights (same as eval-structural.ts and explore_structure.py)
// ---------------------------------------------------------------------------

const RELATION_WEIGHTS: Record<string, number> = {
  cause: 0.3, transform: 0.3,
  prevent: 0.8, enable: 0.8, contain: 0.8,
  coordinate: 1.0, compete: 1.0, select: 1.0, accumulate: 1.0,
  translate: 1.3, decompose: 1.3, restore: 1.3,
};

const EP_WEIGHTS: Record<string, number> = {
  force: 0.5, path: 0.5, container: 0.6,
  boundary: 0.7, matching: 0.7, scale: 0.8,
  flow: 0.9, "part-whole": 0.9, link: 0.9, balance: 0.9,
  "surface-depth": 1.0, "near-far": 1.0, iteration: 1.0,
  blockage: 1.0, "center-periphery": 1.1,
  accretion: 1.2, removal: 1.1, splitting: 1.2,
  merging: 1.3, "self-organization": 1.3,
  superimposition: 1.3, attraction: 1.5,
};

// ---------------------------------------------------------------------------
// Similarity functions
// ---------------------------------------------------------------------------

function parentOf(v: string): string {
  const idx = v.indexOf("/");
  return idx >= 0 ? v.slice(0, idx) : v;
}

function weightedJaccard(a: string[], b: string[], weights: Record<string, number>): number {
  const setA = new Set(a);
  const setB = new Set(b);
  const bMatched = new Set<string>();
  let interWeight = 0;
  let unionWeight = 0;

  const all = new Set([...setA, ...setB]);
  for (const v of all) {
    const w = weights[parentOf(v)] ?? 1.0;
    unionWeight += w;

    if (setA.has(v) && setB.has(v)) {
      interWeight += w;
      bMatched.add(v);
    } else if (setA.has(v) && v.includes("/")) {
      const parent = parentOf(v);
      for (const bv of setB) {
        if (!bMatched.has(bv) && parentOf(bv) === parent && bv !== v) {
          interWeight += w * 0.3;
          bMatched.add(bv);
          break;
        }
      }
    }
  }
  return unionWeight === 0 ? 0 : interWeight / unionWeight;
}

function jaccard(a: string[], b: string[]): number {
  const setA = new Set(a);
  const setB = new Set(b);
  let inter = 0;
  for (const v of setA) if (setB.has(v)) inter++;
  const union = setA.size + setB.size - inter;
  return union === 0 ? 0 : inter / union;
}

interface TaggedEntry {
  slug: string;
  name: string;
  kind: string;
  sourceFrame: string;
  ep: string[];
  rt: string[];
  st: string[];
  al: string;
}

function structuralSim(a: TaggedEntry, b: TaggedEntry): number {
  const epSim = weightedJaccard(a.ep, b.ep, EP_WEIGHTS);
  const rtSim = weightedJaccard(a.rt, b.rt, RELATION_WEIGHTS);
  const stSim = jaccard(a.st, b.st);
  const alSim = a.al === b.al ? 1.0 : 0.0;
  return epSim * 0.35 + rtSim * 0.35 + stSim * 0.20 + alSim * 0.10;
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

const catalog = await readCatalog();
console.log(`Read ${catalog.length} entries`);

// Convert to tagged entries (skip entries without structural tags)
const tagged: TaggedEntry[] = [];
for (const e of catalog) {
  const meta = e as any;
  // readCatalog doesn't expose structural fields — read them from frontmatter
  // We need to re-parse. Use a lightweight approach.
  tagged.push({
    slug: e.slug,
    name: e.name,
    kind: e.kind,
    sourceFrame: e.sourceFrame ?? "",
    ep: (meta.embodiedPatterns ?? []) as string[],
    rt: (meta.relationTypes ?? []) as string[],
    st: (meta.structure ?? []) as string[],
    al: (meta.abstractionLevel ?? "") as string,
  });
}

// readCatalog doesn't have the structural fields — let's parse them directly
import matter from "gray-matter";
import { Glob } from "bun";
import { join } from "path";

const entriesDir = join(ROOT, "catalog", "entries");
const taggedEntries: TaggedEntry[] = [];

const glob = new Glob("*.md");
for await (const file of glob.scan(entriesDir)) {
  const fullPath = join(entriesDir, file);
  const raw = await Bun.file(fullPath).text();
  const { data } = matter(raw);

  if (!data.embodied_patterns) continue; // skip unenriched

  let st = data.structure ?? [];
  if (typeof st === "string") st = [st];

  taggedEntries.push({
    slug: data.slug,
    name: data.name,
    kind: data.kind ?? "",
    sourceFrame: data.source_frame ?? "",
    ep: data.embodied_patterns ?? [],
    rt: data.relation_types ?? [],
    st,
    al: data.abstraction_level ?? "",
  });
}

taggedEntries.sort((a, b) => a.slug.localeCompare(b.slug));
console.log(`${taggedEntries.length} entries with structural tags`);

// Compute neighbors
type NeighborEntry = {
  slug: string;
  name: string;
  kind: string;
  sourceFrame: string;
  sim: number;
  sharedEp: string[];
  sharedRt: string[];
};

type NeighborMap = Record<string, {
  crossDomain: NeighborEntry[];
  sameDomain: NeighborEntry[];
}>;

const TOP_N_CROSS = 8;
const TOP_N_SAME = 4;
const MIN_SIM = 0.25;

console.log("Computing pairwise similarities...");
const neighbors: NeighborMap = {};

for (const a of taggedEntries) {
  const crossDomain: NeighborEntry[] = [];
  const sameDomain: NeighborEntry[] = [];

  for (const b of taggedEntries) {
    if (a.slug === b.slug) continue;
    const sim = structuralSim(a, b);
    if (sim < MIN_SIM) continue;

    const entry: NeighborEntry = {
      slug: b.slug,
      name: b.name,
      kind: b.kind,
      sourceFrame: b.sourceFrame,
      sim: parseFloat(sim.toFixed(3)),
      sharedEp: a.ep.filter((v) => b.ep.includes(v)),
      sharedRt: a.rt.filter((v) => b.rt.includes(v)),
    };

    if (a.sourceFrame !== b.sourceFrame) {
      crossDomain.push(entry);
    } else {
      sameDomain.push(entry);
    }
  }

  crossDomain.sort((a, b) => b.sim - a.sim);
  sameDomain.sort((a, b) => b.sim - a.sim);

  neighbors[a.slug] = {
    crossDomain: crossDomain.slice(0, TOP_N_CROSS),
    sameDomain: sameDomain.slice(0, TOP_N_SAME),
  };
}

// Also build a compact tag index for client-side faceted search
const tagIndex = taggedEntries.map((e) => ({
  s: e.slug,
  n: e.name,
  k: e.kind,
  f: e.sourceFrame,
  ep: e.ep,
  rt: e.rt,
  st: e.st,
  al: e.al,
}));

// Write outputs
mkdirSync(OUT_DIR, { recursive: true });

writeFileSync(OUT_PATH, JSON.stringify(neighbors));
const neighborsSize = (JSON.stringify(neighbors).length / 1024).toFixed(0);
console.log(`Neighbors written to ${OUT_PATH} (${neighborsSize}KB)`);

const tagIndexPath = resolve(OUT_DIR, "tag-index.json");
writeFileSync(tagIndexPath, JSON.stringify(tagIndex));
const tagIndexSize = (JSON.stringify(tagIndex).length / 1024).toFixed(0);
console.log(`Tag index written to ${tagIndexPath} (${tagIndexSize}KB)`);

console.log(`\nDone. ${Object.keys(neighbors).length} entries with neighbors.`);
