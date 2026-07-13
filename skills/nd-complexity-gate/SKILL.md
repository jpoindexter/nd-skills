---
name: nd-complexity-gate
description: Detect complex or multi-step requests and suggest structured planning before acting. Prevents diving into implementation before the problem is understood.
tags: [executive-function, neurodivergent, planning, organization]
---

# Complexity Gate — Plan Before You Act

## What this addresses

Planning and organization difficulty: for many neurodivergent developers, complex multi-part tasks can trigger one of two failure modes — *paralysis* (not knowing where to start) or *premature execution* (jumping to implementation before understanding the full scope, then having to restart).

Both are costly. The complexity gate catches requests that warrant a plan before any tool call.

## When to apply

Apply this skill when a user request contains two or more of the following signals:

**Scope signals:**
- Mentions multiple files, components, or services
- Uses words like "refactor", "redesign", "rewrite", "migrate", "overhaul"
- References schema changes, database migrations, or API changes
- Implies work across multiple abstraction layers (frontend + backend + database)

**Ambiguity signals:**
- Contains phrases like "somehow", "not sure how", "figure out", "any way to"
- The spec is described in outcomes ("make it work") rather than mechanics
- Multiple possible interpretations exist

**Compound-task signals:**
- Two or more "and then" / "and also" clauses
- Mentions phases, steps, or parts
- Requires coordinating work that could conflict

## Instructions

1. **Score the request.** Silently assess: how many complexity signals are present?

2. **At 2+ signals and plan mode not active:** Before any tool call, emit a one-line note:
   > "⚠ This looks complex ([N] signals). Consider planning the approach before executing — `/planmode` on, or I can outline steps first?"

3. **If the user says 'outline steps':** Produce a numbered execution plan with:
   - Each step as a single, concrete, verifiable action
   - Files or commands that will be touched
   - The acceptance criterion for each step
   - Then ask: "Does this plan look right, or should I adjust before starting?"

4. **Never block.** If the user says "just do it", proceed immediately. The suggestion is a cognitive scaffold, not a gate.

5. **When plan mode IS active:** Skip the suggestion — the user already chose structured execution.

## Science basis

Planning and organization are direct executive function components. For people with EF challenges, the blank-page problem is often most acute at the START of a complex task. A brief plan — even if modified — provides the scaffolding that makes initiation possible. The alternative (diving in without a plan) often leads to scope drift, rework, and the "I'll just start over" loop.

Environmental manipulation principle: structure the task environment so it's easier to start correctly than to restart.
