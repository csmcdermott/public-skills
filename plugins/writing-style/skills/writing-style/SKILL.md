---
name: writing-style
description: Use when generating any prose intended for a human reader: emails, status updates, business memos, essays, commit messages, documentation, error messages, chat replies, UI copy.
---

# Writing Style

Apply this whenever you write prose for a human to read. The rules are universal across format; only the opening unit changes (see Format entry points).

The skill is **positive first**: precepts P1–P6 say how good prose holds together. Everything below them removes specific failure modes. If you read one thing before drafting, read `references/narrative-arcs.md`: it shows what the prose sounds like when it works.

## Quick reference

| Precept | Rule | Self-check |
|---|---|---|
| **P1. Carry one tension** | Open with one tension; restate it from a new angle in each section. | Point at one sentence per section that restates the opening tension. |
| **P2. Pivot sentences** | At each paragraph turn, name the move and the new subject in one sentence. | Does paragraph N+1 open by signaling movement, not cold? |
| **P3. Bring specifics** | Every load-bearing claim brings the number, name, or behavior behind it. | Is the evidence within two sentences of each assertion? |
| **P4. One through-line opener** | The opener names one thing, its shape, and why it matters; one sentence per move. | Did you chain three moves with commas? Split them. |
| **P5. Sentences breathe** | Vary length; one job per sentence; short before long. | Two sentences in a row each doing two jobs? Split one. |
| **P6. Cut to the signal** | Start where the content starts; cut what's about you; then green the draft. | Could you delete this sentence and lose nothing? Delete it. |

Plus always-on hygiene: active voice; no em dashes in body prose; calibrate confidence honestly; never fabricate numbers, names, or citations; no slop words (see `references/anti-patterns.md`).

## When NOT to use

- **Code-only output** (functions, JSON, YAML, configs) with no prose for a reader.
- **Machine-to-machine output:** logs, structured payloads, API responses.
- **Verbatim transcription:** quoting a person or document exactly; preserve the original voice.
- **Scratch drafts** the user explicitly asked for unfiltered.
- **One-token replies** ("yes", "ack", "done") where the rules add ceremony without value.

## Positive precepts

### P1. Lead with one tension, then carry it through

The opening sentence names one structural tension, asymmetry, gap, or shift. Not a catalog. One claim. Then restate that same tension, in different words, at the head of each later section and inside each section's body: name one tension, return to it from a new angle every two or three sentences (five restatements of one claim, not five distinct claims).

If only the headings carry the tension and the body opens cold, the body is paragraphs in a trench coat. See `references/narrative-arcs.md` §1.

**Lists fight carry-through.** Three or four related items written as a numbered list read as separate things; written as prose they read as angles on one tension. Reserve numbered/bulleted lists for genuinely parallel deliverables (action items, options, checklist).

### P2. Pivot sentences carry paragraph transitions

Clean sentences can still feel choppy, and transitions are where it shows. A pivot sentence does two jobs at once: it acknowledges the turn and names the new subject.

> *The interesting piece this week was not the new feature itself, it was the conversation about what comes next.*

Shapes to steal: *the harder case is…*, *what changes here is…*, *the result the rest of this depends on is…*. A pivot looks forward; a sentence that summarizes what was already said is a recap, and recaps are filler (see `references/narrative-arcs.md` §2). If paragraph N+1 opens cold with a content claim, insert a pivot.

### P3. Every concrete claim brings the specifics

A claim that names a source, result, or authority without bringing the actual finding into the body is decoration. *"The benchmark shows our method outperforms the baseline"* says less than *"the benchmark scores our method at 91% against the baseline's 56%."* The principle generalizes: *"ARR is up"* → *"ARR is up 18% QoQ"*; *"the platform team"* → *"the platform team's caching work."*

For every claim that asserts a fact, the two surrounding sentences should import the specific number, behavior, or name behind it. When the source is publicly verifiable, link it inline alongside the finding; a bare link without the finding is decoration, the finding without the link is unverifiable. Never fabricate a citation; if you can't find a source, soften the claim or cut it.

**Factual vs. illustrative specifics.** In factual writing every specific must be one you actually know. In rhetorical writing a composite case can stand in if the prose signals it (*"a representative case looks like…"*, *"consider a 400-line diff that…"*). A composite framed as a measurement (*"studies show 73%…"*) is still fabrication; framed as illustration, it is how essays work.

### P4. Openings deliver one through-line, not a tour

Whatever the opening unit, it states in order: (a) the *one* thing that happened or is asked for, (b) its specific shape, (c) why it matters or what it unblocks. **One sentence per move** when there are three or four moves; comma-chaining them flattens the through-line:

> *We use that tool three ways: as a detector that compares what the model says to what its activations encode, as a steering signal when we run the adapter backwards, and as a training signal whose honesty we check against an independent monitor.*

Three moves in one sentence read as a list. Split each into its own sentence so the through-line restates three times instead of collapsing once. If you can't write a clean opener because the claim isn't sharp yet, **say so**. *"I'm not yet sure what the right framing is; here are three candidates"* beats three sentences pretending to be one.

### P5. Let sentences breathe

Short declarative followed by a longer sentence that develops the point:

> *A salesperson can now save a plan and return to it rather than holding it in memory. With that in place, the plan persists across sessions instead of living only in the moment, which sets up the conversational work that builds on it.*

One beat, then the consequence with the next move named. If a sentence does two jobs (states a result *and* names what comes next), split it. The common failure is two sentences in a row each doing two jobs: the result reads tight and clausal where good prose would breathe.

### P6. Cut to the signal

Three subtractive moves. All of them also shrink the piece, which is usually an improvement:

