def show_dynamic_typing() -> None:
    x = 10
    print("x =", x, "type =", type(x), "id =", id(x))

    x = 10.5
    print("x =", x, "type =", type(x), "id =", id(x))

    x = "ten"
    print("x =", x, "type =", type(x), "id =", id(x))


def show_immutability() -> None:
    s = "python"
    print("\nOriginal s:", s, "id =", id(s))
    t = s.upper()
    print("After upper():")
    print("s:", s, "id =", id(s))
    print("t:", t, "id =", id(t))


def show_mutability_and_aliasing() -> None:
    a = [1, 2, 3]
    print("\nOriginal a:", a, "id =", id(a))

    a.append(99)
    print("After a.append(99):", a, "id =", id(a))

    b = a  # alias (same object)
    b.append(100)
    print("\nAfter b = a; b.append(100):")
    print("a:", a, "id =", id(a))
    print("b:", b, "id =", id(b))

    c = a.copy()  # independent copy
    c.append(200)
    print("\nAfter c = a.copy(); c.append(200):")
    print("a:", a, "id =", id(a))
    print("c:", c, "id =", id(c))


def main() -> None:
    print("Dynamic Typing Demo")
    show_dynamic_typing()

    print("\nImmutability Demo (strings)")
    show_immutability()

    print("\nMutability + Aliasing Demo (lists)")
    show_mutability_and_aliasing()


if __name__ == "__main__":
    main()

