---
name: "session-review"
description: "Use when the user asks for an audit of the current session: how well their prompts and session management worked, with quoted evidence and concrete fixes. Triggers include /session-review, \"review this session\", or \"how were my prompts?\""
---

# Session Review

Audit the user's prompts and session management using only the current session as evidence. Deliver the review as a chat reply. Do not create files or documents, compare against earlier reviews, or keep a record of the review.

## Scope

- In scope: the user's messages in the current session and how the assistant's responses interacted with them.
- Out of scope: the message that requested this review (earlier ordinary instructions are still in scope), token usage, the quality of the work product itself, and general prompting lessons.
- If the user pastes a conversation from another session, say in one line that this skill reviews only the current session.
- If earlier parts of the session were compacted and the original text is gone, label that stretch "original unavailable, based on summary" and treat findings there with low confidence. Do not fabricate quotes from it.

## Evidence rules (important)

Users do not scroll back to find a message by its turn number. Never show turn numbers (T1, T2…) in the output; use them only for internal analysis.

- Always show evidence as the user's own words in a block quote (>). Trim long messages to the key sentence and mark cuts with "…". Do not reword or correct the quoted text.
- Add one line of context below each quote, for example "(answering the four open questions in the plan)" or "(right after the assistant delivered a draft)".
- When the evidence for an assistant fault is an assistant response, do not quote it at length; summarize what the assistant did in one line.

## Procedure

1. **Reconstruct the conversation:** list the user's messages in order and classify each as a new request, a revision, a confirmation or answer, or a change of direction.
2. **Find friction points:** rework, misunderstandings, clarifying questions from the assistant, signs of user frustration, repeated instructions, work that went against an instruction, and abandoned work.
3. **Assign a cause** to each friction point:
   - User: the goal, context, or constraints were missing, or the instruction was ambiguous.
   - Assistant: ignored an instruction, made a wrong assumption, or did too much or too little.
   - Both: each contributed.
   - Unavoidable: the task was exploratory, so iteration was natural.
4. **Choose the mode:** brief mode if there are no friction points, full mode if there is at least one. The number of messages is not the criterion.
5. **Rate each axis** using the rubric below.
6. **List findings** in order of severity.
7. **Rewrite** the one or two user prompts whose friction cost the most.
8. **Name three habits** to change in the next session, stated as concrete actions.

## Rubric

Rate each axis as Good, Fair, Poor, or Not assessable. Do not use numeric scores.

| Axis | Good signals | Poor signals |
|---|---|---|
| Goal clarity | States the deliverable and what counts as done | Open-ended requests ("clean this up a bit") |
| Context | Gives audience, constraints, and background | The assistant had to ask or guessed wrong |
| Revision instructions | Says what to change and why | "Not good", "again" |
| Session management | Stays on one topic; hands off at the right time | Unrelated topics mixed; context lost after a long session |
| Efficiency | Converges in few exchanges | The same revision repeats |
| Use of capabilities | Uses skills, documents, scheduled tasks, and similar features where they fit | Works around them manually |

Severity:
- **High:** the result was wrong, or major rework followed.
- **Medium:** caused unnecessary back-and-forth, or something was done contrary to an instruction.
- **Low:** inefficient, but the result was unaffected.
- **Low (latent):** no actual friction, but it would have caused a problem in a different situation. Report at most one per review.

## Tone (audit style)

- Be direct. No hedging, cushioning, or courtesy praise.
- Praise only behavior that has evidence and is worth repeating, in one line at most.
- Every finding needs a quote of the user's words as evidence. No unsupported generalities.
- Report assistant faults in their own section, held to the same standard. Do not shrink them by shifting blame to the user.
- If there is nothing wrong, say so. Do not pad the number of findings.

## Output format (full mode)

Keep tables to a minimum and use lists so the review reads well on narrow screens.

**Verdict:** a one-line judgment.

**Ratings by axis:** a list in the form "Axis: Rating — one-line reason". Leave Not assessable axes out of the list and note them in one line at the end, for example "Not assessable: Use of capabilities (no relevant situation)".

**Findings** (by severity), each as:

[Severity] Title
> Quote of the user's words
(one line of context)
- Impact: …
- Fix: …

**Assistant faults:** same format, with a one-line summary of the assistant's action as evidence. Write "None" if there are none.

**Rewritten prompt:**
> Original
> Rewrite
- Difference: one line.

**Three habits for the next session:** stated as actions, for example "State the deliverable format and length in the first request."

## Brief mode (no friction points)

Output only a one-line verdict, at most one latent risk (with a quote, only if there is one), and one habit for the next session. If there are no messages to review, say so and stop.

## Operating rules

- Write in the user's language unless they request another.
- Use only the visible conversation. Do not invent quotes, messages, or events.

---
Part of Clarity Toolkit (https://github.com/steves460ng/clarity-toolkit).
