def precedence_examples() -> None:
    print("Precedence examples")
    print("2 + 3 * 4 =", 2 + 3 * 4)
    print("(2 + 3) * 4 =", (2 + 3) * 4)
    print()


def bitwise_truth_table() -> None:
    print("Bitwise truth table for a,b in {0,1}")
    print("a b | a&b a|b a^b")
    for a in (0, 1):
        for b in (0, 1):
            print(a, b, "|", a & b, "  ", a | b, "  ", a ^ b)
    print()


def membership_and_identity() -> None:
    nums = [10, 20, 30]
    print("Membership examples")
    print("20 in", nums, "->", 20 in nums)
    print("50 not in", nums, "->", 50 not in nums)
    print()

    a = [1, 2]
    b = a
    c = [1, 2]
    print("Identity examples")
    print("a == c ->", a == c)
    print("a is b ->", a is b)
    print("a is c ->", a is c)
    print()


def main() -> None:
    precedence_examples()
    bitwise_truth_table()
    membership_and_identity()


if __name__ == "__main__":
    main()

