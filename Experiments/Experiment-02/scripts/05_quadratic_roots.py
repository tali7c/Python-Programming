import math


def main() -> None:
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    if a == 0:
        print("Not a quadratic equation (a must be non-zero).")
        return

    d = b * b - 4 * a * c  # discriminant

    if d > 0:
        sqrt_d = math.sqrt(d)
        r1 = (-b + sqrt_d) / (2 * a)
        r2 = (-b - sqrt_d) / (2 * a)
        print("Roots are real and distinct:")
        print("Root 1 =", r1)
        print("Root 2 =", r2)
    elif d == 0:
        r = -b / (2 * a)
        print("Roots are real and equal:")
        print("Root =", r)
    else:
        # Imaginary roots: (-b +/- i*sqrt(-d)) / (2a)
        real = -b / (2 * a)
        imag = math.sqrt(-d) / (2 * a)
        print("Roots are imaginary:")
        print(f"Root 1 = {real} + {imag}i")
        print(f"Root 2 = {real} - {imag}i")


if __name__ == "__main__":
    main()

