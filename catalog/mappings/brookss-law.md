---
slug: brookss-law
name: "Brooks's Law"
kind: conceptual-metaphor
source_frame: manufacturing
target_frame: software-development
categories:
  - software-engineering
  - organizational-behavior
author: agent:metaphorex-miner
contributors: []
related:
  - conways-law
---

## What It Brings

Adding manpower to a late software project makes it later. Brooks's Law
uses the manufacturing frame -- more workers, faster output -- to show
exactly where it fails when applied to software. The law's power comes
not from the metaphor it proposes but from the metaphor it dismantles:
software development is NOT an assembly line.

- **The assembly-line assumption and its refutation** -- manufacturing
  provides the default mental model for project management: work is
  divisible into identical units, workers are interchangeable, and
  throughput scales linearly with headcount. Brooks demonstrates that
  software violates every one of these assumptions. Tasks are not
  independent; they have sequential constraints and intellectual
  dependencies. New workers must be trained by existing workers, diverting
  productive capacity. The manufacturing metaphor predicts acceleration;
  reality delivers deceleration.
- **Communication overhead as quadratic cost** -- Brooks's most precise
  insight: if n people must coordinate, the number of communication
  channels is n(n-1)/2. Adding one person to a team of five adds five new
  channels. Adding one person to a team of twenty adds twenty. The
  manufacturing frame has no analogue for this -- factory workers on
  adjacent stations need not coordinate, they just handle what arrives.
  Software workers must synchronize understanding, merge conflicting
  changes, and agree on interfaces. The communication cost grows faster
  than the productive capacity.
- **"Nine women can't make a baby in one month"** -- Brooks's most
  memorable expression captures irreducible sequential dependency. Some
  tasks have a minimum calendar time regardless of resources applied.
  Manufacturing has such constraints too (curing time, drying time), but
  they are treated as parameters, not as the fundamental nature of the
  work. In software, the sequential dependency IS the work: understanding
  the problem, designing the solution, and implementing it cannot be
  parallelized past a certain point.

## Where It Breaks

- **The law overstates its case for partitionable work** -- Brooks
  himself acknowledged that "perfectly partitionable" tasks do scale with
  headcount. Some software work approaches this: independent bug fixes,
  localized feature work on decoupled modules, porting to new platforms.
  The law is most true for tightly coupled systems with high coordination
  demands and least true for embarrassingly parallel tasks. Stating it as
  an absolute ("makes it later") obscures the spectrum.
- **Modern tooling has changed the communication cost curve** -- Brooks
  wrote in 1975, when communication meant meetings, memos, and shared
  offices. Version control, CI/CD pipelines, code review tools, and
  automated testing have not eliminated communication overhead but have
  changed its shape. A developer joining a well-documented open-source
  project can become productive faster than Brooks's model predicts
  because the documentation and tooling substitute for synchronous human
  communication.
- **The manufacturing metaphor is a straw man** -- by 1975, no serious
  software manager believed that adding programmers was exactly like
  adding factory workers. Brooks's rhetorical power depends on an
  audience that holds the manufacturing assumption, and the law has been
  so successful that its target assumption is now a historical curiosity.
  Citing Brooks's Law today often functions as a status signal ("I know
  the classic texts") rather than a genuine intervention against a live
  misunderstanding.
- **The law says nothing about removing people** -- if adding people
  makes a late project later, does removing people make it faster? The
  manufacturing metaphor runs in both directions, but Brooks's Law is
  strictly one-directional. The actual implication -- that the right team
  size is determined early and should not be changed -- is rarely stated
  because it is managerially inconvenient.

## Expressions

- "Adding manpower to a late software project makes it later" -- the
  canonical formulation from The Mythical Man-Month
- "Nine women can't make a baby in one month" -- the irreducible
  sequentiality argument, Brooks's most quoted illustration
- "The mythical man-month" -- the unit itself is the metaphor: the
  assumption that people and months are interchangeable, that a
  person-month is a fungible commodity
- "The surgical team" -- Brooks's proposed alternative: a small team
  structured like a surgical team rather than a factory floor, with
  specialized roles rather than interchangeable workers
- "No silver bullet" -- Brooks's follow-up essay (1986), extending the
  argument that software's essential complexity cannot be eliminated by
  any single technique

## Origin Story

Frederick Brooks published The Mythical Man-Month in 1975, drawing on
his experience managing the IBM System/360 operating system project in
the 1960s -- one of the largest software projects of its era and one of
the most famously troubled. The OS/360 project ran years late despite
(or because of) continuous additions of staff, providing Brooks with
the empirical basis for his law.

The book became the most widely read text in software engineering and
remained in print for decades. Brooks added the essay "No Silver
Bullet" in the 1995 anniversary edition, extending the argument from
project management to essential versus accidental complexity. The
law's enduring fame owes much to its memorable illustrations and to
the manufacturing metaphor it so effectively demolishes -- it is
easier to remember what is wrong than what is right.

## References

- Brooks, F. *The Mythical Man-Month: Essays on Software Engineering*,
  Addison-Wesley, 1975 -- the original text
- Brooks, F. "No Silver Bullet -- Essence and Accident in Software
  Engineering," *IEEE Computer* 20(4), April 1987 -- the follow-up essay
- DeMarco, T. & Lister, T. *Peopleware: Productive Projects and Teams*,
  Dorset House, 1987 -- extends Brooks's people-centric analysis of
  software project failure
