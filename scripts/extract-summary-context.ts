/**
 * Extract minimal context for summary generation, tiered by difficulty.
 *
 * Reads tier-assignments.json + catalog entries, emits JSONL with just enough
 * context for LLM summary generation (not the whole entry).
 *
 * Usage: bun run scripts/extract-summary-context.ts \
 *          playbooks/summary-enrichment/tier-assignments.json \
 *          > playbooks/summary-enrichment/context.jsonl
 *
 * /// <reference types="bun-types" />
 */

import { readCatalog, parseSections, type CatalogEntry } from "./lib/catalog.ts";
import { join } from "path";
import matter from "gray-matter";

// ---------------------------------------------------------------------------
// Types
// ---------------------------------------------------------------------------

interface TierAssignments {
  tier1: string[];
  tier2: string[];
  tier3: string[];
}

interface SummaryContext {
  slug: string;
  tier: 1 | 2 | 3;
  name: string;
  kind: string;
  sourceFrame?: string;
  appliesTo?: string[];
  dead?: boolean;
  transfers: string[];
  limits: string[];
  bodyExcerpt?: string;
}

// ---------------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------------

function stripPrefix(s: string): string {
  return s.replace(/^\[.*?\]\s*/, "");
}

/** Read the raw body of an entry (below frontmatter) */
async function readEntryBody(slug: string): Promise<string> {
  const repoRoot = join(import.meta.dirname!, "..");
  const path = join(repoRoot, "catalog", "entries", `${slug}.md`);
  const raw = await Bun.file(path).text();
  const { content } = matter(raw);
  return content;
}

/** Get first paragraph from a body section */
function firstParagraph(sectionContent: string): string {
  const lines: string[] = [];
  for (const line of sectionContent.split("\n")) {
    if (line.trim() === "" && lines.length > 0) break;
    if (line.trim() !== "") lines.push(line.trim());
  }
  return lines.join(" ").slice(0, 500);
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

const assignmentsPath = process.argv[2];
if (!assignmentsPath) {
  console.error("Usage: bun run scripts/extract-summary-context.ts <tier-assignments.json>");
  process.exit(1);
}

const assignments: TierAssignments = JSON.parse(
  await Bun.file(assignmentsPath).text()
);

// Build slug → tier map
const slugTier = new Map<string, 1 | 2 | 3>();
for (const slug of assignments.tier1) slugTier.set(slug, 1);
for (const slug of assignments.tier2) slugTier.set(slug, 2);
for (const slug of assignments.tier3) slugTier.set(slug, 3);

const entries = await readCatalog();
const entryMap = new Map(entries.map((e) => [e.slug, e]));

for (const [slug, tier] of slugTier) {
  const entry = entryMap.get(slug);
  if (!entry) {
    console.error(`Warning: ${slug} in tier assignments but not in catalog`);
    continue;
  }

  const transfers = entry.transfers.map(stripPrefix);
  const limits = entry.limits.map(stripPrefix);

  const ctx: SummaryContext = {
    slug,
    tier,
    name: entry.name,
    kind: entry.kind,
    sourceFrame: entry.sourceFrame,
    appliesTo: entry.appliesTo,
    dead: entry.dead || undefined,
    transfers: [],
    limits: [],
  };

  switch (tier) {
    case 1:
      // Minimal: first 2 transfers only
      ctx.transfers = transfers.slice(0, 2);
      break;

    case 2:
      // Medium: all transfers + first limit
      ctx.transfers = transfers;
      ctx.limits = limits.slice(0, 1);
      break;

    case 3: {
      // Full: all transfers + all limits + body excerpt
      ctx.transfers = transfers;
      ctx.limits = limits;
      const body = await readEntryBody(slug);
      const sections = parseSections(body);
      const transfersSection = sections["Transfers"];
      if (transfersSection) {
        ctx.bodyExcerpt = firstParagraph(transfersSection);
      }
      break;
    }
  }

  console.log(JSON.stringify(ctx));
}
