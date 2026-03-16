# Evaluation Framework Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build an evaluation script that measures vector search quality, compares m4x tool results against raw LLM responses, and identifies catalog gaps — producing a structured markdown report.

**Architecture:** A single `scripts/eval.ts` script that runs three eval suites sequentially: (A) structural search quality with known-good expected results, (B) side-by-side m4x vs raw Claude comparisons via OpenRouter, (C) catalog coverage analysis. Results are written to `docs/evals/YYYY-MM-DD-eval-report.md`.

**Tech Stack:** Bun, OpenAI SDK (pointing at OpenRouter for both embeddings and Claude chat), existing `scripts/lib/db.ts` and search infrastructure, sqlite-vec.

---

### Task 1: Extract search into a reusable library function

**Files:**
- Create: `scripts/lib/search.ts`
- Modify: `scripts/search.ts` — import from lib instead of inlining

Currently, the search logic lives inline in `scripts/search.ts`. The eval script needs to call it programmatically. Extract the core search into a library function.

**Step 1: Create scripts/lib/search.ts**

```typescript
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
  score: number;     // cosine similarity (0–1)
  distance: number;  // raw L2 distance
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

  // Model consistency check
  const storedModel = db.query(
    "SELECT value FROM meta WHERE key = 'embedding_model'"
  ).get() as { value: string } | null;
  if (storedModel && storedModel.value !== MODEL) {
    db.close();
    throw new Error(`Model mismatch: DB has ${storedModel.value}, search uses ${MODEL}`);
  }

  // Embed the query
  const openai = getOpenAI();
  const response = await openai.embeddings.create({
    model: MODEL,
    input: [query],
  });
  const queryVec = new Float32Array(response.data[0].embedding);

  // KNN search
  const results = db.query(`
    SELECT r.slug, r.kind, r.section, r.text, e.distance
    FROM embeddings e
    JOIN embedding_records r ON r.id = e.id
    WHERE e.embedding MATCH ? AND k = ?
    ORDER BY e.distance
  `).all(queryVec, k * 3) as Array<{
    slug: string; kind: string; section: string; text: string; distance: number;
  }>;

  // Filter
  let filtered = results;
  if (section) filtered = filtered.filter((r) => r.section === section);
  if (kind) filtered = filtered.filter((r) => r.kind === kind);

  // Dedupe by slug
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
```

**Step 2: Refactor scripts/search.ts to use the library**

Replace the inline search logic with:
```typescript
import { search } from "./lib/search.ts";

// ... arg parsing stays the same ...

const results = await search(query, {
  k: K,
  section: sectionFilter ?? undefined,
  kind: kindFilter ?? undefined,
});

// ... output formatting stays the same, but uses results from lib ...
```

**Step 3: Verify search.ts still works**

Run: `source .envrc && bun run scripts/search.ts "accumulated cost of shortcuts"`
Expected: Same results as before refactor (technical-debt, time-is-money, etc.)

**Step 4: Commit**

```bash
git add scripts/lib/search.ts scripts/search.ts
git commit -m "refactor: extract search into reusable library function"
```

**Verify:** Search CLI produces identical results to before.

---

### Task 2: Eval suite A — Structural search quality

**Files:**
- Create: `scripts/eval.ts`

This suite tests whether vector search finds structurally similar entries across different source domains.

**Step 1: Create the eval runner scaffold and Suite A test cases**

