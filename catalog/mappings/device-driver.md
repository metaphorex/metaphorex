---
author: agent:metaphorex-miner
categories:
- computer-science
- software-engineering
contributors:
- fshot
created: '2026-03-15'
harness: Claude Code
kind: dead-metaphor
name: Device Driver
related:
- process-kill
slug: device-driver
source_frame: travel
target_frame: software-programs
updated: '2026-03-15'
---

## What It Brings

A person who drives -- who operates a vehicle or machine, translating
the rider's intentions into the specific mechanical actions required to
move through terrain. A device driver is software that operates a piece
of hardware, translating the operating system's generic commands into
the specific electrical signals and protocols the device understands.
The metaphor imports expertise, agency, and mediation: the driver knows
how to handle *this particular* machine, so the passenger does not
have to.

Key structural parallels:

- **Specialized knowledge** -- a driver knows things the passenger does
  not: how to work the clutch, when to shift gears, what the engine
  sounds mean. A device driver knows the hardware's register layout,
  timing requirements, command set, and quirks. The metaphor captures
  the asymmetry of expertise: the OS issues high-level requests ("read
  a block") and the driver translates them into the low-level protocol
  the device requires.
- **Mediation between domains** -- the driver sits between the
  passenger (who knows where they want to go) and the vehicle (which
  knows how to move). The device driver sits between the kernel (which
  knows what data it wants) and the hardware (which knows how to
  retrieve it). Neither side needs to understand the other's language;
  the driver bridges the gap.
- **Interchangeability** -- you can hire a different driver for a
  different vehicle, but the passenger's experience remains similar.
  Unix's device driver model provides a uniform interface: all block
  devices look like files, all character devices respond to the same
  system calls. Swap the driver, swap the hardware, and the
  application never notices. The metaphor encodes the abstraction
  layer that drivers provide.
- **Trust and control** -- a passenger trusts the driver with their
  safety. The kernel trusts device drivers with direct hardware access
  -- the most privileged operations in the system. A buggy driver can
  crash the entire system, just as a reckless driver can crash the car.
  Device drivers are the single largest source of kernel crashes in
  modern operating systems, making the trust metaphor uncomfortably
  literal.

## Where It Breaks

- **Drivers are human; device drivers are code** -- a human driver
  exercises judgment, adapts to unexpected conditions, and makes
  real-time decisions. A device driver follows a fixed program. It
  cannot improvise when the hardware behaves unexpectedly -- it either
  handles the case or it does not. The metaphor imports an adaptability
  that software does not possess.
- **The driver metaphor suggests a person in charge** -- "driver"
  implies active, continuous control. But most device drivers spend
  their time idle, waiting for requests. They are less like a driver
  steering through traffic and more like a translator sitting by the
  phone. The metaphor overstates the agency: drivers react to requests,
  they do not initiate journeys.
- **The metaphor has died so thoroughly that "driver" now means
  software** -- most computer users have encountered "install a driver"
  or "driver update" without ever connecting the word to its vehicular
  origin. The metaphor is so dead that "driver" in computing contexts
  is experienced as a purely technical term. Asking "who is driving the
  printer?" would be met with confusion, not comprehension.
- **Modern drivers drive nothing** -- the original metaphor assumed
  a one-driver-one-vehicle relationship: one piece of software
  operating one piece of hardware. Modern device drivers may be
  virtual (driving emulated hardware), stacked (a driver driving
  another driver), or generic (one driver handling an entire class of
  devices via a protocol like USB). The "driver" metaphor suggests a
  specificity that has been abstracted away.

## Expressions

- "Install the driver" -- the most common user-facing usage, where
  the metaphor is entirely dead and "driver" means only "software that
  makes hardware work"
- "Driver update available" -- the driver as something that needs
  maintenance, extending the vehicle metaphor to scheduled servicing
- "The driver crashed the kernel" -- where the driving metaphor
  briefly resurfaces: a bad driver caused a crash, in both the
  vehicular and computational senses
- "Write a driver for it" -- the engineering task of creating a new
  mediator between OS and hardware, where "driver" functions as a
  pure technical category
- "Driverless" -- occasionally used for hardware that needs no
  special software (e.g., USB HID devices that use generic class
  drivers), echoing the autonomous-vehicle sense of needing no operator

## Origin Story

The term "device driver" emerged in the 1960s as operating systems
began abstracting hardware access behind standardized interfaces. The
concept was present in early IBM systems and was formalized in Unix's
device-file model, where every hardware device appears as a file in
`/dev/` and is operated through a driver that implements the file
operations interface (open, read, write, close, ioctl).

The driving metaphor was natural for the era: someone had to "drive"
the hardware, meaning operate it with skill and specific knowledge.
The Unix innovation was making all drivers conform to the same
interface -- the file operations structure -- so that the rest of the
system could treat all hardware uniformly. This standardized driver
interface is one of Unix's most influential design decisions, adopted
by virtually every subsequent operating system.

## References

- Ritchie, D. "The Development of the C Language," ACM SIGPLAN,
  1993 -- context on Unix's device abstraction model
- Kernighan, B. & Pike, R. *The Unix Programming Environment*,
  1984 -- treatment of device files and the /dev/ directory
- Corbet, J., Rubini, A. & Kroah-Hartman, G. *Linux Device Drivers*,
  3rd ed., 2005 -- the canonical reference for writing Linux drivers
