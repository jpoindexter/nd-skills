#!/usr/bin/env python3
"""Mine Claude and Codex JSONL archives for ND-skill failure signals.

The default report stores aggregate counts and short redacted excerpts only. It
never copies full messages, tool results, hidden reasoning, or file contents.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


USER_SIGNALS = {
    "direct_rejection": re.compile(r"^(?:no(?:pe)?[,.!;:]|wrong\b|that['’]?s wrong\b)", re.I),
    "premature_completion": re.compile(
        r"\b(?:not done|isn['’]?t done|still (?:broken|not working|doesn['’]?t work)|"
        r"you (?:didn['’]?t|haven['’]?t) (?:finish|do|implement|fix)|"
        r"(?:it|that) (?:didn['’]?t|doesn['’]?t) work|not actually (?:done|fixed|working))\b",
        re.I,
    ),
    "constraint_miss": re.compile(
        r"\b(?:i (?:said|asked|told you)|as i said|not what i (?:asked|meant|wanted)|"
        r"that['’]?s not what|you (?:ignored|forgot|missed)|wrong (?:file|folder|repo|task)|"
        r"don['’]?t change|do not change)\b",
        re.I,
    ),
    "over_questioning": re.compile(
        r"\b(?:just do it|just do|stop asking|don['’]?t ask|do not ask|no more questions|"
        r"use your (?:judg(?:e)?ment|best judgment)|you decide|proceed without asking)\b",
        re.I,
    ),
    "verbosity_overload": re.compile(
        r"\b(?:too (?:much|long) to read|wall of text|be shorter|"
        r"make (?:the response|your answer|it) shorter|"
        r"keep (?:the response|your answer|it) short|more concise|less detail|"
        r"too much (?:text|information|detail)|overwhelming to read|too verbose)\b",
        re.I,
    ),
    "lost_context": re.compile(
        r"\b(?:where were we|what were we doing|you forgot (?:the|my|our)|lost the (?:thread|context)|"
        r"original goal|go back to (?:the|my) (?:task|request|goal))\b",
        re.I,
    ),
    "research_without_output": re.compile(
        r"\b(?:stop researching|stop planning|enough research|"
        r"nothing (?:was|is|got) (?:made|built|changed)|"
        r"you haven['’]?t (?:made|built|changed|written))\b",
        re.I,
    ),
    "choice_overload": re.compile(
        r"\b(?:too many options|just pick one|choose for me|don['’]?t give me options|"
        r"stop giving me options)\b",
        re.I,
    ),
    "topic_boundary_miss": re.compile(
        r"\b(?:same task|same topic|this is related|not a (?:new|different) task|"
        r"don['’]?t (?:switch|change) (?:tasks|topics))\b",
        re.I,
    ),
    "emotion_misread": re.compile(
        r"\b(?:don['’]?t psychoanaly[sz]e me|stop psychoanaly[sz]ing|i['’]?m not (?:upset|angry|panicking)|"
        r"don['’]?t tell me to calm down|stop coaching me)\b",
        re.I,
    ),
    "repeat_loop": re.compile(
        r"\b(?:you already tried|we already tried|same (?:error|problem|thing) again|"
        r"you['’]?re repeating|stop repeating|going in circles|stuck in a loop)\b",
        re.I,
    ),
    "continuation_reprompt": re.compile(
        r"^(?:please\s+)?(?:continue|keep going|go on|finish it|don['’]?t stop|do not stop)\b",
        re.I,
    ),
    "stopped_before_goal": re.compile(
        r"\b(?:why do you stop|you keep stopping|stop stopping|don['’]?t stop until|"
        r"do not stop until|continue until (?:everything|it is|it['’]?s|done|finished)|"
        r"finish everything|keep going until (?:everything|done|finished))\b",
        re.I,
    ),
    "estimate_miss": re.compile(
        r"\b(?:took (?:way )?longer|estimate was wrong|you said it would take|"
        r"this isn['’]?t (?:quick|small)|not a quick fix)\b",
        re.I,
    ),
}

ASSISTANT_MARKERS = {
    "completion_claim": re.compile(
        r"\b(?:done|completed|fixed|fully working|all set|implemented successfully|finished)\b",
        re.I,
    ),
    "planning_prompt": re.compile(r"(?:/planmode|consider planning|outline (?:the )?steps|plan first)", re.I),
    "topic_shift_marker": re.compile(r"(?:topic shift|task boundary|marking the boundary)", re.I),
    "clarification_question": re.compile(r"\?\s*$", re.S),
    "selfmonitor_marker": re.compile(r"→\s*About to", re.I),
    "skill_sweep_marker": re.compile(r"Skills matched \(\d+\):", re.I),
}

PAIR_SIGNALS = {
    "direct_rejection_after_assistant": ("direct_rejection", "*"),
    "false_done_after_completion_claim": ("premature_completion", "completion_claim"),
    "question_when_action_expected": ("over_questioning", "clarification_question"),
    "planning_instead_of_execution": ("over_questioning", "planning_prompt"),
    "false_topic_boundary": ("topic_boundary_miss", "topic_shift_marker"),
    "selfmonitor_overhead_complaint": ("verbosity_overload", "selfmonitor_marker"),
    "skill_sweep_overhead_complaint": ("verbosity_overload", "skill_sweep_marker"),
}

SYNTHETIC_USER_PREFIXES = (
    "<task-notification>",
    "<command-name>",
    "<command-message>",
    "<local-command-stdout>",
    "<local-command-caveat>",
    "<codex_internal_context",
    "This session is being continued from a previous conversation",
    "# Instructions (read first)",
    "<goal_context>",
    "<skill>",
    "<task>",
)

SENSITIVE_PATTERNS = (
    (re.compile(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}", re.I), "[EMAIL]"),
    (re.compile(r"/Users/[^\s'\"`]+"), "[PATH]"),
    (re.compile(r"\b[0-9a-f]{8}-[0-9a-f-]{27,}\b", re.I), "[UUID]"),
    (re.compile(r"https?://[^\s)\]>]+", re.I), "[URL]"),
    (re.compile(r"\b(?:sk|pk|ghp|xox[baprs])[-_][A-Za-z0-9_-]{16,}\b"), "[TOKEN]"),
    (re.compile(r"\b[A-Za-z0-9+/=_-]{48,}\b"), "[LONG_TOKEN]"),
)


@dataclass
class SignalBucket:
    count: int = 0
    platforms: Counter[str] = field(default_factory=Counter)
    examples: list[dict[str, Any]] = field(default_factory=list)

    def add(self, platform: str, example: dict[str, Any], limit: int) -> None:
        self.count += 1
        self.platforms[platform] += 1
        if len(self.examples) < limit:
            self.examples.append(example)


def redact(text: str, limit: int) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    for pattern, replacement in SENSITIVE_PATTERNS:
        text = pattern.sub(replacement, text)
    if len(text) > limit:
        return text[: limit - 1].rstrip() + "…"
    return text


def is_synthetic_user_message(text: str) -> bool:
    stripped = text.lstrip()
    return (
        "# AGENTS.md instructions" in text
        or "<INSTRUCTIONS>" in text
        or any(stripped.startswith(prefix) for prefix in SYNTHETIC_USER_PREFIXES)
    )


def content_text(content: Any) -> str:
    if isinstance(content, str):
        return content
    if not isinstance(content, list):
        return ""
    parts: list[str] = []
    for block in content:
        if not isinstance(block, dict):
            continue
        block_type = block.get("type")
        if block_type in {"text", "input_text", "output_text"}:
            value = block.get("text")
            if isinstance(value, str):
                parts.append(value)
    return "\n".join(parts)


def claude_message(obj: dict[str, Any]) -> tuple[str, str, str] | None:
    record_type = obj.get("type")
    if record_type not in {"user", "assistant"} or obj.get("isMeta"):
        return None
    message = obj.get("message")
    if not isinstance(message, dict):
        return None
    role = message.get("role")
    if role not in {"user", "assistant"}:
        return None
    text = content_text(message.get("content"))
    return role, text, str(obj.get("timestamp") or "")


def codex_message(obj: dict[str, Any]) -> tuple[str, str, str] | None:
    if obj.get("type") != "response_item":
        return None
    payload = obj.get("payload")
    if not isinstance(payload, dict) or payload.get("type") != "message":
        return None
    role = payload.get("role")
    if role not in {"user", "assistant"}:
        return None
    text = content_text(payload.get("content"))
    return role, text, str(obj.get("timestamp") or "")


def iter_files(root: Path, pattern: str) -> Iterable[Path]:
    if not root.exists():
        return ()
    return (path for path in root.glob(pattern) if path.is_file())


def source_id(path: Path) -> str:
    return hashlib.sha256(str(path).encode("utf-8")).hexdigest()[:12]


def audit_file(
    path: Path,
    platform: str,
    population: str,
    buckets: dict[str, SignalBucket],
    assistant_counts: Counter[str],
    stats: Counter[str],
    example_limit: int,
    snippet_limit: int,
) -> None:
    previous_assistant_markers: set[str] = set()
    previous_assistant_seen = False
    turn = 0
    parser = claude_message if platform.startswith("claude") else codex_message
    sid = source_id(path)

    try:
        handle = path.open("rb")
    except OSError:
        stats[f"{platform}.unreadable_files"] += 1
        return

    with handle:
        for raw_line in handle:
            stats[f"{platform}.bytes_scanned"] += len(raw_line)
            if platform.startswith("claude"):
                if b'"type":"user"' not in raw_line and b'"type":"assistant"' not in raw_line:
                    continue
            elif b'"type":"response_item"' not in raw_line or b'"message"' not in raw_line:
                continue
            try:
                obj = json.loads(raw_line)
            except (json.JSONDecodeError, UnicodeDecodeError):
                stats[f"{platform}.invalid_json_lines"] += 1
                continue
            parsed = parser(obj)
            if parsed is None:
                continue
            role, text, timestamp = parsed
            if not text.strip():
                continue
            turn += 1

            if role == "assistant":
                stats[f"{platform}.{population}.assistant_messages"] += 1
                previous_assistant_seen = True
                previous_assistant_markers = {
                    name for name, pattern in ASSISTANT_MARKERS.items() if pattern.search(text)
                }
                for name in previous_assistant_markers:
                    assistant_counts[f"{platform}.{population}.{name}"] += 1
                continue

            # Ignore injected instruction catalogs; they contain literal examples of
            # failure phrases but are not user feedback about the preceding answer.
            if is_synthetic_user_message(text):
                stats[f"{platform}.{population}.injected_instruction_messages"] += 1
                continue

            stats[f"{platform}.{population}.user_messages"] += 1

            # A sub-agent's user-role message is its assignment, not user feedback.
            # Keep it in population stats but never classify it as a complaint.
            if population == "subagent":
                previous_assistant_markers = set()
                previous_assistant_seen = False
                continue

            # User messages sometimes paste old transcripts, skill definitions, or
            # generated reports. Classify the leading request, not every embedded quote.
            candidate_text = text[:1500]
            matched_user_signals = {
                name for name, pattern in USER_SIGNALS.items() if pattern.search(candidate_text)
            }
            example = {
                "source": sid,
                "population": population,
                "turn": turn,
                "timestamp": timestamp,
                "quote": redact(text, snippet_limit),
            }
            for name in matched_user_signals:
                buckets[name].add(platform, example, example_limit)
            for pair_name, (user_name, assistant_name) in PAIR_SIGNALS.items():
                assistant_match = (
                    previous_assistant_seen
                    if assistant_name == "*"
                    else assistant_name in previous_assistant_markers
                )
                if user_name in matched_user_signals and assistant_match:
                    buckets[pair_name].add(platform, example, example_limit)
            previous_assistant_markers = set()
            previous_assistant_seen = False

    stats[f"{platform}.{population}.files"] += 1


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--claude-root", type=Path, default=Path.home() / ".claude")
    parser.add_argument("--codex-root", type=Path, default=Path.home() / ".codex")
    parser.add_argument("--include-subagents", action="store_true")
    parser.add_argument("--examples-per-signal", type=int, default=8)
    parser.add_argument("--snippet-chars", type=int, default=280)
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    buckets: dict[str, SignalBucket] = defaultdict(SignalBucket)
    assistant_counts: Counter[str] = Counter()
    stats: Counter[str] = Counter()

    claude_projects = args.claude_root / "projects"
    claude_files = list(iter_files(claude_projects, "**/*.jsonl"))
    for path in claude_files:
        is_subagent = "subagents" in path.parts
        if is_subagent and not args.include_subagents:
            continue
        population = "subagent" if is_subagent else "main"
        audit_file(
            path,
            "claude",
            population,
            buckets,
            assistant_counts,
            stats,
            args.examples_per_signal,
            args.snippet_chars,
        )

    codex_sources = (
        (args.codex_root / "sessions", "active"),
        (args.codex_root / "archived_sessions", "archived"),
    )
    for root, population in codex_sources:
        for path in iter_files(root, "**/*.jsonl"):
            audit_file(
                path,
                "codex",
                population,
                buckets,
                assistant_counts,
                stats,
                args.examples_per_signal,
                args.snippet_chars,
            )

    report = {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "privacy": "Aggregate counts and redacted excerpts only; no tool output or hidden reasoning.",
        "stats": dict(sorted(stats.items())),
        "assistant_markers": dict(sorted(assistant_counts.items())),
        "signals": {
            name: {
                "count": bucket.count,
                "platforms": dict(sorted(bucket.platforms.items())),
                "examples": bucket.examples,
            }
            for name, bucket in sorted(buckets.items(), key=lambda item: (-item[1].count, item[0]))
        },
    }
    serialized = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.write_text(serialized, encoding="utf-8")
    else:
        sys.stdout.write(serialized)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
