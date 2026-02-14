def read_float(prompt: str) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("Please enter a valid number.")


def main() -> None:
    print("Mini Calculator (+, -, *, /)")
    a = read_float("Enter a: ")
    b = read_float("Enter b: ")

    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")
    print(f"a * b = {a * b}")

    if b != 0:
        print(f"a / b = {a / b}")
    else:
        print("a / b = undefined (division by zero)")


if __name__ == "__main__":
    main()

