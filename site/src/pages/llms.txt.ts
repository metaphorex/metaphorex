import { getCollection } from "astro:content";

export async function GET() {
  const entries = await getCollection("entries");
  const frames = await getCollection("frames");
  const categories = await getCollection("categories");

  const sortedEntries = entries.sort((a, b) =>
    a.data.name.localeCompare(b.data.name)
  );
  const sortedFrames = frames.sort((a, b) =>
    a.data.name.localeCompare(b.data.name)
  );
  const sortedCategories = categories.sort((a, b) =>
    a.data.name.localeCompare(b.data.name)
  );

  const version = new Date().toISOString().split("T")[0].replace(/-/g, ".");

  const lines = [
    "# Metaphorex",
    "",
    `> A knowledge graph of metaphors. Version ${version}. ${entries.length} entries, ${frames.length} frames, ${categories.length} categories.`,
    "",
    "Metaphorex catalogs metaphors, mental models, patterns, archetypes, and paradigms. Each entry documents what the mapping transfers and where it breaks down.",
    "",
    `## Entries (${entries.length})`,
    "",
    ...sortedEntries.map((m) => {
      const parts = [`- [${m.data.name}](https://metaphorex.org/entries/${m.data.slug}/)`];
      const meta: string[] = [];
      if (m.data.source_frame) meta.push(`source: ${m.data.source_frame}`);
      if (m.data.applies_to?.length) meta.push(`applies to: ${m.data.applies_to.join(", ")}`);
      meta.push(m.data.kind);
      parts.push(`: ${meta.join(", ")}`);
      return parts.join("");
    }),
    "",
    `## Frames (${frames.length})`,
    "",
    ...sortedFrames.map(
      (f) =>
        `- [${f.data.name}](https://metaphorex.org/frames/${f.data.slug}/): roles: ${f.data.roles.join(", ")}`
    ),
    "",
    `## Categories (${categories.length})`,
    "",
    ...sortedCategories.map(
      (c) =>
        `- [${c.data.name}](https://metaphorex.org/categories/${c.data.slug}/)`
    ),
  ];

  return new Response(lines.join("\n"), {
    headers: { "Content-Type": "text/plain; charset=utf-8" },
  });
}
