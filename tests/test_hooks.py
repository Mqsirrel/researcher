#!/usr/bin/env python3
"""Unit tests for Antigravity research gate lifecycle hook."""
import json
import subprocess
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
HOOK_SCRIPT = REPO_ROOT / ".agents" / "hooks" / "research_gate.py"
QUEUE_FILE = REPO_ROOT / "state" / "research-queue.md"


class TestResearchGate(unittest.TestCase):
    def setUp(self):
        self.original_queue = QUEUE_FILE.read_text(encoding="utf-8") if QUEUE_FILE.exists() else None

    def tearDown(self):
        if self.original_queue is not None:
            QUEUE_FILE.write_text(self.original_queue, encoding="utf-8")

    def run_hook(self, event_type: str, stdin_data: dict) -> dict:
        cmd = [sys.executable, str(HOOK_SCRIPT), "--event", event_type]
        proc = subprocess.run(
            cmd,
            input=json.dumps(stdin_data),
            text=True,
            capture_output=True,
            cwd=REPO_ROOT,
        )
        self.assertEqual(proc.returncode, 0, f"Hook failed with stderr: {proc.stderr}")
        return json.loads(proc.stdout)

    def test_pre_invocation_inject_steps(self):
        """PreInvocation must return injectSteps with an ephemeral message."""
        payload = {"invocationNum": 1}
        output = self.run_hook("PreInvocation", payload)
        self.assertIn("injectSteps", output)
        self.assertIsInstance(output["injectSteps"], list)
        self.assertTrue(len(output["injectSteps"]) > 0)
        self.assertIn("ephemeralMessage", output["injectSteps"][0])
        self.assertIn("RESEARCH GATE", output["injectSteps"][0]["ephemeralMessage"])

    def test_stop_hook_blocks_uninitialized_queue(self):
        """Stop must return decision: 'continue' when the research queue is uninitialized."""
        QUEUE_FILE.write_text(
            "# Research Queue\n\n## Highest-information next investigation\n\nNot initialized.\n",
            encoding="utf-8",
        )
        payload = {"terminationReason": "model_stop", "fullyIdle": True}
        output = self.run_hook("Stop", payload)
        self.assertEqual(output.get("decision"), "continue")
        self.assertIn("reason", output)

    def test_stop_hook_allows_populated_queue(self):
        """Stop must return decision: 'allow' when an active investigation is populated."""
        QUEUE_FILE.write_text(
            "# Research Queue\n\n"
            "## Highest-information next investigation\n\n"
            "Investigate whether oral TRPM8 / trigeminal cold sensing triggers locus coeruleus norepinephrine release in anemic hypoxia.\n\n"
            "## Candidate questions\n\n"
            "| ID | Question | Hypotheses distinguished | Expected information gain | Feasibility | Priority |\n"
            "|---|---|---|---:|---:|---:|\n"
            "| Q-001 | Does ice ingestion alter cerebral blood flow via TRPM8? | H-001 vs H-002 | 4/5 | 5/5 | High |\n",
            encoding="utf-8",
        )
        payload = {"terminationReason": "model_stop", "fullyIdle": True}
        output = self.run_hook("Stop", payload)
        self.assertEqual(output.get("decision"), "allow")


if __name__ == "__main__":
    unittest.main()
