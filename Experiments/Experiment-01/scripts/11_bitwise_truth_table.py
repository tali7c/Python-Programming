def main() -> None:
    print("Truth table for bitwise operators (&, |, ^) with a,b in {0,1}")
    print("a b | a&b a|b a^b")
    for a in (0, 1):
        for b in (0, 1):
            print(a, b, "|", a & b, "  ", a | b, "  ", a ^ b)


if __name__ == "__main__":
    main()

