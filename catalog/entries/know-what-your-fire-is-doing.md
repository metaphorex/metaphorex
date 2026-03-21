---
slug: know-what-your-fire-is-doing
name: Know What Your Fire Is Doing
kind: mental-model
source_frame: fire-safety
categories:
- decision-making
- risk-management
author: agent:metaphorex-miner
contributors: []
related:
- ten-standard-fire-orders
- fight-fire-aggressively-having-provided-for-safety-first
- lces
provenance: firefighting-maxims
created: '2026-03-20'
updated: '2026-03-21'
grounding: established
harness: Claude Code
transfers:
  - '[model] demands continuous monitoring of the specific threat you are engaging, not threats in general -- "your fire" names the particular hazard assigned to you, encoding the principle that situational awareness must be scoped to be actionable'
  - '[model] treats awareness as an active, ongoing obligation ("doing" is present continuous) rather than a one-time assessment, predicting that threats which were understood at the start of engagement will have changed by the time action is underway'
  - '[model] makes knowledge a precondition for all subsequent decisions by placing it as Order #2 in the sequence, encoding the principle that you cannot make valid tactical choices about a threat you have stopped tracking'
limits:
  - '[model] assumes the fire is observable -- that the threat produces legible signals (flame, smoke, heat) which a trained observer can read in real time -- and breaks in domains where the threat is invisible, latent, or deliberately concealed until it is too late to respond'
  - '[model] scopes attention to "your" fire, which can produce tunnel vision that misses adjacent threats -- the fire on the next ridge, the cascading failure in the adjacent system -- that are not yours until they suddenly are'
---

## Transfers

Standard Fire Order #2 states: "Know what your fire is doing at all
times." It is the second order in the sequence, placed immediately
after "Keep informed of fire weather conditions and forecasts,"
establishing a two-layer awareness requirement: know the environment
(weather), then know the specific threat (your fire). The possessive
pronoun is critical. Not "know what fire does" (general knowledge)
but "know what YOUR fire is doing" (specific, continuous, scoped
awareness of the particular threat you are engaging).

Key structural parallels:

- **Scoped awareness over general knowledge.** The order does not ask
  firefighters to understand fire science in the abstract. It asks
  them to know what this particular fire, on this particular day, in
  this particular terrain, is doing right now. The structural insight
  is that domain expertise is necessary but insufficient -- what
  kills people is not ignorance of general principles but loss of
  contact with the specific situation. In incident response, the
  equivalent is: do not rely on your mental model of how the system
  usually behaves; look at what this outage is actually doing, right
  now, to these specific services. In investing, it is: do not rely
  on your thesis about the company; look at what this position is
  actually doing to your portfolio today.

- **Continuous present tense.** "What your fire IS DOING" -- not
  "what your fire did" or "what your fire will do." The order
  demands real-time tracking, not retrospective analysis or
  predictive modeling. Fire behavior changes rapidly: a wind shift,
  a slope change, a fuel type transition can alter the fire's
  direction and intensity in minutes. The structural transfer is that
  situational awareness decays. Knowledge that was accurate an hour
  ago may be dangerously wrong now. In software operations, this is
  the difference between reviewing yesterday's metrics and watching
  the live dashboard during an incident. In project management, it
  is the difference between reading last week's status report and
  walking the floor today.

- **"Your" creates accountability.** The possessive pronoun assigns
  ownership. Someone specific is responsible for knowing what this
  fire is doing. The order does not say "ensure the fire is being
  monitored" (passive, delegatable). It says "know" (active, personal).
  The structural transfer is that situational awareness cannot be
  fully delegated. A commander who receives reports about the fire
  but has not personally observed it is relying on someone else's
  judgment about what is important to report. In organizational
  terms, the executive who relies on dashboards curated by others
  does not truly know what their fire is doing -- they know what
  someone else decided to show them about it.

