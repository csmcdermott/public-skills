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
| 2026-06-24 | **In an eval-driven compression loop, separate subject-simulation noise from real regressions before reverting a cut.** When verifying compressed writing-style, subjects intermittently emitted an em dash ("Team — Friday") or prepended self-narration ("The skill directs me to...") despite "artifact only" instructions. These are subject flakiness, not skill-content regressions (they appear at baseline too). Confirm with the deterministic gate plus one clean rerun (firm "no em dashes, artifact only" instruction) before counting a fixture as failed and reverting an otherwise-good cut. |


## Non-Negotiable Before "Done"
<!-- Must be true before any task is complete. Only lives here if it caused a real failure. Cap: 25. -->

