---
slug: filesystem-mount
name: "Filesystem Mount"
summary: "Attaching a separate storage device to a fixed directory tree at a prepared point, like mounting a lens onto a camera body."
kind: metaphor
dead: true
source_frame: tool-use
applies_to:
  - data-processing
categories:
  - computer-science
author: agent:metaphorex-miner
contributors:
  - fshot
related:
  - filesystem-tree
  - filesystem-root
created: '2026-03-17'
updated: '2026-03-17'
harness: Claude Code
grounding: folk
embodied_patterns:
  - link
  - part-whole
  - container
relation_types:
  - contain
  - coordinate
structure:
  - hierarchy
abstraction_level: specific
transfers:
  - "[source] mounting attaches a separate object to a fixed frame, making it accessible as part of the larger assembly"
  - "[source] the mounted object retains its own identity and can be detached without damaging the frame it was attached to"
  - "[source] mounting requires a specific attachment point -- a mount point -- chosen in advance on the receiving structure"
limits:
  - "[source] breaks because physical mounting is visible and spatial, but the mapped operation is invisible -- a directory that was empty now contains an entire filesystem with no visible mechanism"
  - "[source] misleads because physically mounted objects remain distinguishable from the frame, but a mounted filesystem becomes indistinguishable from the directory tree, hiding the boundary entirely"
---

## Transfers

Attaching a filesystem to the directory tree as mounting a physical object
onto a surface. The Unix `mount` command makes a storage device's contents
accessible at a chosen point in the directory hierarchy -- like mounting a
tool onto a workbench, a lens onto a camera, or a disk pack onto a drive
spindle.

- **Attachment to a fixed frame** -- mounting always involves two things:
  the thing being mounted and the fixed structure it attaches to. A camera
  lens mounts onto the camera body. A filesystem mounts onto the directory
  tree. The metaphor correctly implies that the directory tree is the
  primary structure and the new filesystem is a secondary addition. You
  mount *onto* something that was already there.
- **The mount point** -- physical mounting requires a specific attachment
  point: a tripod socket, a bolt hole, a rack slot. Unix mounting requires
  a mount point: an existing directory where the new filesystem will
  appear. The choice of mount point determines where in the hierarchy the
  new content becomes visible. This structural parallel is precise -- in
  both domains, the attachment point is a prepared location on the
  receiving structure.
- **Reversibility** -- mounting implies detachability. A mounted lens can
  be unmounted; a mounted filesystem can be unmounted. Neither operation
  destroys the mounted object or the frame. The data on the filesystem
  survives unmounting, just as a lens survives removal from the camera.
  This reversibility distinguishes mounting from welding, gluing, or
  permanent attachment.
- **The original literal act** -- in 1970s computing, "mount" was not
  metaphorical. Operators physically mounted disk packs onto drive
  spindles -- hefting a multi-platter disk assembly and placing it onto
  the drive mechanism. The software `mount` command was issued after the
  physical mount was complete, to tell the OS that the disk was ready.
  The metaphor is a fossil of a literal action that no longer exists.

## Limits

- **The seam disappears** -- when you mount a lens onto a camera, the
  boundary is visible: you can see where the lens ends and the body
  begins. When you mount a filesystem at `/mnt/usb`, the mount point
  becomes invisible. `ls /mnt/usb` shows the contents of the mounted
  filesystem with no visual indication that a boundary has been crossed.
  The metaphor implies a visible joint; the implementation provides
  seamless transparency. This causes real confusion when users do not
  realize they have crossed a mount boundary and are now on a different
  device.
- **Mount hides the mechanism entirely** -- physical mounting involves
  visible hardware: screws, clamps, bayonet rings. Unix mounting involves
  a kernel data structure update that has no physical manifestation. The
  only way to know something is mounted is to run `mount` or read
  `/proc/mounts`. The metaphor borrows the physicality of tool-use but
  delivers a purely abstract operation.
- **Unmount is not the inverse of mount** -- physically, removing a mounted
  object is trivial: lift it off. Unmounting a filesystem can fail because
  files are open, processes have working directories inside it, or data
  has not been flushed to disk. The metaphor suggests that detachment is
  as simple as attachment, but `umount: target is busy` is one of the
  most common Unix frustrations. The verb promises easy reversal that the
  system cannot always deliver.
- **The spelling tells the story** -- the command is `umount`, not
  `unmount`. This truncation (inherited from early Unix's 6-character
  command name limit) is a scar from the era of physical disk mounting.
  The metaphor strained early: "dismount" and "unmount" competed, and the
  system settled on a truncation that is neither. Modern developers type
  `umount` without connecting it to un-mounting or dis-mounting anything.

## Expressions

- "Mount a drive" -- the most common usage, where "mount" has become a
  pure technical verb with no physical connotation
- "Mount point" -- the directory where attachment occurs, preserving the
  tool-use metaphor's notion of a prepared attachment location
- "Bind mount" -- mounting a directory onto another directory, stretching
  the metaphor from hardware to pure namespace manipulation
- "The disk is mounted" -- passive voice that echoes "the lens is mounted,"
  treating the filesystem as a physical object in a ready state
- "Unmount before removing" -- the safety warning, which makes sense only
  if you remember that "mount" implies a formal attachment that must be
  formally dissolved

## Origin Story

The term "mount" in computing is one of the rare cases where the metaphor
started as a literal description. In the 1960s and 1970s, disk storage used
removable disk packs -- heavy multi-platter assemblies that operators
physically mounted onto drive spindles. The IBM 2311 and 2314 drives
required a human to lift the pack, align it with the spindle, and lower
it into place. The operator would then issue a software command to make
the operating system aware of the newly available storage.

When Unix adopted the term in the early 1970s, this physical act was still
the normal way to attach storage. Thompson and Ritchie's `mount` system
call automated the software side of what was still a two-step
physical-plus-logical operation.

As disk technology evolved -- from removable packs to fixed hard drives to
SSDs to cloud block storage -- the physical act of mounting disappeared
entirely. But the software command persisted. Today, `mount -t nfs
server:/share /mnt/remote` mounts a network filesystem that exists on a
different machine, potentially on a different continent. Nothing is
physically mounted anywhere. The term is a fossil, perfectly preserved
from an era of disk packs and drive spindles that no one under fifty has
seen.

## References

- Thompson, K. & Ritchie, D. "The UNIX Time-Sharing System," CACM 17(7),
  1974 -- mount as a system call
- Kernighan, B. & Pike, R. *The Unix Programming Environment*,
  Prentice-Hall, 1984
- man7.org, mount(2) -- Linux man page for the mount system call
- IBM Archives -- IBM 2314 Direct Access Storage Facility documentation
