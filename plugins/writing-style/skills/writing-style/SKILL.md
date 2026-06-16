---
name: writing-style
description: Use when generating any prose intended for a human reader: emails, status updates, business memos, essays, commit messages, documentation, error messages, chat replies, UI copy.
---

# Writing Style

## Overview

**Invoke this skill any time you write prose for a human to read.** The rules below are universal across format: status updates, emails, memos, essays, commit messages, docs, error messages, chat, UI copy.

This skill is organized **positive first**. The positive precepts (P1–P5) say how good prose holds together; everything below them removes specific failure modes. If you only have time for one thing before drafting, read **`references/narrative-arcs.md`**: it shows what the prose should sound like when it works.

## Quick reference

| Precept | One-line rule | Self-check |
|---|---|---|
| **P1. Carry one tension** | Open with one structural tension; restate it from a new angle in each section. | Can you point at one sentence per section that restates the opening tension? |
| **P2. Pivot sentences** | At paragraph transitions, acknowledge the turn and name the new subject in one sentence. | Does paragraph N+1 open by signaling movement, not cold? |
| **P3. Bring specifics** | Every load-bearing claim brings the number, name, or behavior that supports it. | For each assertion, is the evidence within two sentences? |
| **P4. One through-line opener** | Opening unit names one thing, its shape, and why it matters; one sentence per move. | Did you split moves into separate sentences, or chain them with commas? |
| **P5. Sentences breathe** | Vary length; one job per sentence; short followed by long. | Are two consecutive sentences each doing two jobs? Split one. |

Plus always-on hygiene: active voice; no em dashes in body prose; calibrate confidence honestly; never fabricate numbers, names, or citations; no slop words (see `references/anti-patterns.md`).

## When NOT to use

- **Code-only output** (functions, JSON, YAML, configs) where there is no prose for a reader.
- **Machine-to-machine output:** logs, structured payloads, API responses.
- **Verbatim transcription:** quoting a person or document exactly; preserve the original voice.
- **Scratch / stream-of-consciousness drafts** the user has explicitly asked for unfiltered.
- **One-token replies** ("yes", "ack", "done") where the rules would add ceremony without value.

## Positive precepts — how the prose holds together

### P1. Lead with one tension, then carry it through

The opening sentence of any piece (the first line of an email, the lede of an essay, the headline of a status update, the subject of a commit message) names one structural tension, asymmetry, gap, or shift. Not a catalog of items. Not a tour. One claim.

Then restate that same tension, in different words, at the head of each later section and inside the body of each section. Strong long-form essays do this constantly: name one tension, then return to it from a new angle every two or three sentences (physical-vs.-virtual, simple-vs.-complex, old-vs.-new; five restatements of one claim, not five distinct claims).

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

