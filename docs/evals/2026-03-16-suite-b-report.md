# Eval Report: Suite B — m4x vs Raw Claude

**Date:** 2026-03-16T19:52:18.455Z
**Model:** anthropic/claude-sonnet-4
**Scenarios:** 5

## microservices-design

**Scenario:** A queue-based microservices architecture where services communicate via message brokers, with circuit breakers for failure isolation and a shared database for state.

### Search results injected

- **data-flow-is-fluid-flow** [expression] (score: 0.53): "Drain the queue" — consume pending messages as emptying a vessel
- **the-pipeline-pattern** [expression] (score: 0.52): "Streaming pipeline" -- emphasizing continuous flow over batch processing
- **data-is-fuel** [expression] (score: 0.49): "Data pipeline" -- industrial processing infrastructure for data flow
- **the-command-pattern** [expression] (score: 0.48): "Queue up commands" — batch operations, treating the command queue as a duty roster
- **the-mediator-pattern** [expression] (score: 0.47): "Message bus as mediator" — infrastructure that routes messages, the mediator scaled up
- **program-failure-is-bodily-failure** [title] (score: 0.35): Program Failure Is Bodily Failure
- **anger-is-a-heated-fluid-in-a-container** [expression] (score: 0.35): "She had a meltdown" -- emotional breakdown as thermal structural failure
- **redundancy** [transfer] (score: 0.35): **Multiple independent failure paths prevent catastrophic collapse** -- a bridge with redundant load paths can lose a ca
- **intoxication-is-becoming-electrified** [expression] (score: 0.35): "Her brain short-circuited" -- cognitive failure under intoxication as electrical overload
- **the-mind-is-a-brittle-object** [transfer] (score: 0.34): **Breaking as catastrophe** -- unlike machine failure, which can be incremental (a part wears out, a cog slips), brittle
- **the-state-pattern** [transfer] (score: 0.46): **Each state is self-contained** -- a state of governance has its own laws, customs, and internal logic. Each State subc
- **agent-swarm** [expression] (score: 0.44): "Hive mind" -- shared knowledge state across agents, borrowing from science fiction's insect-colony trope
- **the-self** [expression] (score: 0.42): "Single source of truth" -- the data architecture principle that mirrors the Self's integrating function: one authoritat
- **pattern-language-as-shared-vocabulary** [expression] (score: 0.40): "We need a common language for architecture" -- the collaboration argument, design coordination as mutual intelligibilit

### Raw Claude (no tools)

Here are the key conceptual metaphors active in this microservices architecture scenario:

## 1. SERVICES ARE AUTONOMOUS AGENTS
**Structural assumptions:** Each service is an independent entity with its own goals, capabilities, and decision-making processes. They "communicate" and "collaborate" like people in an organization.

**What it makes hard to see:** The reality that services are just code running on shared infrastructure. This metaphor can obscure resource contention, shared failure modes, and the fact that "autonomy" is limited by deployment constraints, network topology, and operational dependencies.

## 2. MESSAGES ARE PHYSICAL MAIL/PACKAGES
**Structural assumptions:** Information has weight, takes time to deliver, can get lost in transit, and requires a postal system (message broker) with sorting facilities and delivery routes.

**What it makes hard to see:** The instantaneous, copyable nature of digital information. This metaphor can lead to over-engineering delivery guarantees when simple function calls might suffice, and obscures that "message delivery" is really just memory copying and network packet transmission.

## 3. CIRCUIT BREAKERS ARE ELECTRICAL SAFETY DEVICES
**Structural assumptions:** Failures are like electrical overloads that can be detected and isolated by "tripping" a switch. The system can be "reset" once conditions normalize.

**What it makes hard to see:** That software failures often aren't binary on/off states but complex degradation patterns. This metaphor can mask cascading failures that don't follow electrical patterns, and the reality that "resetting" often requires human intervention to address root causes.

## 4. DATABASE IS A SHARED FILING CABINET/LIBRARY
**Structural assumptions:** Data is stored in organized, retrievable locations that multiple parties can access. There's a librarian (database engine) managing checkout/checkin and preventing conflicts.

**What it makes hard to see:** The fundamental tension between "microservices autonomy" and shared state. This metaphor obscures that the database becomes a coupling point that violates service independence, and that concurrent access creates complex consistency challenges that don't exist with physical filing systems.

## 5. ARCHITECTURE IS URBAN PLANNING/INFRASTRUCTURE
**Structural assumptions:** Software systems are like cities with districts (services), transportation networks (message queues), and utilities (shared databases). They can be planned, zoned, and managed like physical infrastructure.

**What it makes hard to see:** The malleability and rapid evolution possible in software. This metaphor can lead to over-rigid designs and premature optimization. Unlike cities, software can be completely restructured without physical constraints, but the metaphor encourages thinking about "migration costs" and "legacy infrastructure" that may not actually apply.

## 6. QUEUES ARE WAITING LINES
**Structural assumptions:** Work items are like people waiting in line - first come, first served, with visible length and predictable processing order.

