from typing import List

def average(scores: List[int]) -> float:
    return sum(scores) / len(scores)


def letter_grade(avg_score: float, boundaries=None) -> str:
    if boundaries is None:
        boundaries = [(90, "A"), (80, "B"), (70, "C"), (60, "D")]
    for cutoff, grade in boundaries:
        if avg_score >= cutoff:
            return grade
    return "F"

scores = [78, 84, 69, 91, 73]

avg = average(scores)
print("Scores:", scores)
print("Average:", round(avg, 2))
print("Grade:", letter_grade(avg))
