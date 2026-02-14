from pathlib import Path


def read_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Invalid integer. Please try again.")


def safe_division_demo() -> None:
    print("\n--- Safe Division Demo ---")
    a = read_int("Enter a: ")
    b = read_int("Enter b: ")

    try:
        print("a / b =", a / b)
    except ZeroDivisionError:
        print("Division by zero is not allowed.")


def safe_file_read_demo() -> None:
    print("\n--- Safe File Read Demo ---")
    data_dir = Path(__file__).resolve().parent.parent / "data"
    data_dir.mkdir(exist_ok=True)

    sample = data_dir / "sample.txt"
    if not sample.exists():
        sample.write_text("Hello from sample.txt\nSecond line\n", encoding="utf-8")

    path = input(f"Enter file path (try: {sample}): ").strip()
    try:
        with open(path, "r", encoding="utf-8") as f:
            print("\nFile content:")
            print(f.read())
    except FileNotFoundError:
        print("File not found.")
    except OSError as e:
        print("OS error:", e)


def main() -> None:
    print("Exception Handling Demo")
    safe_division_demo()
    safe_file_read_demo()
    print("\nDone.")


if __name__ == "__main__":
    main()