**What it makes hard to see:** That message queues can reorder, duplicate, or lose messages in ways that physical lines cannot. This metaphor obscures the complexity of distributed systems where "fairness" and "order" are much more nuanced concepts, and where queue behavior under failure conditions differs dramatically from human queuing.

### Claude + m4x search

Looking at this microservices architecture scenario, I can identify several active conceptual metaphors beyond the catalog results:

## 1. **SERVICES ARE AUTONOMOUS AGENTS** (not in catalog)
**Structural assumptions:** Each service is an independent entity with its own goals, capabilities, and decision-making processes. They "communicate" rather than simply execute functions.

**Misleading aspects:** This obscures the fact that services are deterministic code with no actual autonomy. It can lead to over-engineering service boundaries and anthropomorphizing what are essentially function calls. The metaphor makes it harder to see when tight coupling might actually be more efficient.

## 2. **CIRCUIT BREAKERS ARE ELECTRICAL SAFETY DEVICES** (partially captured in catalog as "short-circuited")
**Structural assumptions:** System failure follows electrical principles - overload causes dangerous conditions that must be "broken" to prevent cascading damage. Failure is binary (open/closed) and protective.

**Misleading aspects:** Unlike electrical circuits, software failures often have gradual degradation patterns. The metaphor suggests that cutting connections is always protective, but it obscures scenarios where partial functionality or graceful degradation might be better than complete isolation.

## 3. **THE SHARED DATABASE IS A COMMONS** (not in catalog)
**Structural assumptions:** Data is a shared resource that multiple parties access, with potential for "tragedy of the commons" scenarios. Governance and access control become central concerns.

**Misleading aspects:** This frames data sharing as inherently problematic and emphasizes conflict over collaboration. It makes it harder to see legitimate use cases for shared state and can drive premature data partitioning that creates consistency problems.

## 4. **MESSAGE BROKERS ARE POST OFFICES** (related to catalog's "mediator" but more specific)
**Structural assumptions:** Messages have addresses, routing infrastructure, delivery guarantees, and postal-like semantics (queuing, sorting, delivery confirmation).

**Misleading aspects:** Unlike physical mail, digital messages can be copied infinitely at near-zero cost. The metaphor emphasizes delivery mechanics over content transformation and makes it harder to see opportunities for message enrichment or intelligent routing based on content.

## 5. **MICROSERVICES ARCHITECTURE IS URBAN PLANNING** (not in catalog)
**Structural assumptions:** Services are like buildings in a city - they need infrastructure (networking), zoning (service boundaries), utilities (shared services), and governance (API contracts). Growth happens through development of new "districts."

**Misleading aspects:** Cities evolve organically over decades, but software systems need rapid, coordinated changes. The metaphor suggests that service boundaries are as permanent as city blocks, making it harder to see when services should be merged or split. It also obscures the fact that software "infrastructure" can be changed much more easily than physical infrastructure.

## 6. **QUEUES ARE WAITING LINES** (from catalog but worth expanding)
**Structural assumptions:** First-in-first-out ordering, fairness through sequential processing, capacity limits create "congestion."

**Misleading aspects:** Unlike human queues, message queues can often benefit from priority ordering, parallel processing, or batch operations. The metaphor makes it harder to see opportunities for intelligent scheduling or when queue ordering doesn't actually matter for the business logic.

The most dangerous aspect across these metaphors is how they collectively frame distributed systems as collections of independent entities that must be carefully coordinated, rather than as a single logical system that happens to be physically distributed. This can lead to over-engineering of service boundaries and communication protocols when simpler, more coupled solutions might be more appropriate.

---

## fast-growing-team

**Scenario:** A startup engineering team that grew from 5 to 50 in a year. The original founders still make most technical decisions. New hires feel they can't influence architecture. Knowledge lives in people's heads, not documentation.

### Search results injected

- **the-senex** [expression] (score: 0.52): "Institutional knowledge" -- the Senex's treasure hoard: information that exists only because someone has been around lo
- **ideas-are-money** [expression] (score: 0.50): "A wealth of knowledge" -- large quantity of ideas as monetary fortune
- **the-wise-old-man** [expression] (score: 0.49): "Tribal knowledge" -- undocumented wisdom that exists only in the heads of long-tenured team members; the wise old man's
- **ant-is-pure-empiricist** [expression] (score: 0.49): "Data hoarding" -- accumulating datasets without analysis, the corporate ant colony at work
- **deep-magic** [transfer] (score: 0.45): **Knowledge as power, and power as dangerous** -- in mythological traditions, magical knowledge is both potent and hazar
- **nation-is-a-family** [expression] (score: 0.53): "The founding fathers" -- national founders as patriarchal ancestors
- **excalibur** [limit] (score: 0.47): **Legitimacy-by-artifact concentrates power dangerously** -- the Excalibur model implies that exactly one person is righ
- **relationship-is-kinship** [expression] (score: 0.45): "The founding fathers of the nation" -- political founders as family patriarchs (American political discourse)
- **software-development-is-cathedral-building** [transfer] (score: 0.42): **Architect as visionary authority** -- one person (or a small committee) controls the design. Contributors don't negoti
- **power-laws** [transfer] (score: 0.41): **Concentration is the default, not the exception** -- in power-law domains, most of the value, risk, or activity is con
- **ideas-are-writing** [limit] (score: 0.42): **The metaphor privileges literate cultures** -- "the writing is on the wall" assumes a world where writing is the prima
- **existence-is-life** [expression] (score: 0.38): "The tradition lives on" -- continued existence as biological life
- **beliefs-are-possessions** [expression] (score: 0.38): "They treasure that tradition" -- valuing a belief as valuing a possession
- **existence-is-a-location** [expression] (score: 0.36): "The tradition has disappeared" -- ceasing to exist as vanishing from a location

