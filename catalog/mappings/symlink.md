---
author: agent:metaphorex-miner
categories:
- computer-science
contributors:
- fshot
created: '2026-03-11'
harness: Claude Code
kind: dead-metaphor
name: Symlink
related:
- unix-pipe
slug: symlink
source_frame: physical-connection
target_frame: filesystem
updated: '2026-03-14'
---

## What It Brings

Unix filesystems borrow the vocabulary of physical chains to describe
references between names and data. A "link" is a connection between a
filename and the underlying data on disk. The metaphor subdivides into two
species: hard links (multiple names attached directly to the same data, like
two chains bolted to the same anchor) and symbolic links (a name that points
to another name, like a sign that says "go there instead").

Key structural parallels:

- **Links as physical connections** -- a link joins two things. In the
  source domain, a chain link connects adjacent segments into a continuous
  whole. In the filesystem, a hard link connects a directory entry to an
  inode. The metaphor makes the abstract relationship between a name and
  its data feel tangible and manipulable -- you can create links, count
  them, and remove them, just as you would with physical connectors.
- **Broken links** -- a symbolic link whose target has been deleted is
  called a "broken link" or "dangling symlink." The metaphor imports the
  failure mode directly from the physical domain: a chain with a missing
  segment no longer connects anything. The term "dangling" adds a
  gravitational image -- the link hangs uselessly, attached on one end
  but reaching nothing on the other. This is one of the most vivid
  error-state metaphors in computing.
- **Link count as structural integrity** -- every inode maintains a link
  count: the number of hard links pointing to it. When the count reaches
  zero, the data is freed. This maps onto the physical intuition that an
  object held by multiple chains remains secure; remove the last chain and
  it falls. Reference counting in garbage collection generalizes this same
  metaphor beyond filesystems.
- **Indirection as redirection** -- a symlink is an explicit level of
  indirection. You follow the link to arrive at the real target, the way
  you follow a signpost to reach a destination. The metaphor of "following"
  a link was later inherited wholesale by the World Wide Web, where
  hyperlinks extended the chain metaphor into networked documents.

## Where It Breaks

- **Physical links are bidirectional; symlinks are not** -- a physical chain
  connects A to B and B to A with equal strength. A symbolic link is purely
  one-directional: it knows its target, but the target does not know it
  exists. You cannot traverse a symlink backward to discover what points to
  a given file without scanning the entire filesystem. The metaphor of a
  "link" implies mutual connection, but symlinks are closer to one-way
  signs than to chains.
- **Hard links defy the connection metaphor** -- a hard link is not really
  a connection between two things; it is two names for the same thing.
  There is no "link" object you can inspect -- the directory entry simply
  contains the inode number. Calling this a "link" imports a sense of
  separation (two things connected by a third) where there is actually
  identity (two names, one object). This misleads newcomers into thinking
  hard links are pointers or references rather than additional names.
- **Circular symlinks have no physical analog** -- you can create a
  symlink that points to itself, or a cycle of symlinks that point to
  each other. Physical chains cannot form a paradox: a chain that leads
  back to its own starting point is simply a loop. But a circular symlink
  is a logical error, an infinite regress that the OS must detect and
  abort. The metaphor provides no intuition for this failure mode.
- **The "link" metaphor obscures permission and ownership** -- a symlink
  has its own ownership and permission bits, but they are mostly ignored;
  the target's permissions govern access. A hard link shares the target's
  permissions exactly. Neither behavior maps to physical links, which do
  not carry access-control semantics. When users reason about "who can
  follow this link," the chain metaphor gives them nothing to work with.

## Expressions

- "Symlink it" -- create a symbolic link; the noun has become a verb
  through regular use
- "Broken link" -- a symlink whose target no longer exists; borrowed
  verbatim by the web for dead hyperlinks
- "Dangling symlink" -- the more evocative variant, adding the image of
  a rope hanging into empty space
- "Hard link" -- two directory entries for the same inode; "hard" implies
  rigidity and permanence versus the "soft" (symbolic) link
- "Follow the link" -- resolve the indirection; later adopted as the
  fundamental web interaction
- "Link count" -- the number of hard links to an inode; when it reaches
  zero, the data is reclaimed

## Origin Story

The link concept dates to the Multics filesystem in the mid-1960s, which
distinguished between "links" (additional directory entries for existing
files) and "branch entries" (the primary name). Unix inherited and
simplified this in the early 1970s, making all directory entries equal --
there is no "primary" name, only a link count. Dennis Ritchie and Ken
Thompson's original Unix treated every directory entry as a hard link.

Symbolic links arrived later, introduced in 4.2BSD in 1983 by Keith Bostic
and others. The "symbolic" qualifier distinguished these new indirect
references from the older "hard" links -- a terminological distinction that
only makes sense within the link metaphor. The success of the metaphor is
measured by its spread: hyperlinks, deep links, backlinks, and link rot all
descend from this filesystem vocabulary.

## References

- Ritchie, D. & Thompson, K. "The UNIX Time-Sharing System," CACM 17(7),
  1974
- McKusick, M.K. et al. "A Fast File System for UNIX," ACM Transactions on
  Computer Systems, 2(3), 1984
- Raymond, E.S. *The Art of Unix Programming*, Addison-Wesley, 2003