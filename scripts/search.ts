// scripts/search.ts
// Usage: bun run scripts/search.ts <query>

import { resolve } from "node:path";
import OpenAI from "openai";
import { openDb } from "./lib/db.ts";

const ROOT = resolve(import.meta.dirname!, "..");
const DB_PATH = resolve(ROOT, "catalog/embeddings.db");
const MODEL = "openai/text-embedding-3-small";
const K = 10;

const query = process.argv.slice(2).join(" ");
if (!query) {
  console.error("Usage: bun run scripts/search.ts <query>");
  process.exit(1);
}

if (!process.env.OPENROUTER_API_KEY) {
  console.error("OPENROUTER_API_KEY environment variable is required");
  console.error("Run: source .envrc");
  process.exit(1);
}

const openai = new OpenAI({
  baseURL: "https://openrouter.ai/api/v1",
  apiKey: process.env.OPENROUTER_API_KEY,
});

const db = openDb(DB_PATH);

// Verify model matches what was used to build the DB
const storedModel = db.query("SELECT value FROM meta WHERE key = 'embedding_model'").get() as { value: string } | null;
if (storedModel && storedModel.value !== MODEL) {
  console.error(`Model mismatch: DB was built with ${storedModel.value}, search uses ${MODEL}`);
  console.error("Rebuild the database with: bun run scripts/build-db.ts");
  process.exit(1);
}

// Embed the query
const response = await openai.embeddings.create({
  model: MODEL,
  input: [query],
});
const queryVec = new Float32Array(response.data[0].embedding);

console.log(`Query: "${query}"\n`);

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
