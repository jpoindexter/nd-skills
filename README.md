# nd-skills

**ND Skills — 14 agent skills.**

Neurodivergent-support behaviors for coding agents — executive-function guards for ADHD, autism, and dyslexia: hyperfocus exits, task boundaries, working-memory re-anchoring, time-blindness estimates.

Works with any agent that reads markdown skills: Claude Code, Codex CLI, Gemini CLI, Copilot, Cursor.

## Install

```bash
npx skills add jpoindexter/nd-skills
```

Or manually: clone and symlink the folders under `skills/` into your agent's skills directory (e.g. `~/.claude/skills/`).

## The Skills

| Skill | Covers |
|---|---|
| [`nd-choicereduce`](skills/nd-choicereduce/SKILL.md) | When presenting options or a backlog, show only the top 3. Hidden items are noted but not shown until one choice is completed. |
| [`nd-closuregate`](skills/nd-closuregate/SKILL.md) | Before starting a new task thread, surface any tasks that are > 50% complete. Ask whether to close one first. One-tap dismiss. Never blocks. |
| [`nd-complexity-gate`](skills/nd-complexity-gate/SKILL.md) | Detect complex or multi-step requests and suggest structured planning before acting. Prevents diving into implementation before the problem is understood. |
| [`nd-hyperfocus-guard`](skills/nd-hyperfocus-guard/SKILL.md) | Detect and name hyperfocus sessions that have gone deep on a rabbit hole. Surface the original goal and offer a structured way back. |
| [`nd-inhibit`](skills/nd-inhibit/SKILL.md) | Before each significant action, check whether it serves the current goal. After 3 adjacent off-goal actions, name the drift explicitly. |
| [`nd-research-gate`](skills/nd-research-gate/SKILL.md) | Interrupt research spirals after N turns without concrete output. Surface the pattern, name the original goal, and offer a one-question redirect to execution. |
| [`nd-selfmonitor`](skills/nd-selfmonitor/SKILL.md) | Before destructive or hard-to-reverse operations, pause to verify the action matches the stated goal. A one-sentence pre-flight check, not a gate. |
| [`nd-sensory-load`](skills/nd-sensory-load/SKILL.md) | Manage information density and context window as cognitive load. Compress, chunk, and simplify output for sessions where cognitive load is already high. |
| [`nd-setshift`](skills/nd-setshift/SKILL.md) | When stuck on the same approach for 3+ iterations, detect the pattern and propose an alternative strategy. Read prior failure logs before attempting a comple… |
| [`nd-task-initiation`](skills/nd-task-initiation/SKILL.md) | When a user faces a blank page or says they don't know where to start, structure the first step explicitly. Break the initiation barrier with the smallest po… |
| [`nd-taskboundary`](skills/nd-taskboundary/SKILL.md) | Mark explicit cognitive task boundaries when topics shift. Archive the current task state and begin fresh without full context loss. |
| [`nd-time-blindness`](skills/nd-time-blindness/SKILL.md) | Give honest, calibrated effort estimates with ND-aware adjustments. Never underestimate. Surface hidden costs. Name the planning fallacy by default. |
| [`nd-velocity-check`](skills/nd-velocity-check/SKILL.md) | Track and surface the ratio of ideas captured vs items shipped. Warn when the capture:ship ratio is high — the ideas-rich/finish-poor pattern made visible. |
| [`nd-working-memory`](skills/nd-working-memory/SKILL.md) | Maintain explicit task context across subtasks. Re-state active goals when context grows long. Track what's in-flight. Answer "where was I?" proactively. |

## License

MIT — see [LICENSE](LICENSE).
