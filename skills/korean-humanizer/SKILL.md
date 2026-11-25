---
name: "korean-humanizer"
description: "Use when the user asks to make Korean text sound less AI-written or more natural (\"AI 티 안 나게\", \"사람이 쓴 것처럼\", \"자연스럽게 다듬어줘\", \"번역체 고쳐줘\"), to find AI tells in Korean text without fixing them (\"AI 흔적 찾아줘\"), or to rewrite Korean text to a target length (\"1000자로 맞춰서\"). Not for spelling-only fixes, translation, or rewrites that add new content."
---

# Korean Humanizer

Rewrite Korean text that reads as AI-written so it reads as written by a person, without changing what it says. Detect AI tells with the catalog below, grade each by severity, replace only what was detected, audit the result, and grade it. Write the rewrite and all user-facing notes in the user's language; keep the pattern names and examples below as reference.

## Four rules

1. **Meaning stays fixed.** Facts, claims, figures, proper nouns, and direct quotations stay exactly as written. Never invent or alter them.
2. **Evidence first.** Edit only spans where a tell was detected. Leave undetected passages alone.
3. **Genre stays.** Do not turn a column into an essay or a report into a blog post. Keep the original register.
4. **No over-editing.** A change rate above **30% triggers a warning**; above **50%, stop and roll back**. Flattening good human writing into average prose is the most common failure.

## Severity

Judge tells as a cluster, and weigh each one by severity.

- **S1 decisive:** one occurrence signals AI. Always remove. Examples: double passive "되어지다", "결론적으로", "시사하는 바가 크다", commas after connective endings, emoji decoration, chatbot leftovers.
- **S2 strong:** one or two are acceptable; remove from the third repetition. Examples: "~을 통해", "~에 의해" passives, three-part formulas, future assertions "~할 것이다".
- **S3 weak:** not a signal on its own. Touch only when it clusters with other tells. Examples: curly quotes alone, a single dash, one short emphatic sentence.

## Never touch

In both detection and rewriting, leave these unchanged:

- Proper nouns, product, model, organization, person, and place names
- Figures, dates, units, statistics, formulas
- Direct quotations in double quotes, legal text
- Industry-standard English abbreviations (LLM, GPU, API, MCP, and so on)
- Specific details and asides the writer put in on purpose (see "Signs of human writing")

## Procedure: detect, rewrite, audit, grade

0. **Triage.** Decide what to fix and how far.
   - Is there a cluster of tells? Do not rewrite a whole text over one dash or one connective.
   - **If only formatting is the problem, fix only formatting.** When heavy bold, emoji, interpuncts, and dashes are all there is, leave the prose as it is.
   - Rewrite sentence by sentence **only when the prose itself reads as AI**.
   - Note any target length.
1. **Detect.** Scan with the catalog (A–J) and mark each tell with its span, category, and severity. Start with S1.
2. **Rewrite.** *Replace* each tell with natural Korean; rewrite rather than delete. Cover everything the original covers and do not shorten it arbitrarily.
3. **Audit.** Ask again: "Why does this still read as AI?" Note remaining tells briefly. Check that *your* rewrite did not add new tells through synonym cycling (F) or added connectives (H), and that the change rate is within 30%. If any of the six self-checks below fails, roll back that edit and rewrite again. Run this loop at most once or twice.
4. **Grade.** Score the result with the grades below. For C or D, recommend another pass or human review.

## Grades

- **A:** no S1 left, at most two S2 left, change rate 10–25%, all six self-checks pass.
- **B:** no S1 left, at most four S2 left, at least five self-checks pass.
- **C:** one or two S1 left, or signs of over-editing. Recommend a second pass.
- **D:** three or more S1 left, or change rate above 50%. Stop and recommend human review.

## Target length

When the user gives a target length ("length=1000", "1000자로 맞춰서", "절반으로 줄여줘", "300자 내외로"), fit the rewrite to it.

