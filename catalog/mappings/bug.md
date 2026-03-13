---
slug: bug
name: "Bug"
kind: dead-metaphor
source_frame: organism
target_frame: software-programs
categories:
  - linguistics
  - software-engineering
author: fshot
contributors: []
related: []
---

## What It Brings

An unwanted creature that has gotten into your system -- something alive,
small, hard to find, and hard to remove. The metaphor imports an entire
pest-control vocabulary into software engineering: we hunt bugs, squash
them, fumigate codebases, and track infestations.

- **Agency and evasion** -- a bug is not a passive defect. The creature
  metaphor implies the flaw hides from you, moves when you look for it,
  and resists extermination. This maps surprisingly well onto certain
  classes of software defects: race conditions that vanish under the
  debugger, heisenbugs that disappear when observed, and intermittent
  failures that resist reproduction. The metaphor gives developers a
  mental model where the defect is an adversary, which turns debugging
  into a hunt rather than an inspection.
- **Infestation logic** -- bugs are never singular. Finding one implies
  others. This maps directly onto engineering heuristics: if you find
  one bug in a module, you assume the module is buggy and look harder.
  The metaphor encodes a statistical insight (defects cluster) as a
  visceral intuition (pests breed).
- **Intrusion from outside** -- the creature metaphor implies the bug
  came from somewhere else and got into your clean system. This frames
  defects as contamination rather than as properties of the system
  itself, which shapes how developers think about quality: as something
  to defend rather than something to build in.

## Where It Breaks

- **Bugs are features of the system, not invaders** -- the creature
  metaphor's most dangerous implication is that defects come from outside.
  In reality, bugs are produced by the system that contains them: the
  architecture, the developer's mental model, the requirements that
  contradict each other. Framing bugs as pests that got in obscures
  the systemic causes and encourages whack-a-mole fixes rather than
  structural improvements.
- **The agency metaphor flatters developers** -- if the bug is a
  creature that hides, then failing to find it is not the developer's
  fault. The metaphor externalizes responsibility. A more honest framing
  would be "mistake" or "oversight," but those implicate the maker. "Bug"
  protects the ego of the person who wrote the code.
- **The Hopper myth distorts the history** -- the popular story that
  Grace Hopper found a moth in the Harvard Mark II in 1947 and coined
  the term is mostly wrong. Edison used "bug" for mechanical faults in
  the 1870s. The term was standard engineering slang decades before
  Hopper's team taped a moth to a logbook with the note "first actual
  case of bug being found." That entry was a joke -- the word was already
  in use. The myth persists because it makes a better story than "the
  metaphor was already dead by 1947."
- **Severity collapse** -- "bug" covers everything from a typo in a
  tooltip to a security vulnerability that exposes millions of records.
  The creature metaphor treats all bugs as the same kind of thing (pests
  to be squashed), which obscures the vast differences in severity,
  origin, and appropriate response.

## Expressions

- "Debugging" -- the hunt, directly descended from the pest metaphor;
  the most common word in software engineering that nobody parses as
  metaphorical
- "Squash a bug" -- extermination language, treating the defect as
  something to kill rather than understand
- "Buggy" -- infested, as if the software were a house with termites
- "Bug report" -- a sighting report, like a naturalist's field notes;
  you document where and when you saw the creature
- "Bug bounty" -- a wanted poster with a reward, importing the Old West
  bounty hunter into software security
- "Known bugs" -- pests you have identified but not yet exterminated,
  a concept that would be alarming in actual pest control but is routine
  in software
- "Bug triage" -- medical metaphor layered on top of the creature
  metaphor; sorting which pests to kill first

## Origin Story

Thomas Edison used "bug" in an 1878 letter to describe faults in his
inventions: "I did find a 'bug' in my apparatus, but it was not in the
telephone proper." The term was already common enough that he put it in
quotes as slang, not as a coinage. It appears to derive from the general
sense of "bugbear" or "bogey" -- an imaginary creature that causes
trouble -- rather than from literal insects.

The metaphor was standard engineering jargon by the early 20th century.
When Grace Hopper's team at Harvard found a moth trapped in a relay of
the Mark II computer on September 9, 1947, they taped it to the logbook
and wrote "first actual case of bug being found." This was a pun, not
a coinage. The moth incident became the origin myth because it has
everything a good story needs: a famous scientist, a literal bug, and
a clear date. The real etymology -- gradual adoption of informal slang
across decades of engineering -- makes for a less satisfying narrative.

By the time software engineering became a recognized discipline in the
1960s, "bug" was already dead. No programmer thinks of insects when
filing a bug report. The creature is gone; only the hunt remains.

## References

- Edison, T. Letter to Theodore Puskas, November 13, 1878
- Hopper, G. Logbook entry, Harvard Mark II, September 9, 1947 --
  preserved at the Smithsonian National Museum of American History
- Kidwell, P. "Stalking the Elusive Computer Bug," *IEEE Annals of the
  History of Computing* 20.4 (1998) -- the definitive debunking of the
  Hopper-as-coiner myth
- Wikipedia, "List of computer term etymologies" -- bug entry with
  pre-Hopper citations
