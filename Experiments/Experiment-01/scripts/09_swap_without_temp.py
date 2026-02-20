def main() -> None:
    a = input("Enter a: ")
    b = input("Enter b: ")

    print("Before swap: a =", a, ", b =", b)
    a, b = b, a
    print("After swap:  a =", a, ", b =", b)


if __name__ == "__main__":
    main()

