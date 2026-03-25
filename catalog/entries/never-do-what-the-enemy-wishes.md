---
slug: never-do-what-the-enemy-wishes
name: "Never Do What the Enemy Wishes"
summary: "In adversarial situations, an opponent's revealed preference is a negative signal about the action's value to you."
kind: mental-model
categories:
- decision-making
- economics-and-finance
author: agent:metaphorex-miner
contributors: []
related:
- decisive-point
- fog-of-war
- contrarian-thinking
provenance: napoleons-military-maxims
created: '2026-03-20'
updated: '2026-03-20'
grounding: established
harness: Claude Code
transfers:
  - '[law] If an adversary visibly encourages a particular action, the action''s expected payoff for the actor is negative, because the adversary''s preference reveals information about the payoff structure'
  - '[law] The strength of the inference scales with the adversary''s competence and information advantage -- a sophisticated adversary''s revealed preference is a stronger signal than a naive one''s'
  - '[law] The principle applies recursively: if the adversary knows you will invert their preference, they can exploit this by feigning desire for the outcome they actually want you to choose'
limits:
  - '[law] fails when the adversary''s interests are partially aligned with yours -- in non-zero-sum games (trade negotiations, partnerships), what the other party wants may also be good for you, and reflexive contrariness destroys cooperative surplus'
  - '[law] breaks under information asymmetry reversal: if you know more than the adversary, their expressed preferences may reflect genuine miscalculation rather than strategic manipulation, making inversion counterproductive'
  - '[law] collapses into infinite regress in games between equally sophisticated players -- "they want me to do X, so I should do not-X, but they anticipated that, so they actually want not-X..." -- the maxim offers no stopping rule for this recursion'
embodied_patterns:
  - force
  - matching
  - path
relation_types:
  - compete
  - prevent
structure: competition
abstraction_level: generic
---

## Transfers

Napoleon's Maxim XVI states: "Never do what the enemy wishes you to
do, for this reason alone, that he desires it. A field of battle which
he has previously studied and reconnoitered should be avoided, and
double care should be taken where he has had time to fortify or
entrench." The maxim distills a game-theoretic insight that predates
formal game theory by a century: in adversarial situations, an
opponent's revealed preferences contain information about the payoff
structure, and that information should update your decision.

Key structural parallels:

- **Revealed preference as negative signal** -- the core logic is that
  in a zero-sum contest, your opponent's gain is your loss. If your
  opponent wants you to take action X, it follows that X benefits them,
  which means X harms you. The opponent's expressed desire is therefore
  a negative signal about X's value to you. This transfers directly to
  competitive strategy: if an incumbent publicly welcomes a startup's
  entry into a particular market segment, the startup should ask what
  the incumbent knows about that segment's unprofitability. In
  negotiation: if the counterpart eagerly agrees to your proposed
  terms, you have probably left value on the table.
- **Information extraction from adversary behavior** -- Napoleon's
  deeper point is that the enemy's dispositions, preparations, and
  encouragements are a form of intelligence. A fortified position
  that the enemy invites you to attack is fortified precisely because
  the enemy expects it to be attacked. This transfers to cybersecurity
  (honeypots exploit the attacker's tendency to go where they think
  they are expected), to poker (a player who bets aggressively may be
  bluffing -- or may want you to think they are bluffing), and to
  market competition (a competitor's visible retreat from a segment
  may be bait to draw you into an unprofitable fight).
- **Asymmetric information as the mechanism** -- the principle works
  because the adversary typically has information you lack (they have
  "previously studied and reconnoitered" the terrain). Their
  preference reveals something about their private information. This
  is the structure behind adverse selection in economics: if the seller
  is eager to sell, the buyer should wonder why. If the acquirer is
  eager to buy, the target's shareholders should wonder what the
  acquirer knows. The maxim is, at root, a heuristic for inferring
  private information from observed enthusiasm.

## Limits

- **Assumes zero-sum competition** -- the maxim's logic depends on the
  adversary's gain being your loss. In cooperative or mixed-motive
  games, what the other party wants may also be good for you.
  Reflexively doing the opposite of what a negotiating partner
  suggests in a joint venture destroys value for both sides. The
  maxim is powerful in war and pure competition but toxic in
  partnerships, alliances, and any relationship where interests
  partially overlap.
- **Vulnerable to double-bluff** -- a sophisticated adversary who knows
  you follow this maxim can exploit it by expressing desire for the
  outcome they actually want you to avoid. Napoleon's principle has no
  built-in defense against this: it tells you to invert the enemy's
  stated preference, but a clever enemy will state preferences
  strategically. This is the problem of higher-order reasoning in
  game theory, and the maxim provides no stopping rule. Poker players
  call this "leveling": thinking about what the opponent thinks you
  think they want.
- **Contrarianism is not strategy** -- the maxim can degenerate into
  reflexive opposition: doing the opposite of whatever the competitor
  does, regardless of merit. A startup that avoids a market solely
  because an incumbent is present may be avoiding the most attractive
  opportunity. The maxim identifies a useful heuristic signal (enemy
  preference reveals information) but does not say that signal should
  override all other analysis. Napoleon himself did not always avoid
  battle on unfavorable terrain -- he attacked at Austerlitz on ground
  the Allies had chosen, because his own analysis told him the Allies
  had misjudged the terrain.
- **Degrades without adversarial competence** -- the inference depends
  on the adversary being rational and well-informed. If the adversary
  is incompetent, confused, or acting on bad information, their
  preferences reveal nothing useful about the payoff structure. A
  competitor who wants you to enter a market may want it because they
  have misread the market, not because they have prepared a trap. The
  maxim assumes a worthy opponent, and fails when applied to noise.

## Expressions

- "Never do what the enemy wishes" -- the direct Napoleonic formulation,
  common in military education
- "If they're eager to sell, I'm not eager to buy" -- Wall Street version
  of the same logic, applied to deal-making and investment
- "When your competitor celebrates your move, worry" -- business strategy
  shorthand
- "Inverse signal" / "contrarian indicator" -- financial market language
  for extracting information from the behavior of other market
  participants
- "It's a trap" -- colloquial (and Star Wars) expression of the
  underlying insight that an invitation to act may conceal a prepared
  position
- "Adverse selection" -- the economics formalization: the party most
  eager to trade is the one with unfavorable private information

## Origin Story

The maxim appears as number XVI in the various published collections of
Napoleon's military maxims, which were compiled from his correspondence,
dictations at St. Helena, and observations recorded by his staff.
Napoleon did not write a systematic treatise; his maxims were extracted
and organized by editors, most notably General Burnod in 1827.

The underlying game-theoretic insight -- that an adversary's revealed
preference is informative about payoff structure -- was not formalized
until John von Neumann and Oskar Morgenstern published *Theory of Games
and Economic Behavior* in 1944. Napoleon's maxim anticipates the
minimax principle: in a two-player zero-sum game, you should assume
your opponent is playing optimally against you, and act accordingly.
The maxim entered business vocabulary through the broader adoption of
military strategic thinking in MBA programs during the 1980s and
through popular game theory treatments in the 1990s.

## References

- Napoleon Bonaparte. *Military Maxims* (Burnod ed., 1827) -- Maxim XVI
- von Neumann, John and Oskar Morgenstern. *Theory of Games and Economic
  Behavior* (1944) -- formal foundation for the adversarial reasoning
  Napoleon intuited
- Dixit, Avinash K. and Barry J. Nalebuff. *Thinking Strategically*
  (1991) -- accessible game theory that draws on military examples
- Akerlof, George A. "The Market for Lemons" (1970) -- adverse selection
  as the economic parallel to Napoleon's insight