```typescript
// scripts/eval.ts
// Usage: bun run scripts/eval.ts [--suite a|b|c|all] [--output docs/evals/report.md]
import { resolve } from "node:path";
import { writeFileSync, mkdirSync } from "node:fs";
import { search, type SearchResult } from "./lib/search.ts";

const ROOT = resolve(import.meta.dirname!, "..");

// ---------------------------------------------------------------------------
// Types
// ---------------------------------------------------------------------------

interface StructuralTestCase {
  name: string;
  query: string;
  section?: string;
  expectedSlugs: string[];    // at least one of these should appear in top 5
  antiSlugs?: string[];       // these should NOT dominate (topical-only matches)
}

interface SuiteAResult {
  name: string;
  query: string;
  hits: SearchResult[];
  expectedFound: string[];    // which expected slugs appeared in top 5
  expectedMissed: string[];   // which expected slugs were absent
  antiSlugViolations: string[]; // anti-slugs that appeared in top 3
  pass: boolean;
}

// ---------------------------------------------------------------------------
// Suite A: Structural search quality
// ---------------------------------------------------------------------------

const STRUCTURAL_TESTS: StructuralTestCase[] = [
  {
    name: "blockage-cascade",
    query: "blockage at one point causes problems everywhere downstream",
    expectedSlugs: ["bottleneck", "the-pipeline-pattern", "data-flow-is-fluid-flow", "yak-shaving"],
    // Should find these across different source frames, not just plumbing
  },
  {
    name: "accumulated-cost",
    query: "accumulated cost of past shortcuts compounds over time",
    expectedSlugs: ["technical-debt", "compounding", "mental-accounting", "moral-accounting"],
  },
  {
    name: "container-boundary",
    query: "boundaries that protect also isolate and trap",
    expectedSlugs: ["relationships-are-enclosures", "firewall", "ai-safety-is-containment", "activities-are-containers", "categories-are-containers"],
  },
  {
    name: "threshold-trigger",
    query: "a small input crosses a threshold and triggers a disproportionately large response",
    expectedSlugs: ["activation-energy", "nonlinearity", "tipping-point"],
  },
  {
    name: "map-territory-reification",
    query: "the model becomes confused with the thing it models",
    expectedSlugs: ["the-map-is-not-the-territory"],
  },
  {
    name: "transfer-only-debt",
    query: "interest compounds on deferred work",
    section: "transfer",
    expectedSlugs: ["technical-debt", "compounding"],
  },
  {
    name: "limit-only-debt",
    query: "the metaphor makes it hard to quantify or prioritize",
    section: "limit",
    expectedSlugs: ["technical-debt"],
  },
  {
    name: "expression-detection",
    query: "we need to pay down our tech debt before the pipeline gets clogged",
    section: "expression",
    expectedSlugs: ["technical-debt", "the-pipeline-pattern"],
  },
  {
    name: "cross-domain-structure",
    query: "removing one part causes the whole system to collapse",
    expectedSlugs: ["redundancy", "jenga"],
  },
  {
    name: "adversarial-framing",
    query: "framing a collaborative activity as a competition with winners and losers",
    expectedSlugs: ["argument-is-war", "competition-is-competition-for-desired-objects"],
  },
];

async function runSuiteA(): Promise<SuiteAResult[]> {
  console.log("\n=== Suite A: Structural Search Quality ===\n");
  const results: SuiteAResult[] = [];

  for (const test of STRUCTURAL_TESTS) {
    process.stdout.write(`  ${test.name}... `);
    const hits = await search(test.query, { k: 10, section: test.section });
    const topSlugs = hits.slice(0, 5).map((h) => h.slug);

    const expectedFound = test.expectedSlugs.filter((s) => topSlugs.includes(s));
    const expectedMissed = test.expectedSlugs.filter((s) => !topSlugs.includes(s));
    const antiSlugViolations = (test.antiSlugs ?? []).filter((s) =>
      hits.slice(0, 3).some((h) => h.slug === s)
    );

    // Pass if at least one expected slug in top 5 and no anti-slug violations
    const pass = expectedFound.length > 0 && antiSlugViolations.length === 0;
    console.log(pass ? "PASS" : "FAIL",
      `(${expectedFound.length}/${test.expectedSlugs.length} expected found)`);

    results.push({
      name: test.name,
      query: test.query,
      hits,
      expectedFound,
      expectedMissed,
      antiSlugViolations,
      pass,
    });
  }

  return results;
}

// ---------------------------------------------------------------------------
// Report generation
// ---------------------------------------------------------------------------

function generateSuiteAReport(results: SuiteAResult[]): string {
  const passed = results.filter((r) => r.pass).length;
  let md = `## Suite A: Structural Search Quality\n\n`;
  md += `**${passed}/${results.length} tests passed**\n\n`;

  for (const r of results) {
    md += `### ${r.name} ${r.pass ? "PASS" : "FAIL"}\n\n`;
    md += `**Query:** "${r.query}"\n\n`;

    if (r.hits[0]?.score !== undefined) {
      md += `| # | slug | section | score | matched text |\n`;
      md += `|---|------|---------|-------|--------------|\n`;
      for (const [i, h] of r.hits.slice(0, 5).entries()) {
        const marker = r.expectedFound.includes(h.slug) ? " **expected**" : "";
        md += `| ${i + 1} | ${h.slug}${marker} | ${h.section} | ${h.score.toFixed(2)} | ${h.matchedText.slice(0, 60)}... |\n`;
      }
      md += `\n`;
    }

    if (r.expectedMissed.length > 0) {
      md += `**Missing expected:** ${r.expectedMissed.join(", ")}\n\n`;
    }
    if (r.antiSlugViolations.length > 0) {
      md += `**Anti-slug violations:** ${r.antiSlugViolations.join(", ")}\n\n`;
    }
  }

  return md;
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

