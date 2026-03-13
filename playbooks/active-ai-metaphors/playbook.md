---
project_issue: 601
repo: metaphorex/metaphorex
source_type: web
status: draft
---

# Active Metaphors of the AI Moment

## Source Description

The live discourse around AI, LLMs, agents, and intelligence augmentation
-- blog posts, talks, essays, and emerging jargon from 2022-present, plus
foundational texts that shaped the framing. This is a **vein** project:
the source is ongoing and effectively unbounded. Each prospecting batch
identifies a coherent set of candidates.

**Batch 1** focuses on two clusters from the parent issue:

- **Cluster A** -- Agent orchestration archetypes (Gas Town, Ralph Wiggum
  Loop, swarm/crew/chain metaphors, tool use, chain-of-thought)
- **Cluster C** -- "What IS an AI?" competing framings (tool, copilot,
  intern, agent, oracle, prosthesis, pair programmer, mirror)

Plus foundational AI-discourse metaphors that cut across clusters:
hallucination, training-as-education, alignment, neural-network-as-brain,
data-as-fuel, prompt-engineering, safety-as-containment.

## Access Method

### Primary Archives

Academic and journalistic sources that enumerate and categorize AI
metaphors. These were used to validate and structure the candidate list.

1. **Matthijs Maas, "AI is Like... A Literature Review of AI Metaphors
   and Why They Matter for Policy" (2023)**
   https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4612468
   Catalogs 55 AI analogies in 5 categories: Essence, Operation, Relation,
   Function, Impact. The most comprehensive structured survey of AI
   metaphors in the policy literature. Full PDF available via SSRN.
   Categories used to validate candidate list completeness.

2. **Leon Furze, "AI Metaphors We Live By" (2024)**
   https://leonfurze.com/2024/07/19/ai-metaphors-we-live-by-the-language-of-artificial-intelligence/
   Blog post applying Lakoff/Johnson framework to AI discourse. Identifies
   black box, copilot, mirror, magnifying glass, spell checker, tsunami,
   digital plastic, and "slop as a service" metaphors. Useful for its
   explicit connection to conceptual metaphor theory.

3. **Making Science Public, "AI Metaphor Observatory" (2025)**
   https://makingsciencepublic.com/2025/11/14/making-the-case-for-an-ai-metaphor-observatory/
   https://makingsciencepublic.com/2025/11/21/ai-metaphor-studies-an-overview/
   Proposes systematic tracking of AI metaphors across media. Overview
   article surveys the full academic landscape of AI metaphor studies.

4. **Springer, "Between fact and fairy: tracing the hallucination
   metaphor in AI discourse" (2025)**
   https://link.springer.com/article/10.1007/s00146-025-02392-w
   Academic analysis of how the "hallucination" metaphor shapes
   understanding of LLM confabulation.

5. **Science, "The metaphors of artificial intelligence" (2025)**
   https://www.science.org/doi/10.1126/science.adt6140
   Science magazine article on anthropomorphic framing in AI terminology.
   Documents Drew McDermott's 1970s critique of "wishful mnemonics."

### Practitioner Primary Sources

Blog posts and tools that originate or document specific AI metaphors.

6. **Steve Yegge, "Welcome to Gas Town" (2025)**
   https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04
   https://github.com/steveyegge/gastown
   Origin of the Gas Town agent orchestration archetype. Mad Max-themed
   metaphor system: Mayor, Deacon, Rigs, Refinery.

7. **Geoffrey Huntley, "Ralph Wiggum as a software engineer" (2025)**
   https://ghuntley.com/ralph/
   Origin of the Ralph Wiggum Loop agent pattern. Simpsons-character
   metaphor for persistent retry loops.

8. **Maggie Appleton, "Gas Town's Agent Patterns" (2025-2026)**
   https://maggieappleton.com/gastown
   Design analysis of Gas Town patterns, bottlenecks, and vibecoding.

9. **Steve Jobs, "Bicycle for the Mind" interview (1990)**
   The foundational metaphor for computing as human amplification.
   Widely documented; no single canonical URL.

10. **Douglas Engelbart, "Augmenting Human Intellect" (1962)**
    The ur-text for intelligence prosthesis framing.

### Scraping Script

