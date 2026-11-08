---
name: juniorize
description: Use when the user asks to juniorize or juniorise, reduce a text's complexity, or rewrite an existing answer or document in clear, accessible language while preserving meaning and making the result self-contained.
---

# Juniorize

Reduce the complexity of an existing answer, report, guide, or document so it is easy to understand and use. This is a general plain-language rewriting workflow across subjects and professions. Preserve accuracy, necessary detail, and a respectful tone.

## When to use

Use when the user explicitly requests "juniorize," "juniorise," "주니어라이즈," "주니어라이징," a simpler rewrite, or a comparable reduction in complexity. The target is the immediately preceding answer or document when that reference is clear. For other targets, use the supplied text or accessible file. If the target cannot be identified or accessed, ask for it rather than inventing one.

Do not automatically juniorize every answer or document. Unlike `wait-what`, which repairs an explanation a user did not understand, this skill rewrites existing content into an accessible standalone artifact, including material the user has already understood.

## Workflow

1. Determine the source, its purpose, intended audience, and any stated constraints. When no audience is specified, write for a general adult reader without assumed specialist background. Do not assume a job, seniority, or years of experience. Honor an explicitly specified audience without repeatedly labeling the reader.
2. Extract the core message, decisions, factual claims, numbers, limitations, dependencies, instructions, and citations that must survive the rewrite.
3. Lead with the main point, then arrange supporting explanations in a logical order. Break up dense sentences and unpack compressed reasoning. Supply essential background where the source assumes knowledge the audience may lack.
4. Replace unnecessary jargon with plain language. Retain technical terms needed for real work, define each at first meaningful use, and keep the term available for future reference. Expand acronyms when their meanings are established; do not guess ambiguous expansions.
5. Explain why important conclusions follow. Add a short, concrete example relevant to the subject when it genuinely helps. Clearly mark invented numerical examples as hypothetical; do not introduce them as source facts.
6. Make any required action, owner, sequence, or decision criterion clear when supported by the source. Do not invent assignments, deadlines, or requirements.
7. Preserve the source's factual meaning, figures, qualifications, uncertainty, risk warnings, and citations. Do not turn conditional advice into definitive instructions or silently remove necessary complexity.
8. Keep the original genre and intended use: a juniorized report should still be a usable report; a procedural guide should remain actionable; a summary should remain concise. Respect the user's requested length, structure, terminology, and output format.
9. Before delivering every rewrite, read and apply [meta-conv-filter](../meta-conv-filter/SKILL.md) as a required final pass. Resolve conversation-dependent references using accessible source and context, include the background needed to understand the content on its own, and remove revision traces, compliance prefaces, and production narration. Preserve substantive status, limitations, and any requested change history. If essential context is unavailable, ask a focused question or mark the specific gap; do not invent details or claim completeness. Apply the filter to added explanations and examples too.
10. Perform a final meaning-preservation and standalone-readability check. Ensure every material decision and qualification remains, necessary terminology is explained, and the result reads naturally for the intended reader without access to the conversation.

## Style

Use clear, concise, professional language in the deliverable language requested by the user, otherwise match the source and conversation language as appropriate. Prefer connected explanations and selective examples over glossary dumps, repetitive headings, or inflated length. Avoid childish analogies, patronizing tone, excessive simplification, and substituting vague everyday words for precise terms when the distinction matters.

Do not introduce or repeatedly emphasize audience labels such as "junior developer," "junior employee," "주니어 개발자," or "초보자" in headings, explanations, or conclusions merely because this workflow is named Juniorize. Keep those terms only where the source subject or an explicit user requirement makes them substantively necessary. Do not announce that the text has been simplified or filtered.

Do not add a comparison table, a teaching quiz, or a long preface unless requested. Present the rewritten artifact directly. When a native editable writing block is appropriate for a standalone draft or document, use it; otherwise follow the host's normal output conventions. If a file was requested and file generation is available, deliver the actual created file. Do not claim to have modified an external document unless the tool action succeeded.

## Quality gate

- Can the reader identify the main point and understand why it matters?
- Are unfamiliar but necessary terms explained on first use?
- Can the reader understand the next practical step when the source specifies one?
- Are original numbers, evidence, citations, uncertainty, and important exceptions intact?
- Does every reference resolve, with enough context to understand the result without the conversation?
- Has the required meta-conv-filter pass removed drafting traces while preserving substantive information?
- Are audience labels absent unless they are necessary to the subject or explicitly requested?
- Is the result simpler without being inaccurate, patronizing, or unnecessarily longer?
