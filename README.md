# Clarity Toolkit

[한국어 README](README.ko.md)

A collection of ChatGPT skills for clarifying ideas, preparing useful questions, understanding complex explanations, and handing work over to the next person.

This unofficial project adapts five skills from [Matt Pocock's skills](https://github.com/mattpocock/skills) for ChatGPT.

## How to use

Select Clarity Toolkit in a ChatGPT environment that supports the plugin, then describe what you need in natural language. The examples below are prompts, not commands that require a slash-command interface.

| Skill | When to use it |
| --- | --- |
| `grill-me` | You have an idea but have not worked out the requirements. |
| `grilling` | You want to examine related decisions in the right order. |
| `to-questionnaire` | You need to organize questions for someone else. |
| `wait-what` | An explanation is hard to follow or you have lost the context. |
| `handoff` | You need to continue the work with another person or in a new session. |

## grill-me — Clarify requirements through an interview

Describe what you want to build, the problem you want to solve, or a plan you are considering, and ask for an interview.

The skill uses decisions already made in the conversation and asks about unresolved points. Follow-up questions help establish the goal, scope, constraints, and success criteria.

### Examples

> Use grill-me to interview me about the requirements.  
> I want to build an onboarding page for new employees.  
> Start by clarifying who is having trouble and what problems they face.

You can set the pace:

> Ask one question at a time. If there are options, include a recommendation and explain why.

To finish early:

> Stop the questions here. Summarize what we have decided and what remains unresolved.

### What you get

A requirements summary covering the goal, main users, scope, confirmed decisions, constraints, and open questions.

## grilling — Examine decisions in dependency order

This shared interview procedure helps with decisions that depend on one another. It powers `grill-me`, and you can also request it directly in conversation.

For example, it avoids settling on a login method before identifying the intended users. It starts with prerequisite decisions and uses your answers to determine what to ask next. By default, a round contains one to three questions.

### Examples

> Use the grilling procedure to examine this plan.  
> I want to launch a paid newsletter, but I have not decided on the audience, price, or publishing schedule.  
> Ask about the connected decisions in the order they need to be made.

Include decisions you have already made to avoid repeating them:

> The audience is developers with fewer than three years of experience.  
> Keep that decision and examine the remaining choices.

### What you get

Recommendations and their reasons, a record of decisions you accept, and their implications for later choices. Agreement in the interview does not authorize implementation or external actions.

## to-questionnaire — Prepare questions for someone else

Use this when an expert, vendor, customer, or colleague holds information you need.

Explain who will answer and what their answers need to help you decide. The skill drafts a questionnaire with context and an answer space for each question, placing the most important questions first.

### Examples

> Use to-questionnaire to draft questions for an external payment provider.  
> The recipient is a technical contact we are working with for the first time.  
> We need to confirm recurring payment support, integration requirements, and the settlement schedule so we can decide whether to use the provider.

You can request a separate language for the document:

> Keep our conversation in Korean, but write the questionnaire in English.

### What you get

A Markdown questionnaire with a purpose, intended recipient, background, answering instructions, questions grouped by topic, and answer spaces.

This skill drafts the questionnaire. It does not automatically send it by email or messenger.

## wait-what — Re-explain with the missing context

Ask for a new explanation when the previous one was difficult to follow.

The skill leads with the main point, adds the necessary background, and explains unfamiliar terms. It uses a concrete example when helpful and preserves the original uncertainty and caveats.

### Examples

> wait-what. I did not understand the explanation.  
> Start by explaining what a cache is, then give an example of how it affects response time.

You can specify the level and length:

> Explain it again in three paragraphs for someone with no development experience.

### What you get

The key point, necessary background, plain-language definitions, and examples.

If the earlier explanation is not available, such as in a new conversation, provide the text you want explained first.

## handoff — Help the next person continue the work

Use this when a conversation has become long or you need to hand work over to another person, agent, or session.

The skill draws on the available conversation to summarize the goal, confirmed decisions, completed work, unresolved issues, and next actions. It distinguishes proposed plans from completed work and excludes sensitive values such as passwords and tokens.

### Examples

> Use handoff to summarize this conversation.  
> The next person will draft the questionnaire.  
> Include confirmed requirements, unverified facts, references, and next actions.

For a new session:

> Prepare a handoff I can paste into a new conversation.  
> The next session will start with the mobile screen design.

### What you get

A Markdown handoff that gives the next person enough context to understand and continue the work.

It is not automatically transferred to a new conversation. Paste or provide the document yourself.

## Use the skills together

1. Clarify your idea and requirements with `grill-me`.
2. Put questions that need external input into a document with `to-questionnaire`.
3. Revisit difficult explanations with `wait-what`.
4. Capture the context and next actions with `handoff` when passing the work on.

## Output format

Documents are provided as Markdown in the conversation by default. In an environment with file creation tools, you can also request a `.md` file.

File creation and skill selection and invocation depend on the ChatGPT environment. This plugin does not require a separate MCP server or runtime scripts, and it does not provide permanent storage or automatic memory across sessions.

## License and attribution

Distributed under the MIT License.

Original copyright: Copyright (c) 2026 Matt Pocock

The original copyright and permission notice are preserved. See [LICENSE](LICENSE) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for details.

This project is not affiliated with or endorsed by Matt Pocock.
