---
project_issue: 9
repo: metaphorex/metaphorex
source_type: corpus
status: draft
---

# Playbook: Unix Design Philosophy and C Language Metaphors

## Source Description

The Unix operating system (Bell Labs, 1969-) and the C programming
language (Dennis Ritchie, 1972-) established the metaphorical vocabulary
that nearly all modern computing inherits. This project catalogs the
conceptual metaphors embedded in Unix/C naming decisions, system call
interfaces, and design philosophy.

### Primary Sources
- Thompson, K. & Ritchie, D. "The UNIX Time-Sharing System," CACM 17(7), 1974
- Ritchie, D. "The Development of the C Language," ACM SIGPLAN, 1993
- Kernighan, B. & Ritchie, D. *The C Programming Language* (K&R), 1978/1988
- McIlroy, M.D. Internal Bell Labs memo on pipes, 1964
- McIlroy, M.D. "A Research UNIX Reader," 1987

### Secondary Sources
- Raymond, E.S. *The Art of Unix Programming*, 2003
- Kernighan, B. & Pike, R. *The Unix Programming Environment*, 1984
- Lions' Commentary on UNIX 6th Edition, John Lions, 1977

### RFCs (Networking Metaphors)
- RFC 793 (TCP, 1981) -- handshake, socket, port, window
- RFC 1035 (DNS, 1987) -- domain, zone, delegation, authority

Estimated yield: 35 mappings. Mostly `dead-metaphor` (these terms are so
embedded that speakers no longer recognize them as metaphorical) with one
`paradigm` (everything-is-a-file).

## Access Method

### Primary Archive: Wikipedia "List of Computer Term Etymologies"

**URL:** https://en.wikipedia.org/wiki/List_of_computer_term_etymologies

A structured, well-maintained encyclopedia article that documents the
etymological origins of computing terms. Contains entries for many Unix/C
terms including daemon, boot/bootstrap, cookie, ping, and compiler.
Cross-referenced with cited sources. This provided verification for
approximately 15 candidates.

**Access issues:** Wikipedia returns 403 to automated fetchers; content
was accessed via WebSearch and mirrored at:
- https://en-academic.com/dic.nsf/enwiki/222729
- https://grokipedia.com/page/List_of_computer_term_etymologies

### Secondary Archive: The Jargon File

**URL:** http://www.catb.org/jargon/html/

The hacker culture glossary (ESR, originally Raphael Finkel at Stanford,
1975). Contains detailed etymologies and usage notes for Unix/C
terminology. The daemon entry is particularly well-sourced.

**Access issues:** catb.org has TLS certificate problems (ERR_TLS_CERT_ALTNAME_INVALID).
Individual entries are accessible via specific URLs like
http://www.catb.org/esr/jargon/html/D/daemon.html

### Tertiary Archives: Primary Source Texts Online

- **Ritchie & Thompson CACM 1974 paper:**
  https://www.nokia.com/bell-labs/about/dennis-m-ritchie/cacm.pdf
  https://dsf.berkeley.edu/cs262/unix.pdf
  (Full text, free access. Establishes core terminology: file, shell,
  process, pipe, mount, directory, link, fork, exec, wait, signal.)

