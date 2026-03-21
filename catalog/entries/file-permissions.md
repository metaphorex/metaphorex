---
slug: file-permissions
name: File Permissions
kind: metaphor
dead: true
source_frame: governance
applies_to:
  - data-processing
categories:
  - computer-science
author: agent:metaphorex-miner
contributors:
  - fshot
related:
  - filesystem-root
  - filesystem-tree
created: '2026-03-17'
updated: '2026-03-17'
harness: Claude Code
grounding: folk
embodied_patterns:
  - boundary
  - container
  - part-whole
relation_types:
  - contain
  - prevent
structure:
  - hierarchy
  - boundary
abstraction_level: specific
transfers:
  - "[source] access is granted or withheld by an owner according to a three-tier social hierarchy of owner, group, and others"
  - "[source] the sovereign (superuser) can override all permissions, operating above the rules that bind ordinary subjects"
  - "[source] permissions encode distinct types of engagement -- reading, modifying, and executing -- mirroring differentiated social rights"
limits:
  - "[source] breaks because governance permissions involve negotiation, appeal, and context, while the mapped system is a rigid bitmask with no mechanism for discretion or exception"
  - "[source] misleads because social group membership is fluid and overlapping, but Unix groups are fixed assignments where a user's effective permissions depend on which single group identity the system evaluates"
---

## Transfers

Access control as social permission-granting. Unix file permissions model a
governance system: an owner controls a resource, grants or withholds access
to a defined group and to the general public, and a sovereign authority can
override all restrictions.

- **Owner, group, others -- a three-tier hierarchy** -- Unix permissions
  divide the world into three social classes: the owner (the individual
  who controls the resource), the group (a defined community with shared
  interests), and others (everyone else). This maps directly to governance
  models: a property owner, an organization, and the public. The
  permission bits encode the owner's decisions about how much access each
  tier receives. The hierarchy is rigid and exhaustive -- every user falls
  into exactly one tier for any given file.
- **Read, write, execute -- differentiated rights** -- the three permission
  types correspond to three kinds of engagement with a resource.
  Reading is passive access: you may observe but not alter. Writing is
  modification authority: you may change the thing. Execution is
  operational authority: you may use the thing as an active agent. This
  three-way split mirrors legal distinctions between viewing, editing,
  and deploying -- or between reading a law, amending it, and enforcing it.
- **The superuser as sovereign** -- root (UID 0) bypasses all permission
  checks. This is the computing equivalent of sovereignty: the entity
  that stands above the rules it enforces on others. The metaphor is
  politically precise. Permissions are social contracts that bind ordinary
  users but not the authority that administers the system. Every Unix
  system has an absolute monarch.
- **Granting and revoking** -- the vocabulary is explicitly social:
  `chmod` changes the mode (the social contract), the owner "grants"
  read access, the administrator "revokes" write permission. The
  operations are performative speech acts borrowed from governance:
  to grant permission is to change reality by declaring it changed.

## Limits

- **No discretion, no context** -- human governance involves judgment. A
  guard can make exceptions; a judge can consider circumstances; a manager
  can grant temporary access for a specific purpose. Unix permissions are
  a 9-bit bitmask. There is no "read this file only on Tuesdays," no
  "write access for this one task," no "execute but only if your manager
  approved." The governance metaphor implies a richness of policy that the
  implementation ruthlessly collapses into on/off bits.
- **Group membership is rigid** -- in human societies, group membership is
  fluid, contextual, and overlapping. You are simultaneously a citizen,
  an employee, a club member, a family member. Unix primary group
  membership is a single assignment. While supplementary groups exist,
  the permission model evaluates one tier at a time. A user who is both
  the owner and a group member gets owner permissions, not the union of
  both. The social metaphor implies flexible, overlapping identities; the
  implementation provides a fixed hierarchy.
- **The octal notation killed the metaphor** -- permissions are commonly
  expressed as octal numbers: `chmod 755`, `chmod 644`. These
  encodings are pure numeric abstractions. No one reading "755" thinks
  "the owner has full sovereignty, the group and public may observe and
  execute but not modify." The governance metaphor exists in the design
  but not in the daily interface. The social model was compressed into
  a number and the number replaced the model.
- **No audit trail** -- governance systems produce records: who granted
  what, when, and why. Unix permissions carry no history. You can see the
  current permission state but not who set it, when it was changed, or
  what it was before. The governance metaphor implies accountability that
  the system does not provide.

## Expressions

- "You don't have permission" -- the error message, delivered in the social
  register of a denied request
- "Grant execute permission" -- performative language borrowed directly
  from governance and legal authority
- "Permission denied" -- the most common Unix error, phrased as a social
  refusal rather than a technical state description
- "World-readable" -- a file accessible to "others," where "world" imports
  the governance sense of the general public
- "Chmod 777" -- granting all permissions to everyone, the Unix equivalent
  of anarchy, spoken as a number that has shed all metaphorical content

## Origin Story

Unix file permissions were part of the original design by Thompson and
Ritchie at Bell Labs in the early 1970s. The three-tier model
(owner/group/other) with three permission types (read/write/execute)
created the 9-bit permission system that survives essentially unchanged
in every Unix-derived system fifty years later.

The governance metaphor was likely not a deliberate design choice but a
natural mapping. Access control in any multi-user system requires deciding
who may do what -- a problem that human societies solved millennia ago
with property rights, group membership, and sovereign authority. The Unix
designers imported this solution wholesale, down to the vocabulary: owner,
group, permission, grant, deny.

The POSIX standard (1988) formalized the permission model. Later systems
added Access Control Lists (ACLs) and capabilities-based security, partly
in response to the limitations the governance metaphor reveals: the
three-tier model is too coarse for complex organizations. But the original
owner/group/other model remains the default, its governance metaphor so
thoroughly dead that "file permissions" reads as a purely technical phrase.

## References

- Thompson, K. & Ritchie, D. "The UNIX Time-Sharing System," CACM 17(7),
  1974
- IEEE Std 1003.1 (POSIX) -- file permission specification
- Kernighan, B. & Pike, R. *The Unix Programming Environment*,
  Prentice-Hall, 1984
- man7.org, chmod(1), stat(2) -- Linux man pages
