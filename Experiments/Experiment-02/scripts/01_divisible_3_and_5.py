def main() -> None:
    n = int(input("Enter an integer: "))
    if n % 3 == 0 and n % 5 == 0:
        print(n, "is divisible by both 3 and 5")
    else:
        print(n, "is NOT divisible by both 3 and 5")


if __name__ == "__main__":
    main()

