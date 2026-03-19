---
project_issue: 1232
repo: metaphorex/metaphorex
source_type: book
status: draft
---

# Playbook: Hauser & Reich's Notes on Directing -- Theatrical Wisdom

## Source Description

This project extracts cross-domain metaphors and mental models from the
theatrical directing tradition, anchored in Frank Hauser & Russell Reich's
*Notes on Directing: 130 Lessons in Leadership from the Director's Chair*
(2003), with supplementary concepts from:

- Keith Johnstone, *Impro: Improvisation and the Theatre* (1979)
- Anne Bogart, *A Director Prepares* (2001) / *The Viewpoints Book* (2005)
- Walter Murch, *In the Blink of an Eye* (1995, rev. 2001)
- Konstantin Stanislavski, *An Actor Prepares* (1936)

The primary source contains 130 numbered lessons organized into ten
chapters: Understanding the Script, The Director's Role, Casting, First
Read-Through, Rehearsal Rules, Building Blocks, Talking to Actors, Getting
a Laugh, Elements of Staging, and Last Tips, plus an Epilogue and five
appendices.

**Estimated yield: 15 entries.**

### What Makes This Source Distinctive

Directing encodes a specific form of leadership reasoning:

1. **Indirect causation.** Directors cannot act; they can only create
   conditions for actors to discover behavior. This is structurally
   identical to the management challenge of leading creative knowledge
   workers.
2. **Ensemble dynamics.** A director manages a group of creative
   individuals who must coordinate without explicit instruction during
   performance. The ensemble is a pre-digital model for self-organizing
   teams.
3. **Scene-as-negotiation.** Hauser's principle that "every scene is a
   chase scene" reframes all human interaction as want-driven negotiation,
   a lens that transfers to sales, management, conflict resolution.
4. **Feedback without prescription.** The directing tradition has developed
   sophisticated techniques for giving feedback that preserves the
   recipient's creative agency -- techniques that management science is
   still rediscovering.

## Access Method

### No Structured Digital Archive Exists

The primary source (*Notes on Directing*) is a copyrighted book. No
complete table of contents listing all 130 individual lesson titles is
available online. The book is available on Internet Archive for borrowing:

- https://archive.org/details/notesondirecting0000haus

However, the 130 lessons are short aphoristic entries without formal
titles -- they are numbered, not named. The book's structure is by chapter
(10 chapters), not by individually titled lessons.

### Partial Content Available From

- **Goodreads quotes page:** https://www.goodreads.com/book/show/254808.Notes_on_Directing
  -- Several key quotes surfaced by readers
- **Amazon Look Inside / reviews:** Partial chapter listings and selected quotes
- **LeadershipNow:** https://www.leadershipnow.com/leadershop/9780802717085.html
  -- Chapter structure confirmed

### Supplementary Sources With Structured Content

- **Johnstone's Impro:** Summary at https://jamesclear.com/book-summaries/impro
  and https://fluidself.org/books/art/impro/ -- Key concepts (status
  transactions, offers and blocks, spontaneity) well documented online
- **Murch's Rule of Six:** https://www.studiobinder.com/blog/walter-murch-rule-of-six/
  -- Structured description of the editing priority framework
- **Stanislavski's system:** https://en.wikipedia.org/wiki/Stanislavski's_system
  -- Well-documented concepts (given circumstances, magic if, objectives)

### Consequence for Source Tagging

Because no structured archive provides a complete enumeration of the 130
lessons, ALL candidates sourced from Hauser & Reich are tagged `"llm"` in
the manifest. Candidates from Johnstone and Murch that are verified against
the online summaries above are also tagged `"llm"` because the summaries
are secondary sources, not authoritative archives. The Surveyor should
verify these against the actual books.

## Extraction Strategy

### Selection Criteria

The issue specifies selectivity: import only lessons encoding reasoning
about leadership, creativity, or collaboration that transfers beyond
theater. An aphorism qualifies ONLY if:

1. **Cross-domain transfer.** The concept must encode a reasoning pattern
   usable outside theater/film. "Don't keep actors hanging about needlessly"
   is good stage management but does not encode a novel reasoning pattern.
   "Every scene is a chase scene" reframes all interaction as negotiation.

2. **Structural mapping.** The theatrical concept must map onto a target
   domain with specific structural correspondences, not just vague analogy.
   "A director is like a leader" is too thin. "Give actions, not emotions"
   maps directing technique onto feedback methodology with specific
   structural parallels.

3. **Distinctiveness.** The concept must not duplicate existing catalog
   entries. Generic leadership wisdom ("be prepared," "listen well") is
   excluded unless the theatrical framing adds something the generic form
   lacks.

### For Miners

