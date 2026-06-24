# Narrative Arcs — how it sounds when it works

This is the positive-example reference. The rest of the skill is bans. This file is what the good prose actually does: one tension, restated from new angles; pivot sentences at paragraph joins; specific evidence carrying the argument forward.

Read this *before* drafting, not after.

## 1. Carry-through inside a paragraph (long-form narrative essay)

A canonical opening from a well-known technology essay introduces two contemporaneous events (selling personal computers, and selling operating systems for them) and names a single tension: *the second was much weirder than the first.* The paragraph then returns to that tension from five angles in succession: a computer had physical reality (you could open the box and watch lights blink), while an OS arrived as a long string of ones and zeros with no tangible incarnation; even people who understood what an OS was treated it as an arcane engineering prodigy, like a breeder reactor or a spy plane, never something that could be "productized."

What's happening: one tension named (*operating systems are weirder to sell than computers*) and then the same claim restated from five angles inside one paragraph: physical box vs. no incarnation, lights blink vs. ones and zeroes, breeder reactor analogy, not productizable. The author does not state the tension once and move to method. The tension returns from a new angle every two or three sentences.

**Lesson:** the section paragraph should not be "topic sentence + supporting detail + supporting detail + closer". It should be "tension restated + first angle on the tension + second angle + third angle". The same claim returns from new angles.

## 2. The pivot sentence (weekly-update corpus)

> In the two weeks since the new engineer joined, the proposal stream has gone from nothing to a working end-to-end scaffold. A salesperson can open an Opportunity, see the list of existing proposals, start a new space-only proposal pulling in the held spaces and the event details, move through the builder, save as a draft, and generate the PDF for review.
>
> **The interesting piece this week was not the scaffold itself, it was the conversation about what comes next.** Proposal generation's hardest problem is not the document, it is the intelligence behind it: recommending packages, services, and add-ons that fit the event. ...

What's happening: paragraph 1 closes a topic (scaffold shipped). Paragraph 2 opens with one sentence that *names what shifted*: "not the scaffold itself, it was the conversation". The pivot does two things at once: it acknowledges the turn (signals to the reader that we are moving), and it names the new subject (what we are moving to). Twenty-three words.

**Pattern shapes to steal:**
- *The interesting piece of [X] was not [Y], it was [Z].*
- *The harder case is when [X].*
- *What changes here is [X].*
- *The result the rest of the [argument / piece / section] depends on is [X].*
- *The piece that matters for [downstream claim] is [X].*

**Lesson:** between any two body paragraphs, ask: does the second open by acknowledging the turn? If it opens cold with a method claim, insert a pivot.

### Pivot vs. recap — the failure mode

A pivot looks forward; a recap looks back. A sentence that summarizes what the previous paragraphs already said is a recap, not a pivot, and it is filler.

Failure pattern (a recap at the end of three sections that already said this):
> *The three sections answer the same question from three angles. Section 1 names the gap. Section 2 tries to close it without touching the weights. Section 3 tries to close it by touching the weights and asks whether closure is what we wanted.*

Each sentence after the first is restating the section that was just described. The reader does not need the recap.

Fixes (pick one):
- **Forecast at the head:** move the summary up so it sets expectations before the three sections, not after.
- **Cut entirely:** if the sections already carry the through-line (per P1), the summary is redundant.

**Test:** does the sentence name what shifts (forward-looking, pivot) or restate what just happened (backward-looking, recap)? Keep the first, cut the second.

## 3. Importing the specifics, not just the assertion

A strong piece extending or referencing prior work does not say "we have a strong result and propose to extend it" or "the team has been making progress." It imports the specifics:

> the adapter reads out the unstated intermediate step of a two-hop question in 91% of cases against 56% untrained, and names the topic encoded in an activation 94% of the time against 1% untrained.

What's happening: the prior result is named with a number, a baseline, and the scope, *before* the downstream claim rests on it. The reader doesn't have to take the writer's word for the foundation; they can see it.

The same move applies outside research writing. Business updates:

> *"Renewals are up"* → *"Renewals are up 18% QoQ, driven mostly by enterprise; mid-market is flat."*

Status updates:

> *"The assistant is more reliable"* → *"The assistant now retains context across multi-step exchanges that used to drop after the third turn."*

**Lesson:** every "we made progress on X" or "the source supports Y" sentence is followed within two sentences by one concrete specific: a number, a measured behavior, a named finding, a quote. Assertion without the specifics is decoration.

## 4. Carry-through across sections (the structural move)

When a piece has three sections, three updates, three arguments, each should read as another angle on the same opening tension, not as three parallel summaries.

If the opening tension is *"the output says one thing but the internal state says another"*, then:

- Section 1 isn't *"we built a thing"*. It is *"we measure the gap directly: read the internal state, compare to the output, flag where they diverge."* The tension returns inside the section.
- Section 2 isn't *"we steer the output"*. It is *"we run the same gap the other way: if the internal state holds the truth, push the output toward what it already encodes."* Same tension, different angle.
- Section 3 isn't *"we train against the signal"*. It is *"the hardest test of the gap is whether closing it produces honesty or only better hiding."* Same tension, sharpest angle.

**Test:** can you point at the one-sentence tension claim from the opening, then point inside each section at a sentence that restates the same tension from a new angle? If the only sentence carrying the tension in a section is the heading, the section is paragraphs in a trench coat.

## 5. The cut pass (P6 in practice)

Good prose is selected, not poured. The discipline is brutal cutting: an eight-page article goes to four, then to three; a finished piece loses ten percent and reads unharmed or better. The pass has three moves: start where the content starts, cut what is about you, then remove every word not doing work.

**Before** (a status update that warms up, narrates itself, and closes with a flourish):

> In today's fast-paced engineering environment, shipping reliably is more important than ever. I wanted to give a quick update on where things stand with the migration. After a lot of hard work and dedication from the whole team, I'm happy to report that we've made significant progress. The migration is now substantially complete, with the vast majority of tables moved over. There's still a bit of work remaining, but we're in a really good place. This is what raising the bar looks like.

**After** (start late, cut the preamble and the closer, green the rest):

> The migration is done except for two tables. We moved 38 of 40 last week; `orders` and `line_items` are blocked on the foreign-key rewrite, which lands Thursday.

What got cut and why: the first two sentences were generic windup and meta (start where the content starts); "hard work and dedication" and "significant progress" were bare claims with no specifics (P3); "substantially complete / vast majority / a bit of work / really good place" were all greened into two numbers; "This is what raising the bar looks like" was a closer that reframes instead of stating. Sixty-eight words to thirty-one, and the short version says more.

**Lesson:** the reader supplies the obvious. State the two numbers and the blocker; trust them to infer that two-of-forty remaining is a good place to be. You do not have to say it.
