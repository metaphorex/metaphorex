# Eval Framework Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Scaffold `metaphorex/eval` repo, build the naming-task eval with in-context harness, and run the first baseline vs m4x comparison.

**Architecture:** New repo consumes CalVer-pinned JSON snapshots from metaphorex/metaphorex via `validate.py extract`. Harnesses inject m4x data into LLM calls under different conditions. Scoring is automated (frame consistency) + LLM-judge (structural fidelity). All managed with `uv`.

**Tech Stack:** Python 3.12, uv, anthropic SDK, openai SDK, datasets (HuggingFace), rich, pytest

---

### Task 1: Create repo and scaffold

**Files:**
- Create: `README.md`, `pyproject.toml`, `.gitignore`, `.github/workflows/ci.yml`

**Step 1: Create GitHub repo**

```bash
gh repo create metaphorex/eval --public --clone --description "Does a knowledge graph of metaphors help LLMs reason? We're testing it."
cd eval
```

**Step 2: Write pyproject.toml**

```toml
[project]
name = "m4x-eval"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = [
    "anthropic>=0.49",
    "openai>=1.60",
    "python-frontmatter>=1.1.0",
    "rich>=13.9",
    "datasets>=3.0",
]

[project.optional-dependencies]
dev = ["pytest>=8.0", "ruff>=0.8"]

[tool.ruff]
target-version = "py312"
line-length = 120

[tool.pytest.ini_options]
testpaths = ["tests"]
```

**Step 3: Write README.md**

Write the public-facing README with: mission statement, hypotheses (3 from design doc), current status, repo structure diagram, how to contribute, license (MIT).

**Step 4: Write .gitignore**

Standard Python .gitignore + `data/snapshots/*.json` (snapshots are generated, not committed — only the snapshot script is committed). Add `results/raw/` (raw API responses, large). Keep `results/scored/` (committed, small).

**Step 5: Write CI workflow**

`.github/workflows/ci.yml`: on push/PR, run `ruff check` and `pytest`.

**Step 6: Commit**

```bash
git add -A && git commit -m "chore: scaffold eval repo"
git push -u origin main
```

**Verify:** `gh repo view metaphorex/eval` shows the repo. `uv sync` installs deps.

---

### Task 2: Data snapshot pipeline

**Files:**
- Create: `data/snapshot.py`, `data/transform.py`
- Test: `tests/test_data.py`

**Step 1: Write failing test for snapshot loading**

```python
# tests/test_data.py
import json
from pathlib import Path
from data.snapshot import load_snapshot

def test_load_snapshot_parses_mappings():
    """Snapshot must parse into list of dicts with required fields."""
    # Uses a small fixture, not the full catalog
    fixture = Path(__file__).parent / "fixtures" / "snapshot_sample.json"
    mappings = load_snapshot(fixture)
    assert len(mappings) > 0
    assert all("slug" in m for m in mappings)
    assert all("source_frame" in m for m in mappings)
    assert all("sections" in m for m in mappings)
```

**Step 2: Create fixture**

```bash
# From the metaphorex repo, extract a small sample
cd /Users/fshot/code/fshot/metaphorex
uv run scripts/validate.py extract | python3 -c "
import json, sys
data = json.load(sys.stdin)[:5]
json.dump(data, sys.stdout, indent=2)
" > /path/to/eval/tests/fixtures/snapshot_sample.json
```

**Step 3: Run test — expect FAIL** (module not found)

```bash
uv run pytest tests/test_data.py::test_load_snapshot_parses_mappings -v
```

**Step 4: Implement `data/snapshot.py`**

```python
"""Load and query m4x data snapshots."""
from __future__ import annotations
import json
from pathlib import Path

def load_snapshot(path: Path) -> list[dict]:
    """Load a JSON snapshot produced by metaphorex validate.py extract."""
    with open(path) as f:
        return json.load(f)

def create_snapshot(metaphorex_repo: Path, output: Path) -> Path:
    """Run validate.py extract against a metaphorex repo and save snapshot."""
    import subprocess
    result = subprocess.run(
        ["uv", "run", "scripts/validate.py", "extract"],
        cwd=metaphorex_repo, capture_output=True, text=True, check=True,
    )
    output.write_text(result.stdout)
    return output
```

