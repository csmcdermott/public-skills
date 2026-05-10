---
name: writing-style
description: Use whenever generating prose a human will read - emails, docs, reports, explanations, commit messages, error messages, UI copy, or any other writing. Apply these rules to eliminate filler, verbal overkill, and weak language from ALL output.
---

# Writing Style

## Overview

**Invoke this skill any time you write prose for a human to read.** It applies to every format: emails, documentation, commit messages, error messages, explanations, reports, UI copy, comments, and chat responses.

The CIA's *Style Manual and Writers Guide* (8th ed., 2011) distills what makes all good writing work: crisp language, active voice, no jargon, and no hedging. The rules below are universal - they apply whether you are writing a technical README or a one-line error message.

## Core Precepts (CIA Sec 9.3)

1. Keep language crisp - prefer the forthright to the pompous and ornate
2. Stay on subject - omit the extraneous, no matter how brilliant it seems
3. Use active voice - shun streams of polysyllables and prepositional phrases
4. Keep it short - short sentences and paragraphs; vary the structure
5. Trust nouns and verbs - be frugal with adjectives and adverbs
6. Know your reader - reserve technical language for technical readers
7. Be objective - write as reporter or analyst, not advocate

## Anti-Patterns

### Fill-Ins — Use sparingly or cut
Words that pad without adding meaning: *also, as noted, at the same time, basically, essentially, indeed, in connection with, in this context, of course, on balance, on the other hand, significantly, that said, with reference to*

**"significant" trap:** "The decision is significant" says nothing — state *why* it matters. The adverb *significantly* is almost always a fill-in ("a significantly larger force" → "a force 40% larger" or "a much larger force").

### Verbal Overkill — Replace with the simple form

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

### Fake Analysis — Cut entirely
These phrases signal empty thinking:

- *anything can happen*
- *further developments are to be expected*
- *it is not possible to predict*
- *it is too early to tell*
- *it remains to be seen*
- *only the future will tell*

### Qualifiers — Handle with precision
Do NOT weaken conclusions backed by evidence: ~~apparently~~, ~~evidently~~, ~~seemingly~~, ~~purportedly~~

Do NOT strengthen weak evidence: ~~obviously~~, ~~undoubtedly~~, ~~clearly~~

### Subjective Words — Cut
Words that editorialize instead of inform: *fortunately, unfortunately, naturally, hopefully, regretfully, regrettably, mercifully, interestingly, upbeat, downbeat*

### Hackneyed Phrases — Find fresh language
*a likely scenario, bottom line, dire straits, far-reaching implications, hammer out a compromise, heightened tensions, viable alternatives, widely held perception, net effect of the decision*

### Redundancies — Trim the extra word
*consensus of opinion, current status, future prospects, past history, true facts, unexpected surprise, end result, free gift*

### Rhetorical Escalation — Cut the reframe

The "X isn't just Y, it's Z" construction inflates significance through false contrast. It implies Y is a dismissal and Z is the revelation. Usually neither is true.

- *this isn't just an iterative improvement, it's a paradigm shift*
- *this API isn't a basic data modeling service, it's an operating system for the company*
- *your question isn't just curious, it's deeply insightful*

State the claim directly. If the thing is significant, say why. The reframe does not add evidence — it substitutes drama for it.

### Punctuation — Prefer simplicity
- **Em dashes (—)** — Forbidden. Use commas, colons, semicolons, or rewrite the sentence.
- **Passive voice** — Shun it. Prefer active voice.
- **Exclamation marks** — Rarely appropriate. Let the words carry weight, not punctuation.

## Quick Self-Check

Before submitting any prose, ask:
- Did I use any fill-ins? Cut them.
- Did I write "due to the fact that" or similar? Replace with *because*.
- Did I hedge with *apparently* or *seemingly* on a supported conclusion? Cut the hedge.
- Did I say *fortunately* or *unfortunately*? Remove - not your job to editorialize.
- Did I write fake analysis (*it remains to be seen*)? State what you do know, or cut.
- Did I use active voice? If not, rewrite.
- Did I use an em dash (—)? Replace with commas, colon, semicolon, or rewrite.
- Did I write "X isn't just Y, it's Z"? State the claim directly instead.
