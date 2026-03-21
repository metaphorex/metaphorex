# Structural enrichment vocabulary

## Purpose

Define the controlled vocabularies for five new frontmatter fields that
enable structural similarity retrieval across the catalog. The goal:
when someone describes a system or problem, surface non-obvious metaphors
that share structural shape, not just topical overlap.

**Parent concern**: content enrichment (#1454), embeddings (#1456)
**Depends on**: schema migration (#1453) landing first

---

## Design principles

- **Casuals first, academics second.** Field names and values should be
  self-explanatory. Academic provenance is noted but doesn't drive naming.
- **Small, closed vocabularies.** Each vocabulary is small enough for high
  inter-annotator agreement and LLM-automatable tagging.
- **Universal across kinds.** All five fields apply to all five entry kinds
  (metaphor, pattern, archetype, paradigm, mental-model). This is what
  enables cross-kind structural retrieval.
- **Additive, not breaking.** All fields are optional. Existing entries
  remain valid without them.

---

## Field 1: `embodied_patterns[]`

**Per entry: 2-4 values. All kinds.**

Pre-conceptual spatial and kinesthetic patterns grounded in bodily
experience. These operate below the domain level --- two entries from
completely different domains can share the same embodied pattern, which
is exactly what makes them useful for non-obvious retrieval.

Academic provenance: "image schemas" (Johnson 1987, *The Body in the
Mind*; Lakoff 1987, *Women, Fire, and Dangerous Things*). We use
"embodied patterns" because "image" misleadingly suggests something
visual. These are felt, bodily patterns --- what it's like to be inside
something, to push against resistance, to follow a path.

### Values

#### Spatial containment and boundary

| Value | Felt experience | Canonical example |
|---|---|---|
| `container` | In/out, boundary, interior/exterior, enclosed vs exposed | Sandbox, echo chamber, filter bubble |
| `boundary` | Edge between regions, crossing point, permeability | Firewall, membrane, threshold |
| `center-periphery` | Core vs margin, focus vs fringe, hub vs spoke | Hub and spoke, ivory tower, margin |
| `surface-depth` | Hidden/revealed, shallow/deep, what's underneath | Iceberg model, deep learning, root cause |

#### Motion and path

| Value | Felt experience | Canonical example |
|---|---|---|
| `path` | Source -> trajectory -> destination, waypoints, progress | Life is a journey, roadmap, pipeline |
| `near-far` | Proximity, distance, horizon, approaching/receding | Planning horizon, technical debt (distant consequence) |
| `flow` | Continuous movement through a channel, current, throughput | Stream processing, pipeline, river |
| `blockage` | Obstruction in a flow or path, dam, bottleneck | Bottleneck, gatekeeper, writer's block |

#### Force dynamics

| Value | Felt experience | Canonical example |
|---|---|---|
| `force` | Compulsion, resistance, pressure, momentum, push/pull | Argument is war, market forces, gravitational pull |
| `balance` | Equilibrium, symmetry, tipping, counterweight | Technical debt, work-life balance, checks and balances |
| `attraction` | Pull toward, gravity, magnetism, convergence | Basin of attraction, market gravity, cultural pull |

#### Structure and composition

| Value | Felt experience | Canonical example |
|---|---|---|
| `part-whole` | Composition, membership, extraction, assembly | Mining (extract part), team as organism, modular design |
| `link` | Connection, attachment, binding, coupling | Network effects, coupling/cohesion, social bonds |
| `merging` | Two things becoming one, fusion, integration | Merge (git), cultural assimilation, synthesis |
| `splitting` | One thing becoming many, division, branching | Fork, cell division, schism |
| `scale` | More/less, up/down, gradient, magnitude | More is up, scaling, diminishing returns |

#### Transformation and change

| Value | Felt experience | Canonical example |
|---|---|---|
| `matching` | Fit, alignment, correspondence, recognition | Pattern matching, key and lock, resonance |
| `iteration` | Repeated application, refinement per pass | Sourdough folding, sword forging, sprint cycle |
| `removal` | Taking away, clearing, pruning, erosion | Refactoring, Occam's razor, pruning |
| `superimposition` | Layering, overlay, stacking, palimpsest | Geological strata, protocol stack, sword steel layers |
| `accretion` | Building up through small deposits over time | Coral reef, common law, trail-making, sedimentation |
| `self-organization` | System structures itself through internal feedback | Sourdough culture, ecosystem resilience, emergent order |

### Annotation guidance

- Tag the **structural** embodied patterns, not the surface domain.
  "Argument Is War" gets `force` and `container`, not because war
  involves force, but because the metaphor structures argument as
  *force against resistance within a bounded arena*.
- Prefer fewer, more confident tags over many speculative ones. If
  you're unsure, leave it off --- sparse correct tags beat noisy ones.
- The distinction between `flow` and `path`: flow implies continuous
  movement of a *substance* through a channel. Path implies discrete
  *movement of an agent* toward a destination. A pipeline is `flow`.
  A career is `path`. A river is both.
- `accretion` vs `accumulation` (not a separate value): accretion is
  in the vocabulary because it implies structure *emerging from*
  accumulation, not just pile-up. Technical Debt uses `scale` +
  `balance` (the accumulation tips the balance). Coral Reef uses
  `accretion` (the deposits *become* the structure).

---

## Field 2: `relation_types[]`

**Per entry: 2-4 values. All kinds.**

What the entry says one thing *does to* another. These capture the
predicate structure --- the verbs of the metaphor, not the nouns.
This is co-priority-one with embodied patterns because it's where the
"aha" retrieval results come from: matching on what things *do*
connects domains that share no surface similarity.

### Values

| Value | Meaning | Canonical example |
|---|---|---|
| `cause` | X produces/creates Y | Butterfly effect, contagion, domino effect |
| `enable` | X makes Y possible without doing Y | Scaffolding, catalyst, platform |
| `prevent` | X blocks/stops Y | Firewall, immune response, gatekeeper |
| `transform` | X changes Y into Z, state change | Alchemy, metamorphosis, refining |
| `contain` | X holds, limits, or bounds Y | Sandbox, container, echo chamber |
| `compete` | X and Y oppose each other over Z | Argument is war, natural selection, market |
| `coordinate` | X aligns Y and Z toward coherence | Orchestra conductor, ATC, weaving |
| `decompose` | X breaks Y into constituent parts | Triage, analysis, work breakdown |
| `translate` | X renders Y intelligible to Z, bridging | Rosetta stone, dendritic cell, API |
| `select` | X chooses among Y based on criteria | Natural selection, curation, triage |
| `accumulate` | X builds up over time, compounding | Technical debt, compound interest, sedimentation |
| `restore` | X returns Y to a prior or healthy state | Self-healing, homeostasis, rollback |

### Annotation guidance

- Tag the **dominant relations in the transfers**, not exhaustive ones.
  Every metaphor technically involves many relations. Pick the 2-4 that
  are structurally load-bearing.
- `translate` is the highest-signal tag for non-obvious retrieval. It
  connects Hollywood producers to dendritic cells to API gateways.
  Use it when the entry's core function is *making one domain legible
  to another*.
- `enable` vs `cause`: enablement is necessary-but-not-sufficient.
  Scaffolding *enables* construction; it doesn't *cause* the building.
  If removing X would prevent Y but X alone doesn't produce Y, that's
  `enable`.
- `select` vs `prevent`: selection implies choosing *among alternatives*.
  Prevention implies blocking a *specific* thing. A firewall `prevents`.
  Natural selection `selects`.

---

## Field 3: `structure`

**Per entry: 1-2 values. All kinds.**

The dominant topology --- the *shape* of the system the entry describes.
Coarser than embodied patterns, useful as a pre-filter for faceted
search before vector retrieval.

### Values

| Value | Shape | Canonical example |
|---|---|---|
| `hierarchy` | Tree, chain of command, ranked layers | Org chart, taxonomy, food chain |
| `network` | Web, many-to-many, distributed | Ecosystem, neural net, social graph |
| `pipeline` | Linear sequence, stages, handoffs | Assembly line, refining, CI/CD |
| `boundary` | Inside/outside, membrane, perimeter | Firewall, cell membrane, walled garden |
| `cycle` | Feedback loop, oscillation, return | Seasons, predator-prey, sprint |
| `competition` | Adversarial, zero-sum, selection pressure | War, market, tournament |
| `growth` | Expansion, branching, compounding | Organism, compound interest, viral |
| `transformation` | State change, metamorphosis, phase transition | Alchemy, chrysalis, smelting |
| `equilibrium` | Self-correcting, homeostatic, balanced | Thermostat, market clearing, homeostasis |
| `emergence` | Macro from micro, no central designer | Flocking, common law, stigmergy |

### Annotation guidance

- Most entries have one dominant structure. Use two only when the entry
  genuinely involves two topologies (e.g., an entry about "ecosystem as
  market" is `network` + `competition`).
- `pipeline` vs `cycle`: a pipeline has a beginning and end, material
  moves through once. A cycle has no endpoint, material (or the system)
  returns. A CI/CD pipeline that runs on every commit is `pipeline`
  (each run is linear). The sprint cadence is `cycle`.
- `emergence` is reserved for entries where the *absence of a designer*
  is structurally important. An ant colony is `emergence`. An assembly
  line is not, even though complex behavior arises.

---

## Field 4: `abstraction_level`

**Per entry: 1 value. All kinds.**

How broadly the entry applies. Used as a ranking signal in retrieval:
generic entries are more likely useful for novel problems, specific
entries are more vivid but narrower.

### Values

| Value | Definition | Canonical example |
|---|---|---|
| `primitive` | Near-universal, grounded in embodied experience, rarely domain-specific. Most people wouldn't even call it a "metaphor" because it's so deeply embedded in cognition. | More Is Up, Container (conceptual), Time Is Space |
| `generic` | Applicable across many target domains. The source frame is concrete but maps broadly. These are the workhorses of the catalog. | Journey, War, Machine, Ecosystem, Debt |
| `specific` | Grounded in a particular domain. Vivid and precise, but narrower applicability. The source frame requires domain knowledge to understand. | Surgery, Chess opening, Sourdough, Sword forging |

### Annotation guidance

- When in doubt between `generic` and `specific`, ask: "Could someone
  with zero domain knowledge understand the source frame?" If yes,
  `generic`. If the source frame requires knowing how chess/surgery/
  metallurgy works, `specific`.
- Most archetypes and paradigms are `generic`. Most patterns are
  `generic` or `specific`. Metaphors span all three levels.
- Mental models are almost always `generic` --- they're cognitive
  tools designed to be domain-independent.

---

## Field 5: `abstract_roles{}` (frames only)

**On frames, not entries. Map of frame-specific role -> abstract role type.**

Maps each frame's concrete roles to a small set of abstract role types.
This enables role-signature matching: two frames with the same abstract
role profile (agent, counter-agent, instrument, contested-resource) are
structurally analogous even when their domains are unrelated.

### Abstract role types (~18)

| Type | Meaning | Example mappings |
|---|---|---|
| `agent` | Entity that acts with intention | combatant, surgeon, conductor, detective |
| `counter-agent` | Entity that opposes the agent | enemy, defendant, competitor, pathogen |
| `patient` | Entity acted upon, changed by the action | patient, workpiece, audience, ore |
| `instrument` | Tool used by agent to act | weapon, scalpel, baton, reagent |
| `medium` | Substance or channel through which action flows | water, network, language, air |
| `contested-resource` | Thing competed over or extracted | territory, market share, attention, mineral |
| `goal-state` | Desired outcome | victory, health, harmony, product |
| `anti-goal-state` | Undesired outcome | defeat, death, collapse, failure |
| `obstacle` | Impediment between current state and goal | wall, illness, friction, bug |
| `path` | Route from current to goal state | road, pipeline, career ladder, channel |
| `container` | Bounded space that holds or limits | sandbox, cell, frame, arena |
| `boundary` | Edge of a container, crossing point | membrane, firewall, deadline, threshold |
| `source` | Origin of material, energy, or action | mine, spring, origin, sender |
| `product` | Result of transformation | refined metal, diagnosis, artifact, verdict |
| `catalyst` | Enables transformation without being consumed | enzyme, mentor, seed crystal, spark |
| `substrate` | Material being worked on or transformed | ore, dough, codebase, raw data |
| `signal` | Information that triggers detection or response | symptom, alert, market signal, clue |
| `coordinator` | Entity that aligns multiple agents/parts | conductor, ATC, hub, scheduler |

### Example mapping

```yaml
# catalog/frames/war.md
abstract_roles:
  combatant: agent
  enemy: counter-agent
  weapon: instrument
  territory: contested-resource
  strategy: plan        # note: 'plan' is not in the type list --
                        # this signals we may need to add it,
                        # or map it to 'instrument'
  victory: goal-state
  defeat: anti-goal-state
  casualty: patient
  ally: agent           # second agent, same type
```

### Annotation guidance

- Not every frame role maps cleanly. When a role doesn't fit any type,
  note it --- this is how the vocabulary grows. But resist adding new
  types for one-off cases.
- Some roles map to the same abstract type (combatant and ally are both
  `agent`). That's fine --- the abstract type captures structural position,
  not identity.
- The value of this mapping is in the *signature*, not individual
  mappings. A frame with `[agent, counter-agent, instrument,
  contested-resource, goal-state]` is structurally comparable to any
  other frame with the same signature, regardless of domain.

---

## Cross-kind retrieval: how the fields combine

The five fields serve different retrieval functions:

```
Query: "Find me a metaphor for a system where..."

Step 1: Extract embodied_patterns from the description
        -> narrows 900 entries to ~50-100

Step 2: Match relation_types
        -> narrows to ~10-20 (this is where "aha" results appear)

Step 3: Filter by structure
        -> narrows to ~5-10

Step 4: Rank by abstraction_level
        -> generic entries surface first for novel problems

Step 5: Cross-kind grouping
        -> assemble an "explanation stack":
           primitive metaphor (embodied intuition)
           + generic metaphor (communicable analogy)
           + pattern (actionable structure)
           + mental-model (decision framework)
           + archetype (narrative handle)
```

### Connection types enabled

| From kind | To kind | Bridge field | Example |
|---|---|---|---|
| metaphor | archetype | `embodied_patterns` | "Argument Is War" -> The Warrior (both: force + competition) |
| mental-model | metaphor | `relation_types` | Inversion of Control -> Trellis (both: enable + transform) |
| pattern | metaphor | `structure` + `relation_types` | Second-System Effect -> Technical Debt (both: cycle + accumulate) |
| archetype | mental-model | `embodied_patterns` + `structure` | The Trickster -> Lateral Thinking (both: boundary + transformation) |
| any kind | any kind | `abstract_roles` (via frame) | Same role signature connects war frame to courtroom frame to immune-response frame |

---

## Eval design

Before enriching all 900 entries, validate the vocabulary on 50 entries
using analogy triples.

### Analogy triple format

Each triple contains:
- **A** (query): an entry
- **B** (structural match): an entry from a different domain that shares
  structural shape with A. This is the *right answer*.
- **C** (topical trap): an entry from the *same domain* as A that has
  different structural shape. This is the *wrong answer* that text
  embeddings will prefer.

### Eval metric: Structural Surprise Rate

For each entry, retrieve top-10 neighbors using enriched embeddings.
Score: what fraction are (a) structurally relevant AND (b) from a
different source domain than the query?

High SSR = the system finds non-obvious connections.

### Eval sequence

1. Build 50 analogy triples from existing catalog
2. Tag the ~100-150 entries involved with all five fields
3. Baseline: embed raw transfers/limits text, score against triples
4. Enriched: embed structured representation (embodied patterns +
   relation types prepended to text), score against triples
5. If enriched significantly outperforms baseline: proceed to tag all 900
6. If not: revisit vocabulary design before scaling

### Seed triples (from brainstorm sessions)

| A (query) | B (structural match) | C (topical trap) |
|---|---|---|
| Argument Is War | Immune Response | Argument Is Journey |
| Mining | Archaeology | Gold Rush |
| Sourdough (process) | Coral Reef | Baking a Cake |
| Sword Forging | Geological Sedimentation | Blacksmithing (horseshoe) |
| Improv Theater | Common Law | Scripted Theater |
| Middle Loop Manager | Dendritic Cell | Scrum Master |
| Self-Healing System | Bone Remodeling | Auto-Scaling |
| Technical Debt | Boiling Frog | Code Smell |
| Bottleneck | Eye of the Needle | Traffic Jam |
| Natural Selection | Curation | Survival of the Fittest |

---

## Vocabulary evolution

This vocabulary is a living document. Expected changes:

- **New embodied patterns** may be needed. `accretion` and
  `self-organization` were added during brainstorming because the
  standard image-schema list didn't cover emergent-architecture
  metaphors. More gaps will surface during the 50-entry tagging pass.
- **Relation types** may need splitting. `transform` may need to
  distinguish reversible from irreversible transformation. This
  will become clear during annotation.
- **Abstract role types** will grow as more frames are mapped. The
  current 18 types cover the frames explored so far. Expect 20-25
  when all 183 frames are mapped.
- **Retirement**: values that never discriminate (appear on >80% of
  entries) should be retired or split. If everything is `force`,
  `force` isn't useful.

### Process for vocabulary changes

1. Annotator encounters a case where no existing value fits
2. Document the case and proposed value in this file
3. Check: does the proposed value appear on >= 5 existing entries?
   If not, it's too specific --- find a broader pattern.
4. Check: would the proposed value appear on > 80% of entries?
   If so, it's too general --- find a narrower distinction.
5. Add the value, update this file, re-run eval if triples exist
