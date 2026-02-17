def main() -> None:
    s1 = {"Red", "yellow", "orange", "blue"}
    s2 = {"violet", "blue", "purple"}

    print("S1 =", s1)
    print("S2 =", s2)
    print()

    print("Union (S1 | S2) =", s1 | s2)
    print("Intersection (S1 & S2) =", s1 & s2)
    print("Difference (S1 - S2) =", s1 - s2)
    print("Difference (S2 - S1) =", s2 - s1)
    print("Symmetric difference (S1 ^ S2) =", s1 ^ s2)


if __name__ == "__main__":
    main()