- **Count characters including spaces by default.** Count without spaces when the user says so ("공백 제외"). When unclear, report both.
- **Tolerance is ±5%** (a 1000-character target allows 950–1050). When the user asks for an exact length, stay within ±2%.
- **To lengthen,** never pad with filler or AI phrasing; that is what this skill removes. Expand facts already in the text. **Do not invent facts.** If there is not enough to expand, ask the user instead of guessing.
- **To shorten,** cut filler, hedges, vague endings, and repetition first. Keep specific details and core facts to the end.
- **Count, do not estimate.** If code execution is available, count with code; otherwise count carefully by hand. **Report both counts, with and without spaces.**
- Without a target, **keep the original length**.

## Voice calibration (optional)

When the user provides a sample of their own writing, analyze it before rewriting.

1. **Read the sample and take notes:** sentence length pattern (short and clipped or long and flowing), endings and speech level (해요체, 합니다체, 반말; spoken or written), vocabulary level, verbal habits and connectives ("근데", "그래서", "암튼"), and the share of Sino-Korean and loan words.
2. **Rewrite in that voice.** Do not stop at removing AI patterns; *replace* them with the sample's voice. If the writer uses "되게" or "약간", do not upgrade them to "매우" or "다소".
3. **Without a sample,** use a natural voice with varied rhythm (see "Personality and soul").

The sample can be pasted inline ("내 말투 샘플은 이거야: …") or attached as a file.

## Personality and soul

Removing AI patterns is half the job. Writing without a voice gives itself away as much as slop does.

**Apply this section only when the genre allows it:** blogs, essays, columns, reviews, personal writing. In encyclopedic, technical, legal, and official writing, a neutral and plain style *is* the correct human voice. Do not force opinions or the first person into it (rule 3).

Signs of voiceless writing, even when grammatically clean:

- Every sentence has the same length and structure.
- It reports neutrally with no opinion.
- There is no hesitation or mixed feeling.
- There is no first person where one would fit.
- There is no humor, edge, or personality; it reads like a press release or a wiki.

How to add a voice:

- **Have an opinion.** "솔직히 이걸 어떻게 받아들여야 할지 모르겠다" sounds more human than a neutral list of pros and cons.
- **Vary the rhythm.** Short sentences, then now and then a long one that runs to the end. Mix them.
- **Allow some looseness.** Perfect structure reads as algorithmic. Tangents, asides, and unfinished thoughts read as human.

Before (clean but voiceless):

> 이번 실험은 흥미로운 결과를 보여주었다. 에이전트는 300만 줄의 코드를 생성했다. 일부 개발자는 깊은 인상을 받았고, 다른 이들은 회의적이었다. 그 함의는 여전히 불분명하다.

After (with a pulse):

> 이걸 어떻게 받아들여야 할지 솔직히 모르겠다. 코드 300만 줄을, 사람이 자는 동안 기계가 짜놨다. 개발자 절반은 멘붕이 왔고, 나머지 절반은 이게 왜 별거 아닌지 설명하느라 바쁘다. 진실은 아마 그 사이 어디 시시한 지점에 있겠지만, 나는 밤새 일했을 그 에이전트들이 자꾸 떠오른다.

## Pattern catalog (A–J)

Each pattern is labeled `ID · severity`. The full table is in the appendix. Below are the patterns that appear most often and most strongly in Korean AI writing. Where an After example contains a fact the Before lacks, assume that fact appears elsewhere in the source; never add facts to a rewrite.

### A. Translationese (the main tell in Korean AI writing)

**A-1, A-2, A-3. Prepositions translated literally as particles · S1.** Watch for ~을 통해 (through), ~에 대해/대한 (about), ~에 있어서 (in), ~로서 (as), ~와 함께 (with), ~의 경우 (in the case of), ~중 하나 (one of the), ~라는 사실 (the fact that). English prepositional phrases mapped one-to-one onto particles make sentences long and stiff. Korean folds them into verbs and word order.

> Before: 이 도구를 통해 사용자는 데이터에 대한 분석을 수행함에 있어서 효율성을 가질 수 있다. 이것은 가장 중요한 기능 중 하나이다.
> After: 이 도구로 사용자는 데이터를 효율적으로 분석할 수 있다. 핵심 기능이다.