async function main() {
  const args = process.argv.slice(2);
  let suite = "all";
  let outputPath: string | null = null;

  for (let i = 0; i < args.length; i++) {
    if (args[i] === "--suite" && i + 1 < args.length) suite = args[++i];
    if (args[i] === "--output" && i + 1 < args.length) outputPath = args[++i];
  }

  const today = new Date().toISOString().slice(0, 10);
  if (!outputPath) outputPath = resolve(ROOT, `docs/evals/${today}-eval-report.md`);

  let report = `# Metaphorex Search Evaluation Report\n\n`;
  report += `**Date:** ${today}\n`;
  report += `**Catalog size:** (see stats below)\n\n---\n\n`;

  if (suite === "a" || suite === "all") {
    const suiteAResults = await runSuiteA();
    report += generateSuiteAReport(suiteAResults);
    report += `---\n\n`;
  }

  // Suite B and C placeholders — added in subsequent tasks
  if (suite === "b" || suite === "all") {
    report += `## Suite B: m4x vs Raw LLM\n\n*Not yet implemented*\n\n---\n\n`;
  }
  if (suite === "c" || suite === "all") {
    report += `## Suite C: Catalog Coverage\n\n*Not yet implemented*\n\n---\n\n`;
  }

  // Write report
  const dir = resolve(outputPath, "..");
  mkdirSync(dir, { recursive: true });
  writeFileSync(outputPath, report);
  console.log(`\nReport written to ${outputPath}`);
}

main();
```

**Step 2: Run Suite A**

Run: `source .envrc && bun run scripts/eval.ts --suite a`
Expected: 10 test cases run, each showing PASS/FAIL. Report written to `docs/evals/`.

Some tests may fail — that's signal, not bugs. Adjust expected slugs if the catalog doesn't contain what we assumed.

**Step 3: Commit**

```bash
git add scripts/eval.ts
git commit -m "feat: eval framework with Suite A structural search tests"
```

**Verify:** Suite A runs without errors. Report file exists and contains per-test result tables.

---

### Task 3: Eval suite B — m4x vs raw Claude

**Files:**
- Modify: `scripts/eval.ts` — add Suite B

This suite sends identical prompts to Claude models via OpenRouter, once with m4x search results in context and once without. Compares breadth, depth, and non-obvious insight.

**Step 1: Add Claude chat helper and Suite B types**

Add to `scripts/eval.ts`:

```typescript
// ---------------------------------------------------------------------------
// LLM helper (Claude via OpenRouter)
// ---------------------------------------------------------------------------

const CLAUDE_MODELS = [
  "anthropic/claude-sonnet-4",
] as const;

async function chatCompletion(
  model: string,
  systemPrompt: string,
  userPrompt: string,
): Promise<string> {
  const openai = new OpenAI({
    baseURL: "https://openrouter.ai/api/v1",
    apiKey: process.env.OPENROUTER_API_KEY!,
  });

  const response = await openai.chat.completions.create({
    model,
    messages: [
      { role: "system", content: systemPrompt },
      { role: "user", content: userPrompt },
    ],
    max_tokens: 1500,
    temperature: 0,  // deterministic for eval reproducibility
  });

  return response.choices[0]?.message?.content ?? "";
}
```

**Step 2: Add Suite B test cases and runner**

```typescript
interface SuiteBTestCase {
  name: string;
  scenario: string;       // the situation to analyze
  searchQueries: string[]; // queries to run against m4x before prompting
}

