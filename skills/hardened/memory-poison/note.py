"""
Notes skill (hardened) - with protected keys.
"""

PROTECTED_KEYS = {"trusted_domains", "safety_mode", "system_note", "permissions"}

agent_memory = {
    "user_name": "Alice",
    "preferences": {"theme": "dark"},
    "trusted_domains": ["company.com"],
}

audit_log = []


def run(key: str, value: str) -> dict:
    """Save note with protection."""

    if key in PROTECTED_KEYS:
        print(f"[BLOCKED] Cannot modify protected key: {key}")
        audit_log.append({"action": "blocked", "key": key})
        return {"status": "blocked", "reason": f"'{key}' is protected"}

    old = agent_memory.get(key)
    agent_memory[key] = value
    audit_log.append({"action": "write", "key": key, "old": old, "new": value})

    return {"status": "success", "message": f"Saved '{key}'"}


def get_memory() -> dict:
    return agent_memory.copy()


def get_audit() -> list:
    return audit_log.copy()
