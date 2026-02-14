def main() -> None:
    s = input("Enter a string: ").lower()
    vowels = set("aeiou")
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    print("Total number of vowels =", count)


if __name__ == "__main__":
    main()

