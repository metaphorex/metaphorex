---
project_issue: 3
repo: metaphorex/metaphorex
source_type: book
status: draft
---

# Design Patterns as Metaphors

## Source Description

Three primary sources, all treating recurring problem/solution structures
as named patterns:

1. **Gang of Four (GoF)** -- Gamma, Helm, Johnson, Vlissides. *Design
   Patterns: Elements of Reusable Object-Oriented Software* (1994). 23
   patterns organized into Creational, Structural, and Behavioral
   categories. Each pattern name is a metaphor drawn from architecture,
   manufacturing, social roles, or physical processes.

2. **Martin Fowler** -- *Patterns of Enterprise Application Architecture*
   (2002). Architectural patterns for enterprise software. Many names are
   metaphorical (Repository, Gateway, Registry, Unit of Work).

3. **Christopher Alexander** -- *A Pattern Language* (1977). 253 patterns
   for architecture and urban planning, explicitly designed as a shared
   vocabulary. The origin of pattern languages. Several patterns have
   metaphorical names that illuminate cross-domain thinking.

The focus is on the *metaphorical structure of the pattern name* -- what
source domain does the name invoke, what does that mapping reveal, and
where does it break?

## Access Method

These are published books. The Miner should work from:

- The pattern name and its etymology
- The stated intent/problem/solution from the original source
- Common usage in developer discourse (Stack Overflow, blog posts, etc.)
- The Miner's own knowledge of these well-documented patterns

No API or scraping needed. These patterns are thoroughly documented in
secondary sources and in the Miner's training data.

## Extraction Strategy

Each pattern becomes one mapping entry. The extraction template:

1. **Identify the source domain** of the pattern name. "Observer" comes
   from surveillance/watching. "Factory" comes from manufacturing.
   "Bridge" comes from civil engineering.

2. **Map the structural parallels** -- what features of the source domain
   carry over to the software pattern, and what makes the mapping apt?

3. **Find the breaks** -- where does the metaphor mislead? This is the
   highest-value section. A "Factory" in software doesn't consume raw
   materials. An "Observer" in software doesn't have agency.

4. **Collect expressions** -- real phrases developers use that extend or
   rely on the metaphor. "The factory produces widgets" (treating objects
   as manufactured goods). "The observer is listening" (treating
   notification as perception).

5. **Determine kind** -- most GoF and Fowler patterns are
   `conceptual-metaphor`. Some Alexander patterns are `paradigm`. Patterns
   whose names are so embedded the metaphorical origin is forgotten are
   `dead-metaphor`. The only valid kinds are: `conceptual-metaphor`,
   `archetype`, `dead-metaphor`, `paradigm`.

### Prioritization

The candidates are ordered by metaphorical richness -- how much the
name reveals and hides. Patterns with bland or purely technical names
(Abstract Factory, Template Method) are still included but are lower
priority because their metaphorical content is thinner.

## Schema Mapping

### Frames needed (create if missing)

These frames may need to be created by the Miner alongside their
mapping entries:

| Frame slug | Description |
|---|---|
| manufacturing | Factories, assembly lines, production |
| civil-engineering | Bridges, structural load, foundations |
| surveillance | Observation, monitoring, watching |
| military-command | Chain of command, strategy, delegation |
| mediation | Intermediaries, brokers, go-betweens |
| publishing | Documents, templates, printing |
| governance | Registries, repositories, bureaucracy |
| theater | Proxies, stand-ins, roles |
| object-oriented-design | Classes, objects, inheritance, polymorphism |

Note: `architecture-and-building`, `software-abstraction`, `containers`,
and `social-roles` already exist and will be reused heavily.

### Categories

Existing categories that apply: `software-engineering`,
`systems-thinking`, `organizational-behavior`.

### Kind assignments

Valid kinds: `conceptual-metaphor`, `archetype`, `dead-metaphor`, `paradigm`.

- GoF patterns: `conceptual-metaphor` (they're A→B mappings with active
  source domains — calling something a "factory" still evokes manufacturing)
