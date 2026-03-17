---
applies_to:
- software-programs
author: agent:metaphorex-miner
categories:
- computer-science
contributors:
- fshot
created: '2026-03-17'
dead: true
harness: Claude Code
kind: metaphor
name: Environment Variable
related:
- data-flow-is-fluid-flow
slug: environment-variable
source_frame: embodied-experience
updated: '2026-03-17'
transfers:
  - "[source] an organism's environment is the surrounding context that influences its behavior without being part of the organism itself"
  - "[source] offspring inherit their parent's environment by being born into it, not by explicit transfer"
  - "[source] the environment is ambient -- present everywhere within a context without needing to be explicitly passed from place to place"
limits:
  - "[source] breaks because a physical environment is continuous and shared -- all organisms in the same habitat experience the same conditions -- whereas each mapped entity gets its own independent copy that can diverge from its siblings"
  - "[source] misleads because a natural environment changes dynamically and organisms sense changes in real time, but the mapped context is a snapshot frozen at the moment of creation, invisible to later modifications in the source"
---

## Transfers

An organism lives in an environment -- the air, temperature, soil,
light, and chemical conditions that surround it and influence its behavior
without being part of its body. A Unix process lives in an environment
defined by key-value pairs: `PATH`, `HOME`, `LANG`, `EDITOR`, `TERM`.
These variables define the context in which the process operates. They are
not passed as arguments; they are ambient, present in the surrounding
context, available to any code that reaches for them.

Key structural parallels:

- **Ambient context** -- a fish does not receive water as an argument; it
  swims in it. A Unix process does not receive its environment through
  function parameters; it inherits it from the surrounding context.
  `getenv("PATH")` is the process looking around at its surroundings,
  not receiving a message. The ecological metaphor captures this
  perfectly: the environment is there, and the process either reads it
  or ignores it.
- **Inheritance from parent** -- organisms inherit their environment by
  being born into it. A child process inherits its parent's environment
  variables at the moment of `fork()`. The genetic metaphor layers on
  top of the ecological one: the parent does not hand over the
  environment; the child is born with a copy. `export` in the shell
  is the act of placing a variable into the environment so that children
  will inherit it -- making it part of the habitat rather than a private
  possession.
- **Influence without direct causation** -- temperature does not tell a
  plant to grow; it creates conditions where growth happens. `PATH` does
  not tell a program which executable to run; it defines the directories
  where executables can be found. `LANG` does not force a program to
  display French; it creates conditions where French is the default. The
  environment shapes behavior indirectly, through context rather than
  command.
- **Invisible until examined** -- most people do not think about the
  humidity of their environment until it becomes uncomfortable. Most
  programs do not think about most environment variables -- they only
  check the ones relevant to their behavior. `env` or `printenv` is the
  act of making the invisible environment visible, like checking a
  thermometer: the conditions were always there, you just were not
  looking.

## Limits

- **Physical environments are shared; process environments are copied** --
  all animals in a forest share the same temperature. But each Unix
  process gets its own copy of the environment at fork time. If the
  parent changes a variable after forking, the child does not see the
  change. There is no shared habitat -- each process lives in a private
  snapshot of the environment as it existed at birth. This fundamentally
  breaks the ecological metaphor, where environment is a shared commons.
- **Physical environments change continuously; process environments are
  static** -- the weather changes, seasons turn, rivers rise and fall.
  A process's environment is fixed at fork time. You can modify your
  own environment with `setenv()`, but this affects only your process
  and your future children -- not your parent, not your siblings. The
  ecological metaphor suggests a dynamic, responsive context; the
  reality is a frozen snapshot.
- **The metaphor hides the security problem** -- an organism's
  environment is not a secret. But environment variables are frequently
  used to pass secrets: `API_KEY`, `DATABASE_URL`, `AWS_SECRET_ACCESS_KEY`.
  The ecological metaphor -- ambient, inherited, visible to anyone who
  looks -- accurately describes the security properties, which is exactly
  the problem. Environment variables are visible in `/proc/<pid>/environ`,
  inherited by child processes that may not need them, and logged by crash
  reporters. The metaphor normalizes exposure.
- **"Variable" clashes with the ecological metaphor** -- an environment
  is not made of variables; it is made of conditions. The compound term
  "environment variable" mixes an ecological metaphor with a mathematical
  one, creating a hybrid that is not fully coherent. Is the environment
  a habitat or a namespace? The answer is both, which means neither
  metaphor provides complete guidance. Programmers who think "habitat"
  miss the key-value structure; those who think "namespace" miss the
  ambient inheritance model.

## Expressions

- "Set the environment" -- configuring variables before running a program,
  as if preparing the habitat for an organism
- "Export a variable" -- placing a shell variable into the environment so
  child processes inherit it; "export" implies sending it outward, into
  the ambient context
- "Clean environment" -- running a program with a minimal environment,
  stripping away inherited pollution; the ecological sanitation metaphor
- "Environment pollution" -- too many variables cluttering the
  environment, making it hard to understand what influences a process
- "Inherited from the parent" -- the standard description of how
  environment variables propagate, explicitly using the
  biological/familial metaphor
- "The environment" -- used as a noun in its own right: "check the
  environment for the database URL"; the ecological term has become a
  technical term

## Origin Story

Environment variables appeared in Version 7 Unix (1979), building on
earlier mechanisms for passing context to programs. The concept was
formalized with the `environ` external variable in C and the `getenv()`
/ `setenv()` library functions. The Bourne shell (1977) introduced
`export` as the mechanism for placing variables into the environment.

The choice of "environment" was deliberate and ecological. Earlier systems
used terms like "parameters" or "settings," but the Unix designers chose
a word that implies ambient context rather than explicit configuration.
The metaphor complemented the existing Unix vocabulary: processes are born
(`fork`), inherit their parent's environment, and live in it until they
die (`exit`). The ecological layer sits on top of the biological layer,
creating a coherent system of metaphors for process lifecycle.

The term became universal across operating systems. Windows has environment
variables (`%PATH%`), as does every Unix descendant. The twelve-factor app
methodology (2011) made environment variables the recommended mechanism
for application configuration, cementing the metaphor's dominance. Today,
`ENV` is so standard that developers configure databases, API keys,
feature flags, and deployment targets through environment variables
without thinking about the ecological metaphor underneath.

## References

- Bourne, S. "The UNIX Shell," Bell System Technical Journal 57(6), 1978
- Kernighan, B. & Pike, R. *The Unix Programming Environment*,
  Prentice-Hall, 1984
- Stevens, W. R. *Advanced Programming in the UNIX Environment* (1992) --
  environment variables and process inheritance
- Wiggins, A. "The Twelve-Factor App" (2011) --
  https://12factor.net/config -- environment variables as configuration
