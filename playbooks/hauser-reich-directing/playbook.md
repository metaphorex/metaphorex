---
project_issue: 1232
repo: metaphorex/metaphorex
source_type: book
status: draft
---

# Playbook: Hauser & Reich's Notes on Directing

## Source Description

**Frank Hauser & Russell Reich, *Notes on Directing: 130 Lessons in
Leadership from the Director's Chair*** (2003, self-published; 2008,
RCR Creative Press; 2011, Walker & Company). 130 numbered aphorisms
with commentary covering script interpretation, the director's role,
casting, rehearsal, actor communication, staging, and comedy technique.

Supplementary sources from the original issue:
- **Keith Johnstone, *Impro: Improvisation and the Theatre*** (1979) --
  status transactions, offers/blocks, spontaneity
- **Anne Bogart, *A Director Prepares*** (2001) / **Bogart & Landau,
  *The Viewpoints Book*** (2005) -- nine physical + five vocal Viewpoints
- **Walter Murch, *In the Blink of an Eye*** (1995/2001) -- Rule of Six
  editing criteria
- **Konstantin Stanislavski, *An Actor Prepares*** (1936) -- the Magic If,
  given circumstances, emotion memory

The issue's selectivity guidance: import only lessons encoding reasoning
about leadership, creativity, or collaboration that transfers beyond
theater. Purely technical staging notes do not qualify.

## Access Method

### Primary Source: No Open Archive

The primary text (*Notes on Directing*) is a copyrighted book. There is
**no freely accessible structured digital archive** of the 130 lessons:

- **Archive.org**: Two copies exist but are borrow-only (1-hour checkout):
  - https://archive.org/details/notesondirecting0000haus
  - https://archive.org/details/notesondirecting00haus
- **Google Books**: Preview only, no full text:
  - https://books.google.com/books/about/Notes_on_Directing.html?id=SsvnQQAACAAJ
- **Bookey.app**: Chapter summary exists but returned 403 on fetch:
  - https://www.bookey.app/book/notes-on-directing

**Publicly accessible fragments** (used for archive-sourced candidates):
- Goodreads quotes page (3 quotes visible): https://www.goodreads.com/work/quotes/246935-notes-on-directing
- LeadershipNow product page (chapter headings + casting insight): https://www.leadershipnow.com/leadershop/9780802717085.html

### Supplementary Sources: Structured Web Summaries

These sources have extensive, freely-accessible structured summaries
online that the scraping script targets:

| Source | Archive URL | What it provides |
|--------|-------------|-----------------|
| Johnstone *Impro* | https://fluidself.org/books/art/impro | Status, offers/blocks, spontaneity concepts |
| Johnstone *Impro* | https://jamesclear.com/book-summaries/impro | Core principles summary |
| Johnstone *Impro* | https://taylorpearson.me/bookreview/impro-johnstone-notes/ | Teaching methodology, mask work |
| Johnstone *Impro* | https://blas.com/impro/ | Detailed concept breakdown |
| Bogart Viewpoints | https://dramatics.org/understanding-viewpoints/ | 9 physical + 5 vocal viewpoint definitions |
| Murch Rule of Six | https://nofilmschool.com/2016/11/6-rules-good-cutting-according-oscar-winning-editor-walter-murch | Six criteria with percentages |
| Murch Rule of Six | https://www.studiobinder.com/blog/walter-murch-rule-of-six/ | Detailed analysis |
| Stanislavski system | https://www.backstage.com/magazine/article/the-definitive-guide-to-the-stanislavsky-acting-technique-65716/ | Magic If, given circumstances, emotion memory |

### Scraping Script

`playbooks/hauser-reich-directing/scripts/scrape_sources.py` fetches from
Goodreads quotes, fluidself.org Impro summary, and Dramatics.org Viewpoints.
Run with: `uv run playbooks/hauser-reich-directing/scripts/scrape_sources.py`

The script produces JSON to stdout. It is idempotent and produces
consistent output across runs (modulo page content changes).

## Extraction Strategy

### Candidate Selection Criteria

From the 130 Hauser/Reich lessons, select only those that:
1. Encode a **structural mapping** from theater to another domain
   (leadership, feedback, hiring, system design, learning)
2. Have a **named or nameable** aphorism (not just general advice)
3. Are **not purely technical** stage-directing instructions

