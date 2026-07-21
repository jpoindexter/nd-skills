---
name: nd-goal-persistence
description: Preserve an explicit terminal goal across subtasks and keep executing safe, authorized work until its end-to-end done condition is observed or a genuine blocker is reached. Use when the user says finish all, do not stop, continue until done, complete every item, or supplies a multi-item backlog whose intermediate milestones must not be mistaken for completion.
---

# Goal Persistence

Carry the finish line, not just the current step. A status update, passing lower-layer test, or completed subtask is not the terminal outcome.

## Procedure

1. Capture a compact goal contract before execution:

```text
Outcome: observable terminal result
Required: explicit inclusions and quality bars
Forbidden: do-not-change constraints
Authority: actions the user authorized
Done evidence: end-to-end path that must be executed
Remaining: unchecked units
```

2. Promote every user correction into Required or Forbidden immediately. Do not rely on remembering the correction from prose.

3. Work through Remaining continuously. Completing one unit advances the goal; it does not end the task. Continue into the next safe in-scope unit without asking for permission already granted.

4. Treat commentary and progress reports as checkpoints, not handoffs. Do not return control solely because a subgoal, plan phase, commit, or proxy test finished.

5. Stop only when one condition is true:
   - the stated Done evidence was executed and observed;
   - a required action needs new authority, missing user input, or unavailable external state;
   - safety or policy prevents continuation;
   - the user changes or cancels the goal.

6. A terminal condition increases persistence, not permission. Keep destructive actions, external writes, purchases, publishing, and scope expansion inside the authority actually granted.

7. Before claiming completion, reconcile every Required and Forbidden item, run the real end-to-end path, and classify evidence:
   - `executed`: directly observed behavior
   - `code-path`: traced but not run
   - `assumed`: not verified

Only an all-executed terminal condition earns a done claim. Report the verification gap first otherwise.

## Continuity

If the context, session, or external process must end before the goal does, persist:

```text
Outcome:
Required / Forbidden:
Last executed evidence:
Remaining:
Blocked by:
Exact re-entry action:
```

Resume from Remaining, not from a reconstructed plan. After three similar failed attempts, use `$nd-setshift` rather than retrying indefinitely.

## Guardrails

- Do not invent new deliverables to keep the loop alive.
- Do not conceal a blocker behind optimistic wording.
- Do not repeatedly ask whether to continue when the user already supplied a terminal condition.
- Do not call a lower-layer build, unit test, or code inspection proof of user-visible behavior.

## Source Basis

Apply Dawson and Guare's goal-directed persistence model as an external task scaffold: keep the target and payoff visible, divide long work into observable checkpoints, monitor progress, and adjust from feedback. Combine it with explicit evidence boundaries so persistence cannot turn proxy success into false completion.