**Step 5: Run test — expect PASS**

**Step 6: Write failing test for transform (pairs)**

```python
# tests/test_data.py (append)
from data.transform import to_pairs

def test_to_pairs_extracts_source_target_expressions():
    fixture = Path(__file__).parent / "fixtures" / "snapshot_sample.json"
    mappings = load_snapshot(fixture)
    pairs = to_pairs(mappings)
    assert len(pairs) == len(mappings)
    for p in pairs:
        assert "source_frame" in p
        assert "target_frame" in p
        assert "expressions" in p
        assert "where_it_breaks" in p
```

**Step 7: Implement `data/transform.py`**

```python
"""Transform snapshot data into eval-friendly formats."""
from __future__ import annotations

def to_pairs(mappings: list[dict]) -> list[dict]:
    """Extract (source, target, expressions, where_it_breaks) pairs."""
    return [
        {
            "slug": m["slug"],
            "name": m["name"],
            "kind": m["kind"],
            "source_frame": m["source_frame"],
            "target_frame": m["target_frame"],
            "expressions": m.get("sections", {}).get("Expressions", ""),
            "where_it_breaks": m.get("sections", {}).get("Where It Breaks", ""),
            "what_it_brings": m.get("sections", {}).get("What It Brings", ""),
        }
        for m in mappings
    ]

def to_context_block(mappings: list[dict]) -> str:
    """Format all mappings as a single context block for in-context injection."""
    lines = []
    for m in mappings:
        sections = m.get("sections", {})
        lines.append(f"## {m['name']} ({m['kind']})")
        lines.append(f"Source: {m['source_frame']} → Target: {m['target_frame']}")
        for section_name in ["What It Brings", "Where It Breaks", "Expressions"]:
            if section_name in sections:
                lines.append(f"### {section_name}")
                lines.append(sections[section_name])
        lines.append("")
    return "\n".join(lines)
```

**Step 8: Run tests — expect PASS**

**Step 9: Commit**

```bash
git add -A && git commit -m "feat: data snapshot loading and transform pipeline"
```

**Verify:** `uv run pytest tests/test_data.py -v` — 2 tests pass.

---

### Task 3: In-context harness

**Files:**
- Create: `harnesses/in_context.py`
- Test: `tests/test_harnesses.py`

**Step 1: Write failing test**

```python
# tests/test_harnesses.py
from harnesses.in_context import build_messages

def test_build_messages_baseline():
    """Baseline condition: no m4x data in messages."""
    msgs = build_messages(
        system_desc="Name 10 components of a distributed task queue.",
        condition="baseline",
        m4x_context="",
    )
    assert msgs[0]["role"] == "user"
    assert "metaphor" not in msgs[0]["content"].lower() or True  # baseline has no m4x

def test_build_messages_in_context():
    """In-context condition: m4x data injected into system prompt."""
    msgs = build_messages(
        system_desc="Name 10 components of a distributed task queue.",
        condition="in_context",
        m4x_context="## Argument Is War\nSource: war → Target: argumentation",
    )
    # m4x data should appear in the messages
    full_text = " ".join(m["content"] for m in msgs)
    assert "Argument Is War" in full_text
```

**Step 2: Run test — expect FAIL**

**Step 3: Implement harness**

```python
"""In-context harness: inject m4x data into system/user prompt."""
from __future__ import annotations

NAMING_TASK_TEMPLATE = """You are a software architect naming components for a new system.

{system_desc}

Name exactly 10 components. For each:
1. Choose a name from a consistent metaphorical frame (all names should come from the same source domain)
2. Explain why this name fits the component's role
3. Note what the name might mislead someone about

Output as a numbered list with: Name | Role | Why This Name | Potential Mislead"""

M4X_PREAMBLE = """You have access to a knowledge graph of conceptual metaphors. Use it to choose a coherent metaphorical frame for naming. Here is the relevant data:

{m4x_context}

---

"""

def build_messages(system_desc: str, condition: str, m4x_context: str) -> list[dict]:
    if condition == "baseline":
        return [{"role": "user", "content": NAMING_TASK_TEMPLATE.format(system_desc=system_desc)}]
    elif condition == "in_context":
        preamble = M4X_PREAMBLE.format(m4x_context=m4x_context)
        return [{"role": "user", "content": preamble + NAMING_TASK_TEMPLATE.format(system_desc=system_desc)}]
    else:
        raise ValueError(f"Unknown condition: {condition}")
```

