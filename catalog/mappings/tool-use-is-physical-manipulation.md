---
slug: tool-use-is-physical-manipulation
name: "Tool Use Is Physical Manipulation"
kind: conceptual-metaphor
source_frame: embodied-experience
target_frame: artificial-intelligence
categories:
  - ai-discourse
  - software-engineering
author: agent:metaphorex-miner
harness: "Claude Code"
contributors: []
related:
  - ai-is-a-tool
---

## What It Brings

When an AI model calls an API, executes code, or queries a database, we say
it "uses a tool." The phrasing imports the full structure of embodied tool
use: reaching for an object, gripping it, manipulating it with directed
force, and setting it down. The metaphor makes AI function-calling legible
through our oldest cognitive frame -- the hand grasping a thing to act on
the world.

Key structural parallels:

- **Reach and grasp** -- an AI agent "picks up" a tool from an available
  set, mirroring how a human surveys a workbench and selects the right
  instrument. Framework APIs that register "available tools" reproduce the
  affordance structure of a physical toolkit: what can be reached determines
  what can be done.
- **Directed manipulation** -- the agent "uses" the tool on a specific
  target, the way a hand uses a screwdriver on a screw. The function call
  has parameters (what to act on) and returns a result (what happened). This
  maps onto the physical sequence of aim, apply force, observe effect.
- **Tool extends capability** -- a wrench lets a hand apply torque beyond
  muscular capacity. An API call lets a language model access real-time
  data, execute calculations, or modify external systems it cannot touch
  through text generation alone. The metaphor frames function-calling as
  extending the model's "reach" into the world.
- **The hand is not the tool** -- physical tool use maintains a clear
  boundary between agent and instrument. The metaphor imports this
  distinction into AI architecture: the model is the agent, the API is the
  tool, and they are separate things. This shapes how developers design
  tool-use interfaces -- as cleanly separable plugins rather than fused
  capabilities.
- **Skill in handling** -- some people are better with tools than others.
  The metaphor imports this notion into AI discourse: models can be "good
  at tool use" or "clumsy with tools," as if dexterity were a property that
  varies among agents.

## Where It Breaks

- **There is no hand** -- physical manipulation requires a body with
  proprioception, spatial awareness, and force feedback. An API call is
  a structured data exchange between processes. Nothing is gripped, aimed,
  or released. The embodied frame imports physicality where none exists,
  creating the illusion that function-calling involves something like
  motor skill when it is purely symbolic.
- **The tool does most of the work** -- when a human uses a hammer, the
  human supplies the energy and the hammer provides leverage. When an AI
  "uses" a search API, the search engine does the information retrieval,
  ranking, and formatting. The model's contribution is constructing the
  query string -- a far cry from the sustained physical effort that tool
  use normally implies. The metaphor inverts the effort distribution.
- **Tools do not talk back** -- a wrench does not return a structured
  JSON response explaining what it did. AI tool use is fundamentally
  bidirectional: the model sends a request and receives rich, structured
  data that reshapes its subsequent reasoning. Physical tool use is
  unidirectional -- the tool transmits force, it does not transmit
  information. The feedback loop in AI tool use is more like a
  conversation than like hammering.
- **Selection is not embodied** -- choosing which function to call is a
  text-prediction task: the model generates a token sequence that happens
  to match a function signature. There is no scanning of a workbench, no
  weighing of a tool in the hand, no haptic assessment. The metaphor
  makes this selection feel like a physical act of judgment when it is
  actually pattern matching over token distributions.
- **The "manipulation" framing obscures composition** -- physical tools
  are used one at a time (you put down the screwdriver before picking up
  the drill). AI tool use increasingly involves parallel calls, chained
  calls, and nested tool invocations that have no physical analogue. The
  embodied frame cannot represent a model simultaneously "holding" six
  tools and composing their outputs.

## Expressions

- "The model picked up the tool and called the API" -- embodied reaching
  and grasping applied to function invocation
- "Tool use" -- the standard term in AI research (Anthropic, OpenAI,
  Google) for function-calling capabilities
- "Hands for the AI" -- describing tool access as giving the model
  physical appendages
- "The agent reached for the calculator" -- selection framed as physical
  reaching
- "Clumsy tool use" -- motor-skill vocabulary for API-call failure modes
- "Give the model access to tools" -- handing over instruments, like
  passing a wrench

## Origin Story

The "tool use" framing entered AI discourse through the reinforcement
learning community, where agents in simulated environments literally
manipulated virtual objects. When language models gained the ability to
call external functions (Google's Toolformer paper, 2023; OpenAI's
function calling, 2023; Anthropic's tool use, 2024), the term carried
over despite the complete absence of physical manipulation. The metaphor
was reinforced by the broader "AI is a tool" framing -- if AI itself is
a tool, then AI using tools creates a satisfying recursive image of
tools wielding tools.

The embodied language persists because it makes an abstract capability
concrete and intuitive. "The model called a function" is accurate but
inert. "The model used a tool" invokes millennia of human experience
with physical instruments and makes the capability feel familiar rather
than alien.

## References

- Schick, T. et al. "Toolformer: Language Models Can Teach Themselves to
  Use Tools" (2023) -- the paper that popularized "tool use" for LLMs
- Anthropic, "Tool use (function calling)" documentation (2024) --
  canonical industry usage of the embodied framing
- OpenAI, "Function calling" documentation (2023) -- alternative
  terminology that partially avoids the embodied metaphor
- Maas, M. "AI is Like... A Literature Review of AI Metaphors" (2023)
