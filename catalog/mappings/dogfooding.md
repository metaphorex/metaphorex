---
author: agent:metaphorex-miner
categories:
- software-engineering
- organizational-behavior
contributors:
- fshot
created: '2026-03-11'
harness: Claude Code
kind: dead-metaphor
name: Dogfooding
related: []
slug: dogfooding
source_frame: animal-husbandry
target_frame: software-programs
updated: '2026-03-14'
---

## What It Brings

Eating your own dog food -- the practice of using your own product
internally before selling it to customers. The metaphor maps a trust
test from animal husbandry (would you feed this to your own animal?)
onto product quality validation. If you would not use your own
software, why should anyone else?

Key structural parallels:

- **The trust test** -- a dog food manufacturer who eats their own
  product demonstrates ultimate confidence in its quality. The gesture
  is viscerally persuasive precisely because dog food is unappetizing:
  you would only do this if you genuinely believed in the product. In
  software, using your own tool internally makes the same statement.
  It says the product is good enough for the people who know its flaws
  best.
- **Feedback through lived experience** -- feeding the dog your own
  food means you observe the results directly. Does the dog eat it?
  Does the dog thrive? In software, dogfooding generates feedback that
  no amount of user testing can replicate. When developers use their
  own product for real work, they encounter friction, missing features,
  and bugs in the natural course of their day rather than in
  artificial test scenarios.
- **Alignment of incentives** -- if the team must use what it builds,
  quality becomes self-interest rather than abstract professional
  obligation. Bugs are not tickets in a backlog; they are personal
  annoyances. Missing features are not customer requests; they are
  things the team needs right now. The metaphor encodes a powerful
  organizational incentive: make the builders the users.
- **Social proof as marketing** -- "we use it ourselves" is one of
  the most effective sales arguments in technology. The dogfooding
  metaphor gives this argument a memorable, slightly self-deprecating
  name that disarms skepticism through humor.

## Where It Breaks

- **Developers are not representative users** -- the team that builds
  a product has deep technical expertise, knows the workarounds, and
  has internalized the product's mental model. Their experience of the
  product is fundamentally different from a new user's. Dogfooding can
  create a false sense of usability: the team finds the product
  perfectly usable because they built it, while actual users struggle
  with the same interface. The metaphor assumes that if the dog food
  is good enough for the manufacturer, it is good enough for the dog,
  but the manufacturer and the dog have very different palates.
- **Internal use may not exercise critical paths** -- a company using
  its own email client internally does not necessarily test the
  migration experience, the enterprise compliance features, or the
  behavior at 100,000-user scale. Dogfooding validates *a* use case,
  not *the* use case. The metaphor suggests comprehensive validation
  but often delivers only partial coverage.
- **The metaphor's self-deprecation can backfire** -- calling your
  product "dog food" was meant as humility, but the term imports the
  idea that the product is barely fit for consumption. In competitive
  markets, the metaphor can undermine the very confidence it was
  designed to project. Rival companies have been known to seize on the
  phrase: "even they call it dog food."
- **Forced dogfooding breeds resentment** -- when companies mandate
  internal use of immature products, the practice becomes punishment
  rather than validation. Developers forced to use a broken internal
  tool learn to hate it rather than improve it, producing cynicism
  instead of the alignment the metaphor promises. The dog, in this
  scenario, would rather eat something else.

## Expressions

- "Eating our own dog food" -- the full canonical form, used to
  announce or justify internal use of one's own product
- "We dogfood it" -- the compressed verb form, now standard in
  tech culture
- "Drinking our own champagne" -- the aspirational rebranding,
  attributed to Microsoft, replacing the self-deprecating "dog food"
  with something celebratory. The shift reveals discomfort with the
  original metaphor's implication of low quality.
- "Ice cream testing" -- another rebrand, used at some companies to
  make internal testing sound pleasant rather than punitive
- "We use it ourselves" -- the de-metaphorized version, stripped of
  the animal-husbandry framing but carrying the same logical argument
- "If we won't use it, why would they?" -- the rhetorical question
  that encapsulates the dogfooding principle

## Origin Story

The phrase "eating your own dog food" entered tech culture in the
1980s. The most widely cited origin attributes it to Microsoft, where
Paul Maritz reportedly sent an email in 1988 urging the company to
increase internal use of its own products, using the dog food
metaphor. However, the phrase existed in general business usage before
Microsoft adopted it, appearing in advertising and brand-trust
contexts: the Alpo dog food company ran television advertisements in
the 1970s featuring spokesperson Lorne Greene declaring that he fed
Alpo to his own dogs.

At Microsoft, dogfooding became institutionalized corporate practice.
Internal groups were expected to use pre-release versions of Windows,
Office, and other products, and the practice generated both genuine
quality improvement and considerable internal complaint. The term
spread to the broader tech industry through the 1990s and is now
standard vocabulary at most software companies.

The "drinking our own champagne" rebranding is sometimes attributed
to Microsoft executives uncomfortable with the dog food metaphor,
though it never fully displaced the original. The persistence of the
less flattering version suggests that the self-deprecation is part of
the metaphor's rhetorical power: the willingness to call your own
product "dog food" signals honesty in a way that "champagne" does not.

## References

- Lee, E. "Eating Your Own Dog Food," *Queue* (ACM) 7(4) (2009) --
  analysis of dogfooding as engineering practice
- Harrison, W. "Eating Your Own Dog Food," *IEEE Software* 23(3)
  (2006) -- examines the practice's effectiveness and limitations