const SUITE_B_TESTS: SuiteBTestCase[] = [
  {
    name: "microservices-design",
    scenario: "A queue-based microservices architecture where services communicate via message brokers, with circuit breakers for failure isolation and a shared database for state.",
    searchQueries: [
      "message queue processing pipeline",
      "circuit breaker failure isolation",
      "shared state coordination",
    ],
  },
  {
    name: "fast-growing-team",
    scenario: "A startup engineering team that grew from 5 to 50 in a year. The original founders still make most technical decisions. New hires feel they can't influence architecture. Knowledge lives in people's heads, not documentation.",
    searchQueries: [
      "knowledge hoarded by few people",
      "authority concentrated in founders",
      "oral tradition versus written documentation",
    ],
  },
  {
    name: "permissions-system",
    scenario: "We're designing a permissions system. Users have 'roles' that 'grant' them 'access' to 'resources'. Admins can 'delegate' permissions. There's an 'audit trail' of who 'gave' what access to whom.",
    searchQueries: [
      "roles as containers for capabilities",
      "granting access as giving possession",
      "hierarchical authority delegation",
    ],
  },
  {
    name: "ml-model-opacity",
    scenario: "A machine learning model has been retrained on production data so many times that nobody understands why it makes specific decisions. The team calls it 'the black box' and treats its outputs as 'predictions' that need 'confidence scores'.",
    searchQueries: [
      "black box opacity understanding",
      "prediction as oracle or prophecy",
      "confidence and certainty as measurable quantities",
    ],
  },
  {
    name: "code-review-as-war",
    scenario: "A team's code review process has become adversarial. Reviewers 'attack' PRs, authors 'defend' their decisions, people 'pick their battles' about which comments to address. Senior engineers use reviews to 'assert dominance'. New hires are afraid to submit PRs.",
    searchQueries: [
      "collaboration framed as combat",
      "critique as attack",
      "dominance hierarchy in technical evaluation",
    ],
  },
];

const SYSTEM_PROMPT_RAW = `You are analyzing which conceptual metaphors are active in a given scenario. For each metaphor you identify:
1. Name it (e.g., "ARGUMENT IS WAR")
2. Explain what structural assumptions it carries
3. Identify where it might mislead — what does the metaphor make hard to see?

Be specific. Focus on non-obvious metaphors, not just the surface-level ones. List at least 5 metaphors.`;

const SYSTEM_PROMPT_WITH_M4X = `You are analyzing which conceptual metaphors are active in a given scenario. You have access to results from a metaphor catalog search. Use these results as a starting point, but also identify metaphors the search may have missed.

For each metaphor you identify:
1. Name it (e.g., "ARGUMENT IS WAR") and note if it came from the catalog search
2. Explain what structural assumptions it carries
3. Identify where it might mislead — what does the metaphor make hard to see?

Be specific. Focus on non-obvious metaphors, not just the surface-level ones. List at least 5 metaphors.`;

async function runSuiteB(): Promise<string> {
  console.log("\n=== Suite B: m4x vs Raw Claude ===\n");
  let md = `## Suite B: m4x vs Raw Claude\n\n`;

  for (const test of SUITE_B_TESTS) {
    console.log(`  ${test.name}...`);

    // Run m4x searches
    const searchResults: SearchResult[] = [];
    for (const q of test.searchQueries) {
      const results = await search(q, { k: 5 });
      searchResults.push(...results);
    }

    // Dedupe search results by slug
    const seen = new Set<string>();
    const uniqueResults = searchResults.filter((r) => {
      if (seen.has(r.slug)) return false;
      seen.add(r.slug);
      return true;
    }).slice(0, 15);

    // Format search results for injection
    const searchContext = uniqueResults.map((r) =>
      `- **${r.slug}** [${r.section}] (score: ${r.score.toFixed(2)}): ${r.matchedText.slice(0, 120)}`
    ).join("\n");

    for (const model of CLAUDE_MODELS) {
      const modelShort = model.split("/")[1];
      process.stdout.write(`    ${modelShort} raw... `);

      // (A) Raw — no tools
      const rawResponse = await chatCompletion(
        model, SYSTEM_PROMPT_RAW,
        `Scenario: ${test.scenario}`
      );
      console.log("done");

      // (B) With m4x results
      process.stdout.write(`    ${modelShort} +m4x... `);
      const m4xResponse = await chatCompletion(
        model, SYSTEM_PROMPT_WITH_M4X,
        `Scenario: ${test.scenario}\n\n## Catalog search results:\n\n${searchContext}`
      );
      console.log("done");

      md += `### ${test.name} (${modelShort})\n\n`;
      md += `**Scenario:** ${test.scenario}\n\n`;
      md += `**Search results injected (${uniqueResults.length} entries):**\n${searchContext}\n\n`;
      md += `#### Raw Claude (no tools)\n\n${rawResponse}\n\n`;
      md += `#### Claude + m4x search\n\n${m4xResponse}\n\n`;
      md += `---\n\n`;
    }
  }

  return md;
}
```

**Step 3: Wire Suite B into main()**

In the `main()` function, replace the Suite B placeholder:
```typescript
  if (suite === "b" || suite === "all") {
    const suiteBReport = await runSuiteB();
    report += suiteBReport;
    report += `---\n\n`;
  }