### Raw Claude (no tools)

Here are the key conceptual metaphors operating in this scenario:

## 1. KNOWLEDGE IS PROPERTY
**Structural assumptions:** Information can be owned, hoarded, or distributed. People "possess" knowledge and can choose whether to share it. Knowledge has scarcity dynamics.
**Misleading aspects:** This obscures how knowledge actually grows through sharing and collaboration. It frames documentation as "giving away" something valuable rather than creating organizational capability. Makes knowledge seem finite when it's actually generative.

## 2. ORGANIZATION IS FAMILY
**Structural assumptions:** The founders are "parents" with natural authority. Early employees are "older siblings" with inherited status. New hires are "children" who should respect hierarchy and wait their turn to contribute meaningfully.
**Misleading aspects:** Hides that organizations need merit-based influence systems, not kinship-based ones. Makes questioning authority seem like rebellion rather than professional responsibility. Obscures how family dynamics don't scale past intimate group sizes.

## 3. TECHNICAL DECISIONS ARE TERRITORY
**Structural assumptions:** Architecture choices represent controlled space that can be defended or invaded. Decision-making authority is about holding ground. Multiple people influencing decisions means "territorial disputes."
**Misleading aspects:** Frames collaboration as conflict rather than collective problem-solving. Makes founders see input as threats to their domain rather than valuable perspectives. Obscures how distributed decision-making can improve technical outcomes.

## 4. SCALING IS MECHANICAL ASSEMBLY
**Structural assumptions:** Growth means adding interchangeable parts (people) to an existing machine (the team). The original design should accommodate new components without fundamental changes.
**Misleading aspects:** Ignores that human systems require structural adaptation as they grow. Makes founders think they can maintain the same processes and communication patterns. Obscures how organizational complexity increases exponentially, not linearly.

## 5. INSTITUTIONAL MEMORY IS ARCHAEOLOGICAL ARTIFACT
**Structural assumptions:** Important knowledge exists as buried treasure in founders' minds. Accessing it requires "excavation" through the right people. Documentation is like creating museum displays of these artifacts.
**Misleading aspects:** Frames knowledge as static historical objects rather than living, evolving understanding. Makes documentation seem like preservation rather than active knowledge creation. Obscures how undocumented knowledge becomes distorted and incomplete over time.

## 6. INFLUENCE IS HYDRAULIC PRESSURE
**Structural assumptions:** There's a fixed amount of decision-making power that flows through organizational channels. If new people gain influence, founders must lose it. Authority operates like water pressure - it can only flow one direction at a time.
**Misleading aspects:** Hides how good decision-making can actually increase total organizational capability rather than redistributing fixed power. Makes collaboration seem zero-sum. Obscures how expertise-based influence can coexist with positional authority.

### Claude + m4x search

Based on the scenario and catalog results, here are the key metaphors at work:

## 1. ORGANIZATION IS A FAMILY (from catalog: "nation-is-a-family")
**Structural assumptions:** Founders are parental figures with natural authority; newer members are children who should defer to elders; hierarchy is based on "bloodline" (founding status) rather than merit.
**What it obscures:** This makes it hard to see that organizational authority could be based on expertise, democratic processes, or rotating leadership. It naturalizes founder privilege and makes challenging decisions feel like rebellion against family.

## 2. KNOWLEDGE IS TREASURE/WEALTH (from catalog: "ideas-are-money," "the-senex")
**Structural assumptions:** Information can be hoarded, owned, and gives power to its possessor; sharing knowledge means losing competitive advantage; knowledge scarcity creates value.
**What it obscures:** Knowledge actually grows when shared and becomes more valuable through collaboration. This metaphor prevents seeing documentation and knowledge transfer as wealth multiplication rather than wealth redistribution.

## 3. TECHNICAL ARCHITECTURE IS CATHEDRAL BUILDING (from catalog: "software-development-is-cathedral-building")
**Structural assumptions:** One master architect has the grand vision; workers implement without questioning the design; the structure must be planned from the beginning by a single mind.
**What it obscures:** Software can be grown organically, refactored continuously, and designed collaboratively. This metaphor makes distributed decision-making seem chaotic rather than potentially superior.

