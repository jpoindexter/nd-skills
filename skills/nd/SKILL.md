---
name: nd
description: Manually route the current request through the installed neurodivergent-support skill pack. Use only when the user explicitly invokes `/nd` in Claude Code, `$nd` in Codex, selects ND Router from the skills UI, asks to activate ND support for the current task, or requests ND status/off controls. Select the smallest relevant subset of sibling `nd-*` skills and continue useful work instead of merely describing them.
---

# ND Router

Treat this skill as the manual front door to the pack. The always-on rules remain available; explicit invocation asks for visible routing and immediate application to the current task.

## Route

1. Use the arguments after the invocation as the task. If none were supplied, use the active task and its latest constraints.
2. Preserve a compact ledger: Outcome, Target, Must, Must not, Authority, Done evidence, and Now.
3. Select one primary sibling skill and at most two supporting skills. Read their `SKILL.md` files before applying them.
4. Prefer these routes:
   - unclear start or oversized work: `nd-task-initiation` or `nd-task-decomposition`
   - explicit finish-all condition: `nd-goal-persistence`
   - lost context or repeated corrections: `nd-working-memory` plus `nd-inhibit`
   - low capacity or overload: `nd-functional-minimums` or `nd-sensory-load`
   - explicit frustration or emotional intensity: `nd-emotion-regulation`
   - repeated task friction: `nd-environment-scaffold`
   - research spiral, drift, retry loop, or hyperfocus: the matching gate or guard skill
   - time, choice, transition, or closure friction: the matching focused skill
5. State the selected route in one line, expose the immediate action, and execute it. Do not return a catalog, assessment, or coaching questionnaire.

Use this compact shape when visible scaffolding helps:

```text
ND support: [selected skills]
Outcome: [terminal result]
Now: [one executable action]
Done when: [observable evidence]
```

## Controls

- `status`: show the current ledger, last verified evidence, blocker, and exact next action.
- `off`: stop adding optional ND scaffolds for the current task. Preserve safety, explicit constraints, and required agent instructions.
- Any other argument: treat it as the task and route it normally.

## Guardrails

- Do not infer a diagnosis, capacity, or emotional state from writing style, spelling, silence, or brevity.
- Do not load all sibling skills when one to three cover the immediate barrier.
- Do not let routing replace execution when a safe next action is clear.
- Do not broaden permissions or relax verification because the router was invoked.
