---
author: agent:metaphorex-miner
categories:
- ai-discourse
- software-engineering
contributors: []
created: '2026-03-13'
harness: Claude Code
kind: archetype
name: Gas Town
related:
- ralph-wiggum-loop
- ai-is-an-agent
- ai-is-a-tool
slug: gas-town
source_frame: governance
target_frame: artificial-intelligence
updated: '2026-03-13'
---

## What It Brings

Steve Yegge's Mad Max-inspired architecture for multi-agent AI systems.
In Gas Town, autonomous agents are citizens of a post-apocalyptic
settlement, each with a role in a civic hierarchy. The metaphor maps the
full apparatus of town governance -- a mayor who coordinates, a deacon
who schedules, rigs that transport work, and a refinery that processes
raw material -- onto the orchestration layer that manages multiple AI
agents working on a shared task.

This is not a loose analogy. Yegge's original system uses the Mad Max
vocabulary as its literal API: the orchestrator is the Mayor, task
queues are Rigs, the scheduler is the Deacon, and the processing
pipeline is the Refinery. The metaphor is the architecture.

Key structural parallels:

- **Mayor as orchestrator** -- the Mayor does not do the work. The Mayor
  decides which citizen handles which task, resolves disputes, and
  maintains the big picture. This maps onto the coordinator agent in
  multi-agent systems: the component that decomposes tasks, assigns them
  to specialist agents, and integrates their outputs. The civic metaphor
  makes the coordinator's authority legible without implying omniscience.
- **Citizens as specialist agents** -- each citizen has a role (mechanic,
  scout, trader) and operates semi-autonomously within it. The metaphor
  makes agent specialization feel natural: just as a town needs both a
  blacksmith and a doctor, an agent system needs both a coder and a
  reviewer. No citizen does everything; no agent should either.
- **Rigs as task transport** -- in Mad Max, rigs are armored vehicles that
  move resources between settlements. In Gas Town, rigs carry tasks
  between agents. The metaphor makes the message-passing layer concrete
  and dramatic: tasks are not abstract data structures but cargo that
  must be protected, routed, and delivered.
- **The Refinery as processing pipeline** -- raw material goes in, refined
  product comes out. The refinery maps onto the pipeline that transforms
  raw agent outputs (drafts, partial results, intermediate reasoning)
  into polished final products. The metaphor imports industrial process
  logic: stages, quality control, throughput.
- **Post-apocalyptic scarcity as resource constraint** -- the Mad Max
  setting is defined by scarcity: fuel, water, safety are all limited.
  This maps onto the real constraints of agent systems: API rate limits,
  context window sizes, token budgets, and latency. The wasteland
  metaphor makes resource management feel urgent rather than merely
  technical.

## Where It Breaks

- **Towns have persistent inhabitants; agent systems may not** -- in a
  town, citizens have continuous existence, memory, and relationships.
  Most current agent systems instantiate agents per-task and discard
  them when done. The town metaphor imports an assumption of persistence
  and accumulated relationships that does not match the stateless
  reality of most agent orchestration frameworks. Agents do not "know"
  each other across sessions the way townsfolk do.
- **Governance implies consent and legitimacy** -- a town's governance
  derives from the consent (or at least the acquiescence) of its
  citizens. In an agent system, the orchestrator has absolute authority
  because a human programmed it that way. The civic metaphor adds a
  layer of political legitimacy that obscures the purely hierarchical
  reality: the Mayor is not elected, and agents cannot rebel.
- **The Mad Max frame romanticizes dysfunction** -- Mad Max is a story
  about civilization after collapse. Mapping agent orchestration onto a
  post-apocalyptic wasteland implies that the current state of AI
  tooling is a chaotic frontier -- exciting, dangerous, and lawless.
  This framing is appealing to early adopters but may normalize
  instability and discourage the kind of boring reliability engineering
  that mature systems need.
- **The metaphor is author-bound** -- Gas Town is Steve Yegge's creation,
  tied to his specific implementation and aesthetic. Unlike "pipeline"
  or "workflow," it does not generalize easily across different teams
  and cultures. A team that adopts Gas Town vocabulary is adopting
  Yegge's worldview along with his architecture, which limits the
  metaphor's reach as a shared industry vocabulary.
- **Civic complexity exceeds orchestration complexity** -- real towns have
  economies, cultures, conflicts, generational change, and emergent
  social phenomena. Agent orchestration systems have task queues,
  routing logic, and error handling. The governance metaphor is far
  richer than what it maps onto, and the unused complexity creates
  false expectations about agent system capabilities.

## Expressions

- "The Mayor" -- the orchestrator agent that coordinates all others
- "Rigs" -- task transport units moving work between agents
- "The Deacon" -- the scheduler that prioritizes and sequences work
- "The Refinery" -- the processing pipeline that transforms raw output
  into finished product
- "Citizens" -- specialist agents with defined roles in the system
- "Welcome to Gas Town" -- Yegge's introductory framing, establishing the
  post-apocalyptic setting for agent work
- "Vibecoding" -- associated term for the programming style Gas Town
  enables, where developers describe intent and agents write code

## Origin Story

Steve Yegge published "Welcome to Gas Town" on Medium in early 2025,
introducing a Mad Max-themed framework for multi-agent AI orchestration.
Yegge, known for his long-form technical essays and his tenure at Google
and Amazon, chose the post-apocalyptic metaphor deliberately: it captured
the chaotic, resource-constrained, frontier feeling of working with AI
agent systems in their early days.

Maggie Appleton's design analysis at maggieappleton.com/gastown extended
the metaphor, examining Gas Town's architectural patterns, bottlenecks,
and its relationship to vibecoding -- the emerging practice of
programming through natural language intent rather than explicit code.

The Gas Town archetype sits in a lineage of named software patterns that
use vivid narrative metaphors: the Gang of Four patterns (Factory,
Observer, Singleton), Martin Fowler's refactoring catalog (Shotgun
Surgery, Feature Envy), and antipatterns (Big Ball of Mud, Spaghetti
Code). What distinguishes Gas Town is its coherent fictional world rather
than isolated metaphors -- an entire setting mapped onto an entire
architecture.

## References

- Yegge, S. "Welcome to Gas Town" (2025) --
  https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04
- Yegge, S. Gas Town GitHub repository --
  https://github.com/steveyegge/gastown
- Appleton, M. "Gas Town's Agent Patterns" (2025-2026) --
  https://maggieappleton.com/gastown