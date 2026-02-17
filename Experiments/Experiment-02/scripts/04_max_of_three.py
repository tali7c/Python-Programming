def main() -> None:
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    greatest = a
    if b > greatest:
        greatest = b
    if c > greatest:
        greatest = c

    print("Greatest number =", greatest)


if __name__ == "__main__":
    main()

