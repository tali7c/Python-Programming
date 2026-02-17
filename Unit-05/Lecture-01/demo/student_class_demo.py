from __future__ import annotations


class Student:
    college = "UPES"

    def __init__(self, name: str, sapid: str, marks: list[int] | None = None) -> None:
        self.name = name
        self.sapid = sapid
        self.marks = marks[:] if marks else []

    def add_mark(self, m: int) -> None:
        self.marks.append(m)

    def percentage(self) -> float:
        if not self.marks:
            return 0.0
        return sum(self.marks) / (len(self.marks) * 100) * 100

    def __str__(self) -> str:
        return f"Student(name={self.name}, sapid={self.sapid}, college={Student.college})"


def main() -> None:
    s1 = Student("Asha", "5001", [80, 90, 85, 70, 75])
    s2 = Student("Bilal", "5002")
    s2.add_mark(88)
    s2.add_mark(92)

    print(s1)
    print("s1 marks:", s1.marks, "percentage:", round(s1.percentage(), 2))
    print()

    print(s2)
    print("s2 marks:", s2.marks, "percentage:", round(s2.percentage(), 2))
    print()

    # Class variable shared by all
    Student.college = "UPES Dehradun"
    print("After changing Student.college:")
    print(s1)
    print(s2)


if __name__ == "__main__":
    main()

