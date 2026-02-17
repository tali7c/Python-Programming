import math


def main() -> None:
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))

    if a < 0 or b < 0:
        print("Sides must be non-negative.")
        return

    c = math.sqrt(a * a + b * b)
    print(f"Hypotenuse c = {c:.4f}")


if __name__ == "__main__":
    main()

