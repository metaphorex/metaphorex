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
    created: z.coerce.date(),
    updated: z.coerce.date(),
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
    created: z.coerce.date(),
    updated: z.coerce.date(),
  }),
});

const categories = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "src/content/categories" }),
  schema: z.object({
    slug: z.string(),
    name: z.string(),
    broader: z.string().optional(),
    related: z.array(z.string()).default([]),
    created: z.coerce.date(),
    updated: z.coerce.date(),
  }),
});

const changelog = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "../docs/changelog" }),
  schema: z.object({
    date: z.coerce.date(),
    type: z.literal("changelog"),
    week: z.string(),
  }),
});

const ops = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "../docs/ops" }),
  schema: z.object({
    date: z.coerce.date(),
    type: z.literal("ops"),
  }),
});

export const collections = { mappings, frames, categories, changelog, ops };
