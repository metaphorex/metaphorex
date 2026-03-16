// scripts/lib/search.ts
import { resolve } from "node:path";
import OpenAI from "openai";
import { openDb } from "./db.ts";

const ROOT = resolve(import.meta.dirname!, "..", "..");
const DB_PATH = resolve(ROOT, "catalog/embeddings.db");
const MODEL = "openai/text-embedding-3-small";

export interface SearchResult {
  slug: string;
  kind: string;
  section: string;
  matchedText: string;
  score: number;
  distance: number;
}

export interface SearchOptions {
  k?: number;
  section?: string;
  kind?: string;
}

let _openai: OpenAI | null = null;

function getOpenAI(): OpenAI {
  if (!_openai) {
    if (!process.env.OPENROUTER_API_KEY) {
      throw new Error("OPENROUTER_API_KEY environment variable is required");
    }
    _openai = new OpenAI({
      baseURL: "https://openrouter.ai/api/v1",
      apiKey: process.env.OPENROUTER_API_KEY,
    });
  }
  return _openai;
}

export async function search(
  query: string,
  opts: SearchOptions = {}
): Promise<SearchResult[]> {
  const { k = 10, section, kind } = opts;
  const db = openDb(DB_PATH);

  const storedModel = db.query(
    "SELECT value FROM meta WHERE key = 'embedding_model'"
  ).get() as { value: string } | null;
  if (storedModel && storedModel.value !== MODEL) {
    db.close();
    throw new Error(`Model mismatch: DB has ${storedModel.value}, search uses ${MODEL}`);
  }

  const openai = getOpenAI();
  const response = await openai.embeddings.create({
    model: MODEL,
    input: [query],
  });
  const queryVec = new Float32Array(response.data[0].embedding);

  const results = db.query(`
    SELECT r.slug, r.kind, r.section, r.text, e.distance
    FROM embeddings e
    JOIN embedding_records r ON r.id = e.id
    WHERE e.embedding MATCH ? AND k = ?
    ORDER BY e.distance
  `).all(queryVec, k * 3) as Array<{
    slug: string; kind: string; section: string; text: string; distance: number;
  }>;

  let filtered = results;
  if (section) filtered = filtered.filter((r) => r.section === section);
  if (kind) filtered = filtered.filter((r) => r.kind === kind);

  const bySlug = new Map<string, typeof filtered[0]>();
  for (const row of filtered) {
    if (!bySlug.has(row.slug) || bySlug.get(row.slug)!.distance > row.distance) {
      bySlug.set(row.slug, row);
    }
  }

  db.close();

  return [...bySlug.values()]
    .sort((a, b) => a.distance - b.distance)
    .slice(0, k)
    .map((r) => ({
      slug: r.slug,
      kind: r.kind,
      section: r.section,
      matchedText: r.text,
      score: Math.max(0, 1 - (r.distance * r.distance) / 2),
      distance: r.distance,
    }));
}
