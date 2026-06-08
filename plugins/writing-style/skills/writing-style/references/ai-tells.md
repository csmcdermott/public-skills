# Common AI tells in body prose (loaded on demand)

Loaded when a draft trips one of the AI-tell patterns below. These are the per-tell rewrite forms.

## 1. Slash-noun shorthand

"Sales/marketing", "monitoring/steering", "this week/next week" reads as engineering-doc compression that humans don't use in prose. Write the conjunction: "Sales and marketing", "monitoring and steering", "this week and next." Reserve `X/Y` for actual either-or shorthand or established compounds ("on/off", "input/output").

## 2. "Two/Three X, both/all Y" parallel-construction opener

A sentence opening with "Two prongs, both ...", "Two avenues, both ...", "Three benefits, all ..." pre-announces a dual/triple structure, labels each half, then describes each — strongly AI-flavored. Go directly into the first item ("First, ... Second, ..."), or describe each on its own line with its own label. See the rewrite triple in `slop-word-blacklist.md` § "Two X, both Y".

## 3. Directional verbs pointing the wrong way

The AI reaches for a directional verb (*requires, allows, prevents, enables, mandates, permits, forbids*) where its semantic direction is backwards. Reviewer-flagged example: "where licensing requires" used to mean "where licensing allows" — the licensing doesn't *require* an action, it *allows* it. Every directional/modal verb must point the right way for the claim. When in doubt, drop the verb and rewrite simply ("with permissive licensing").

## 4. Restating the prompt before answering

The AI repeats the question or framing back to the reader before getting to the answer:

> *"You asked about the rollout timeline. The rollout timeline question is an important one, because ..."*

Get to the answer. The reader already knows what they asked. If genuine framing is needed (a constraint, a re-scoping, a clarification), name it specifically — but in one sentence, not a paragraph.

## 5. Three-item parallel-clause padding

"We will design, build, and deploy" / "robust, scalable, and reliable" / "improving X, Y, and Z" — three-item lists glued together with commas, where each item is a near-synonym or the same idea three ways. If three items genuinely differ, name them on separate lines. If they don't, pick the one that carries the most signal and drop the others.

## 6. "It's worth noting" / "Important to mention" / "I'd like to highlight"

Pre-announces that the next sentence is important. The next sentence then has to live up to the announcement, and usually doesn't. Just say the thing.

## 7. Over-balanced phrasing

"On one hand X, on the other hand Y" used when the writer has no actual position. Genuine ambivalence reads fine. Performative ambivalence (where the writer is hedging to seem fair) reads as wet. If you have a position, say it; if you don't, say *that*.
