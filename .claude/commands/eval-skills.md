---
description: Run behavioral evals against skill plugins, using subagents as subject and judge. Optional first arg filters to one plugin (e.g. `/eval-skills writing-style`).
allowed-tools: Bash, Agent
---

# Eval Skills

Run every behavioral-eval fixture under `plugins/<plugin>/skills/<skill>/evals/*.toml`. For each fixture, dispatch a subject subagent (skip if the fixture supplies a `known_bad_output`) and then a judge subagent that returns a structured verdict. Aggregate verdicts; report failures with the judge's reasoning.

Argument: `$ARGUMENTS` — optional plugin name to filter to (e.g. `writing-style`). Empty means run all fixtures.

## Steps

**1. Load fixtures.**

Run `python3 scripts/eval_skills.py $ARGUMENTS --emit-json` and parse the JSON array. Each entry has:

- `plugin`, `skill`, `name`, `description`, `path` — identifiers and the on-disk path.
- `prompt` — the user message to feed the subject.
- `criteria` — array of rubric items for the judge.
- `known_bad_output` — string or null. If non-null, skip the subject call; feed this text directly to the judge.
- `skill_body` — the SKILL.md body (frontmatter already stripped).

If the array is empty, print `No fixtures found.` and stop.

**2. Per fixture, run subject then judge.**

For each fixture, run these two subagents sequentially. Across fixtures, dispatch in parallel (one tool-call block holding multiple Agent calls) so subjects and judges run concurrently across the suite.

### Subject subagent (skip if `known_bad_output` is set)

- `subagent_type`: `general-purpose`
- `description`: `Subject: {plugin}/{skill}/{name}`
- `prompt` (verbatim, substituting `{skill_body}` and `{prompt}`):

  > You are simulating Claude with one specific skill active. Apply the rules in the SKILL block to your response. Reply with the requested artifact ONLY — no preamble, no meta-commentary, no explanation, no markdown fences around the artifact. Do not invoke any other skills.
  >
  > --- ACTIVE SKILL ---
  > {skill_body}
  > --- END SKILL ---
  >
  > User request:
  > {prompt}

- Capture the returned text verbatim as `subject_output`.

If `known_bad_output` is set, use that string as `subject_output` and skip the subject subagent.

### Judge subagent

- `subagent_type`: `general-purpose`
- `description`: `Judge: {plugin}/{skill}/{name}`
- `prompt` (verbatim, substituting `{criteria_bullets}` — one `- ` line per criterion — and `{subject_output}`):

  > You are a strict evaluator. Decide whether the OUTPUT below satisfies every CRITERION.
  >
  > Reply with a SINGLE JSON object and NOTHING ELSE — no prose before or after, no markdown code fences.
  >
  > Shape: `{"pass": true|false, "violations": ["verbatim criterion text that failed", ...], "reason": "one short sentence overall verdict"}`
  >
  > A criterion is satisfied only when the output clearly meets it. If unclear or partial, mark it a violation. Be strict.
  >
  > CRITERIA:
  > {criteria_bullets}
  >
  > OUTPUT:
  > ---
  > {subject_output}
  > ---

- Parse the agent's reply as JSON. If parsing fails, treat the verdict as `pass=false, reason="judge returned unparseable output"`.

The judge MUST NOT see the skill body. Do not include it in the judge prompt.

**3. Resolve verdicts.**

For each fixture:

- If `known_bad_output` is null: fixture passes iff judge said `pass: true`.
- If `known_bad_output` is set: fixture passes iff judge said `pass: false` (the rubric must catch the hand-written violations). If the judge passed a known-bad, mark the verdict `JUDGE CALIBRATION FAILED` — the rubric is too loose.

**4. Report.**

For each fixture, print:

```
→ {plugin}/{skill}/{name} — {description}
  {PASS|FAIL}: {reason}
    - {violation 1}
    - {violation 2}
```

Show violations only on FAIL. End with:

```
Summary: {N} passed, {M} failed.
```

Do not include the subject output in the report unless a fixture failed; on failure, include the subject output as a quoted block so the user can see what the subject actually produced.
