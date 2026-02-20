def normalize_spaces(text: str) -> str:
    """Collapse multiple spaces and trim edges."""
    parts = text.split()
    return " ".join(parts)


def word_count(text: str) -> int:
    text = normalize_spaces(text)
    if not text:
        return 0
    return len(text.split(" "))

