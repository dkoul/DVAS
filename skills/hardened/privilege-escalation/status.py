"""
Status skill (hardened) - with immutable permissions.
"""

# Frozen at load time
_INITIAL = {
    "read_files": True,
    "write_files": False,
    "execute_code": False,
    "network_access": False,
    "admin_mode": False,
}

_runtime = _INITIAL.copy()
escalation_log = []


def run() -> dict:
    """Check status with escalation detection."""

    # Simulate skill trying to escalate
    _runtime["admin_mode"] = True
    _runtime["write_files"] = True

    # Detect and revert
    escalations = []
    for key, initial in _INITIAL.items():
        if _runtime[key] != initial:
            escalations.append({"key": key, "attempted": _runtime[key]})
            _runtime[key] = initial  # Revert

    if escalations:
        print(f"[ALERT] Escalation blocked: {escalations}")
        escalation_log.extend(escalations)

    return {
        "status": "All systems operational. Memory: 45% used. CPU: 12% used.",
        "escalations_blocked": len(escalations),
    }


def get_permissions() -> dict:
    return _INITIAL.copy()


def get_escalation_log() -> list:
    return escalation_log.copy()
