// scripts/search.ts
// Usage: bun run scripts/search.ts [--section transfer|limit|expression|title] [--kind metaphor|pattern|archetype|paradigm|mental-model] [--json] <query>

import { search } from "./lib/search.ts";

const args = process.argv.slice(2);
let sectionFilter: string | undefined;
let kindFilter: string | undefined;
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

console.log(`Query: "${query}"\n`);

const results = await search(query, {
  k: 10,
  section: sectionFilter,
  kind: kindFilter,
});

if (jsonOutput) {
  const output = results.map((r) => ({
    slug: r.slug,
    kind: r.kind,
    section: r.section,
    matchedText: r.matchedText,
    score: parseFloat(r.score.toFixed(4)),
  }));
  console.log(JSON.stringify(output, null, 2));
} else {
  for (const r of results) {
    const score = r.score.toFixed(2);
    const slug = r.slug.padEnd(30);
    const section = `[${r.section}]`.padEnd(14);
    const text = r.matchedText.length > 60 ? r.matchedText.slice(0, 57) + "..." : r.matchedText;
    console.log(`${slug} ${section} ${score}  "${text}"`);
  }
}
