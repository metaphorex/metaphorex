import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

const entries = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "src/content/entries" }),
  schema: z.object({
    slug: z.string(),
    name: z.string(),
    kind: z.enum([
      "metaphor",
      "pattern",
      "archetype",
      "paradigm",
      "mental-model",
    ]),
    source_frame: z.string().optional(),
    applies_to: z.array(z.string()).optional(),
    categories: z.array(z.string()),
    author: z.string(),
    contributors: z.array(z.string()).default([]),
    related: z.array(z.string()).default([]),
    transfers: z.array(z.string()).optional(),
    limits: z.array(z.string()).optional(),
    grounding: z.enum(["proven", "established", "folk", "contested"]).optional(),
    dead: z.boolean().optional(),
    deprecated: z.boolean().optional(),
    harness: z.string().optional(),
    provenance: z.string().optional(),
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

const works = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "src/content/works" }),
  schema: z.object({
    slug: z.string(),
    name: z.string(),
    type: z.enum(["book", "paper", "collection", "repository", "talk", "post"]),
    authors: z.array(z.string()),
    year: z.number(),
    url: z.string().default(""),
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

export const collections = { entries, frames, categories, works, changelog, ops };
