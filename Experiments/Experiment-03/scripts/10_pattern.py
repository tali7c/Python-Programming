# Print pattern
n = 5

for i in range(n):
    left_end = n - i
    left = "".join(str(j) for j in range(1, left_end + 1))
    right = "".join(str(j) for j in range(left_end - 1, 0, -1))
    if i == 0:
        middle = ""
    else:
        middle = " " * i + " ".join(["*"] * i) + " " * i
    print(left + middle + right)
