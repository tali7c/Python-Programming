def main() -> None:
    n = int(input("Enter an integer n: "))
    k = int(input("Enter shift amount k (>= 0): "))

    if k < 0:
        print("Shift amount must be non-negative.")
        return

    left = n << k
    right = n >> k

    print(f"{n} << {k} = {left}")
    print(f"{n} >> {k} = {right}")


if __name__ == "__main__":
    main()