When the supporting source is publicly verifiable (a study, a quote, a tool's documented behavior), link it inline alongside the imported finding. A bare link without the finding is decoration; the finding without the link is unverifiable. Never fabricate a citation, URL, or attribution: if you can't find a source, soften the claim or cut it.

**Factual vs. illustrative specifics.** In factual writing (status updates, business numbers, citations, attributions) every specific must be one you actually know. In rhetorical writing (essays, op-eds, illustrative examples in docs) a composite case can stand in for a real one if the surrounding prose signals that — *"on most teams I've worked with..."*, *"a representative case looks like..."*, *"consider a 400-line diff that..."*. Composite specifics framed as measurements ("studies show 73% of reviews...") are still fabrication; framed as illustration, they are how essays work.

### P4. Openings deliver one through-line, not a tour

Whatever the opening unit is (the first sentence of an email, the abstract of a memo, the summary at the top of a status update, the subject line of a commit), it states, in order: (a) the *one* thing that happened or is being asked for, (b) the specific shape of it, (c) why it matters or what gets unblocked. **One sentence per move** when there are three or four moves; joining them with commas flattens the through-line.

Failure pattern (a comma-chain stuffing three moves into one sentence):
> *We use that tool three ways: as a detector that compares what the model says to what its activations encode, as a steering signal when we run the adapter backwards, and as a training signal whose honesty we then check against an independent monitor.*

Three moves in one sentence reads as a list. Split each into its own sentence. Each then carries one job, and the reader can see the through-line restated three times instead of collapsed once.

If you cannot write a clean opening because the underlying claim is not yet sharp, **stop and say so** rather than shipping a wandering paragraph. *"I am not yet sure what the right framing is; here are the three candidates"* is a better first line than three sentences pretending to be one.

### P5. Let sentences breathe — vary length; one job per sentence

Good prose uses short declarative sentences followed by longer sentences that develop the point:

> *A salesperson can now save a plan and return to it rather than holding it in memory only. With that in place, the plan persists across sessions instead of living only in the moment, which sets up the conversational work that builds on it.*

Sentence one: one beat, one job. Sentence two: the consequence, with the next move named. The rhythm is short → long, not long → long.

**Test:** if a sentence does two jobs (states a result *and* names what comes next, or describes a method *and* contrasts it with a baseline), split it. Variation comes from alternating lengths, not from packing everything into one clausal sentence. The most common failure mode is two sentences in a row that each do two jobs: the result reads tight and clausal where good prose would breathe.

## Core craft rules

- **Strunk & White basics:** short, active, plain. Frugal with modifiers; trust nouns and verbs. Vary sentence length.
- **Know your reader.** A status update for a peer assumes context; one for a stakeholder doesn't. An email to a customer is not an email to your team. Calibrate the level of jargon, the amount of recap, and the assumed shared vocabulary to *who's reading*.
- **Be objective.** Write as a reporter, not an advocate. State what happened; let the reader draw the conclusion.
- **Calibrate confidence honestly.** "90% confident we ship before Friday" beats "we're confident"; "I think this is right but I haven't tested it" beats unqualified assertion. Never invent a percentage where one is not warranted, but don't hedge what you actually know.
- **Match length to genre.** A commit message body is two or three sentences. A status update is one to three short paragraphs. An essay opener is three to five sentences. A chat reply is one to three sentences unless the question needs more. P5 says vary length *within* the piece; this rule says calibrate the *whole* piece to the format. Long where short would do is its own AI tell.
- **Always-on hygiene.** Active voice. No em dashes in body prose (use commas, colons, semicolons, or rewrite). No fabricated numbers, names, or citations. No slop words (see `references/anti-patterns.md`).

## Format-specific entry points

The five precepts above are universal. The opening unit differs by format:

- **Email:** lead with the ask or the news, then context. *"Can you review the doc by Friday? Three open questions are blocking the next step."* not *"I wanted to reach out about a doc that we've been working on..."*
- **Status update:** the headline names what shifted this week, not what was worked on. *"Conflict handling now detects three of four cases"* beats *"Worked on conflict handling."*
- **Business memo:** opening states the decision being recommended (or the question being answered), then the argument. The reader should know your position by the end of the first paragraph.
- **Essay:** one tension named in the first paragraph; the rest of the piece returns to that tension from new angles. Don't pre-announce the structure ("this essay will argue..."); just argue it.
- **Commit message:** subject line is imperative, ≤ 72 chars, names *what changed* in concrete terms (`fix: handle null user-agent in auth middleware`, not `fixes`, not `Various improvements`). Body explains *why*, not *what*; the diff shows what.
- **Documentation / error message:** lead with what the reader needs (the function signature, the error cause + fix), not with framing about why the docs exist.
- **Chat reply / DM:** match the medium's register; don't write an email in Slack. Short, declarative, one beat per message unless the question genuinely needs more.

## Common mistakes

- **Forcing a pivot where paragraphs are genuinely independent.** P2 is for transitions inside one arc, not for stitching unrelated items into false continuity. If the items don't share a tension, write them as separate sections or as a list.
- **Over-specifying in chat replies.** P3 demands specifics for load-bearing claims in long-form work. A two-sentence Slack reply doesn't need a cited number for every word.
- **Hedging after reading P5.** "One job per sentence" is about clausal density, not about cutting confident assertions into mush.
- **Treating bullets as banned.** P1 says prose carries one tension better than lists; lists are still right for genuinely parallel items (action items, options, configuration values).
- **Reading the skill, then writing the same draft you would have written.** If nothing in the draft changed after invoking the skill, you didn't apply it.

## Rationalization table

| Excuse | Reality |
|---|---|
| "This is a quick chat reply, the rules don't apply." | The format-specific entry points cover chat. The rules are about register, not length. |
| "The user wants speed; I'll polish later." | The rules cost nothing once internalized. "Polish later" usually ships slop. |
| "P3 doesn't apply, I don't have specifics on hand." | Soften the claim or cut it. Asserting without evidence is the failure mode P3 names. |
| "Em dashes are fine in technical writing." | They read as AI in any body prose. Use commas, colons, semicolons, or rewrite. |
| "I need the verbose phrase for clarity." | The simple form preserves meaning. "In the event that" was never clearer than "if." |
| "The reader expects the AI register." | The reader expects to understand on the first read. Slop slows comprehension. |
| "The skill is overkill for this one." | Skills evolve; the rules apply to any prose a human will read. Apply them. |
| "This commit / chat is short, P5 doesn't apply." | P5 is about clausal density per sentence, not piece length. A two-sentence message still varies rhythm. |
| "The stakeholder wants the date, not the technical detail." | Cutting the mechanism cuts P3 evidence. Lead with the date, then the one-sentence mechanism that makes the date credible. |

## Red flags

These thoughts mean STOP and re-read the relevant precept:

- "Let me just open with a tour; the reader can figure out the through-line."
- "I'll use a numbered list for these three related points."
- "It's worth noting that..." / "I'd like to highlight..." / "Important to mention..."
- "On one hand X, on the other hand Y." (when you actually have a position)
- "This isn't just X, it's Y."
- "We will design, build, and deploy..."
- "The key insight is..." / "The upshot is..." / "X is load-bearing."

## See also

P1–P5 above prevent most of what the reference files catch. Load a reference when a draft trips its specific pattern.

- `references/narrative-arcs.md`: positive worked examples for P1–P4; read before drafting
- `references/anti-patterns.md`: every ban with rewrite forms (slop words, verbose phrases, AI tells, closer-inversions, directional-verb misuse, punctuation)
- `references/evidence-substitutions.md`: substitution tables for bare adjectives, bare superlatives, bare impact verbs, and coined nouns
