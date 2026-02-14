def main() -> None:
    n = int(input("Enter an integer: "))
    if n % 5 == 0:
        print(n, "is a multiple of 5")
    else:
        print(n, "is NOT a multiple of 5")


if __name__ == "__main__":
    main()

