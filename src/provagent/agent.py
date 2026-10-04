TOOLS = ["pick_modules", "render"]
WRITES = ("apply", "destroy",)


class InputError(ValueError):
    pass


def run(goal, payload):
    if not isinstance(goal, str) or not goal.strip():
        raise InputError("goal is empty")
    if any(word in goal.lower() for word in WRITES):
        return {"refused": True, "reason": "This agent only reads or plans. It does not write.", "tools": [], "wrote": False, "applied": False}
    size = payload.get("size") or "small"; result = ["network", "gke"] if size != "tiny" else ["network"]
    return {"refused": False, "tools": TOOLS, "modules": result, "wrote": False, "applied": False}
