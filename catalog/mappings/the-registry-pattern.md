---
author: agent:metaphorex-miner
categories:
- software-engineering
contributors:
- fshot
created: '2026-03-10'
harness: Claude Code
kind: archetype
name: The Registry Pattern
provenance: fowler-peaa
related:
- the-repository-pattern
- the-state-pattern
slug: the-registry-pattern
source_frame: governance
target_frame: software-abstraction
updated: '2026-03-14'
---

## What It Brings

A registry is a government office that maintains official records. The
registry of births, deaths, and marriages. The land registry. The
registry of motor vehicles. These are bureaucratic institutions where
entities are recorded, looked up, and verified against authoritative
records. Fowler's Registry pattern maps this onto software: a
well-known object that other objects use to find common objects and
services.

Key structural parallels:

- **The registry is authoritative** -- when you need to know who owns
  a property, you check the land registry, not the neighbor's
  recollection. A software Registry is the single authoritative source
  for locating services or shared objects. The governance metaphor
  establishes that the registry's answer is the truth, not a guess.
- **Registration is a formal act** -- you don't just exist; you must
  register. A birth must be recorded to be officially recognized. In
  the pattern, services must explicitly register themselves before they
  can be found. The bureaucratic metaphor frames registration as a
  necessary formality that grants legitimacy.
- **Lookup is the primary operation** -- people visit the registry to
  look things up, not to browse. The pattern's core operation is
  `Registry.get(key)`. The metaphor shapes the API: you arrive knowing
  what you want, and the clerk retrieves it.
- **The registry is a known location** -- everyone knows where the
  town hall is. A software Registry is typically a well-known global
  or singleton object. The metaphor naturalizes the single access
  point: of course there's one registry, and of course everyone knows
  where it is.
- **Categories and classification matter** -- government registries
  organize records by type: births in one ledger, marriages in
  another. A software Registry often organizes services by interface
  type or string key. The metaphor imports the bureaucratic instinct
  for classification.

## Where It Breaks

- **Government registries are trustworthy because they're backed by
  law; software registries just hold references** -- a land registry
  entry is backed by the legal system. A software Registry entry is
  backed by whatever object was registered, which may be null,
  misconfigured, or no longer running. The governance metaphor imports
  authority and reliability that the pattern doesn't inherently
  provide. Looking something up in a Registry doesn't guarantee it
  works.
- **Registries become god objects** -- a government registry's scope
  is limited by jurisdiction. A software Registry has no natural scope
  boundary. Developers add more and more entries until the Registry
  becomes a global grab bag -- a service locator that everything
  depends on. The bureaucratic metaphor suggests orderly
  administration; the reality is often a bloated singleton that
  couples the entire application.
- **The bureaucracy metaphor carries negative connotations** -- nobody
  enjoys visiting the DMV. Calling a pattern a "registry" imports
  associations of inefficiency, red tape, and overhead. Developers
  sometimes resist the pattern because the name feels heavy for what
  is often just a `Map<String, Object>`. The metaphor over-dignifies
  a dictionary lookup.
- **Real registries handle updates with legal process; software
  registries are mutable** -- changing a birth certificate requires
  court orders. Overwriting a Registry entry requires one line of
  code. The governance metaphor suggests permanence and deliberation
  where the pattern offers casual mutability. Nothing prevents a
  registration from being silently overwritten.
- **The registry pattern has been largely replaced** -- dependency
  injection containers do what Registries do, but without the
  service locator anti-pattern's global coupling. The governance
  metaphor persists in names (Windows Registry, Docker Registry,
  npm registry) while the GoF/Fowler pattern itself is often
  discouraged. The metaphor outlived its pattern.

## Expressions

- "Register a service" -- the formal act of recording, making the
  service officially available
- "Look up in the registry" -- consulting the authoritative record,
  the clerk behind the counter
- "Service locator" -- the Registry's alternate name, less
  bureaucratic, more functional
- "The Windows Registry" -- the most famous software registry, a
  hierarchical database of configuration that every Windows user has
  cursed
- "Container registry" -- Docker's usage, a storehouse of images
  available for deployment
- "Package registry" -- npm, PyPI, the catalog of available software
  components

## Origin Story

The Registry pattern was described by Martin Fowler in *Patterns of
Enterprise Application Architecture* (2002) as a well-known object
that other objects can use to find common objects and services. The
governance metaphor was deliberate: Fowler wanted to convey a central,
authoritative lookup mechanism. The pattern is closely related to the
Service Locator pattern, which Martin Fowler later criticized in his
influential 2004 article "Inversion of Control Containers and the
Dependency Injection Pattern," arguing that Service Locators (and by
extension, Registries) create hidden dependencies. Despite this
critique, the registry metaphor thrives at larger scales -- container
registries, package registries, and DNS itself function as distributed
registries. The word has proven more durable than the pattern.

## References

- Fowler, Martin. *Patterns of Enterprise Application Architecture*
  (2002), Chapter 18: Base Patterns
- Fowler, Martin. "Inversion of Control Containers and the Dependency
  Injection Pattern" (2004) -- the critique of Service Locator
- Microsoft. "Windows Registry" documentation -- the most ubiquitous
  software registry in practice
