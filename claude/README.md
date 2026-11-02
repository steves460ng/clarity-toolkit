# Clarity Toolkit for Claude

A port of Clarity Toolkit to Claude skills. It contains four skills; the ChatGPT package in `../clarity-toolkit/` is unchanged.

| Skill | What it does | When it is used |
| --- | --- | --- |
| `grill-me` | Interviews you one or two questions at a time, prerequisite decisions first, and ends with a summary of decisions and open questions. Includes the former `grilling` procedure. | You ask to be interviewed, grilled, or helped to organize your thoughts on a plan through questions. |
| `to-questionnaire` | Drafts a questionnaire for someone else to answer, with context, priorities, and blank answer fields. It does not send it. | You ask for questions to send to an expert, vendor, customer, or colleague. |
| `wait-what` | Re-explains a confusing message: main point first, missing background, plain terms, caveats kept. | You say an explanation did not land and ask for it again. |
| `handoff` | Writes a handoff with goal, decisions, evidence, open questions, and next actions, with secrets redacted. Also continues from a pasted handoff, treating it as context to verify. | You ask for a handoff, or paste one and want to continue. |

## Install

Each `skills/<name>/SKILL.md` is a self-contained skill. Templates that the ChatGPT version kept in `references/` are inlined, so no other files are needed.

- **Claude app:** give Claude this repository's URL and ask it to add the four skills in `claude/skills/` to your account. Claude shows each skill as a card; choose Save to add it.
- **Claude Code:** copy the folders in `claude/skills/` into `~/.claude/skills/` (personal) or `.claude/skills/` (project).

Claude decides from each skill's description whether to use it. To be sure a skill runs, name it, for example "Use grill-me to interview me about this plan."

## Differences from the ChatGPT package

| ChatGPT package | Claude port |
| --- | --- |
| Five skills; `grill-me` loads `../grilling/SKILL.md` | Four skills; `grilling` is merged into `grill-me` |
| Templates in `references/` | Templates inlined in each SKILL.md |
| "Native editable writing block", with a copyable text block as fallback | Interview rounds are written in the chat; questionnaires and handoffs become an editable Claude document when the session can create one, otherwise one copyable Markdown block |
| `agents/openai.yaml` sets implicit invocation per skill | No equivalent; when a skill is used is set by its `description` |
| "Do not rely on a tool named Skill" | Removed; Claude loads skills through its Skill tool |
| Shared operating rules repeated in full in every skill | Each skill keeps only the rules it needs |
| Receiving a handoff covered by one line | `handoff` has a section for continuing from a supplied handoff |

## Testing

`../tests/claude/self_simulations.md` records 25 self-simulated scenarios: the 19 from `../tests/self_simulations.json`, adapted to Claude, plus 6 Claude-specific cases on triggering and delivery. The same model wrote and graded the responses, and triggering was predicted from the descriptions rather than measured in fresh sessions. Two partial results led to the changes listed at the end of the record; those changes have not been re-simulated.

## License and attribution

Unofficial adaptation of [Matt Pocock's skills](https://github.com/mattpocock/skills), MIT License. See [LICENSE](LICENSE) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