- **Ritchie "Development of the C Language" (1993):**
  https://www.nokia.com/bell-labs/about/dennis-m-ritchie/chist.html
  (Discusses naming decisions in C's design.)

- **McIlroy pipes memo origin:**
  http://doc.cat-v.org/unix/pipes/
  (The "garden hose" memo text and commentary.)

- **Linux man pages:**
  https://man7.org/linux/man-pages/
  (Definitive documentation for each system call. Used to verify
  terminology and trace naming history.)

### Cross-Reference Methodology

1. Started with the issue's enumerated metaphor list (18 items)
2. Cross-referenced against Wikipedia etymology list, Jargon File entries,
   and Ritchie/Thompson CACM 1974 paper
3. Expanded to include additional metaphors found in archives but not
   listed in the issue (e.g., tee, trap, heap, stack, thread)
4. Verified each candidate has at least one citable source
5. Excluded terms already in the metaphorex catalog (9 entries)

### Already in Catalog (excluded)

The following Unix/C-origin metaphors already exist in the catalog and
are excluded from this manifest:

- `data-flow-is-fluid-flow` -- pipes/streams general metaphor (seed entry)
- `firewall` -- network security barrier (sw-eng-vernacular)
- `zombie-process` -- terminated but unreaped process (sw-eng-vernacular)
- `orphan-process` -- process whose parent died (sw-eng-vernacular)
- `race-condition` -- concurrent access timing bug (sw-eng-vernacular)
- `garbage-collection` -- automatic memory reclamation (sw-eng-vernacular)
- `sandbox` -- isolated execution environment (sw-eng-vernacular)
- `bottleneck` -- performance constraint point (catalog)
- `the-pipeline-pattern` -- data transformation chain (design-patterns)

Miners should use `related:` to link new entries to these existing ones
where appropriate.

## Extraction Strategy

### For Miners

Each candidate in the manifest has:
- `slug`: filename for `catalog/mappings/{slug}.md`
- `name`: the ALL-CAPS term name
- `kind`: `paradigm`, `dead-metaphor`, or `conceptual-metaphor`
- `source_frame` and `target_frame`: existing or needed frames
- `archive_refs`: specific citations for the Miner to consult
- `description`: brief note on what makes this entry distinctive

**Miner workflow:**

1. Read the `archive_refs` for the candidate -- these are the primary
   research sources. Most link to freely available online texts.
2. For system calls, fetch the man page from man7.org for precise
   terminology and historical context.
3. For candidates with Wikipedia refs, use the etymology article for
   origin story details.
4. The "What It Brings" section should trace the original metaphor:
   what physical/biological/social domain was borrowed, and what
   structural parallels were intended.
5. The "Where It Breaks" section should identify where the metaphor
   misleads. Many of these are dead metaphors -- the break point is
   often that the original source domain has been forgotten entirely.

### Batching Recommendation

Process in thematic clusters:

- **Batch 1 -- Core Unix System (6):** everything-is-a-file, unix-shell,
  kernel, daemon-process, process-fork, unix-pipe. These are the most
  foundational and interconnected. The shell/kernel pairing should be
  mined together.

- **Batch 2 -- Filesystem (5):** filesystem-tree, filesystem-root,
  filesystem-mount, file-permissions, symlink. All relate to the
  spatial metaphor of a hierarchical namespace.

- **Batch 3 -- Process Life Cycle (5):** process-parent-child,
  process-kill, process-sleep, process-trap, unix-signal. The biological
  life/death metaphor system. Should cross-reference existing
  zombie-process and orphan-process entries.

- **Batch 4 -- Plumbing (4):** unix-filter, unix-tee,
  stdin-stdout-stderr, environment-variable. The fluid dynamics cluster.
  Should cross-reference existing data-flow-is-fluid-flow entry.

- **Batch 5 -- C Language (4):** c-pointer, null-pointer, c-string,
  c-casting. The core C naming metaphors.

- **Batch 6 -- Memory (4):** memory-stack, memory-heap, memory-leak,
  buffer-overflow. The spatial/container metaphors for memory management.

- **Batch 7 -- Networking (4):** network-socket, network-port,
  tcp-handshake, dns-domain. The maritime/social networking vocabulary.

- **Batch 8 -- Remaining (3):** process-thread, cron-job, device-driver.

## Schema Mapping

### Kind Assignment

| Category | Kind | Count | Criteria |
|----------|------|-------|----------|
| Paradigm | `paradigm` | 1 | everything-is-a-file (a system of metaphors) |
| Dead metaphor | `dead-metaphor` | 33 | Terms so embedded speakers don't recognize them as metaphors |
| Conceptual metaphor | `conceptual-metaphor` | 1 | c-casting (still somewhat recognizable as metaphorical) |

The overwhelming majority are dead metaphors. Unix/C terminology has been
absorbed so thoroughly into computing culture that "shell", "kernel",
"pipe", "fork", "daemon", "socket", "port", and "string" are experienced
as literal technical terms, not as metaphors borrowed from other domains.

### Frame Inventory

**Existing reusable frames (in catalog):**
- `fluid-dynamics` -- pipes, streams, filters, tees, leaks, overflow
- `embodied-experience` -- stack, heap, pointer, kill, sleep, trap
- `social-roles` -- parent/child processes
- `social-behavior` -- handshake
- `mythology` -- daemon
- `horticulture` -- kernel, tree, root
- `containers` -- shell
- `manufacturing` -- thread, casting
- `governance` -- permissions, domains
- `travel` -- port, driver
- `tool-use` -- socket, fork, mount
- `economics` -- job
- `communication` -- signal
- `software-programs` -- target frame for most entries
- `data-processing` -- target frame for filesystem/networking entries

**New frames potentially needed:**
- None. All source and target frames already exist in the catalog.

### Categories

All entries get `computer-science` as primary category. Additional:
- Networking metaphors: `security` where relevant
- Memory/safety metaphors: `security` where relevant (buffer-overflow)
- Philosophy-adjacent: `philosophy` (null-pointer, everything-is-a-file)
- Systems thinking: `systems-thinking` (memory-leak)

## Gotchas

1. **Overlap with existing catalog entries:** 9 entries are already in the
   catalog from other projects (seed set, sw-eng-vernacular, design-patterns).
   Miners must check the existing entries and use `related:` links rather
   than duplicating content.

2. **The plumbing family is interconnected:** pipe, filter, tee, stream,
   sink, drain, backpressure -- these form a coherent metaphor system.
   The existing `data-flow-is-fluid-flow` entry covers the general
   principle. This project's entries (unix-pipe, unix-filter, unix-tee,
   stdin-stdout-stderr) cover the specific Unix implementations and
   naming decisions. Miners should clearly distinguish the general
   metaphor from the Unix-specific naming.

