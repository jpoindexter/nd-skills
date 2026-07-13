---
name: nd-setshift
description: When stuck on the same approach for 3+ iterations, detect the pattern and propose an alternative strategy. Read prior failure logs before attempting a complex fix.
tags: [executive-function, neurodivergent, cognitive-flexibility, debugging]
---

# Set Shifting — Break the Stuck Loop

## What this addresses

Cognitive flexibility (set shifting): the ability to abandon a failing approach and try something genuinely different. For people with ADHD or autism, perseveration — continuing the same strategy even when it's not working — is a common difficulty. In coding, this appears as trying the same fix slightly differently 5 times, or approaching the same problem from the same angle repeatedly.

This skill detects the "stuck loop" and proposes a strategy switch before it wastes more time.

## When to apply

Apply when:
- The same error has appeared 3+ times despite attempts to fix it
- Three or more similar tool calls (same function, similar args) have returned similar results
- The user has expressed frustration ("I've tried everything", "this keeps not working")
- A debugging session has lasted more than 20 tool calls without resolution

**Also apply at task start:** Before attempting a complex fix, check prior failure logs (ERRORS.md or similar) for similar problems.

## Instructions

**At task start for complex fixes:**
1. Check if there's an ERRORS.md, debug log, or prior session notes
2. Search for the error message or symptom
3. If found, summarize what was tried before and what failed:
   > "Found prior attempts at this: [summary]. Approaches that didn't work: [list]. Starting from a different angle."

**When detecting a stuck loop (3+ similar failed approaches):**
1. Name the pattern explicitly:
   > "We've tried [approach] in [N] different variations without success. That's the pattern; the approach may be wrong."

2. Propose a genuinely different strategy. "Different" means:
   - A different debugging tool or technique
   - Working from the other end (check the consumer instead of the producer, or vice versa)
   - A different hypothesis about the root cause
   - Asking whether the problem statement itself is correct
   - Reducing the problem to a simpler reproducer

3. State the new approach clearly before taking any action:
   > "Trying a completely different angle: [new approach] — reason: [why this is different from what we've been doing]."

4. If 3 more attempts with the new approach also fail, surface a second pivot:
   > "Two stuck loops. Consider: is the problem framing correct? What does a working version of this look like from outside?"

## Science basis

Perseveration — the tendency to persist with a cognitive set even when it's not producing results — is directly linked to set-shifting difficulty. The prefrontal cortex (PFC) normally suppresses the prior approach and activates a new one; in ADHD and some autism presentations, this PFC-mediated switching is slower or requires more effort.

External signaling — having the agent name the stuck loop — serves as the environmental substitute for the PFC's switching signal. This is why "I've tried everything" is a diagnostic statement: it signals perseveration, not actual exhaustion of approaches.

The check for prior failures before starting is a prospective memory aid: the brain has likely forgotten what was tried last time. The log is external storage for what internal memory would normally hold.
