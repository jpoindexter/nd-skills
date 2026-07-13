---
name: nd-taskboundary
description: Mark explicit cognitive task boundaries when topics shift. Archive the current task state and begin fresh without full context loss.
tags: [executive-function, neurodivergent, set-shifting, cognitive-flexibility]
---

# Task Boundary — Clean Cognitive Transitions

## What this addresses

*Cognitive set persistence* — a prior task's mental context bleeds into a new task. For many neurodivergent developers, switching tasks mid-session without an explicit transition leaves the old "cognitive set" (the assumptions, constraints, and vocabulary of the previous task) active. This contaminates the new task with irrelevant prior context.

Unlike ending the session or clearing history, a task boundary preserves what happened and explicitly marks where one cognitive set ends and another begins.

## When to apply

Apply this skill when:
- The user's new message is substantively about a different topic than the active goal
- The user explicitly says something like "switching gears", "new thing", "different task", or "while I'm thinking about it"
- The topic shift would benefit from a clean mental context (not a /clear — you want to keep the history)
- A long session has just resolved one task and is about to start another

## Signals of a topic shift (keyword-based heuristic)
- Less than 15% word overlap between the new request and the active goal statement
- New domain vocabulary that has not appeared in the last 5 turns
- A different software component, service, or codebase is suddenly the subject

## Instructions

1. **Detect the shift.** Before the agent processes the new request, notice the topic has changed.

2. **Name the transition** (one line only, before responding to the new request):
   > "↩ Topic shift — moving from [prior task summary] to [new task]. Marking the boundary."

3. **Insert the boundary marker** into the conversation context:
   ```
   [TASK BOUNDARY — new cognitive set begins here]
   Previous task: [one sentence summary]
   New task: [one sentence framing of the new request]
   ```

4. **Begin the new task clean.** Do not carry forward assumptions from the prior task unless explicitly told to. Treat the new task as if starting fresh — while still having access to the conversation history above the boundary.

5. **If uncertain:** Ask once:
   > "Are you switching tasks, or is this related to [current goal]?"

## Science basis

Set shifting (cognitive flexibility) is a core executive function that is commonly impaired in ADHD, autism, and other neurodivergent profiles. The difficulty is not with the new task itself but with *deactivating* the mental set from the old task.

Research on set-shifting impairment shows that an explicit environmental cue — a visible marker of transition — significantly reduces the interference from prior task context. The boundary acts as a cognitive anchor: "this is where that stopped and this started."

The boundary is NOT a /clear. The history is preserved. The marker is the signal that old context assumptions no longer apply.
