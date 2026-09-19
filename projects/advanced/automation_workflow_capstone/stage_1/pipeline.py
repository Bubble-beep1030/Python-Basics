def normalize_tasks(raw_tasks: list[dict]) -> list[dict]:
    normalized = []
    for item in raw_tasks:
        name = str(item.get("name", "")).strip()
        if not name:
            continue
        normalized.append({"name": name, "done": bool(item.get("done", False))})
    return normalized
