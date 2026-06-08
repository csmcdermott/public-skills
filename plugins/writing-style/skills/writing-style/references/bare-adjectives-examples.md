# Bare adjectives — substitutions and fix options (loaded on demand)

Loaded when the writer needs calibration on how a bare adjective, bare superlative, or bare impact verb should be rewritten. The catch rule stays in SKILL.md; this file holds the substitution examples and the fix options.

## Adjective substitution table

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

Pattern: replace the adjective with a proper noun (name), a quantity (number), or a hyperlink to the artifact. If none of the three is available, cut the claim — the adjective alone is not evidence.

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

The verbs are not forbidden — using them as a substitute for the anchored object they should govern is.