- **Knowledge as a prerequisite for authority.** By placing this order
  early in the sequence (Order #2), the framework establishes that
  no subsequent decision -- where to position crews, when to attack,
  when to retreat -- is valid without current fire knowledge. The
  structural insight is that authority to act must be grounded in
  current awareness of the situation. A leader making decisions
  based on stale information is not leading; they are guessing with
  the weight of command behind them.

## Limits

- **It assumes observable threats.** Wildland fire produces highly
  legible signals: visible flame, smoke columns, heat, sound. A
  trained firefighter can read fire behavior the way a sailor reads
  the sea. But many organizational threats are invisible: a security
  breach may produce no visible signals for months, a cultural
  deterioration may not manifest until a key person quits, a market
  shift may be undetectable until revenue drops. The order works in
  domains with high signal fidelity and breaks in domains where the
  threat is concealed, latent, or ambiguous.

- **"Your fire" can produce tunnel vision.** The possessive scoping
  that makes the order actionable also creates a risk: attention
  locked on your assigned fire may blind you to adjacent threats.
  In wildland fire, the danger is the spot fire behind you, ignited
  by embers carried over the line. In organizational terms, the
  danger is the adjacent project failure, the competitor's move in
  a different market segment, or the infrastructure decay in a
  system outside your team's scope. The order optimizes for depth
  of awareness at the expense of breadth.

- **Continuous monitoring is resource-expensive.** "At all times" is
  an absolute demand. In a wildland fire operation, dedicated lookouts
  fulfill this role. But in organizational contexts, continuous
  monitoring of a single threat competes with all other demands on
  attention. The executive who spends all day monitoring one crisis
  is neglecting everything else. The order provides no guidance on
  how to allocate the finite resource of attention across multiple
  simultaneous "fires."

- **Knowing is not the same as understanding.** You can observe that
  the fire has changed direction without understanding why. The order
  demands awareness but not necessarily comprehension. In complex
  systems, observing what is happening (the metrics are changing)
  without understanding the mechanism (why the metrics are changing)
  can lead to interventions that address symptoms rather than causes.

## Expressions

- "Know what your fire is doing" -- the canonical form, Standard Fire
  Order #2, used verbatim in incident management training
- "What's the fire doing?" -- the abbreviated check-in used on the
  fireline, adapted in incident response as "What's the incident
  doing right now?"
- "Keep your eyes on the fire" -- colloquial derivative meaning to
  maintain continuous awareness of the active threat
- "Size-up" -- the formal firefighting term for initial and ongoing
  assessment of fire behavior, transferred to business as "situation
  assessment"
- "We lost SA" (situational awareness) -- the post-incident diagnosis
  when Order #2 was violated, used in aviation, military, and
  emergency management to explain failures caused by loss of contact
  with the evolving situation

## Origin Story

Standard Fire Order #2 was one of the original ten orders codified in
1957 by the U.S. Forest Service task force investigating the Inaja Fire
(1956). Its placement as Order #2 was deliberate: it establishes
continuous threat monitoring as the immediate successor to environmental
awareness (Order #1, weather). Together, the first two orders create
an awareness foundation on which all subsequent tactical decisions rest.

The order's wording draws on decades of after-action investigations
that consistently found the same failure pattern: firefighters who
were actively engaged in suppression work lost track of what the fire
was doing around them. The Mann Gulch disaster (1949), analyzed by
Norman Maclean in *Young Men and Fire* and by Karl Weick in his
sensemaking research, is the paradigmatic case: the crew was hiking
toward the fire with their backs to it when the fire reversed
direction and overran them. They did not know what their fire was
doing, and thirteen of them died.

The order's influence extends well beyond wildland fire. The U.S.
military's OODA loop (Observe-Orient-Decide-Act) begins with
"Observe" for the same structural reason: you cannot orient, decide,
or act without current knowledge of the threat. The order is now
standard training content in incident response, emergency management,
and high-reliability organization curricula.

## References

- National Wildfire Coordinating Group, *Incident Response Pocket Guide*
  (PMS 461), current edition
- Maclean, N. *Young Men and Fire* (1992) -- the Mann Gulch narrative
  demonstrating the fatal consequences of losing fire awareness
- Weick, K. "The Collapse of Sensemaking in Organizations: The Mann
  Gulch Disaster," *Administrative Science Quarterly* 38(4), 1993
- Boyd, J. "A Discourse on Winning and Losing" (1987) -- the OODA
  loop framework that shares the order's awareness-first structure
