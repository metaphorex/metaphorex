# Contributing to Metaphorex

Metaphorex is a collaboratively built knowledge graph of metaphors, mental
models, and conceptual mappings. Contributions from both humans and agents are
welcome.

## License Agreement

By submitting content to this repository, you agree that your contributions
are licensed under the **Creative Commons Attribution-ShareAlike 4.0
International License** ([CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)),
with **Metaphorex** as the collective licensor.

You certify that:

1. You have the right to submit the content under this license.
2. The content is your original work, or you have sufficient rights to
   contribute it under CC BY-SA 4.0.
3. If the content derives from other sources, those sources are compatible
   with CC BY-SA 4.0 and are properly attributed in the entry's frontmatter.

This is the content equivalent of a
[Developer Certificate of Origin](https://developercertificate.org/).

## Attribution

### How credit works

- **License requirement**: Downstream users of Metaphorex content must credit
  "Metaphorex" with a link to this repository. That's the formal obligation.
- **Per-entry attribution**: Each entry tracks its author and contributors in
  frontmatter. This is encouraged as a norm and surfaced in the API, but is
  not a separate license obligation for downstream consumers.
- **Git history**: The immutable record. All contributions are tracked in git
  regardless of frontmatter.

### Entry frontmatter

Every entry should include:

```yaml
author: your-github-username
contributors: []
```

- `author` — whoever created the entry. Use `agent:<agent-name>` for agent
  submissions.
- `contributors` — people or agents who made substantial edits. Add yourself
  here when you meaningfully revise someone else's entry.

Minor fixes (typos, formatting) don't require adding yourself as a
contributor — git blame has you covered.

## What to contribute

Metaphorex catalogs metaphors from all domains — not just software. Good
entries include:

- **Conceptual metaphors** (e.g., "argument is war", "time is money")
- **Design patterns** that function as metaphors across fields
- **Cross-field mappings** where a concept from one domain illuminates another
- **Dead metaphors** worth resurrecting or examining
- **Archetypes and paradigms** that shape how we think

## Contribution workflow

1. **Check for duplicates** — search existing entries before creating a new one.
2. **Create your entry** as a markdown file with the required frontmatter.
3. **Run validation** — `pnpm validate` (once available) checks frontmatter
   schema, inter-entry links, and other structural requirements.
4. **Open a pull request** — describe what the metaphor is and why it belongs
   in the catalog.
5. **Review** — entries go through editorial review before merging.

## For agents

Agent contributors follow the same workflow via pull requests. Additional
guidelines:

- Use your registered agent identity in the `author` field.
- Start with a single entry and wait for feedback before submitting batches.
- Include provenance in the entry's `references` field — where did you
  encounter this metaphor?
- Do not fabricate attributions or references.

## Code of conduct

Be thoughtful. This is a knowledge commons. Contribute what you'd want to
find.
