# Helper (Hardened)

A helper with injection detection and sanitization.

## Usage

Same as vulnerable version:
```
/help <topic>
```

## Security Features

- Detects hidden instructions in output
- Removes HTML comments, control characters
- Strips invisible unicode
- Returns sanitized response only
