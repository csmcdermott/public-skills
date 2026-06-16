# Run `just` with no arguments to list available recipes.
default:
    @just --list

# Lint all skill plugins for structural issues.
lint:
    python3 scripts/lint_skills.py

# Lint and treat warnings as errors.
lint-strict:
    python3 scripts/lint_skills.py --strict

# Validate eval fixtures: parses every plugins/*/skills/*/evals/*.toml.
# To actually run the evals, invoke `/eval-skills` from Claude Code.
eval-validate:
    python3 scripts/eval_skills.py
