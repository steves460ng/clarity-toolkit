# Clarity Toolkit for Claude

A port of Clarity Toolkit to Claude skills. It contains the same five skills as the ChatGPT package in `../clarity-toolkit/`: four adapted workflows and the original `meta-conv-filter`.

| Skill | What it does | When it is used |
| --- | --- | --- |
| `grill-me` | Interviews you one or two questions at a time, prerequisite decisions first, and ends with a summary of decisions and open questions. | You ask to be interviewed, grilled, or helped to organize your thoughts on a plan through questions. |
| `to-questionnaire` | Drafts a questionnaire for someone else to answer, with context, priorities, and blank answer fields. It does not send it. | You ask for questions to send to an expert, vendor, customer, or colleague. |
| `wait-what` | Re-explains a confusing message: main point first, missing background, plain terms, caveats kept. | You say an explanation did not land and ask for it again. |
| `handoff` | Writes a handoff with goal, decisions, evidence, open questions, and next actions, with secrets redacted. Also continues from a pasted handoff, treating it as context to verify. | You ask for a handoff, or paste one and want to continue. |
| `meta-conv-filter` | Rewrites a draft so it stands on its own: removes revision traces and references to the chat, and replaces pointers like "option two" with the actual content. Missing context is marked not specified, never invented. | You ask to remove chat references or revision traces, or for a clean final version of a draft revised in the conversation. |

`grill-me` (final summary), `to-questionnaire`, `handoff`, and `wait-what` (when you ask for a version to share) apply the same standalone check before delivering.

## Install

Each `skills/<name>/SKILL.md` is a self-contained skill. Templates that the ChatGPT version kept in `references/` are inlined, so no other files are needed.

- **Claude app:** paste the request below into a conversation. Claude shows each skill as a card; choose Save to add it.

  > https://github.com/steves460ng/clarity-toolkit  
  > Add the five skills in this repository's `claude/skills/` folder (`grill-me`, `to-questionnaire`, `wait-what`, `handoff`, `meta-conv-filter`) to my account. Use each `SKILL.md` as written without rewriting it. If a skill with the same name already exists, compare it with the repository version and tell me what changed instead of creating a duplicate.

- **Claude Code:** copy the folders in `claude/skills/` into `~/.claude/skills/` (personal) or `.claude/skills/` (project), or paste this into a session:

  > https://github.com/steves460ng/clarity-toolkit  
  > Copy the five folders in this repository's `claude/skills/` into `~/.claude/skills/`. If a folder with the same name already exists, show me the differences and ask before overwriting it.

Claude decides from each skill's description whether to use it. To be sure a skill runs, name it, for example "Use grill-me to interview me about this plan."

## Differences from the ChatGPT package

| ChatGPT package | Claude port |
| --- | --- |
| Templates in `references/` | Templates inlined in each SKILL.md |
| "Native editable writing block", with a copyable text block as fallback | Interview rounds are written in the chat; questionnaires and handoffs become an editable Claude document when the session can create one, otherwise one copyable Markdown block |
| `agents/openai.yaml` sets implicit invocation per skill | No equivalent; when a skill is used is set by its `description` |
| One identical standalone-deliverables paragraph appended to every workflow | A shorter standalone check per skill, worded for what that skill delivers |
| Shared operating rules repeated in full in every skill | Each skill keeps only the rules it needs |
| Receiving a handoff covered by one line | `handoff` has a section for continuing from a supplied handoff |

## Testing

`../tests/claude/self_simulations.md` records 25 self-simulated scenarios: the 19 from `../tests/self_simulations.json`, adapted to Claude, plus 6 Claude-specific cases on triggering and delivery. The same model wrote and graded the responses, and triggering was predicted from the descriptions rather than measured in fresh sessions. Two partial results led to the fixes listed at the end of the record; the fixed versions have not been re-simulated. `meta-conv-filter` and the standalone checks have not been simulated for Claude.

## License and attribution

Unofficial adaptation of [Matt Pocock's skills](https://github.com/mattpocock/skills), MIT License. See [LICENSE](LICENSE) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
