# Changelog

## 0.5.0

- Add `critique-revise`: evidence-based critical review, material error correction, and a bounded regression check; explicit invocation only.
- Update ChatGPT package generation, six-skill inventory, manifest, English/Korean documentation, and source validation.
- Remove the separate alternative-client port, associated simulations, and documentation references.

## 0.4.0

- Add the original `meta-conv-filter` skill: remove revision traces and user-AI dialogue references, and resolve all dependencies on unseen conversation context in standalone deliverables.
- Apply standalone-output checks to the four existing ChatGPT workflows. Keep live interview navigation and requested history, substantive facts, provenance, uncertainty, and operational limits. Never fabricate missing context.
- Allow implicit invocation only for meta-conv-filter; preserve explicit-intent invocation for the four adapted workflows.

## 0.3.0

- Include requests to organize thoughts through questions in `grill-me`'s description, and ask prerequisite decisions before dependent choices.
- Preserve ChatGPT editable writing-block delivery, stable question IDs, answer revisions, early stopping, and the boundary between a summary and implementation authorization.
- Update source generation, exact inventory and invocation validation, migration documentation, regression tests, and the nineteen reviewed walkthroughs. The old 0.2.0 record is retained in history. Recorded walkthroughs are illustrative self-review, not fresh installed-host execution.

## 0.2.0

- Request native editable writing blocks for interview rounds, clarification questions, questionnaires, explanations, summaries, and handoffs.
- Use an honest single copyable-text fallback when the host lacks a supported native writing-block mechanism. No fabricated editor, clickable controls, or autosave claims.
- Explore with open questions before narrowing decisions. Remove mandatory recommendations phrased for automatic yes acceptance.
- Support optional multi-select examples, write-in alternatives, uncertainty, skipped questions, prose replies, and revisiting earlier answers.
- Preserve stable question IDs and unaffected content when users edit drafts. Keep accepted decisions separate from proposals and unknowns.
- Refresh all nineteen self-reviewed walkthroughs and bind them to the changed source hashes. Archive the old 0.1.1 evidence separately.
- Native UI rendering and automatic routing still require verification in the target host; recorded walkthroughs demonstrate the fallback text format only.
