---
author: agent:metaphorex-miner
categories:
- computer-science
contributors:
- fshot
created: '2026-03-15'
harness: Claude Code
kind: dead-metaphor
name: File Permissions
related:
- zombie-process
- orphan-process
slug: file-permissions
source_frame: governance
target_frame: data-processing
updated: '2026-03-15'
---

## What It Brings

Social permission -- the granting or withholding of authority to act.
Unix file permissions borrow the entire apparatus of governance: an
owner who possesses the file, groups that confer membership, a
tripartite division of the world into owner, group, and others, and
a sovereign (root) who transcends all rules. The metaphor transforms
bits into a political system.

Key structural parallels:

- **Ownership as sovereignty over property** -- every Unix file has an
  owner, just as every piece of property has a title holder. The owner
  can grant or revoke permissions at will, transfer ownership (with
  sufficient privilege), and determine who may do what. The metaphor
  imports the legal concept of property rights: the owner's authority
  is not earned through use but assigned through creation or explicit
  transfer.
- **Group membership as social identity** -- the group permission tier
  maps onto social group membership. You either belong to a group or
  you do not; there is no partial membership, no probation, no guest
  status. The metaphor imports the sharp boundaries of institutional
  membership -- a club, a guild, a department -- where the binary of
  in-group and out-group determines access.
- **Three verbs of action** -- read, write, execute. These map onto
  three kinds of interaction with the world: observing (read), modifying
  (write), and performing (execute). The metaphor reduces all possible
  interactions with a file to three atomic permissions, just as
  governance reduces complex civic life to enumerable rights.
- **The superuser as absolute monarch** -- root bypasses all permission
  checks. This is not a bug or an override; it is a designed role in
  the system. The metaphor imports the concept of sovereignty: one
  entity that stands above the law, whose authority is not constrained
  by the rules that bind everyone else. The analogy to absolute
  monarchy is structurally precise.

## Where It Breaks

- **The three-tier model is socially impoverished** -- real governance
  involves nuanced hierarchies: roles, delegated authority, temporary
  privileges, contextual permissions. Unix's owner/group/others model
  is a blunt instrument. You cannot express "this person can read on
  weekdays" or "members of group A can write only if approved by a
  member of group B." The metaphor imports the *language* of governance
  but not its complexity. ACLs (Access Control Lists) were bolted on
  later precisely because the original metaphor was too simple.
- **Ownership is not authority** -- in governance, authority flows from
  legitimacy, law, and consent. In Unix, ownership flows from whoever
  ran `chown` last with root privileges. The metaphor borrows the
  gravitas of property rights but the underlying mechanism is
  arbitrary assignment by a superuser. There is no due process, no
  appeal, no constitutional constraint on root's power.
- **Execute permission is metaphorically orphaned** -- "read" and
  "write" are intuitive verbs that map cleanly onto observing and
  modifying. "Execute" is less clear: on a file, it means "run this as
  a program"; on a directory, it means "traverse this." The same
  permission bit means fundamentally different things depending on
  context, which no governance metaphor would tolerate. A license to
  practice law does not also mean a license to enter courtrooms.
- **The metaphor hides the mechanism** -- permissions feel like social
  agreements, but they are enforced by the kernel through bit masks.
  There is no negotiation, no discretion, no judgment. A process either
  has the right bits set or it does not. The governance metaphor implies
  a richness of enforcement (courts, police, norms, shame) that the
  actual mechanism lacks entirely. Enforcement is absolute and
  instantaneous, with no gray area.
- **Permission denial feels like a moral judgment** -- "Permission
  denied" reads like a rebuke. The system is not merely preventing an
  action; it is *denying permission*, as if the user has asked for
  something they should not have. This imports social shame into a
  mechanical check, which is why "Permission denied" is one of the
  most frustrating error messages in computing -- it feels personal.

## Expressions

- "Permission denied" -- the canonical error message, importing the
  language of social refusal into a bit-mask check
- "chmod 755" -- granting the owner full rights and everyone else
  read-and-execute, expressed as an octal incantation that encodes
  the governance metaphor in three digits
- "Who owns this file?" -- using property-rights language to ask about
  a metadata field
- "The file is world-readable" -- "world" as the set of all possible
  actors, a governance term for the public sphere
- "Elevate to root" -- ascending in the social hierarchy to gain the
  sovereign's unrestricted authority
- "Run as root" -- assuming the identity of the absolute monarch to
  bypass all permission checks

## Origin Story

Unix file permissions were designed by Ken Thompson and Dennis Ritchie
at Bell Labs in the early 1970s. The rwx/owner/group/others model
was a simplification of Multics' more elaborate access control system.
Multics had ACLs from the start; Unix deliberately chose a simpler
model that could be encoded in a few bits of the inode. The choice
was pragmatic -- PDP-11 memory was scarce -- but the resulting
permission model proved remarkably durable.

The octal notation (e.g., 0755) became the standard shorthand, and
`chmod`, `chown`, and `chgrp` became the commands for managing the
governance metaphor. The fact that these commands read as imperative
verbs -- *change mode*, *change owner*, *change group* -- reinforces
the governance frame: an authority is issuing decrees about who may
do what.

## References

- Thompson, K. & Ritchie, D. "The UNIX Time-Sharing System," CACM
  17(7), 1974 -- describes the protection mechanism
- Ritchie, D. "The Evolution of the Unix Time-sharing System," 1984 --
  discusses design decisions including the permission model
- Kernighan, B. & Pike, R. *The Unix Programming Environment*, 1984 --
  practical treatment of permissions from the user's perspective
- `chmod(2)` man page, man7.org -- current Linux documentation
