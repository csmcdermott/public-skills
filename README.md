# mcds-public-skills

A Claude Code marketplace with plugins you can install individually.

## Installation

Add this repo as a marketplace, then install any plugin by name:

```bash
claude plugin marketplace add https://github.com/csmcdermott/public-skills
claude plugin install writing-style@public-skills
```

### Update

```bash
claude plugin marketplace update public-skills
claude plugin update writing-style
```

## Plugins

### writing-style

Applies [CIA *Style Manual*](https://irp.fas.org/cia/product/style.pdf) principles to all prose: active voice, no filler, no hedging, short sentences. Claude activates it whenever it writes emails, docs, commit messages, error messages, UI copy, or explanations.

## License

MIT
