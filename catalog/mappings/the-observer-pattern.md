---
slug: the-observer-pattern
name: "The Observer Pattern"
kind: design-pattern
source_frame: observation
target_frame: event-systems
categories:
  - software-engineering
author: metaphorex
contributors: []
related:
  - the-facade-pattern
---

## What It Brings

Maps the act of watching onto event subscription. The intuition it
provides is separation: an observer doesn't need to know the subject's
internals, just as a birdwatcher doesn't need to understand avian
physiology to watch birds. You register interest, you wait, you react
when something happens.

Key structural parallels:

- **Decoupling through attention** — the observer and the subject are
  independent entities connected only by the act of observation. In
  software: the subscriber and the publisher share only an event
  interface. This is the core insight, and it's genuinely powerful.
- **Multiple observers, one subject** — many birdwatchers can watch
  the same bird. Many event listeners can subscribe to the same
  publisher. The subject doesn't need to know or care how many are
  watching.
- **The observer chooses what to watch** — you pick your vantage point,
  your species of interest, your time of day. Software observers
  register for specific event types. Selective attention as a design
  principle.

## Where It Breaks

The metaphor is misleading in several important ways, and the
misleading parts have real consequences for how developers think about
event-driven systems.

- **Real observers are passive; software observers trigger side
  effects.** A birdwatcher watching a heron doesn't cause the heron
  to do anything. A software observer receiving an event might write
  to a database, send an email, or crash the process. The word
  "observer" imports an assumption of non-interference that's flatly
  wrong in practice.
- **Real observation is pull-based; the pattern is push-based.** You
  look at something (pull). The Observer pattern notifies you (push).
  These are fundamentally different control flows. The metaphor
  suggests the observer is in charge — choosing when and where to
  look — but in the pattern, the subject decides when to notify. The
  direction of control is reversed from what the name implies.
- **"Observer" suggests awareness; the pattern is mechanical.** A human
  observer interprets, contextualizes, forms judgments. A software
  observer executes a callback. The metaphor oversells the intelligence
  of the receiving end.
- **Observation implies a single point in time; events are streams.**
  You observe a moment. Event systems process continuous flows. The
  metaphor doesn't prepare you for backpressure, ordering guarantees,
  or the complexity of managing event streams at scale.

Honestly, "Subscriber" or "Listener" would have been more accurate
names. The industry has partly corrected for this — "pub/sub" and
"event listener" are now more common than "observer" in practice —
but the GoF name persists in textbooks and interviews.

## Expressions

- "Subscribe to events" — the pub/sub variant, more honest about
  the mechanism
- "Watch for changes" — retains the observation metaphor
- "Listen for updates" — the auditory variant; listening is already
  more passive-receptive than watching, so arguably more accurate
- "Notify observers" — reveals the push direction that "observe"
  conceals
- "Event listener" — the DOM/browser version, now more widely used
  than "observer"
- "Callback" — the implementation stripped of metaphor entirely
- "Pub/sub" — publish/subscribe, the pattern renamed to match what
  it actually does

## Origin Story

The Observer pattern was codified by the Gang of Four in *Design
Patterns* (1994), but the underlying mechanism — callback registration
— predates it by decades. The Smalltalk-80 MVC framework (late 1970s)
used a dependency mechanism that was essentially the Observer pattern
before it had the name.

The choice of "Observer" as the name was probably influenced by the
MVC framing: the View *observes* the Model. This makes sense in the
GUI context — a view literally displays what it sees in the model.
But when the pattern escaped from GUI programming into distributed
systems, message queues, and reactive streams, the observation
metaphor stopped fitting and "pub/sub" gradually took over.

## References

- Gamma, E. et al. *Design Patterns: Elements of Reusable Object-
  Oriented Software* (1994)
- Krasner, G.E. & Pope, S.T. "A Cookbook for Using the Model-View-
  Controller User Interface Paradigm in Smalltalk-80," *JOOP* 1(3)
  (1988): 26-49
