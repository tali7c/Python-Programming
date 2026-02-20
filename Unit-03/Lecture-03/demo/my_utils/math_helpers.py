import math


def hypotenuse(a: float, b: float) -> float:
    return math.sqrt(a * a + b * b)


def average(values: list[float]) -> float:
    if not values:
        raise ValueError("values must be non-empty")
    return sum(values) / len(values)

