from __future__ import annotations

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius * self.radius

    def __str__(self) -> str:
        return f"Circle(radius={self.radius})"


class Rectangle(Shape):
    def __init__(self, length: float, width: float) -> None:
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width

    def __str__(self) -> str:
        return f"Rectangle(length={self.length}, width={self.width})"


def main() -> None:
    shapes: list[Shape] = [Circle(3), Rectangle(4, 5)]

    for s in shapes:
        print(s, "area =", round(s.area(), 4))

    # Uncommenting the next line would raise TypeError because Shape is abstract:
    # x = Shape()


if __name__ == "__main__":
    main()

