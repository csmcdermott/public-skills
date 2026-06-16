#!/usr/bin/env python3
"""Lint Claude Code skill plugins in this marketplace.

Checks structural rules that aren't visible at runtime but break discovery
or violate conventions captured in docs/agent/lessons.md.

Run from anywhere; paths are resolved relative to the repo root.

Exit codes:
    0  no errors (warnings allowed unless --strict)
    1  one or more errors, or warnings with --strict
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PLUGINS_DIR = REPO_ROOT / "plugins"
MARKETPLACE = REPO_ROOT / ".claude-plugin" / "marketplace.json"

SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+(?:[-+].+)?$")
REF_LINK_RE = re.compile(r"`?(references/[A-Za-z0-9_./-]+\.md)`?")

SKILL_WORD_WARN = 500
DESC_LEN_WARN = 500


@dataclass
class Findings:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def err(self, path: Path, msg: str) -> None:
        self.errors.append(f"{_rel(path)}: ERROR: {msg}")

    def warn(self, path: Path, msg: str) -> None:
        self.warnings.append(f"{_rel(path)}: WARN:  {msg}")


def _rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def parse_frontmatter(text: str) -> tuple[dict[str, str] | None, str]:
    """Parse simple YAML frontmatter (single-line key: value pairs).

    Returns (frontmatter dict, body). frontmatter is None if missing or malformed.
    """
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    raw = text[4:end]
    body = text[end + 5:]
    fm: dict[str, str] = {}
    for line in raw.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if ":" not in line:
            continue
        k, _, v = line.partition(":")
        fm[k.strip()] = v.strip()
    return fm, body


def load_json(path: Path, f: Findings) -> dict | None:
    try:
        return json.loads(path.read_text())
    except FileNotFoundError:
        f.err(path, "file not found")
    except json.JSONDecodeError as e:
        f.err(path, f"invalid JSON: {e.msg} (line {e.lineno})")
    return None


def lint_marketplace(f: Findings) -> None:
    data = load_json(MARKETPLACE, f)
    if data is None:
        return
    for key in ("name", "owner", "plugins"):
        if key not in data:
            f.err(MARKETPLACE, f"missing required key '{key}'")
    plugins = data.get("plugins")
    if not isinstance(plugins, list):
        f.err(MARKETPLACE, "'plugins' must be a list")
        return

    listed_names: set[str] = set()
    for i, entry in enumerate(plugins):
        ctx = f"plugins[{i}]"
        name = entry.get("name")
        source = entry.get("source")
        if not name:
            f.err(MARKETPLACE, f"{ctx} missing 'name'")
            continue
        if not source:
            f.err(MARKETPLACE, f"{ctx} ({name}) missing 'source'")
            continue
        listed_names.add(name)
        src_path = (REPO_ROOT / source).resolve()
        if not src_path.is_dir():
            f.err(MARKETPLACE, f"{ctx} ({name}) source path missing: {source}")
            continue
        if src_path.name != name:
            f.err(
                MARKETPLACE,
                f"{ctx} ({name}) source dir '{src_path.name}' != plugin name",
            )

    if PLUGINS_DIR.is_dir():
        on_disk = {p.name for p in PLUGINS_DIR.iterdir() if p.is_dir()}
        for missing in sorted(on_disk - listed_names):
            f.err(
                MARKETPLACE,
                f"plugin '{missing}' exists on disk but is not listed in marketplace.json",
            )


def lint_plugin(plugin_dir: Path, f: Findings) -> None:
    plugin_json = plugin_dir / ".claude-plugin" / "plugin.json"
    data = load_json(plugin_json, f)
    if data is None:
        return

    for key in ("name", "description", "version", "author", "license"):
        if key not in data:
            f.err(plugin_json, f"missing required key '{key}'")

    name = data.get("name")
    if name and name != plugin_dir.name:
        f.err(plugin_json, f"name '{name}' != directory '{plugin_dir.name}'")

    version = data.get("version", "")
    if version and not SEMVER_RE.match(version):
        f.err(plugin_json, f"version '{version}' is not semver (X.Y.Z)")

    skills_dir = plugin_dir / "skills"
    if not skills_dir.is_dir():
        f.err(plugin_dir, "missing skills/ directory")
        return

    skill_dirs = [d for d in skills_dir.iterdir() if d.is_dir()]
    if not skill_dirs:
        f.err(skills_dir, "no skills found")
        return

    for skill_dir in skill_dirs:
        lint_skill(skill_dir, f)


def lint_skill(skill_dir: Path, f: Findings) -> None:
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        f.err(skill_dir, "missing SKILL.md")
        return
    text = skill_md.read_text()
    fm, body = parse_frontmatter(text)
    if fm is None:
        f.err(skill_md, "missing or malformed YAML frontmatter")
        return

    for key in ("name", "description"):
        if not fm.get(key):
            f.err(skill_md, f"frontmatter missing '{key}'")

    name = fm.get("name", "")
    if name and name != skill_dir.name:
        f.err(skill_md, f"frontmatter name '{name}' != directory '{skill_dir.name}'")

    desc = fm.get("description", "")
    if desc:
        if "use when" not in desc.lower()[:60]:
            f.warn(
                skill_md,
                "description should start with 'Use when ...' (triggering condition, not workflow summary)",
            )
        if len(desc) > DESC_LEN_WARN:
            f.warn(
                skill_md,
                f"description is {len(desc)} chars (>{DESC_LEN_WARN}); likely summarizing the workflow",
            )

    word_count = len(body.split())
    if word_count > SKILL_WORD_WARN:
        f.warn(
            skill_md,
            f"SKILL.md body is {word_count} words (>{SKILL_WORD_WARN}); consider moving detail to references/",
        )

    check_reference_links(skill_md, body, f)


def check_reference_links(skill_md: Path, body: str, f: Findings) -> None:
    seen: set[str] = set()
    for match in REF_LINK_RE.finditer(body):
        rel = match.group(1)
        if rel in seen:
            continue
        seen.add(rel)
        if not (skill_md.parent / rel).is_file():
            f.err(skill_md, f"broken reference link: {rel}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--strict", action="store_true", help="treat warnings as errors"
    )
    args = parser.parse_args()

    f = Findings()
    lint_marketplace(f)

    if PLUGINS_DIR.is_dir():
        for plugin_dir in sorted(p for p in PLUGINS_DIR.iterdir() if p.is_dir()):
            lint_plugin(plugin_dir, f)
    else:
        f.err(PLUGINS_DIR, "plugins/ directory missing")

    for line in f.warnings:
        print(line)
    for line in f.errors:
        print(line)

    n_err, n_warn = len(f.errors), len(f.warnings)
    if n_err == 0 and n_warn == 0:
        print("OK: no findings.")
        return 0

    print(f"\n{n_err} error(s), {n_warn} warning(s).")
    if n_err > 0:
        return 1
    if args.strict and n_warn > 0:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
