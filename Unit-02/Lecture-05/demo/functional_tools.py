from typing import List

raw = [3, -1, 4, None, 0, 7, 2]

clean = list(filter(lambda x: isinstance(x, int) and x > 0, raw))
transformed = list(map(lambda x: x * 2, clean))


def recursive_sum(items: List[int]) -> int:
    if not items:
        return 0
    return items[0] + recursive_sum(items[1:])

print("Raw:", raw)
print("Clean:", clean)
print("Transformed (x2):", transformed)
print("Recursive sum:", recursive_sum(clean))
