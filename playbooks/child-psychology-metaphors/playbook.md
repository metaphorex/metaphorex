---
project_issue: 1357
repo: metaphorex/metaphorex
source_type: corpus
status: draft
---

# Playbook: Child Psychology's Load-Bearing Metaphors

## Source Description

The conceptual metaphors that constitute the core vocabulary of child and
developmental psychology -- scaffolding, zone of proximal development,
the good enough mother, attachment, holding environment, transitional
object, and the meta-debate about whether these metaphors are adequate.

This source spans five major theorists and their schools:

- **D.W. Winnicott** (1896-1971): Object relations / pediatric
  psychoanalysis. Key metaphors: good enough mother, holding environment,
  transitional object, potential space, true self/false self, mirror role,
  primary maternal preoccupation, environmental impingement, going on being,
  facilitating environment.
- **John Bowlby** (1907-1990): Attachment theory. Key metaphors: secure
  base, safe haven, internal working models, attachment as bond, proximity
  maintenance, monotropy, separation anxiety.
- **Jean Piaget** (1896-1980): Genetic epistemology. Key metaphors: schema,
  assimilation and accommodation, equilibration, object permanence, stages
  of development.
- **Lev Vygotsky** (1896-1934): Sociocultural theory. Key metaphors: zone
  of proximal development, more knowledgeable other, internalization.
- **Jerome Bruner** (1915-2016) / **Barbara Rogoff** (1950-): Scaffolding
  and its critiques. Key metaphors: scaffolding (Wood/Bruner/Ross 1976),
  guided participation, apprenticeship in thinking (Rogoff 1990).
- **Erik Erikson** (1902-1994): Psychosocial development. Key metaphors:
  identity crisis, trust vs. mistrust, generativity vs. stagnation.

This field is notable because practitioners have explicitly debated the
adequacy of their own metaphors. Stone (1998) asked "Should We Salvage the
Scaffolding Metaphor?" -- a rare example of a discipline performing
reflexive metaphor criticism on its own core vocabulary.

## Access Method

### Primary Archives

No single structured database exists for this domain. The candidate list
was assembled from multiple structured reference sources:

1. **MythosAndLogos Winnicott page** --
   http://mythosandlogos.com/Winnicott.html
   Structured list of Winnicott's core concepts with descriptions. Used as
   primary source for the Winnicott cluster (10 candidates).

2. **Wikipedia: Attachment theory** --
   https://en.wikipedia.org/wiki/Attachment_theory
   Comprehensive structured article with named concepts, definitions, and
   citations. Used for the Bowlby/Ainsworth cluster (7 candidates).

3. **Simply Psychology: Piaget, Bowlby, Attachment** --
   https://www.simplypsychology.org/piaget.html
   https://www.simplypsychology.org/bowlby.html
   https://www.simplypsychology.org/attachment.html
   Structured educational glossaries with concept definitions. Cross-
   referenced against Wikipedia entries.

4. **Wikipedia: Zone of Proximal Development** --
   https://en.wikipedia.org/wiki/Zone_of_proximal_development
   Structured article with named concepts for the Vygotsky cluster.

5. **Wikipedia: Erikson's stages of psychosocial development** --
   https://en.wikipedia.org/wiki/Erikson's_stages_of_psychosocial_development

6. **Stone (1998) via SFU mirror** --
   https://www.sfu.ca/~jcnesbit/EDUC220/ThinkPaper/Stone1998.htm
   Full text of "The Metaphor of Scaffolding: Its Utility for the Field of
   Learning Disabilities." Lists alternative metaphors (guided participation,
   apprenticeship) and critiques of scaffolding.

7. **EyeMindSpirit: Winnicott's Theories** --
   https://www.eyemindspirit.com/blogs/spirituality-science/what-are-winnicotts-theories

8. **PsyProfi: Donald Winnicott** --
   https://psyprofi.si/donald-winnicott/eng

### Methodology

All 31 candidates were identified from the structured archives above.
Candidates were cross-referenced across at least two independent sources.
All entries are tagged `source: "archive"` because they come from published,
verifiable reference material.

No scraping script is provided because the sources are structured reference
pages (Wikipedia, educational glossaries) rather than machine-parseable
indexes or HTML directory listings. The candidate extraction was manual but
systematic: each source was fetched and concepts were enumerated.

## Extraction Strategy

### For Miners

Each candidate has a theorist cluster. Mine in clusters to maintain thematic
coherence and cross-reference within `related:` fields.

**Cluster 1 -- Winnicott (10 entries):**
good-enough-mother, holding-environment, transitional-object,
potential-space, true-self-false-self, mirror-role-of-mother,
primary-maternal-preoccupation, environmental-impingement,
going-on-being, facilitating-environment

