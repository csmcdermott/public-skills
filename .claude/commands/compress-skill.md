---
description: Ralph loop that shrinks a skill's total word count without losing effectiveness. Greedily proposes cuts, keeps any that leave every eval fixture passing, and git-reverts the rest. Args: <plugin/skill> [reps] [max-stall]. Default writing-style/writing-style, reps 2, max-stall 3.
allowed-tools: Bash, Agent, Read, Edit, Write
---

# Compress Skill

Reduce a skill to its irreducible core. The fixtures are the fitness function; `git` is the safety net. Each round proposes one coherent cut, verifies the whole eval suite still passes, and keeps the cut only if it does. Stop when several cuts in a row all regress: what remains is load-bearing.

Argument: `$ARGUMENTS` = `<plugin>/<skill>` `[reps]` `[max-stall]`. Defaults: `writing-style/writing-style`, `reps=2`, `max-stall=3`.

**Objective:** minimize total words across `SKILL.md` AND `references/*.md`. No relocation credit — moving text from SKILL.md into a reference does not count as a cut. Words must be genuinely removed.

**Constraint:** every behavior fixture must still pass after the cut, every rep.

## Preconditions

Run `git status --porcelain` for the skill directory. If it is dirty, stop and tell the user to commit or stash first — the loop relies on `git checkout` to revert, and that would clobber their uncommitted work. The loop commits each kept cut, so the working tree must start clean.

## Steps

**1. Baseline.** Record starting total word count (`wc -w SKILL.md references/*.md`). Run the full behavior suite once (see "Run the suite") to confirm the skill currently passes everything. Any fixture that fails at baseline is excluded from the constraint (it was already failing; note it, don't let it block cuts). Set `stall = 0`.

**2. Propose one cut.** Dispatch a **compressor subagent** (`subagent_type: general-purpose`, `description: Compress {skill} round {n}`):

  > You are tightening a skill document to its irreducible core. Read every file under {skill_dir} (SKILL.md and references/). Propose THE single highest-value reduction that removes the most words while changing no rule's meaning.
  >
  > Target, in priority order: (1) the same rule stated in more than one place — keep the strongest statement, cut the echoes; (2) verbose prose that a tighter sentence carries; (3) redundant or over-long examples — one crisp example beats three; (4) hedging and meta-commentary about the rules.
  >
  > Do NOT delete a unique rule, a unique example, or a distinction that appears only once, even if you think it minor. Do NOT move text into another file to make one file shorter — the goal is fewer total words. Do NOT touch YAML frontmatter.
  >
  > Apply the edit directly with your file tools. Then reply with ONLY: the files touched, the approx words removed, and one sentence on what redundancy you cut.

**3. Verify.** Re-run `wc -w`. If total did not drop, treat as a stall (revert is a no-op). Otherwise run the suite (reps per fixture). A cut is **safe** iff every behavior fixture passes every rep AND total words dropped.

**4. Keep or revert.**

- **Safe:** `git add -A {skill_dir} && git commit -m "compress {skill}: <one-line summary> (-NNN words)"`. Reset `stall = 0`.
- **Unsafe:** `git checkout -- {skill_dir}` to discard the cut. Increment `stall`. Record which fixture(s) regressed and what was cut — that content is load-bearing for those fixtures.

**5. Loop.** If `stall >= max-stall`, stop: the remaining text resisted `max-stall` consecutive cut attempts. Otherwise go to step 2. (To keep proposals fresh after a revert, tell the next compressor which region was just tried and reverted so it picks a different target.)

## Run the suite

For each behavior fixture (skip `known_bad_output` fixtures), `reps` times:

1. **Subject** (`general-purpose`): "Read {skill_dir}/SKILL.md and apply its rules. You may read references/ if it directs you to. Reply with the artifact ONLY." + the fixture `prompt`.
2. **Deterministic gate** (Bash): write the output to a temp file; `grep -n $'—'` for em dashes and `grep -niE` for any literal banned words named in that fixture's criteria. Any hit is a forced violation.
3. **Judge** (`general-purpose`, skill-blind, MUST NOT see the skill body): the strict-JSON rubric from `/draft-loop` step (c), using the fixture's `criteria`.

A rep passes iff the gate is clean AND the judge returns `pass: true`. Load fixtures with `python3 scripts/eval_skills.py <plugin> --emit-json`.

## Report

```
Compression: {start} -> {end} words ({pct}% smaller), {K} cuts kept, {S} reverted.
Kept cuts:
  - <summary> (-NNN)
Load-bearing (reverted because a fixture regressed):
  - <what was cut> -> regressed {fixture}
```

The "load-bearing" list is the valuable output: it maps which words are doing real work. Leave the skill on the last committed (passing) state.