Each candidate in the manifest has:
- `slug`: the filename for `catalog/entries/{slug}.md`
- `name`: human-readable name
- `kind`: `cross-field-mapping`, `conceptual-metaphor`, or `mental-model`
- `source_frame`: the theatrical/directing domain
- `target_frame`: the domain where the concept transfers
- `categories`: primary categorization
- `source`: `"llm"` (all candidates -- see Access Method)
- `description`: what makes this interesting as a cross-domain mapping

**Miner workflow:**

1. Research the theatrical origin: what directing problem does this concept
   solve? How does it work in practice on stage?
2. Document the cross-domain transfer: how does this theatrical concept
   illuminate leadership, management, creative work, or organizational
   design? What structural parallels make the transfer work?
3. **Limits are critical.** Theatrical contexts differ from organizational
   ones in key ways: directors have more authority than most managers, the
   "performance" has a defined end (opening night), actors are trained
   collaborators. The Miner must interrogate where the theatrical framing
   breaks down.
4. Set `provenance: hauser-reich-directing`
5. Set `related:` links to other entries from this project and to existing
   catalog entries where relevant
6. The `author` field should be `agent:metaphorex-miner`

### Batching Recommendation

Process in thematic clusters:

- **Batch 1 -- Feedback and communication (4):** give-actions-not-emotions,
  talk-to-the-character-not-the-actor, every-scene-is-a-chase-scene,
  every-object-tells
- **Batch 2 -- Leadership and control (4):** you-cannot-create-results,
  the-directors-duty-is-to-the-author, casting-is-ninety-percent,
  rehearsal-is-not-performance
- **Batch 3 -- Ensemble and improvisation (4):** status-transactions,
  offers-and-blocks, the-ensemble, yes-and
- **Batch 4 -- Creative process (3):** the-magic-if, the-rule-of-six,
  just-tell-the-story

## Schema Mapping

### Kind Assignment

| Pattern | Kind | Criteria |
|---------|------|----------|
| Theatrical concept mapping to organizational/creative domain | `cross-field-mapping` | Directing technique that illuminates management, leadership, or collaboration |
| Status/negotiation as universal frame | `conceptual-metaphor` | Theatrical lens that reframes how we understand all interaction |
| Decision framework from theater/film | `mental-model` | Prioritization or evaluation heuristic |

Most entries will be `cross-field-mapping` because they transfer specific
theatrical techniques to organizational contexts. A few (status
transactions, every-scene-is-a-chase) are `conceptual-metaphor` because
they provide a universal reframing lens.

### Frame Inventory

**Existing reusable frames:**
- `creative-process` -- target for directing methodology entries
- `collaborative-work` -- target for ensemble/improv entries
- `authority-and-delegation` -- target for director-as-leader entries
- `communication` -- target for feedback entries
- `decision-making` -- target for prioritization entries

**New frames needed:**
- `theatrical-directing` -- source frame for Hauser & Reich concepts
- `improvisation` -- source frame for Johnstone concepts
- `film-editing` -- source frame for Murch concepts
- `feedback-and-coaching` -- target frame for directing communication entries

### Categories

Primary category for most entries: `arts-and-culture`.

Additional categories by cluster:
- Feedback/communication: `organizational-behavior`
- Leadership/control: `organizational-behavior`
- Ensemble/improv: `social-dynamics`, `psychology`
- Creative process: `cognitive-science`

## Gotchas

1. **Copyright on all primary sources.** Hauser & Reich, Johnstone, Bogart,
   Murch, and Stanislavski (translations) are all under copyright. Miners
   should not reproduce verbatim passages. The concepts and aphorisms
   themselves are ideas (not copyrightable), but the specific prose is.

2. **All candidates are LLM-sourced.** No structured digital archive
   provides a complete enumeration of the source material. The candidate
   list is assembled from online quotes, reviews, book summaries, and
   the prospector's knowledge of the texts. The Surveyor should verify
   completeness against the actual books.

3. **"Yes, and" is ubiquitous.** The improv principle has been so
   widely adopted in business training that it risks being a cliche.
   The Miner should address this directly -- what does the original
   theatrical meaning add that corporate improv workshops have lost?

4. **Hauser's lessons are unnumbered aphorisms, not titled concepts.**
   The 130 "lessons" are short paragraphs within chapters, not formally
   named concepts. The slugs and names in the manifest are our
   constructions, not Hauser's titles. Miners should make this clear
   in the entries.

5. **Multiple sources overlap.** "Status transactions" comes from
   Johnstone, not Hauser, but relates to Hauser's "every scene is a
   chase scene." The provenance field should credit the specific source
   author, not the project generically. Use `provenance: hauser-reich-directing`
   for all entries (as the project provenance), but note the specific
   author in the Origin Story section.

6. **Candidate count is under 100.** No sub-issue cap concerns for
   this project.

7. **The "directing as leadership" analogy has limits.** Directors
   work with trained performers in a structured creative process with
   a defined endpoint (opening night). Most organizational leadership
   lacks all three of these conditions. Every entry should address this
   structural disanalogy in the Limits section.
