# mcds-public-skills — Agent Guide

A public Claude Code plugin marketplace. Users install individual plugins (skills) by name via the Claude Code CLI. This repo is content, not code: plain Markdown skill files and JSON manifests. No build step, no test suite, no runtime.


## Session Start

Before planning or editing anything:

1. Read `docs/agent/project-analysis.md` — current architecture, directory layout, recently-changed areas, known issues.
2. Read `docs/agent/lessons.md` — corrections and project-specific gotchas from prior sessions.

Update both files at the end of any session that changes architecture, adds a plugin, or surfaces a new gotcha.


## Repository Layout

```
public-skills/
├── .claude-plugin/marketplace.json   # marketplace registry — lists every plugin
├── plugins/
│   └── <plugin-name>/
│       ├── .claude-plugin/plugin.json   # per-plugin manifest
│       └── skills/
│           └── <skill-name>/
│               ├── SKILL.md             # skill body + YAML frontmatter
│               └── references/          # optional supporting docs
├── scripts/lint_skills.py            # structural linter (see Linting)
├── justfile                          # task recipes (`just lint`, `just lint-strict`)
├── docs/agent/                       # persistent agent memory (see Session Start)
└── README.md                         # user-facing install instructions
```

Notes:

- There is no `src/` directory. Do not create one unless a real need appears.
- The skill's frontmatter `name:` MUST match its containing directory name. A mismatch breaks discovery (see `docs/agent/lessons.md`).
- The skill `description:` field is for triggering, not summarizing. Use `Use when ...`; never describe the workflow the skill performs.


## Common Workflows

### Adding a new plugin

1. Create `plugins/<name>/.claude-plugin/plugin.json` — name, description, version, author, homepage, repository, license, keywords.
2. Create `plugins/<name>/skills/<skill-name>/SKILL.md` with frontmatter (`name`, `description`).
3. Add a plugin entry to `.claude-plugin/marketplace.json`.
4. Add a short section to `README.md`.
5. Update `docs/agent/project-analysis.md` (Directory Structure + Recently Changed Areas).

### Editing an existing skill

1. Check `~/.claude/skills/<name>/SKILL.md` for a personal-scope shadow. If one exists, decide whether to delete it before testing — it can take precedence over the plugin version in skill discovery.
2. Edit the SKILL.md in `plugins/<name>/skills/<skill-name>/`.
3. Bump the `version` in the plugin's `plugin.json` if the change is user-visible.
4. Note the change in `docs/agent/project-analysis.md` → Recently Changed Areas.

### Linting

Run `just lint` before opening a PR. The linter (`scripts/lint_skills.py`, Python stdlib only) checks:

- `marketplace.json`: valid JSON; every `plugins[]` entry resolves to a real directory; every plugin on disk is listed.
- Each `plugin.json`: required fields present; `name` matches directory; `version` is semver.
- Each `SKILL.md`: well-formed frontmatter; **frontmatter `name:` matches the directory**; description starts with "Use when ..."; body under 500 words (warning only); `references/*.md` links resolve.

Use `just lint-strict` to treat warnings as errors — useful in CI once that exists.

### Behavioral evals

Skills can have behavioral-eval fixtures at `plugins/<name>/skills/<skill>/evals/*.toml`. Each fixture declares a `prompt`, a list of `criteria`, and optionally a `known_bad_output` (judge calibration). To run the evals, invoke `/eval-skills` from Claude Code — the slash command at `.claude/commands/eval-skills.md` dispatches subject + judge subagents per fixture and aggregates verdicts. The judge is never shown the skill body. `just eval-validate` parses fixtures without running them.


## Conventions

- **Prose quality.** Skill bodies are prose written for an LLM reader. Apply the `writing-style` plugin's principles: active voice, no hedging, no filler, length matched to content. Skill descriptions and frontmatter are not exempt.
- **Skill length.** Aim for under 500 words for non-getting-started skills. Move detail to `references/<topic>.md` and link from the main body.
- **Markdown.** 2-space indentation in Markdown lists (standard CommonMark). JSON files: 2-space indent, trailing newline.
- **Timestamps.** Use `YYYY-MM-DD` for dates in agent memory files. Use `YYYY-MM-DD HH:mm` only when time-of-day matters.
- **Versioning.** Semantic versioning in each plugin's `plugin.json`.


## Core Principles

- **Simplicity first.** Every change should touch the minimum surface area. A new plugin is three files plus a marketplace entry — not a framework.
- **Minimal dependencies.** There are none today. Adding one (a build tool, a linter, a generator) requires explicit justification.
- **No secrets in the repo.** API keys, tokens, personal email beyond the public maintainer address — none of these belong in committed files.
- **Root-cause fixes.** If a skill is being mis-invoked or shadowed, fix the frontmatter, the directory name, or the install path. Don't paper over it with a description tweak.


## What This Repo Is Not

- Not a software project. There is no typecheck, no test runner, no CI to satisfy. Don't add comments like `// TODO: add tests` or principles about type discipline.
- Not a documentation site. The README is the user-facing entry point; skill files are agent-facing. Keep them separate.
- Not the right place for personal skills. Anything experimental, half-formed, or specific to one workflow belongs in `~/.claude/skills/`, not here.
