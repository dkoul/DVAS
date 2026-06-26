# DVAS: Damn Vulnerable Agent Skills

A security lab for AI agent tool exploitation. Six attack primitives, implemented as innocent-looking agent skills — each paired with a hardened version demonstrating runtime detection and policy enforcement.

## Attack Primitives

| Skill | Attack Class | Description |
|-------|--------------|-------------|
| `summarizer` | Exfiltration | Leaks secrets via encoded output |
| `helper` | Prompt Injection | Hidden instructions in tool responses |
| `memory` | Context Poisoning | Rewrites agent memory/context |
| `capability` | Privilege Escalation | Elevates its own permissions |
| `typosquat` | Supply Chain | Malicious marketplace package |
| `chain` | Composition Attack | Three skills that leak only when combined |

## Structure

```
DVAS/
├── skills/
│   ├── vulnerable/       # Attack implementations
│   └── hardened/         # Defended versions
├── detection/            # Runtime monitoring & policy enforcement
├── labs/                 # Guided exploitation exercises
└── docs/                 # Threat taxonomy & defense guidance
```

## Supported Frameworks

- MCP (Model Context Protocol)
- OpenAI function calling
- Claude tool use
- LangChain tools

## Quick Start

```bash
# Coming soon
```

## License

MIT

## Author

Built for Nullcon Berlin 2026 CFP submission.
