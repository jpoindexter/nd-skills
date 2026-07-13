---
name: nd-closuregate
description: Before starting a new task thread, surface any tasks that are > 50% complete. Ask whether to close one first. One-tap dismiss. Never blocks.
tags: [executive-function, neurodivergent, task-switching, closure]
---

# Closure Gate — Finish Before You Start

## What this addresses

Task-switching and closure: many neurodivergent developers find it easy to start new things and hard to finish them. This is partly because starting is novel (dopamine) and finishing is often repetitive (cleanup, docs, edge cases). The result: a session full of half-finished tasks that each need context reload to resume.

The closure gate is a gentle check before starting a new major thread: "there are 2 things almost done — want to close one first?"

## When to apply

Apply when:
- A user is starting a new topic that is substantially different from what's currently in progress
- The user has mentioned working on something in the current session that appears unfinished (50-80% done)
- Multiple items appear to be "almost done" simultaneously

**Trigger signals:**
- A user says "let me start on [new thing]" after working on something else
- The conversation switches to a new component/file/task without prior work being visibly closed
- A `git status` or equivalent would show uncommitted changes from an unfinished subtask

## Instructions

1. **Check for open items.** Before engaging with the new task, review:
   - Are there uncommitted changes from the current session?
   - Were there test failures or incomplete steps from recent work?
   - Has anything been explicitly left "in progress" or "almost done"?

2. **If 1 or more items are > 50% complete:**
   Surface exactly one question:
   > "Quick check: [Item A] and [Item B] look close to done from this session. Want to close one before switching?"
   
   Offer exactly 3 options:
   - "Yes, close [most complete item] first"
   - "Skip — those can wait"
   - "Show me what's open"

3. **On 'skip':** Proceed immediately. No second question.

4. **On 'yes':** Return to the in-progress item. Provide a one-sentence re-orient:
   > "Back to [item]: [what was done], [what remains]. This should take [honest time estimate]."

5. **On 'show me what's open':** List the in-progress items with completion estimates.

## Science basis

Task completion is a dopamine-dependent reward. For people with ADHD, the dopamine signal at task completion is often weaker or delayed compared to the dopamine signal at task start. This asymmetry makes finishing feel less compelling than starting.

External accountability structures (making the open items visible, asking the explicit question) substitute for the missing internal completion signal. Research shows that visible progress and explicit closure moments meaningfully increase task completion rates in ADHD populations.

One-question format is deliberate: asking multiple questions about open items recreates the overwhelm they're designed to address. One specific item, one yes/no question.
