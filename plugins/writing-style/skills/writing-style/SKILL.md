---
name: writing-style
description: Use when generating any prose intended for a human reader: emails, status updates, business memos, essays, commit messages, documentation, error messages, chat replies, UI copy.
---

# Writing Style

Apply this whenever you write prose for a human to read. The rules are universal; only the opening unit changes by format (see Format entry points). The skill is **positive first**: precepts P1–P6 say how good prose holds together; the sections below remove specific failure modes. Read `references/narrative-arcs.md` before drafting; it shows what the prose sounds like when it works.

## Quick reference

| Precept | Rule | Self-check |
|---|---|---|
| **P1. Carry one tension** | Open with one tension; restate it from a new angle in each section. | Point at one sentence per section that restates the opening tension. |
| **P2. Pivot sentences** | At each paragraph turn, name the move and the new subject in one sentence. | Does paragraph N+1 open by signaling movement, not cold? |
| **P3. Bring specifics** | Every load-bearing claim brings the number, name, or behavior behind it. | Is the evidence within two sentences of each assertion? |
| **P4. One through-line opener** | The opener names one thing, its shape, and why it matters; one sentence per move. | Did you chain three moves with commas? Split them. |
| **P5. Sentences breathe** | Vary length; one job per sentence; short before long. | Two sentences in a row each doing two jobs? Split one. |
| **P6. Cut to the signal** | Start where the content starts; cut what's about you; then green the draft. | Could you delete this sentence and lose nothing? Delete it. |

Plus always-on hygiene: active voice; calibrate confidence honestly; never fabricate numbers, names, or citations; no slop words (see `references/anti-patterns.md`).

**Never put an em dash (—) in body prose.** It is the top AI tell. Use a comma or parentheses for an aside, a colon for a reveal, a period for a hard stop, or recast the sentence. Final pass before sending: search the text for `—` and delete every one.

## When NOT to use

- **Code-only output** (functions, JSON, YAML, configs) with no prose for a reader.
- **Machine-to-machine output:** logs, structured payloads, API responses.
- **Verbatim transcription:** quoting a person or document exactly; preserve the original voice.
- **Scratch drafts** the user explicitly asked for unfiltered.
- **One-token replies** ("yes", "ack", "done") where the rules add ceremony without value.

## Positive precepts

### P1. Lead with one tension, then carry it through

Name one structural tension, asymmetry, gap, or shift in the opening, not a catalog. Then restate it from a new angle at the head of each section and inside each section's body: five restatements of one claim, not five distinct claims. If only the headings carry the tension and the body opens cold, the body is paragraphs in a trench coat (`narrative-arcs.md` §1). **Lists fight carry-through:** three related items as a numbered list read as separate things; as prose they read as angles on one tension. Reserve lists for genuinely parallel deliverables.

### P2. Pivot sentences carry paragraph transitions

A pivot sentence acknowledges the turn and names the new subject at once:

> *The interesting piece this week was not the new feature itself, it was the conversation about what comes next.*

Shapes to steal: *the harder case is…*, *what changes here is…*, *the result the rest depends on is…*. A pivot looks forward; a sentence summarizing what was already said is a recap, which is filler (§2). If paragraph N+1 opens cold, insert a pivot.

### P3. Every concrete claim brings the specifics

A claim that names a source, result, or authority without the actual finding is decoration. *"The benchmark shows our method outperforms the baseline"* says less than *"…scores 91% against the baseline's 56%."* So does *"ARR is up"* against *"ARR is up 18% QoQ."* Within two sentences of any factual claim, import the number, behavior, or name behind it. Link a publicly verifiable source inline beside the finding; never fabricate a citation; if you can't find one, soften the claim or cut it.

**Factual vs. illustrative.** In factual writing every specific must be one you actually know. In rhetorical writing a composite can stand in if the prose signals it (*"a representative case looks like…"*, *"consider a 400-line diff that…"*). A composite framed as a measurement (*"studies show 73%…"*) is still fabrication.

### P4. Openings deliver one through-line, not a tour

The opening states, in order: (a) the *one* thing that happened or is asked for, (b) its shape, (c) why it matters. **One sentence per move**; comma-chaining three moves flattens the through-line:

> *We use that tool three ways: as a detector that compares what the model says to its activations, as a steering signal when we run the adapter backwards, and as a training signal whose honesty we check against a monitor.*

Split each move into its own sentence so the through-line restates three times instead of collapsing once. If the claim isn't sharp yet, **say so** rather than shipping a wandering paragraph.

### P5. Let sentences breathe

Short declarative, then a longer sentence that develops it:

> *A salesperson can now save a plan and return to it rather than holding it in memory. With that in place, the plan persists across sessions, which sets up the conversational work that builds on it.*

