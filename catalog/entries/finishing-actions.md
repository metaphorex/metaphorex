---
slug: finishing-actions
name: Finishing Actions
kind: mental-model
source_frame: food-and-cooking
categories:
  - organizational-behavior
  - systems-thinking
author: agent:metaphorex-miner
contributors: []
related:
  - mise-en-place
  - cleaning-as-you-go
  - prep
dead: false
created: '2026-03-21'
updated: '2026-03-21'
grounding: established
harness: Claude Code
provenance: culinary-mise-en-place
transfers:
  - '[model] completing a task through its full lifecycle -- including cleanup, filing, and handoff -- before starting the next task eliminates the hidden overhead of resumption, because incomplete tasks accumulate cognitive and physical carrying costs that grow with each unfinished item'
  - '[model] batching similar finishing actions (wiping all stations at once, filing all documents at once) reduces context-switching cost only when the batch is completed in its entirety, because an interrupted batch is worse than unbatched individual completion'
  - '[model] the decision to "finish later" is itself a task that consumes working memory -- tracking what is unfinished, where it was left, and what remains to be done -- so deferring completion creates invisible overhead that makes the next primary task slower'
limits:
  - '[model] assumes that tasks have clear, discrete endpoints where "finished" is unambiguous -- breaks in creative, research, or design work where quality is asymptotic and no objective completion criterion exists, leading to either premature closure or perfectionist loops'
  - '[model] the principle''s emphasis on completing before switching conflicts with legitimate interleaving strategies where partial progress on multiple fronts yields better outcomes than serial completion, such as letting ideas incubate or waiting for external dependencies'
---

## Transfers

"Finishing Actions" is the fifth of Dan Charnas's ten *Work Clean*
principles, derived from the professional kitchen's discipline of
completing tasks through their full cycle before moving to the next
one. In the kitchen, this means: when you chop the onions, sweep the
trimmings into the bin, wipe the board, and put the prep container in
its designated position before pulling out the next ingredient. When
you plate a dish, deliver it to the pass, wipe down, and reset your
station before reading the next ticket. Every action has a beginning,
a middle, and a finishing action -- and the finishing action is the
one most often skipped under pressure.

Key structural parallels:

- **Incomplete work has carrying costs** -- the core insight is that
  a task left at 90% completion does not cost 10% to finish later; it
  costs more, because returning to it requires reconstructing context.
  Where did I leave off? What was the next step? Where did I put the
  half-chopped herbs? In the kitchen, the carrying cost is physical: a
  half-prepped station clutters the workspace and creates confusion
  during service. In knowledge work, the carrying cost is cognitive:
  each unfinished task occupies a slot in working memory (what
  psychologists call the Zeigarnik effect), reducing capacity for the
  current task. Finishing actions eliminate these carrying costs by
  driving each task to zero residual obligation before starting the
  next.

- **The last 10% is the most important 10%** -- finishing actions are
  the cleanup, filing, communication, and handoff that happen after
  the "real work" is done. In the kitchen: you cooked the dish, but
  did you wipe the rim of the plate? Did you reset your station? Did
  you call "ready" to the expediter? In software: you wrote the code,
  but did you update the documentation? Close the ticket? Notify the
  stakeholder? The principle recognizes that the final steps of a task
  are the ones most easily deferred and most costly when deferred,
  because they are the interface between your work and the next
  person's work.

- **Batching is valid only if the batch completes** -- the principle
  does not oppose batching similar tasks. A cook who needs to dice
  onions, carrots, and celery for three different recipes should dice
  all three consecutively (same tool, same motion, same station setup).
  But the batch must finish: all three diced, all three stored, all
  trimmings cleared, board wiped. An interrupted batch -- two diced,
  one still whole, board cluttered -- is worse than no batching at all,
  because the in-progress state of the batch adds its own carrying
  cost on top of the unfinished items.

