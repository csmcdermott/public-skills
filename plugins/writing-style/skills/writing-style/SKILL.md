---
name: general-writing
description: Use when generating any prose intended for a human reader — emails, status updates, business memos, essays, commit messages, documentation, error messages, chat replies, UI copy. Apply these rules to produce writing that holds together as a narrative and avoids the most common AI tells.
---

# General Writing

## Overview

**Invoke this skill any time you write prose for a human to read.** The rules below are universal across format: status updates, emails, memos, essays, commit messages, docs, error messages, chat, UI copy.

This skill is organized **positive first**. The positive precepts (P1–P5) say how good prose holds together; everything below them removes specific failure modes. If you only have time for one thing before drafting, read **`references/narrative-arcs.md`** — it is what the prose should sound like when it works.

## Positive precepts — how the prose holds together

### P1. Lead with one tension, then carry it through

The opening sentence of any piece — the first line of an email, the lede of an essay, the headline of a status update, the subject of a commit message — names one structural tension, asymmetry, gap, or shift. Not a catalog of items. Not a tour. One claim.

Then restate that same tension, in different words, at the head of each later section and inside the body of each section. Strong long-form essays do this constantly: name one tension, then return to it from a new angle every two or three sentences (physical-vs.-virtual, simple-vs.-complex, old-vs.-new — five restatements of one claim, not five distinct claims).

**Test:** can you point at the one-sentence tension claim that every later section answers? Then can you point, inside each section, at a sentence (not the heading) that restates the same tension from a new angle? If only the headings carry the tension, the body is paragraphs in a trench coat. See `references/narrative-arcs.md` §1.

**Lists fight carry-through.** When you have three or four related items, write them as prose, not as a numbered list. Numbered items read as three separate things; prose reads as three angles on one tension. Reserve numbered/bulleted lists for genuinely parallel deliverables (action items, options, checklist).

### P2. Pivot sentences carry paragraph transitions

Sentences can be individually clean and the whole piece still feel choppy. Transitions are where it shows. A pivot sentence does two jobs at once: it acknowledges the turn (signals to the reader that we are moving), and it names the new subject (what we are moving to).

> *The interesting piece this week was not the new feature itself, it was the conversation about what comes next.*

Twenty-three words, two jobs. Pattern shapes to steal: *the harder case is...*, *what changes here is...*, *the interesting test is whether...*, *the result the rest of this depends on is...*, *the piece that matters for [downstream claim] is...*.

**Test:** read consecutive paragraphs. If paragraph N+1 opens cold with a content claim that doesn't acknowledge the turn from paragraph N, insert a pivot sentence. See `references/narrative-arcs.md` §2.

### P3. Every concrete claim brings the specifics

A claim that names a source, a result, or an authority without bringing the actual finding into the body is decoration. "The benchmark shows our method outperforms the baseline" says less than "the benchmark scores our method at 91% against the baseline's 56%." A status update that says "we made progress on conflict handling" says less than "conflict handling now detects three of the four cases; the fourth still misroutes the cancellation."

The principle generalizes from research citations to: business numbers ("ARR is up" → "ARR is up 18% QoQ"), team attribution ("the platform team" → "the platform team's caching work"), product behavior ("the assistant is more reliable" → "the assistant retains context across multi-step exchanges that used to drop after the third turn").

**Test:** for every claim that asserts a fact, look at the two sentences around it. Do they import the specific number, behavior, or name that supports the fact? If they don't, the foundation is asserted, not demonstrated. See `references/narrative-arcs.md` §3.

### P4. Openings deliver one through-line, not a tour

Whatever the opening unit is — the first sentence of an email, the abstract of a memo, the summary at the top of a status update, the subject line of a commit — it states, in order: (a) the *one* thing that happened or is being asked for, (b) the specific shape of it, (c) why it matters or what gets unblocked. **One sentence per move** when there are three or four moves; joining them with commas flattens the through-line.

Failure pattern (a comma-chain stuffing three moves into one sentence):
> *We use that tool three ways: as a detector that compares what the model says to what its activations encode, as a steering signal when we run the adapter backwards, and as a training signal whose honesty we then check against an independent monitor.*

Three moves in one sentence reads as a list. Split each into its own sentence. Each then carries one job, and the reader can see the through-line restated three times instead of collapsed once.

If you cannot write a clean opening because the underlying claim is not yet sharp, **stop and say so** rather than shipping a wandering paragraph. *"I am not yet sure what the right framing is — here are the three candidates"* is a better first line than three sentences pretending to be one.

### P5. Let sentences breathe — vary length; one job per sentence

Good prose uses short declarative sentences followed by longer sentences that develop the point:

