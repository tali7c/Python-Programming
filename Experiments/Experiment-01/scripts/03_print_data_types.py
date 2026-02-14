def main() -> None:
    a = 10                 # int
    b = 3.14               # float
    c = True               # bool
    d = "Python"           # str
    e = [1, 2, 3]          # list

    values = [a, b, c, d, e]
    for v in values:
        print("Value:", v, "| Type:", type(v))


if __name__ == "__main__":
    main()