**A-7. "가지다" for "have" · S1.** 중요성을 가지다, 의미를 가지다, 영향력을 가지다, ~을 가지고 있다. Rewrite with "있다", an adjective, or a verb.

> Before: 이 연구는 중요한 의미를 가진다. 또한 큰 영향력을 가지고 있다.
> After: 이 연구는 중요하다. 영향력도 크다.

**A-8, A-9. Excess and double passives · S1.** ~되어진다, ~지게 된다, ~여겨진다, ~보여진다 ("되어지다" is a double passive, close to ungrammatical), and "~에 의해" passives. Make the actor the subject and use the active voice.

> Before: 이 방법은 효과적이라고 보여지며, AI에 의해 생성된 코드가 많은 곳에서 사용되어지고 있다.
> After: 이 방법은 효과적이고, AI가 만든 코드가 여러 곳에서 쓰인다.

**A-16. Compulsive "그/그녀/그것/그들" · S1.** Three or more literal translations of he/she/it/they in one paragraph. Korean often drops the subject or refers back with a title or noun phrase. Inanimate subjects such as "이것은/그것은 ~이다" share the same root.

> Before: 이 기능은 사용자에게 편의성을 제공한다. 그것은 작업 시간의 단축을 가능하게 한다. 그리고 그것은 비용도 줄인다.
> After: 이 기능을 쓰면 편하다. 작업 시간이 줄고 비용도 준다.

**A-17. Overused plural "~들" · S2.** The English plural -s rendered mechanically. Drop "~들" when context shows the plural, especially next to a quantifier ("많은 사용자들이").

> Before: 많은 개발자들이 다양한 도구들을 사용하여 여러 문제들을 해결한다.
> After: 많은 개발자가 여러 도구로 다양한 문제를 해결한다.

**A-18. Long left-branching modifiers · S2.** Three or more words of relative clause stacked before a noun. Split the sentence or move the description after the noun.

> Before: 지난해 출시되어 시장에서 큰 호응을 얻으며 빠르게 점유율을 늘려온 이 제품은 곧 단종된다.
> After: 이 제품은 곧 단종된다. 지난해 출시돼 점유율을 빠르게 늘려온 제품이다.

**A-19. Stacked particles "~에서의/~으로의/~에의" · S2.** Rewrite as a clause or phrase (a plain "~의" is not a target).

> Before: 일터에서의 변화와 미래로의 도약을 위한 준비
> After: 일터가 어떻게 바뀌고, 미래로 나아가려면 무엇을 준비해야 하는지

**A-6. Excess nominalization · S2.** ~의 진행, ~의 향상, ~을 실시/수행/진행, ~을 도모: verbs frozen into nouns with "~하다" or "실시하다" attached. Turn them back into verbs.

> Before: 성능의 향상을 위해 코드의 최적화를 진행하였다.
> After: 성능을 높이려고 코드를 최적화했다.

### B. Excess English

**B-1, B-2. Parenthetical English every time, or English left untranslated · S2.** Gloss in English only at first mention ("주권 AI(Sovereign AI)"), then use Korean only. Keep industry-standard abbreviations.

### C. Structural patterns

**C-11. Comma after a connective ending · S1.** A comma right after -고, -며, -지만, -면서, -아서/-어서. A strong tell in Korean AI writing; six or more is decisive. Usually the comma can simply go.

> Before: 그는 회의를 마치고, 사무실로 돌아왔으며, 보고서를 작성했지만, 만족하지 못했다.
> After: 그는 회의를 마치고 사무실로 돌아와 보고서를 썼지만 만족하지 못했다.

**C-7. Three-part formula, rule of three · S2.** Items forced into threes to look comprehensive ("A, B, 그리고 C", three nouns in a row, "먼저·반면·결국").

> Before: 이 서비스는 빠르고, 안전하며, 편리합니다. 사용자에게 혁신과 가치와 만족을 제공합니다.
> After: 이 서비스는 빠르고 안전합니다. 무엇보다 쓰기 편합니다.

