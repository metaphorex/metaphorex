---
project_issue: 1234
repo: metaphorex/metaphorex
source_type: web
status: draft
---

# Comedy Writers' Room Glossary — Extraction Playbook

## Source Description

Andy Riley's "How to Talk Comedy Writer" is a crowdsourced glossary of insider
terminology from British TV comedy writers' rooms. Riley (credits include Veep,
Black Books, Smack the Pony) solicited terms from working comedy writers and
published them on his blog starting in 2014, with updates through 2019. The
glossary contains 100+ terms with attributions to their originators.

Supplementary sources:
- **Greg Dean's stand-up comedy glossary** (stand-upcomedy.com) -- a more
  formal, pedagogical glossary of stand-up mechanics
- **OtherNetwork comedy writers glossary** -- aggregated TV writers' room terms
  from SNL, 30 Rock, Family Guy, The Simpsons veteran writers
- **John Vorhaus, *The Comic Toolbox*** -- formalized comedy principles
  ("comedy = truth + pain", "clash of context")
- **Halpern & Close, *Truth in Comedy*** -- improv principles, especially
  "Yes, and..."
- **Keith Johnstone, *Impro*** (1979) -- status transactions, spontaneity

## Access Method

### Primary archive: Riley's glossary (HTML blog posts)

The glossary exists across four blog post versions:

| Version | URL | Approx. terms |
|---------|-----|---------------|
| Oct 2019 | https://misterandyriley.com/2019/10/25/how-to-talk-comedy-writer-updated-25th-october-2019/ | ~110 |
| Oct 2018 | https://misterandyriley.com/2018/10/12/how-to-talk-comedy-writer-updated-3/ | ~90 |
| Mar 2017 | https://misterandyriley.com/2017/03/31/how-to-talk-comedy-writer-updated-2/ | ~70 |
| Dec 2014 | https://misterandyriley.com/2014/12/16/how-to-talk-comedy-writer/ | ~40 |

Each version is a single HTML page with terms formatted as bold term names
followed by em-dash-separated definitions in paragraph tags. The scraping
script at `scripts/scrape_riley_glossary.py` fetches all four versions and
deduplicates by normalized term name.

### Secondary archives

- Greg Dean glossary: https://stand-upcomedy.com/glossary/ (HTML, ~100 terms)
- OtherNetwork glossary: https://othernetwork.com/free-comedy-writers-glossary/
  (HTML, ~20 terms aggregated from TV writer interviews)

### Non-archive sources (LLM-supplemented)

- Vorhaus's "Comic Toolbox" concepts are not available as a structured online
  glossary. The "comedy is truth and pain" candidate is sourced from LLM
  knowledge of the book and is flagged accordingly.
- "Yes, and..." is documented in multiple improv archives but the specific
  cross-domain transfer framing is synthesized from LLM knowledge of Kulhan's
  *Getting to "Yes And"* (Stanford UP, 2017) and therapeutic applications.

## Extraction Strategy

### Selectivity filter (from issue #1234)

The issue specifies strong selectivity: import only terms encoding reasoning
applicable to creativity, communication, persuasion, or collaboration beyond
comedy. The test: "would a non-comedy practitioner gain insight from this
mapping?"

From Riley's ~110 terms, approximately 15 pass this filter. Most terms are
delightfully specific writers' room jargon (e.g., "Zammo", "Tariq",
"Gooberfruit") that do not encode transferable reasoning patterns.

### Selection criteria applied

A term was included if it meets at least one of:

1. **Already transferred**: The term is documented in use outside comedy
   (yes-and, shit sandwich, lampshading, callback, vomit draft)
2. **Structural parallel**: The term names a pattern with clear structural
   analogues in other domains (lightning rod / negotiation, oxbow lake /
   dead code, hat-on-a-hat / single responsibility principle)
3. **Diagnostic precision**: The term names a failure mode or dynamic that
   non-comedy practitioners would recognize but lack a word for (clapter,
   raptor pit, load-bearing pun)

### What was excluded and why

- **Comedy-specific technique terms** (detonator word, bicycle cut, Gilligan
  cut, bananas on bananas): these describe comedy mechanics without
  transferable reasoning
- **Proper-noun insider jokes** (Zammo, Tariq, Bono, Group 4): meaning
  depends entirely on the cultural reference; no structural transfer
- **Synonyms and variants**: Riley documents multiple independent coinages
  for the same concept (lightning rod / queen mum / purple goat / clay
  pigeon). We take one canonical entry and note variants
- **Terms already in the catalog**: rubber-duck-debugging already exists;
  the rubber-duck-solution candidate is noted as a comedy-origin parallel
  that should cross-reference rather than duplicate

## Schema Mapping

| Riley field | Metaphorex field | Notes |
|-------------|-----------------|-------|
| Term name | `name` | Title-cased, parenthetical gloss added when the comedy term is opaque |
| Term name (slugified) | `slug` | kebab-case, suffixed to disambiguate if needed |
| Definition | Informs `Transfers` section | The definition is the raw material, not a direct mapping |
| Attribution | `References` section | "via Chris Addison" becomes a reference line |
| (inferred) | `kind` | Most are `cross-field-mapping`; some are `conceptual-metaphor` |
| (inferred) | `source_frame` | Usually `comedy-craft`; sometimes the metaphor's source domain (geology for oxbow lake) |
| (inferred) | `applies_to` | The target domain(s) where the term transfers |
| (inferred) | `categories` | Primarily `arts-and-culture`, `organizational-behavior` |

### Frames needed

New frames to create:

- `comedy-craft` -- the practice of writing and performing comedy; roles
  include writer, performer, showrunner, room, audience, material, draft
- `creative-process` -- the cognitive and practical process of creative
  production; roles include creator, material, draft, revision, constraint
- `narrative-and-storytelling` -- structure and mechanics of narrative;
  roles include narrator, audience, plot, exposition, payoff
- `negotiation-and-persuasion` -- interpersonal influence and deal-making;
  roles include negotiator, counterpart, offer, concession, anchor
- `problem-solving` -- general problem-solving reasoning; roles include
  solver, problem, approach, insight, solution

Check existing frames before creation -- some of these may already exist
or overlap with existing frames.

## Gotchas

1. **Rubber duck overlap**: `rubber-duck-debugging` already exists in the
   catalog. The `rubber-duck-solution` candidate should cross-reference it
   in `related:` and frame the comedy-origin angle as a convergent coinage,
   not a duplicate entry. Miner should read the existing entry first.

2. **Attribution chains**: Riley attributes terms to specific writers (e.g.,
   "via Chris Addison", "via Charlie Brooker"). These are not academic
   citations but should be preserved in the References section as oral
   tradition attributions.

3. **Variant names**: Several concepts have 3-4 independent names in the
   glossary (lightning rod variants, vomit draft variants, oxbow lake
   variants). The entry should pick one canonical name and list variants
   in Expressions.

4. **"Yes, and..." scope**: This is arguably the most important candidate
   but also the largest in scope. It has an entire book (*Getting to "Yes
   And"*) and extensive cross-domain literature. The Miner should scope
   the entry to the improv-origin framing and cross-domain transfer pattern,
   not attempt to survey all business-improv literature.

5. **Candidate count is within sub-issue cap**: 15 candidates is well under
   the 100 sub-issue GitHub limit. No overflow handling needed.

6. **Riley's site stability**: The blog posts have been stable since 2019
   but are on a personal WordPress site with no guaranteed uptime. The
   scraping script should be run during prospecting to capture the data;
   the manifest is the system of record, not the live site.
