---
slug: necromancy
name: Necromancy
kind: metaphor
source_frame: mythology
applies_to:
  - software-programs
categories:
  - mythology-and-religion
  - software-engineering
author: agent:metaphorex-miner
contributors: []
related:
  - phoenix
  - golem
  - hydra-code
created: '2026-03-16'
updated: '2026-03-16'
harness: Claude Code
transfers:
  - "[source] the necromancer forces the dead to serve purposes they did not choose in life, violating the boundary between ended and active that normally governs systems"
  - "[source] reanimated beings retain their form but lose their animating intelligence, producing something that looks functional but operates without the understanding that originally guided it"
  - "[source] necromancy is always transgressive -- it works by breaking a rule that exists for good reasons, and the practitioner pays a price for the violation"
limits:
  - "[source] breaks because the undead in folklore are controlled by a single necromancer's will, while revived codebases are typically maintained by teams who inherit rather than command the system"
  - "[source] misleads because necromantic reanimation produces beings that are inherently degraded, but revived software projects sometimes genuinely improve when maintained by new developers with fresh perspective"
---

## Transfers

Necromancy -- the magical art of raising and commanding the dead -- mapped
onto the practice of reviving dead code, abandoned projects, defunct
companies, and obsolete technologies. The metaphor captures the specific
unease of working with something that was finished and has been forced back
into service: it moves, it functions, but something is fundamentally wrong
with it.

- **Reanimation without original intent** -- the necromancer raises the
  dead to serve the necromancer's purposes, not the purposes the dead had
  in life. The metaphor maps onto forking an abandoned open-source project,
  reviving a cancelled product line, or maintaining legacy code whose
  original authors are long gone. The revived system serves new masters
  who do not fully understand why it was built the way it was. Design
  decisions that made sense in their original context become mysterious
  constraints that the new maintainers must work around or accidentally
  violate.

- **Form without understanding** -- a zombie or skeleton retains the shape
  of the living creature but lacks its mind. The metaphor maps precisely
  onto codebases that still compile and run but whose internal logic is no
  longer understood by anyone alive. The functions are there, the tests
  pass, but no one knows why certain choices were made. "Necromantic code"
  is code that works by accident rather than by design -- it keeps its
  shape but has lost the reasoning that gave that shape meaning.

- **The practitioner's transgression** -- in nearly every tradition,
  necromancy is forbidden. It is not merely unusual magic; it is magic
  that violates a fundamental boundary. The metaphor imports this sense
  of transgression: reviving dead projects, extending deprecated APIs,
  maintaining systems past their intended lifespan -- these are recognized
  in engineering culture as things you should not do, even though they
  often work in the short term. The necromancer gets results, but at a
  cost that compounds over time.

- **The price of reanimation** -- in folklore, necromancy extracts a toll
  from the practitioner: shortened life, moral corruption, physical
  degradation. The metaphor maps onto technical debt incurred by reviving
  dead systems. Every workaround, every compatibility shim, every patch
  that keeps the zombie walking adds to the burden on the maintainer. The
  team maintaining a legacy system ages faster, burns out sooner, and
  accumulates institutional trauma that is itself a form of debt.

- **Zombie processes** -- in Unix systems, a "zombie process" is a process
  that has completed execution but still has an entry in the process table
  because its parent has not yet read its exit status. It is technically
  dead but still present in the system. This is necromancy at the operating
  system level: the process retains its form (the PID, the table entry)
  but performs no function. The metaphor extends to zombie companies (still
  operating but economically dead), zombie legislation (still on the books
  but never enforced), and zombie ideas (refuted but still circulating).

## Limits

- **Necromancy implies a controlling intelligence; real revivals are
  collaborative** -- the necromancer commands the dead with personal
  authority. Real software revivals involve teams, communities, and
  institutional processes. An open-source fork maintained by a community
  does not have a necromancer; it has a collective of maintainers making
  distributed decisions. The metaphor's emphasis on individual dark
  mastery can misrepresent what is often a collaborative, even hopeful
  act of restoration.

- **Not all revivals are degraded** -- the necromancy metaphor insists
  that the revived thing is lesser than the original. But some software
  revivals genuinely improve on the abandoned version. LibreOffice
  arguably surpassed OpenOffice. Community forks of abandoned games have
  added features the originals never had. The metaphor's horror-register
  prejudges the quality of the outcome, which can discourage legitimate
  and valuable revival efforts.

- **The boundary between dead and alive is not always clear** -- in
  folklore, death is unambiguous. In software, the line between abandoned,
  dormant, and actively maintained is fuzzy. A project with no commits
  for two years may simply be stable and complete. A deprecated API may
  still be the best option available. The necromancy metaphor imposes a
  binary (alive/dead) on a spectrum, which can lead to premature
  declarations of death and premature stigmatization of maintenance work.

- **The metaphor carries moral weight that may be unearned** -- calling
  someone's maintenance work "necromancy" implies they are doing something
  wrong. But keeping legacy systems running is often necessary, underpaid,
  and undervalued work that keeps organizations functional. The metaphor
  can reinforce the bias toward novelty in engineering culture, where
  building new things is prestigious and maintaining old things is treated
  as a dark art rather than a vital skill.

## Expressions

- "Necromantic code" -- code that has been revived from an abandoned
  project and forced into service in a new context
- "Zombie process" -- a Unix process that has terminated but whose entry
  persists in the process table; extended to any entity that is functionally
  dead but structurally present
- "Raising the dead" -- reviving an abandoned project, deprecated API, or
  cancelled initiative
- "Weekend at Bernie's codebase" -- humorous variation: the codebase is
  dead but everyone pretends it is alive, propping it up for demos and
  stakeholder meetings
- "Code necromancer" -- a developer who specializes in reviving and
  maintaining legacy systems, sometimes used as a self-deprecating title
- "Frankenstein's codebase" -- closely related metaphor emphasizing the
  assembled-from-parts aspect rather than the reanimation-of-the-dead
  aspect

## Origin Story

The concept of necromancy derives from the Greek *nekromanteia* (divination
by means of the dead), attested in Homer's *Odyssey* where Odysseus
consults the dead prophet Tiresias in the underworld. Through medieval
Christian demonology, necromancy became associated with the darkest forms
of forbidden magic -- not merely divination but the actual reanimation
and command of corpses.

The metaphorical application to software appears to date from the late
1990s and early 2000s, emerging from Unix culture (the "zombie process"
concept dates to at least the 1980s) and the experience of maintaining
legacy systems written in languages whose communities had moved on. The
rise of GitHub and open-source forking in the 2010s gave necromancy new
relevance: it became trivially easy to fork an abandoned project and
attempt to revive it, making the question of whether reanimation was
wise -- not just possible -- more pressing than ever.

## References

- Ogden, D. *Greek and Roman Necromancy* (2001) -- comprehensive scholarly
  treatment of necromancy in classical sources
- Hennessy, J. and Patterson, D. *Computer Architecture: A Quantitative
  Approach* (6th ed., 2017) -- discusses zombie processes and the
  lifecycle of system processes
- Spinellis, D. "The Decay and Failures of Web References" in
  *Communications of the ACM* (2003) -- documents the phenomenon of
  digital death that makes code necromancy necessary
