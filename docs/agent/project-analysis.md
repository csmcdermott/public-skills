## Project Overview

| Field | Value |
| --- | --- |
| **Project name** | mcds-public-skills |
| **Purpose** | Public Claude Code plugin marketplace. Users install individual plugins via the Claude Code CLI. |
| **Target release** | Ongoing / open-ended |
| **Last updated** | 2026-06-26 |

## Tech Stack

| Layer | Technology | Notes |
| --- | --- | --- |
| Runtime | Claude Code plugin system | No build step; plain Markdown/JSON files |
| Package format | `.claude-plugin/plugin.json` + `skills/*/SKILL.md` | Standard Claude Code plugin structure |
| Marketplace manifest | `.claude-plugin/marketplace.json` | Root-level; lists all available plugins |
| Testing (FE) | None | Skills are prose; no automated tests |
| Testing (BE) | None | |
| IaC | None | |

## Architecture Overview

```
mcds-public-skills/                     ← git repo root
├── .claude-plugin/marketplace.json     ← marketplace registry (lists all plugins)
├── plugins/
│   └── <plugin-name>/
│       ├── .claude-plugin/plugin.json  ← plugin metadata (name, version, author, license)
│       └── skills/
│           └── <skill-name>/
│               └── SKILL.md           ← skill content with YAML frontmatter
└── README.md
```

**Key design decisions:**
- Plugins are self-contained subdirectories under `plugins/`; the marketplace manifest at the root acts as an index.
- Skills are plain Markdown files with YAML frontmatter (`name`, `description`). Claude Code reads the frontmatter to decide when to auto-invoke the skill.
- No code, no build pipeline. Adding a plugin means creating the directory structure and JSON/Markdown files, then updating `marketplace.json`.
- Each plugin has its own `plugin.json`; the root `marketplace.json` references plugins by source path.

## Directory Structure

```
public-skills/
├── .claude/
│   └── settings.local.json        # project-local permission allowlist (gitignored)
├── .claude-plugin/
│   └── marketplace.json           # root marketplace registry
├── plugins/
│   ├── writing-style/             # narrative-arc writing rules with positive precepts P1-P6
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   └── skills/
│   │       └── writing-style/
│   │           ├── SKILL.md       # main skill: precepts P1-P6, five slop tells, format entry points
│   │           ├── references/    # narrative-arcs, anti-patterns, evidence-substitutions
│   │           └── evals/         # behavior fixtures (01-13, incl. 03 known-bad) for /eval-skills, /draft-loop, /compress-skill
│   └── create-persona/            # structured interview that emits persona review skills
│       ├── .claude-plugin/
│       │   └── plugin.json
│       └── skills/
│           └── create-persona/
│               └── SKILL.md
├── docs/
│   └── agent/
│       └── project-analysis.md   # this file
├── .gitignore
├── LICENSE                        # MIT
└── README.md
```

## Core Components

| Component | Location | Description |
| --- | --- | --- |
| Marketplace registry | `.claude-plugin/marketplace.json` | Lists all plugins with source paths; consumed by `claude plugin marketplace add` |
| Plugin manifest | `plugins/<name>/.claude-plugin/plugin.json` | Per-plugin metadata: name, version, author, homepage, license, keywords |
| Skill definition | `plugins/<name>/skills/<skill>/SKILL.md` | Skill content + YAML frontmatter; defines when Claude auto-invokes the skill |

## Data Flow

**Installing a plugin:**
1. User runs `claude plugin marketplace add <repo-url>` — Claude Code fetches `marketplace.json`.
2. User runs `claude plugin install <plugin-name>@<marketplace-name>` — Claude Code reads the plugin's `plugin.json` and copies skills to the user's Claude config.
3. On session start, Claude Code loads skill frontmatter; skill triggers when description matches the task.

**Adding a new plugin to this repo:**
1. Create `plugins/<name>/.claude-plugin/plugin.json`.
2. Create `plugins/<name>/skills/<skill-name>/SKILL.md` with frontmatter.
3. Add entry to `.claude-plugin/marketplace.json`.
4. Update `README.md`.

## External Integrations

