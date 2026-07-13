---
name: nd-inhibit
description: Before each significant action, check whether it serves the current goal. After 3 adjacent off-goal actions, name the drift explicitly.
tags: [executive-function, neurodivergent, inhibitory-control, scope]
---

# Inhibitory Control — Goal-Check Before Acting

## What this addresses

Inhibitory control: the executive function that stops you from acting on impulse when the action doesn't serve the current goal. In coding, this shows up as scope creep, yak-shaving, and "while I'm here I'll also fix..." patterns that expand a 1-hour task into a 3-day refactor.

The inhibitory control skill is a lightweight, non-blocking pre-action check: does this action serve the goal we stated at the start of this task?

## When to apply

Apply this skill during any task that has a defined goal. Run the check:
- Before each tool call that writes files, executes commands, or changes state
- Before starting a new subtask that wasn't in the original plan
- When noticing the scope of the current step is larger than originally described

**Do NOT apply to:** Read-only operations (reading files, searching), clearly pre-planned steps, or when the user has explicitly expanded scope.

## Instructions

1. **State the current goal** (from the start of the task):
   *"Active goal: [goal]"*

2. **Before a potentially off-goal action, ask silently:** Does [this specific action] directly serve [the current goal]?

3. **If yes:** proceed without comment.

4. **If uncertain:** Emit a one-line annotation before the action:
   > "→ [action] — this serves [goal] because [reason]"

5. **After 3 consecutive actions that seem tangentially related to the goal:** Name the drift:
   > "⚠ Drift check: the last 3 actions were [list]. The original goal was [goal]. Want to continue this direction, or return to the original path?"

6. **Never block.** The check is always a pause for awareness, not a gate. If the user confirms the drift is intentional, note it and continue.

## Science basis

Inhibitory control failure in ADHD often manifests as *off-task intrusions* — thoughts or impulses that pull attention away from the current task. In coding, the trigger is often seeing something that could be "improved while I'm here." The brain treats this as an opportunity (reward signal) rather than a distraction.

The 3-action threshold before naming drift is deliberate: 1 tangential action is normal problem-solving, 2 is still plausibly connected, 3 establishes a pattern that warrants naming. Naming the drift without blocking it gives the human the choice to re-engage the goal — which is the correct intervention, since sometimes the drift IS the right thing.
