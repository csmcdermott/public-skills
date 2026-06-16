# Evidence Substitutions — bare adjectives, bare impact verbs, coined nouns

Loaded when the writer needs calibration on how a decorative term should be replaced with a name, number, or link. The catch rules stay in `anti-patterns.md`; this file holds the substitution tables and fix options.

## Bare adjectives — substitution table

| Bare adjective | Replace with |
|---|---|
| "leading company in the space" | name the company ("Stripe", "Anthropic") |
| "top university" | "Princeton" or whatever the actual school is |
| "prestigious venue" | "ICML 2026 (spotlight)" or the named venue |
| "substantial funding" | "$13.4M / 3 years" |
| "experienced team" | "ten engineers, six years average tenure" |
| "significant acceleration" | "from 4 hours to 18 minutes" |
| "strong track record" | three named outputs with links |
| "robust system" | name what it survives ("survives Postgres failover") |
| "scalable approach" | name the scale ("works at 10M rows; tested through 100M") |

Pattern: replace the adjective with a proper noun (name), a quantity (number), or a hyperlink to the artifact. If none of the three is available, cut the claim; the adjective alone is not evidence.

## Bare superlatives — fix options

Bare definite-article superlatives ("the strongest", "the most rigorous", "the best", "the leading") claim a top rank without naming the field. Fix options:

(a) name the comparison source ("the highest score on the X benchmark"),
(b) soften with "among" / "one of" while keeping the citation ("among the strongest results on the X benchmark"),
(c) cut the claim.

"The strongest X" with no benchmark attached reads as advertising copy.

## Bare impact verbs — fix options

Bare impact verbs ("advances the field", "demonstrates commitment", "unlocks investment", "lowers the entry cost", "accelerates progress", "enables the work") claim impact without naming the beneficiary, the metric, or the artifact that delivers it. Fix options:

(a) name the beneficiary and the mechanism ("releases the dataset, which other teams building deception detectors can use without rebuilding the labeling pipeline"),
(b) point at the concrete artifact / number ("the $700k of in-kind matching"),
(c) cut the claim.

The verbs are not forbidden; using them as a substitute for the anchored object they should govern is.

## Coined nouns — slop → plain substitution table

| Coined / vague noun (slop) | Plain replacement |
|---|---|
| "we built a **primitive** for X" | name the actual thing ("a deduplication step", "a retry wrapper") |
| "the **substrate** the assistant runs on" | "the base model the assistant runs on" |
| "tracked as a **primitive** rather than a feature" | "tracked as a building block rather than an emergent feature" |
| "the **mechanism** by which we route requests" | "how we route requests" |
| "this **paradigm** for handling errors" | "this approach to handling errors" |
| "the **fabric** of the team's collaboration" | name the actual practice ("our review cycle", "the way the team pairs on hard bugs") |
| "the **machinery** that drives the build" | "the build pipeline" or "the build script" |

Pattern: the coined noun is doing decorative work; it sounds technical or weighty but does not add information the plain English form would not carry. Substitute and the meaning is preserved; if not, the noun is doing genuine work and you may be in the deliberately-coining case.

## The Tell test (for coined nouns)

The noun's only job is to make the sentence sound more technical or more important. Substitute the plain word; if the sentence still says exactly what you meant, the plain word wins.

## When you do coin a term

The first mention defines the concept in one sentence ("a property we call **weight identity**: the adapter shares its weights with the base model"), and every subsequent mention uses the same coined name unchanged. Don't drift across "the property we call X" → "the X mechanism" → "X-based architecture" within a single piece. Pick one form, hold it.
