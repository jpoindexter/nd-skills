---
name: nd-interrupt-budget
description: Govern every unprompted nudge, reminder, or check-in a host or agent sends to the person. Use when an agent, companion app, scheduler, or ambient sensor can speak without being asked: stay silent by default, spend a daily budget the person set, keep each nudge to one sentence with a Not now, and never repeat, never interrupt a declared quiet mode.
---

# Interrupt Budget — consent before attention

## What this addresses

Every unprompted message costs an ND person a context switch they did not choose. A helper that nudges whenever it has something to say becomes one more notification source to mute. This skill makes silence the default and treats the person's attention as a budget they own.

## Rules

1. **Silent by default.** The agent speaks when asked, when a time-box the person started ends, or when the person opens it. Anything else is a nudge and must pass the rules below.
2. **A daily budget.** At most 3 nudges per local day unless the person set another number. When the budget is spent, nothing else is sent until the next day; the thing waits where the person will see it when they come back.
3. **One sentence, with a Not now.** A nudge is one plain sentence naming the thing and at most two choices, one of which is always "Not now". No sound, no banner, no opening a window.
4. **Never twice about the same thing within 30 minutes.** A dismissed or snoozed nudge does not come back for 30 minutes, and the same reason is not raised more than once a day.
5. **Never during a declared quiet or off mode.** When the person has said quiet, off, focus, or do not disturb, no nudge is sent; the state keeps updating so nothing is lost.
6. **One-click Off.** Turning all nudges off is one action, always visible, never confirmed with a dialog. Turning them back on is the person's choice.
7. **The budget is the person's to set and never inferred.** Do not raise, lower, or "earn back" the budget from behaviour, mood, or history. Do not guess a good moment from activity signals; signals only say when not to speak.
8. **Nudges are templates, not model calls.** A nudge is a fixed sentence filled from state (task name, minutes), so it is predictable and costs nothing to send.

## Guardrails

- Do not count replies to the person's own questions as nudges; do not use that to smuggle nudges into replies.
- Do not stack: one nudge is pending at a time.
- Do not describe the budget as a limit on the person; it is a limit on the agent.

## Completion Check

The person can see how many nudges are left today, turn them off in one click, and nothing was sent while quiet mode was on.
