def main() -> None:
    principal = float(input("Enter principal (P): "))
    rate = float(input("Enter rate of interest (R in %): "))
    time = float(input("Enter time (T in years): "))

    if principal < 0 or rate < 0 or time < 0:
        print("P, R, and T must be non-negative.")
        return

    si = (principal * rate * time) / 100.0
    print(f"Simple Interest = {si:.2f}")


if __name__ == "__main__":
    main()

