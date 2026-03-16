// scripts/search.ts
// Usage: bun run scripts/search.ts [--section transfer|limit|expression|title] [--kind metaphor|pattern|archetype|paradigm|mental-model] [--json] <query>

import { resolve } from "node:path";
import OpenAI from "openai";
import { openDb } from "./lib/db.ts";

const ROOT = resolve(import.meta.dirname!, "..");
const DB_PATH = resolve(ROOT, "catalog/embeddings.db");
const MODEL = "openai/text-embedding-3-small";
const K = 10;

const args = process.argv.slice(2);
let sectionFilter: string | null = null;
let kindFilter: string | null = null;
let jsonOutput = false;
const queryParts: string[] = [];

for (let i = 0; i < args.length; i++) {
  if (args[i] === "--section" && i + 1 < args.length) {
    sectionFilter = args[++i];
  } else if (args[i] === "--kind" && i + 1 < args.length) {
    kindFilter = args[++i];
  } else if (args[i] === "--json") {
    jsonOutput = true;
  } else {
    queryParts.push(args[i]);
  }
}

const query = queryParts.join(" ");
if (!query) {
  console.error("Usage: bun run scripts/search.ts [--section transfer|limit|expression|title] [--kind metaphor|pattern|archetype|paradigm|mental-model] [--json] <query>");
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

// Apply post-query filters
let filtered = results;
if (sectionFilter) {
  filtered = filtered.filter((r) => r.section === sectionFilter);
}
if (kindFilter) {
  filtered = filtered.filter((r) => r.kind === kindFilter);
}

// Deduplicate by slug — keep best (lowest distance) match per mapping
const bySlug = new Map<string, typeof filtered[0]>();
for (const row of filtered) {
  if (!bySlug.has(row.slug) || bySlug.get(row.slug)!.distance > row.distance) {
    bySlug.set(row.slug, row);
  }
}

// Sort by distance, take top K
const topResults = [...bySlug.values()]
  .sort((a, b) => a.distance - b.distance)
  .slice(0, K);

// Print results
// sqlite-vec returns L2 distance. For normalized vectors (OpenAI embeddings are
// normalized), convert to cosine similarity: cos_sim = 1 - (L2² / 2)
if (jsonOutput) {
  const output = topResults.map((r) => ({
    slug: r.slug,
    kind: r.kind,
    section: r.section,
    matchedText: r.text,
    score: parseFloat(Math.max(0, 1 - (r.distance * r.distance) / 2).toFixed(4)),
  }));
  console.log(JSON.stringify(output, null, 2));
} else {
  for (const r of topResults) {
    const cosineSim = 1 - (r.distance * r.distance) / 2;
    const score = Math.max(0, cosineSim).toFixed(2);
    const slug = r.slug.padEnd(30);
    const section = `[${r.section}]`.padEnd(14);
    const text = r.text.length > 60 ? r.text.slice(0, 57) + "..." : r.text;
    console.log(`${slug} ${section} ${score}  "${text}"`);
  }
}

db.close();
