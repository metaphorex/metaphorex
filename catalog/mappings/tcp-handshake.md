---
author: agent:metaphorex-miner
categories:
- computer-science
contributors:
- fshot
created: '2026-03-15'
harness: Claude Code
kind: dead-metaphor
name: TCP Handshake
related:
- network-socket
- network-port
slug: tcp-handshake
source_frame: social-behavior
target_frame: data-processing
updated: '2026-03-15'
---

## What It Brings

A handshake is one of the oldest human social rituals: two parties extend
hands, grasp, and release, signaling mutual recognition, good faith, and
the absence of concealed weapons. TCP's three-way handshake (SYN, SYN-ACK,
ACK) borrows this social contract to describe connection establishment
between two machines. The metaphor is remarkably precise -- more so than
most networking terminology.

Key structural parallels:

- **Bilateral consent** -- a handshake requires both parties to
  participate. You cannot shake hands with someone who refuses. TCP's
  three-way handshake encodes the same requirement: the initiator sends
  SYN ("I want to connect"), the responder sends SYN-ACK ("I agree, and
  I want to connect too"), and the initiator confirms with ACK ("agreed,
  we are connected"). Neither party can be coerced into a connection.
  A refused handshake maps directly to a RST (reset) packet.
- **Sequence as protocol** -- a physical handshake follows an implicit
  protocol: extend, grasp, shake, release. Deviation is noticed (the
  too-long grip, the limp hand, the refusal to let go). TCP's handshake
  similarly has a strict sequence, and deviation is an error condition.
  The metaphor imports the idea that communication requires an agreed-upon
  ritual before the actual conversation can begin.
- **Identity and trust establishment** -- shaking hands traditionally
  means "I am who I appear to be, and I mean you no harm." TCP's
  handshake establishes that both endpoints exist and are responsive,
  though it does not authenticate identity (that requires TLS, a layer
  above). The trust is shallow -- presence, not identity -- just as a
  handshake with a stranger establishes contact, not trustworthiness.
- **The handshake as preamble** -- in social settings, you shake hands
  before the conversation, not during it. The TCP handshake similarly
  precedes data transfer. It is overhead, a cost paid for the assurance
  of reliable communication. This maps to the real performance cost of
  connection establishment: three round trips before any payload flows.

## Where It Breaks

- **Handshakes are symmetric; TCP's is not** -- a physical handshake is
  roughly equal: both parties extend, both grasp. TCP's three-way
  handshake is asymmetric: one party initiates (the client sends SYN),
  the other responds (the server sends SYN-ACK). There is an inherent
  client-server power dynamic that the social metaphor obscures. The
  server is always waiting to be approached; the client always initiates.
  Physical handshakes do not have this built-in hierarchy.
- **SYN flood attacks exploit the metaphor's trust assumption** -- the
  social handshake assumes good faith. TCP's handshake can be weaponized:
  a SYN flood sends thousands of half-open handshakes, exhausting the
  server's resources waiting for ACKs that never come. This is like
  someone extending their hand to a thousand people simultaneously and
  leaving them all hanging. The metaphor has no vocabulary for this
  deliberate abuse because social handshakes assume a one-to-one,
  good-faith encounter.
- **No physical co-presence** -- a handshake requires physical proximity.
  TCP endpoints can be on opposite sides of the planet. The metaphor
  imports an intimacy and directness that does not exist in network
  communication, where packets traverse dozens of intermediary routers.
  The "handshake" feels like a direct connection, but it is mediated
  by an entire infrastructure that the metaphor renders invisible.
- **The metaphor died because it succeeded** -- network engineers say
  "three-way handshake" without any image of hands or greeting rituals.
  The term has become pure jargon, detached from its source domain.
  This is the defining mark of a dead metaphor: the word survives, but
  the image does not.

## Expressions

- "Three-way handshake" -- the standard technical term for TCP connection
  establishment, used in every networking textbook
- "The handshake failed" -- connection could not be established, mapping
  to a refused or unanswered social greeting
- "Handshake timeout" -- the other party did not respond in time, like
  an extended hand left hanging
- "TLS handshake" -- the security layer's own connection ritual, a
  handshake on top of a handshake, adding identity verification to
  the presence verification of TCP
- "SYN flood" -- weaponizing the handshake by overwhelming the server
  with half-completed greetings

## Origin Story

The term "handshake" for a connection establishment protocol predates
TCP. It appears in telecommunications and modem protocols of the 1960s
and 1970s, where two devices would exchange signals to agree on
communication parameters (baud rate, parity) before data transfer.
TCP's three-way handshake was formalized in RFC 793 (September 1981)
by Jon Postel, which describes the SYN, SYN-ACK, ACK sequence. Postel
did not invent the handshake metaphor but cemented it in the protocol
specification that became the foundation of the internet. The term was
natural enough that it required no explanation even in 1981 -- engineers
already understood what a "handshake" meant in a protocol context.

## References

- Postel, J. "Transmission Control Protocol," RFC 793 (1981) -- the
  specification that formalized TCP's three-way handshake
- Eddy, W. "Transmission Control Protocol (TCP)," RFC 9293 (2022) --
  the modern TCP specification, still using handshake terminology
- Wikipedia, "Handshaking" -- documents the pre-TCP history of
  handshake protocols in telecommunications
