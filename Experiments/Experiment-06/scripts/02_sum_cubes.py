# Sum of cubes of positive integers smaller than n

def sum_cubes(n):
    total = 0
    for i in range(1, n):
        total += i ** 3
    return total

n = int(input("Enter n: "))
print("Sum of cubes:", sum_cubes(n))
