def main() -> None:
    n = int(input("Enter n (non-negative integer): "))
    if n < 0:
        print("n must be non-negative.")
        return

    total = n * (n + 1) // 2
    print(f"Sum of first {n} natural numbers =", total)


if __name__ == "__main__":
    main()

