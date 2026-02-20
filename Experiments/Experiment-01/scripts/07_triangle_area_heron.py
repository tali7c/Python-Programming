import math


def is_valid_triangle(a: float, b: float, c: float) -> bool:
    return a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a)


def main() -> None:
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    c = float(input("Enter side c: "))

    if not is_valid_triangle(a, b, c):
        print("Invalid triangle (check positivity and triangle inequality).")
        return

    s = (a + b + c) / 2.0
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"Area = {area:.4f}")


if __name__ == "__main__":
    main()

