def grade_from_cgpa(cgpa: float) -> str:
    if cgpa < 0:
        return "Invalid"
    if cgpa <= 3.4:
        return "F"
    if cgpa <= 5.0:
        return "C+"
    if cgpa <= 6.0:
        return "B"
    if cgpa <= 7.0:
        return "B+"
    if cgpa <= 8.0:
        return "A"
    if cgpa <= 9.0:
        return "A+"
    if cgpa <= 10.0:
        return "O"
    return "Invalid"


def read_mark(prompt: str) -> float:
    while True:
        try:
            m = float(input(prompt).strip())
        except ValueError:
            print("Please enter a valid number.")
            continue
        if 0 <= m <= 100:
            return m
        print("Marks must be between 0 and 100.")


def main() -> None:
    print("Grade Sheet Generator")
    name = input("Name: ").strip()
    roll = input("Roll Number: ").strip()
    sapid = input("SAP ID: ").strip()
    sem = input("Semester: ").strip()
    course = input("Course: ").strip()

    subjects = ["PDS", "Python", "Chemistry", "English", "Physics"]
    marks = {}
    for sub in subjects:
        marks[sub] = read_mark(f"Marks in {sub}: ")

    total = sum(marks.values())
    percentage = total / len(subjects)
    cgpa = percentage / 10.0
    grade = grade_from_cgpa(cgpa)

    print("\n--- Grade Sheet ---")
    print(f"Name: {name}")
    print(f"Roll Number: {roll}")
    print(f"SAP ID: {sapid}")
    print(f"Sem: {sem}")
    print(f"Course: {course}")
    print("\nSubject name: Marks")
    for sub in subjects:
        print(f"{sub}: {marks[sub]}")
    print(f"\nPercentage: {percentage:.2f}%")
    print(f"CGPA: {cgpa:.1f}")
    print(f"Grade: {grade}")


if __name__ == "__main__":
    main()