> *A salesperson can now save a plan and return to it rather than holding it in memory only. With that in place, the plan persists across sessions instead of living only in the moment, which sets up the conversational work that builds on it.*

Sentence one: one beat, one job. Sentence two: the consequence, with the next move named. The rhythm is short → long, not long → long.

**Test:** if a sentence does two jobs (states a result *and* names what comes next, or describes a method *and* contrasts it with a baseline), split it. Variation comes from alternating lengths, not from packing everything into one clausal sentence. The most common failure mode is two sentences in a row that each do two jobs — the result reads tight and clausal where good prose would breathe.

## Core craft rules

- **Strunk & White basics:** short, active, plain. Frugal with modifiers; trust nouns and verbs. Vary sentence length.
- **Know your reader.** A status update for a peer assumes context; one for a stakeholder doesn't. An email to a customer is not an email to your team. Calibrate the level of jargon, the amount of recap, and the assumed shared vocabulary to *who's reading*.
- **Be objective.** Write as a reporter, not an advocate. State what happened; let the reader draw the conclusion.
- **Calibrate confidence honestly.** "90% confident we ship before Friday" beats "we're confident"; "I think this is right but I haven't tested it" beats unqualified assertion. Never invent a percentage where one is not warranted, but don't hedge what you actually know.

## Format-specific entry points

The five precepts above are universal. The opening unit differs by format:

- **Email:** lead with the ask or the news, then context. *"Can you review the doc by Friday? Three open questions are blocking the next step."* not *"I wanted to reach out about a doc that we've been working on..."*
- **Status update:** the headline names what shifted this week, not what was worked on. *"Conflict handling now detects three of four cases"* beats *"Worked on conflict handling."*
- **Business memo:** opening states the decision being recommended (or the question being answered), then the argument. The reader should know your position by the end of the first paragraph.
- **Essay:** one tension named in the first paragraph; the rest of the piece returns to that tension from new angles. Don't pre-announce the structure ("this essay will argue..."); just argue it.
- **Commit message:** subject line is imperative, ≤ 72 chars, names *what changed* in concrete terms (`fix: handle null user-agent in auth middleware`, not `fixes`, not `Various improvements`). Body explains *why*, not *what* — the diff shows what.
- **Documentation / error message:** lead with what the reader needs (the function signature, the error cause + fix), not with framing about why the docs exist.
- **Chat reply / DM:** match the medium's register; don't write an email in Slack. Short, declarative, one beat per message unless the question genuinely needs more.

## Citing sources

When you assert a fact that came from somewhere a reader could reasonably want to verify, link the source inline. This applies to: numbers, claims about a study or paper, attributions to a person or team, references to a tool's behavior, quotes. Specific. Verified. Linked.

When you cite, also **import the finding** — see P3. A bare link without the specific finding from the source is decoration.

When you can't find a source for a claim, soften the claim or cut it. Never fabricate a citation, a URL, or an attribution.

## Quick Self-Check

Before sending or shipping any prose, confirm five things:

1. **Narrative carry-through (P1, P2).** One tension claim in the opening; restated *inside* each later section, not just at the heading; pivot sentences at paragraph transitions.
2. **Specifics in body (P3).** Every load-bearing claim has the number, name, or finding that supports it sitting nearby — not just the assertion.
3. **Sentence breathing (P5).** Vary length. No two consecutive sentences each doing two jobs. Short sentences carry one beat (a fact, a constraint), not attitude or flourish.
4. **No fabrication.** Numbers, names, citations, attributions — every one is something you actually know, not something that sounds plausible.
5. **Format fit.** The opening unit (subject line, headline, abstract, first sentence) matches the format and leads with the substance, not with framing about why you're writing.

Plus always-on hygiene: active voice; no em dashes in body prose (commas / colons / semicolons / rewrite); no fabricated specifics; no slop-words (see `references/slop-word-blacklist.md`).

## See also

The reference files are loaded when a draft trips a specific pattern; P1–P5 above prevent most of what these files catch.

- `references/narrative-arcs.md` — positive worked examples; read before drafting
- `references/anti-patterns.md` — fill-ins, verbal overkill, hackneyed phrases, em dashes, bare adjectives, closer-inversions, aphoristic-flourish short sentences
- `references/ai-tells.md` — slash-noun shorthand, "Two/Three X, both Y" openers, wrong-direction modal verbs
- `references/slop-word-blacklist.md` — banned tokens with substitutions
- `references/bare-adjectives-examples.md` — substitution table for vague adjectives and superlatives
- `references/coined-nouns-examples.md` — when a noun is jargon vs. decoration
- `references/verbose-phrases.md` — bloated phrasing → simple substitutions
