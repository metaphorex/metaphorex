---
project_issue: 1230
repo: metaphorex/metaphorex
source_type: book
status: draft
---

# Napoleon's Military Maxims -- Strategic Reasoning as Metaphor

## Source Description

Three primary sources of military strategic concepts that have been transferred
into business, management, decision-making, and everyday discourse:

1. **Napoleon Bonaparte, Military Maxims** -- 78 numbered maxims compiled by
   General Burnod and translated by Sir George C. D'Aguilar. Available on
   Project Gutenberg (EBook #50750). A bounded, enumerable source.

2. **Carl von Clausewitz, On War** -- particularly the concepts of "fog of war"
   (Book I, Chapter 7), "friction" (Book I, Chapter 7), and "center of gravity"
   (Book VI). Available via clausewitzstudies.org.

3. **Sun Tzu, The Art of War** -- 13 chapters, available on MIT Classics Archive.
   Key transferable concepts: deception as strategy, subduing without fighting,
   know yourself/know your enemy.

This is an **archive-type** project. The primary source (Napoleon's 78 maxims)
is finite and enumerable. The supplementary sources (Clausewitz, Sun Tzu) are
bounded. The candidate list is exhaustive relative to concepts that encode
transferable strategic reasoning.

## Access Method

### Primary Archives

1. **Project Gutenberg: Napoleon's Maxims of War**
   https://www.gutenberg.org/files/50750/50750-h/50750-h.htm
   Full HTML text of all 78 maxims with commentary. Scraped via
   `scripts/extract_napoleon_maxims.py`. The HTML uses encoding that requires
   careful parsing; the script includes a verified static fallback dataset.

2. **NapoleonGuide.com: Maxims on War**
   https://www.napoleonguide.com/maxim_war.htm
   Unnumbered collection of 80+ Napoleon quotations on warfare. Used as a
   cross-reference and to identify aphorisms not in the Burnod compilation
   (e.g., "An army marches on its stomach," "Every soldier carries a marshal's
   baton in his pack").

3. **MIT Classics Archive: Sun Tzu, The Art of War**
   https://classics.mit.edu/Tzu/artwar.html
   Lionel Giles translation, 13 chapters. Key concepts extracted manually.

4. **ClausewitzStudies.org: On War, Book I Chapter 7**
   https://clausewitzstudies.org/readings/OnWar1873/BK1ch07.html
   The "fog" and "friction" concepts from Clausewitz's foundational text.

### Scraping Script

`scripts/extract_napoleon_maxims.py` fetches the Project Gutenberg HTML and
extracts all 78 maxims. Due to HTML encoding issues in the Gutenberg text,
the script includes a verified static fallback dataset extracted and validated
against the source on 2026-03-19. The script outputs JSON to stdout and is
idempotent.

### Candidate Selection Methodology

Of Napoleon's 78 maxims, most are specific tactical advice about cavalry,
artillery, fortifications, river crossings, and troop deployment. These do
not transfer meaningfully beyond military contexts. The issue's selectivity
guidance is explicit: "Import only maxims that encode strategic reasoning
transferable beyond military contexts."

**Selection criteria applied:**
- Does the maxim encode a general principle of strategic reasoning?
- Has the concept demonstrably transferred to business, management, or
  everyday discourse?
- Does the mapping carry structural insight (not just vocabulary borrowing)?

**Result:** 14 Napoleon maxims selected out of 78 (18%). Supplemented with
3 Clausewitz concepts and 3 Sun Tzu concepts. 5 additional military metaphors
from general military discourse (LLM-sourced gap-fill).

### LLM Gap-Fill

5 of 25 candidates are LLM-sourced (marked `"source": "llm"` in manifest):
- `boots-on-the-ground` -- common military-to-business dead metaphor
- `collateral-damage` -- common military-to-business dead metaphor
- `beachhead-strategy` -- from Moore's "Crossing the Chasm"
- `flanking-maneuver` -- general military concept widely used in business

These are well-attested in business and everyday language but do not trace
to a specific numbered maxim or canonical text passage.

## Extraction Strategy

### What makes a good candidate for this project

A military maxim or concept qualifies when it encodes **transferable strategic
reasoning** -- a structural insight about competition, decision-making,
organizational design, or resource allocation that maps cleanly from the
military source domain to non-military target domains.

**Good candidates:**
- "The moral is to the physical as three to one" -- quantifies the importance
  of intangible factors, transfers to team management
- "Never do what the enemy wishes" -- pure game-theoretic reasoning, transfers
  to negotiation and competitive strategy
- "Fog of war" -- decision-making under uncertainty, transfers everywhere

**Bad candidates (excluded):**
- "Among mountains, a great number of positions are always to be found very
  strong in themselves" (Maxim XIV) -- specific terrain advice, no transfer
- "Charges of cavalry are equally useful at the beginning, the middle, and
  the end of a battle" (Maxim XLIX) -- specific tactical advice about cavalry
- "It is contrary to the usages of war to allow parks or batteries of
  artillery to enter a defile" (Maxim XXXIII) -- specific operational rule

### Kind assignments

- **conceptual-metaphor** (21 entries): active mappings from war domain to
  competition, decision-making, or organizational behavior. The war frame
  structures how people think about the target domain.
- **dead-metaphor** (4 entries): military terms so thoroughly naturalized that
  most speakers are unaware of the military origin. "Boots on the ground,"
  "collateral damage."

### Relationship to existing entries

The catalog already contains several WAR-frame entries:
- `argument-is-war` -- the Lakoff/Johnson canonical example
- `competition-is-war` -- the broad conceptual metaphor
- `love-is-war`, `morality-is-war`, `social-conflict-is-war` -- domain-specific
  applications
- `treating-illness-is-fighting-a-war` -- medical domain application

This project adds **specific strategic reasoning patterns** from the war
domain that are NOT covered by the broad "X IS WAR" entries. Where
`competition-is-war` says "we think about competition using war vocabulary,"
entries like `fog-of-war` or `unity-of-command` say "here is a specific
structural insight from war that has been imported into non-military thinking."

The Miner should cross-reference each entry with `competition-is-war` in the
`related:` field.

## Schema Mapping

### Frames

**Existing frames that will be reused:**
- `war` (source frame for all entries)
- `competition` (target frame for competitive strategy entries)
- `decision-making` (target frame for entries about choice under uncertainty)
- `organizational-behavior` (target frame for entries about command structure)
- `systems-performance` (target frame for friction)

**New frames needed:** None. The existing frame set covers all target domains.

### Categories

**Existing categories that will be reused:**
- `systems-thinking` -- all entries (strategic reasoning as systems analysis)
- `cognitive-science` -- entries about perception and knowledge (fog-of-war,
  know-your-enemy)
- `organizational-behavior` -- entries about command and morale
- `mathematics-and-logic` -- entries with game-theoretic reasoning
- `linguistics` -- dead-metaphor entries

### Entry template guidance for Miner

Each entry should include:
- **Source attribution**: which maxim number (Napoleon), which chapter (Sun Tzu),
  or which concept (Clausewitz)
- **The original military context**: what problem the maxim addressed in warfare
- **Transfer mechanisms**: how the insight maps to non-military domains, with
  specific examples from business, technology, or everyday life
- **Limits**: where the military-to-civilian transfer breaks down. This is
  especially important because military metaphors carry hidden assumptions
  about adversarial dynamics, zero-sum competition, and hierarchical authority
  that may not apply in the target domain.
- **Expressions**: common phrases that use this concept in non-military contexts

## Gotchas

1. **Overlap with ARGUMENT IS WAR and COMPETITION IS WAR.** The Miner must
   differentiate: those entries document the broad conceptual metaphor (we
   structure argument/competition using war vocabulary). These entries document
   specific strategic reasoning patterns (fog of war, interior lines, unity of
   command) that carry distinct structural insights. Cross-reference with
   `related:` but do not duplicate.

2. **Napoleon attribution is unreliable.** Many famous "Napoleon quotes"
   (especially from napoleonguide.com) are apocryphal or mis-attributed. The
   Burnod/D'Aguilar compilation (Project Gutenberg) is the most reliable
   source for the numbered maxims. Quotations not in that compilation should
   be treated with skepticism. The Miner should note attribution uncertainty
   where relevant.

3. **"Strategy" vs "tactics" distinction matters.** The issue explicitly asks
   for strategic reasoning that transfers. Tactical advice (how to position
   cavalry, how to cross a river) does not transfer. The Miner should be
   clear about what level of abstraction makes each concept transferable.

4. **Military metaphors carry ideological freight.** The war frame imports
   adversarial, zero-sum, hierarchical assumptions. The Limits section of
   each entry should address this honestly. "Unity of command" sounds clean
   but imports authoritarianism. "Scorched earth" normalizes destruction.
   These are not neutral frames.

5. **Dead metaphors vs conceptual metaphors.** Some candidates (boots on the
   ground, collateral damage) are dead metaphors -- the military origin has
   faded. Others (fog of war, strategic retreat) are active conceptual metaphors
   where speakers are aware of the military framing. The Miner should assign
   `kind: dead-metaphor` only where the military origin is genuinely invisible
   to most speakers.

6. **25 candidates total.** Well within GitHub's 100 sub-issue limit.

7. **The `military-command` and `military-history` frames already exist** in
   the catalog but are not used as target frames here -- the transfer goes
   FROM war TO non-military domains.
