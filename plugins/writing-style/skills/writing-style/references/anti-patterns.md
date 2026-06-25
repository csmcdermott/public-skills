# Anti-Patterns — bans, with rewrite forms

SKILL.md carries the one-line index; this file carries the rules. Load when you suspect the draft has tripped one.

## Word-level bans

### Fill-Ins — use sparingly or cut

Words that pad without adding meaning: *also, as noted, at the same time, basically, essentially, indeed, in connection with, in this context, of course, on balance, on the other hand, significantly, that said, with reference to*.

The **"significant" trap:** "The decision is significant" says nothing; state *why* it matters. *Significantly* is almost always a fill-in: "a significantly larger force" → "a force 40% larger".

### Slop words — replace with plain English

Words that trigger an "AI smell" in human reading; they leak from thinking-partner conversations, brainstorm dumps, and prior drafts. Strip on the way out.

| Banned word | Plain substitution |
|---|---|
| **substrate** | the base / the underlying system / the activations / the platform |
| **machinery** | the system / the tool / the approach |
| **primitive** (bare noun for your own deliverable) | the tool / the method / the building block / name the actual thing |
| **deconfusion**, **deconfusing** | the clearer framing / clarifies / disambiguates |
| **scaffolding** (metaphor for "framework") | the framework / the structure / the supporting work |
| **structurally** (as filler: "structurally different") | drop it, or "fundamentally different" if you mean different in kind |
| **paradigm**, **paradigmatic** (used casually) | the approach / the kind / the model |
| **leverage** (verb meaning "use") | use / apply / draw on / build on |
| **modality** | the way / the format / the channel |

**Term-of-art exceptions (NOT slop):** *structurally isolates* / *structurally aligns* (modifying a specific verb to claim a real mechanism); domain uses ("paradigm shift" in a Kuhn citation; "leverage" in finance; "modality" in HCI). Real scaffolding (construction, biology) is fine.

### Verbose phrases — use the simple form

| Verbose | Simple |
|---|---|
| are in a position to | can |
| at that point in time | then |
| at the present time | now |
| due to the fact that | because |
| in the event that | if |
| in the near future | soon |
| it is highly likely that | probably |
| it is possible that | may |
| subsequent to | after |
| the majority of | most |
| the manner in which | how |
| whether or not | whether |

The list is not exhaustive; the principle is "prefer the simple form when meaning is preserved." Humans contract or drop these constructions; AI keeps them.

**Postposed *alone* / *by itself* limiting a verb:** when "X alone Y" means "only X Y", move the limiter to the front. "Detectors operate on outputs alone" → "detectors only operate on outputs". Keep the postposed form only when *alone* modifies a quantity ("three hours for setup alone").

### Hackneyed phrases — find fresh language

*a likely scenario, at the end of the day, bottom line, dire straits, far-reaching implications, hammer out a compromise, heightened tensions, in the weeds, low-hanging fruit, move the needle, viable alternatives, widely held perception*.

### Redundancies — trim the extra word

*consensus of opinion, current status, future prospects, past history, true facts, unexpected surprise, end result, free gift, advance planning, completely eliminate, basic fundamentals*.

### Subjective words — cut

*fortunately, unfortunately, naturally, hopefully, regretfully, regrettably, mercifully, interestingly, upbeat, downbeat*.

## Sentence-level patterns

### Fake analysis — cut entirely

*anything can happen*, *further developments are to be expected*, *it is not possible to predict*, *it is too early to tell*, *it remains to be seen*, *only the future will tell*.

### Empty connective sentences — cut and merge

"Three outcomes follow.", "Several considerations arise here.", "This warrants further discussion.", "Two factors are at play.", "It is worth noting that ..."

Each pre-announces structure the next sentence delivers. **Test:** if removing the sentence leaves the paragraph intact, it was filler. **Exception:** a connective adding real constraint, comparison, or ranking earns its place (e.g., "Three outcomes are on the critical path; only the first ships this quarter").

### Closer-inversions — end the sentence plainly

Sentences that end with constructions like *"itself the X the field needs"*, *"the thing the X is for"*, *"exactly the X the Y has to read through"*, or *"the same constraint that made it Y in the first place"* read as the writer reaching for a closer. The shape is a clever inversion that reframes the just-stated claim as significant by the act of restating it (*"treat obfuscation not as a reason to avoid the experiment but as the thing the experiment is for"*).

Good writers do this occasionally. LLMs trained on essays do it too often. **Rewrite:** state the substance plainly and end the sentence. If the inversion is doing real work (a tight contrast), keep at most one per page.

### Aphoristic-flourish short sentences — short is for one beat, not for attitude

Short declaratives are good when they carry one load-bearing beat. They are slop when they carry attitude: opinion, register-shift, or rhetorical flourish dressed up as a punchy line. This is the sibling failure mode to closer-inversion: when closers get suppressed, the same impulse migrates into pithy short sentences.

