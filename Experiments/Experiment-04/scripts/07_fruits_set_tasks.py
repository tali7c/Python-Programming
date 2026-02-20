def read_fruits(n: int, label: str) -> set[str]:
    s: set[str] = set()
    print(f"Enter {n} fruit name(s) for {label}:")
    for i in range(n):
        fruit = input(f"{label}[{i+1}]: ").strip().lower()
        if fruit:
            s.add(fruit)
    return s


def main() -> None:
    n = int(input("Enter n (number of fruits in each set): "))
    if n <= 0:
        print("n must be positive.")
        return

    s1 = read_fruits(n, "s1")
    s2 = read_fruits(n, "s2")

    common = s1 & s2
    only_s1 = s1 - s2
    all_fruits = s1 | s2

    print("\n--- Results ---")
    print("Fruits in both sets (intersection):", common)
    print("Fruits only in s1 (difference):", only_s1)
    print("All unique fruits (union):", all_fruits)
    print("Count of all unique fruits =", len(all_fruits))


if __name__ == "__main__":
    main()

