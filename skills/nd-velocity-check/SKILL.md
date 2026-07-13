---
name: nd-velocity-check
description: Track and surface the ratio of ideas captured vs items shipped. Warn when the capture:ship ratio is high — the ideas-rich/finish-poor pattern made visible.
tags: [executive-function, neurodivergent, metacognition, productivity]
---

# Velocity Check — Making the Ideas:Shipped Ratio Visible

## What this addresses

A common neurodivergent productivity pattern: *ideas-rich, finish-poor*. A session generates 10 new feature ideas, 3 new research threads, and 2 refactoring proposals — and ships zero things. The backlog grows faster than the done list. The backlog *feels* like progress (it's full of good ideas!) while the actual delivery rate is low.

This is a fluency excess pattern: divergent thinking generates more than convergent thinking can close. Making the ratio visible is the first intervention.

## When to apply

Apply this skill:
- At the start of a new session, when reviewing what's been done recently
- When a user asks "what should I work on?" and there's a long backlog
- When a user proposes adding something new and already has uncompleted items
- As a periodic check-in when a session has been long

## Instructions

1. **Track captures and ships mentally** (or read them from a log if available):
   - A *capture* is: adding an item to the backlog, proposing a new feature, filing a ticket, writing a roadmap item
   - A *ship* is: merging code, deploying, completing a tracked task, marking something done

2. **Compute the 7-day ratio:**
   `captures in last 7 days : ships in last 7 days`

3. **Surface the ratio** as a dim, non-blocking note:
   > "📊 Last 7 days: [N] ideas captured, [M] shipped ([ratio]:1). [Warn/OK]"

4. **Warn when ratio > 5:1** (or when ships = 0 and there are captures):
   > "📊 Last 7 days: 12 captured, 2 shipped (6:1) — the backlog is growing faster than it's closing. Consider finishing before capturing."

5. **Do not block or moralize.** This is a visible metric, not a rule. The user may have a legitimate reason. Surface it once and move on.

6. **On 'finish before capturing':** Offer to show the top 3 backlog items (use nd-choicereduce skill).

## Science basis

Metacognition — the ability to observe and regulate one's own thinking — is often reduced in ADHD and related profiles. The capture:ship ratio makes a hidden pattern legible. Once visible, the user can act on it. Without visibility, the pattern continues invisibly.

The *fluency excess* pattern (high ideation, lower completion) is well-documented in ADHD research and is not a character flaw — it's a cognitive style that benefits from external metrics. "What gets measured gets managed."

The 5:1 threshold is approximate: a healthy ratio in product work is roughly 3:1 (three ideas for every shipped item). At 5:1 and above, the backlog is actively growing in a way that will generate future decision paralysis.
