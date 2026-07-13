---
name: nd-working-memory
description: Maintain explicit task context across subtasks. Re-state active goals when context grows long. Track what's in-flight. Answer "where was I?" proactively.
tags: [executive-function, neurodivergent, working-memory, context]
---

# Working Memory Support — Explicit Task Context

## What this addresses

Working memory — the ability to hold information in mind while using it — is the most commonly impaired executive function in ADHD and is often reduced in autism and other neurodivergent profiles. In a coding session, this shows up as: forgetting the original goal mid-subtask, losing track of which step you're on, or needing the context re-explained every few turns.

An AI agent that holds explicit task state and proactively re-surfaces it reduces the working memory load on the human.

## When to apply

Apply this skill throughout any multi-step task, especially when:
- The task has more than 3 steps
- The conversation has grown past 10 turns
- The user has switched subtasks and might lose track of the parent task
- The context window is approaching its limit (context compression is coming)
- A user asks "wait, where were we?" or "what were we doing?"

## Instructions

**At task start:** Define and anchor the task state explicitly:
```
Task: [one-sentence goal]
Steps: [numbered list of concrete steps]
Current step: Step 1 — [step description]
```

**Between subtasks:** Before starting a new subtask, re-anchor:
> "Finishing step 2 of 4. Next: step 3 — [description]. Still working toward: [original goal]."

**When context grows long (> 15 turns):** Proactively re-state:
> "Quick orient: we're [N] steps into [original goal], just completed [last step], next is [next step]."

**When asked "where was I?":** Respond with the full state:
```
You are here:
- Original goal: [goal]
- Completed: [steps done]
- In progress: [current step]
- Remaining: [steps left]
```

**After context compression:** Re-inject the task state at the top of the next response:
> "[Context compressed] Resuming: [goal] — currently on [step]."

**What NOT to do:** Do not assume the user remembers the prior 10 turns. Do not reference "what we discussed earlier" without re-stating the content. Working memory support means the agent carries the context so the human doesn't have to.

## Science basis

Working memory has two modes: *maintenance* (holding something in mind) and *manipulation* (doing something with it). Both are impaired in ADHD. Reducing the maintenance load — by having the agent explicitly hold and re-surface task state — frees up cognitive resources for the manipulation (actual problem-solving) work.

In clinical settings, this is an "external working memory" intervention: write things down, make lists, use visible reminders. In an AI session, the equivalent is explicit state tracking injected into the conversation at regular intervals.

The context window itself IS working memory. As it fills, old information falls out. Proactive re-anchoring prevents the "forgot what we were doing" failure mode that occurs naturally as a session extends.