**C-5. Emoji decoration · S1.** Emoji before headings or items. Remove all of them in columns and reports.

> Before: 🚀 **출시:** 3분기에 출시됩니다 / 💡 **핵심:** 사용자는 단순함을 선호합니다
> After: 제품은 3분기에 출시된다. 사용자 조사에서 단순한 쪽이 선호됐다.

**C-10. Repeated "X: Y" subtitle headings · S1.** Use short or declarative headings instead.

### D. AI signature phrases

**D-1. Summary pivots · S1.** 결론적으로, 따라서, 이를 통해, 그러므로, 요약하면, 정리하면. Beyond three, keep one or two as other endings and delete the rest.

**D-2, D-3. "시사하는 바가 크다", "주목할 만하다", "본질적으로", "핵심적으로" · S1.** Delete or replace with a concrete conclusion.

**D-4. Hype vocabulary · S1.** 다채로운, 풍부한, 깊이 있는, 진정한, 궁극적으로, 중추적인, 필수적인, 혁신적인, 독보적인, 파격적인, 압도적인, 획기적인, ~을 아우르다, ~을 녹여내다, ~을 담아내다, ~을 선사하다, 자리매김하다, 발돋움하다, 방증하다, ~의 향연. They arrive together in post-2023 writing. Replace with concrete figures and facts.

> Before: 이번 행사는 다채로운 볼거리를 선사하며, 지역 문화의 진정한 가치를 담아낸 축제로 자리매김했다. 이는 지역의 저력을 방증한다.
> After: 이번 축제에는 공연과 먹거리 장터가 열렸다. 지난해보다 방문객이 두 배 늘었다.

**D-5. Personified abstract subjects · S1.** "기술이 묻는다", "시대가 부른다". Use a person or an organization as the subject.

**D-6. Closing formulas · S1.** "~할 때다", "~해야 한다", "지금이야말로", and vague upbeat endings (귀추가 주목된다, 무한한 가능성, 밝은 미래). End plainly or delete.

> Before: 앞으로 회사의 행보가 기대된다. 무한한 가능성을 향한 도약이 계속될 것이며, 이는 더 나은 미래를 향한 큰 걸음이다.
> After: 회사는 내년에 지점 두 곳을 더 열 계획이다.

**D-8. Inflated significance · S1.** 단순한 ~를 넘어, ~의 중요한 이정표, 한 획을 그었다, 새로운 지평을 열었다, ~의 산물, ~을 상징한다: grand narratives attached to minor facts.

> Before: 1989년 설립된 이 연구소는 지역 통계 발전사에 중요한 이정표를 세우며, 행정 분권화라는 시대적 흐름을 상징하는 산물로 자리매김했다.
> After: 이 연구소는 1989년에 설립돼, 국가 통계청과 별개로 지역 통계를 수집·발표한다.

**D-9. Unsourced authority · S2.** 전문가들은 ~라고 말한다, 많은 사람들이 ~로 평가한다, ~로 알려져 있다. Name a concrete source or delete. Never invent a source; if the original gives none, say the claim is unsourced or drop the sentence.

### E. Rhythm and endings

**E-1, E-2. Uniform sentence length, repeated endings · S2.** Low variation in sentence length, "~다" four or more sentences in a row, and "~고 있다" used by default. Mix short and long sentences and vary endings. Turn "읽고 있다" into "읽는다" where the simple tense works.

**E-7. Inconsistent speech level (dialogue and spoken text only) · S2.** 해라체, 하게체, 하오체, 해요체, and 합쇼체 mixed in one paragraph. Use one.

### F. Excess modification and repetition

**F-4, F-5. Stacked nominal suffixes, "~적 N" chains · S2.** -성, -적, -화 plus -tion, -ment, -ness twelve or more times in one text, or chains such as "전략적 함의·실천적 기반". Return to verb and adjective roots ("정책의 시행" → "정책을 시행").

