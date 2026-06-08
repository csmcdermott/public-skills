# Slop-Word Blacklist

A short list of words that trigger an "AI smell" in human reading even when defined inline. Strip on the way out — the words leak from AI-thinking-partner conversations, brainstorm dumps, and prior drafts, and the response should not carry them.

| Banned word | Why it reads as AI slop | Plain substitution |
|---|---|---|
| **substrate** (any use: "the substrate", "X substrate", "the substrate is silent") | LLM-coined framing that loads the word with conceptual baggage the reader has to unpack. Real distinction survives without the word. | the base / the underlying system / the activations / the platform |
| **machinery** (as in "the same machinery", "X machinery") | Reads as filler that adds weight without substance. | the system / the tool / the approach / the same technique |
| **primitive** (as a bare noun for your own deliverable: "we built a primitive for X", "the X primitive") | Sounds technical but adds nothing; "we built X" or naming X works better. | the tool / the method / the building block / name the actual thing |
| **deconfusion**, **deconfusing** | Coined fake-jargon; reviewers ask "is this really a word?" | the clearer framing / clarifies / disambiguates |
| **scaffolding** (as a metaphor for "framework" or "structure") | Reads as AI register. Real scaffolding (construction, biology) is fine. | the framework / the structure / the supporting work |
| **structurally** (as filler before an adjective: "structurally different", "structurally distinct", "structurally similar") | Adds no information. | drop the word, or "fundamentally different" if you mean "different in kind" |
| **paradigm**, **paradigmatic** (used casually) | Big-noun decoration; the plain "approach" or "kind" usually works. | the approach / the kind / the model |
| **leverage** (as a verb meaning "use") | Corporate-deck register. | use / apply / draw on / build on |
| **modality** (outside specific technical fields where it means something) | Often pads "way" or "format". | the way / the format / the channel |

**Established term-of-art exceptions (NOT slop):**

- **structurally isolates / structurally aligns / structurally separates** — `structurally` modifying a specific verb to claim a real mechanism. Different from the adjective-filler use above.
- Domain-specific technical uses of any of the above when they are the actual term (e.g., "paradigm shift" in a Kuhn citation; "leverage" in finance; "modality" in HCI).

**Test:** before sending, search the text for these tokens. Any hit needs a rewrite or a documented exception.

## "Two X, both Y" parallel construction

Slop:
> *Two prongs, both using the same technique. The first prong addresses X: ... The second prong addresses Y: ...*

Why it reads as AI-flavored: pre-announces a dual structure, labels the two halves, then describes each. Human writers go directly to the first item.

Rewrites:

(a) Drop the announcement, go directly:
> *First, we apply the technique to X ... Second, the same technique applies to Y ...*

(b) State the unified method, then list applications:
> *The technique applies in two settings. For X, ... For Y, ...*

(c) Just describe each on its own line, no preamble:
> ***Setting 1: X.*** ... ***Setting 2: Y.*** ...

**Rule:** no "Two/Three X, both/all Y" opener at the start of a paragraph, section, or after a bold inline label. Go directly into the first item.

## Word-misuse / confidently wrong verbs

Anti-pattern: a directional verb (*requires, allows, prevents, enables, mandates, permits, forbids*) used where its semantic direction is backwards or unclear.

Example flagged in review: "where licensing requires" used to mean "where licensing allows" — the licensing doesn't *require* an action, it *allows* it. The sentence reads confidently but means the opposite of what the writer intended.

**Rule:** every directional/modal verb must point the right way for the claim. When in doubt, drop the verb and rewrite simply ("with permissive licensing" instead of "where licensing requires/allows ...").
