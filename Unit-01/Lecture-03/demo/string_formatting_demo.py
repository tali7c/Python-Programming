def read_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Please enter a valid integer.")


def main() -> None:
    print("String Cleaning + Formatting Demo")

    name = input("Enter student name: ").strip()
    sapid = input("Enter SAP ID: ").strip()

    # Normalize name: collapse extra spaces and Title Case.
    words = name.split()
    clean_name = " ".join(words).title()

    marks = []
    for sub in ["PDS", "Python", "Chemistry", "English", "Physics"]:
        marks.append(read_int(f"Marks in {sub} (0-100): "))

    total = sum(marks)
    percentage = total / len(marks)
    cgpa = percentage / 10.0

    print("\n--- Summary ---")
    print(f"Name: {clean_name}")
    print(f"SAP ID: {sapid}")
    print(f"Total: {total} / {len(marks)*100}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"CGPA: {cgpa:.1f}")


if __name__ == "__main__":
    main()

