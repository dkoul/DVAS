"""
Summarizer skill (hardened) - with secret detection.
"""

import re

SECRET_PATTERNS = [
    r'(?:api[_-]?key|apikey)[=:]\s*["\']?([a-zA-Z0-9_\-]{20,})',
    r'(?:password|passwd)[=:]\s*["\']?([^\s"\']{8,})',
    r'(?:token|secret)[=:]\s*["\']?([a-zA-Z0-9_\-]{16,})',
]


def run(text: str, policy: str = "block") -> dict:
    """Summarize with secret detection."""

    # Detect secrets
    secrets = []
    for pattern in SECRET_PATTERNS:
        secrets.extend(re.findall(pattern, text, re.IGNORECASE))

    if secrets:
        print(f"[ALERT] {len(secrets)} secrets detected in input")

        if policy == "block":
            return {
                "status": "blocked",
                "reason": "Input contains sensitive data",
                "secrets_count": len(secrets),
            }

        if policy == "redact":
            for secret in secrets:
                text = text.replace(secret, "[REDACTED]")

    # Safe summarization
    sentences = [s.strip() for s in text.split('.') if len(s.strip()) > 10]
    summary = '. '.join(sentences[:2]) + '.' if sentences else "Nothing to summarize."

    return {
        "status": "success",
        "summary": summary,
        "secrets_detected": len(secrets),
    }
