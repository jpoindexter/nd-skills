---
name: nd-task-initiation
description: When a user faces a blank page, explicitly says they are stuck or avoiding a known task, or does not know where to start, create the smallest concrete first action and, when needed, add one truthful interest, novelty, challenge, feedback, or body-doubling bridge. Never invent urgency or use shame.
---

# Task Initiation — Breaking the Blank Page

## What this addresses

Task initiation difficulty: the paradox where knowing what needs to be done doesn't translate into starting to do it. This is one of the most common and least understood EF challenges. It's not laziness, fear, or disorganization — it's a mismatch between available activation energy and the perceived entry cost of the task.

The blank page is the worst starting condition. The smallest concrete first step is the best intervention.

## When to apply

Apply when:
- A user says "I don't know where to start" or "this feels overwhelming"
- A user describes a goal but hasn't taken any steps toward it
- A session starts without a clear first action
- A user returns to a project after time away and seems to need a re-entry point
- Silence + vague questions = likely initiation stall

## Instructions

1. **Identify the barrier.** Distinguish a technical unknown from cognitive load, emotional resistance, low feedback, or environmental friction. Do not diagnose the user.

2. **Do not ask "what do you want to do?"** This recreates the blank page. Instead, propose the first step.

When the user asked the agent to execute and the answer is discoverable from code, files, configuration, or safe inspection, take the first action yourself. Do not turn task initiation support into homework for the user or ask them to repeat information the environment already contains.

3. **Name the smallest possible concrete starting action:**
   > "Let's start here: [specific file/command/action]. This is the entry point. Everything else follows from this."

4. **Make the first step reversible and quick to verify:**
   - If it's a new feature: "Open [file] and add one comment describing what this should do."
   - If it's a bug: "Run [command] and paste the output."
   - If it's planning: "Name three things this needs to NOT do."
   - If it's creative work: "Write the first sentence / first function name / first test name."

5. **Provide the literal action, not guidance:**
   Not: "You should start with the data model."
   But: "Run this: `touch src/models/user.ts` — then open it and write one interface."

6. **Add at most one truthful activation bridge when reducing the step is not enough:**
   - interest: connect the step to a real user value or question
   - novelty: change the representation, tool, or order
   - challenge: add a bounded constraint or proof target
   - feedback: choose a step with a visible result
   - body doubling: use a live checklist or checkpoint

   Use urgency only when a real deadline already exists. Never invent consequences.

7. **After the first step is done:** Immediately anchor the next step before any other conversation:
   > "Step 1 done. Step 2 is: [specific action]. Ready when you are."

8. **For frozen sessions:** Suggest a tiny warmup:
> "Let's do a 5-minute version: just the smallest thing that counts as starting. What's one line of code, one test name, or one decision you can make right now?"

If the start remains blocked, reassess the task or environment with `$nd-environment-scaffold` instead of escalating pressure.

## Science basis

Task initiation difficulty in ADHD is associated with impaired dopamine signaling: the brain doesn't produce sufficient motivation activation for tasks that don't have immediate reward or urgency. The blank page has high activation cost and low immediate reward.

The "minimum viable start" technique works by reducing the activation cost to near-zero: the first action is so small that it doesn't trigger the avoidance response. Once in motion, continuation is significantly easier (the "body in motion" effect).

The key insight: the problem is not the task, it's the transition from non-doing to doing. External structure (a specific prescribed first action) bridges that transition in the same way as a countdown timer or a physical "ready? go." signal.

This procedure also incorporates Rosier's interest and emotional-intensity framing and Dawson and Guare's task-initiation interventions. Treat interest-based activation as a heuristic, not a diagnostic rule.
