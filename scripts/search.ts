// scripts/search.ts
// Usage: bun run scripts/search.ts <query>
// With random vectors this returns random results — proves plumbing works.

import { resolve } from "node:path";
import { openDb } from "./lib/db.ts";

const ROOT = resolve(import.meta.dirname!, "..");
const DB_PATH = resolve(ROOT, "catalog/embeddings.db");
const DIMS = 1536;
const K = 10;

const query = process.argv.slice(2).join(" ");
if (!query) {
  console.error("Usage: bun run scripts/search.ts <query>");
  process.exit(1);
}

const db = openDb(DB_PATH);

// Generate a random query vector (placeholder until real embeddings)
const queryVec = new Float32Array(DIMS);
for (let d = 0; d < DIMS; d++) queryVec[d] = Math.random() - 0.5;

console.log(`Query: "${query}"`);
console.log(`(Using random vectors — results are meaningless placeholders)\n`);

// sqlite-vec nearest neighbor search
const results = db.query(`
  SELECT
    r.slug,
    r.kind,
    r.section,
    r.text,
    e.distance
  FROM embeddings e
  JOIN embedding_records r ON r.id = e.id
  WHERE e.embedding MATCH ?
    AND k = ?
  ORDER BY e.distance
`).all(queryVec, K * 3) as Array<{
  slug: string;
  kind: string;
  section: string;
  text: string;
  distance: number;
}>;

// Deduplicate by slug — keep best (lowest distance) match per mapping
const bySlug = new Map<string, typeof results[0]>();
for (const row of results) {
  if (!bySlug.has(row.slug) || bySlug.get(row.slug)!.distance > row.distance) {
    bySlug.set(row.slug, row);
  }
}

// Sort by distance, take top K
const topResults = [...bySlug.values()]
  .sort((a, b) => a.distance - b.distance)
  .slice(0, K);

// Print results
for (const r of topResults) {
  const score = Math.max(0, 1 - r.distance).toFixed(2);
  const slug = r.slug.padEnd(30);
  const section = `[${r.section}]`.padEnd(14);
  const text = r.text.length > 60 ? r.text.slice(0, 57) + "..." : r.text;
  console.log(`${slug} ${section} ${score}  "${text}"`);
}

db.close();
