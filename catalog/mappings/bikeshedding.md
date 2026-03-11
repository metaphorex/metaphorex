---
slug: bikeshedding
name: "Bikeshedding"
kind: conceptual-metaphor
source_frame: architecture-and-building
target_frame: collaborative-work
categories:
  - software-engineering
  - organizational-behavior
author: metaphorex-miner
contributors: []
related:
  - bottleneck
---

## What It Brings

A committee that must approve a nuclear power plant spends most of its
time debating the color of the bike shed. The reactor is too complex for
most members to have an opinion on; the bike shed is simple enough that
everyone does. Trivial accessibility maps onto disproportionate attention.

Key structural parallels:

- **Inverse complexity-attention relationship** -- the easier something
  is to understand, the more opinions it attracts. This is Parkinson's
  original insight, and it maps with uncomfortable precision onto code
  review culture: a PR that rearchitects the database gets two
  approvals in ten minutes; a PR that renames a variable gets forty-seven
  comments about naming conventions.
- **Competence as a barrier to participation** -- the nuclear reactor
  requires specialized knowledge to evaluate. The bike shed requires only
  the ability to perceive color. The metaphor maps the distribution of
  competence onto the distribution of attention: people contribute where
  they can, which means they contribute to the trivial parts.
- **Democratic dysfunction** -- everyone gets a vote on the bike shed
  because everyone *can* vote on the bike shed. The metaphor exposes a
  failure mode of democratic decision-making: equal voice does not
  produce equal value when competence is unequal. In software teams, this
  manifests as style debates consuming more collective energy than
  architecture decisions.
- **The feeling of contribution** -- debating the bike shed *feels*
  productive. You're participating, you're engaged, you have opinions.
  The metaphor maps the psychological satisfaction of contribution onto
  its actual value and finds them wildly misaligned.

## Where It Breaks

- **Sometimes the bike shed matters** -- the metaphor assumes that
  trivial decisions are actually trivial. But naming conventions,
  formatting standards, and API surface design are "bike shed" topics
  that have real consequences for maintainability. Dismissing discussion
  of these as bikeshedding can suppress legitimate quality concerns.
- **The reactor/shed binary is too clean** -- real decisions exist on a
  spectrum of complexity and importance. The metaphor creates two
  categories (important-and-complex vs. trivial-and-simple) when most
  decisions are somewhere in between. This binary can be weaponized:
  calling a discussion "bikeshedding" is an effective way to shut down
  debate you find tedious, regardless of its actual importance.
- **It pathologizes accessibility** -- the metaphor implies that if
  everyone can understand something, it probably doesn't matter. This is
  a form of complexity worship: the assumption that important things must
  be hard. Sometimes the most impactful decisions are the simplest ones.
- **Power dynamics, not just complexity** -- Parkinson's original
  example involves a committee, which has implicit hierarchy. People may
  avoid commenting on the reactor not because they lack competence but
  because they lack *standing*. The metaphor attributes to cognitive
  limitations what may actually be social dynamics: junior engineers
  review naming because they don't feel authorized to question
  architecture.

## Expressions

- "This is pure bikeshedding" -- the dismissal, deployed in code reviews
  and meeting rooms to end a discussion deemed trivial
- "Let's not bikeshed this" -- the preemptive form, attempting to
  prevent a discussion from beginning
- "The bikeshed problem" -- the general principle, applied to any
  situation where attention is inversely proportional to importance
- "Painting the bikeshed" -- variant emphasizing the decorative,
  superficial nature of the work being debated
- "We've been bikeshedding for thirty minutes" -- the time-check
  intervention, making the cost of the discussion explicit

## Origin Story

C. Northcote Parkinson introduced the concept in *Parkinson's Law*
(1957) as the "Law of Triviality": the time spent on any agenda item
is inversely proportional to the sum of money involved. His examples
were a nuclear reactor (approved in minutes) and a bicycle shed
(debated at length). He also included a third example: the budget for
refreshments at committee meetings, which generated the most debate of
all.

The term "bikeshedding" was introduced to the software community by
Poul-Henning Kamp in a 1999 email to the FreeBSD developers mailing
list, where he explicitly cited Parkinson and applied the concept to
open-source project governance. The email ("Why Should I Care What Color
the Bikeshed Is?") became one of the most widely cited pieces of
developer culture writing. Kamp's contribution was to map Parkinson's
committee dynamics onto the specific pathologies of open-source
collaboration, where the absence of formal authority makes bikeshedding
especially acute.

## References

- Parkinson, C.N. *Parkinson's Law* (1957) -- the original articulation
  of the Law of Triviality
- Kamp, P.-H. "Why Should I Care What Color the Bikeshed Is?" FreeBSD
  mailing list (1999) -- the email that brought bikeshedding to software
  culture
