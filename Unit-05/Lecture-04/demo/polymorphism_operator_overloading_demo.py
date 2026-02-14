from __future__ import annotations

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, r: float) -> None:
        self.r = r

    def area(self) -> float:
        return math.pi * self.r * self.r

    def __str__(self) -> str:
        return f"Circle(r={self.r})"


class Rectangle(Shape):
    def __init__(self, l: float, w: float) -> None:
        self.l = l
        self.w = w

    def area(self) -> float:
        return self.l * self.w

    def __str__(self) -> str:
        return f"Rectangle(l={self.l}, w={self.w})"


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self) -> str:
        return f"Point({self.x},{self.y})"


def main() -> None:
    print("Polymorphism demo (area):")
    shapes: list[Shape] = [Circle(3), Rectangle(4, 5)]
    for s in shapes:
        print(s, "area =", round(s.area(), 4))

    print("\nOperator overloading demo (+):")
    p1 = Point(10, 20)
    p2 = Point(12, 15)
    p3 = p1 + p2
    print("p1 =", p1)
    print("p2 =", p2)
    print("p3 = p1 + p2 =", p3)


if __name__ == "__main__":
    main()

