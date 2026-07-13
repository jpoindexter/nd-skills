---
name: nd-selfmonitor
description: Before destructive or hard-to-reverse operations, pause to verify the action matches the stated goal. A one-sentence pre-flight check, not a gate.
tags: [executive-function, neurodivergent, self-monitoring, safety]
---

# Self-Monitor — Pre-Action Intent Check

## What this addresses

Self-monitoring: the executive function that asks "is what I'm about to do actually what I meant to do?" This is a brief meta-cognitive step that normally happens automatically before consequential actions. In ADHD and high-focus states, it can be skipped — leading to "I don't know how I got here" moments where a command was run or a file was overwritten unexpectedly.

The self-monitor skill inserts a visible intent-check before high-consequence actions.

## When to apply

Apply before:
- Overwriting an existing file (write_file to a path that already exists)
- Running destructive shell commands (rm, drop, truncate, git reset --hard, force push)
- Database mutations (DELETE, DROP, UPDATE without WHERE)
- Committing code (verify the right files are staged, the message matches the work)
- Closing or deleting items from a tracked backlog

## Instructions

Before any of the above operations, emit a one-sentence pre-flight check:

```
→ About to [action] — this serves [current goal] because [reason]. Proceeding.
```

Examples:
- "→ About to overwrite auth.ts — this serves 'fix the login bug' because the session token logic needs replacing. Proceeding."
- "→ About to run `git reset --hard HEAD~2` — this serves 'undo the broken migration' because both commits are in the bad batch. Proceeding."

**If the reason feels unclear when writing it:** Do not proceed. Surface the uncertainty:
> "I was about to [action] but I'm not certain it serves [goal]. Want me to check before I run it?"

**The check is internal by default.** Show it only when:
- The action is irreversible (cannot be undone without effort)
- The user would reasonably want to know
- Something feels misaligned

## Science basis

Self-monitoring is the meta-cognitive component of executive function: evaluating one's own actions against intention in real time. It's distinct from planning (deciding what to do) and from task execution (doing it) — it's the bridge between them.

In ADHD research, impaired self-monitoring is associated with impulsive errors: correct intention, wrong execution. The intervention is an externalized check that makes the intent explicit at the moment of action — so a mismatch becomes visible before the action is taken.

The "proceeding" ending is intentional: the check should not add friction to correct actions. Only uncertain actions get a pause.
