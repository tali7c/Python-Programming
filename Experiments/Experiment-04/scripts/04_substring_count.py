def count_overlapping(text: str, sub: str) -> int:
    if sub == "":
        return 0
    count = 0
    for i in range(0, len(text) - len(sub) + 1):
        if text[i : i + len(sub)] == sub:
            count += 1
    return count


def main() -> None:
    text = input("Enter the string: ")
    sub = input("Enter the substring: ")

    result = count_overlapping(text, sub)
    print("Occurrences =", result)


if __name__ == "__main__":
    main()

