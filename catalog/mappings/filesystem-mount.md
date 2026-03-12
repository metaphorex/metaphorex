---
slug: filesystem-mount
name: "Filesystem Mount"
kind: dead-metaphor
source_frame: tool-use
target_frame: data-processing
categories:
  - computer-science
author: agent:metaphorex-miner
harness: "Claude Code"
contributors: []
related:
  - filesystem-tree
  - filesystem-root
---

## What It Brings

"Mount" in Unix means attaching a filesystem to the directory tree at a
specified point. The term comes from a literal physical action: in the
1960s and 1970s, operators mounted disk packs onto drive spindles by hand.
You physically lifted a multi-platter disk assembly, placed it onto the
spindle of a disk drive, and secured it. The operating system then made
the data on that disk accessible. The metaphor mapped the physical act of
attaching hardware onto the logical act of making a filesystem visible.

Key structural parallels:

- **Attachment to a fixed point** -- a disk pack mounts onto a specific
  drive. A filesystem mounts onto a specific directory (the mount point).
  In both cases, the thing being mounted is a discrete unit of storage
  that becomes accessible at a defined location. The mount point is a
  slot, a socket, a place prepared to receive something.
- **Reversibility** -- you can unmount the disk pack and carry it away.
  You can unmount the filesystem and the directory returns to its
  previous (empty) state. The data is not destroyed; it is merely
  disconnected. This reversibility is central to the metaphor: mounting
  is attachment, not fusion. The filesystem retains its identity as a
  separate entity even while mounted.
- **The grafting extension** -- mounting a filesystem onto the directory
  tree is structurally similar to grafting a branch onto a tree: you
  take a separately grown piece and attach it at a specific point in
  the existing structure. After mounting, the grafted filesystem is
  indistinguishable from the host tree in normal traversal. `ls` does
  not tell you whether a directory is a mount point or a regular
  subdirectory.
- **Opacity at the mount point** -- when you mount a filesystem at
  `/mnt/data`, anything previously in that directory becomes invisible,
  hidden behind the mounted filesystem. This is like hanging a painting
  over a window: the mount obscures whatever was at the mount point.
  The hidden content is not deleted but is inaccessible until the
  filesystem is unmounted.

## Where It Breaks

- **Nobody mounts disk packs anymore** -- the source domain has
  physically disappeared. Modern storage is solid-state, permanently
  connected, or hot-plugged automatically. The operator who lifted a
  30-pound disk pack onto a spindle has no equivalent in a modern data
  center. The metaphor survived the extinction of its source, which is
  the textbook definition of a dead metaphor: the word persists but the
  image it once evoked is gone.
- **The naming could not decide on its own negation** -- the opposite of
  "mount" should be "dismount" (following equestrian convention) or
  "unmount" (following standard English prefixing). Unix chose "umount"
  -- a truncation that is neither proper English nor a consistent
  metaphor extension. The `umount` command is a scar in the vocabulary,
  evidence that the metaphor was already dying when the reverse operation
  was named: the developers were abbreviating for convenience, not
  extending a coherent metaphor.
- **Automounting erases the metaphor entirely** -- modern systems
  automatically mount filesystems at boot time via `/etc/fstab`, and
  removable media is automounted by desktop environments. The user
  never performs or observes the mount action. The metaphor assumed a
  human operator performing a deliberate physical act; when the act
  becomes automatic and invisible, the metaphor's experiential basis
  disappears. A user who has never typed `mount` has no reason to think
  of filesystem access as an act of attachment.
- **Mount points are misleadingly inert** -- the metaphor of physical
  mounting suggests a static attachment: you put the disk on the spindle
  and it stays. But mount points in modern systems are dynamic: bind
  mounts, overlay filesystems, union mounts, FUSE filesystems, and
  mount namespaces create a complex topology that has nothing to do
  with placing hardware onto hardware. The metaphor cannot stretch to
  cover a bind mount (mounting a directory onto another directory) or
  an overlay filesystem (stacking multiple directories into a single
  view) because these have no physical analogue in the original
  disk-pack-on-spindle image.

## Expressions

- "Mount the drive" -- the standard instruction, even when no physical
  mounting occurs
- "Mount point" -- the directory where a filesystem attaches to the tree,
  a term that makes sense only if you know the physical metaphor
- "Unmount before removing" -- the safety warning for removable media,
  preserving the metaphor of orderly detachment
- "Mounted filesystem" -- the state of being attached and accessible,
  contrasted with an unmounted filesystem that exists but cannot be
  reached
- "Mount namespace" -- Linux containers' mechanism for giving processes
  their own view of mount points, extending the metaphor into
  virtualization territory
- "Bind mount" -- mounting a directory onto another directory, a usage
  that strains the physical metaphor beyond recognition

## Origin Story

The physical act of mounting disk packs was a daily ritual in 1960s and
1970s computing centers. IBM's 2311 and 2314 disk drives required
operators to physically place removable disk packs onto drive spindles.
The pack -- a stack of magnetic platters in a protective shell -- weighed
up to 30 pounds. You opened the drive, removed the protective cover,
lowered the pack onto the spindle, and locked it in place. Only then
could the operating system access the data.

Unix inherited this terminology from its mainframe-era context. The
`mount` system call (present in the first edition of Unix, 1971) made a
filesystem accessible at a directory. Thompson and Ritchie's 1974 CACM
paper describes mounting as part of the filesystem's design. By the time
removable disk packs disappeared in the 1980s, the term was too deeply
embedded in Unix vocabulary to change. It persists today in every Linux
`mount` command, every Docker volume mount, and every Kubernetes
persistent volume claim -- layers of abstraction built atop a metaphor
whose physical referent no longer exists.

## References

- Thompson, K. & Ritchie, D. "The UNIX Time-Sharing System," CACM 17(7),
  1974
- mount(2) -- Linux man page, man7.org
- mount(8) -- Linux man page, man7.org
- Kernighan, B. & Pike, R. *The Unix Programming Environment*,
  Prentice-Hall, 1984
- IBM 2314 Direct Access Storage Facility reference manual, IBM, 1966
