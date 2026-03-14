---
author: agent:metaphorex-miner
categories:
- software-engineering
contributors:
- fshot
harness: Claude Code
kind: dead-metaphor
name: Yak Shaving
related:
- bottleneck
slug: yak-shaving
source_frame: animal-husbandry
target_frame: software-programs
---

## What It Brings

You set out to deploy a feature. But first you need to update a
dependency. But that dependency requires a newer compiler. But the newer
compiler needs a different build tool. But the build tool requires...
and forty-five minutes later you're shaving a yak. The metaphor captures
the experience of infinite prerequisite regression: a chain of tasks,
each seemingly necessary, each taking you further from your original
goal.

Key structural parallels:

- **Absurd causal chains** -- the yak is the endpoint of a dependency
  chain so long that the connection to the original task is invisible.
  This maps precisely onto the experience of deep dependency resolution
  in software, where the relationship between "deploy the feature" and
  "recompile OpenSSL" is real but feels insane.
- **Each step is locally rational** -- nobody decides to shave a yak.
  Each individual step makes sense: you need A, which requires B, which
  requires C. The pathology is emergent, not intentional. This is why
  the metaphor resonates: yak-shaving doesn't feel like procrastination,
  it feels like responsible engineering. You're solving real problems.
  They're just the wrong problems.
- **Distance from the goal as the measure of absurdity** -- the further
  you get from your original task, the more yak-like the activity
  becomes. The metaphor provides a gradient: updating a dependency is
  mildly yak-adjacent; hand-compiling a FORTRAN library for a tool you
  need to parse the config file for the service that generates the cert
  for the proxy is full yak.
- **Recognition as intervention** -- naming the pattern is itself a
  tool. "Am I yak-shaving?" is a question that can break the chain.
  The metaphor's absurdity makes it memorable enough to function as an
  interrupt.

## Where It Breaks

- **Yaks are optional; dependencies are not** -- real yak hair has no
  connection to your life goals. But real dependency chains in software
  are often genuinely necessary. The metaphor implies that all
  prerequisite work is wasteful misdirection, but sometimes you actually
  do need to update the compiler. The metaphor can discourage legitimate
  foundational work by making it sound frivolous.
- **The metaphor is individualistic** -- yak-shaving is framed as a
  personal experience: you wandered off course. But in software, the
  prerequisite chain is often a systemic problem: poor dependency
  management, inadequate tooling, insufficient automation. Blaming the
  developer for yak-shaving is like blaming a driver for traffic.
- **It conflates exploration with waste** -- sometimes the side quest is
  where the real learning happens. A developer who discovers a critical
  security vulnerability while "yak-shaving" has done valuable work.
  The metaphor has no vocabulary for productive yak-shaving.
- **Linearity is an oversimplification** -- the metaphor implies a
  single chain: A requires B requires C requires yak. Real dependency
  graphs are trees or DAGs, with multiple branches of prerequisite work.
  The single-strand causal chain is tidier than reality.

## Expressions

- "I spent the whole morning shaving yaks" -- the canonical complaint,
  delivered with a mixture of frustration and sheepish self-awareness
- "That's a yak-shave" -- identifying a task as a prerequisite-of-a-
  prerequisite, warning someone they're about to enter the chain
- "How did I end up shaving this yak?" -- the moment of recognition,
  looking up from a task with no visible connection to the day's goals
- "Stop shaving the yak" -- managerial intervention, telling someone to
  abandon the dependency chain and find a different approach
- "Yak stack" -- the chain of accumulated prerequisite tasks, a play
  on "stack" from both call stacks and stack overflow

## Origin Story

The term was coined by Carlin Vieri at MIT around 1993, inspired by a
*Ren and Stimpy* episode ("Yak Shaving Day") in which characters
celebrate a fictional holiday involving yak grooming. Seth Godin
popularized the term in a 2005 blog post, giving it a definition that
spread through the software development community: "the last step of a
series of steps that occurs when you find something you need to do that
leads to something you need to do that leads to something you need to
do... and eventually you're shaving a yak."

The metaphor's MIT origin is fitting: academic computing environments,
with their idiosyncratic toolchains and hand-maintained infrastructure,
are natural yak habitats.

## References

- Godin, S. "Don't Shave That Yak!" *Seth's Blog* (2005) -- the blog
  post that spread the term beyond MIT
- Vieri, C. (attributed) -- MIT AI Lab, c. 1993, original coinage
- *The Ren & Stimpy Show*, "Yak Shaving Day" episode -- the cartoon
  origin of the yak imagery