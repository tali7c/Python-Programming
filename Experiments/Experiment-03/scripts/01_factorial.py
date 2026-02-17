# Factorial of a number
n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    print("Factorial:", fact)