**F-1. Synonym cycling · S2.** The same referent renamed each time (주인공 → 캐릭터 → 인물 → 그 → 히어로). **Be especially careful not to do this yourself while rewriting.**

> Before: 주인공은 많은 시련을 겪는다. 이 캐릭터는 역경을 이겨내야 한다. 해당 인물은 마침내 승리한다.
> After: 주인공은 숱한 시련을 겪지만 결국 이겨낸다.

**F-2. False ranges and negative parallels · S2.** "~에서 ~까지" joining things not on one scale, or "단순한 X가 아니라 Y다" inflating an ordinary statement.

> Before: 이것은 단순한 노래가 아니다. 그것은 하나의 선언이다.
> After: 묵직한 비트가 곡의 공격적인 분위기를 살린다.

### G. Hedging

**G-1, G-2, G-3. Future assertions, guesses, safe balancing · S2.** Layers of "~할 것이다", "~로 보인다/~인 듯하다", and "장점도 있지만/신중하게/균형". State plainly where a plain statement holds.

> Before: 이 정책은 어느 정도 결과에 다소 영향을 미칠 수도 있다고 볼 수 있을 것이다.
> After: 이 정책은 결과에 영향을 줄 수 있다.

### H. Connective overuse

**H-1, H-3. Sentence-initial connectives and meta openers · S1.** 또한, 따라서, 즉, 나아가, 아울러, 게다가, 더욱이 five or more times, or "이는", "이 점에서", "이 관점에서" three or more times. Remove most and let the sentences carry the flow.

> Before: 또한, 이 기능은 편리하다. 더불어, 속도도 빠르다. 나아가, 비용도 절감된다. 이처럼, 장점이 많다.
> After: 이 기능은 편리하고 빠르다. 비용도 줄어든다.

### I. Formal and dependent nouns

**I-1. "~인 것이다 / ~한 것이다" endings · S1.** Use a plain ending. Remove authoritative essence framing as well ("진정한 문제는", "본질적으로", "결국 중요한 것은").

> Before: 진정한 문제는 조직이 변화할 수 있는가이다. 본질적으로, 결국 중요한 것은 조직의 준비 태세인 것이다.
> After: 관건은 조직이 변할 수 있느냐다. 그건 대개 일하는 습관을 바꿀 의지에 달렸다.

**I-4. Preachy obligation and preview lines · S2.** "~하는 것이 중요하다", "~할 필요가 있다", "명심해야 한다", and previews such as "지금부터 ~을 살펴보자", "본격적으로 들어가기에 앞서". Replace with concrete content from the text.

> Before: 무엇보다 사용자 경험을 최우선으로 고려하는 것이 중요하다. 지금부터 그 방법을 자세히 살펴보겠습니다.
> After: 가입 절차를 3단계에서 1단계로 줄이자 이탈률이 절반으로 떨어졌다.

### J. Visual decoration

**J-1. Bold overuse, bullets with bold labels · S2.** Bold on phrases that need no emphasis, or every item cut into a "**label:**" bullet. In columns and reports, turn them into prose.

> Before: - **사용자 경험:** 인터페이스가 개선되었습니다. - **성능:** 알고리즘으로 향상되었습니다. - **보안:** 암호화로 강화되었습니다.
> After: 이번 업데이트로 인터페이스가 새로워졌고, 알고리즘 최적화로 속도가 빨라졌으며, 종단 간 암호화가 추가됐다.

**J-2. Dashes, interpuncts, curly quotes, tildes · S1 (dashes) / S2 / S3.** No em dash (—) or en dash (–) in the final text. The em dash is the biggest tell in English AI writing, and Korean AI writing borrows it. Use periods, commas, colons, or parentheses, or restructure the sentence. Also tidy chains of words joined by interpuncts (·), five or more quotation marks used for emphasis, and sentence-final tildes (~). **Before delivering, search for `—` and `–`. If any remain, you are not done.**

> Before: 이 정책은 — 예고도 없이 발표되어 — 수천 명에게 영향을 준다. 빠르고·정확하고·강력한 처리가 가능하다.
> After: 이 정책은 예고 없이 발표돼 수천 명에게 영향을 준다. 처리가 빠르고 정확하다.

