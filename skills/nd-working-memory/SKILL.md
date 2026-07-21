---
name: nd-working-memory
description: Maintain explicit task context across subtasks and persist it in one durable working surface when interruptions, multiple turns, or multiple agents could lose the thread. Re-state active goals when context grows long, track what is in flight, and provide an exact re-entry action.
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
Target: [repo, artifact, surface, or environment]
Must: [required inclusions]
Must not: [negative constraints]
Authority: [material actions already authorized]
Done evidence: [observable end-to-end check]
Steps: [numbered list of concrete steps]
Current step: Step 1 — [step description]
```

Treat Target, Must, Must not, Authority, and Done evidence as a constraint ledger. Promote user corrections into it immediately. Before each write, compare the intended target and effect against the ledger; do not let a recent subtask silently replace the parent deliverable.

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

**When interruption risk is material:** Persist the state in the project's existing task, handoff, roadmap, or notes system:

```text
Outcome:
Now:
Known:
Must / Must not:
Blocked by:
Next:
Later:
Done when:
Re-entry:
```

Use one working surface. Update the existing source of truth rather than maintaining a second contradictory plan. Prefer links, checkboxes, concrete file names, and verified facts over prose recap. Do not claim the memory is durable until the target file or store has been read back.

Store task state, not diagnoses, inferred traits, or unnecessary private biography. Fade the scaffold when it no longer reduces effort.

**What NOT to do:** Do not assume the user remembers the prior 10 turns. Do not reference "what we discussed earlier" without re-stating the content. Working memory support means the agent carries the context so the human doesn't have to.

Do not re-ask for a constraint that can be recovered from the active conversation, repository, task file, or saved ledger. Inspect those sources first. Ask only when the missing answer materially changes the result and cannot be discovered safely.

## Science basis

Working memory has two modes: *maintenance* (holding something in mind) and *manipulation* (doing something with it). Both are impaired in ADHD. Reducing the maintenance load — by having the agent explicitly hold and re-surface task state — frees up cognitive resources for the manipulation (actual problem-solving) work.

In clinical settings, this is an "external working memory" intervention: write things down, make lists, use visible reminders. In an AI session, the equivalent is explicit state tracking injected into the conversation at regular intervals.

The context window itself IS working memory. As it fills, old information falls out. Proactive re-anchoring prevents the "forgot what we were doing" failure mode that occurs naturally as a session extends.

Kolberg and Nadeau's externalizing systems, Dawson and Guare's working-memory interventions, and NESTL's predictable visible structures support moving state into the environment rather than relying on rehearsal.
