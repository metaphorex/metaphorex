---
slug: network-socket
name: "Network Socket"
kind: dead-metaphor
source_frame: tool-use
target_frame: network-communication
categories:
  - computer-science
author: agent:metaphorex-miner
harness: "Claude Code"
contributors: []
related:
  - network-port
  - tcp-handshake
---

## What It Brings

A socket is a hollow opening into which something is inserted to make a
connection -- a lightbulb socket, a wall socket, an eye socket. The
Berkeley sockets API (1983), designed by Bill Joy and Sam Leffler for
4.2BSD, borrowed this term to name the endpoint of a network connection.
You create a socket, bind it to an address, and then either listen for
incoming connections or connect to a remote socket. The metaphor imports
several structural features from the physical domain.

Key structural parallels:

- **Standardized interface** -- a wall socket accepts any plug that
  conforms to the standard. A network socket accepts any connection that
  speaks the right protocol. The metaphor encodes the idea that the
  interface is generic and the specifics are negotiated by what gets
  plugged in. This is why the same socket API serves TCP, UDP, Unix
  domain sockets, and raw sockets -- the "shape of the opening" varies
  by address family, but the abstraction remains a socket.
- **Fixed endpoint** -- a physical socket is mounted in a wall or fixture.
  It does not move. A network socket is bound to an address and port. The
  metaphor imports stationarity: once a server socket is bound, it stays
  there, waiting for connections like an electrical outlet waiting for a
  plug.
- **Connection through insertion** -- the plug-and-socket model implies
  that connection requires physical contact between two complementary
  parts. The Berkeley API models this as `connect()` on the client side
  and `accept()` on the server side -- two halves joining to form a
  complete circuit.
- **Bidirectional flow once connected** -- once a plug is in a socket,
  electricity flows. Once a network socket connection is established,
  data flows in both directions. The metaphor naturally suggests
  full-duplex communication, which is exactly what TCP sockets provide.

## Where It Breaks

- **Sockets are not physical objects** -- a physical socket is a thing you
  can see and touch. A network socket is a kernel data structure: a file
  descriptor associated with a protocol, a local address, a remote
  address, and some state. The metaphor encourages thinking of sockets as
  scarce physical resources, which is partially true (file descriptor
  limits) but misleading about their nature. You cannot "wear out" a
  socket by using it too much, and creating a new socket costs nothing
  like installing an electrical outlet.
- **The multiplexing problem has no physical analog** -- a wall socket
  serves one plug. A server socket, through `accept()`, spawns a new
  connected socket for each client while continuing to listen. This is
  like an electrical outlet that, when you plug something in, grows a
  new outlet next to itself. The metaphor provides no vocabulary for
  this one-to-many behavior, which is why the `listen()`/`accept()`
  pattern confuses every programmer learning socket programming for
  the first time.
- **Socket "types" are invisible** -- physical sockets vary by visible
  shape: a lightbulb socket, a USB socket, an RJ45 jack. Network socket
  types (SOCK_STREAM, SOCK_DGRAM, SOCK_RAW) are invisible protocol
  choices. The metaphor suggests you could "look at" a socket and know
  what it accepts, but a network socket's type is determined at creation
  time by a parameter, not by observable shape.
- **The metaphor died into the API** -- programmers calling `socket()`,
  `bind()`, `listen()`, `accept()`, and `close()` do not think about
  lightbulb sockets or wall outlets. The term is experienced as a pure
  technical noun. The Berkeley sockets API is so foundational that the
  word "socket" in computing now primarily means "network endpoint," and
  the physical origin is trivia rather than active metaphor.

## Expressions

- "Open a socket" -- create the endpoint, borrowing from "open" as in
  opening a file (itself a spatial metaphor)
- "Socket programming" -- the entire subdomain of network programming,
  named after the metaphor
- "Socket pair" -- the two endpoints of a connection, like two sockets
  wired together
- "Raw socket" -- a socket without protocol processing, where "raw"
  imports the cooking metaphor (unprocessed, uncooked)
- "Unix domain socket" -- a socket for local inter-process communication,
  where the network metaphor is applied to processes on the same machine
- "Socket exhaustion" -- running out of available sockets, treating the
  abstraction as a finite physical resource

## Origin Story

The Berkeley sockets API was developed for 4.2BSD Unix in 1983 by Bill
Joy, Sam Leffler, and colleagues at UC Berkeley's Computer Systems
Research Group. The API needed to provide a uniform interface for network
communication that felt natural within Unix's "everything is a file"
philosophy. The term "socket" was chosen because the connection model --
two endpoints that join to form a communication channel -- mapped onto the
plug-and-socket model from electrical engineering.

The choice was consequential. The Berkeley sockets API became the de facto
standard for network programming across virtually all operating systems.
Windows Sockets (Winsock) adopted the same abstraction and naming. The
POSIX standard codified it. Every modern programming language provides
socket abstractions that trace back to the 1983 BSD interface and its
physical-connection metaphor.

## References

- Joy, W. et al. *4.2BSD System Manual*, University of California,
  Berkeley, 1983
- Stevens, W.R. *Unix Network Programming*, Prentice Hall, 1990
- RFC 793, "Transmission Control Protocol," Postel, J., 1981
- IEEE Std 1003.1 (POSIX), socket interface specification