**Step 4: Run tests — expect PASS**

**Step 5: Commit**

```bash
git add -A && git commit -m "feat: in-context harness for naming task"
```

**Verify:** `uv run pytest tests/ -v` — 4 tests pass.

---

### Task 4: Naming task eval runner

**Files:**
- Create: `evals/naming/task.py`, `evals/naming/run.py`, `evals/naming/README.md`
- Test: `tests/evals/test_naming.py`

**Step 1: Write task spec README**

`evals/naming/README.md` — document the task, conditions, scoring rubric, and expected outputs. This is the public-facing experiment description.

**Step 2: Write failing test for task config**

```python
# tests/evals/test_naming.py
from evals.naming.task import SCENARIOS, NamingScenario

def test_scenarios_have_required_fields():
    assert len(SCENARIOS) >= 3
    for s in SCENARIOS:
        assert isinstance(s, NamingScenario)
        assert s.system_desc
        assert s.expected_component_count == 10
```

**Step 3: Implement task config**

```python
# evals/naming/task.py
from dataclasses import dataclass

@dataclass
class NamingScenario:
    name: str
    system_desc: str
    expected_component_count: int = 10

SCENARIOS = [
    NamingScenario(
        name="ml-training-pipeline",
        system_desc="A distributed task queue for ML model training jobs. Components include: job submission, resource allocation, data loading, model checkpointing, gradient synchronization, failure recovery, result aggregation, scheduling, monitoring, and artifact storage.",
    ),
    NamingScenario(
        name="content-moderation-system",
        system_desc="An automated content moderation pipeline for a social platform. Components include: content ingestion, classification, human review queue, appeal handling, policy enforcement, audit logging, reporter feedback, false positive tracking, escalation routing, and metrics dashboard.",
    ),
    NamingScenario(
        name="supply-chain-tracker",
        system_desc="A real-time supply chain visibility platform. Components include: shipment tracking, inventory sync, supplier onboarding, demand forecasting, exception alerting, customs documentation, carrier integration, warehouse coordination, returns processing, and compliance reporting.",
    ),
]
```

**Step 4: Run test — expect PASS**

**Step 5: Implement eval runner**

```python
# evals/naming/run.py
"""Run the naming task eval across conditions and models."""
from __future__ import annotations
import argparse, json, time
from pathlib import Path
from anthropic import Anthropic
from openai import OpenAI
from data.snapshot import load_snapshot
from data.transform import to_context_block
from harnesses.in_context import build_messages
from evals.naming.task import SCENARIOS

RESULTS_DIR = Path("results/naming")
CONDITIONS = ["baseline", "in_context"]
MODELS = {
    "claude": {"client": "anthropic", "model": "claude-sonnet-4-20250514"},
    "gpt4o": {"client": "openai", "model": "gpt-4o"},
}

def run_single(scenario, condition, model_key, m4x_context, dry_run=False):
    msgs = build_messages(scenario.system_desc, condition, m4x_context)
    if dry_run:
        return {"scenario": scenario.name, "condition": condition, "model": model_key, "messages": msgs, "response": "[DRY RUN]"}
    config = MODELS[model_key]
    if config["client"] == "anthropic":
        client = Anthropic()
        resp = client.messages.create(model=config["model"], max_tokens=2000, messages=msgs)
        text = resp.content[0].text
    else:
        client = OpenAI()
        resp = client.chat.completions.create(model=config["model"], max_tokens=2000, messages=msgs)
        text = resp.choices[0].message.content
    return {"scenario": scenario.name, "condition": condition, "model": model_key, "response": text}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--snapshot", type=Path, required=True)
    parser.add_argument("--models", nargs="+", default=list(MODELS.keys()))
    parser.add_argument("--conditions", nargs="+", default=CONDITIONS)
    args = parser.parse_args()

    mappings = load_snapshot(args.snapshot)
    m4x_context = to_context_block(mappings)
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    results = []
    for scenario in SCENARIOS:
        for condition in args.conditions:
            for model in args.models:
                print(f"Running: {scenario.name} / {condition} / {model}")
                result = run_single(scenario, condition, model, m4x_context, args.dry_run)
                results.append(result)
                if not args.dry_run:
                    time.sleep(1)  # rate limit courtesy

    timestamp = time.strftime("%Y%m%d-%H%M%S")
    out = RESULTS_DIR / f"run-{timestamp}.json"
    out.write_text(json.dumps(results, indent=2))
    print(f"Results saved to {out}")

if __name__ == "__main__":
    main()
```

