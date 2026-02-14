def main() -> None:
    s = input("Enter a string: ")
    count = 0
    for ch in s:
        if ch.isupper():
            count += 1
    print("Number of capital letters =", count)


if __name__ == "__main__":
    main()

