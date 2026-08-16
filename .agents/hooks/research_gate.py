#!/usr/bin/env python3
"""Small, dependency-free research gate for Antigravity hooks.

The hook intentionally does not perform research. It enforces that the
research agent maintains a persistent state and cannot silently finish a
cycle without recording the next uncertainty to investigate.
"""
from __future__ import annotations

import json
import os
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
]


def main() -> None:
    event = json.load(sys.stdin)
    hook = event.get("hook_event_name", "unknown")
    prompt = event.get("prompt", "")

    missing = [str(p.relative_to(ROOT)) for p in REQUIRED if not p.exists()]
    warnings = []
    if missing:
        warnings.append("Initialize missing research state: " + ", ".join(missing))

    # Pre-invocation: inject a compact operational reminder.
    if hook == "PreInvocation":
        context = (
            "RESEARCH GATE: Before this cycle, read state/world-model.md, "
            "state/uncertainty-map.md, state/hypothesis-pool.md and "
            "state/research-queue.md. Identify ONE uncertainty this cycle is "
            "intended to reduce. Prefer a discriminating investigation over "
            "confirmatory searching. Persist meaningful updates."
        )
        if warnings:
            context += " " + " ".join(warnings)
        print(json.dumps({"decision": "allow", "additional_context": context}))
        return

    # Stop: only block when there is no persistent state at all. Do not create
    # an infinite autonomous loop; the scientific prompt owns continuation.
    if hook == "Stop":
        queue = STATE / "research-queue.md"
        if not queue.exists() or queue.stat().st_size < 80:
            print(json.dumps({
                "decision": "block",
                "reason": "Research state has no usable next-investigation queue. Record the highest-information next question before stopping."
            }))
        else:
            print(json.dumps({"decision": "allow"}))
        return

    print(json.dumps({"decision": "allow"}))


if __name__ == "__main__":
    main()
