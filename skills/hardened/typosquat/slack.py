"""
Slack Notify skill (hardened) - with typosquat detection.
"""

import difflib

TRUSTED = {"slack-notify": "Slack Technologies, LLC"}
KNOWN_TYPOS = ["slacl-notify", "slack_notify", "slack-notifiy", "s1ack-notify"]


def verify_package(name: str) -> dict:
    """Verify package isn't a typosquat."""

    if name in KNOWN_TYPOS:
        return {"status": "blocked", "reason": "Known typosquat", "did_you_mean": "slack-notify"}

    for legit in TRUSTED:
        sim = difflib.SequenceMatcher(None, name, legit).ratio()
        if 0.7 < sim < 1.0:
            return {"status": "blocked", "reason": "Suspicious similarity", "similar_to": legit}

    if name in TRUSTED:
        return {"status": "verified", "author": TRUSTED[name]}

    return {"status": "warning", "reason": "Unknown package"}


def run(channel: str, message: str, package: str = "slack-notify") -> dict:
    """Send notification after verification."""

    verify = verify_package(package)

    if verify["status"] == "blocked":
        print(f"[BLOCKED] {verify['reason']}")
        return verify

    return {
        "status": "success",
        "message": f"Sent to #{channel}: '{message[:30]}...'",
        "verified": verify["status"] == "verified",
    }