- **The Zeigarnik overhead is real and measurable** -- Bluma Zeigarnik
  demonstrated in 1927 that incomplete tasks occupy cognitive resources
  disproportionate to their size. The kitchen quantifies this: a cook
  with three unfinished tasks is measurably slower on the current task
  than a cook with zero, even when the current task is identical. The
  mental model makes this overhead a first-class design constraint
  rather than a personality trait ("some people are just better at
  finishing things").

## Limits

- **Not all tasks have clear endpoints** -- the principle works in the
  kitchen because culinary tasks have unambiguous completion criteria:
  the onion is diced or it is not, the plate is wiped or it is not.
  Many knowledge-work tasks lack this property. When is a design
  "finished"? When is a document "done"? When is code "clean enough"?
  Applying finishing-actions discipline to tasks without clear endpoints
  either forces premature closure (shipping before the work is ready)
  or enables perfectionist loops (endlessly finishing what cannot be
  finished).

- **Serial completion is not always optimal** -- the principle assumes
  that the best strategy is to finish task A completely before starting
  task B. But some work benefits from interleaving: writing a first
  draft, then switching to a different problem while the draft
  incubates, then returning to revise with fresh perspective.
  Scientific research often requires running multiple experiments in
  parallel, not because of poor discipline but because waiting for
  results creates idle time that parallel work can fill. The principle
  is designed for the kitchen's fast-cycle, sequential work and
  transfers poorly to domains with long feedback loops.

- **WIP limits are not the same as finishing actions** -- the principle
  is sometimes conflated with work-in-progress limits from lean and
  Kanban. Both reduce concurrent work, but the mechanisms differ. WIP
  limits constrain how much work enters the system. Finishing actions
  constrain how work exits. A team can have strict WIP limits and still
  defer finishing actions within each work item (writing code but not
  tests, building features but not documentation). The principle
  addresses a finer grain than WIP limits and should not be treated as
  redundant with them.

- **Urgency can legitimately override completion** -- in the kitchen
  itself, finishing actions are sometimes correctly abandoned. When the
  chef calls an on-the-fly order, the cook drops their current task
  mid-finish to address the emergency. The principle does not claim
  that finishing is always correct, but practitioners sometimes apply
  it rigidly, resisting legitimate interruptions because "I need to
  finish this first." The model should include an override mechanism
  for genuine emergencies, which the kitchen provides but the
  productivity formulation often omits.

## Expressions

- "Finish the action" -- kitchen instruction to complete through
  cleanup, not just through cooking
- "Don't leave it hanging" -- exhortation to complete the finishing
  actions rather than walking away at 90%
- "Close the loop" -- general organizational term for completing the
  communication and handoff that constitute finishing actions
- "That task is done done" -- software team vernacular distinguishing
  code-complete from truly finished (tested, documented, deployed)
- "Reset your station" -- the paradigmatic finishing action in the
  kitchen, ensuring readiness for the next task

## Origin Story

Charnas formulated "Finishing Actions" as the fifth *Work Clean*
principle by observing the discipline professional chefs enforce on
their cooks: every task ends with a reset. The station is wiped. The
tools are returned. The next task begins from a clean state. Charnas
connected this to Bluma Zeigarnik's 1927 research on incomplete
tasks and to David Allen's Getting Things Done methodology, which
similarly emphasizes driving tasks to completion or to a clearly
defined "next action" to free cognitive resources. The culinary
formulation adds a physical, embodied dimension that Allen's
information-processing model lacks: the finishing action is not just
a cognitive commitment but a bodily practice -- the hand wiping the
board, the arm returning the container to its place.

## References

- Charnas, D. *Work Clean: The Life-Changing Power of Mise-en-Place*
  (2016) -- the principle as formulated
- Zeigarnik, B. "On Finished and Unfinished Tasks" (1927) -- the
  cognitive cost of incomplete tasks
- Allen, D. *Getting Things Done* (2001) -- the "open loop" concept
  and cognitive overhead of undone work
- Anderson, D.J. *Kanban: Successful Evolutionary Change for Your
  Technology Business* (2010) -- WIP limits as a related but distinct
  mechanism
