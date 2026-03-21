---
slug: coming-to-zero
name: Coming to Zero
kind: mental-model
source_frame: food-and-cooking
categories:
- organizational-behavior
- software-engineering
author: agent:metaphorex-miner
contributors: []
related:
- mise-en-place
- stretch-it
created: '2026-03-19'
updated: '2026-03-19'
grounding: folk
harness: Claude Code
provenance: culinary-mise-en-place
transfers:
  - '[model] defines a periodic reset to a known clean state as a first-class work practice rather than an occasional cleanup, distinguishing between the entropy that accumulates during a work session and the deliberate act of reversing it'
  - '[model] establishes that the reset must be complete -- partial clearing creates a false sense of order that is worse than acknowledged mess, because residual items from the previous cycle contaminate the next one'
  - '[model] frames the reset as a cognitive transition marker that separates one work epoch from another, making it possible to begin the next cycle without carrying forward the attentional residue of the previous one'
limits:
  - '[model] breaks in domains where accumulated state is the product rather than waste -- a researcher''s cluttered desk may contain spatial arrangements that encode relationships between ideas, and zeroing it destroys information'
  - '[model] assumes the clean state is quickly achievable, but in complex systems (code repositories, organizational processes, infrastructure) the cost of returning to zero can exceed the cost of the entropy it would eliminate'
embodied_patterns:
  - removal
  - iteration
  - boundary
relation_types:
  - restore
  - coordinate
structure: cycle
abstraction_level: specific
---

## Transfers

In professional kitchens, "coming to zero" means periodically
clearing your station back to its pristine pre-service state:
wiping surfaces, discarding spent ingredients, returning tools to
their designated positions, restocking depleted mise en place.
Charnas identified this as a distinct practice from mise en place
itself -- mise en place is the initial setup; coming to zero is the
periodic reset during and after service. The cook does not wait
until the end of the night to clean. They reset between tickets,
between courses, between rushes.

Key structural parallels:

- **Entropy is a work product** -- every task generates disorder as
  a byproduct. A cook who plates three entrees has dirty pans, food
  scraps, and displaced tools. A developer who ships a feature has
  open browser tabs, stale branches, draft documents, and Slack
  threads. Coming to zero treats this accumulated disorder not as a
  moral failing but as a predictable output of productive work that
  must be systematically reversed. The model normalizes cleanup as
  part of the work cycle rather than something separate from "real
  work."

- **The reset is complete, not partial** -- a half-cleaned station
  is worse than a visibly dirty one, because the cook might assume
  a contaminated surface is clean. Coming to zero demands totality:
  everything back to the known state, no exceptions. The inbox-zero
  methodology captures this: the inbox is either at zero or it
  isn't. Marking emails as read without processing them creates a
  false zero that guarantees future failures. The model insists
  that the reset is binary -- you are at zero or you are not.

- **The reset marks a cognitive boundary** -- the physical act of
  clearing the station signals to the cook's brain that the
  previous rush is over and the next one has not begun. This
  transition ritual provides the same function as a commit in
  version control: a checkpoint that separates "before" from
  "after." Without it, the cook carries forward the stress and
  attentional residue of the last rush into the next one. In
  knowledge work, the equivalent is the end-of-day shutdown
  ritual: close all applications, clear the desk, write tomorrow's
  task list. The reset is not just physical but psychological.

- **Frequency matters more than thoroughness** -- a quick wipe
  between every ticket prevents the station from ever reaching
  chaos. A deep clean only at the end of the night means working
  through progressively worse disorder all evening. The model
  argues that small, frequent resets are more effective than rare,
  thorough ones. In software, this is the argument for frequent
  small commits over infrequent large ones, for daily standups
  over weekly status meetings, for continuous deployment over
  quarterly releases.

- **The known state must be defined** -- you cannot come to zero
  unless zero is specified. In a kitchen, zero is defined by the
  mise en place setup: each tool in its place, each container at
  its mark, each surface clean. In software, zero might be "all
  tests pass, no open PRs, inbox cleared, Jira board current."
  The model requires that the clean state be explicitly defined,
  not left to individual interpretation.

## Limits

- **Accumulated state is sometimes the product** -- a researcher's
  desk covered in papers, sticky notes, and open books may look
  disordered but encode a spatial arrangement that reflects the
  structure of their thinking. A developer with twenty open tabs
  may be maintaining a mental model of a complex system. Coming to
  zero would destroy this information. The model assumes that
  accumulated state is waste, but in creative and analytical work,
  it is sometimes the most valuable artifact of the work session.

- **The cost of resetting can exceed the cost of entropy** -- in a
  kitchen, wiping a station takes seconds. In a complex software
  system, "returning to zero" might mean rebasing branches, closing
  stale PRs, archiving documents, and reconciling divergent
  configurations -- hours of work that could be spent on new
  features. The model assumes a low reset cost, and fails when
  the reset is expensive relative to the work it enables.

- **The model assumes a repeating cycle** -- kitchens have service
  rushes that start and end predictably. Many knowledge work contexts
  do not have natural boundaries: the inbox is never empty for long,
  the code repository never stops receiving commits, the Slack
  channel never goes quiet. Applying coming-to-zero to a continuous
  flow requires artificially imposing boundaries (end of day, end of
  sprint) that the work itself does not respect.

- **Zero can become a procrastination tool** -- the ritual of
  cleaning and resetting can feel productive while actually deferring
  the difficult work that created the mess. A developer who spends
  thirty minutes "clearing their workspace" before writing code may
  be engaging in sophisticated procrastination. The model does not
  distinguish between reset-as-preparation and reset-as-avoidance.

## Expressions

- "Inbox zero" -- Merlin Mann's productivity methodology, which is
  coming-to-zero applied to email
- "Clean as you go" -- the culinary version, emphasizing frequency
  over thoroughness
- "Wipe down" -- the physical act of station reset, metaphorically
  applied to workspace clearing in any domain
- "Start fresh" -- the cognitive benefit of the reset, framed as
  a new beginning rather than a cleanup
- "Reset to known good state" -- the engineering formulation:
  return the system to a state where all invariants hold
- "End-of-day shutdown" -- Cal Newport's productivity ritual,
  structurally identical to coming-to-zero

## Origin Story

Dan Charnas identified "coming to zero" as a distinct practice
within the mise-en-place philosophy in *Work Clean: The
Life-Changing Power of Mise-en-Place* (2016). Charnas observed
that master chefs did not simply set up their stations before
service; they periodically reset them during service, maintaining
a discipline of returning to the clean state between rushes.
Charnas drew explicit connections to Merlin Mann's inbox-zero
methodology, Cal Newport's shutdown rituals, and David Allen's
Getting Things Done weekly reviews, arguing that all of these
were instances of the same structural practice: periodic complete
reset to a known clean state.

The practice itself is far older than Charnas's naming of it.
Escoffier's brigade system, formalized in the late nineteenth
century, implicitly required station resets between courses. But
Charnas was the first to extract the practice from its culinary
context, give it a name, and argue for its transferability.

## References

- Charnas, Dan. *Work Clean: The Life-Changing Power of
  Mise-en-Place* (2016) -- the primary source for the concept
  and its name
- Mann, Merlin. "Inbox Zero" (2006) -- the email productivity
  methodology that is structurally identical
- Newport, Cal. *Deep Work* (2016) -- the shutdown ritual as a
  daily coming-to-zero practice
- Allen, David. *Getting Things Done* (2001) -- the weekly review
  as a periodic reset
