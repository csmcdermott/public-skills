# mcds-public-skills

A Claude Code marketplace with plugins you can install individually.

## Installation

Add this repo as a marketplace, then install any plugin by name:

```bash
claude plugin marketplace add https://github.com/csmcdermott/public-skills
claude plugin install writing-style@mcds-public-skills
```

### Update

```bash
claude plugin marketplace update mcds-public-skills
claude plugin update writing-style
```

## Plugins

### writing-style

Applies [CIA *Style Manual*](https://irp.fas.org/cia/product/style.pdf) principles to all prose: active voice, no filler, no hedging, short sentences. Claude activates it whenever it writes emails, docs, commit messages, error messages, UI copy, or explanations.

### create-persona

Builds custom product persona skills through a structured interview. Answer four groups of questions about a target user — role, goals, pain points, and decision style — and the skill generates a `SKILL.md` file that embodies that persona. Invoke the generated persona skill to get in-character feedback on PRDs, user stories, and design specs, including gut reactions, rational analysis, and behavioral predictions that separate what the user would say from what they would actually do.

## License

MIT
