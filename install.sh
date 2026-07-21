#!/usr/bin/env bash
# install.sh — install ND skills and synchronize always-on agent instructions

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DIR="$SCRIPT_DIR/skills"
TEMPLATES_DIR="$SCRIPT_DIR/templates"
TARGET_HOME="${ND_SKILLS_TARGET_HOME:-$HOME}"
CLAUDE_ROOT="$TARGET_HOME/.claude"
CLAUDE_SKILLS="$CLAUDE_ROOT/skills"
CLAUDE_MD="$CLAUDE_ROOT/CLAUDE.md"
CODEX_ROOT="$TARGET_HOME/.codex"
CODEX_AGENTS="$CODEX_ROOT/AGENTS.md"

sync_managed_block() {
  local target_file="$1"
  local block_file="$2"
  local start_marker="$3"
  local end_marker="$4"
  local sync_tmp

  touch "$target_file"
  sync_tmp="$(mktemp "${TMPDIR:-/tmp}/nd-skills-sync.XXXXXX")"

  awk \
    -v block_path="$block_file" \
    -v start_marker="$start_marker" \
    -v end_marker="$end_marker" '
      function emit_block( line) {
        while ((getline line < block_path) > 0) print line
        close(block_path)
      }

      BEGIN {
        inside = 0
        inserted = 0
        legacy_tail = 0
      }

      $0 == start_marker {
        if (!inserted) {
          emit_block()
          inserted = 1
        }
        inside = 1
        next
      }

      inside && $0 == end_marker {
        inside = 0
        next
      }

      inside && $0 ~ /^<!--[[:space:]].*-->$/ {
        inside = 0
        print
        next
      }

      inside && $0 ~ /^- \*\*nd-sensory-load\*\*/ {
        legacy_tail = 1
        next
      }

      inside && legacy_tail && $0 !~ /^[[:space:]]*$/ {
        inside = 0
        legacy_tail = 0
        print
        next
      }

      inside { next }
      { print }

      END {
        if (!inserted) {
          if (NR > 0) print ""
          emit_block()
        }
      }
    ' "$target_file" > "$sync_tmp"

  mv "$sync_tmp" "$target_file"
}

install_skill_folders() {
  local destination_root="$1"
  local skill_dir
  local name
  local destination

  mkdir -p "$destination_root"
  for skill_dir in "$SKILLS_DIR"/*/; do
    name="$(basename "$skill_dir")"
    destination="$destination_root/$name"
    mkdir -p "$destination"
    cp -R "$skill_dir/." "$destination/"
    echo "  ✓ $name"
  done
}

if [ -d "$CLAUDE_ROOT" ]; then
  echo "Installing skills to Claude Code ($CLAUDE_SKILLS)..."
  install_skill_folders "$CLAUDE_SKILLS"
  sync_managed_block \
    "$CLAUDE_MD" \
    "$TEMPLATES_DIR/claude-always-on.md" \
    "<!-- nd-skills-always-on -->" \
    "<!-- /nd-skills-always-on -->"
  echo "  ✓ synchronized always-on block in $CLAUDE_MD"
else
  echo "  ⚠ Claude Code directory not found at $CLAUDE_ROOT"
fi

if [ -d "$CODEX_ROOT" ]; then
  echo "Installing skills to Codex ($CODEX_ROOT/skills)..."
  install_skill_folders "$CODEX_ROOT/skills"
  sync_managed_block \
    "$CODEX_AGENTS" \
    "$TEMPLATES_DIR/codex-always-on.md" \
    "<!-- nd-skills -->" \
    "<!-- /nd-skills -->"
  echo "  ✓ synchronized always-on block in $CODEX_AGENTS"
else
  echo "  ⚠ Codex directory not found at $CODEX_ROOT"
fi

echo ""
echo "Done. All 20 skills and their always-on behaviors are synchronized."
echo "Restart Claude Code / Codex to pick up the changes."
