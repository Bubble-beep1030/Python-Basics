def word_frequency(text: str) -> dict[str, int]:
    freq: dict[str, int] = {}
    for word in text.lower().split():
        normalized = ''.join(ch for ch in word if ch.isalnum())
        if not normalized:
            continue
        freq[normalized] = freq.get(normalized, 0) + 1
    return freq
