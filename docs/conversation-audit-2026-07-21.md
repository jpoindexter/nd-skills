# Claude + Codex Conversation Audit — 2026-07-21

## Scope

The audit streamed every locally stored JSONL session under `~/.claude/projects`, `~/.codex/sessions`, and `~/.codex/archived_sessions`:

- 3,278 session files
- 13,224,725,799 bytes scanned
- 90,248 assistant messages parsed
- 9,751 user-role messages parsed after injected instruction blocks were separated
- 1,568 Claude subagent files counted separately and excluded from user-feedback classification

The audit did not access server-only, deleted, unsynchronized, or non-JSONL conversations.

## Method

`scripts/audit_conversations.py` streams JSONL instead of loading archives into memory. It ignores tool results and hidden reasoning, removes common injected instruction messages, redacts paths, emails, URLs, UUIDs, and long tokens, and stores only aggregate counts plus short excerpts.

The signal counts are retrieval candidates, not automatic proof that an agent failed. Strong conclusions require a direct correction or a correction immediately following a matching assistant behavior. Generic “continue” messages are supporting evidence only.

## Confirmed failure clusters

### 1. Constraints were not retained across execution

- 128 correction messages matched high-precision constraint-loss language.
- Examples: “this should have been for the presnation not the microsite i said that multiple times” and “what file i told you not to deltee anything”.
- What the user wants: preserve the target, positive requirements, negative constraints, authority, and done evidence across every subtask and correction.

Changes:

- `nd-working-memory` now maintains an explicit constraint ledger.
- `nd-inhibit` checks the target and negative constraints, not only broad goal relevance.
- `nd-task-decomposition` reconciles every unit and constraint before a terminal claim.

### 2. Agents stopped at milestones instead of the terminal goal

- 9 messages explicitly said the agent stopped before the requested finish line.
- 232 generic continuation prompts support a broader persistence risk but are not all classified as failures.
- Example: “continue with all why do you stop on the goals”.
- What the user wants: progress updates should be checkpoints; safe authorized work should continue across subgoals until end-to-end evidence or a genuine blocker.

Changes:

- Added `nd-goal-persistence` with terminal-goal, authority, stop-condition, continuity, and evidence rules.
- Added its trigger to the executive-function router and both always-on templates.

### 3. Completion language exceeded the evidence

- 3 user corrections immediately followed a completion claim and said the behavior still failed.
- 9 broader premature-completion signals were retained as review candidates.
- What the user wants: run the actual user-visible path; distinguish executed evidence from traced code and assumptions.

Changes:

- `nd-goal-persistence` requires all-executed terminal evidence.
- `nd-task-decomposition` states that a completed unit, build, or lower-layer test proves only itself.

### 4. Agents asked questions the environment could answer

- 2 direct paired failures said: “look at the code dont ask me”.
- 16 broader autonomy/over-questioning messages were retained as candidates.
- What the user wants: inspect code, files, configuration, and saved task state before asking them to repeat information or reconfirm authorized work.

Changes:

- `nd-task-initiation`, `nd-working-memory`, `nd-inhibit`, and the router now prefer safe inspection and immediate action when the answer is discoverable.
- `nd-complexity-gate` no longer turns planning into a blocking question after autonomous execution was authorized.

## Preventive load reductions

Codex active sessions contained 6,115 visible self-monitor markers in 61,279 assistant messages. No direct user complaint was paired with these markers, so this is an inference rather than a confirmed failure. The rate was high enough to tighten `nd-selfmonitor`: routine reversible edits are now checked silently, and related consequential actions receive one batched visible check.

The research gate now distinguishes discovery commands from concrete output. A read-only file listing no longer resets the counter merely because a shell command ran.

## Regression coverage

`evals/behavior-regressions.json` contains six conversation-derived synthetic cases covering constraint retention, terminal persistence, inspect-before-questioning, self-monitor batching, research-output accounting, and proxy-test completion, plus a manual-router invocation case. `scripts/check_behavior_regressions.py` verifies that each case remains represented in the relevant skill instructions.

These static checks prove rule coverage, not future model compliance. Conversation-level forward evaluation is still needed to measure whether newly generated responses follow the rules reliably.