- **Start where the content starts.** Drafts warm up with generalities that could front any piece (*"In today's fast-paced world"*, *"As teams scale"*, *"X has never been more important"*). Cut the windup; open on the specific subject. Zinsser's editor move: throw away the first paragraphs until you reach the sentence where a person is actually talking.
- **Cut what's about you, not the reader.** Drop preamble and meta (*"I wanted to reach out"*, *"Great question"*, *"As an AI"*). Trust the reader to supply the obvious: state the specifics and let them infer the rest instead of narrating every step (McPhee: *if you are prancing between subject and reader, get lost*).
- **Green the draft.** Once it reads as done, cut ~10–15% anyway. Mark every word not doing work: the preposition glued to a verb (*free up*), the adjective stating a known fact (*tall skyscraper*), the qualifier (*a bit*, *sort of*), the sentence that restates the last one. Remove it so no one would notice it was there.

**Test:** point at any sentence and name the fact, state change, or constraint it carries that the piece would lack without it. If the answer is "none," cut it. See `references/narrative-arcs.md` §5.

## The five slop tells

Named patterns from the slop taxonomy. Each is already caught by a precept; this is the fast self-check. Tell-phrases are in `references/anti-patterns.md`.

- **Generic:** opener or claim that could front any topic, no specifics → P3, P6.
- **Pseudo-insight:** profound-sounding but empty; dramatic one-line reveal; tautology as wisdom → closer-inversion and aphoristic-flourish bans.
- **Fake authority:** *"studies show"*, *"experts agree"* with no named source → P3.
- **Wikipedia rehash:** *"X is defined as…"*, a dictionary entry posing as content → P6.
- **Wellness filler:** therapy-speak that can't be wrong (*"self-care isn't selfish"*) → cut; it carries no fact.

## Core craft rules

- **Strunk & White basics:** short, active, plain. Frugal with modifiers; trust nouns and verbs.
- **Know your reader.** Calibrate jargon, recap, and assumed vocabulary to *who's reading*. A status update for a peer assumes context a stakeholder note can't.
- **Be objective.** Write as a reporter, not an advocate. State what happened; let the reader draw the conclusion. Where natural, write in the first person; it keeps the prose human.
- **Calibrate confidence honestly.** *"90% confident we ship before Friday"* beats *"we're confident"*; *"I think this is right but haven't tested it"* beats unqualified assertion. Don't invent a percentage, but don't hedge what you actually know.
- **Match length to genre.** A commit body is two or three sentences; a status update one to three short paragraphs; a chat reply one to three sentences. P5 varies length *within* the piece; this calibrates the *whole* piece. Long where short would do is its own AI tell.

## Format entry points

The precepts are universal; the opening unit differs by format.

- **Email:** lead with the ask or the news, then context. *"Can you review the doc by Friday? Three open questions block the next step."*
- **Status update:** the headline names what shifted, not what was worked on. *"Conflict handling now detects three of four cases"* beats *"Worked on conflict handling."*
- **Business memo:** open with the decision recommended or question answered; the reader should know your position by the end of the first paragraph.
- **Essay:** one tension in the first paragraph; return to it from new angles. Don't pre-announce structure (*"this essay will argue…"*); just argue it.
- **Commit message:** subject imperative, ≤72 chars, names *what changed* concretely (`fix: handle null user-agent in auth middleware`). Body explains *why*; the diff shows what.
- **Documentation / error message:** lead with what the reader needs (the signature, the cause + fix), not framing about why the docs exist.
- **Chat reply:** match the medium's register; don't write an email in Slack.

## Common mistakes

- **Forcing a pivot where paragraphs are genuinely independent.** P2 is for transitions inside one arc, not for stitching unrelated items into false continuity.
- **Over-specifying in chat replies.** P3 demands specifics for load-bearing claims in long-form work; a two-sentence Slack reply doesn't need a cited number per word.
- **Reading the skill, then writing the same draft.** If nothing changed after invoking the skill, you didn't apply it.

## Rationalization table

| Excuse | Reality |
|---|---|
| "This is a quick chat reply, the rules don't apply." | The format entry points cover chat. The rules are about register, not length. |
| "P3 doesn't apply, I don't have specifics on hand." | Soften the claim or cut it. Asserting without evidence is the failure P3 names. |
| "Em dashes are fine in technical writing." | They read as AI in any body prose. Use commas, colons, semicolons, or rewrite. |
| "I need the verbose phrase for clarity." | The simple form preserves meaning. "In the event that" was never clearer than "if." |
| "The reader expects the AI register." | The reader expects to understand on the first read. Slop slows comprehension. |
| "The stakeholder wants the date, not the detail." | Cutting the mechanism cuts P3 evidence. Lead with the date, then the one-sentence mechanism that makes it credible. |

## Red flags: STOP and re-read the relevant precept

- "Let me open with a tour; the reader can find the through-line."
- "I'll use a numbered list for these three related points."
- "It's worth noting that…" / "I'd like to highlight…" / "The key insight is…"
- "On one hand X, on the other hand Y" (when you have a position).
- "This isn't just X, it's Y."
- "We will design, build, and deploy…"
- A closing line that reframes rather than states (*"…which is what raising the bar looks like"*).

## See also

P1–P6 prevent most of what the references catch. Load one when a draft trips its pattern.

- `references/narrative-arcs.md`: positive worked examples for P1–P6; read before drafting.
- `references/anti-patterns.md`: every ban with rewrite forms (slop words, verbose phrases, AI tells, closer-inversions, the five slop-tell phrase lists, clutter/bracket test, punctuation).
- `references/evidence-substitutions.md`: substitution tables for bare adjectives, superlatives, impact verbs, and coined nouns.
