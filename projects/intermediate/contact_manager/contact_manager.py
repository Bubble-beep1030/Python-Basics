def add_contact(book: dict[str, str], name: str, phone: str) -> None:
    if not name.strip() or not phone.strip():
        raise ValueError("Name and phone are required")
    book[name.strip().lower()] = phone.strip()


def find_contact(book: dict[str, str], name: str) -> str | None:
    return book.get(name.strip().lower())
