#!/usr/bin/env python3
"""Dependency-free Antigravity research gate conforming to Antigravity Hook Spec.

Enforces research discipline without doing research itself:
1. Injects guidance during PreInvocation reminding the agent to use persistent state
   and search-cache, and flags any missing state files.
2. Gates the Stop lifecycle event to prevent the agent from finishing if
   state/research-queue.md has not been populated with a concrete next investigation.
"""
from __future__ import annotations

import argparse
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


def is_queue_uninitialized(content: str) -> bool:
    """Check if the research queue lacks an active, user-defined investigation."""
    stripped = content.strip()
    if not stripped or len(stripped) < 80:
        return True
    
    # Check if still purely in placeholder state
    lines = [line.strip() for line in stripped.splitlines() if line.strip()]
    has_custom_highest = False
    for line in lines:
        if line.startswith("## Highest-information next investigation"):
            continue
        if "Not initialized" not in line and not line.startswith("#") and not line.startswith("|") and not line.startswith("Do not select"):
            has_custom_highest = True
            break

    # If the candidate questions table or highest-information field only has placeholders
    if not has_custom_highest and "Not initialized" in stripped:
        return True

    return False


def main() -> None:
    parser = argparse.ArgumentParser(description="Antigravity research gate hook")
    parser.add_argument("--event", choices=["PreInvocation", "PostInvocation", "PreToolUse", "PostToolUse", "Stop"], default=None)
    args, _ = parser.parse_known_args()

    try:
        payload = json.load(sys.stdin) if not sys.stdin.isatty() else {}
    except Exception:
        payload = {}

    hook = args.event
    if not hook:
        if "invocationNum" in payload:
            hook = "PreInvocation"
        elif "terminationReason" in payload:
            hook = "Stop"
        else:
            hook = "unknown"

    missing = [str(p.relative_to(ROOT)) for p in REQUIRED if not p.exists()]

    if hook == "PreInvocation":
        message = (
            "RESEARCH GATE: Before this cycle, inspect persistent state in state/ and "
            "search-cache.md. Identify ONE specific uncertainty this cycle is intended to "
            "reduce. Check search-cache.md before launching literature searches. "
            "Reuse existing evidence; if the cache partially answers the question, search "
            "only the missing dimension. Prefer a small, discriminating investigation over "
            "broad confirmatory searching. Update state only when evidence changes the model, "
            "ranking, or queue."
        )
        if missing:
            message += " [WARNING] Missing state files: " + ", ".join(missing)

        print(json.dumps({
            "injectSteps": [
                {"ephemeralMessage": message}
            ]
        }))
        return

    if hook == "Stop":
        queue = STATE / "research-queue.md"
        if not queue.exists():
            print(json.dumps({
                "decision": "continue",
                "reason": "RESEARCH GATE: state/research-queue.md is missing. Create and populate the research queue before stopping."
            }))
            return

        content = queue.read_text(encoding="utf-8")
        if is_queue_uninitialized(content):
            print(json.dumps({
                "decision": "continue",
                "reason": "RESEARCH GATE: No usable next-investigation queue. Record the highest-information next question in state/research-queue.md before stopping."
            }))
            return

        print(json.dumps({"decision": "allow"}))
        return

    print(json.dumps({}))


if __name__ == "__main__":
    main()