```

**Step 4: Run Suite B alone first (it's slower — LLM calls)**

Run: `source .envrc && bun run scripts/eval.ts --suite b`
Expected: 5 scenarios x 1 model x 2 modes = 10 LLM calls. Takes 1-2 minutes.
Report shows raw vs m4x responses side by side.

**Step 5: Commit**

```bash
git add scripts/eval.ts
git commit -m "feat: Suite B — m4x vs raw Claude side-by-side comparison"
```

**Verify:** Report contains side-by-side responses. m4x-augmented responses should reference specific catalog entries.

---

### Task 4: Eval suite C — Catalog coverage analysis

**Files:**
- Modify: `scripts/eval.ts` — add Suite C

This suite runs diverse structural queries and measures the hit/miss rate to identify catalog gaps.

**Step 1: Add Suite C test cases and runner**

```typescript
interface CoverageTestCase {
  name: string;
  query: string;
  domain: string;   // what domain this probes
}

const COVERAGE_TESTS: CoverageTestCase[] = [
  { name: "feedback-loop", query: "output feeds back as input, amplifying or dampening over time", domain: "systems" },
  { name: "erosion", query: "gradual degradation that is invisible until sudden failure", domain: "materials" },
  { name: "immune-response", query: "system detects foreign elements and mounts a defense that can itself cause damage", domain: "biology" },
  { name: "debt-servicing", query: "ongoing payments consume resources that could be used productively", domain: "economics" },
  { name: "scaffolding", query: "temporary structure that enables building but must be removed", domain: "construction" },
  { name: "fermentation", query: "controlled decay that produces something valuable", domain: "biology" },
  { name: "triage", query: "rapid sorting under resource scarcity to maximize outcomes", domain: "medicine" },
  { name: "terraforming", query: "reshaping an environment to support a different kind of life", domain: "science-fiction" },
  { name: "composting", query: "breaking down old material to nourish new growth", domain: "agriculture" },
  { name: "signal-noise", query: "separating meaningful information from random interference", domain: "engineering" },
  { name: "vaccination", query: "controlled exposure to a weakened threat builds resistance", domain: "medicine" },
  { name: "pruning", query: "removing parts to strengthen the whole", domain: "agriculture" },
  { name: "migration", query: "moving from one habitat to another when conditions change", domain: "ecology" },
  { name: "crystallization", query: "gradual solidification from fluid to rigid structure", domain: "chemistry" },
  { name: "phase-transition", query: "sudden qualitative change when a quantitative threshold is crossed", domain: "physics" },
  { name: "keystone-species", query: "one component whose removal causes ecosystem collapse", domain: "ecology" },
  { name: "sedimentation", query: "layers accumulate over time, earlier layers become inaccessible", domain: "geology" },
  { name: "pollination", query: "cross-fertilization between separate entities produces novel offspring", domain: "biology" },
  { name: "pressure-valve", query: "controlled release mechanism that prevents catastrophic failure", domain: "engineering" },
  { name: "succession", query: "one type of growth prepares the conditions for the next type", domain: "ecology" },
];

async function runSuiteC(): Promise<string> {
  console.log("\n=== Suite C: Catalog Coverage Analysis ===\n");
  let md = `## Suite C: Catalog Coverage Analysis\n\n`;

  const gaps: string[] = [];
  const covered: string[] = [];

  for (const test of COVERAGE_TESTS) {
    process.stdout.write(`  ${test.name}... `);
    const results = await search(test.query, { k: 5 });

    // A "hit" means the top result has score > 0.40 (meaningful similarity)
    const topScore = results[0]?.score ?? 0;
    const isHit = topScore > 0.40;

    if (isHit) {
      covered.push(test.name);
      console.log(`HIT (${topScore.toFixed(2)}) → ${results[0].slug}`);
    } else {
      gaps.push(test.name);
      console.log(`GAP (${topScore.toFixed(2)})`);
    }

    md += `### ${test.name} (${test.domain}) — ${isHit ? "HIT" : "GAP"}\n\n`;
    md += `**Query:** "${test.query}"\n\n`;
    md += `| # | slug | section | score | matched text |\n`;
    md += `|---|------|---------|-------|--------------|\n`;
    for (const [i, r] of results.slice(0, 3).entries()) {
      md += `| ${i + 1} | ${r.slug} | ${r.section} | ${r.score.toFixed(2)} | ${r.matchedText.slice(0, 60)}... |\n`;
    }
    md += `\n`;
  }

  md += `### Summary\n\n`;
  md += `**Coverage:** ${covered.length}/${COVERAGE_TESTS.length} (${(covered.length / COVERAGE_TESTS.length * 100).toFixed(0)}%)\n\n`;
  md += `**Covered:** ${covered.join(", ")}\n\n`;
  md += `**Gaps:** ${gaps.join(", ")}\n\n`;
  md += `Gaps represent either missing catalog entries or propositions that don't embed near the structural query. Each gap is a candidate for new content or for improving existing entry wording.\n\n`;

  return md;
}
```

**Step 2: Wire Suite C into main()**

Replace the Suite C placeholder in `main()`:
```typescript
  if (suite === "c" || suite === "all") {
    const suiteCReport = await runSuiteC();
    report += suiteCReport;
  }