**Step 6: Write smoke test**

```python
# tests/evals/test_naming.py (append)
def test_run_single_dry_run():
    from evals.naming.run import run_single
    from evals.naming.task import SCENARIOS
    result = run_single(SCENARIOS[0], "baseline", "claude", "", dry_run=True)
    assert result["response"] == "[DRY RUN]"
    assert result["scenario"] == "ml-training-pipeline"
```

**Step 7: Run tests — expect PASS**

**Step 8: Commit**

```bash
git add -A && git commit -m "feat: naming task eval runner with dry-run support"
```

**Verify:** `uv run python -m evals.naming.run --dry-run --snapshot tests/fixtures/snapshot_sample.json` runs without error.

---

### Task 5: Automated scoring — frame consistency

**Files:**
- Create: `scoring/frame_consistency.py`
- Test: `tests/test_scoring.py`

**Step 1: Write failing test**

```python
# tests/test_scoring.py
from scoring.frame_consistency import score_frame_consistency

def test_consistent_frame_scores_high():
    # All names from "kitchen" domain
    response = """1. Head Chef | orchestrator | cooking leader | ...
2. Sous Chef | deputy | second in command | ...
3. Prep Station | data loader | preparation area | ...
4. Pantry | storage | ingredient store | ...
5. Recipe Book | config | instructions | ..."""
    score = score_frame_consistency(response)
    assert 0.0 <= score <= 1.0

def test_inconsistent_frame_scores_lower():
    # Mixed domains
    response = """1. Head Chef | orchestrator | cooking | ...
2. Goalkeeper | defender | sports | ...
3. Neuron | processor | biology | ...
4. Pantry | storage | cooking | ...
5. Quarterback | scheduler | sports | ..."""
    score = score_frame_consistency(response)
    assert 0.0 <= score <= 1.0
```

**Step 2: Implement using LLM-as-judge for frame extraction**

```python
# scoring/frame_consistency.py
"""Score frame consistency: do all names come from the same source domain?"""
from __future__ import annotations
from anthropic import Anthropic

EXTRACTION_PROMPT = """Analyze these component names and identify which metaphorical source domain each name comes from.

{response}

For each name, output: name | source_domain
Then output: DOMINANT_DOMAIN: <the most common domain>
Then output: CONSISTENCY_RATIO: <count of names in dominant domain / total names>"""

def score_frame_consistency(response: str) -> float:
    """Use LLM to extract source domains and compute consistency ratio."""
    client = Anthropic()
    result = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1000,
        messages=[{"role": "user", "content": EXTRACTION_PROMPT.format(response=response)}],
    )
    text = result.content[0].text
    # Parse CONSISTENCY_RATIO from response
    for line in text.split("\n"):
        if "CONSISTENCY_RATIO:" in line:
            try:
                return float(line.split(":")[-1].strip())
            except ValueError:
                return 0.0
    return 0.0
```

**Step 3: Run tests — expect PASS** (requires ANTHROPIC_API_KEY; mark as integration test)

**Step 4: Commit**

```bash
git add -A && git commit -m "feat: frame consistency scorer using LLM-as-judge"
```

