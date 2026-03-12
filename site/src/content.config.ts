import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

const mappings = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "src/content/mappings" }),
  schema: z.object({
    slug: z.string(),
    name: z.string(),
    kind: z.enum([
      "conceptual-metaphor",
      "design-pattern",
      "archetype",
      "paradigm",
      "cross-field-mapping",
      "dead-metaphor",
    ]),
    source_frame: z.string(),
    target_frame: z.string(),
    categories: z.array(z.string()),
    author: z.string(),
    contributors: z.array(z.string()).default([]),
    related: z.array(z.string()).default([]),
    deprecated: z.boolean().optional(),
    harness: z.string().optional(),
  }),
});

const frames = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "src/content/frames" }),
  schema: z.object({
    slug: z.string(),
    name: z.string(),
    broader: z.string().optional(),
    related: z.array(z.string()).default([]),
    roles: z.array(z.string()),
  }),
});

const categories = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "src/content/categories" }),
  schema: z.object({
    slug: z.string(),
    name: z.string(),
    broader: z.string().optional(),
    related: z.array(z.string()).default([]),
  }),
});

export const collections = { mappings, frames, categories };