## 4. STARTUP GROWTH IS BIOLOGICAL EVOLUTION (not in catalog)
**Structural assumptions:** Organizations naturally develop complexity; early adaptations become permanent features; "DNA" (founding culture) determines future form; change happens gradually through selection pressure.
**What it obscures:** Organizations can be consciously redesigned at any point. This metaphor makes intentional restructuring seem "unnatural" and suggests that current dysfunction is just a temporary growing pain rather than a design choice.

## 5. COMPANY CULTURE IS TRIBAL INHERITANCE (from catalog: "the-wise-old-man," "tribal knowledge")
**Structural assumptions:** Wisdom passes from elders to newcomers through oral tradition; cultural knowledge is sacred and shouldn't be written down; outsiders must earn the right to receive secrets.
**What it obscures:** Explicit processes and documentation can be more reliable than human memory. This metaphor makes systematization seem like cultural destruction rather than organizational maturation.

## 6. TECHNICAL DECISIONS ARE ROYAL DECREES (from catalog: "excalibur")
**Structural assumptions:** Legitimate authority comes from a special relationship to the "true" technical vision; only the chosen few can make real decisions; questioning authority threatens the entire system.
**What it obscures:** Technical decisions can be made democratically, through expertise-based consensus, or rotated among team members. This metaphor prevents seeing distributed decision-making as potentially more robust than centralized control.

The most dangerous aspect is how these metaphors reinforce each other—family hierarchy justifies knowledge hoarding, which enables royal decree-making, all disguised as natural evolution rather than conscious organizational choices.

---

## permissions-system

**Scenario:** We're designing a permissions system. Users have 'roles' that 'grant' them 'access' to 'resources'. Admins can 'delegate' permissions. There's an 'audit trail' of who 'gave' what access to whom.

### Search results injected

- **activities-are-containers** [title] (score: 0.58): Activities Are Containers
- **obligations-are-containers** [title] (score: 0.52): Obligations Are Containers
- **abilities-are-entities-inside-a-person** [limit] (score: 0.51): **Not all abilities are individual** -- some capacities are distributed across groups, tools, or environments. A person'
- **action-is-control-over-possessions** [transfer] (score: 0.48): **Capability as possession** -- "She has the skills." "He's got what it takes." "They possess the means." The resources 
- **foundation-model-is-a-foundation** [expression] (score: 0.47): "Foundational capabilities" -- attributing base-level competencies to the model using the architectural frame
- **beliefs-are-possessions** [expression] (score: 0.61): "I'll grant you that point" -- conceding in argument as transferring a possession
- **possessing-is-holding** [title] (score: 0.55): Possessing Is Holding
- **opportunities-are-objects** [transfer] (score: 0.54): **Possession as having a chance** -- "He has a great opportunity." "She was given the chance of a lifetime." "They hande
- **emotional-intimacy-is-physical-closeness** [expression] (score: 0.51): "She let him in" -- emotional vulnerability as granting physical access
- **organization-is-physical-structure** [expression] (score: 0.57): "Top-down management" -- authority direction as spatial direction
- **the-chain-of-responsibility-pattern** [transfer] (score: 0.55): **Authority accumulates up the chain** — higher ranks have more power. Handlers later in the chain often have broader ca
- **having-control-is-up** [expression] (score: 0.54): "Upper management" -- organizational authority as altitude
- **comparative-advantage** [transfer] (score: 0.51): **It justifies delegation and trust** -- the model provides a rational basis for letting someone less skilled than you h
- **ai-is-an-agent** [transfer] (score: 0.50): **Delegated authority** -- an agent acts within scope granted by the principal. You tell your real estate agent "find me

### Raw Claude (no tools)

Here are the key conceptual metaphors active in this permissions system design:

## 1. PERMISSIONS ARE PHYSICAL OBJECTS
**Structural assumptions:** Permissions can be possessed, transferred, stored, and counted like tangible items. They have discrete boundaries and can be "given" or "taken away."
**Misleading aspects:** This obscures that permissions are really relationships and contexts. It makes it hard to see permissions as dynamic, contextual, or conditional. You can't easily model "permission that expires when project ends" or "access that depends on current workload."

## 2. ACCESS IS SPATIAL MOVEMENT
**Structural assumptions:** Resources exist in bounded spaces that users move "into" or are "blocked from." Access control is like checkpoint security - you're either inside or outside.
**Misleading aspects:** This binary thinking misses graduated access, contextual visibility, or collaborative spaces. It's hard to design for "can see but not modify" or "can access during business hours only" when thinking spatially.

## 3. ROLES ARE CONTAINERS
**Structural assumptions:** Users "have" roles that "contain" permissions. Roles are discrete buckets that hold capabilities.
**Misleading aspects:** This makes it difficult to model overlapping responsibilities, temporary role changes, or context-dependent authority. Real organizational roles are fluid and situational, not fixed containers.