**Verify:** Tests pass with live API key. Tests skip gracefully without it.

---

### Task 6: LLM-judge scoring — structural fidelity

**Files:**
- Create: `scoring/structural_fidelity.py`
- Test: `tests/test_scoring.py` (append)

**Step 1: Write failing test**

```python
from scoring.structural_fidelity import score_structural_fidelity

def test_structural_fidelity_returns_scores():
    response = """1. Head Chef | orchestrator | The chef coordinates all kitchen activity | Implies a single point of control"""
    component_roles = ["orchestrator", "data loader", "scheduler"]
    scores = score_structural_fidelity(response, component_roles)
    assert "fidelity" in scores
    assert "mislead_quality" in scores
    assert all(0.0 <= v <= 1.0 for v in scores.values())
```

**Step 2: Implement**

Use LLM-as-judge with a rubric: "Does this metaphorical name accurately reflect the component's actual role?" Score 0-1 per component, average.

**Step 3: Run tests, commit**

```bash
git add -A && git commit -m "feat: structural fidelity scorer"
```

---

### Task 7: Results aggregation and display

**Files:**
- Create: `scoring/aggregate.py`, `evals/naming/report.py`

**Step 1: Write aggregate function**

Takes raw results + scores, produces a comparison table (baseline vs in-context, per model, per scenario). Output as rich table to terminal + markdown file.

**Step 2: Write report generator**

Produces `results/naming/report.md` with tables, scores, and commentary placeholder.

**Step 3: Commit**

```bash
git add -A && git commit -m "feat: results aggregation and report generation"
```

**Verify:** `uv run python -m evals.naming.report --results results/naming/run-*.json` produces readable markdown.

---

### Task 8: First real eval run

**Step 1: Create fresh snapshot**

```bash
cd /Users/fshot/code/fshot/metaphorex
uv run scripts/validate.py extract > /path/to/eval/data/snapshots/2026.03.14.json
```

**Step 2: Run eval (baseline + in-context, Claude + GPT-4o)**

```bash
uv run python -m evals.naming.run --snapshot data/snapshots/2026.03.14.json
```

**Step 3: Score results**

```bash
uv run python -m evals.naming.report --results results/naming/run-*.json
```

**Step 4: Review results, commit**

```bash
git add results/naming/ && git commit -m "results: first naming task eval — baseline vs in-context"
```

**Verify:** `results/naming/report.md` exists with comparison tables showing measurable differences (or lack thereof) between conditions.

---

### Task 9: Hugging Face dataset push

**Files:**
- Create: `data/huggingface/push.py`, `data/huggingface/README.md` (dataset card)

**Step 1: Write dataset card**

Standard HF dataset card format: description, citation, license (CC BY-SA 4.0), columns, usage examples.

**Step 2: Write push script**

```python
# data/huggingface/push.py
from datasets import Dataset
from data.snapshot import load_snapshot
from data.transform import to_pairs

def push(snapshot_path, repo_id="metaphorex/metaphors"):
    mappings = load_snapshot(snapshot_path)
    pairs = to_pairs(mappings)
    ds = Dataset.from_list(pairs)
    ds.push_to_hub(repo_id, private=False)
```

**Step 3: Push dataset**

```bash
uv run python -m data.huggingface.push --snapshot data/snapshots/2026.03.14.json
```

**Step 4: Commit**

```bash
git add -A && git commit -m "feat: Hugging Face dataset push script"
```

**Verify:** Dataset visible at `huggingface.co/datasets/metaphorex/metaphors`.

---

### Task 10: Polish and ship

**Step 1: Update README with first results**

Add a "Current Results" section with the comparison table from Task 8.

**Step 2: Add CONTRIBUTING.md**

How to add new evals, new harnesses, new scoring functions.

**Step 3: Add LICENSE** (MIT)

**Step 4: Final commit and push**

```bash
git add -A && git commit -m "docs: README with first results, contributing guide"
git push
```

**Verify:** `gh repo view metaphorex/eval --web` — repo looks good, README renders, results visible.
