---
name: meta-conv-filter
description: Use when the user asks to remove meta-conversation or revision traces, make text understandable without the chat history, or prepare a standalone final deliverable from a conversation or draft.
---

# Meta Conversation Filter

Turn supplied text or a completed draft into a standalone deliverable for readers who have not seen the user-AI conversation. Meta-conversation includes every trace of revision, every reference to that dialogue, and all content whose meaning depends on seeing it.

## Procedure

1. Identify the requested artifact, audience, format, available source, and whether the user wants a clean result, an actual change log, or a transcript. Reuse visible context. If no target is available, ask for it; never pretend to have read a missing source. Do not start a requirements interview when the text is sufficient.
2. Mark revision traces ("improved", "updated version"), conversation references ("as discussed", "you requested"), compliance prefaces, and production narration. Resolve implicit pointers ("that approach", "option two", "the Q3 audience") and omissions ("same as before", "the rest is unchanged"). These are semantic cases, not prohibited words.
3. Rewrite the actual content with the latest explicit user decisions and unaffected facts intact. Remove drafting-history qualifiers and acknowledgments. Replace references with concrete supported names, constraints, or content. Incorporate necessary background from accessible material without copying the whole conversation or exposing private details. Do not embed the private back-and-forth in an artifact for another audience.
4. If essential context is missing, ask a focused clarification before finalizing. For a useful partial artifact, label the specific gap as unknown or not specified; do not silently delete the requirement, fabricate an antecedent, or claim unsupported completeness. Preserve unresolved conflicts as unresolved unless a later explicit user decision resolves them.
5. Do not add new claims or unsolicited recommendations while rewriting. Preserve facts, scope, numbers, dates, qualifications, uncertainty, citations, permissions, and evidence. A material failure or verification limit is substantive information. In a handoff, retain relevant provenance, actual work status, open questions, and next actions using self-contained descriptions. A proposal remains a proposal. A version identifier that identifies a real release remains meaningful.
6. When the requested subject is a change log, comparison, audit trail, transcript, or discussion history, retain the relevant changes or dialogue and supply the needed context. Do not remove valid domain terms such as an improved clinical outcome or a document titled Improvement Plan just because a word resembles a revision marker. Live interviews may keep question IDs and revision navigation; apply cleanup when producing their standalone summary.
7. Check the result as a first-time reader: every reference resolves, necessary context is present, and no sentence merely describes how the AI produced the answer. Use the user's language unless another deliverable language is requested, and follow the requested format. Return the artifact itself without an "I removed meta-conversation" preface, modification report, or unsolicited closing offer. Retain a necessary operational limitation outside an artifact only when it affects delivery or use; do not mix it into audience-facing copy.

## Examples

| Drafting-dependent text | Standalone result |
| --- | --- |
| Improved onboarding procedure | Onboarding procedure |
| As discussed, use option two. Context identifies option two as email sign-in. | Use email sign-in. |
| Q3's audience, with the same duration. Context confirms eight-year-olds and 20 minutes. | Audience: eight-year-olds. Duration: 20 minutes. |
| Your requested changes are reflected below. [Artifact] | [Artifact] |
| Keep the previous budget. The previous budget is unavailable. | Budget: not specified. |
| I have not tested it yet. The task is a handoff about an untested deployment. | Deployment verification: pending. |

This is a drafting workflow. Use accessible material only, protect secrets, and do not send messages, publish, save files, or claim work was done without the necessary tools and authorization. File output is optional when requested and supported. Do not claim that rewriting permanently edits an external document.
