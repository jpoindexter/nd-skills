#!/usr/bin/env python3
"""Check that conversation-derived ND behavior rules remain represented."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASES_PATH = ROOT / "evals" / "behavior-regressions.json"


def main() -> int:
    payload = json.loads(CASES_PATH.read_text(encoding="utf-8"))
    failures: list[str] = []

    for case in payload["cases"]:
        corpus_parts: list[str] = []
        for skill in case["skills"]:
            skill_path = ROOT / "skills" / skill / "SKILL.md"
            if not skill_path.is_file():
                failures.append(f"{case['id']}: missing {skill_path.relative_to(ROOT)}")
                continue
            corpus_parts.append(skill_path.read_text(encoding="utf-8"))
        corpus = "\n".join(corpus_parts).casefold()
        for requirement in case["requirements"]:
            if requirement.casefold() not in corpus:
                failures.append(f"{case['id']}: missing rule phrase {requirement!r}")

    nd_metadata = ROOT / "skills" / "nd" / "agents" / "openai.yaml"
    if not nd_metadata.is_file():
        failures.append("manual-nd-router-executes: missing agents/openai.yaml")
    elif "allow_implicit_invocation: false" not in nd_metadata.read_text(encoding="utf-8"):
        failures.append("manual-nd-router-executes: router must remain explicit-only")

    if failures:
        print("Behavior regression check failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(f"Behavior regression check passed: {len(payload['cases'])} cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
