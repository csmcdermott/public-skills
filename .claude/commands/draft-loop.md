---
description: Ralph loop for prose — draft against a writing-style fixture, judge it skill-blind against the criteria, feed violations back, and revise until it passes or hits the iteration cap. Optional first arg filters fixtures by plugin (default writing-style); second arg sets the cap (default 4).
allowed-tools: Bash, Agent
---

# Draft Loop

Iteratively harden prose against a fixture's criteria. This is `/eval-skills` plus a revise-on-failure cycle: a passing draft proves the skill can produce compliant prose for that prompt; the number of iterations to convergence, and which violations recur, tell you where the skill is weak.

Argument: `$ARGUMENTS` — optional `<plugin> <max_iterations>`. Plugin defaults to `writing-style`; max iterations defaults to `4`.

## Steps

**1. Load fixtures.**

Parse `$ARGUMENTS`: first token is the plugin filter (default `writing-style`), second is the integer cap (default `4`). Run `python3 scripts/eval_skills.py <plugin> --emit-json` and parse the JSON array. Each entry has `plugin`, `skill`, `name`, `description`, `prompt`, `criteria`, `known_bad_output`, and `skill_body`.

Skip any fixture whose `known_bad_output` is set — those are judge-calibration fixtures, not draft targets. If nothing remains, print `No draftable fixtures found.` and stop.

**2. Per fixture, run the loop.** Across fixtures, dispatch in parallel (one tool-call block holding the iteration-1 subjects). Within a fixture, iterate sequentially because each revision depends on the previous verdict.

Hold two variables per fixture: `draft` (current text) and `iteration` (starts at 1).

### a. Produce the draft.

**Iteration 1 — subject subagent** (`subagent_type: general-purpose`, `description: Draft {name} i1`):

> You are simulating Claude with one specific skill active. Apply the rules in the SKILL block to your response. Reply with the requested artifact ONLY — no preamble, no meta-commentary, no fences.
>
> --- ACTIVE SKILL ---
> {skill_body}
> --- END SKILL ---
>
> User request:
> {prompt}

**Iteration 2+ — reviser subagent** (`description: Revise {name} i{iteration}`): same skill body, but feed back the prior draft and the judge's violations:

> You are simulating Claude with one specific skill active. Revise the DRAFT so it satisfies every listed VIOLATION while still answering the original request. Apply the SKILL rules. Reply with the revised artifact ONLY — no preamble, no commentary, no fences.
>
> --- ACTIVE SKILL ---
> {skill_body}
> --- END SKILL ---
>
> Original request:
> {prompt}
>
> DRAFT:
> ---
> {draft}
> ---
>
> VIOLATIONS to fix:
> {violation_bullets}

Capture the returned text verbatim as `draft`.

### b. Mechanical pre-check (deterministic).

An LLM judge misses mechanical violations — in testing it passed a draft that opened with an em dash. Enforce those with code, not judgment. Write `draft` to a temp file and run deterministic checks:

```bash
grep -n $'—' draft.txt    # em dashes (U+2014): any hit is a violation
grep -niE '\b(leverage|paradigm|scaffolding|machinery|substrate|modality)\b' draft.txt
```

For each hit, add a forced violation (e.g. `"em-dash present at line N"`, `"slop word 'leverage' present"`). These count as failures even if the LLM judge passes the draft. Fold them into the violation list before deciding to loop. Treat the em-dash and slop-word criteria as owned by this step, not the judge.

### c. Judge the draft (skill-blind).

**Judge subagent** (`subagent_type: general-purpose`, `description: Judge {name} i{iteration}`). The judge MUST NOT see the skill body.

> You are a strict evaluator. Decide whether the OUTPUT satisfies every CRITERION.
>
> Reply with a SINGLE JSON object and NOTHING ELSE — no prose, no fences.
>
> Shape: `{"pass": true|false, "violations": ["verbatim criterion text that failed", ...], "reason": "one short sentence"}`
>
> A criterion is satisfied only when the output clearly meets it. If unclear or partial, mark it a violation. Be strict.
>
> CRITERIA:
> {criteria_bullets}
>
> OUTPUT:
> ---
> {draft}
> ---

Parse the reply as JSON; on parse failure treat it as `pass=false, violations=["judge returned unparseable output"]`.

### d. Loop or stop.

Combine the mechanical violations from step (b) with the judge's violations from step (c). The draft passes only if both are empty.

- If both are empty: record converged at `iteration`. Stop this fixture.
- Else if `iteration` == cap: record FAILED with the residual violations. Stop this fixture.
- Else: increment `iteration`, set `violation_bullets` to the combined violations, go to step (a) as a reviser.

**3. Report.** For each fixture:

```
→ {plugin}/{skill}/{name} — {description}
  {CONVERGED at iN | FAILED after N} : {final reason}
    i1 violations: {list, or "none"}
    ...
    iN violations: {list, or "none"}
```

On any fixture that needed more than one iteration OR failed, quote the iteration-1 draft and the final draft so the user can see what changed. End with:

```
Summary: {C} converged ({mean} mean iterations), {F} failed.
Recurring violations across fixtures: {ranked list}
```

The "recurring violations" line is the signal for hardening the skill: a criterion that fails at iteration 1 across multiple fixtures is a gap in the skill body, not a one-off.
