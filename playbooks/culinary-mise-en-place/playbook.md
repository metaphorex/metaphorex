---
project_issue: 1351
repo: metaphorex/metaphorex
source_type: web
status: draft
---

# Playbook: Culinary Mise en Place -- Kitchen Wisdom as Metaphor

## Source Description

Culinary **mise en place** philosophy and professional kitchen culture --
from Escoffier's brigade system (1890s) through Anthony Bourdain's
*Kitchen Confidential* (2000) to Dan Charnas's *Work Clean* (2016).

The professional kitchen is one of the richest metaphor-exporting domains
in modern culture. Its terminology has migrated into:

- **Project management** -- mise en place as preparation methodology
- **Software engineering** -- front-of-house/back-of-house, on the fly, 86'd
- **Operations** -- the rush, in the weeds, dying on the pass
- **Communication protocols** -- call and callback, Behind!/Corner!/Hot!
- **Organizational design** -- brigade system, expo role, station specialization

Dan Charnas explicitly codified this migration in *Work Clean*, extracting
10 universal principles from 100+ chef interviews.

## Access Method

### Primary Archives

**Escoffier School -- Kitchen Slang and Lingo**
- URL: https://www.escoffier.edu/blog/culinary-arts/slang-and-lingo-every-chef-should-learn/
- Format: HTML article with bold-tagged terms and inline definitions
- Coverage: ~14 kitchen slang terms
- Scraping script: `scripts/extract_kitchen_glossaries.py`

**Escoffier School -- Kitchen Jargon**
- URL: https://www.escoffier.edu/blog/culinary-arts/more-useful-examples-of-chef-jargon/
- Format: HTML article organized by category (front-of-house, back-of-house,
  communication alerts, prep and cooking, general operations)
- Coverage: ~25 terms across 5 categories
- Scraping script: `scripts/extract_kitchen_glossaries.py`

**WebstaurantStore -- Kitchen Slang A-Z**
- URL: https://www.webstaurantstore.com/article/511/kitchen-slang-phrases.html
- Format: HTML glossary with bold terms and paragraph definitions
- Coverage: ~29 kitchen slang terms
- Scraping script: `scripts/extract_kitchen_glossaries.py`

**WebstaurantStore -- Culinary Terms Glossary**
- URL: https://www.webstaurantstore.com/article/939/culinary-terms-glossary.html
- Format: HTML glossary organized A-Z
- Coverage: ~60 culinary terms
- Scraping script: `scripts/extract_kitchen_glossaries.py`

### Secondary Sources (manual research, not scraped)

**Dan Charnas, Work Clean (2016) -- 10 Principles of Mise en Place**
- URL: https://www.nateliason.com/notes/work-clean-dan-charnas (book notes)
- URL: https://workclean.com/ (author site)
- The 10 principles were extracted from Nat Eliason's detailed book notes
  and cross-referenced with the Amazon/Goodreads descriptions
- Principles: (1) Planning is prime, (2) Arranging spaces/perfecting
  movements, (3) Cleaning as you go, (4) Making first moves, (5) Finishing
  actions, (6) Slowing down to speed up, (7) Call and callback, (8) Open
  ears and eyes, (9) Inspect and correct, (10) Total utilization

**Escoffier's Brigade de Cuisine**
- URL: https://www.escoffier.edu/blog/culinary-pastry-careers/different-types-of-chef-jobs-in-the-brigade-de-cuisine/
- The kitchen hierarchy system: chef de cuisine, sous chef, chef de partie,
  commis chef, and specialized station roles

**Anthony Bourdain, Kitchen Confidential (2000)**
- No online archive; book source. Bourdain popularized kitchen culture
  for mainstream audiences. Key contributions: the intensity metaphors
  (the rush, in the weeds), the machismo culture, and the idea that
  kitchen work is combat.

## Extraction Strategy

### Candidate Selection Criteria

Not every culinary term is a metaphor worth cataloging. The filter:

