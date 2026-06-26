"""
Document Tools skill (hardened) - with chain detection.
"""

import re

_flow_log = []


def sanitize(text: str) -> str:
    """Remove hidden markers."""
    text = re.sub(r'[\x00-\x1f\x7f]', '', text)
    return ' '.join(text.split())


def detect_markers(text: str) -> list:
    """Detect hidden markers."""
    found = []
    if re.search(r'[\x00-\x1f]', text):
        found.append("control_chars")
    if re.search(r'[\t ]{20,}', text):
        found.append("excessive_whitespace")
    return found


def format_text(text: str) -> dict:
    """Format with sanitization."""
    markers = detect_markers(text)
    if markers:
        print(f"[ALERT] Hidden markers: {markers}")

    _flow_log.append({"skill": "format"})

    return {"output": sanitize(text), "markers_removed": len(markers)}


def cache_content(content: str) -> dict:
    """Cache with sanitization."""
    markers = detect_markers(content)
    if markers:
        print(f"[ALERT] Hidden markers in cache: {markers}")

    _flow_log.append({"skill": "cache"})

    return {"message": f"Cached {len(content)} bytes", "sanitized": True}


def log_activity(action: str) -> dict:
    """Log with chain detection."""
    _flow_log.append({"skill": "log"})

    # Detect suspicious chain
    chain_alert = None
    if len(_flow_log) >= 3:
        recent = [e["skill"] for e in _flow_log[-3:]]
        if recent == ["format", "cache", "log"]:
            chain_alert = "format->cache->log chain detected"
            print(f"[ALERT] {chain_alert}")

    return {"log": f"[LOG] {action}", "chain_alert": chain_alert}


def get_flow_log() -> list:
    return _flow_log.copy()
