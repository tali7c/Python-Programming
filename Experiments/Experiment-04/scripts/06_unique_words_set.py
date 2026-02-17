def normalize_word(w: str) -> str:
    return w.strip(".,!?;:\"'()[]{}").lower()


def main() -> None:
    sentence = input("Enter a sentence: ").strip()
    words = [normalize_word(w) for w in sentence.split()]
    words = [w for w in words if w]  # drop empty

    unique = set(words)
    print("Unique word count =", len(unique))
    print("Unique words =", unique)


if __name__ == "__main__":
    main()

