---
name: studyplan
description: Generate a progressive study course on a technical topic
---

Generate a study course using the studyplan skill.

**Usage:**
- `/studyplan <topic>` — generate a study course on a specific topic
- `/studyplan` — ask what topic to cover

**Examples:**
- `/studyplan embeddings and vector search`
- `/studyplan CRDT-based real-time collaboration`
- `/studyplan WebAssembly for server-side plugins`

The course is saved to `docs/study/YYYY-MM-DD-<topic-slug>.md` and committed.

Invoke the studyplan skill with the topic provided (or ask the user for one).
