/**
 * Catalog parser — reads all mapping markdown files, extracts frontmatter
 * and per-proposition bullet lists (transfers, limits, expressions).
 */

import { Glob } from "bun";
import matter from "gray-matter";
import { join } from "path";

// ---------------------------------------------------------------------------
// Types
// ---------------------------------------------------------------------------

export interface CatalogEntry {
  slug: string;
  name: string;
  kind: "metaphor" | "pattern" | "archetype" | "paradigm" | "mental-model";
  sourceFrame?: string;
  appliesTo?: string[];
  categories: string[];
  grounding: "proven" | "established" | "folk" | "contested";
  transfers: string[];
  limits: string[];
  expressions: string[];
}

// ---------------------------------------------------------------------------
// Parsing helpers
// ---------------------------------------------------------------------------

/**
 * Split markdown body into { heading: content } dict.
 * Mirrors validate.py's parse_sections().
 */
export function parseSections(content: string): Record<string, string> {
  const sections: Record<string, string> = {};
  let currentHeading: string | null = null;
  let currentLines: string[] = [];

  for (const line of content.split("\n")) {
    const m = line.match(/^## (.+)$/);
    if (m) {
      if (currentHeading !== null) {
        sections[currentHeading] = currentLines.join("\n").trim();
      }
      currentHeading = m[1].trim();
      currentLines = [];
    } else if (currentHeading !== null) {
      currentLines.push(line);
    }
  }

  if (currentHeading !== null) {
    sections[currentHeading] = currentLines.join("\n").trim();
  }

  return sections;
}

/**
 * Extract `- ` bullet items from a section body.
 *
 * Rules:
 *  - Only lines starting with `- ` begin a bullet.
 *  - Continuation lines (indented 2+ spaces) are joined with a space.
 *  - Non-bullet prose lines (paragraphs, blank lines) are skipped.
 */
export function extractBullets(sectionContent: string): string[] {
  const bullets: string[] = [];
  let current: string | null = null;

  for (const line of sectionContent.split("\n")) {
    if (line.startsWith("- ")) {
      // Flush previous bullet
      if (current !== null) bullets.push(current);
      current = line.slice(2); // strip leading "- "
    } else if (current !== null && /^ {2,}/.test(line)) {
      // Continuation of current bullet
      current += " " + line.trim();
    } else {
      // Prose or blank line — flush any open bullet
      if (current !== null) {
        bullets.push(current);
        current = null;
      }
    }
  }

  // Flush last bullet
  if (current !== null) bullets.push(current);

  return bullets;
}

// ---------------------------------------------------------------------------
// Catalog reader
// ---------------------------------------------------------------------------

export async function readCatalog(): Promise<CatalogEntry[]> {
  const repoRoot = join(import.meta.dirname!, "..", "..");
  const mappingsDir = join(repoRoot, "catalog", "mappings");

  const glob = new Glob("*.md");
  const entries: CatalogEntry[] = [];

  for await (const file of glob.scan(mappingsDir)) {
    const fullPath = join(mappingsDir, file);
    const raw = await Bun.file(fullPath).text();
    const { data, content } = matter(raw);

    const sections = parseSections(content);

    entries.push({
      slug: data.slug,
      name: data.name,
      kind: data.kind,
      sourceFrame: data.source_frame ?? undefined,
      appliesTo: data.applies_to ?? undefined,
      categories: data.categories ?? [],
      grounding: data.grounding ?? "folk",
      transfers: extractBullets(sections["Transfers"] ?? ""),
      limits: extractBullets(sections["Limits"] ?? ""),
      expressions: extractBullets(sections["Expressions"] ?? ""),
    });
  }

  // Sort by slug for deterministic output
  entries.sort((a, b) => a.slug.localeCompare(b.slug));
  return entries;
}

// ---------------------------------------------------------------------------
// Self-test
// ---------------------------------------------------------------------------

if (import.meta.main) {
  const entries = await readCatalog();

  console.log(`Total mappings: ${entries.length}`);

  const totalTransfers = entries.reduce((s, e) => s + e.transfers.length, 0);
  const totalLimits = entries.reduce((s, e) => s + e.limits.length, 0);
  const totalExpressions = entries.reduce((s, e) => s + e.expressions.length, 0);

  console.log(`Total transfers: ${totalTransfers}`);
  console.log(`Total limits:    ${totalLimits}`);
  console.log(`Total expressions: ${totalExpressions}`);

  const sample = entries.find((e) => e.slug === "argument-is-war");
  if (sample) {
    console.log(`\n--- argument-is-war ---`);
    console.log(`transfers (${sample.transfers.length}):`);
    sample.transfers.slice(0, 2).forEach((t) => console.log(`  ${t.slice(0, 100)}...`));
    console.log(`limits (${sample.limits.length}):`);
    sample.limits.slice(0, 2).forEach((l) => console.log(`  ${l.slice(0, 100)}...`));
    console.log(`expressions (${sample.expressions.length}):`);
    sample.expressions.slice(0, 2).forEach((e) => console.log(`  ${e.slice(0, 100)}...`));
  } else {
    console.log("argument-is-war not found!");
  }
}
