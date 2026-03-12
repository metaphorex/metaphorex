---
slug: the-observer-pattern
name: "The Observer Pattern"
kind: archetype
source_frame: surveillance
target_frame: object-oriented-design
categories:
  - software-engineering
author: agent:metaphorex-miner
contributors: []
related:
  - the-mediator-pattern
  - the-command-pattern
---

## What It Brings

An observer watches. The word carries the weight of sustained,
purposeful attention -- a birdwatcher at the marsh, a UN observer at
an election, a scientist recording data. The GoF Observer pattern maps
this onto software: objects register interest in another object's state
changes and are notified when those changes occur. The surveillance
metaphor makes this one-to-many dependency feel like a natural
relationship -- of course important things should be watched, and of
course watchers should be informed when something changes.

Key structural parallels:

- **Observers watch subjects, not the reverse** -- the relationship
  is asymmetric. A surveillance camera watches the room; the room
  doesn't watch the camera. In the pattern, the subject broadcasts
  changes and observers receive them. The metaphor establishes the
  correct directionality: information flows from the watched to the
  watcher.
- **Multiple observers can watch the same subject** -- a public
  figure may be watched by journalists, security personnel, and fans
  simultaneously. The pattern supports multiple observers registering
  with a single subject. The metaphor naturalizes this one-to-many
  relationship as standard practice.
- **Observers can start and stop watching** -- surveillance can be
  activated and deactivated. The pattern's subscribe/unsubscribe
  mechanism maps onto this: observers choose when to begin and end
  their watch. The metaphor makes dynamic registration feel like
  reasonable operational procedure.
- **The subject doesn't need to know who's watching** -- in many
  surveillance contexts, the observed party doesn't know the identities
  of all observers. The pattern decouples the subject from its
  observers through an abstract interface. The metaphor justifies this
  anonymity as standard surveillance protocol.
- **Notification is the observer's payoff** -- the whole point of
  watching is to learn when something happens. The pattern's
  notification mechanism is the metaphor's fulfillment: the observer
  waited, and now they know. The metaphor gives the callback a sense
  of purpose.

## Where It Breaks

- **Real observers have agency; software observers don't** -- a UN
  election observer can intervene, file reports, apply judgment, and
  decide what matters. A software observer receives a callback and
  executes predetermined code. The metaphor imports intelligence and
  discretion where the pattern provides only mechanical notification.
- **Surveillance implies suspicion; the pattern is neutral** -- calling
  something an "observer" carries connotations of distrust, control,
  and power asymmetry. Software observers are typically collaborative
  -- a UI widget observing a data model is not policing it. The
  metaphor adds an adversarial undertone to what is usually a
  cooperative relationship.
- **The subject in surveillance is unaware; the software subject
  actively notifies** -- a surveillance target doesn't choose to be
  watched. The software subject explicitly maintains a list of
  observers and calls their update methods. The subject is a willing,
  active participant in its own observation. The metaphor reverses the
  power dynamic: in software, the "watched" controls the process.
- **Observers in the real world observe continuously; software
  observers receive discrete events** -- a security guard watches a
  monitor continuously. A software observer is dormant until a
  notification arrives. The metaphor suggests constant vigilance where
  the reality is event-driven passivity -- observers sleep until poked.
- **The panopticon problem is inverted** -- Bentham's panopticon works
  because prisoners don't know if they're being watched. In the
  Observer pattern, the subject knows exactly how many observers it
  has (it maintains the list). The architectural power of surveillance
  -- uncertainty about being watched -- is absent.
- **"Observer" hides the real complexity: update ordering and
  cascading** -- real surveillance has simple information flow (watch,
  record, report). Software observers can trigger state changes in
  the subject, causing cascading notifications, infinite loops, and
  ordering dependencies. The calm watchfulness of the metaphor masks
  the pattern's potential for chaotic feedback.

## Expressions

- "Subscribe to events" -- registering interest, the observer signing
  up for a watch shift
- "The observer is listening" -- treating notification as perception,
  auditory surveillance
- "Notify all observers" -- broadcasting a change, the subject
  announcing to its watchers
- "Publish-subscribe" -- the pattern's alternate name, shifting from
  surveillance to publishing metaphors
- "Event listener" -- the DOM's synonym, softening "observer" into
  passive attention
- "Unsubscribe" -- ending observation, the watcher going off duty
- "Observer leak" -- forgetting to unsubscribe, a watcher who never
  leaves their post, consuming resources indefinitely

## Origin Story

The Observer pattern has roots in Smalltalk's Model-View-Controller
architecture from the late 1970s, where views needed to update when
models changed. The MVC framework at Xerox PARC formalized the idea
of dependent objects that automatically reflect changes in a model.
The GoF codified this as the Observer pattern in 1994, choosing a name
that emphasizes the watching relationship over the notification
mechanism. The surveillance metaphor has since expanded into variants:
"publish-subscribe" shifts the frame from watching to media
distribution, "event listener" domesticates it into passive attention,
and "reactive streams" moves into fluid dynamics. Each renaming
reflects discomfort with or extension of the original watching
metaphor.

## References

- Gamma, E. et al. *Design Patterns: Elements of Reusable Object-
  Oriented Software* (1994), Chapter 5: Behavioral Patterns
- Krasner, G.E. & Pope, S.T. "A Cookbook for Using the Model-View-
  Controller User Interface Paradigm in Smalltalk-80" (1988) -- the
  MVC architecture that preceded the Observer pattern
- Meszaros, G. & Doble, J. "A Pattern Language for Pattern Writing"
  (1998) -- discusses the naming conventions for patterns
