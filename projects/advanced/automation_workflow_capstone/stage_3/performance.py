def fast_unique_names(tasks: list[dict]) -> list[str]:
    return sorted({str(task.get("name", "")).strip() for task in tasks if str(task.get("name", "")).strip()})
