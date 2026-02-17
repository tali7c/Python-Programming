from __future__ import annotations


class Person:
    def __init__(self, name: str) -> None:
        self.name = name

    def describe(self) -> str:
        return f"Person(name={self.name})"


class Student(Person):
    def __init__(self, name: str, sapid: str) -> None:
        super().__init__(name)
        self.sapid = sapid

    def describe(self) -> str:
        return f"Student(name={self.name}, sapid={self.sapid})"


class PlacementStudent(Student):
    def __init__(self, name: str, sapid: str, company: str) -> None:
        super().__init__(name, sapid)
        self.company = company

    def describe(self) -> str:
        return f"PlacementStudent(name={self.name}, sapid={self.sapid}, company={self.company})"


def main() -> None:
    p = Person("Ravi")
    s = Student("Asha", "5001")
    ps = PlacementStudent("Bilal", "5002", "TechCorp")

    for obj in (p, s, ps):
        print(obj.describe())


if __name__ == "__main__":
    main()

