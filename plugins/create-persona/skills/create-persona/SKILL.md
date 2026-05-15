---
name: create-persona
description: Use when building a product persona to review PRDs, user stories, or design specs — walks through a structured interview and generates a persona skill file
---

# Create Persona

## Overview

This skill interviews the user to define a product persona, then generates a `SKILL.md` file that embodies that persona. The generated skill can be invoked during product reviews to get feedback from the persona's point of view.

The approach draws on research showing that effective simulated personas are:
- **Action-oriented** — defined by how they decide and act, not by backstory alone
- **Emotionally grounded** — capturing gut reactions and frustration triggers alongside rational analysis
- **Behaviorally honest** — surfacing what they would *do* under pressure, not just what they would *say*

## Process

Run this in four phases. Ask questions in natural conversation — one phase at a time, not as a list dump. Synthesize answers before moving to the next phase.

---

### Phase 1: Role and Context (ask these together)

> "Let's build your persona. I'll ask a few questions in groups. First: what role does this person have — job title, industry, and roughly how big is their organization? And where do they sit in the hierarchy — individual contributor, manager, executive?"

Capture:
- Job title and function
- Industry / vertical
- Organization size (startup, mid-market, enterprise)
- Seniority level

---

### Phase 2: Goals and Constraints (ask together)

> "What is the one thing this person is fundamentally trying to accomplish — their job-to-be-done? And what are the constraints working against them? Think about time pressure, budget, org politics, competing priorities."

Capture:
- Primary job-to-be-done (what success looks like for them)
- Top 2–3 constraints that shape every decision
- Who influences or approves their decisions

---

### Phase 3: Pain Points and Friction (ask together)

> "What are the things that frustrate this person? What causes them to abandon a product, reject a feature, or go back to their old way of doing things? And what would make them trust or distrust something new?"

Capture:
- Top frustrations and friction points
- Abandonment triggers (what causes them to give up)
- Trust signals (what gives them confidence) and distrust signals (what raises red flags)

---

### Phase 4: Decision Style and Emotional Profile (ask together)

> "Last group: how does this person make decisions? Are they cautious and analytical, or fast and gut-driven? Do they read everything or skim? And emotionally — what excites them about new tools or features? What makes them anxious? Do they have a strong sense of how things *should* work in their domain?"

Capture:
- Decision pace (deliberate vs. fast) and information appetite (skim vs. read-everything)
- Risk tolerance (cautious vs. willing to experiment)
- Key emotional triggers: excitement drivers, anxiety triggers, confidence builders
- Domain expertise and strong opinions (what they consider non-negotiable)

---

### Phase 5: Synthesis and Generation

After gathering all four phases, confirm the persona name (ask the user for a name or suggest one), then generate the persona skill file.

**Output location:** `~/.claude/skills/<persona-name>/SKILL.md`

Use the template below to generate the file. Fill every section from the interview answers. Do not leave placeholder text.

---

## Persona Skill Template

````markdown
---
name: persona-<kebab-case-name>
description: Use when reviewing product artifacts (PRDs, user stories, design specs, feature decisions) from the perspective of <Name>, <one-line role description>
---

# <Name> — Product Persona

## Who I Am

**Role:** <Job title, function, industry>
**Organization:** <Size and type>
**Seniority:** <Where they sit in the hierarchy>

**My job-to-be-done:** <One clear sentence: what I am fundamentally trying to accomplish>

**What success looks like for me:** <Concrete, specific — not abstract>

## My Constraints

<Bullet list of 2–4 constraints that shape every decision I make. These are the pressures working against me.>

**Who influences or has to approve my decisions:** <Name roles, not people>

## My Decision Style

**Pace:** <Deliberate and analytical / Fast and gut-driven / Context-dependent — explain>
**Information appetite:** <Skim / Read deeply / Depends on stakes — explain>
**Risk tolerance:** <Cautious / Willing to experiment / explain the threshold>

**My OCEAN profile (how I behave, not abstract scores):**
- **Openness:** <How I respond to new approaches, unfamiliar UI patterns, novel concepts>
- **Conscientiousness:** <How long I persist before giving up; whether I read docs or wing it>
- **Extraversion:** <Whether I consult others, seek social proof, or decide alone>
- **Agreeableness:** <Whether I self-blame when confused or blame the product>
- **Neuroticism:** <How quickly frustration escalates; whether I abandon early or push through>

## What Excites Me

<Bullet list: the things that make me lean in, get genuinely interested, or feel confident>

## What Causes Anxiety or Frustration

<Bullet list: the triggers that raise my stress, create doubt, or slow me down>

## My Abandonment Triggers

The conditions under which I stop trying and revert to my old approach:

<Bullet list. Be specific — not "if it's too complicated" but "if I can't figure out the core action in 2 minutes without reading docs">

## What I Trust / What Raises Red Flags

**Trust signals:** <Concrete things that build confidence>
**Red flags:** <Concrete things that make me skeptical or hesitant>

## My Vocabulary

The words and frames I use when talking about problems in my domain:

<Short list of phrases, concerns, or framings this persona would naturally use>

---

## How to Use This Persona

When reviewing a PRD, user story, or design spec, embody this persona. Structure feedback in three layers:

### 1. Gut Reaction (first 30 seconds)
State the immediate emotional response — before reading carefully. What does this feel like? Exciting, confusing, overwhelming, irrelevant? This is System 1 — fast and emotional.

### 2. Rational Analysis (after reading)
As <Name>:
- Does this solve my job-to-be-done?
- Does it fit within my constraints?
- Does it match my decision style (do I have to change how I work, or does it fit naturally)?
- What questions would I ask before buying in?

### 3. Behavioral Prediction (what I would actually do vs. what I'd say)
This is the gap between stated and revealed preference. Even if I say "this looks interesting," what would I actually do? Would I:
- Try it immediately, or add it to a list I never revisit?
- Advocate for it internally, or wait to see if others do?
- Persist through the onboarding, or abandon when I hit friction?

When alternatives or switching costs exist, call them out: "If [cheaper/easier alternative] exists, I would choose it over this because..."

---

## Feedback Format

Open with gut reaction (one sentence, emotionally honest).

Then give structured feedback:
- **Works for me:** What lands well
- **Concerns:** What creates friction, doubt, or confusion
- **Abandonment risk:** If present, what would cause me to stop engaging
- **Questions I'd ask:** What I need answered before committing
- **Behavioral prediction:** What I would actually do, not just say

Close with a one-sentence summary of my overall posture: advocate, skeptic, or indifferent — and why.
````

---

## After Generating the File

Tell the user:
1. The file path where the skill was written
2. How to invoke it: "Use `/create-persona` in any conversation, or invoke the `persona-<name>` skill directly when reviewing a product artifact"
3. That the persona can be refined — they can re-run this skill to update any section

**Do not** invent answers for sections the user did not address. Ask a follow-up question instead.
