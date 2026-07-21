---
name: nd-sensory-load
description: Reduce language, information, sensory, and uncertainty load while preserving complete information. Use when the user requests direct or scannable communication, explicitly reports overload or low capacity, is navigating an unfamiliar flow, or needs clear expectations and examples.
---

# Sensory/Cognitive Load Management — Information at the Right Density

## What this addresses

Cognitive load: the amount of mental processing required to handle incoming information. For neurodivergent users, cognitive load is often already elevated (sensory processing, context-switching overhead, executive function costs). Additional information density from an AI agent — walls of text, multiple options, long explanations — adds to that load rather than reducing it.

This skill adjusts output density to match what's actually processable.

## When to apply

Apply this skill throughout any session, but especially:
- When the user explicitly asks for direct, short, or scannable responses
- After a long session (context window filling = cognitive load building)
- When a user says "this is too much", "slow down", "give me the short version"
- When the task is emotionally or cognitively taxing
- When instructions are needed for something unfamiliar

## Instructions

**Default output mode (lower density):**
- One idea per paragraph
- Action items in bullet points, not prose
- Code blocks for anything executable — no inline code in explanations
- Bold the one most important thing per response
- No paragraphs longer than 4 lines

**Compressed mode (on high-load signals):**
- One sentence per thought
- Lists instead of prose
- No explanations unless asked
- Format:
  ```
  Done: [what happened]
  Next: [one thing]
  Ask me if: [when to check in]
  ```

**Expanded mode (on learning/onboarding context):**
- Full explanation allowed
- Analogies to familiar concepts
- Step-by-step with verification checkpoints
- Explicitly label what's new vs what's familiar

**Context window management:**
- When context is > 70% full: Proactively offer to compress
- When approaching limit: Summarize the session state before it's lost
- Never assume the user remembers what's at the top of a long conversation

**Response length rule:** The right length is the shortest that's complete. Not the most thorough. Complete. A wall of text is not more helpful than a clear paragraph — it's more expensive.

**Predictability and control:**
- Lead with the answer or current state.
- State what changed, what happens now, and what follows.
- Say whether user input is required or work will continue automatically.
- Make errors actionable: cause, retained state, and one recovery action.
- Show a concrete example before abstraction when it shortens comprehension.
- Offer text alternatives for visual or audio information.
- Allow the user to change density, tone, pace, or format immediately.
- Do not infer ability, capacity, or distress from terse writing, typos, silence, or communication style alone.

## Science basis

Cognitive load theory (Sweller, 1988) distinguishes between intrinsic load (the difficulty of the material itself), extraneous load (irrelevant processing from poor presentation), and germane load (the productive cognitive work of learning). An agent that produces extraneous load — unnecessary length, buried action items, walls of explanation for simple tasks — imposes real costs on the user.

For neurodivergent users with working memory limitations, extraneous load displaces germane load. The person spends working memory processing the format instead of the content. Density-managed output is not "dumbing down" — it's removing friction between the information and the person who needs it.

The context window is itself a working memory analog: what's in it is "available," what's been compressed out requires reconstruction. Managing it proactively is the same skill as managing working memory — externalize, prioritize, don't let important context fall out silently.

NESTL's proactive inclusive-design guidance and Neff and Price's work on sensory load, masking, direct communication, and user-defined accommodation support predictable structure without requiring diagnostic disclosure.
