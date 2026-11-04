# Changelog

## Unreleased: Claude port 0.4.0

- Port `meta-conv-filter` to `claude/skills/`, with Claude delivery rules (edit an existing Docs artifact when asked, otherwise a new editable document or one Markdown block) and a description that names the triggering requests.
- Add a standalone check to the four existing Claude skills, worded per skill: `grill-me` final summaries, `to-questionnaire` and `handoff` deliverables, and `wait-what` versions the user asks to share. Live interview rounds keep question IDs and revision notes.
- Update install requests in `README.md`, `README.ko.md`, and `claude/README.md` to five skills. The 0.4.0 Claude changes have not been self-simulated.

## 0.4.0

- Add the original `meta-conv-filter` skill: remove revision traces and user-AI dialogue references, and resolve all dependencies on unseen conversation context in standalone deliverables.
- Apply standalone-output checks to the four existing ChatGPT workflows. Keep live interview navigation and requested history, substantive facts, provenance, uncertainty, and operational limits. Never fabricate missing context.
- Allow implicit invocation only for meta-conv-filter; preserve explicit-intent invocation for the four adapted workflows.
- Update generation, package metadata, documentation, regression tests, and reviewed examples. The Claude port remains unchanged.

## 0.3.0

- Merge the former `grilling` interview procedure into `grill-me`, following the Claude port's self-contained interview structure. Remove the separate skill and its metadata; four explicit-intent workflows remain.
- Include requests to organize thoughts through questions in `grill-me`'s description, and ask prerequisite decisions before dependent choices.
- Preserve ChatGPT editable writing-block delivery, stable question IDs, answer revisions, early stopping, and the boundary between a summary and implementation authorization.
- Update source generation, exact inventory and invocation validation, migration documentation, regression tests, and the nineteen reviewed walkthroughs. The old 0.2.0 record is retained in history. Recorded walkthroughs are illustrative self-review, not fresh installed-host execution.

## Unreleased: Claude port

- Add `claude/`, a Claude port with four self-contained skills: `grill-me` (with `grilling` merged in), `to-questionnaire`, `wait-what`, and `handoff`. Templates are inlined and the ChatGPT-specific writing-block and invocation-policy rules are replaced with Claude delivery rules.
- `grill-me` also triggers on requests for help organizing thoughts through questions. `handoff` also covers continuing from a supplied handoff. `to-questionnaire` asks for a missing recipient and purpose in one message.
- Record 25 self-simulated scenarios in `tests/claude/self_simulations.md` (23 pass, 2 partial before the fixes above; the fixes were not re-simulated).
- Add copy-paste install requests for the Claude app and Claude Code to `README.md`, `README.ko.md`, and `claude/README.md`.
- The ChatGPT package in `clarity-toolkit/` is unchanged.

## 0.2.0

- Request native editable writing blocks for interview rounds, clarification questions, questionnaires, explanations, summaries, and handoffs.
- Use an honest single copyable-text fallback when the host lacks a supported native writing-block mechanism. No fabricated editor, clickable controls, or autosave claims.
- Explore with open questions before narrowing decisions. Remove mandatory recommendations phrased for automatic yes acceptance.
- Support optional multi-select examples, write-in alternatives, uncertainty, skipped questions, prose replies, and revisiting earlier answers.
- Preserve stable question IDs and unaffected content when users edit drafts. Keep accepted decisions separate from proposals and unknowns.
- Refresh all nineteen self-reviewed walkthroughs and bind them to the changed source hashes. Archive the old 0.1.1 evidence separately.
- Native UI rendering and automatic routing still require verification in the target host; recorded walkthroughs demonstrate the fallback text format only.