If a sentence does two jobs (states a result *and* names what comes next), split it. The common failure is two two-job sentences in a row, tight and clausal where good prose would breathe.

### P6. Cut to the signal

Three subtractive moves, all of which also shrink the piece:

- **Start where the content starts.** Cut the windup of generalities that could front any piece (*"In today's fast-paced world"*, *"As teams scale"*); open on the specific subject.
- **Cut what's about you.** Drop preamble and meta (*"I wanted to reach out"*, *"Great question"*, *"As an AI"*). Trust the reader to infer the obvious instead of narrating every step.
- **Green the draft.** Once it reads as done, cut ~10–15% anyway: the preposition glued to a verb (*free up*), the adjective stating a known fact (*tall skyscraper*), the qualifier (*a bit*), the sentence that restates the last one.

**Test:** name the fact, state change, or constraint each sentence carries that the piece would lack without it. If "none," cut it (§5).

## The five slop tells

Five named patterns of AI slop. Each is already caught by a precept; this is the fast self-check. Tell-phrases are in `references/anti-patterns.md`.

- **Generic:** opener or claim that could front any topic, no specifics → P3, P6.
- **Pseudo-insight:** profound-sounding but empty; dramatic one-line reveal; tautology as wisdom → closer-inversion and aphoristic-flourish bans.
- **Fake authority:** *"studies show"*, *"experts agree"* with no named source → P3.
- **Wikipedia rehash:** *"X is defined as…"*, a dictionary entry posing as content → P6.
- **Wellness filler:** therapy-speak that can't be wrong (*"self-care isn't selfish"*) → cut; it carries no fact.

## Core craft rules

- **Plain style:** short, active, plain; frugal with modifiers; trust nouns and verbs.
- **Know your reader.** Calibrate jargon, recap, and assumed vocabulary to who's reading.
- **Report or argue, but commit.** In status updates, news, and docs, report what happened and let the reader draw the conclusion. In essays, memos, and op-eds, take a position and say what you think; neutral both-sides hedging there reads as evasion. Write in the first person where natural, and don't write anything you wouldn't say aloud.
- **Calibrate confidence.** *"90% confident we ship before Friday"* beats *"we're confident."* Don't invent a percentage, but don't hedge what you actually know.
- **Match length to genre.** A commit body is two or three sentences; a chat reply one to three. P5 varies length within a piece; this calibrates the whole piece. Long where short would do is its own AI tell.

## Format entry points

The precepts are universal; the opening unit differs by format.

- **Email:** lead with the ask or the news, then context. *"Can you review the doc by Friday? Three open questions block the next step."*
- **Status update:** the headline names what shifted, not what was worked on. *"Conflict handling now detects three of four cases"* beats *"Worked on conflict handling."*
- **Business memo:** open with the decision recommended or question answered; the reader knows your position by the end of the first paragraph.
- **Essay:** one tension in the first paragraph; return to it from new angles. Don't pre-announce structure (*"this essay will argue…"*); just argue it.
- **Commit message:** subject imperative, ≤72 chars, names *what changed* concretely (`fix: handle null user-agent in auth middleware`). Body explains *why*; the diff shows what.
- **Documentation / error message:** lead with what the reader needs (the signature, the cause + fix), not framing about why the docs exist.
- **Chat reply:** match the medium's register; don't write an email in Slack. Answer first; don't restate the question.

## Pitfalls and red flags

These thoughts mean STOP and re-read the relevant precept:

- Opening with a tour instead of one through-line, or a numbered list for three related points (P1).
- Forcing a pivot between genuinely independent paragraphs; P2 is for one arc, not false continuity.
- "It's worth noting…" / "The key insight is…", or restating the prompt before answering.
- "On one hand X, on the other hand Y" when you have a position; "This isn't just X, it's Y."
- A closing line that reframes rather than states (*"…which is what raising the bar looks like"*).
- Reading the skill, then shipping the draft you'd have written anyway. If nothing changed, you didn't apply it.

False economies: over-specifying a two-sentence chat reply (P3 is for load-bearing claims in long-form); cutting confident assertions into hedge mush (P5 is about clausal density, not certainty); treating bullets as banned (lists are right for genuinely parallel items).

## See also

P1–P6 prevent most of what the references catch. Load one when a draft trips its pattern.

- `references/narrative-arcs.md`: positive worked examples for P1–P6; read before drafting.
- `references/anti-patterns.md`: every ban with rewrite forms (slop words, verbose phrases, AI tells, closer-inversions, the five slop-tell phrase lists, clutter/bracket test, punctuation).
- `references/evidence-substitutions.md`: substitution tables for bare adjectives, superlatives, impact verbs, and coined nouns.
