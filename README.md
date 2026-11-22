# Clarity Toolkit

[한국어 README](README.ko.md)

Four conversation skills for AI assistants: clarify an idea through an interview, prepare questions for someone who holds the answers, turn a draft into standalone final text, and hand work over to the next person or session.

| Skill | Use it when |
| --- | --- |
| `grill-me` | You have an idea or plan but have not worked out the requirements. |
| `to-question` | An expert, vendor, customer, or colleague holds facts or decisions you need. |
| `meta-conv-filter` | A draft revised in a conversation must make sense to someone who never saw that conversation. |
| `handoff` | Work continues with another person, agent, or a new session, or you are resuming from a handoff. |

Each skill counters a common assistant habit: starting to build instead of interviewing, asking the user the recipient's questions instead of drafting a questionnaire for the recipient, leaving references such as "as discussed" in final text, and blurring proposed plans with completed work.

The skills are written in plain Markdown and do not depend on a particular model, app, or service. Where a skill can use a capability such as an editable document, it also says what to do when the capability is missing.

## Install

Each skill is a single, self-contained file at `skills/<name>/SKILL.md`, with a `name` and `description` header followed by instructions. No shared files, templates, or scripts are required.

- **Tools that load `SKILL.md` skills:** copy each `skills/<name>/` folder into the tool's skills directory, or add the skills through its settings. Check the tool's documentation for the location.
- **Tools without skill support:** paste the body of a `SKILL.md` into a custom instruction, system prompt, or project instruction, or attach it to a conversation and ask the assistant to follow it.

A Claude-specific edition with a Claude Code plugin manifest is available at [clarity-toolkit-claude](https://github.com/steves460ng/clarity-toolkit-claude).

## Usage

Ask in natural language. Naming the skill makes the choice explicit.

### grill-me — Clarify requirements through an interview

> Use grill-me to interview me. I want to build an onboarding page for new employees.

By default, the assistant asks one or two questions at a time in the chat, which stays easy to read on a phone. Prerequisite decisions come first (who the users are before how they log in). For a full survey, say "survey mode" or "ask me everything at once": the assistant then asks 10–15 questions per round, grouped by theme, for up to three rounds (round 1 maps the topic, round 2 goes deeper, round 3 closes the gaps), and more rounds are available on request. When the session can create an editable document, the survey goes into one so you can type answers directly under each question; later rounds are added to the same document. Answer in prose or by question ID, answer only some questions, skip a question, or rewrite it. Say "stop here and summarize" at any time.

**What you get:** a summary of the goal, main users, scope, accepted decisions, constraints, and open questions. Confirming the summary does not authorize implementation.

### to-question — Prepare questions for someone else

> Use to-question to draft questions for an external payment provider. The recipient is a technical contact we are working with for the first time. We need to confirm recurring payment support, integration requirements, and the settlement schedule.

The assistant drafts the document instead of asking you questions you cannot answer yourself. It asks at most two short questions first, and only when the recipient or the purpose is unclear. High-impact questions come first, each with a blank answer field. Deadlines and names are never invented. The questionnaire can be in a different language from the conversation.

**What you get:** a questionnaire with its purpose, recipient, context, answering instructions, and grouped questions. The assistant drafts it but does not send it.

### meta-conv-filter — Make text stand on its own

> Use meta-conv-filter to make this plan readable without our conversation.

Removes revision traces ("improved version") and conversation references ("as discussed"), and replaces pointers such as "option two" with the actual decision. Missing information is marked as not specified rather than invented. Facts, numbers, uncertainty, and sources are kept.

**What you get:** the cleaned text itself, without a preface about what was removed.

### handoff — Pass the work on

> Use handoff to summarize this conversation. The next session will start with the mobile screen design.

Separates confirmed decisions, completed work with evidence, proposals, open questions, and next actions. Passwords and tokens are replaced with `[REDACTED]`. When you paste a handoff into a new conversation, the assistant treats it as context to verify, not as proof of current state.

**What you get:** a handoff document the next person or session can continue from. A new conversation does not remember earlier ones unless the tool provides memory; carry the handoff over yourself.

## Use them together

1. Clarify the idea with `grill-me`.
2. Put questions that need someone else's input into a document with `to-question`.
3. Turn the summary or resulting draft into final text with `meta-conv-filter`.
4. Pass the work on with `handoff`.

## Output

Interview rounds appear in the chat. Summaries, questionnaires, final text, and handoffs are created as an editable document when the session supports it; otherwise they come as one copyable Markdown block. A `.md` file is created only on request.

## License and attribution

MIT License. `grill-me`, `to-question`, and `handoff` are adapted from [Matt Pocock's skills](https://github.com/mattpocock/skills); `meta-conv-filter` is original to Clarity Toolkit. See [LICENSE](LICENSE) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

This project is not affiliated with or endorsed by Matt Pocock or any AI provider.
