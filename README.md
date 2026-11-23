# Clarity Toolkit

[한국어 README](README.ko.md)

Four conversation skills for AI assistants: clarify an idea or stress-test a plan through an interview, prepare questions for someone who holds the answers, hand work over to the next person or session, and audit how a session went.

| Skill | Use it when |
| --- | --- |
| `grill-me` | You have an idea or plan but have not worked out the requirements, or you want a finished plan challenged. |
| `to-question` | An expert, vendor, customer, or colleague holds facts or decisions you need. |
| `handoff` | Work continues with another person, agent, or a new session, or you are resuming from a handoff. |
| `session-review` | You want an audit of your prompts and session management in the current session. |

Each skill counters a common assistant habit: starting to build instead of interviewing, asking the user the recipient's questions instead of drafting a questionnaire for the recipient, blurring proposed plans with completed work, and glossing over what went wrong in a session.

The skills are written in plain Markdown and do not depend on a particular model, app, or service. Where a skill can use a capability such as an editable document, it also says what to do when the capability is missing.

## Install

Each skill is a single, self-contained file at `skills/<name>/SKILL.md`, with a `name` and `description` header followed by instructions. No shared files, templates, or scripts are required.

- **Tools that load `SKILL.md` skills:** copy each `skills/<name>/` folder into the tool's skills directory, or add the skills through its settings. Check the tool's documentation for the location.
- **Tools without skill support:** paste the body of a `SKILL.md` into a custom instruction, system prompt, or project instruction, or attach it to a conversation and ask the assistant to follow it.

### Install with a prompt

If the assistant can read GitHub and add skills or instructions in your tool, paste this into a conversation:

> https://github.com/steves460ng/clarity-toolkit
> Read the four SKILL.md files under `skills/` and install them as skills in this tool. If a skill with the same name already exists, update it instead of creating a duplicate. If this tool cannot install skills, tell me where to put each file or how to add it as a custom instruction instead. Do not change any other settings.

## Usage

Ask in natural language. Naming the skill makes the choice explicit.

### grill-me — Clarify requirements through an interview

> Use grill-me to interview me. I want to build an onboarding page for new employees.

By default, the assistant asks one or two questions at a time in the chat, which stays easy to read on a phone. Prerequisite decisions come first (who the users are before how they log in). For a full survey, say "survey mode" or "ask me everything at once"; the word "survey" alone does not switch modes. The assistant then asks 10–15 questions per round, grouped by theme, for up to three rounds (round 1 maps the topic, round 2 goes deeper, round 3 closes the gaps), and more rounds are available on request. When the session can create an editable document, the survey goes into one so you can type answers directly under each question; later rounds are added to the same document. Answer in prose or by question ID, answer only some questions, skip a question, or rewrite it. Say "stop here and summarize" at any time.

For a short session, say "quick": at most five questions, then two challenge points. Before the summary, the assistant runs a challenge round that tests the plan: unverified assumptions, conflicting decisions, failure scenarios, and missing stakeholders or costs. Accept, rebut, or defer each point. If you bring a finished plan and ask to have it grilled, the assistant skips the exploration, lists the decisions it read from the plan so you can correct them, and goes straight to repeated challenge rounds.

**What you get:** a summary of the goal, main users, scope, accepted decisions, constraints, challenge outcomes, and open questions. For a finished plan, decisions are grouped into held, revised, and still at risk. Confirming the summary does not authorize implementation.

### to-question — Prepare questions for someone else

> Use to-question to draft questions for an external payment provider. The recipient is a technical contact we are working with for the first time. We need to confirm recurring payment support, integration requirements, and the settlement schedule.

The assistant drafts the document instead of asking you questions you cannot answer yourself. It asks at most two short questions first, and only when the recipient or the purpose is unclear. High-impact questions come first, each with a blank answer field. Deadlines and names are never invented. The questionnaire can be in a different language from the conversation.

**What you get:** a questionnaire with its purpose, recipient, context, answering instructions, and grouped questions. The assistant drafts it but does not send it.

### handoff — Pass the work on

> Use handoff to summarize this conversation. The next session will start with the mobile screen design.

Separates confirmed decisions, completed work with evidence, proposals, open questions, and next actions. Passwords and tokens are replaced with `[REDACTED]`. When you paste a handoff into a new conversation, the assistant treats it as context to verify, not as proof of current state.

**What you get:** a handoff document the next person or session can continue from. A new conversation does not remember earlier ones unless the tool provides memory; carry the handoff over yourself.

### session-review — Audit the current session

> Use session-review to audit this session.

Reviews only the current session. Every finding quotes your own words with a line of context, so you do not have to scroll back to find the message. Each friction point is attributed to the user, the assistant, both, or the nature of the task, and assistant faults are reported in their own section, each with a countermeasure you can apply, such as a standing instruction to add. The tone is direct: no courtesy praise and no padded findings. A session without friction gets a brief review.

**What you get:** a review in the chat with a verdict, ratings by axis, findings by severity, assistant faults, one or two rewritten prompts, and three habits for the next session. Nothing is saved, and earlier reviews are not compared.

## Use them together

1. Clarify the idea with `grill-me`.
2. Put questions that need someone else's input into a document with `to-question`.
3. Pass the work on with `handoff`.
4. Check how the session went with `session-review`.

## Output

Interview rounds and session reviews appear in the chat. Summaries, questionnaires, and handoffs are created as an editable document when the session supports it; otherwise they come as one copyable Markdown block. A `.md` file is created only on request.

## License and attribution

MIT License. `grill-me`, `to-question`, and `handoff` are adapted from [Matt Pocock's skills](https://github.com/mattpocock/skills). `session-review` is original to this project. See [LICENSE](LICENSE) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

This project is not affiliated with or endorsed by Matt Pocock or any AI provider.