### K. Chatbot leftovers

**K-1, K-2. Chatbot replies and flattery · S1.** 물론이죠!, 좋은 질문이에요!, 도움이 되었으면 좋겠습니다, 더 궁금한 점이 있으면 말씀해 주세요, 아래는 ~입니다, 정말 훌륭한 지적이세요!. Delete entirely.

> Before: 좋은 질문이에요! 아래는 프랑스 혁명에 대한 개요입니다. 도움이 되었으면 좋겠습니다!
> After: 프랑스 혁명은 1789년 재정 위기와 식량난으로 인한 불만에서 시작됐다.

**G-4. Knowledge-limit hedges and speculative filler · S2.** "공개된 정보가 제한적이지만", "~로 추정된다", "조용한 행보를 보이는 것으로". If unknown, say it is not in the source or drop the sentence. Do not dress up a guess as fact (rule 1).

## Avoiding false positives

People hit some of these patterns too. On their own, the following are not AI signals (treat them as S3):

- **Clean spelling and a consistent style.** Polished is not AI.
- **Formal style and Sino-Korean words.** AI overuses *specific* words (D-4); not every Sino-Korean word is a tell. "방증" or "기실" in legal or academic writing is normal.
- **One or two connectives.** A signal only when they stack paragraph after paragraph.
- **Curly quotes or a dash alone.** They may be a word processor default or an editor's habit. Count them only alongside other tells.
- **One short emphatic sentence.** Flag only when several in a row inflate the tone.
- **Numbered or bulleted lists themselves.** A normal format for reports and manuals.
- **Letter-style greetings and closings, or an unsourced claim.** Neither proves anything alone.

When unsure, look for a **cluster**, not a single hit. One dash means nothing. A dash plus a rule of three plus "다채로운 향연" plus an outlook paragraph in one text is a confession.

## Signs of human writing (keep them)

When you see these, lean toward leaving the text alone. Over-editing erases what makes it human.

- **Specific, odd details that are hard to invent:** a real address, a strange quote, "치과 윗층 변호사".
- **Mixed feelings and unresolved tension.** AI converges on tidy conclusions.
- **References tied to a time or group:** a specific year, subculture memes, slang, inside jokes.
- **First-person editorial choices the writer could defend, uneven sentence lengths, real asides, parentheses, and self-corrections.**

## Self-check (after rewriting; roll back any edit that fails an item)

1. **Proper nouns, figures, dates, and quotations are 100% preserved,** identical to the original.
2. **The change rate is 30% or less** (above 50%, stop).
3. **The genre has not shifted:** no column turned into an essay, no report into a blog post.
4. **The register is preserved:** formal in, formal out.
5. **No S1 remains:** A-7, A-8, A-16, C-5, C-10, C-11, D-1 to D-6, D-8, H-1, I-1, J-2, K-1, K-2.
6. **No invented flourishes:** no metaphors, rhetoric, or literary phrasing that the original lacked.

## Output

Deliver, in order: a draft, a short bullet list of what still reads as AI (remaining tells with severity), the final text, and optionally a one-line summary of what changed with the self-assigned grade (A–D). With a target length, add the final character counts with and without spaces. If the user asks for the result only, deliver only the final text. If the user asks only to find AI tells, report the tells with span, category, and severity, and do not rewrite.

## When not to use

- Only spelling and spacing need fixing.
- The task is fact-checking or adding sources. This skill fixes style and does not verify facts.
- The task needs new content the original does not contain. Meaning is preserved, not extended.

## Done when

- The final text has no dashes (`—`, `–`) or emoji, and no S1 tell remains.
- Translationese (literal particles, "가지다", double passives, compulsive "그/그녀", left-branching modifiers) reads as natural Korean.
- Hype vocabulary, rules of three, closing clichés, and commas after connective endings are cleaned up.
- Everything in the original is covered, no fact is changed or invented, and the change rate is 30% or less (stop above 50%).
- The false-positive guidance was applied, so human details were not damaged.
- With a target length, the text was actually counted, falls within ±5% (±2% when exact), and both counts are reported.
- All six self-checks pass and a grade (A–D) is given.