1. **Has the term migrated outside the kitchen?** -- "In the weeds" is used
   by project managers who have never cooked. "Brunoise" is not.
2. **Does the term encode a structural insight?** -- "Dying on the pass"
   encodes queuing theory. "Julienne" encodes a cutting technique.
3. **Is the term's kitchen origin still legible?** -- "86'd" has kitchen
   provenance but the origin story is debatable. Include it.
4. **Does the Charnas framework explicitly bridge domains?** -- All 10
   Work Clean principles qualify because the book's entire purpose is
   cross-domain transfer.

### Kind Assignment

- **paradigm**: Overarching systems (mise en place, brigade system)
- **pattern**: Repeatable protocols (call and callback, behind/corner/hot,
  expo role)
- **mental-model**: Charnas principles and decision heuristics
  (planning is prime, meeze point, coming to zero)
- **metaphor**: Terms that carry structural meaning from kitchen to other
  domains (in the weeds, 86'd, dying on the pass, the line)

### Frame Mapping

All candidates use `source_frame: food-and-cooking` (existing frame).

Target frames:
- `organizational-behavior` -- most candidates (preparation, hierarchy, operations)
- `communication` -- call/callback protocols, spatial awareness calls
- `systems-thinking` -- WIP limits, flow, waste concepts

### Entry Structure

Each entry should include:

**Transfers**: How the kitchen concept maps structurally to other domains.
Focus on the structural parallel, not the surface similarity. Example:
"Dying on the pass maps the physics of food temperature decay onto the
economics of delayed handoffs in any pipeline."

**Limits**: Where the metaphor breaks down. Kitchen metaphors often carry
implicit assumptions:
- High-pressure, time-bounded service windows (not all work has a "rush")
- Physical co-location (kitchen callouts assume shared space)
- Hierarchical authority (not all teams have a "chef de cuisine")
- Perishability (not all work products degrade on the pass)

**Expressions**: Documented usage in non-kitchen contexts.

## Schema Mapping

| Manifest field   | Entry frontmatter field |
|------------------|------------------------|
| slug             | slug (and filename)     |
| name             | name                    |
| kind             | kind                    |
| source_frame     | source_frame            |
| target_frame     | applies_to[0] (loosely) |
| categories       | categories              |

Additional frontmatter fields to set:
- `author: agent:metaphorex-miner`
- `grounding: established` for widely-used terms (mise en place, 86'd, in the weeds)
- `grounding: folk` for Charnas principles and less-migrated terms
- `related:` cross-link within the project (mise-en-place <-> cleaning-as-you-go, etc.)

## Gotchas

1. **Charnas principles overlap with kitchen jargon.** "Call and callback"
   appears both as a Charnas principle and as the kitchen "Heard!" protocol.
   The manifest has separate entries for the kitchen practice (`heard`) and
   the Charnas abstraction (`call-and-callback`). The Miner should
   cross-reference them via `related:` fields.

2. **"Open ears and eyes" (Charnas principle 8) is too generic.** It is
   included in the Charnas list for completeness but may be too thin for
   a standalone entry. The Miner should fold it into the mise-en-place
   entry's Transfers section if it cannot stand alone.

3. **The `food-and-cooking` frame already exists** in the catalog. No new
   frame creation needed for the source side. Target frames
   (`organizational-behavior`, `communication`) also exist.

4. **34 candidates is under the 100 sub-issue cap.** No overflow handling
   needed.

5. **Brigade system roles vs. the brigade system itself.** The manifest
   includes `brigade-system` as the overarching paradigm, plus `sous-chef`
   and `chef-de-partie` as specific role metaphors. Other brigade roles
   (saucier, poissonnier, rotisseur, etc.) are NOT included because they
   have not migrated outside kitchen culture as metaphors.

6. **"The rush" is the only LLM-sourced candidate.** It was not found in
   any scraped glossary (glossaries tend to define jargon, not experiential
   states) but is widely used in kitchen culture and has migrated into
   general operations language. All other candidates are archive-sourced.
