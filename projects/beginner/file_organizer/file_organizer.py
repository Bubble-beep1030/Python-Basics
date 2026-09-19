from pathlib import Path


def group_by_extension(files: list[str]) -> dict[str, list[str]]:
    grouped: dict[str, list[str]] = {}
    for file_name in files:
        suffix = Path(file_name).suffix.lower() or ".no_ext"
        grouped.setdefault(suffix, []).append(file_name)
    return grouped


if __name__ == "__main__":
    print(group_by_extension(["a.py", "b.txt", "README", "c.PY"]))
