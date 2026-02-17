from pathlib import Path


def starts_with_vowel(name: str) -> bool:
    name = name.strip().lower()
    return bool(name) and name[0] in {"a", "e", "i", "o", "u"}


def main() -> None:
    data_dir = Path(__file__).resolve().parent.parent / "data"
    data_dir.mkdir(exist_ok=True)

    file_path = data_dir / "names.txt"

    names = ["Alice", "Bob", "Uma", "Irfan", "Esha", "Zara"]

    # Write sample data
    with open(file_path, "w", encoding="utf-8") as f:
        for n in names:
            f.write(n + "\n")

    # Read + compute stats
    read_names: list[str] = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            n = line.strip()
            if n:
                read_names.append(n)

    if not read_names:
        print("No names found.")
        return

    count = len(read_names)
    longest = max(read_names, key=len)
    vowel_count = sum(1 for n in read_names if starts_with_vowel(n))

    print("File:", file_path)
    print("Names:", read_names)
    print("Count:", count)
    print("Longest name:", longest)
    print("Names starting with a vowel:", vowel_count)


if __name__ == "__main__":
    main()