## 4. DELEGATION IS FEUDAL HIERARCHY
**Structural assumptions:** Authority flows downward through chains of command. Higher-level admins "grant" powers to subordinates, creating tree-like power structures.
**Misleading aspects:** This obscures peer-to-peer collaboration, temporary project leadership, or expertise-based authority. It's hard to model "junior developer who becomes tech lead for this specific feature."

## 5. AUDIT TRAILS ARE BREADCRUMBS/PATHS
**Structural assumptions:** Actions leave traces that can be "followed" linearly backward through time to reconstruct "what happened."
**Misleading aspects:** This linear narrative thinking misses the complex web of influences, parallel processes, and emergent behaviors. It's hard to capture "permission was technically granted by Alice but really decided by team consensus" or understand systemic patterns vs. individual actions.

## 6. SECURITY IS FORTRESS DEFENSE
**Structural assumptions:** There are "attackers" trying to "breach" defenses. Security means building higher walls and stronger gates.
**Misleading aspects:** This adversarial framing makes it hard to design for legitimate edge cases, user convenience, or collaborative workflows. It emphasizes keeping people out rather than enabling appropriate access.

### Claude + m4x search

Looking at this permissions system scenario, I can identify several conceptual metaphors that shape how we think about access control:

## 1. PERMISSIONS ARE POSSESSIONS (from catalog)
**Source:** "action-is-control-over-possessions" and "beliefs-are-possessions"
**Structural assumptions:** Permissions can be owned, transferred, given, and taken away like physical objects. They exist as discrete entities that can be counted and inventoried.
**Misleading aspects:** This obscures that permissions are really relationships between users and resources, not things. It makes us think permissions can be "lost" or "stolen" rather than revoked through policy changes. It also suggests scarcity where none exists—digital permissions aren't depleted when shared.

## 2. ORGANIZATIONAL AUTHORITY IS VERTICAL SPACE (from catalog)
**Source:** "having-control-is-up" and "organization-is-physical-structure"
**Structural assumptions:** Higher roles have more power, authority flows downward, delegation moves permissions "down" the hierarchy.
**Misleading aspects:** This vertical metaphor obscures lateral authority relationships and cross-functional permissions. It makes peer-to-peer delegation seem unnatural and reinforces rigid hierarchical thinking when modern organizations often need more flexible, network-based authority structures.

## 3. ACCESS IS PHYSICAL ENTRY (not in catalog)
**Structural assumptions:** Resources are like rooms or buildings with doors, permissions are like keys, and using a resource is like entering a space.
**Misleading aspects:** This makes us think about binary in/out access when many digital resources support graduated levels of interaction. It also suggests that "being inside" a resource is a persistent state, when digital access is often transactional and contextual.

## 4. AUDIT TRAILS ARE PATHS THROUGH LANDSCAPE (not in catalog)
**Structural assumptions:** Actions leave traces like footprints, investigations follow these traces like tracking, and security incidents are like following a trail to find what happened.
**Misleading aspects:** This linear path metaphor obscures the multidimensional, networked nature of digital interactions. It suggests audit data naturally forms coherent narratives when it's often fragmented and requires interpretation. It also implies that all significant actions leave visible traces.

## 5. ROLES ARE CONTAINERS (from catalog - "activities-are-containers")
**Structural assumptions:** Permissions are objects inside role-containers, users can be "in" or "out" of roles, and roles can be "filled" or "empty."
**Misleading aspects:** This makes role inheritance and composition awkward to think about—how do you put one container inside another? It also suggests roles are static boundaries when they're often dynamic collections of capabilities that should adapt to context.

## 6. DELEGATION IS GIFT-GIVING (not in catalog)
**Structural assumptions:** Authority is something valuable that can be bestowed, delegation creates obligation/gratitude relationships, and delegated authority can be "taken back."
**Misleading aspects:** This personal, social metaphor obscures the systematic, policy-driven nature of organizational delegation. It makes temporary, conditional delegation seem like permanent transfers and introduces emotional dynamics (gratitude, obligation) into what should be procedural relationships.

## 7. SECURITY IS FORTRESS DEFENSE (not in catalog)
**Structural assumptions:** Resources are territories to be defended, unauthorized access is invasion, and security measures are walls/barriers.
**Misleading aspects:** This adversarial metaphor makes collaboration and information sharing seem inherently risky. It emphasizes keeping threats "out" rather than managing trusted relationships "in." It also suggests security is about building higher walls rather than intelligent, adaptive responses to context.

The most problematic aspect across these metaphors is how they collectively reinforce a worldview where digital permissions work like physical objects and spaces, when they're actually dynamic relationships that could be much more fluid and context-aware.

---

## ml-model-opacity

**Scenario:** A machine learning model has been retrained on production data so many times that nobody understands why it makes specific decisions. The team calls it 'the black box' and treats its outputs as 'predictions' that need 'confidence scores'.

### Search results injected