## Appendix: full pattern table

### A. Translationese

| ID | Pattern | Severity | Fix |
| --- | --- | --- | --- |
| A-1 | "~에 대해(서)" | S1 | Use the object particle directly ("X에 대해 논의" → "X를 논의") |
| A-2 | Overused "~를 통해/통하여" | S1 | Spread across "~로", "~해서", "~함으로써" |
| A-3 | "~에 있어(서)" | S1 | "~에서", "~을 볼 때" |
| A-4 | "~라는 점에서" 3+ times | S2 | "~서", "~라는 이유로" |
| A-5 | "~와 관련하여/관련된" | S2 | "~에", "~의" |
| A-6 | Excess nominalization, "~에 기반하여/바탕으로" | S2 | Back to verbs ("성능의 향상" → "성능을 높이려고") |
| A-7 | "가지고 있다", literal have/make/take/give + noun | S1 | Adjective or verb ("경쟁력을 가지고 있다" → "경쟁력이 강하다") |
| A-8 | Double passive "~되어진다/보여진다" | S1 | Active or single passive ("판단되어진다" → "판단된다") |
| A-9 | "~에 의해" passive | S2 | Actor as subject ("AI에 의해 생성" → "AI가 만든") |
| A-10 | Overused "~할 수 있다" | S2 | Plain statement ("높일 수 있다" → "높인다") |
| A-11 | Overused "~을 위해" purpose clauses | S2 | "~려고", "~위한" |
| A-15 | Abstract subject + all-purpose verb, literal causative or cognitive verbs | S2 | Concrete subject; split "suggest/show" into "~에 따르면 ~이다" |
| A-16 | "그/그녀/그것/그들" 3+ times in a paragraph | S1 | Drop the subject in most cases, or use a title or noun phrase (김도훈 2009) |
| A-17 | Overused plural "~들" | S2 | Drop when context shows the plural ("개발자들이" → "개발자가") |
| A-18 | 3+ words of left-branching modifier before a noun | S2 | Split the sentence or move the description after the noun (박옥수 2018) |
| A-19 | Stacked particles "~에서의/~으로의/~에의/~으로부터의" | S2 | Rewrite as a clause or phrase (김정우 2007) |

### B. Excess English

| ID | Pattern | Severity | Fix |
| --- | --- | --- | --- |
| B-1 | Korean + parenthetical English every time | S2 | Gloss at first mention only |
| B-2 | Translatable English left as is | S2 | Translate; keep standard abbreviations |

### C. Structural patterns

| ID | Pattern | Severity | Fix |
| --- | --- | --- | --- |
| C-5 | Emoji overuse | S1 | Remove all in columns and reports |
| C-7 | "먼저·반면·결국" formula, rule of three | S2 | Cut to one or two connectives or fold into the prose |
| C-8 | Repeated "A인가, B인가" pairs | S2 | Keep one; make the rest plain statements |
| C-9 | Numbered parentheses "(1)·(2)·(3)" | S2 | Fold into the prose or use plain line breaks |
| C-10 | Repeated "X: Y" subtitle headings | S1 | Short or declarative headings |
| C-11 | Comma right after -고/-며/-지만/-아서 | S1 | Remove the comma; 6+ is a strong signal |

### D. Signature phrases

