# Clarity Toolkit

[한국어 README](README.ko.md)

A collection of ChatGPT skills for clarifying ideas, preparing useful questions, understanding complex explanations, and handing work over to the next person.

This unofficial project adapts five skills from [Matt Pocock's skills](https://github.com/mattpocock/skills) for ChatGPT.

## Add the plugin from GitHub

In a ChatGPT environment with repository access and plugin creation or registration tools, you can provide this repository's URL and ask ChatGPT to add it as a private plugin. This is an assisted packaging and registration workflow, not a universal one-click GitHub installer. Availability depends on your account, workspace policy, and connected tools.

### 1. Request the plugin

Paste this into a conversation with the required tools available:

> https://github.com/steves460ng/clarity-toolkit  
> Review the `clarity-toolkit/` folder in this repository and add it to my ChatGPT account as a private plugin. If the same plugin already exists, compare it with the repository version instead of creating a duplicate. Preserve the MIT license and attribution. After registration, provide the plugin link, report which of the five skills were registered, and distinguish confirmed results from anything still unverified.

The installable plugin source is in `clarity-toolkit/`. The repository root also contains development tools and should not be packaged wholesale as the plugin.

### 2. Select the registered plugin

Open the returned plugin link and follow the host's instructions to enable or select it. Start a new conversation if the host requires one for newly added plugins to become available.

Registration alone does not prove that skill invocation works. Once the plugin is available in the conversation, try a short request such as:

> @Clarity Toolkit Use grill-me to interview me about a lesson plan. Ask one question at a time.

### 3. Reuse or update an existing plugin

If you have already added Clarity Toolkit, use the existing plugin rather than registering it again. To request an update, provide this repository's URL and identify the existing plugin.

Adding a plugin from this repository does not by itself establish automatic synchronization with GitHub. Later repository changes may require a separate update.

If your ChatGPT environment does not provide the required tools, the URL alone cannot install the plugin. Use a supported plugin import workflow available to your account or an environment with plugin creation and registration tools.

## How to use

Select Clarity Toolkit in a ChatGPT environment that supports the plugin, then describe what you need in natural language. The examples below are prompts, not commands that require a slash-command interface.

| Skill | When to use it |
| --- | --- |
| `grill-me` | You have an idea but have not worked out the requirements. |
| `grilling` | You want to examine related decisions in the right order. |
| `to-questionnaire` | You need to organize questions for someone else. |
| `wait-what` | An explanation is hard to follow or you have lost the context. |
| `handoff` | You need to continue the work with another person or in a new session. |

### Edit questions and drafts

Interview rounds and deliverables now request an editable writing block, so you can revise a question, select optional examples, add your own ideas, or change an earlier answer. The interview begins with open exploration rather than a recommended answer to accept. You can reply in prose, skip a question, or keep a decision open.

For example:

> Ask me one open question at a time in a writing block. Leave the answer blank. If choices help, make them optional and let me write my own answer. Do not recommend a solution yet.

To revise a draft:

> Keep the 20-minute duration, change the audience to eight-year-olds, and rewrite Q2 as an open question. Preserve the other answers.

Native editing depends on the host. If a native writing block is unavailable, the plugin provides one copyable text block and states that it is not an interactive editor. Checkboxes in that fallback are text markers, not clickable controls; no autosave or automatic synchronization is implied.

### Request a workflow in natural language

After selecting the plugin with `@`, you can describe your goal without naming a skill every time. The model can use the request's context to apply a suitable workflow. The shared `grilling` skill currently allows implicit invocation; the other four entry skills are configured for explicit user invocation.

For example:

> @Clarity Toolkit I want to create a lesson plan about preventing colds for children. Interview me to help organize my thoughts.

This asks for an interview to clarify your own thinking, so `grilling` is a suitable procedure. It can start with the children's ages, lesson duration, and learning goals, then follow up based on your answers.

By contrast, “Draft a questionnaire to distribute to parents” calls for `to-questionnaire`: a document for other people to answer.

For a clearer request:

> @Clarity Toolkit I want to create a lesson plan about preventing colds for children. Before writing it, ask me one question at a time to clarify the audience, learning goals, and activities.

Skill selection depends on the model's interpretation and the host's plugin support; this is not a guarantee of deterministic routing. To make the intended procedure explicit, include its name, such as “Use grill-me to interview me.” These examples illustrate intended usage, not verified installed-host behavior.

## grill-me — Clarify requirements through an interview

Describe what you want to build, the problem you want to solve, or a plan you are considering, and ask for an interview.

The skill uses decisions already made in the conversation and asks about unresolved points. Follow-up questions help establish the goal, scope, constraints, and success criteria.

### Examples

> Use grill-me to interview me about the requirements.  
> I want to build an onboarding page for new employees.  
> Start by clarifying who is having trouble and what problems they face.

You can set the pace:

> Ask one open question at a time. Leave the answer blank and let me add my own ideas or change the question.

To finish early:

> Stop the questions here. Summarize what we have decided and what remains unresolved.

### What you get

A requirements summary covering the goal, main users, scope, confirmed decisions, constraints, and open questions.

## grilling — Examine decisions in dependency order

This shared interview procedure helps with decisions that depend on one another. It powers `grill-me`, and you can also request it directly in conversation.

For example, it avoids settling on a login method before identifying the intended users. It starts with prerequisite decisions and uses your answers to determine what to ask next. By default, a round contains one or two questions, with open exploration before narrowing choices.

### Examples

> Use the grilling procedure to examine this plan.  
> I want to launch a paid newsletter, but I have not decided on the audience, price, or publishing schedule.  
> Ask about the connected decisions in the order they need to be made.

Include decisions you have already made to avoid repeating them:

> The audience is developers with fewer than three years of experience.  
> Keep that decision and examine the remaining choices.

### What you get

An editable record of ideas, decisions you explicitly accept, open possibilities, and their implications for later choices. Advice is offered when requested or after enough exploration, rather than prefilled into your answers. Agreement in the interview does not authorize implementation or external actions.

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

Questions, explanations, summaries, and handoffs request native editable writing blocks by default. If unsupported, one copyable fenced text block is used with an explicit limitation notice. You can also request another format or, when file tools are available, a `.md` file of the latest draft.

File creation and skill selection and invocation depend on the ChatGPT environment. This plugin does not require a separate MCP server or runtime scripts, and it does not provide permanent storage or automatic memory across sessions.

## License and attribution

Distributed under the MIT License.

Original copyright: Copyright (c) 2026 Matt Pocock

The original copyright and permission notice are preserved. See [LICENSE](LICENSE) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for details.

This project is not affiliated with or endorsed by Matt Pocock.