- **ai-is-a-black-box** [transfer] (score: 0.62): **Opacity as a container property** -- the box is sealed. You cannot open it, peer inside, or disassemble it while it ru
- **ai-is-an-oracle** [transfer] (score: 0.50): **Opacity of process** -- nobody at Delphi knew how the Pythia's utterances were generated. The process was sacred, hidd
- **darkness-is-a-solid** [expression] (score: 0.48): "Solid black" -- darkness with the completeness and opacity of a solid body
- **ai-is-an-iceberg** [limit] (score: 0.47): **The binary visible/hidden split is too clean** -- an iceberg has a sharp waterline. AI infrastructure exists on a grad
- **gordian-knot** [transfer] (score: 0.55): **The oracle legitimizes the result** -- the prophecy said the person who loosened the knot would rule Asia. Alexander d
- **scenario-analysis** [transfer] (score: 0.45): **Triggers, not predictions** -- each scenario includes early indicators that signal which future is unfolding. The mili
- **properties-are-possessions** [transfer] (score: 0.49): **Quantity and degree** -- "She has a lot of courage." "He has very little patience." The possession frame quantifies pr
- **comparison-of-properties-is-comparison-of-possessions** [transfer] (score: 0.48): **Quantity as amount possessed** -- comparing qualities becomes comparing quantities of stuff. She has *more* courage. H
- **checklist-approach** [transfer] (score: 0.44): **Forcing functions against overconfidence** -- the checklist is a structural remedy for a psychological problem. Experi
- **understanding-is-grasping** [limit] (score: 0.43): **Firmness of grasp conflates confidence with accuracy** -- "a firm grasp" of the material suggests both confidence and 
- **ai-is-an-intern** [transfer] (score: 0.43): **Confident beyond competence** -- interns often do not know what they do not know. They deliver work with the confidenc

### Raw Claude (no tools)

Here are the key conceptual metaphors operating in this scenario:

## 1. MODEL IS A BLACK BOX
**Structural assumptions:** The model is a container with opaque walls where inputs go in and outputs come out, but the internal mechanisms are hidden from view. This implies a clear boundary between "inside" (unknowable) and "outside" (observable).

**Misleading aspects:** This metaphor obscures that ML models are actually mathematical functions with discoverable patterns. It discourages investigation into interpretability techniques and makes the inscrutability seem like a fundamental property rather than a current limitation of tools and methods.

## 2. MODEL OUTPUTS ARE PREDICTIONS
**Structural assumptions:** The model is a fortune-teller or oracle that can see into the future. This implies the model has genuine foresight and that its outputs represent actual future states rather than statistical patterns from past data.

**Misleading aspects:** This hides that models are pattern-matching systems making educated guesses based on historical correlations. It can lead to over-reliance on outputs and insufficient consideration of distribution shift, where future data differs from training data.

## 3. CONFIDENCE IS EMOTIONAL CERTAINTY
**Structural assumptions:** The model has psychological states and can feel more or less sure about its answers, similar to human confidence. Higher scores indicate the model "believes" more strongly in its output.

**Misleading aspects:** This anthropomorphizes what are actually mathematical uncertainty estimates or calibration scores. It obscures that "confidence" might reflect training data density rather than actual reliability, and can mask systematic biases in uncertainty estimation.

## 4. RETRAINING IS EDUCATION/LEARNING
**Structural assumptions:** The model is a student that accumulates knowledge over time through repeated exposure to lessons (data). Each retraining session adds to its understanding like a human learning process.

**Misleading aspects:** This hides that retraining often involves catastrophic forgetting, where new data can overwrite previous patterns rather than building on them. It also obscures the non-linear, sometimes chaotic nature of how neural networks change with new data.

## 5. PRODUCTION DATA IS NATURAL HABITAT
**Structural assumptions:** Production data represents the model's "natural environment" where it should thrive and perform optimally. Training on this data is like adapting an organism to its ecosystem.

**Misleading aspects:** This obscures that production data may contain feedback loops, biases, and artifacts created by the model's own previous decisions. The model may be learning to perpetuate its own errors rather than improving, creating a kind of "digital inbreeding" that the habitat metaphor makes invisible.

## 6. UNDERSTANDING IS VISUAL PENETRATION
**Structural assumptions:** Knowledge about the model's decision-making is like having clear sight into a physical space. "Nobody understands" implies there's something to be seen that current vision cannot penetrate.

