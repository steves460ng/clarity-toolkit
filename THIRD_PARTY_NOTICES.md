# Third-party notices

This is an unofficial adaptation, not an official Matt Pocock product or endorsement.

Source: https://github.com/mattpocock/skills
Pinned commit: 59db609eb1e18aaf59b63284d0e52255aff0c63c
Original copyright: Copyright (c) 2026 Matt Pocock
License: MIT; the original permission and warranty notice is included in LICENSE.

Adapted skills: `grill-me` (with the upstream `grilling` procedure merged in), `to-question` (renamed from the upstream `to-questionnaire`), and `handoff`. Changes include tool-neutral delivery (interview rounds in the chat, editable documents where the session supports them, a Markdown fallback otherwise), open-ended interview rounds, a recipient-facing questionnaire template, a structured handoff template, a procedure for resuming from a supplied handoff, a built-in standalone check, and, in `grill-me`, a challenge round, a quick mode, and a path for stress-testing an existing plan.

No other upstream skills, hooks, scripts, or external service connections are included.

## korean-humanizer

This is an unofficial adaptation, not an official product or endorsement of the k-skill or im-not-ai projects.

Source: https://github.com/NomaDamas/k-skill (`korean-humanizer/instruction.md` and `korean-humanizer/references/ai-tell-taxonomy.md`)
Pinned commit: c41a11703b0ea25b8c5c3c62bd0f06f31997f7f8
Original copyright: Copyright (c) 2026 (the upstream LICENSE names no holder)
License: MIT

Method source: https://github.com/epoko77-ai/im-not-ai (Humanize KR)
Pinned commit: e9793d75a584169108906ee5f7332b27898efef4
Original copyright: Copyright (c) 2026 epoko77-ai
License: MIT

The upstream k-skill credits happy-nut (Hyungsun Song) for the first Korean humanizer skill and its 33-pattern catalog, and im-not-ai for the A–J taxonomy, S1/S2/S3 severity, the four rules, the 30%/50% change-rate guard, and the A–D grades. The English-language precedent is https://github.com/blader/humanizer.

Changes: the instructions were translated into English to match the other skills, with Korean patterns and examples kept as written; the pattern table was merged into the single `SKILL.md`; the upstream CLI stub (`npx @nomadamas/k-skill`) and references to other k-skill skills were removed; duplicated checklists were consolidated; and a note was added that examples never license adding facts.

