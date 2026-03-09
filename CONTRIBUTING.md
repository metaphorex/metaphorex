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

### Authorship principle

**Authorship follows the editorial decision, not the keystrokes.**

Most catalog entries are drafted with AI assistance. That doesn't change who
the author is. The author is the person (or agent) who made the curatorial
and editorial decisions:

- **Which** metaphor belongs in the catalog
- **How** it should be framed — what it illuminates, what it hides
- **Where** it connects to other entries

Writing prose is labor; choosing what to write about and how to frame it is
authorship. An LLM drafting text from a prompt is a tool, like a word
processor or a research assistant. The `harness` field in frontmatter
records which tool was used — that's where generation transparency lives.

### Entry frontmatter

Every entry should include:

```yaml
author: your-github-username
contributors: []
```

- `author` — the person or agent who initiated the entry and directed its
  framing. For human-steered entries (including those drafted by an LLM from
  a human prompt or import issue), this is the human. For fully
  agent-directed entries, use `agent:<agent-name>` or the identity of whoever
  filed the import issue.
- `contributors` — people or agents who made substantial edits after
  creation. Add yourself here when you meaningfully revise someone else's
  entry.
- `harness` — the tool used to generate the entry (e.g., `Claude Code`).
  This field provides transparency about the drafting process without
  confusing tooling with authorship.

Minor fixes (typos, formatting) don't require adding yourself as a
contributor — git blame has you covered.

### Examples

| Scenario | `author` | `harness` |
|---|---|---|
| Human writes entry by hand | `github-username` | _(omit)_ |
| Human prompts LLM to draft entry | `github-username` | `Claude Code` |
| Human files import issue, agent writes entry | `github-username` | `Claude Code` |
| Agent autonomously identifies and imports a metaphor | `agent:agent-name` | `Claude Code` |

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

## Writing style

### Voice

The house style is Strunk & White: omit needless words, use the active
voice, prefer the specific to the general, put statements in positive form.
If you have access to an explicit writing-quality skill or tool (e.g. a
Strunk-and-White editing pass), use it on every entry before submitting. If
you don't, apply these principles directly. Either way, the standard is the
same: tight, clean, assertive prose. State claims, then support them. No
hedging, no throat-clearing, no filler.

### Em-dash policy

Em-dashes (`—`) are permitted only as **structural delimiters** in list items
(see below). Do not use em-dashes in running prose to join clauses. Use a
period, comma, colon, or parentheses instead.

Bad: `The metaphor breaks down — and it breaks down often — when applied
to distributed systems.`

Good: `The metaphor breaks down when applied to distributed systems, and
it breaks down often.`

### Structured list format

Mapping entries use three recurring list sections. Each follows the same
**header — explanation** pattern to keep entries parseable as semi-structured
data.

**What It Brings** (key structural parallels):
```
- **Bold label** — explanation of the structural parallel
```

**Where It Breaks** (failure modes):
```
- **Bold label** — explanation of how or why the metaphor fails here
```

**Expressions** (common phrases):
```
- "Quoted expression" — gloss explaining the metaphorical origin
```

The bold or quoted text before the ` — ` is the extractable key. Keep it
short (2-6 words). The explanation after the delimiter is a sentence or
sentence fragment; it should not itself contain em-dashes.

### AI-slop indicators to avoid

- Gratuitous em-dashes in prose (see above)
- "It's worth noting that..." / "Interestingly..." / "Importantly..."
- Bullet lists where a paragraph would do
- Rhetorical questions used as transitions
- "Let's unpack this" / "Let's dive in"
- Needless hedging: "arguably," "perhaps," "it could be said"
- Emojis, unless the emoji is itself the subject of the mapping discussion

Write like you mean it.

## Code of conduct

Be thoughtful. This is a knowledge commons. Contribute what you'd want to
find.
