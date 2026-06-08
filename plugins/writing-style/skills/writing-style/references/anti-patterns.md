# Anti-Patterns — bans, with rewrite forms

SKILL.md carries the one-line index; this file carries the rules. Load when you suspect the draft has tripped one.

## Fill-Ins — use sparingly or cut

Words that pad without adding meaning: *also, as noted, at the same time, basically, essentially, indeed, in connection with, in this context, of course, on balance, on the other hand, significantly, that said, with reference to*.

The **"significant" trap:** "The decision is significant" says nothing — state *why* it matters. *Significantly* is almost always a fill-in: "a significantly larger force" → "a force 40% larger".

## Verbal Overkill — replace with the simple form

"in the near future" → "soon"; "subsequent to" → "after"; "due to the fact that" → "because". Full table in `verbose-phrases.md`.

**Postposed *alone* / *by itself* limiting a verb:** when "X alone Y" means "only X Y", move the limiter to the front. "Detectors operate on outputs alone" → "detectors only operate on outputs". Keep the postposed form only when *alone* modifies a quantity ("three hours for setup alone").

## Fake Analysis — cut entirely

*Anything can happen*, *further developments are to be expected*, *it is not possible to predict*, *it is too early to tell*, *it remains to be seen*, *only the future will tell*.

## Empty Connective Sentences — cut and merge

"Three outcomes follow.", "Several considerations arise here.", "This warrants further discussion.", "Two factors are at play.", "It is worth noting that ..."

Each pre-announces structure the next sentence delivers. **Test:** if removing the sentence leaves the paragraph intact, it was filler. **Exception:** a connective adding real constraint, comparison, or ranking earns its place — e.g., "Three outcomes are on the critical path; only the first ships this quarter."

## Qualifiers — handle with precision

Do NOT weaken conclusions backed by evidence (~~apparently~~, ~~evidently~~, ~~seemingly~~, ~~purportedly~~). Do NOT strengthen weak evidence (~~obviously~~, ~~undoubtedly~~, ~~clearly~~). Hedge what is genuinely uncertain ("I think", "probably", "we don't know yet"); don't hedge what you actually know.

## Subjective Words — cut

*Fortunately, unfortunately, naturally, hopefully, regretfully, regrettably, mercifully, interestingly, upbeat, downbeat*.

## Hackneyed Phrases — find fresh language

*a likely scenario, at the end of the day, bottom line, dire straits, far-reaching implications, hammer out a compromise, heightened tensions, in the weeds, low-hanging fruit, move the needle, viable alternatives, widely held perception*.

## AI-flavored meta-claims — state the substance directly

*Load-bearing* ("the 12-month timeline is load-bearing"), *non-trivial* used as a hedge, *crucially*, *the key insight is*, *the upshot*, *the through-line*. A reader hears "X is load-bearing" and asks "load-bearing of what?" — the writer is asserting X matters without explaining how. The rewrite always states the mechanism: "Without a 12-month timeline, [the specific consequence] happens."

## AI-coined parenthetical labels — replace with natural prepositional phrasing

Hyphen-compound modifiers used as standalone labels in parentheses or before a colon: ***scope-distinct***, ***budget-clean***, ***timeline-compatible***, ***outcome-aligned***. Natural English uses a preposition:

> *"(scope-distinct: inference-time steering rather than training-time)"* → *"(with distinct scope: inference-time steering rather than training-time)"*

**Test:** if the compound modifier sits before a colon (`X-Y: ...`) or is used as a predicative adjective (`is X-Y from Z`), rewrite with a preposition or just delete the compound.

## Redundancies — trim the extra word

*consensus of opinion, current status, future prospects, past history, true facts, unexpected surprise, end result, free gift, advance planning, completely eliminate, basic fundamentals*.

## Closer-inversions — end the sentence plainly

Sentences that end with constructions like *"itself the X the field needs"*, *"the thing the X is for"*, *"exactly the X the Y has to read through"*, or *"the same constraint that made it Y in the first place"* read as the writer reaching for a closer. The shape is a clever inversion that reframes the just-stated claim as significant by the act of restating it.

Examples:
- *"treat obfuscation not as a reason to avoid the experiment but as the thing the experiment is for"*
- *"itself the finding the field needs"*
- *"exactly the structural asymmetry the detector has to read through"*

Good writers do this occasionally. LLMs trained on essays do it too often. **Rewrite:** state the substance plainly and end the sentence. If the inversion is doing real work (a tight contrast), keep at most one per page.

## Aphoristic-flourish short sentences — short is for one beat, not for attitude

Short declaratives are good when they carry one load-bearing beat. They are slop when they carry attitude — opinion, register-shift, or rhetorical flourish dressed up as a punchy line. This is the sibling failure mode to closer-inversion: when closers get suppressed, the same impulse migrates into pithy short sentences.

Slop examples:
- *"The numbers are what they are."* — cliché-closer; says nothing the surrounding sentences haven't said.
- *"A method many teams are quietly assuming is safe."* — rhetorical hedge in opinion-journalism register.
- *"The field has been mixing up two things."* — colloquial-pundit register.

Good short sentences (load-bearing, one beat):
- *"The model does not change. The adapter is small."*
- *"The detector reads the gap."*
- *"Tests passed. Deployed."*

**Test:** for every short declarative, ask — does it carry one beat the reader needs (a fact, a measurement, a constraint, a state change)? Or does it carry attitude (a stance, a hedge, a reframe)? Keep the first kind, cut the second.

## Rhetorical Escalation — cut the reframe

"X isn't just Y, it's Z" inflates significance through false contrast ("*this isn't just an iterative improvement, it's a paradigm shift*"). State the claim directly.

## Punctuation — prefer simplicity

**Em dashes (—)** read as AI in body prose; prefer commas, colons, semicolons, or rewrite. Exceptions: em dashes inside titles or verbatim quotes are fine. **Passive voice:** shun it; prefer active. **Exclamation marks:** rarely appropriate; let the words carry weight.

## Bare Adjectives Posing as Evidence — replace with a name, number, or link

Every load-bearing claim is paired with a name, a number, or a URL. **Bare superlatives:** "the strongest", "the most rigorous", "the best", "the leading" — claim a top rank without naming the field. **Bare impact verbs:** "advances the field", "demonstrates commitment", "unlocks investment", "accelerates progress", "enables the work" — claim impact without naming the beneficiary or the artifact. See `bare-adjectives-examples.md` for the substitution table.

## Coined Nouns Posing as Technical Terms — define or replace

A noun reading as technical jargon must be either established field terminology, a name you are deliberately coining (define on first mention, then reuse unchanged), or plain English. Anything else is decoration. See `coined-nouns-examples.md`.
