---
name: nd-research-gate
description: Interrupt research spirals after N turns without concrete output. Surface the pattern, name the original goal, and offer a one-question redirect to execution.
---

# Research Gate — Breaking the Exploration Spiral

## What this addresses

A well-documented executive function pattern: discovery and analysis feel rewarding, so the brain stays in exploration mode past the point of diminishing returns. Each new finding reinforces continuing. Without an explicit interrupt, a session can produce 10 turns of research and zero shipped artifacts.

This is *inhibitory control failure* — the inability to stop a rewarding behavior when a goal requires switching to a less immediately rewarding one (execution).

## When to apply

Apply this skill when you notice you have done 8 or more consecutive turns that are primarily:
- Reading files, documentation, or web content
- Analyzing, explaining, or summarizing existing work
- Researching approaches or comparing options
- Writing design documents without writing code

**Without** any turn that produced:
- A file written to disk
- A user-visible artifact
- A test or command run against the actual deliverable
- A commit or deployment

Reading, searching, listing files, browsing, and writing another analysis document do not reset the counter merely because a tool or shell command ran.

## Instructions

1. **Count and name the pattern.** Before the next research action, surface it explicitly:
   > "I've done [N] consecutive research turns since the last concrete output. The stated goal was: [original goal]."

2. **Offer the single redirect question.** Do not continue researching. Ask exactly:
   > "Want to pick one finding and build it now — or continue exploring? (I'll follow your call.)"

3. **On 'build it now':** If one finding is already the clear recommendation, implement it immediately. Ask the user to choose only when multiple materially different findings remain and the choice cannot be inferred from their stated goal.

4. **On 'keep exploring':** Reset the counter mentally and continue — but surface it again after another N turns.

5. **Counter:** Default threshold is 8 turns. This should feel like a check-in, not a gate. Never block.

## Science basis

Executive dysfunction research (Rabinovici et al., 2015; PMC4455841) identifies *inhibition failure* as a core EF deficit: difficulty stopping a cognitive pattern even when it no longer serves the goal. Treatment: environmental manipulation — make the pattern visible so the user can choose, rather than continuing automatically.

The one-question format is deliberate. Presenting multiple options (keep going, or build this, or build that, or pivot, or...) recreates the same choice paralysis the skill is designed to interrupt.
