def main() -> None:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if a > b:
        print("Greatest number =", a)
    elif b > a:
        print("Greatest number =", b)
    else:
        print("Numbers are equal")


if __name__ == "__main__":
    main()