`scripts/extract_ai_metaphors.py` attempts to extract structured metaphor
data from the Furze blog and Maas paper summary page. Results are partial
-- these sources are written as prose, not structured data. The script
serves as a starting point for future archive scraping if structured
datasets (like the proposed AI Metaphor Observatory) become available.

### LLM Gap-Fill

12 of 31 candidates (39%) are LLM-sourced. These are metaphors actively
used in AI discourse but not explicitly cataloged in the archive sources
above. They include: alignment-is-physical-alignment, weights-are-knowledge,
chain-of-thought-is-self-talk, tool-use-is-physical-manipulation,
agent-swarm, ai-is-a-pair-programmer, context-window-is-working-memory,
guardrails, temperature-is-creativity, fine-tuning-is-specialization,
compute-is-a-resource, the-internet-is-a-mine. All are easily verifiable
in active AI discourse.

## Extraction Strategy

### What makes a good candidate

This project is NOT a dictionary of AI jargon. A candidate must be a
genuine **structural mapping** between domains, not just a technical term.
The test: does the metaphor import non-obvious structural assumptions from
the source domain that shape how people think about and build AI?

Good: "AI HALLUCINATION IS PERCEPTION DISORDER" -- imports psychiatric
framing that presupposes the model has perception, shapes whether people
treat confabulation as a bug or a fundamental limitation.

Bad: "Transformer" -- a technical architecture name that no longer functions
as an active metaphor (nobody thinks about electrical transformers).

### Prioritization (Batch 1)

- **Tier 1 (most structurally rich, do first):** ai-hallucination-is-
  perception-disorder, training-is-education, neural-network-is-a-brain,
  ai-is-a-tool, ai-is-a-copilot, gas-town, data-is-fuel, ai-safety-is-
  containment
- **Tier 2 (solid metaphors with clear breaks):** ai-is-an-agent,
  alignment-is-physical-alignment, prompt-engineering-is-programming,
  bicycle-for-the-mind, ralph-wiggum-loop, foundation-model-is-a-foundation,
  context-window-is-working-memory
- **Tier 3 (thinner but worth documenting):** ai-is-an-intern,
  ai-is-an-oracle, ai-is-a-mirror, weights-are-knowledge,
  temperature-is-creativity, fine-tuning-is-specialization, guardrails

### Kind assignments

- `conceptual-metaphor` -- most candidates. The source domain is active in
  users' minds when they use the term.
- `archetype` -- Gas Town, Ralph Wiggum Loop. These are named patterns with
  narrative structure, not just domain mappings.
- No `dead-metaphor` entries in this batch -- all these metaphors are
  actively contested in AI discourse. "Neural network" is the closest to
  dead, but the brain metaphor is actively debated.
- No `paradigm` entries in batch 1. The issue suggests "INTELLIGENCE
  AUGMENTATION IS A SPECTRUM" as a paradigm for batch 2+.

### Distinguishing from existing entries

Check `catalog/mappings/` for overlap. Currently no AI-specific mappings
exist. The general `people-are-machines` mapping is tangentially related
but covers the opposite direction (applying machine metaphors to humans,
not human metaphors to machines).

## Schema Mapping

### New frames needed

| Frame slug | Description |
|---|---|
| artificial-intelligence | AI systems, LLMs, agents, ML models as target domain |
| aviation | Pilot/copilot hierarchy, cockpit, instruments, flight |

### Existing frames that will be reused

- `tool-use` -- AI-as-tool
- `governance` -- AI-as-agent (legal/business agency)
- `religion` -- AI-as-oracle
- `medicine` -- hallucination, neural-network, prosthesis
- `containers` -- black box, safety-as-containment, jailbreaking
- `social-roles` -- intern, training-as-education
- `embodied-experience` -- bicycle, weights, tool-use-as-manipulation
- `mental-experience` -- chain-of-thought, context-window
- `economics` -- data-as-fuel, compute-as-resource, internet-as-mine
- `physics` -- alignment, temperature
- `architecture-and-building` -- foundation model
- `manufacturing` -- prompt engineering, fine-tuning
- `animal-behavior` -- swarm
- `social-behavior` -- ralph-wiggum-loop
- `collaborative-work` -- pair programmer
- `vision` -- mirror
- `journeys` -- guardrails

