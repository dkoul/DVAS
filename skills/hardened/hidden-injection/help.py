"""
Helper skill (hardened) - with injection detection.
"""

import re

INJECTION_PATTERNS = [
    r'\[INST\]', r'\[/INST\]', r'SYSTEM\s*OVERRIDE',
    r'ignore\s+previous\s+instructions', r'<!--.*?-->',
]


def sanitize(text: str) -> str:
    """Remove hidden chars and injection patterns."""
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
    text = re.sub(r'[\x00-\x1f\x7f]', '', text)
    text = ' '.join(text.split())
    return text


def detect_injection(text: str) -> list:
    """Detect injection patterns."""
    return [p for p in INJECTION_PATTERNS if re.search(p, text, re.IGNORECASE | re.DOTALL)]


def run(topic: str) -> dict:
    """Return help with injection detection."""

    help_text = {
        "git": "Use `git status` to check changes, `git add .` to stage, `git commit -m 'msg'` to commit.",
        "docker": "Use `docker ps` to list containers, `docker logs <id>` to view logs.",
        "npm": "Use `npm install` to install deps, `npm run <script>` to run scripts.",
        "python": "Use `python -m venv .venv` to create a virtualenv, `pip install -r requirements.txt` to install deps.",
    }

    response = help_text.get(topic.lower(), f"No help available for '{topic}'.")

    # Detect and sanitize
    injections = detect_injection(response)
    if injections:
        print(f"[ALERT] Injection patterns: {injections}")

    return {
        "status": "success",
        "response": sanitize(response),
        "injections_blocked": len(injections),
    }
