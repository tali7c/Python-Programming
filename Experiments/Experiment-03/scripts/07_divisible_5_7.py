# Numbers divisible by 5 or 7 between 1 and 100
numbers = [i for i in range(1, 101) if i % 5 == 0 or i % 7 == 0]

print("Numbers:", numbers)
print("Count:", len(numbers))
