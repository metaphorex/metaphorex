import { getCollection } from "astro:content";

export async function GET() {
  const mappings = await getCollection("mappings");
  const frames = await getCollection("frames");
  const categories = await getCollection("categories");

  const sortedMappings = mappings.sort((a, b) =>
    a.data.name.localeCompare(b.data.name)
  );

  const version = new Date().toISOString().split("T")[0].replace(/-/g, ".");

  const sections: string[] = [
    "# Metaphorex (Full)",
    "",
    `> Version ${version}. ${mappings.length} mappings, ${frames.length} frames, ${categories.length} categories.`,
    "",
  ];

  for (const m of sortedMappings) {
    sections.push(`## ${m.data.name}`);
    sections.push("");
    const meta: string[] = [`**Kind:** ${m.data.kind}`];
    if (m.data.source_frame) meta.push(`**Source:** ${m.data.source_frame}`);
    if (m.data.applies_to?.length) meta.push(`**Applies to:** ${m.data.applies_to.join(", ")}`);
    meta.push(`**Categories:** ${m.data.categories.join(", ")}`);
    if (m.data.grounding) meta.push(`**Grounding:** ${m.data.grounding}`);
    sections.push(meta.join(" | "));
    sections.push("");
    sections.push(m.body || "");
    sections.push("");
    sections.push("---");
    sections.push("");
  }

  return new Response(sections.join("\n"), {
    headers: { "Content-Type": "text/plain; charset=utf-8" },
  });
}
