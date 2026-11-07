---
name: juniorize
description: Use when the user asks to juniorize, simplify for junior employees, or rewrite an existing answer or document so less-experienced staff can understand and use it without losing essential accuracy.
---

# Juniorize

Rewrite an existing expert-level answer, report, guide, or document for junior employees. Make it easier to understand and apply, not less accurate or condescending.

## When to use

Use when the user explicitly requests "juniorize," "주니어라이즈," a junior-friendly rewrite, or a comparable audience adaptation. The target is the immediately preceding answer or document when that reference is clear. For other targets, use the supplied text or accessible file. If the target cannot be identified or accessed, ask for it rather than inventing one.

Do not automatically juniorize every answer or document. Unlike `wait-what`, which repairs an explanation a user did not understand, this skill adapts content for a specified less-experienced workplace audience, including material the user has already understood.

## Workflow

1. Determine the source, its purpose, intended audience, and any stated constraints. Default to a junior employee with roughly one to three years of relevant experience when the user does not specify a level. Adapt to entry-level readers or more experienced practitioners when requested. Do not infer their intelligence or treat them as children.
2. Extract the core message, decisions, factual claims, numbers, limitations, dependencies, instructions, and citations that must survive the rewrite.
3. Lead with the main point, then arrange supporting explanations in a logical order. Break up dense sentences and unpack compressed reasoning. Supply essential background where the source assumes knowledge the audience may lack.
4. Replace unnecessary jargon with plain language. Retain technical terms needed for real work, define each at first meaningful use, and keep the term available for future reference. Expand acronyms when their meanings are established; do not guess ambiguous expansions.
5. Explain why important conclusions follow. Add a short, concrete workplace example when it genuinely helps. Clearly mark invented numerical examples as hypothetical; do not introduce them as source facts.
6. Make any required action, owner, sequence, or decision criterion clear when supported by the source. Do not invent assignments, deadlines, or requirements.
7. Preserve the source's factual meaning, figures, qualifications, uncertainty, risk warnings, and citations. Do not turn conditional advice into definitive instructions or silently remove necessary complexity.
8. Keep the original genre and intended use: a juniorized report should still be a usable report; a procedural guide should remain actionable; a summary should remain concise. Respect the user's requested length, structure, terminology, and output format.
9. Perform a final meaning-preservation check. Ensure every material decision and qualification remains, necessary terminology is explained, and the result reads naturally for an adult colleague.

## Style

Use clear, concise, professional language in the deliverable language requested by the user, otherwise match the source and conversation language as appropriate. Prefer connected explanations and selective examples over glossary dumps, repetitive headings, or inflated length. Avoid childish analogies, patronizing tone, excessive simplification, and substituting vague everyday words for precise terms when the distinction matters.

Do not add a comparison table, a teaching quiz, or a long preface unless requested. Present the rewritten artifact directly. When a native editable writing block is appropriate for a standalone draft or document, use it; otherwise follow the host's normal output conventions. If a file was requested and file generation is available, deliver the actual created file. Do not claim to have modified an external document unless the tool action succeeded.

## Quality gate

- Can the intended junior employee identify the main point and understand why it matters?
- Are unfamiliar but necessary terms explained on first use?
- Can the reader understand the next practical step when the source specifies one?
- Are original numbers, evidence, citations, uncertainty, and important exceptions intact?
- Is the result simpler without being inaccurate, patronizing, or unnecessarily longer?