| ID | Pattern | Severity | Fix |
| --- | --- | --- | --- |
| D-1 | Summary pivots "결론적으로/따라서/이를 통해/요약하면" | S1 | Beyond 3, keep 1–2 as other endings, delete the rest |
| D-2 | "시사하는 바가 크다/주목할 만하다" | S1 | Delete or give a concrete conclusion |
| D-3 | "본질적으로/핵심적으로" | S1 | Delete |
| D-4 | Hype words (파격적, 압도적, 획기적, 다채로운, 진정한, 자리매김) 3+ times | S1 | Concrete figures and facts |
| D-5 | Personified abstract subjects ("기술이 묻는다") | S1 | A person or organization as subject |
| D-6 | Closing formulas "~할 때다/~해야 한다/지금이야말로", vague upbeat endings | S1 | End plainly or delete |
| D-7 | Repeated "X에서 Y로" transformation formula | S2 | Once; describe the rest plainly |
| D-8 | Inflated significance (이정표, 산물, 새 지평, 상징) | S1 | Concrete facts |
| D-9 | Unsourced authority (전문가들은, ~로 알려져 있다) | S2 | Name the source or delete |

### E. Rhythm and endings

| ID | Pattern | Severity | Fix |
| --- | --- | --- | --- |
| E-1 | Uniform sentence length | S2 | Mix short and long sentences |
| E-2 | "~다" 4 sentences in a row, default "~고 있다" | S2 | Vary endings; use the simple tense |
| E-7 | Inconsistent speech level (dialogue and spoken text only) | S2 | One speech level per paragraph (김혜영 2019) |

### F. Modification and repetition

| ID | Pattern | Severity | Fix |
| --- | --- | --- | --- |
| F-1 | Synonym cycling (주인공 → 캐릭터 → 인물 → 그) | S2 | One name |
| F-2 | False ranges "A에서 B까지", negative parallels "단순한 X가 아니라 Y" | S2 | Plain statement |
| F-4 | -성/-적/-화 plus -tion/-ment stacked 12+ times | S2 | Verb and adjective roots |
| F-5 | "~적 N" chains ("전략적 함의·실천적 기반") | S2 | Noun + noun or spell it out |

### G. Hedging

| ID | Pattern | Severity | Fix |
| --- | --- | --- | --- |
| G-1 | Overused future assertions "~것이다/~할 것이다" | S2 | Present or definite form |
| G-2 | Overused guesses "~로 보인다/~인 듯하다" | S2 | State plainly where possible |
| G-3 | Safe balancing "장점도 있지만/신중하게/균형" 4+ times | S2 | Keep 1–2 as the writer's position |
| G-4 | Knowledge-limit hedges ("공개된 정보가 제한적이지만") | S2 | Say it is not in the source, or delete |

### H. Connectives

| ID | Pattern | Severity | Fix |
| --- | --- | --- | --- |
| H-1 | Sentence-initial "또한·따라서·즉·나아가·게다가" 5+ times | S1 | Remove most; let sentences carry the flow |
| H-3 | Meta openers "이는·이 점에서·이 관점에서" 3+ times | S1 | Fold into the prose or delete |
| H-4 | Overused "즉" | S2 | Once at most |

### I. Formal and dependent nouns

| ID | Pattern | Severity | Fix |
| --- | --- | --- | --- |
| I-1 | "~인 것이다/~한 것이다" endings, authoritative essence framing | S1 | Plain ending |
| I-2 | "X은 ~라는 점에 있다" | S2 | Direct "X는 ~다" |
| I-3 | "~다는 뜻이다/~다는 의미다" endings | S2 | Spell it out in the prose |
| I-4 | Preachy "~해야 한다·~할 필요가 있다", repeated previews | S2 | Plain statements; delete previews |

### J. Visual decoration

| ID | Pattern | Severity | Fix |
| --- | --- | --- | --- |
| J-1 | Bold overuse, bullets with bold labels | S2 | Prose in columns and reports |
| J-2 | Em dash (—), en dash (–), quotes for emphasis 5+ times, curly quotes, tildes | S1 (dashes) | Remove dashes (periods, commas, parentheses); keep one or two emphases |
| J-3 | Bullet lists in columns and reports | S2 | Prose paragraphs |

### K. Chatbot leftovers

| ID | Pattern | Severity | Fix |
| --- | --- | --- | --- |
| K-1 | Chatbot replies ("좋은 질문이에요!", "도움이 되었으면") | S1 | Delete entirely |
| K-2 | Flattery and excess politeness ("정말 훌륭한 지적이세요!") | S1 | Delete; keep the substance |
