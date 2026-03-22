---
created: '2026-03-22'
name: Distributed Systems
related:
- information-security
- software-architecture
roles:
- node
- cluster
- partition
- replica
- consensus
- heartbeat
- failover
- coordinator
slug: distributed-systems
updated: '2026-03-22'
---

Computing systems in which components located on networked computers
communicate and coordinate their actions by passing messages. The frame
foregrounds the fundamental tensions of distribution: consistency vs.
availability, detection vs. false positives, and the impossibility of
distinguishing a slow node from a dead one. Its core structural insight is
that coordination without shared memory requires protocols that trade off
between safety (never doing the wrong thing) and liveness (eventually doing
something). Failure detection, leader election, and state replication are the
recurring problems; consensus algorithms, heartbeat protocols, and quorum
systems are the recurring solutions.
