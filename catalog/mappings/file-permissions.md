---
slug: file-permissions
name: "File Permissions"
kind: dead-metaphor
source_frame: governance
target_frame: access-control
categories:
  - computer-science
author: agent:metaphorex-miner
harness: "Claude Code"
contributors: []
related:
  - everything-is-a-file
---

## What It Brings

Unix file permissions import the vocabulary and logic of institutional
governance into the operating system. Every file has an owner, belongs
to a group, and is exposed to "others" -- a three-tier social hierarchy
borrowed directly from how organizations regulate access to resources.
The three permission types -- read, write, execute -- map onto three
kinds of sanctioned activity, each independently grantable or
revocable. The entire system reads like a miniature constitution: who
may do what, under whose authority.

Key structural parallels:

- **Owner, group, others as a social hierarchy** -- in governance, access
  to resources is tiered: the property owner has the most control, a
  defined group (a department, a family, a guild) has delegated access,
  and the general public gets whatever remains. Unix maps this exactly:
  the file's owner sets the rules, the group gets a separate set of
  permissions, and everyone else gets a third. The three-tier model is
  a direct import from institutional access control, not an invention
  of computer science.
- **Permissions as grants of authority** -- "permission" is itself a
  governance term. To "grant read access" is the language of a sovereign
  or administrator authorizing a subject to perform an action. The Unix
  `chmod` command -- "change mode" -- even echoes the bureaucratic
  language of modifying an access policy. The metaphor frames the
  operating system as an authority that can give and take away rights.
- **The superuser as sovereign** -- root can override any permission,
  read any file, modify any setting. This maps the concept of sovereign
  immunity onto the system administrator: a power above the rules,
  justified by necessity, constrained only by convention. The metaphor
  imports both the utility and the danger of unchecked authority.
- **The octal notation as bureaucratic encoding** -- permissions are
  represented as three-digit octal numbers (755, 644), a compact
  encoding that is opaque to outsiders but fluent to insiders. This
  mirrors how institutional rules get encoded in regulatory shorthand
  that only practitioners can read.

## Where It Breaks

- **Governance is negotiable; Unix permissions are absolute** -- in
  real governance, access decisions involve context, appeals,
  exceptions, and judgment. A librarian might grant a researcher
  special access to restricted materials based on stated purpose. Unix
  permissions have no concept of context or appeal: you either have the
  bit set or you don't. The metaphor imports the vocabulary of
  governance but strips out the deliberative process that makes
  governance work. Access control lists (ACLs) were later bolted on to
  address this rigidity, but they feel like an afterthought because the
  original metaphor did not accommodate nuance.
- **Three tiers are not enough** -- real organizations have complex,
  overlapping jurisdictions: departments, project teams, temporary
  committees, external partners. Unix's owner/group/others model
  provides exactly one group per file. A file that needs to be
  accessible to both the engineering team and the marketing team
  requires workarounds (supplementary groups, ACLs, directory
  permissions) because the metaphor borrowed a simplified version of
  governance that does not reflect how actual organizations structure
  access.
- **Execute permission has no governance analog** -- "read" and "write"
  map cleanly onto governance concepts (the right to inspect, the
  right to modify). But "execute" -- the right to run a file as a
  program -- has no natural analog in institutional access control. You
  do not "execute" a document in a filing cabinet. This is where the
  metaphor stretches beyond its source domain, and it causes real
  confusion: new users struggle to understand why a shell script needs
  both read and execute permission, because the governance metaphor
  provides no intuition for the distinction.
- **The metaphor obscures the implementation** -- permissions feel like
  properties of files, but they are actually properties of inodes. Hard
  links share permissions because they share an inode. This surprises
  users because the governance metaphor suggests each "document" has its
  own access policy, when in reality the policy is attached to the
  underlying storage object, not the name.

## Expressions

- "chmod 755" -- granting owner full access, group and others read and
  execute; the incantation that every Unix user learns by rote, often
  without understanding the governance metaphor embedded in the numbers
- "Permission denied" -- the system's refusal, phrased exactly as an
  institutional authority would phrase it
- "You don't have permission to do that" -- the anthropomorphized
  system speaking as a gatekeeper
- "Run as root" -- escalating to the sovereign authority level to bypass
  the normal permission hierarchy
- "World-readable" -- a file accessible to "others," using "world" as
  the governance term for the general public
- "Setuid" -- granting a program the permissions of its owner rather
  than its executor, a delegation of authority that maps onto the
  governance concept of acting "on behalf of" a higher authority

## Origin Story

Unix file permissions were designed by Ken Thompson and Dennis Ritchie
at Bell Labs as part of the original Unix filesystem (1969-1971). The
owner/group/others model reflected the multi-user environment at Bell
Labs, where researchers needed to share a single machine while
protecting their work from accidental interference. The three-tier
model was a pragmatic simplification of the more complex access control
systems in Multics, Unix's predecessor. Where Multics offered elaborate
access control lists, Unix compressed everything into nine bits -- three
permissions for three classes of user -- a design choice that
privileged simplicity over expressiveness. The governance metaphor was
never stated explicitly; it was simply the natural language for talking
about who gets to do what with shared resources.

## References

- Ritchie, D. & Thompson, K. "The UNIX Time-Sharing System," *CACM*
  17(7), 1974
- Kernighan, B. & Pike, R. *The Unix Programming Environment*,
  Prentice-Hall, 1984
- Saltzer, J. & Schroeder, M. "The Protection of Information in
  Computer Systems," *Proceedings of the IEEE* 63(9), 1975
