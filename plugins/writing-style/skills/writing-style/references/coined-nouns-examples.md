# Coined Nouns — slop → plain substitutions, Tell test, coining discipline (loaded on demand)

Loaded when the writer is uncertain whether a noun is genuine terminology or decoration. The rule: a noun reading as technical jargon must be one of (1) established field terminology, (2) a name you are deliberately coining for a genuinely new concept and will define on first mention, or (3) plain English. Decorative nouns dressed as jargon are slop.

## Slop → plain substitution table

| Coined / vague noun (slop) | Plain replacement |
|---|---|
| "we built a **primitive** for X" | name the actual thing ("a deduplication step", "a retry wrapper") |
| "the **substrate** the assistant runs on" | "the base model the assistant runs on" |
| "tracked as a **primitive** rather than a feature" | "tracked as a building block rather than an emergent feature" |
| "the **mechanism** by which we route requests" | "how we route requests" |
| "this **paradigm** for handling errors" | "this approach to handling errors" |
| "the **fabric** of the team's collaboration" | name the actual practice ("our review cycle", "the way the team pairs on hard bugs") |
| "the **machinery** that drives the build" | "the build pipeline" or "the build script" |

Pattern: the coined noun is doing decorative work — it sounds technical or weighty but does not add information the plain English form would not carry. Substitute and the meaning is preserved; if not, the noun is doing genuine work and you may be in the deliberately-coining case.

## The Tell test

The noun's only job is to make the sentence sound more technical or more important. Substitute the plain word; if the sentence still says exactly what you meant, the plain word wins.

## When you do coin a term

The first mention defines the concept in one sentence ("a property we call **weight identity**: the adapter shares its weights with the base model"), and every subsequent mention uses the same coined name unchanged. Don't drift across "the property we call X" → "the X mechanism" → "X-based architecture" within a single piece. Pick one form, hold it.
