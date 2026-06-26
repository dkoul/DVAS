# Summarizer (Hardened)

A summarizer with secret detection and blocking.

## Usage

Same as vulnerable version:
```
/summarize <text>
```

## Security Features

- Detects secrets in input (API keys, passwords, tokens)
- Blocks or redacts sensitive content
- No network exfiltration
- Returns detection alerts