- GoF patterns with forgotten origins: `dead-metaphor` (e.g., Iterator,
  Singleton — most developers don't think about the source domain)
- Alexander patterns that map beyond architecture: `conceptual-metaphor`
  or `paradigm`
- Fowler patterns: `conceptual-metaphor`

## Candidates

### Already in catalog (skip)

- `the-facade-pattern` -- exists as seed entry

### GoF Creational Patterns (5)

| # | Slug | Name | Source Frame | Target Frame | Notes |
|---|---|---|---|---|---|
| 1 | the-factory-pattern | The Factory Pattern | manufacturing | object-oriented-design | Objects as manufactured goods. Rich metaphor -- production lines, assembly, raw materials. |
| 2 | the-abstract-factory-pattern | The Abstract Factory Pattern | manufacturing | object-oriented-design | Factory of factories. Meta-manufacturing. Thinner metaphor but interesting recursion. |
| 3 | the-builder-pattern | The Builder Pattern | architecture-and-building | object-oriented-design | Construction as step-by-step assembly. Blueprints, foremen, materials. |
| 4 | the-prototype-pattern | The Prototype Pattern | manufacturing | object-oriented-design | Cloning from a master copy. Prototyping in industrial design. |
| 5 | the-singleton-pattern | The Singleton Pattern | social-roles | object-oriented-design | "There can be only one." Social/mathematical uniqueness mapped to object instantiation. |

### GoF Structural Patterns (6, excluding Facade)

| # | Slug | Name | Source Frame | Target Frame | Notes |
|---|---|---|---|---|---|
| 6 | the-adapter-pattern | The Adapter Pattern | manufacturing | object-oriented-design | Electrical adapters, plug converters. Interface compatibility as physical fitting. |
| 7 | the-bridge-pattern | The Bridge Pattern | civil-engineering | object-oriented-design | Spanning two independent hierarchies. Civil engineering's most elegant metaphor. |
| 8 | the-composite-pattern | The Composite Pattern | architecture-and-building | object-oriented-design | Part-whole hierarchies. Trees, nested containers. |
| 9 | the-decorator-pattern | The Decorator Pattern | architecture-and-building | object-oriented-design | Adding ornamentation without changing structure. Interior design meets OOP. |
| 10 | the-flyweight-pattern | The Flyweight Pattern | competition | object-oriented-design | Boxing weight class -- the lightest category. Memory optimization as dieting. |
| 11 | the-proxy-pattern | The Proxy Pattern | social-roles | object-oriented-design | Stand-in, surrogate, representative. Legal/political proxies. |

### GoF Behavioral Patterns (11)

| # | Slug | Name | Source Frame | Target Frame | Notes |
|---|---|---|---|---|---|
| 12 | the-chain-of-responsibility-pattern | The Chain of Responsibility Pattern | military-command | object-oriented-design | Bureaucratic delegation. Passing the buck up the chain. |
| 13 | the-command-pattern | The Command Pattern | military-command | object-oriented-design | Orders as objects. Military command structure reified. |
| 14 | the-interpreter-pattern | The Interpreter Pattern | social-roles | object-oriented-design | Human interpreters translating between languages. |
| 15 | the-iterator-pattern | The Iterator Pattern | social-roles | object-oriented-design | Traversal as walking through a collection. Cursor, pointer, index. |
| 16 | the-mediator-pattern | The Mediator Pattern | mediation | object-oriented-design | Dispute resolution, diplomatic intermediary. |
| 17 | the-memento-pattern | The Memento Pattern | social-roles | object-oriented-design | Keepsakes, souvenirs -- capturing a moment to restore later. |
| 18 | the-observer-pattern | The Observer Pattern | surveillance | object-oriented-design | Watching, listening, subscribing. The panopticon of event systems. |
| 19 | the-state-pattern | The State Pattern | governance | object-oriented-design | State machines as political states -- transitions, territories. Thin metaphor. |
| 20 | the-strategy-pattern | The Strategy Pattern | military-command | object-oriented-design | Military/game strategy -- interchangeable battle plans. |
| 21 | the-template-method-pattern | The Template Method Pattern | publishing | object-oriented-design | Templates, fill-in-the-blanks, stencils. |
| 22 | the-visitor-pattern | The Visitor Pattern | social-roles | object-oriented-design | A guest who visits each room. Double dispatch as hospitality protocol. |

### Fowler / Architectural Patterns (5)

| # | Slug | Name | Source Frame | Target Frame | Notes |
|---|---|---|---|---|---|
| 23 | the-repository-pattern | The Repository Pattern | governance | software-abstraction | A repository is a storehouse, archive, library. Data access as curation. |
| 24 | the-gateway-pattern | The Gateway Pattern | architecture-and-building | software-abstraction | Gateways, portals, controlled entry points. |
| 25 | the-pipeline-pattern | The Pipeline Pattern | fluid-dynamics | data-processing | Unix pipes, assembly lines, oil pipelines. Data as fluid. |
| 26 | the-registry-pattern | The Registry Pattern | governance | software-abstraction | Government registries, public records. Service location as bureaucracy. |
| 27 | the-unit-of-work-pattern | The Unit of Work Pattern | manufacturing | software-abstraction | A discrete batch of work. Transactional boundaries as shift work. |

### Alexander / Cross-Domain Patterns (5)

| # | Slug | Name | Source Frame | Target Frame | Notes |
|---|---|---|---|---|---|
| 28 | pattern-language-as-shared-vocabulary | Pattern Language as Shared Vocabulary | social-behavior | collaborative-work | Alexander's core insight: patterns form a *language* for collaborative design. The meta-metaphor. |
| 29 | a-place-to-wait | A Place to Wait | architecture-and-building | software-abstraction | Alexander's pattern #150. Waiting rooms in software: loading states, queues, buffers. |
| 30 | light-on-two-sides | Light on Two Sides | architecture-and-building | creative-process | Alexander's pattern #159. Rooms need light from two directions. Ideas need multiple perspectives. |
| 31 | main-entrance | Main Entrance | architecture-and-building | software-abstraction | Alexander's pattern #110. The main entry should be obvious. API design, onboarding. |
| 32 | intimacy-gradient | Intimacy Gradient | architecture-and-building | software-abstraction | Alexander's pattern #127. Public-to-private transitions. Access control as spatial design. |

**Total: 32 candidates** (plus 1 already in catalog = 33 patterns covered)

## Gotchas

1. **The Facade Pattern already exists.** Do not create a duplicate.
   Link new entries to it via `related:` where appropriate.

2. **"Pattern" vs "metaphor" confusion.** Each entry is about the
   *metaphorical structure of the pattern name*, not about the pattern
   itself. The Miner should resist writing a pattern tutorial. The
   question is always: what does calling this a "factory" (or "bridge"
   or "observer") reveal and conceal?

3. **Thin metaphors.** Some patterns have weak metaphorical names
   (Iterator, State, Template Method). These entries will be shorter
   but should still exist -- even noting that the name is metaphorically
   thin is valuable analysis.

4. **Frame proliferation.** Many candidates share frames. The Miner
   should check what frames already exist before creating new ones.
   Prefer reusing `architecture-and-building`, `manufacturing`,
   `social-roles`, `military-command` across multiple entries.

5. **Alexander patterns are the riskiest.** The five Alexander candidates
   are cross-domain mappings that require the Miner to articulate how an
   architectural pattern illuminates software/creative work. These should
   be attempted after the GoF patterns establish the project's rhythm.

6. **Kind selection.** Most GoF patterns are `conceptual-metaphor`. But some
   names are so embedded in developer vocabulary that they function as
   dead metaphors (Iterator, Singleton). The Miner should choose
   `dead-metaphor` when the metaphorical origin is genuinely forgotten
   by most users, and `conceptual-metaphor` when the name still evokes its
   source domain. Do not use `design-pattern` or `cross-field-mapping` —
   these are not valid kinds.
