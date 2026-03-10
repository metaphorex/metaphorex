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

Metaphorex catalogs metaphors from all domains, not just software. Every
entry is one of four kinds, organized as a 2x2 grid (specific vs generative,
source active vs dormant):

- **Conceptual metaphors** — specific A→B mappings where the source domain is
  still active (e.g., "argument is war", "data flow is fluid flow")
- **Archetypes** — generative patterns appearing across many mappings
  (e.g., The Commons, The Trickster)
- **Dead metaphors** — mappings where the source domain is forgotten; the
  value is reactivating it (e.g., bottleneck, firewall)
- **Paradigms** — foundational frames that shape how entire fields think
  (e.g., survival of the fittest, the map is not the territory)

## Contribution workflow

1. **Check for duplicates** — search existing entries before creating a new one.
2. **Create your entry** as a markdown file with the required frontmatter.
3. **Run validation** — `uvx --with python-frontmatter --with pyyaml python
   scripts/validate.py validate` checks frontmatter schema, inter-entry
   links, and other structural requirements.
4. **Open a pull request** — describe what the metaphor is and why it belongs
   in the catalog.
5. **Review** — entries go through editorial review before merging.

## Editorial guide for mapping entries

This section encodes the editorial standards that all mapping entries must
meet. It applies equally to human and agent contributors.

### What each section does

A mapping entry has five sections. Each serves a distinct analytical purpose:

**What It Brings** — the structural parallels between source and target.
Not "this is interesting" but "here is how the source domain's structure
maps onto the target domain, and what that mapping makes visible." Lead
with the core structural insight, then enumerate specific parallels as
labeled list items. Each parallel should name what the source contributes
that the target domain lacks on its own.

**Where It Breaks** — the failure modes of the mapping. Where does the
metaphor mislead, obscure, or import false assumptions? This section earns
its keep. Every metaphor has blind spots; a catalog entry that doesn't name
them is marketing, not analysis. Be specific: name the structural mismatch,
explain what it hides, give an example of the real-world consequence.

**Expressions** — phrases in common use that instantiate this metaphor.
These should be things people actually say, not invented examples. Each
expression gets a gloss explaining its metaphorical origin. Prefer
expressions where the metaphorical origin is non-obvious or illuminating;
skip expressions that are self-explanatory.

**Origin Story** — the historical path from source domain to metaphorical
usage. When did people start using this metaphor? Who formalized it? How
has it evolved? Ground this in specific dates, people, and texts. When a
metaphor has competing intellectual traditions (like Hardin vs Ostrom for
the commons), present both and make clear which has better empirical support.

**References** — real, verifiable sources. Prefer primary sources. Include
the foundational text, the most important critique or extension, and any
source that directly influenced the entry's framing. Do not fabricate
citations. If you aren't certain a source exists, omit it.

### Quality bar

Before submitting a mapping entry, verify:

- [ ] **"What It Brings" names structural parallels, not vibes.** Each
  bullet should identify a specific structural feature of the source domain
  and explain how it maps onto the target. "This metaphor is illuminating"
  is not a structural parallel. "The source domain's X maps onto the
  target's Y, which makes Z visible" is.
- [ ] **"Where It Breaks" is substantive and specific.** At least two
  distinct failure modes. Each should name a structural mismatch between
  source and target, not just say "it's imperfect." The best "Where It
  Breaks" bullets reveal something about how the metaphor does invisible
  cognitive work.
- [ ] **Expressions are real.** Things people actually say in professional
  or everyday use, not invented examples. If you can't find the expression
  in the wild, don't include it.
- [ ] **References are verifiable.** Real authors, real titles, real dates.
  No hallucinated citations.
- [ ] **Related links are structurally meaningful.** Two entries are related
  when understanding one genuinely illuminates the other. Superficial
  similarity (both involve "narrowing" or both are "about software") is not
  enough. If you can't articulate why the link helps a reader, don't add it.
- [ ] **Categories are accurate.** An entry belongs in a category when the
  category's domain is either the source or target of the mapping, or when
  the mapping is primarily studied within that field.
- [ ] **The entry passes validation.** Run the validator before submitting.

### When to reference vs create a new entry

If a concept is closely related to an existing entry but structurally
distinct, mention it in the existing entry's prose and add a reference.
Create a new entry only when the concept has its own source frame, target
frame, and distinct set of structural parallels. Example: Spolsky's "leaky
abstractions" is mentioned in the facade-pattern entry because it names the
theoretical limit of facades, but it warrants its own entry because it has a
distinct source domain (material degradation/porosity) and maps onto a
broader target than just the Facade pattern.

### Common mistakes

- **Listing features instead of structure.** "What It Brings" should explain
  the mapping's structural logic, not just list interesting facts about the
  source domain.
- **Shallow "Where It Breaks."** "No metaphor is perfect" is not analysis.
  Name the specific structural mismatch and its consequences.
- **Orphan references.** Don't include a reference that isn't connected to
  something in the entry's prose. If you cite it, the entry should show why.
- **Circular roles.** Don't use a term in a frame's role list when that term
  is itself a metaphor from another frame. "Bottleneck" is a metaphor from
  the containers frame; the systems-performance frame should use
  "constraint" instead.
- **Spurious related links.** Bottleneck and firewall were both "about
  narrowing" but had no structural relationship. The link was removed.
  Related means "reading this entry teaches you something about that entry."

## For agents

Agent contributors follow the same workflow via pull requests. Additional
guidelines:

- Use your registered agent identity in the `author` field.
- Start with a single entry and wait for feedback before submitting batches.
- Include provenance in the entry's `references` field. Where did you
  encounter this metaphor?
- Do not fabricate attributions or references. If you are uncertain whether
  a source exists, omit it entirely. A missing reference is better than a
  hallucinated one.
- Run a Strunk-and-White editing pass (or equivalent writing-quality skill)
  on every entry before submitting. Tighten prose, cut filler, kill hedges.
- After writing, re-read the "Quality bar" checklist above and verify each
  item. This is not optional.
- Study `data-flow-is-fluid-flow.md` as the primary style exemplar before
  writing your first entry. It demonstrates the standard format (labeled
  lists in both "What It Brings" and "Where It Breaks"), the right level
  of structural analysis, well-glossed expressions, and a grounded origin
  story. Some entries (like `the-commons.md`) use prose paragraphs instead
  of labeled lists when the analysis doesn't decompose into parallel items;
  this is acceptable, but labeled lists are the default.

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

### Frame roles

Every frame has a `roles` list in its frontmatter. Roles are the structural
slots that make the frame a frame: the participants, instruments, settings,
and outcomes that must exist for the domain to function.

**The test:** "In this frame, there is a ___." If the word fills that blank
as a noun, it's a role. If it describes something that *happens* (a process)
or a quality something *has* (a property), it belongs in the frame's prose
description, not the role list.

Good roles: gardener, seed, harvest, pest (all nouns that fill structural slots)
Not roles: pruning (process), sustainability (property), cooperation (dynamic)

Guidelines:
- Prefer concrete nouns over abstract processes
- Prefer the general over the specific (livestock, not sheep)
- Include the frame's agent if it has one (gardener, builder, mapmaker)
- Aim for 5-9 roles per frame: enough for rich mappings, few enough to audit
- Don't import roles from other frames (bottleneck belongs in containers, not
  in systems-performance where it's already a metaphor)
- Roles should be useful for mapping: when someone creates a mapping FROM or
  TO this frame, these are the things they'll map between

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
