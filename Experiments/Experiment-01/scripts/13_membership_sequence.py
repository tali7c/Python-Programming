def main() -> None:
    seq = (10, 20, 56, 78, 89)
    n = int(input("Enter a number to search: "))

    if n in seq:
        print(n, "is present in", seq)
    else:
        print(n, "is NOT present in", seq)


if __name__ == "__main__":
    main()