```

**Step 3: Run Suite C**

Run: `source .envrc && bun run scripts/eval.ts --suite c`
Expected: 20 coverage queries, each showing HIT or GAP with top matches.

**Step 4: Commit**

```bash
git add scripts/eval.ts
git commit -m "feat: Suite C — catalog coverage analysis with gap detection"
```

**Verify:** Report shows coverage percentage and lists specific gaps. Gaps are real signal about where the catalog needs content.

---

### Task 5: Add docs/evals/ to gitignore, full run, create branch and PR

**Files:**
- Modify: `.gitignore` — add `docs/evals/` (reports are generated artifacts)

**Step 1: Gitignore eval reports**

Add to `.gitignore`:
```
docs/evals/
```

Reports are generated artifacts — they contain LLM responses that shouldn't be committed. The eval *script* is committed; the *output* is not.

**Step 2: Run the full eval suite**

Run: `source .envrc && bun run scripts/eval.ts --suite all`
Expected: All three suites run. Full report written to `docs/evals/YYYY-MM-DD-eval-report.md`.
Takes 3-5 minutes (embedding calls + LLM calls).

**Step 3: Read and sanity-check the report**

Open the report. Check:
- Suite A: Do PASS/FAIL results make sense? Are any expected slugs wrong?
- Suite B: Do the m4x-augmented responses reference catalog entries? Are they richer?
- Suite C: Does the coverage percentage feel right? Do gaps point to real missing content?

**Step 4: Commit everything on a branch and open a PR**

```bash
git checkout -b feat/eval-framework
git add scripts/lib/search.ts scripts/eval.ts scripts/search.ts .gitignore
git commit -m "feat: evaluation framework for vector search quality

Three eval suites:
- Suite A: structural search quality (10 tests with expected results)
- Suite B: m4x vs raw Claude side-by-side (5 scenarios)
- Suite C: catalog coverage analysis (20 structural queries)

Uses OpenRouter for both embeddings and Claude API calls."

git push -u origin feat/eval-framework
gh pr create --title "Evaluation framework for vector search" --body "$(cat <<'EOF'
## Summary
- Extracts search into reusable `scripts/lib/search.ts`
- Adds `scripts/eval.ts` with three evaluation suites
- Suite A: structural matching quality (expected slugs in top-5)
- Suite B: m4x vs raw Claude comparison (side-by-side responses)
- Suite C: catalog coverage gaps (20 structural probes)

## How to run
```bash
source .envrc
bun run scripts/eval.ts --suite all    # full run (~3 min)
bun run scripts/eval.ts --suite a      # just structural tests (~30 sec)
bun run scripts/eval.ts --suite b      # just LLM comparison (~2 min)
bun run scripts/eval.ts --suite c      # just coverage analysis (~30 sec)
```

Reports written to `docs/evals/YYYY-MM-DD-eval-report.md` (gitignored).

## Test plan
- [ ] Suite A runs without errors, PASS/FAIL results are reasonable
- [ ] Suite B produces side-by-side LLM responses, m4x responses cite catalog entries
- [ ] Suite C identifies real coverage gaps
- [ ] `scripts/search.ts` CLI still works identically after refactor
- [ ] `uv run scripts/validate.py validate` still passes

🤖 Generated with [Claude Code](https://claude.com/claude-code)
EOF
)"
```

**Verify:** PR is created. All commands in the test plan checklist can be run successfully.
