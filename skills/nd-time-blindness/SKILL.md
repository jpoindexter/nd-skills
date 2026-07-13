---
name: nd-time-blindness
description: Give honest, calibrated effort estimates with ND-aware adjustments. Never underestimate. Surface hidden costs. Name the planning fallacy by default.
tags: [executive-function, neurodivergent, time-blindness, estimation, adhd]
---

# Time Blindness — Honest Effort Estimates

## What this addresses

Time blindness: the reduced ability to intuitively sense how long things take. This is one of the most functionally impactful ADHD symptoms. In development work, it manifests as chronic underestimation ("this should take an hour" → 8 hours), missed deadlines, and the constant surprise that things took longer than expected.

An agent that gives honest, calibrated estimates with ND-aware adjustments significantly reduces the gap between planned and actual time.

## When to apply

Apply when:
- A user asks "how long will this take?" or "is this a quick fix?"
- You are proposing a plan with time estimates
- A user is deciding whether to start something before a deadline
- A scope estimate is needed for prioritization

## Instructions

1. **Never give only the "ideal" estimate.** Always give a range with explicit hidden costs:

   ```
   Time estimate:
   - Best case (no surprises, you stay focused): 1 hour
   - Realistic (typical session with distractions + one unexpected thing): 2-3 hours
   - Discovery overhead (if [unknown] turns out to be more complex): 4-6 hours
   
   Hidden costs I'm counting:
   - [Reading/understanding existing code]: ~30 min
   - [Testing and edge cases]: ~45 min
   - [Debugging the one thing that won't work as expected]: ~30 min
   ```

2. **Apply the 2.5× rule for ND-adjusted estimates.** For any task involving:
   - Code the user hasn't seen recently
   - A new tool, library, or pattern
   - Coordination with other systems
   
   Multiply the "best case" by 2.5 to get the realistic estimate.

3. **Surface the planning fallacy by name** when estimates seem optimistic:
   > "Quick note: 'this looks like 30 minutes' estimates almost always run longer when they involve [unfamiliar code / debugging / multiple files]. The realistic range is probably [N-M hours]."

4. **Never round down.** If you're uncertain, round up.

5. **Mark effort on the task, not just time:**
   - Low: familiar code, clear spec, isolated change
   - Medium: unfamiliar area, moderate dependencies, some unknowns
   - High: new architecture, cross-system coordination, significant unknowns
   
   Effort level predicts the chance of time overrun more reliably than initial time estimates.

## Science basis

Time blindness in ADHD is not a misconception about time — it's a failure of the *prospective* working memory system that normally allows people to sense the passage of time and anticipate how long tasks will take. The brain runs without a reliable internal clock.

The planning fallacy (Kahneman & Tversky, 1979) affects everyone — ADHD amplifies it. Reference class forecasting (comparing to similar past tasks) is the most reliable correction, which is why explicit range estimates with labeled hidden costs outperform single-point estimates.

The 2.5× rule is a rough empirical correction based on software project estimation research (Hofstadter's Law and variations). It's imprecise but systematically closer to reality than naive estimates for work with any unknowns.
