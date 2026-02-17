def read_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Please enter a valid integer.")


def is_even(n: int) -> bool:
    return n % 2 == 0


def sum_1_to_n(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact


def main() -> None:
    while True:
        print("\n=== Menu ===")
        print("1) Check even/odd")
        print("2) Sum of first n natural numbers")
        print("3) Factorial")
        print("4) Exit")

        choice = input("Choose option (1-4): ").strip()

        match choice:
            case "1":
                n = read_int("Enter n: ")
                print("Even" if is_even(n) else "Odd")
            case "2":
                n = read_int("Enter n (>= 0): ")
                if n < 0:
                    print("Please enter a non-negative integer.")
                else:
                    print("Sum =", sum_1_to_n(n))
            case "3":
                n = read_int("Enter n (>= 0): ")
                try:
                    print("Factorial =", factorial(n))
                except ValueError as e:
                    print("Error:", e)
            case "4":
                print("Goodbye.")
                break
            case _:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