From supplementary sources, select concepts that:
1. Have become **cross-domain vocabulary** (status transactions,
   offers/blocks, the Magic If)
2. Encode a **transferable reasoning pattern** (Rule of Six priority
   hierarchy, ensemble dynamics)

### Source Attribution

Each candidate is marked with its source provenance:
- `"archive"` -- verifiable from a publicly accessible web page (URL cited)
- `"llm"` -- from LLM knowledge of the book, not independently verifiable
  from a free online source

**7 of 15 candidates are archive-sourced; 8 are LLM-sourced.**

The LLM-sourced candidates come from the copyrighted primary text. They are
well-known directing aphorisms widely cited in theater education, but no
free structured archive enumerates them. The Surveyor should verify these
against the book if a copy is available.

### Deduplication

- `yes-and` was removed: already claimed by comedy-writers-glossary project
  (issue #1885)
- `status-is-up` exists in the catalog (provenance: lakoff-johnson-mwlb) as
  the cognitive-linguistics metaphor. Our `status-transactions` is the
  Johnstone improvisation concept -- distinct entry, different source frame
  (economics vs spatial-orientation), different emphasis (social technique
  vs linguistic metaphor).

## Schema Mapping

| Manifest field | Entry frontmatter | Notes |
|---------------|-------------------|-------|
| `slug` | `slug` | kebab-case, matches filename |
| `name` | `name` | Human-readable title |
| `kind` | `kind` | `metaphor` or `mental-model` only |
| `source_frame` | `source_frame` | Required for metaphor kind |
| `target_frame` | `applies_to[0]` | Maps to applies_to array |
| `categories` | `categories` | Array of category slugs |
| -- | `provenance` | Set to `hauser-reich-directing` |
| -- | `author` | Set to `agent:metaphorex-miner` |
| -- | `grounding` | Default `folk` for most; `established` for Stanislavski/Murch |

### Kind Assignment Rationale

All candidates use either `metaphor` or `mental-model`:
- **metaphor**: Candidates with a clear source-target structural mapping
  (director-as-obstetrician, every-scene-is-a-chase, status-transactions,
  offers-and-blocks, rehearsal-is-not-performance)
- **mental-model**: Candidates that are decision heuristics or reasoning
  frameworks without a strict metaphorical source domain (give-actions-not-
  emotions, casting-is-ninety-percent, rule-of-six, just-tell-the-story)

The rejected `cross-field-mapping` kind does not exist in the schema.
Valid kinds are: `metaphor`, `pattern`, `archetype`, `paradigm`, `mental-model`.

### Frames Needed

New frames to create alongside entries:
- `theatrical-directing` -- director's craft, staging, rehearsal process
- `improvisation` -- improv theater technique, spontaneity, scene work
- `film-editing` -- cutting, montage, editorial decision-making
- `feedback-and-communication` -- giving feedback, communication patterns
- `pursuit-and-escape` -- chase, pursuit, evasion dynamics

Existing frames that apply:
- `economics` (for status-transactions source frame)
- `leadership-and-management`, `collaboration`, `decision-making`,
  `social-dynamics`, `learning-and-development` (various target frames)

## Gotchas

1. **No archive for primary source.** The 8 LLM-sourced candidates cannot
   be independently verified from free web resources. The Surveyor should
   verify against a physical or borrowed copy of the book.

2. **Candidate count is below the 130-lesson total.** The issue's
   selectivity guidance explicitly calls for filtering to ~10-18 lessons
   with cross-domain transfer. We have 15 candidates, within that range.
   This is NOT an exhaustive enumeration of the 130 lessons.

3. **`status-transactions` vs `status-is-up`.** These are distinct entries:
   Johnstone's improvisational concept (status as social behavior) vs.
   Lakoff/Johnson's cognitive metaphor (status mapped to vertical
   orientation). The Miner should cross-reference in `related:` fields.

4. **`yes-and` excluded.** Already claimed by comedy-writers-glossary
   project (issue #1885). If the Surveyor wants it here instead, move
   the sub-issue.

5. **Viewpoints not included as candidates.** Bogart's nine Viewpoints
   (spatial relationship, kinesthetic response, shape, gesture, repetition,
   architecture, tempo, duration, topography) are interesting but are
   performance-technique vocabulary, not metaphors or mental models with
   cross-domain transfer. Could be reconsidered if the Surveyor disagrees.
