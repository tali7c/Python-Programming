marks = [72, 88, 95, 64, 51, 43, 77, 90, 58, 69]

avg = sum(marks) / len(marks)

sorted_marks = sorted(marks, reverse=True)
top_three = sorted_marks[:3]

pass_mark = 50
passing = [m for m in marks if m >= pass_mark]

print("Marks:", marks)
print("Average:", round(avg, 2))
print("Top 3:", top_three)
print("Passing (>=50):", passing)
