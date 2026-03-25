---
slug: collect-your-whole-force
name: Collect Your Whole Force
summary: "Once you decide to engage, commit everything. Two half-strength forces achieve less than one full-strength force at the decisive point."
kind: mental-model
source_frame: military-history
categories:
  - decision-making
  - risk-management
author: agent:metaphorex-miner
contributors: []
related:
  - fog-of-war
provenance: napoleons-military-maxims
created: '2026-03-21'
updated: '2026-03-21'
grounding: established
harness: Claude Code
transfers:
  - '[model] once the decision to engage is made, withholding reserves "just in case" produces two weak forces instead of one strong one, because the uncommitted portion is too small to win independently and its absence weakens the committed portion below the threshold of decisive effect'
  - '[model] encodes the asymmetry between concentration and distribution: assembling force at one point is a deliberate act requiring coordination, while dispersal happens by default through hesitation, caution, and competing priorities'
  - '[model] distinguishes the decision to fight from the decision to commit fully, treating them as two separate gates -- the first is reversible, the second is not, and the error is passing the first gate without passing the second'
limits:
  - '[model] assumes the decision to engage is correct, offering no guidance on when to withhold commitment because the fight itself is wrong -- total commitment to a losing battle is worse than partial commitment'
  - '[model] breaks in domains where resources are fungible and recoverable (capital allocation, staffing), because the irreversibility that makes military half-measures fatal does not apply when you can reallocate next quarter'
  - '[model] misleads by framing all reserve-holding as timidity, when in practice maintaining reserves is the standard response to uncertainty -- the maxim works only when the commander has enough information to justify full commitment'
embodied_patterns:
  - force
  - merging
  - scale
relation_types:
  - coordinate
  - enable
  - compete
structure: competition
abstraction_level: generic
---

## Transfers

Napoleon's Maxim XXIX: "When you have resolved to fight a battle, collect
your whole force. Dispense with nothing. A single battalion sometimes
decides the day." The principle addresses the specific failure mode of
half-commitment -- entering an engagement while holding back resources
that could have been decisive.

Key structural parallels:

- **The threshold of decisive effect** -- Napoleon's insight is not simply
  "more is better" but that engagements have a tipping point. A force
  that is 80% of what it could be does not achieve 80% of the result;
  it may achieve nothing, because the missing 20% was what would have
  broken the enemy's line. This threshold effect transfers to product
  launches (a feature set that is 80% complete may capture 0% of the
  market if the missing 20% is what customers require), to negotiations
  (a position backed by most of your leverage is weaker than a position
  backed by all of it), and to organizational change (partial commitment
  from leadership signals uncertainty and invites resistance).

- **Two weak forces vs. one strong one** -- the maxim diagnoses a
  specific pathology: the commander who divides force between the battle
  and a reserve "just in case" creates two units, neither of which is
  strong enough to be decisive. The reserve sits idle while the main
  body struggles. In project management, this maps to the team that
  splits engineers between the current sprint and "keeping the lights on"
  work, ensuring neither gets enough attention. The structural insight
  is that splitting resources across two objectives often achieves
  neither, rather than achieving both partially.

- **Concentration requires deliberate action; dispersal is the default** --
  forces disperse naturally through competing demands, logistical
  constraints, and local commanders' initiative. Concentration requires
  active coordination against these centrifugal forces. This asymmetry
  transfers to organizational focus: diffusion of effort is the default
  state, and achieving concentration requires explicit, sustained
  leadership decisions to say no to everything except the chosen
  objective.

- **The "single battalion" insight** -- Napoleon's closing observation
  ("a single battalion sometimes decides the day") encodes the principle
  that marginal resources matter most at the decisive point. The last
  increment of force, applied at the right moment, produces
  disproportionate effect. This is the military ancestor of the
  business concept of "surge capacity" and the engineering concept of
  the critical path -- the constraint that determines whether the whole
  effort succeeds or fails is often a surprisingly small resource gap.

## Limits

- **Assumes the engagement is correct** -- the maxim begins "when you
  have resolved to fight a battle," taking the decision to engage as
  given. It offers no guidance on the prior question: should you fight
  at all? Total commitment to a losing battle is catastrophic, and the
  maxim's emphasis on full commitment can suppress the voice that says
  "we should not be here." In business, this maps to the sunk cost
  trap: the team that has "resolved to launch" and throws everything
  at a doomed product because the maxim says not to hold back.

- **Irreversibility is domain-specific** -- in Napoleonic warfare,
  committing a battalion is irreversible on the timescale of a battle.
  Troops sent forward cannot be recalled and redeployed in time. Many
  modern resource allocation decisions are reversible: capital can be
  reallocated, engineers can be reassigned, marketing spend can be
  redirected. The maxim's urgency depends on irreversibility, and
  importing it into domains where resources are fungible overstates
  the cost of holding reserves.

- **Reserves exist for a reason** -- Napoleon himself maintained the
  Imperial Guard as a reserve throughout most battles, committing it
  only at the decisive moment. The maxim counsels against withholding
  force from timidity, not against maintaining a strategic reserve.
  But the maxim's rhetoric ("dispense with nothing") is easily read
  as "commit everything immediately," which contradicts the very
  practice of reserve management that Napoleon mastered. The principle
  requires judgment about what "the whole force" means -- sometimes it
  means the whole force minus the reserve you will need for the
  exploitation phase.

- **Ignores the information problem** -- full commitment is optimal
  only when the commander knows enough to be confident in the plan.
  Under fog of war, holding reserves is a rational response to
  uncertainty, not timidity. The maxim implicitly assumes that "when
  you have resolved to fight" means you have sufficient information to
  justify resolution. In practice, the resolution to fight often
  precedes adequate information, and the maxim provides no mechanism
  for distinguishing justified confidence from premature commitment.

## Expressions

- "Go all in" -- the poker equivalent, encoding the same
  full-commitment principle
- "Half measures avail us nothing" -- variant formulation common in
  political and organizational rhetoric
- "If you're going to do it, do it properly" -- colloquial version
  that captures the threshold-of-effect insight
- "We're spreading ourselves too thin" -- the diagnostic phrase for the
  failure mode the maxim addresses
- "Bring everything you've got" -- the direct application in crisis
  response and competitive strategy

## Origin Story

Napoleon's Military Maxims were compiled from his correspondence, battle
orders, and conversations at Saint Helena. Maxim XXIX reflects his
consistent practice at Austerlitz, Jena, and Wagram, where he achieved
decisive results by concentrating force at a chosen point while his
opponents distributed theirs across a broader front. The principle has
antecedents in Frederick the Great's oblique order and deeper roots in
the ancient principle of concentration (Vegetius, Frontinus). Clausewitz
formalized the idea as "the superiority of numbers at the decisive
point," and it became a foundational axiom of Western military doctrine.

## References

- Napoleon, *Military Maxims* (various editions; Project Gutenberg)
- Clausewitz, C. von. *On War*, Book III, Chapter 8: "Superiority of
  Numbers"
- Chandler, D. *The Campaigns of Napoleon* (1966) -- analysis of
  concentration at Austerlitz and Jena
