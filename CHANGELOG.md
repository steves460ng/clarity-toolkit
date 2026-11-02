# Changelog

## Unreleased: Claude port

- Add `claude/`, a Claude port with four self-contained skills: `grill-me` (with `grilling` merged in), `to-questionnaire`, `wait-what`, and `handoff`. Templates are inlined and the ChatGPT-specific writing-block and invocation-policy rules are replaced with Claude delivery rules.
- `grill-me` also triggers on requests for help organizing thoughts through questions. `handoff` also covers continuing from a supplied handoff. `to-questionnaire` asks for a missing recipient and purpose in one message.
- Record 25 self-simulated scenarios in `tests/claude/self_simulations.md` (23 pass, 2 partial before the fixes above; the fixes were not re-simulated).
- The ChatGPT package in `clarity-toolkit/` is unchanged.

## 0.2.0

- Request native editable writing blocks for interview rounds, clarification questions, questionnaires, explanations, summaries, and handoffs.
- Use an honest single copyable-text fallback when the host lacks a supported native writing-block mechanism. No fabricated editor, clickable controls, or autosave claims.
- Explore with open questions before narrowing decisions. Remove mandatory recommendations phrased for automatic yes acceptance.
- Support optional multi-select examples, write-in alternatives, uncertainty, skipped questions, prose replies, and revisiting earlier answers.
- Preserve stable question IDs and unaffected content when users edit drafts. Keep accepted decisions separate from proposals and unknowns.
- Refresh all nineteen self-reviewed walkthroughs and bind them to the changed source hashes. Archive the old 0.1.1 evidence separately.
- Native UI rendering and automatic routing still require verification in the target host; recorded walkthroughs demonstrate the fallback text format only.