Slop examples:
- *"The numbers are what they are."* (cliché-closer; says nothing the surrounding sentences haven't said).
- *"A method many teams are quietly assuming is safe."* (rhetorical hedge in opinion-journalism register).
- *"The field has been mixing up two things."* (colloquial-pundit register).

Good short sentences (load-bearing, one beat):
- *"The model does not change. The adapter is small."*
- *"The detector reads the gap."*
- *"Tests passed. Deployed."*

**Test:** does the sentence carry one beat the reader needs (a fact, a measurement, a constraint, a state change)? Or does it carry attitude (a stance, a hedge, a reframe)? Keep the first; cut the second.

**Boundary cases.** Two short declaratives at the close of a paragraph look identical whether they earn their place or perform it. These sit on the line; the verdict comes from what is *in* the sentence, not its shape.

| Sentence | Verdict | Why |
|---|---|---|
| *"The review happened in the tracker. The bug shipped to production."* | Keep | Two facts (a process completed, an outcome reached) with a contrast the surrounding prose hasn't already drawn. |
| *"And everyone involved feels productive, which is the most expensive part."* | Cut | "Most expensive part" is a rhetorical reframe, not a measurement. No new fact. |
| *"The system is fast enough."* | Cut | "Enough" is a judgment masquerading as a fact. Replace with the measurement: *"The system handles 8k qps."* |
| *"The team has been busy."* | Cut | Vague gesture. Replace with the count: *"The team shipped four releases this week."* |
| *"It's not what you'd expect."* | Cut | Attitude reframe. State what it *is*, not what it surprises. |
| *"Tests passed. Deployed."* | Keep | Two state changes; no judgment, no reframe. |

### Rhetorical escalation — cut the reframe

"X isn't just Y, it's Z" inflates significance through false contrast ("*this isn't just an iterative improvement, it's a paradigm shift*"). State the claim directly.

### Restating the prompt before answering

The AI repeats the question or framing back to the reader before getting to the answer:

> *"You asked about the rollout timeline. The rollout timeline question is an important one, because ..."*

Get to the answer. The reader already knows what they asked. If genuine framing is needed (a constraint, a re-scoping, a clarification), name it specifically, in one sentence, not a paragraph.

### "It's worth noting" / "Important to mention" / "I'd like to highlight"

Pre-announces that the next sentence is important. The next sentence then has to live up to the announcement, and usually doesn't. Just say the thing.

### Over-balanced phrasing

"On one hand X, on the other hand Y" used when the writer has no actual position. Genuine ambivalence reads fine. Performative ambivalence (where the writer is hedging to seem fair) reads as wet. If you have a position, say it; if you don't, say *that*.

## AI tells

### Slash-noun shorthand

"Sales/marketing", "monitoring/steering", "this week/next week" reads as engineering-doc compression that humans don't use in prose. Write the conjunction: "Sales and marketing", "monitoring and steering", "this week and next." Reserve `X/Y` for actual either-or shorthand or established compounds ("on/off", "input/output").

### "Two/Three X, both/all Y" parallel-construction opener

Slop:
> *Two prongs, both using the same technique. The first prong addresses X: ... The second prong addresses Y: ...*

Pre-announces a dual structure, labels the two halves, then describes each. Human writers go directly to the first item.

**Rule:** no "Two/Three X, both/all Y" opener at the start of a paragraph, section, or after a bold inline label. Rewrite by dropping the announcement and going directly (*"First, we apply the technique to X ... Second, the same technique applies to Y ..."*), or by stating the unified method then listing applications (*"The technique applies in two settings. For X, ... For Y, ..."*).

### Three-item parallel-clause padding

"We will design, build, and deploy" / "robust, scalable, and reliable" / "improving X, Y, and Z": three-item lists glued together with commas, where each item is a near-synonym or the same idea three ways. If three items genuinely differ, name them on separate lines. If they don't, pick the one that carries the most signal and drop the others.

### AI-flavored meta-claims — state the substance directly

*Load-bearing* ("the 12-month timeline is load-bearing"), *non-trivial* used as a hedge, *crucially*, *the key insight is*, *the upshot*, *the through-line*. A reader hears "X is load-bearing" and asks "load-bearing of what?"; the writer is asserting X matters without explaining how. The rewrite always states the mechanism: "Without a 12-month timeline, [the specific consequence] happens."

### AI-coined parenthetical labels — replace with natural prepositional phrasing

Hyphen-compound modifiers used as standalone labels in parentheses or before a colon: ***scope-distinct***, ***budget-clean***, ***timeline-compatible***, ***outcome-aligned***. Natural English uses a preposition:

> *"(scope-distinct: inference-time steering rather than training-time)"* → *"(with distinct scope: inference-time steering rather than training-time)"*

**Test:** if the compound modifier sits before a colon (`X-Y: ...`) or is used as a predicative adjective (`is X-Y from Z`), rewrite with a preposition or just delete the compound.

## Word-misuse — qualifiers and directional verbs

### Qualifiers — handle with precision

Do NOT weaken conclusions backed by evidence (~~apparently~~, ~~evidently~~, ~~seemingly~~, ~~purportedly~~). Do NOT strengthen weak evidence (~~obviously~~, ~~undoubtedly~~, ~~clearly~~). Hedge what is genuinely uncertain ("I think", "probably", "we don't know yet"); don't hedge what you actually know.

### Directional verbs pointing the wrong way

A directional/modal verb (*requires, allows, prevents, enables, mandates, permits, forbids*) used where its semantic direction is backwards or unclear. Example flagged in review: "where licensing requires" used to mean "where licensing allows". The licensing doesn't *require* an action, it *allows* it. The sentence reads confidently but means the opposite of what the writer intended.

**Rule:** every directional/modal verb must point the right way for the claim. When in doubt, drop the verb and rewrite simply ("with permissive licensing" instead of "where licensing requires/allows ...").

## Bare adjectives posing as evidence

Every load-bearing claim is paired with a name, a number, or a URL.

**Bare superlatives:** "the strongest", "the most rigorous", "the best", "the leading". These claim a top rank without naming the field.

**Bare impact verbs:** "advances the field", "demonstrates commitment", "unlocks investment", "accelerates progress", "enables the work". These claim impact without naming the beneficiary or the artifact.

See `evidence-substitutions.md` for the substitution tables and fix options.

## Coined nouns posing as technical terms

A noun reading as technical jargon must be either (1) established field terminology, (2) a name you are deliberately coining (define on first mention, then reuse unchanged), or (3) plain English. Anything else is decoration. See `evidence-substitutions.md`.

## Punctuation — prefer simplicity

**Em dashes (—)** read as AI in body prose; prefer commas, colons, semicolons, or rewrite. Exceptions: em dashes inside titles or verbatim quotes are fine.

**Passive voice:** shun it; prefer active.

**Exclamation marks:** rarely appropriate; let the words carry weight.

## The five slop tells — phrase lists

SKILL.md names the five taxonomy categories; this is the catalog of tell-phrases. Each is a symptom of a precept being skipped, not a new rule.

**Generic** (could front any topic; no specifics). *In today's fast-paced world; in the world of X; it's more important than ever; whether you're a beginner or an expert; by leveraging best practices; take it to the next level; at the end of the day; as teams scale; X has never been more important.* Fix: cut the windup, open on the specific subject (P6), bring a number or name (P3).

**Pseudo-insight** (profound-sounding but content-free). *The key is to find balance; it's not about the destination; true growth comes from within; when you change the way you look at things; Something shifted.* The tells: a dramatic single-sentence reveal, a tautology presented as wisdom, a vague metaphor that doesn't clarify. Fix: state the concrete fact or cut the line (closer-inversion and aphoristic-flourish bans above).

**Fake authority** (claim without a source). *Studies have shown; experts agree; research suggests; the data speaks for itself; industry leaders recognize.* Fix: name the study, the expert, or the number, or drop the claim (P3, and bare-superlatives below).

**Wikipedia rehash** (definition posing as content). *X is defined as; X refers to the process of; X is a type of; in simple terms, X is; there are several types of X.* Fix: lead with what the reader needs from X, not its dictionary entry (P6).

**Wellness filler** (gentle advice that cannot be wrong). *Self-care isn't selfish; honor your journey; you are enough; set healthy boundaries; embrace your authentic self; rest is productive; protect your peace.* Fix: cut it. It carries no fact, no state change, no constraint.

## Clutter — the bracket test

The self-editing pass behind P6's "green the draft": put mental brackets around every component not doing useful work, then cut what's bracketed. Most first drafts shed ~50% without losing meaning or voice.

What to bracket:

- The preposition draped on a verb: *order up* → *order*, *free up* → *free*, *head up* → *head*, *face up to* → *face*.
- The adverb that repeats the verb: *smile happily*, *shout loudly*, *plan in advance*.
- The adjective stating a known fact: *tall skyscraper*, *personal opinion*, *end result*.
- The little qualifier that weakens: *a bit*, *sort of*, *in a sense*, *kind of*, *somewhat*.
- The euphemism that inflates: *experiencing* (for *having*), *utilize* (for *use*), *at this point in time* (for *now*), *in order to* (for *to*).
- The whole sentence that restates the previous one, or tells the reader what they can infer.

The discipline: read the sentence without the bracketed words. If the meaning survives, the words were clutter.