| Integration | Purpose | Docs location |
| --- | --- | --- |
| Claude Code plugin CLI | Installs and manages plugins | README.md |
| GitHub | Source hosting; `claude plugin marketplace add` fetches from it | — |

## Key Interfaces / API Surface

There is no code API. The public interface is the marketplace install command:

```bash
claude plugin marketplace add https://github.com/csmcdermott/public-skills
claude plugin install <plugin-name>@mcds-public-skills
```

**Plugin manifest schema** (`plugin.json`):
- `name`, `description`, `version`, `author`, `homepage`, `repository`, `license`, `keywords`

**Skill frontmatter schema** (`SKILL.md`):
- `name` — identifier used in Skill tool calls
- `description` — used by Claude to decide when to auto-invoke

## Known Issues / Technical Debt

| Date | Area | Description |
| --- | --- | --- |
| 2026-05-14 | `.claude/settings.local.json` | Contains stale `mkdir`/`cp`/`rm` permission entries from initial plugin scaffolding; can be cleaned up |
| 2026-06-26 | `plugins/writing-style/skills/writing-style/SKILL.md` | Body is 1,703 words (linter count), total content 6,113 across SKILL.md + 3 references. Above the writing-skills <500 target, but intentionally rich and loads every session. Compression is exhausted: a 9-round `/compress-skill` run confirmed the remaining text is load-bearing (precepts P1-P6, Quick reference, format entry points, five slop tells, and the references' unique catch-rules are all fixture-verified). The aphoristic-flourish section of `anti-patterns.md` in particular cannot be compressed without regressing fixture 07 |

## Recently Changed Areas

| Date | File / Area | What changed |
| --- | --- | --- |
| 2026-06-26 | `plugins/writing-style/skills/writing-style/SKILL.md` | **Strengthened the em-dash rule (v1.4.0).** Measurement during a compression run showed subjects slipping a U+2014 in ~20-25% of business-memo/Slack/email drafts despite the rule, because it sat buried as the 2nd clause of the always-on "hygiene" run-on. Pulled it into a salient standalone rule that (a) names it "the top AI tell", (b) gives function-based substitutions (comma/parens for an aside, colon for a reveal, period for a hard stop, else recast), and (c) adds a literal final-pass "search for `—` and delete every one" step. Controlled before/after test (4 prone fixtures × 5 reps): slip rate **4/20 → 0/20**, zero regressions across all 11 fixtures (full gate+judge). +45 words to the always-on body, accepted given the durability gain |
| 2026-06-26 | `plugins/writing-style/skills/writing-style/` (SKILL.md + references) | Ran `/compress-skill` 9 rounds: 6326 → 6068 words (−4.1%), 7 cuts kept, 2 reverted. Every kept cut removed a *restatement* (guidance duplicated across files); no unique rule lost. **Key finding: the aphoristic-flourish section of `anti-patterns.md` is load-bearing** — cutting its keep/cut Test/examples regressed the essay-opener fixture (07), which then produced exactly the flourish endings it suppresses. Reverted. Also confirmed fixture 07 is intrinsically ~30% unstable on the flourish criterion even at the skill's best state (a hard target, not a regression signal). Did NOT bump version for the compression alone (behavior-preserving); the v1.4.0 bump above covers this release |
| 2026-06-24 | `plugins/writing-style/skills/writing-style/SKILL.md` + `evals/11-13` | Re-read the writing guides for contradictions and missing positive patterns. Three candidate additions (positive ending guidance, unity of tense/register, opinion-voice vs "be objective"). RED baseline: the current skill already passed all three fixtures (and no-skill controls committed to a position and held unity), so per the test-before-adding discipline only ONE change was warranted: the skill text self-contradicted ("be objective / write as a reporter" in Core craft vs "argue"/"take a position" in the essay and memo entries). Reworded that one bullet to scope objectivity to reporting genres and fold in the "don't write what you wouldn't say aloud" heuristic. Kept fixtures 11-13 as regression guards. Did NOT add unity/ending sections (would bloat the always-on body for non-failures). Bumped to v1.3.1 |
| 2026-06-24 | `.claude/commands/compress-skill.md` + `evals/07-10` | New `/compress-skill` ralph loop: greedily shrinks a skill's total word count, keeping only cuts that leave every fixture passing (git revert is the safety net), reports the load-bearing core. Added fixtures 07-10 (essay, memo, chat, error message) to broaden the oracle across formats before compressing |
| 2026-06-24 | `plugins/writing-style/skills/writing-style/SKILL.md` + references | Ran the compression loop. SKILL.md 2,128 → 1,655 words (−22%): deduped the always-loaded body (each precept was stated 3-4x), merged Common mistakes + Red flags + Rationalization into one "Pitfalls and red flags" section. anti-patterns.md 2,663 → 2,553: dropped the redundant slop-table "why" column and duplicate example sets. Total content 6,876 → 6,293 (−8.5%). All 10 fixtures verified passing skill-blind. Bumped plugin to v1.3.0 |
| 2026-06-24 | `plugins/writing-style/skills/writing-style/SKILL.md` | Moderate trim (2,442 → ~2,100 words) while adding content. New **P6 "Cut to the signal"** precept (start late / cut self-reference / green the draft) folding in the bracket test and omission + greening. New compact **"five slop tells"** checklist mapping the AI-slop taxonomy (generic, pseudo-insight, fake-authority, Wikipedia-rehash, wellness) to existing precepts. Trimmed redundancy in P1-P5 sections, rationalization table, common mistakes. Bumped plugin to v1.2.0 |
| 2026-06-24 | `plugins/writing-style/skills/writing-style/` (SKILL.md + references) | Scrubbed all source attributions (author/book/website names) from skill-facing content per user request; skill reads as self-contained guidance. Provenance kept only in agent docs/memory, not in the skill. The guides themselves (`writing-guides/` PDFs) are gitignored as local-only copyrighted material |
| 2026-06-24 | `plugins/writing-style/skills/writing-style/references/` | `anti-patterns.md`: added "five slop tells" phrase lists + "Clutter — the bracket test" section. `narrative-arcs.md`: added §5 "The cut pass" worked before/after example |
| 2026-06-24 | `plugins/writing-style/skills/writing-style/evals/` | Added fixtures 04 (thought-leadership), 05 (doc-intro), 06 (team-message) tempting the slop categories the skill covered least; double as `/eval-skills` and `/draft-loop` inputs |
| 2026-06-24 | `.claude/commands/draft-loop.md` | New "ralph loop" slash command: `/eval-skills` plus a revise-on-failure cycle (draft → deterministic mechanical gate → skill-blind judge → feed violations back → revise until pass or cap). Built/verified via TDD: RED baseline showed the current skill already prevented slop; GREEN run converged all fixtures (06 in 2 iterations after the gate caught an em dash the judge missed) |
| 2026-06-15 | `plugins/writing-style/skills/writing-style/SKILL.md` | Renamed frontmatter `general-writing` -> `writing-style` to match plugin/directory; stripped workflow-summary tail from description; added Quick reference table, When NOT to use, Common mistakes, Rationalization table, Red flags; added P3 factual-vs-illustrative carve-out and Core craft length-matching rule |
| 2026-06-15 | `plugins/writing-style/skills/writing-style/references/` | Em-dash sweep across SKILL.md and all references (body prose only; headings preserved per skill's own title exception). Added Boundary cases sub-table + sharper test under Aphoristic-flourish in `anti-patterns.md`. Consolidated four old reference files into `evidence-substitutions.md` (slop-word-blacklist, verbose-phrases, ai-tells, bare-adjectives-examples, coined-nouns-examples removed) |
| 2026-05-14 | `plugins/create-persona/` | Added create-persona plugin: structured interview skill that generates persona SKILL.md files for product reviews |
| 2026-05-14 | `.claude-plugin/marketplace.json` | Added create-persona entry |
| 2026-05-14 | `docs/agent/project-analysis.md` | Created initial project analysis |
| 2026-05 | `plugins/writing-style/` | Plugin moved into `plugins/` subdirectory structure; typo in `.claud-plugin` dir fixed to `.claude-plugin` |
| 2026-05 | `.claude-plugin/marketplace.json` | Marketplace manifest created |
