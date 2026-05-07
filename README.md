# public-skills

A collection of Claude Code skills, installable as a plugin.

## Installation

Add this repo as a marketplace, then install individual skills:

```bash
claude plugin marketplace add https://github.com/csmcdermott/public-skills
claude plugin install writing-style@public-skills
```

### Update

```bash
claude plugin update writing-style
```

## Skills

### writing-style

Applies [CIA *Style Manual*](https://irp.fas.org/cia/product/style.pdf) principles to all prose: active voice, no filler, no hedging, short sentences. Use it whenever Claude writes emails, docs, commit messages, error messages, UI copy, or explanations.

## License

MIT
