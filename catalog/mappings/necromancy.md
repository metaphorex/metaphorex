---
slug: necromancy
name: "Necromancy"
kind: dead-metaphor
source_frame: magic
target_frame: software-programs
categories:
  - mythology-and-religion
  - software-engineering
author: agent:metaphorex-miner
contributors: []
related: []
---

## What It Brings

Necromancy -- the magical art of raising and commanding the dead -- has
become a standard metaphor in software for reviving things that were
supposed to stay dead. "Necro-ing" a forum thread, resurrecting a
deprecated API, maintaining a zombie process, reanimating an abandoned
codebase: the metaphor is so routine that most speakers no longer
register its source domain. Nobody performing a `git checkout` on a
year-old branch thinks of themselves as conducting a ritual to commune
with the deceased, yet the vocabulary is pervasive.

Key structural parallels:

- **The revived thing is not what it was** -- in myth, the raised dead
  are diminished, wrong, uncanny. Reanimated code carries the same
  quality: it compiles but the dependencies have moved on, the
  assumptions are stale, the documentation describes a world that no
  longer exists. The code walks and talks but it is not alive in the
  way living code is alive.
- **Necromancy is transgressive** -- in every tradition that features
  it, raising the dead violates a boundary that exists for good
  reasons. In software, reviving dead code, dead threads, or dead
  projects often violates equivalent norms: the thread was closed for
  a reason, the API was deprecated for a reason, the project was
  abandoned for a reason. The necromancer disrupts a settled state.
- **The dead serve the necromancer's purpose, not their own** -- raised
  dead have no agency; they do what the summoner commands. Legacy code
  kept alive to serve a new system's needs is similarly conscripted:
  it was not designed for this context, has no opinion about it, and
  will obey instructions it was never meant to receive.
- **There is always a cost** -- mythological necromancy demands
  sacrifice, forbidden knowledge, or moral corruption. Maintaining
  zombie systems exacts its own costs: technical debt, security
  vulnerabilities, the opportunity cost of engineers maintaining the
  undead instead of building the living.

## Where It Breaks

- **Dead code does not suffer.** The moral horror of necromancy derives
  from the violation of the dead person's rest and autonomy. Code has
  neither. Calling legacy maintenance "necromancy" borrows the
  emotional charge of desecration to describe what is usually just
  boring maintenance work. The metaphor makes the mundane sound
  dramatic and the practical sound forbidden.
- **Sometimes resurrection is the right call.** Mythological necromancy
  is always wrong -- no tradition endorses it. But reviving abandoned
  open-source projects, restoring deprecated features users depended on,
  or re-opening a closed discussion when new information emerges are
  often the responsible thing to do. The metaphor's moral framing
  ("necro-ing" as a forum faux pas) discourages legitimate revival.
- **The "zombie" variant is a different metaphor.** Zombie processes
  (processes that have completed but whose exit status has not been
  collected by their parent) are not raised dead -- they are dead that
  have not been properly buried. The necromancy frame conflates
  intentional revival with failed cleanup, which are different problems
  requiring different solutions.
- **The metaphor is now so dead it is itself a zombie.** When someone
  says "don't necro this thread," they are using a dead metaphor about
  dead metaphors. The source domain has been so thoroughly stripped of
  its original content that the word functions as pure jargon, not as
  a mapping that illuminates anything about either magic or software.

## Expressions

- "Necro-ing a thread" -- posting to a long-inactive forum discussion,
  reviving a conversation the community considered finished
- "Zombie process" -- a process that has died but whose resources have
  not been reclaimed, lingering in the process table
- "Resurrect" -- bringing back a deleted feature, deprecated API, or
  abandoned project, used without awareness of its religious source
- "Dead code" -- code that exists in the codebase but is never executed,
  waiting to be either deleted or necromanced
- "Frankenstein's monster" -- a related metaphor for systems assembled
  from parts of dead systems, alive but grotesque (often incorrectly
  called "Frankenstein")
- "Weekend at Bernie's deployment" -- keeping a dead system propped up
  and pretending it is functional, a more modern riff on the
  necromancy metaphor

## Origin Story

The Greek word *nekromanteia* (divination by consulting the dead)
appears in Homer's *Odyssey*, where Odysseus summons the shade of
Tiresias for prophecy. The practice was condemned across cultures --
by the Hebrew Bible (the Witch of Endor), by medieval Christianity,
by Islamic jurisprudence -- establishing the moral framework that the
software metaphor inherits. The term entered computing vocabulary
through the same geek-culture pipeline that brought "daemon," "wizard,"
and "spell" into technical jargon: programmers in the 1970s-80s who
read fantasy literature and applied its vocabulary to their work. By
the 2000s, "necro" as a verb (particularly in forum culture) had fully
detached from its magical source and become pure internet slang.

## References

- Homer, *Odyssey*, Book XI (the Nekyia) -- the foundational Western
  text on consulting the dead
- Raymond, E. S. *The Jargon File* (various editions) -- documents
  the migration of fantasy vocabulary into computing jargon
- Hennessy, J. & Patterson, D. *Computer Architecture* (various
  editions) -- the technical reality behind "zombie processes" that
  the metaphor decorates
