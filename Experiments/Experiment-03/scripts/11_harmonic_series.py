# Sum of series 1 + 1/2 + ... + 1/n
n = int(input("Enter n: "))

total = 0.0
for i in range(1, n + 1):
    total += 1 / i

print("Sum of series:", round(total, 4))