Winnicott entries should emphasize:
- The clinical origin (pediatric practice, not abstract theory)
- The radical quality of his reframings (imperfection as feature, not bug)
- Migration to other fields (organizational theory, therapy, design)
- Cross-links within the Winnicott cluster (these concepts form a system)

**Cluster 2 -- Bowlby/Ainsworth (7 entries):**
secure-base, safe-haven, internal-working-model, attachment-styles,
separation-anxiety, attachment-as-bond, proximity-maintenance, monotropy

Bowlby entries should emphasize:
- The ethological/evolutionary foundation
- The spatial/physical metaphor structure (bonds, bases, havens, distances)
- Migration to adult relationship psychology and organizational theory
- The "internal working model" as cognitive science avant la lettre

**Cluster 3 -- Piaget (5 entries):**
object-permanence, assimilation-and-accommodation, schema,
equilibration, stages-of-development

Piaget entries should emphasize:
- Biology-to-cognition transfer (Piaget's signature metaphorical move)
- Schema migration to computer science and UX
- Stage theory as contested metaphor (continuous vs. discrete debate)

**Cluster 4 -- Vygotsky/Bruner/Rogoff (5 entries):**
scaffolding, zone-of-proximal-development, more-knowledgeable-other,
internalization, guided-participation, apprenticeship-in-thinking

This cluster should emphasize:
- The scaffolding meta-debate (Stone 1998)
- Rogoff's critique and alternatives
- Scaffolding's migration to education, management, and software
- ZPD as spatial metaphor that redefines competence

**Cluster 5 -- Erikson (3 entries):**
identity-crisis, trust-vs-mistrust, generativity

Erikson entries should emphasize:
- "Identity crisis" as one of psychology's most successful metaphor exports
- The oppositional framing (vs.) as structural choice
- Migration to everyday language

### Author Attribution

All entries should use `author: agent:metaphorex-miner` and set
`provenance: child-psychology-metaphors` in the frontmatter.

### Frame Creation

**Existing frames that will be reused:**
architecture-and-building, spatial-location, manufacturing, containers,
nurturing-and-creation, vision, medicine, physics, fluid-dynamics,
exploration, seafaring, materials, biology, journeys, social-roles,
conflict-escalation, natural-selection, folk-taxonomy, organism,
education, performance, mental-experience

**No new frames are required.** All source frames map to existing catalog
frames.

### Categories

All entries get `psychology` as primary category. Additional categories
per cluster:
- Piaget + Vygotsky entries: `cognitive-science`
- Vygotsky/Bruner/Rogoff + Piaget stages: `education-and-learning`
- Bowlby attachment-styles + Erikson entries: `social-dynamics`
- Winnicott potential-space: `arts-and-culture`

## Schema Mapping

| Field | Value | Notes |
|-------|-------|-------|
| `kind` | `metaphor` or `mental-model` | Metaphor if there is a clear source-target mapping; mental-model if it is primarily a framework for analysis |
| `source_frame` | See manifest | Mapped to existing catalog frames |
| `target_frame` | Mostly `nurturing-and-creation`, `education`, `mental-experience` | |
| `applies_to` | Omit | These are general-purpose metaphors |
| `author` | `agent:metaphorex-miner` | |
| `provenance` | `child-psychology-metaphors` | |
| `grounding` | `established` | All are from peer-reviewed, widely-cited literature |

## Gotchas

1. **Winnicott's concepts form a system.** The holding environment enables
   going-on-being; environmental impingement interrupts it; the good enough
   mother provides the facilitating environment; transitional objects bridge
   the potential space. Miners must cross-link extensively via `related:`.

2. **"Scaffolding" is the most meta-reflexive entry.** It has an explicit
   literature debating whether the metaphor is adequate. The Limits section
   should draw on Stone (1998) and Rogoff's critiques, not just the Miner's
   own analysis. This is a rare case where the source material itself
   provides the metaphor criticism.

3. **Attachment theory vocabulary has been diluted by pop psychology.**
   "Attachment styles" in particular has been oversimplified in dating
   advice and self-help. Entries should distinguish the clinical/research
   concept from the pop-psychology usage.

4. **Piaget's stage theory is contested.** Neo-Piagetians and dynamic
   systems theorists argue development is more continuous. The entry should
   cover this debate in Limits.

5. **The "schema" entry overlaps with database/computing usage.** The
   Piaget concept predates and inspired the computing usage. The entry
   should trace this migration explicitly.

6. **31 candidates is well under the 100 sub-issue cap.** No overflow
   handling needed.

7. **Existing catalog entry overlap:** `possessing-is-holding` exists but
   is from the Osaka Conceptual Metaphor List (cognitive linguistics), not
   Winnicott. No conflict -- different concept, different source frame.
