#!/usr/bin/env python3
"""Dependency-free Antigravity research gate.

The hook enforces research discipline without doing research itself. It gives
Gemini a compact reminder to use persistent state and the search cache, and it
prevents a cycle from ending without a usable next investigation.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "state"
REQUIRED = [
    STATE / "world-model.md",
    STATE / "uncertainty-map.md",
    STATE / "hypothesis-pool.md",
    STATE / "research-queue.md",
    STATE / "dead-ends.md",
    STATE / "search-cache.md",
]


def main() -> None:
    event = json.load(sys.stdin)
    hook = event.get("hook_event_name", "unknown")

    missing = [str(p.relative_to(ROOT)) for p in REQUIRED if not p.exists()]

    if hook == "PreInvocation":
        context = (
            "RESEARCH GATE: Before this cycle, inspect the persistent state and "
            "search cache. Identify ONE uncertainty this cycle is intended to "
            "reduce. Check search-cache.md before launching literature searches. "
            "Reuse sufficient existing evidence; if the cache partially answers "
            "the question, search only the missing dimension. Prefer a small, "
            "discriminating investigation over broad confirmatory searching. "
            "Update state only when evidence changes the model, ranking, or queue."
        )
        if missing:
            context += " Missing state files: " + ", ".join(missing)
        print(json.dumps({"decision": "allow", "additional_context": context}))
        return

    if hook == "Stop":
        queue = STATE / "research-queue.md"
        if not queue.exists() or queue.stat().st_size < 80:
            print(json.dumps({
                "decision": "block",
                "reason": "No usable next-investigation queue. Record the highest-information next question before stopping."
            }))
        else:
            print(json.dumps({"decision": "allow"}))
        return

    print(json.dumps({"decision": "allow"}))


if __name__ == "__main__":
    main()
