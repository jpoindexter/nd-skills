# nd-skills

**ND Skills — 25 agent skills: 24 focused behaviors plus one manual router.**

[![Release](https://img.shields.io/github/v/release/jpoindexter/nd-skills)](https://github.com/jpoindexter/nd-skills/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Diagnosis-free neurodivergent-support behaviors for coding agents: executive-function routing, functional minimums, task decomposition, environmental scaffolding, emotion regulation, hyperfocus exits, task boundaries, working-memory support, realistic time estimates, and more.

Works with any agent that reads Markdown skills, including Claude Code and Codex.

## What's New

### v2.2.0

- Companion pack: `autism-layer` (literal reading, scripts, invitations), `biz-weekly-review` (coach-style week review), `nd-interrupt-budget` (silent by default, a nudge budget the person sets), `nd-inbox-digest` (at most three literal actions, read-only).
- Ambient signals section: what a host must supply for turn-count triggers, and the working-memory schema gap.

### v2.1.0

- Adds the manual `nd` router for one-command access to the full pack.

### v2.0.0

- Six new skills for routing, functional minimums, decomposition, goal persistence, environmental scaffolding, and emotion regulation.
- Conversation-derived fixes for constraint loss, premature stopping, false completion, and unnecessary clarification questions.
- Synchronized always-on instructions for Claude Code and Codex while preserving surrounding configuration.
- Redacted conversation-audit tooling and deterministic behavior-regression cases.

## Install

For invocable skills only:

```bash
npx skills add jpoindexter/nd-skills
```

For invocable skills **plus synchronized always-on behavior** in `~/.claude/CLAUDE.md` and `~/.codex/AGENTS.md`:

```bash
git clone https://github.com/jpoindexter/nd-skills.git
cd nd-skills
./install.sh
```

The installer updates its managed blocks on every run, preserves surrounding content, and copies complete skill folders including `agents/openai.yaml` metadata.

Restart Claude Code or Codex after installation so the refreshed skill inventory and always-on instructions are loaded.

## Always On and Manual Invocation

The installer makes the 24 focused behaviors always-on by synchronizing a managed block into Claude Code and Codex. The block is loaded at the start of new sessions and routes only from explicit task signals; it does not load every full skill body into every response.

Use the `nd` umbrella skill when you want to invoke the router yourself:

```text
Claude Code: /nd [task]
Codex:       $nd [task]
```

Claude Code resolves installed skills directly as slash commands. Current Codex versions use skill mentions or the skills picker; custom slash prompts were removed, so Codex does not support a literal custom `/nd`. Use `$nd` there.

You can also use `/nd status` or `$nd status` to show the active constraint ledger, and `off` to remove optional ND scaffolding for the current task.

## How It Works

- **Invocable layer:** every folder under `skills/` is a standalone agent skill with trigger metadata and focused instructions.
- **Always-on layer:** `install.sh` synchronizes a managed instruction block into Claude Code and Codex without replacing unrelated user configuration.
- **Behavior layer:** the router selects the smallest useful support, while constraint and goal state stay explicit across longer tasks.
- **Evaluation layer:** synthetic regression cases preserve the rules derived from real conversation failures without committing private conversation archives.

## The Skills

| Skill | Covers |
|---|---|
| [`nd`](skills/nd/SKILL.md) | Manually routes a task through the smallest relevant subset of the pack. Invoke as `/nd` in Claude Code or `$nd` in Codex. |
| [`nd-executive-function-router`](skills/nd-executive-function-router/SKILL.md) | Routes explicit task-state barriers to the least intrusive support. |
| [`nd-functional-minimums`](skills/nd-functional-minimums/SKILL.md) | Preserves safe, useful outcomes when capacity is low. |
| [`nd-task-decomposition`](skills/nd-task-decomposition/SKILL.md) | Converts oversized work into verifiable Now, Next, Later, Re-entry, and Done units with restart-safe authority refresh. |
| [`nd-goal-persistence`](skills/nd-goal-persistence/SKILL.md) | Carries terminal conditions across subtasks until end-to-end evidence or a genuine blocker. |
| [`nd-environment-scaffold`](skills/nd-environment-scaffold/SKILL.md) | Changes cues, defaults, tools, and support at the point of action. |
| [`nd-emotion-regulation`](skills/nd-emotion-regulation/SKILL.md) | Protects work and decision quality during explicit emotional intensity. |
| [`nd-choicereduce`](skills/nd-choicereduce/SKILL.md) | Shows only the top three options when a larger choice set would add load. |
| [`nd-closuregate`](skills/nd-closuregate/SKILL.md) | Surfaces nearly finished work before a substantially new task begins. |
| [`nd-complexity-gate`](skills/nd-complexity-gate/SKILL.md) | Suggests structured planning before complex or ambiguous execution. |
| [`nd-hyperfocus-guard`](skills/nd-hyperfocus-guard/SKILL.md) | Detects deep rabbit holes and offers a route back to the original goal. |
| [`nd-inhibit`](skills/nd-inhibit/SKILL.md) | Checks significant actions against the active goal and names repeated drift. |
| [`nd-research-gate`](skills/nd-research-gate/SKILL.md) | Interrupts research spirals that produce no concrete output. |
| [`nd-selfmonitor`](skills/nd-selfmonitor/SKILL.md) | Adds a visible intent check before destructive or hard-to-reverse actions. |
| [`nd-sensory-load`](skills/nd-sensory-load/SKILL.md) | Makes communication compressed, predictable, layered, and controllable. |
| [`nd-setshift`](skills/nd-setshift/SKILL.md) | Detects repeated failed approaches and forces a genuinely different strategy. |
| [`nd-task-initiation`](skills/nd-task-initiation/SKILL.md) | Prescribes a concrete first action and a truthful activation bridge when needed. |
| [`nd-taskboundary`](skills/nd-taskboundary/SKILL.md) | Saves restartable state and marks clean context transitions. |
| [`nd-time-blindness`](skills/nd-time-blindness/SKILL.md) | Externalizes ranges, hidden costs, checkpoints, and stopping rules. |
| [`nd-velocity-check`](skills/nd-velocity-check/SKILL.md) | Makes the ideas-captured to items-shipped ratio visible. |
| [`nd-working-memory`](skills/nd-working-memory/SKILL.md) | Re-anchors active context and persists one durable working surface. |
| [`autism-layer`](skills/autism-layer/SKILL.md) | Reads messages literally in four labelled lines, drafts scripts in the person's voice, phrases every suggestion as an invitation, protects special interests, names masking plainly. |
| [`biz-weekly-review`](skills/biz-weekly-review/SKILL.md) | Sorts the week into motion vs action, picks one front, gives at most three commitments and one hard recommendation. |
| [`nd-interrupt-budget`](skills/nd-interrupt-budget/SKILL.md) | Silent by default; unprompted nudges spend a daily budget the person set, one sentence each with a Not now, never during quiet mode. |
| [`nd-inbox-digest`](skills/nd-inbox-digest/SKILL.md) | Turns an inbox into at most three literal one-line actions, read-only, never sends, lists what the model saw. |

## Ambient signals

Several skills fire on counts: `nd-research-gate` after 8 research turns, `nd-hyperfocus-guard` after 10 turns in one area, `nd-working-memory` every 5 turns. A turn count is the only signal a chat agent has, and it is a weak proxy for what those skills are about (time lost, attention gone elsewhere). A host that supplies three ambient signals can fire them on the real thing:

- **idle time** — seconds since the last keyboard or mouse input
- **front app** — which application is in front, by name or bundle id, not its window title or URL
- **clock** — local time, so a rule can say "20 minutes" instead of "8 turns"

Example: Heel, a macOS companion, reads the front app and idle seconds every 5 s with no permission prompt, keeps per-app seconds for the day only, never sends them to the model, and turns them into one-sentence nudges inside `nd-interrupt-budget`. A host without these signals keeps the turn-count triggers as they are.

**Gap:** `nd-working-memory` names one durable working surface but this repo gives it no schema. Proposed shape, one record per task: `outcome`, `target`, `must`, `must_not`, `authority`, `done_evidence`. Not added here; a host that persists it should say where.

## Source Basis

The pack synthesizes and paraphrases task-support concepts from:

- Peg Dawson and Richard Guare, the *Smart but Scattered* series
- Judith Kolberg and Kathleen Nadeau, *ADD-Friendly Ways to Organize Your Life*
- KC Davis, *How to Keep House While Drowning*
- Tamara Rosier, *Your Brain's Not Broken Workbook*
- Megan Anna Neff, *Self-Care for Autistic People*
- Devon Price, *Unmasking Autism*
- University of Oxford, *NESTL Toolkit*

No source text, diagnostic assessment, or personal profile is bundled. The skills modify tasks, environments, and agent behavior; they are not medical advice.

## Validation

Run the deterministic behavior checks:

```bash
python3 scripts/check_behavior_regressions.py
bash -n install.sh
```

The sanitized findings and limitations are documented in the [Claude + Codex conversation audit](docs/conversation-audit-2026-07-21.md).

## License

MIT — see [LICENSE](LICENSE).
