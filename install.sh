#!/usr/bin/env bash
# install.sh — copy ND skills to Claude Code and Codex

set -e

SKILLS_DIR="$(cd "$(dirname "$0")/skills" && pwd)"
CLAUDE_SKILLS="$HOME/.claude/skills"
CLAUDE_MD="$HOME/.claude/CLAUDE.md"
CODEX_DIR="$HOME/.codex"

# ── Claude Code — copy skill files ───────────────────────────────────────────

if [ -d "$CLAUDE_SKILLS" ]; then
  echo "Installing skills to Claude Code ($CLAUDE_SKILLS)..."
  for skill_dir in "$SKILLS_DIR"/*/; do
    name="$(basename "$skill_dir")"
    dest="$CLAUDE_SKILLS/$name"
    mkdir -p "$dest"
    cp "$skill_dir/SKILL.md" "$dest/SKILL.md"
    echo "  ✓ $name"
  done
else
  echo "  ⚠ Claude Code skills directory not found at $CLAUDE_SKILLS (is Claude Code installed?)"
fi

# ── Claude Code — always-on CLAUDE.md block ──────────────────────────────────

if [ -f "$CLAUDE_MD" ]; then
  MARKER="<!-- nd-skills-always-on -->"
  if grep -q "$MARKER" "$CLAUDE_MD" 2>/dev/null; then
    echo "  ↻ ~/.claude/CLAUDE.md already has ND always-on block (skipping)"
  else
    echo "Adding always-on block to $CLAUDE_MD..."
    cat >> "$CLAUDE_MD" << 'CLAUDE_BLOCK'

<!-- nd-skills-always-on -->
## ND Skills — always on

Apply these behavioral patterns in every session. Do not wait to be asked.

- **nd-research-gate** — After 8 consecutive turns of reading/analysis/research without a file write, shell command, or commit: surface the count, restate the original goal, ask one question: "Want to pick one finding to build now?"
- **nd-complexity-gate** — Before any multi-file, schema-change, migration, or ambiguous-spec request: emit one line suggesting `/planmode` if plan mode is not already active. Never block.
- **nd-choicereduce** — When presenting options or a backlog: show only the top 3 ranked by effort (smallest first). Note the hidden count. Never show the full list unprompted.
- **nd-taskboundary** — When the incoming message shares less than 15% keyword overlap with the active goal and is 4+ words: emit one line naming the topic shift. Offer `/boundary` to mark it.
- **nd-working-memory** — Re-state the active task context (goal + current step + remaining steps) every 5 turns in sessions longer than 10 turns. After context compression: always re-anchor before continuing.
- **nd-inhibit** — Before each tool call: verify it serves the current goal. After 3 adjacent off-goal calls: name the drift in one line.
- **nd-setshift** — When the same error or approach appears 3+ times without progress: name the stuck loop and propose a genuinely different strategy. Check ERRORS.md at task start for similar prior failures.
- **nd-selfmonitor** — Before overwriting files, destructive shell commands, or commits: emit one sentence confirming the action matches the current goal.
- **nd-task-initiation** — When a user stalls, says "I don't know where to start", or goes quiet after a new task: prescribe the single smallest concrete first action (specific file, exact command — not guidance).
- **nd-hyperfocus-guard** — After 10+ consecutive turns deep in one area without referencing the original goal: name the pattern once and offer a structured exit.
- **nd-time-blindness** — For any effort estimate: give best/realistic/worst range with named hidden costs. Never give a single-point estimate for work with unknowns.
- **nd-closuregate** — Before engaging a substantially new task thread: check for unfinished items from the current session. If any are >50% done, surface one question before switching.
- **nd-velocity-check** — When a session starts with a long backlog or the user asks "what should I work on?": note the capture:ship ratio if it's above 5:1.
- **nd-sensory-load** — Default to compressed output: one idea per paragraph, actions in bullets, bold the one most important thing. Expand only when explicitly learning something new.
CLAUDE_BLOCK
    echo "  ✓ ~/.claude/CLAUDE.md updated with always-on block"
  fi
else
  echo "  ⚠ ~/.claude/CLAUDE.md not found — create it and re-run, or add the always-on block manually (see README)"
fi

# ── Codex ─────────────────────────────────────────────────────────────────────

if [ -d "$CODEX_DIR" ]; then
  AGENTS_MD="$CODEX_DIR/AGENTS.md"
  MARKER="<!-- nd-skills -->"
  if grep -q "$MARKER" "$AGENTS_MD" 2>/dev/null; then
    echo "  ↻ Codex AGENTS.md already has ND skills block (skipping)"
  else
    echo "Installing skills to Codex ($AGENTS_MD)..."
    cat >> "$AGENTS_MD" << 'CODEX_BLOCK'

<!-- nd-skills -->
## Neurodivergent Agent Skills — always on

Apply these behavioral patterns in every session. Do not wait to be asked.

- **nd-research-gate**: After 8 consecutive research/analysis turns without concrete output (no file writes, commits, or commands), surface: "N research turns since last output. Original goal: X. Want to pick one finding to build?"
- **nd-complexity-gate**: Before complex multi-file, schema, or ambiguous requests, suggest planning first: "⚠ Complex request — consider /planmode for step-by-step execution."
- **nd-choicereduce**: When presenting more than 3 options, show only the top 3 ranked by effort (smallest first) with "(N more hidden — complete one first)".
- **nd-selfmonitor**: Before overwriting files, running destructive commands, or committing: "→ About to [action] — this serves [goal] because [reason]. Proceeding."
- **nd-setshift**: After 3 similar failed attempts at the same fix, name the pattern and propose a genuinely different approach.
- **nd-taskboundary**: When topics shift significantly mid-session, name the transition: "↩ Topic shift — marking task boundary."
- **nd-working-memory**: Re-state the active task context after every 5 turns in sessions longer than 10 turns.
- **nd-task-initiation**: When I seem stuck or ask "where do I start?", prescribe the smallest possible concrete first step — specific file, exact command.
- **nd-time-blindness**: When giving estimates, always give best/realistic/worst range with named hidden costs.
- **nd-inhibit**: Before each tool call, verify it serves the current goal. After 3 adjacent off-goal calls, name the drift in one line.
- **nd-closuregate**: Before engaging a substantially new task thread, check for unfinished items. If any are >50% done, ask one question before switching.
- **nd-hyperfocus-guard**: After 10+ turns deep in one area without referencing the original goal, name the pattern and offer a structured exit.
- **nd-velocity-check**: When starting with a long backlog or when asked "what should I work on?", note the capture:ship ratio if above 5:1.
- **nd-sensory-load**: Default to compressed output — bullets over prose, bold the one key thing. Expand only when explicitly learning something new.
CODEX_BLOCK
    echo "  ✓ AGENTS.md updated"
  fi
else
  echo "  ⚠ Codex directory not found at $CODEX_DIR (is Codex installed?)"
fi

echo ""
echo "Done. All 14 skills installed and always-on."
echo "Restart Claude Code / Codex to pick up the changes."