3. **Dead metaphors require extra work:** For entries marked `dead-metaphor`,
   the "What It Brings" section needs to *resuscitate* the metaphor --
   explain what the original source domain was, because most readers will
   not spontaneously see "shell" as a metaphor from biology/containers.
   The "Where It Breaks" section should explain why the metaphor died
   (typically because the term became purely technical).

4. **The family metaphor is remarkably complete:** fork, parent, child,
   orphan, zombie, kill, inherit, wait, adopt (init). This is one of the
   most internally consistent metaphor systems in computing. Miners
   handling process-parent-child should document the full system.

5. **Historical context matters:** Many of these metaphors were chosen by
   specific people at specific times. Ritchie, Thompson, McIlroy,
   Corbato, and Pouzin made deliberate naming choices. The "Origin Story"
   sections should credit the namers where documented.

6. **"Kernel" predates Unix:** Dijkstra used it for the THE system (1968).
   "Shell" predates Unix too -- Pouzin coined it for Multics (1964-65).
   Unix inherited and cemented these terms but did not originate all of them.
   Miners should note the pre-Unix history.

7. **Plan 9 as the logical extension:** Several metaphors (especially
   everything-is-a-file, mount, namespace) were pushed further in Plan 9
   from Bell Labs (1992). This is useful context for "What It Brings" but
   should not dominate the entries.

8. **C's pointer metaphor is unique:** Most languages have abstracted away
   pointers. C is the only mainstream language where the pointing metaphor
   is still directly manipulated by the programmer. This makes c-pointer
   a particularly rich entry -- the metaphor is alive in C but dead in
   languages that hide it.

9. **The violence of process management:** kill, terminate, abort, die,
   trap, signal, interrupt -- the process lifecycle vocabulary is
   surprisingly violent. This is worth noting in process-kill but should
   not be belabored across multiple entries.

10. **RFC terminology is formal:** The networking metaphors (socket, port,
    handshake, domain) are defined precisely in RFCs. Miners should cite
    the specific RFC text that introduces each term, not just describe it
    in general terms.
