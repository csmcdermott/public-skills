## Correction Log

<!-- Append a row every time the user corrects your approach.
     Be honest and specific — the point is to not repeat the mistake.
     Cap: 50 entries. Review before adding if at limit. -->

| Date | Context | What went wrong | Rule learned |
| --- | --- | --- | --- |
| 2026-06-24 | Refining writing-style from two books + a website | Left source attributions ("Zinsser", "McPhee", "slop taxonomy", "Strunk & White") in the skill body and references. User had to ask for their removal — they want only the takeaways in skill-facing content, not citations of the sources it was distilled from. | When distilling named external sources into a skill, strip attributions from SKILL.md and references by default. The skill reads as self-contained guidance; keep provenance in agent docs, commit messages, and memory only. Also gitignore copyrighted source material (the PDFs) rather than committing it to a public repo. |


## Patterns to Follow
<!-- Promoted from Correction Log after applying in a second session. Cap: 30. -->


## Anti-Patterns to Avoid
<!-- Promoted from Correction Log after applying in a second session. Cap: 30. -->


## Project-Specific Gotchas
<!-- One-off facts easy to forget: quirky build steps, non-obvious dependencies,
     environment requirements, ordering constraints. Cap: 50. -->

| Date | Gotcha |
| --- | --- |
| 2026-06-15 | **Personal skills in `~/.claude/skills/<name>/` shadow same-named plugin skills.** When iterating on a plugin skill, check whether a competing entry exists in the user's personal-scope directory; if so, plan to delete or rename it before testing. The skill registry shows both, and the personal one may take precedence in discovery. |
| 2026-06-15 | **SKILL.md frontmatter `name:` must match the directory name** for clean discovery. The system surfaces the skill as `<plugin>:<skill-name-from-frontmatter>`, so a mismatch (e.g. directory `writing-style/` with frontmatter `name: general-writing`) makes the skill hard to invoke and confuses search. |
| 2026-06-15 | **Skill `description:` fields should not summarize the skill's workflow or process.** Per superpowers:writing-skills, descriptions that summarize what the skill does create a shortcut Claude follows instead of reading the body. Keep descriptions to triggering conditions only ("Use when..."). |
| 2026-06-15 | **Verification subagents default to confirmatory tone.** When dispatching a subagent to test a skill or review work, explicitly ask for "RAW REACTIONS," "negative findings preferred," or self-caught rationalizations. Without that, the subagent's raw findings get buried under a polite executive summary. |
| 2026-06-24 | **Run a no-skill control before adding skill content.** When asked to harden writing-style against the slop taxonomy, the RED baseline showed the existing skill already prevented all five slop categories (Opus subjects reading the full SKILL.md), and even the no-skill control barely produced Wikipedia-rehash or wellness slop. Adding five taxonomy sections would have solved a non-problem and fought the brevity goal. Lesson: test what actually leaks before authoring; trim + a compact pointer beat new sections. |
| 2026-06-24 | **LLM judges miss mechanical violations; gate them deterministically.** In the draft-loop GREEN run, a judge passed a draft that opened with an em dash ("Team — Friday"). Mechanical bans (em dashes U+2014, literal slop words, word count) must be checked with `grep`/code, not an LLM rubric. The `/draft-loop` command now has a deterministic pre-check step that forces those violations regardless of the judge. |
| 2026-06-24 (refined 2026-06-26) | **In an eval-driven compression/edit loop, separate subject-simulation noise from real regressions before reverting a cut.** Subjects intermittently emit an em dash ("Team —"), passive voice, a 1-word over-count, or self-narration regardless of the cut. Decision procedure, sharpest first: (1) **Causal proximity** — did the cut touch guidance for the *failing criterion*? If not (e.g. an em-dash slip after a narrative-arcs cut), it is almost certainly noise. (2) **Majority-of-3**, never a single rep — a fixture that fails 1/3 passes; 2/3 fails. (3) If still ambiguous, `git stash` the cut and sample the SAME fixture on the committed state: if it fails at the same rate there, the fixture is *baseline-unstable* (exclude it from the constraint), not regressed by the cut. Only revert when the failure is causally plausible AND a majority of samples fail. Confirmed this session: fixture 07 fails the flourish criterion ~30% of the time even at the skill's best state, so its single failures are not regression signals. |
| 2026-06-26 | **writing-style: the aphoristic-flourish section of `references/anti-patterns.md` is load-bearing — do not compress it.** Cutting its keep/cut Test, boundary table, and examples regressed the essay-opener fixture (07), which then produced exactly the flourish endings it suppresses. Everything else compresses safely because it is restatement; this section is not. Leave it intact in future compression passes. |
| 2026-06-26 | **For a mechanical prompt rule that keeps getting violated (em dash, banned token, word cap), salience + a named substitute + an explicit final-pass scan beats a bare prohibition buried in a list.** The em-dash rule was the 2nd clause of a 7-item run-on and got slipped ~20% of the time; rewriting it as a standalone rule ("the top AI tell" + comma/parens/colon/period/recast + "final pass: search for `—` and delete every one") took the slip rate from 4/20 to 0/20. Validate any such change with a controlled *same-version* before/after batch (N reps on the prone fixtures), not scattered loop observations, and run a full-suite regression gate+judge. For a guaranteed zero, a deterministic post-process hook beats any prompt wording — but it lives in the harness, not the skill. |


## Non-Negotiable Before "Done"
<!-- Must be true before any task is complete. Only lives here if it caused a real failure. Cap: 25. -->

