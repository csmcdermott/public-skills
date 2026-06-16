## Correction Log

<!-- Append a row every time the user corrects your approach.
     Be honest and specific — the point is to not repeat the mistake.
     Cap: 50 entries. Review before adding if at limit. -->

| Date | Context | What went wrong | Rule learned |
| --- | --- | --- | --- |


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


## Non-Negotiable Before "Done"
<!-- Must be true before any task is complete. Only lives here if it caused a real failure. Cap: 25. -->

