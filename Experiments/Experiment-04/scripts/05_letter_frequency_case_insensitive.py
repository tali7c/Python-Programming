def main() -> None:
    s = input("Enter a string (alphabets only or mixed): ")

    freq = {}
    for ch in s:
        if ch.isalpha():
            key = ch.upper()
            freq[key] = freq.get(key, 0) + 1

    if not freq:
        print("No alphabets found.")
        return

    # Print in alphabetical order
    for key in sorted(freq):
        print(f"{freq[key]}{key}")


if __name__ == "__main__":
    main()