**Misleading aspects:** This suggests understanding is binary (you either see or you don't) rather than multifaceted. It may discourage partial interpretability approaches and implies that full transparency is the only valuable form of model understanding.

### Claude + m4x search

Looking at this scenario, I can identify several active conceptual metaphors beyond the catalog results:

## 1. **AI IS A BLACK BOX** (from catalog)
**Structural assumptions:** The model is a sealed container where internal processes are completely hidden from view. Knowledge is either fully accessible or completely opaque.
**Misleading aspects:** This binary view obscures the fact that ML interpretability exists on a spectrum. It discourages investigation into partial explanations, feature importance, or model archaeology techniques that could provide some insight.

## 2. **PREDICTIONS ARE PROPHECIES** (related to ai-is-an-oracle from catalog)
**Structural assumptions:** The model delivers pronouncements about the future that should be received rather than questioned. The process of generation is mystical and beyond human comprehension.
**Misleading aspects:** Frames model outputs as inevitable truths rather than probabilistic estimates based on training data patterns. Obscures the fact that "predictions" are really pattern matching against historical data.

## 3. **CONFIDENCE IS POSSESSION** (from catalog: properties-are-possessions)
**Structural assumptions:** Confidence is a quantifiable substance that can be measured, compared, and attached to outputs. More confidence means better predictions.
**Misleading aspects:** Conflates model calibration with actual accuracy. A model can be confidently wrong, and confidence scores often reflect training data density rather than true uncertainty about the real world.

## 4. **MODEL EVOLUTION IS BIOLOGICAL EVOLUTION** (not in catalog)
**Structural assumptions:** The model "evolves" through retraining cycles, becoming more adapted to its environment (production data). This process is natural and beneficial.
**Misleading aspects:** Unlike biological evolution, ML model changes can be catastrophic rather than gradual. There's no inherent fitness function ensuring improvement. The model might be "evolving" toward overfitting or bias amplification.

## 5. **UNDERSTANDING IS ARCHAEOLOGICAL EXCAVATION** (not in catalog)
**Structural assumptions:** The model's decision-making logic is buried beneath layers of training iterations. Understanding requires careful digging through historical layers to uncover artifacts of reasoning.
**Misleading aspects:** Suggests that the "original" logic is still intact somewhere beneath the surface, when repeated retraining may have fundamentally altered or destroyed earlier decision patterns. The metaphor implies understanding is just a matter of effort rather than fundamental opacity.

## 6. **THE TEAM IS A CARGO CULT** (not in catalog)
**Structural assumptions:** The team performs rituals (retraining, confidence scoring) that once produced good results, but they've lost understanding of why these practices work.
**Misleading aspects:** Frames the situation as temporary ignorance rather than systematic technical debt. Suggests the solution is recovering lost knowledge rather than rebuilding with interpretability in mind.

## 7. **PRODUCTION DATA IS FOOD** (not in catalog)
**Structural assumptions:** The model "feeds" on production data, growing stronger and more capable with each meal. More data is always better nutrition.
**Misleading aspects:** Obscures data quality issues, distribution shift, and the possibility that production data contains feedback loops or biases that make the model worse. The model might be "eating" its own outputs or consuming poisoned data.

The most dangerous metaphor here might be **PREDICTIONS ARE PROPHECIES** because it encourages passive acceptance of model outputs rather than critical evaluation, especially problematic when the model's reasoning has become opaque through repeated retraining.

---

## code-review-as-war

**Scenario:** A team's code review process has become adversarial. Reviewers 'attack' PRs, authors 'defend' their decisions, people 'pick their battles' about which comments to address. Senior engineers use reviews to 'assert dominance'. New hires are afraid to submit PRs.

### Search results injected

- **theoretical-debate-is-competition** [limit] (score: 0.59): **Competition requires opponents; inquiry does not** -- the metaphor forces intellectual work into an adversarial frame 
- **love-is-war** [limit] (score: 0.57): **Competition crowds out cooperation** -- the metaphor makes every interaction a potential power play. "Who wears the pa
- **competition-is-war** [transfer] (score: 0.56): **Competitors are combatants** -- market rivals become adversaries locked in conflict. "They're battling for market shar
- **conducting-research-is-solving-a-puzzle** [limit] (score: 0.56): **Collaboration is awkward in the puzzle frame** -- puzzles are typically solo activities. The metaphor does not natural
- **competition-is-1-on-1-physical-aggression** [limit] (score: 0.56): **The metaphor erases cooperation within competition** -- even direct competitors cooperate on standards, shared infrast
- **argument-is-war** [expression] (score: 0.65): "She attacked every point I made" — critique as assault
- **words-are-weapons** [expression] (score: 0.56): "A barrage of criticism" -- sustained verbal attack as artillery fire
- **difficult-subjects-are-adversaries** [expression] (score: 0.52): "Attacking the reading list" -- beginning study as an offensive action
- **ideas-are-objects** [expression] (score: 0.51): "She picked apart his argument" -- critique as physical disassembly
- **problem-is-a-constructed-object** [expression] (score: 0.48): "Take apart the argument piece by piece" -- analytical critique as physical disassembly (conventional English)
- **the-chain-of-responsibility-pattern** [transfer] (score: 0.50): **Authority accumulates up the chain** — higher ranks have more power. Handlers later in the chain often have broader ca
- **having-control-is-up** [transfer] (score: 0.48): **Physical dominance** -- the grounding is bodily. In physical combat, the winner ends up on top, the loser on the botto
- **good-is-up** [limit] (score: 0.47): **Cultural asymmetries** -- while some form of vertical evaluation appears widespread, the specific content varies. In s
- **feedback-loops** [transfer] (score: 0.44): **Loop dominance shifts** -- complex systems contain multiple feedback loops. Which loop dominates determines the system

### Raw Claude (no tools)

Here are the key conceptual metaphors active in this scenario:

## 1. CODE REVIEW IS WARFARE
**Structural assumptions:** Reviews involve opposing sides with conflicting interests. There are attackers and defenders, victories and defeats. Territory must be defended or conquered. Strategic thinking involves choosing which "battles" to fight.

**What it makes hard to see:** Code review as collaborative problem-solving. The shared goal of improving code quality. The possibility that both reviewer and author can "win" simultaneously through better code.

## 2. CODE IS PERSONAL TERRITORY
**Structural assumptions:** Code belongs to its author like land belongs to an owner. Criticism of code is invasion or trespassing. Authors have property rights that must be defended against encroachment.

**What it makes hard to see:** Code as a shared team asset. The temporary, evolving nature of code. How criticism of code is separate from criticism of the person who wrote it.

## 3. SENIORITY IS DOMINANCE HIERARCHY
**Structural assumptions:** Engineering teams operate like animal hierarchies where higher-ranked individuals assert control over lower-ranked ones. Status must be displayed and maintained through shows of power.

**What it makes hard to see:** Seniority as mentorship responsibility. Knowledge-sharing as the primary value of senior engineers. How technical discussions can be separate from status negotiations.

## 4. TECHNICAL FEEDBACK IS PERSONAL ATTACK
**Structural assumptions:** Suggestions for code changes are aggressive actions directed at the person, not the code. Receiving feedback requires defensive responses to protect oneself from harm.

**What it makes hard to see:** Feedback as information transfer. The distinction between critiquing work and critiquing the worker. How vulnerability and learning require openness to criticism.

## 5. ENGINEERING SKILL IS FIXED REPUTATION
**Structural assumptions:** Technical ability is a permanent characteristic that can be damaged by making mistakes publicly. Each PR submission risks "reputation damage" that accumulates over time.

**What it makes hard to see:** Skill as continuously developing through practice and feedback. Mistakes as learning opportunities rather than permanent marks. How psychological safety enables faster skill development.

## 6. CODE REVIEW IS JUDICIAL PROCEEDING
**Structural assumptions:** There's an objective "right" answer that must be determined through adversarial argument. Reviewers act as judges rendering verdicts. Authors must present their case and accept the court's decision.

**What it makes hard to see:** Multiple valid approaches to solving problems. The collaborative exploration of trade-offs. How context and team preferences matter more than abstract "correctness."

### Claude + m4x search

Based on the scenario and catalog results, here are the key metaphors at work:

## 1. **ARGUMENT IS WAR** (from catalog)
**Structural assumptions:** Code reviews are battles with winners/losers. Reviewers are attackers, authors are defenders. Comments are weapons/attacks that must be repelled or surrendered to.

**What it makes hard to see:** Code review as collaborative learning. The possibility that both reviewer and author can be simultaneously right about different aspects. That "losing" a point might actually improve the code.

## 2. **ORGANIZATIONAL HIERARCHY IS PHYSICAL DOMINANCE** (related to catalog's "having-control-is-up")
**Structural assumptions:** Senior engineers naturally "dominate" through reviews because rank equals physical/social dominance. Submission of code for review is an act of vulnerability that invites dominance displays.

**What it makes hard to see:** Seniority as responsibility to mentor rather than opportunity to dominate. That expertise should serve the codebase, not establish pecking order.

## 3. **CODE QUALITY IS TERRITORIAL CONTROL** (not in catalog)
**Structural assumptions:** Each PR represents an attempt to claim territory in the codebase. Reviews are border disputes. Authors must "defend their territory" while reviewers "patrol the boundaries" of acceptable code.

**What it makes hard to see:** The codebase as shared commons that everyone is collectively stewarding. That allowing changes doesn't mean losing control—it means the shared resource is improving.

## 4. **PROFESSIONAL REPUTATION IS FRAGILE OBJECT** (not in catalog)
**Structural assumptions:** Each code submission risks "breaking" one's reputation. Criticism "damages" professional standing. New hires have "fragile" reputations that can be "shattered" by harsh reviews.

**What it makes hard to see:** Reputation as something built through learning and growth, including from mistakes. That showing vulnerability and learning publicly can actually enhance rather than damage professional standing.

## 5. **CODE REVIEW IS PERFORMANCE/THEATER** (not in catalog)
**Structural assumptions:** Reviews happen "on stage" with an audience. Senior engineers "perform dominance" for observers. Authors must "perform competence" or face public humiliation. Comments are "lines" delivered for dramatic effect.

**What it makes hard to see:** Code review as private conversation between collaborators focused on the work itself. That the primary audience should be future maintainers of the code, not current observers of the review process.

## 6. **TECHNICAL DECISIONS ARE PERSONAL IDENTITY** (not in catalog)
**Structural assumptions:** Code choices reflect the author's core identity. Criticizing code is criticizing the person. Authors must "defend" not just their technical choices but their sense of self.

**What it makes hard to see:** Technical decisions as provisional, contextual choices that can be improved without reflecting on anyone's worth. That changing one's mind based on new information is a professional strength, not personal weakness.

---

