#!/usr/bin/env python3
"""Load behavioral-eval fixtures for skills in this marketplace.

Fixtures live at `plugins/<plugin>/skills/<skill>/evals/*.toml`. This script is
the deterministic data layer for the eval pipeline: it parses fixtures, validates
the schema, and (with `--emit-json`) dumps them along with the relevant SKILL.md
body so an orchestrator can run subject + judge calls without re-implementing
the file walk.

The orchestrator is the `/eval-skills` slash command in `.claude/commands/`,
which dispatches subject + judge subagents inside Claude Code. There is no
direct API client here.

Fixture schema (TOML):

    mode             = "behavior"           # required (only "behavior" supported today)
    prompt           = "..."                # required: user message for the subject
    criteria         = ["...", ...]         # required: rubric items the judge checks
    description      = "..."                # optional: human-readable label
    known_bad_output = "..."                # optional: skip subject call;
                                            #   judge MUST find a violation, else the
                                            #   rubric is broken (calibration fail)

Usage:

    python3 scripts/eval_skills.py                  # validate schema, print summary
    python3 scripts/eval_skills.py writing-style    # filter by plugin name
    python3 scripts/eval_skills.py --emit-json      # dump fixtures + skill bodies as JSON
"""
from __future__ import annotations

import argparse
import json
import sys
import tomllib
from dataclasses import asdict, dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PLUGINS_DIR = REPO_ROOT / "plugins"


@dataclass
class Fixture:
    plugin: str
    skill: str
    name: str
    path: str
    mode: str
    description: str | None
    prompt: str
    criteria: list[str]
    known_bad_output: str | None
    skill_body: str


def parse_fixture(path: Path, plugin: str, skill: str, skill_body: str) -> Fixture:
    data = tomllib.loads(path.read_text())
    for key in ("mode", "prompt", "criteria"):
        if key not in data:
            raise ValueError(f"{path}: missing required key '{key}'")
    if data["mode"] != "behavior":
        raise ValueError(f"{path}: unsupported mode {data['mode']!r}")
    if not isinstance(data["criteria"], list) or not data["criteria"]:
        raise ValueError(f"{path}: 'criteria' must be a non-empty list")
    return Fixture(
        plugin=plugin,
        skill=skill,
        name=path.stem,
        path=str(path.relative_to(REPO_ROOT)),
        mode=data["mode"],
        description=data.get("description"),
        prompt=str(data["prompt"]).strip(),
        criteria=[str(c) for c in data["criteria"]],
        known_bad_output=(
            str(data["known_bad_output"]).strip()
            if "known_bad_output" in data
            else None
        ),
        skill_body=skill_body,
    )


def load_skill_body(plugin: str, skill: str) -> str:
    text = (PLUGINS_DIR / plugin / "skills" / skill / "SKILL.md").read_text()
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[end + 5:].strip()
    return text


def load_fixtures(plugin_filter: str | None) -> list[Fixture]:
    fixtures: list[Fixture] = []
    if not PLUGINS_DIR.is_dir():
        return fixtures
    for plugin_dir in sorted(p for p in PLUGINS_DIR.iterdir() if p.is_dir()):
        if plugin_filter and plugin_dir.name != plugin_filter:
            continue
        skills_dir = plugin_dir / "skills"
        if not skills_dir.is_dir():
            continue
        for skill_dir in sorted(s for s in skills_dir.iterdir() if s.is_dir()):
            evals_dir = skill_dir / "evals"
            if not evals_dir.is_dir():
                continue
            skill_body = load_skill_body(plugin_dir.name, skill_dir.name)
            for path in sorted(evals_dir.glob("*.toml")):
                fixtures.append(
                    parse_fixture(path, plugin_dir.name, skill_dir.name, skill_body)
                )
    return fixtures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plugin", nargs="?", help="filter to one plugin by name")
    parser.add_argument(
        "--emit-json",
        action="store_true",
        help="dump fixtures (with skill bodies) as a JSON array on stdout",
    )
    args = parser.parse_args()

    try:
        fixtures = load_fixtures(args.plugin)
    except ValueError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1

    if args.emit_json:
        print(json.dumps([asdict(f) for f in fixtures], indent=2))
        return 0

    if not fixtures:
        print("No fixtures found.")
        return 0

    print(f"Loaded {len(fixtures)} fixture(s).")
    for f in fixtures:
        label = f.description or "(no description)"
        kind = "judge-calibration" if f.known_bad_output else "behavior"
        print(f"  OK [{kind:17s}] {f.plugin}/{f.skill}/{f.name} — {label}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
