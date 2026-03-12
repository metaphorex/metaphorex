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
    sections.push(
      `**Kind:** ${m.data.kind} | **Source:** ${m.data.source_frame} | **Target:** ${m.data.target_frame} | **Categories:** ${m.data.categories.join(", ")}`
    );
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
