## Project Overview

| Field | Value |
| --- | --- |
| **Project name** | mcds-public-skills |
| **Purpose** | Public Claude Code plugin marketplace. Users install individual plugins via the Claude Code CLI. |
| **Target release** | Ongoing / open-ended |
| **Last updated** | 2026-05-14 |

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
│   └── writing-style/             # first and currently only plugin
│       ├── .claude-plugin/
│       │   └── plugin.json        # plugin metadata
│       └── skills/
│           └── writing-style/
│               └── SKILL.md       # CIA Style Manual-based writing rules
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

## Recently Changed Areas

| Date | File / Area | What changed |
| --- | --- | --- |
| 2026-05-14 | `plugins/create-persona/` | Added create-persona plugin: structured interview skill that generates persona SKILL.md files for product reviews |
| 2026-05-14 | `.claude-plugin/marketplace.json` | Added create-persona entry |
| 2026-05-14 | `docs/agent/project-analysis.md` | Created initial project analysis |
| 2026-05 | `plugins/writing-style/` | Plugin moved into `plugins/` subdirectory structure; typo in `.claud-plugin` dir fixed to `.claude-plugin` |
| 2026-05 | `.claude-plugin/marketplace.json` | Marketplace manifest created |