### New categories needed

| Category slug | Description |
|---|---|
| ai-discourse | Metaphors actively shaping AI development, policy, and public understanding |

### Existing categories that will be reused

- `cognitive-science` -- for metaphors about AI cognition
- `software-engineering` -- for metaphors about AI tooling
- `philosophy` -- for metaphors about AI nature and alignment
- `systems-thinking` -- for metaphors about AI infrastructure
- `security` -- for safety/containment metaphors
- `organizational-behavior` -- for workplace metaphors (intern, pair)

### Target frame

Most candidates target `artificial-intelligence` (new frame). Exceptions:
- `bicycle-for-the-mind` targets `computing`
- `the-internet-is-a-mine` targets `data-processing`

## Gotchas

1. **This is a vein, not an archive.** The candidate list is a batch, not
   an exhaustive enumeration. The issue identifies 6 clusters; batch 1
   covers clusters A and C plus cross-cutting foundational metaphors.
   Future batches should cover: B (growth/scaling), D (collective
   intelligence), E (machine interface optimization), F (computing as
   vehicle / Stephenson & Jobs lineage).

2. **No single canonical archive exists.** Unlike the Lakoff/Johnson
   project (which has the Osaka archive), AI-discourse metaphors are
   distributed across blog posts, academic papers, and live conversation.
   The Maas (2023) paper is the closest to a structured catalog but covers
   metaphors at the policy/analogy level, not the conceptual-metaphor level.
   The proposed "AI Metaphor Observatory" (Making Science Public, 2025)
   would be ideal but does not yet exist as a structured dataset.

3. **Rapid evolution.** These metaphors are being contested and
   consolidated in real-time. "Vibe coding" emerged in early 2025 and is
   already spawning sub-metaphors. The Miner should capture current usage
   but note that framings may shift. Date-stamping references is important.

4. **Anthropomorphism is the meta-pattern.** Almost every AI metaphor in
   this batch involves some degree of anthropomorphism. The Miner should
   address this explicitly in the "Where It Breaks" section of each entry
   rather than repeating it mechanically.

5. **The tool-copilot-agent progression.** Several candidates (ai-is-a-tool,
   ai-is-a-copilot, ai-is-an-agent) form a progression of increasing
   autonomy. The Miner should use `related:` links and cross-reference the
   progression in each entry. The issue suggests this progression is itself
   a paradigm ("INTELLIGENCE AUGMENTATION IS A SPECTRUM") for a future batch.

6. **LLM-sourced entries (39%).** Higher than the sw-eng-vernacular project
   (27%) because no structured archive comprehensively catalogs these
   metaphors at the conceptual-metaphor granularity. The academic sources
   catalog analogies and framings; this project maps them as structural
   metaphors with source/target frames. All LLM-sourced entries are
   verifiable in active discourse.

7. **Overlap with Maas categories.** Maas organizes by function
   (Essence/Operation/Relation/Function/Impact). This project organizes by
   source-to-target mapping. A single Maas category may contain multiple
   candidates here, and vice versa.

8. **31 candidates in batch 1.** Well within GitHub's 100 sub-issue limit.
   Future batches for remaining clusters should be similarly sized.

## Future Batches

### Batch 2: Growth, scaling, and computing-as-vehicle (Clusters B + F)

Candidates to research:
- S-curve / inflection point
- "Feeling the exponential" -- exponential growth as physical force
- Dyson sphere / intelligent sun -- scaling as megastructure
- Bootstrapping -- AI-bootstrapping-AI
- Stephenson's OS-as-vehicle archetypes (Mac=Beetle, Windows=wagon, etc.)
- Vibe coding -- programming without understanding
- Scaling laws -- physics metaphor for capability prediction
- Chinchilla / compute-optimal -- animal names for scaling regimes

### Batch 3: Collective intelligence and machine interfaces (Clusters D + E)

Candidates to research:
- Truth is a market price (prediction markets)
- The crowd is wise
- Folksonomy -- classification as democratic process
- Synthetic data -- data as manufactured product
- SEO-to-LLM optimization cross-field mapping
- Machine interfaces as the new DX
- MCP / function calling as API metaphors
