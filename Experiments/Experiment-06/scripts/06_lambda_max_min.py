# Lambda for tuple of max and min
values = list(map(int, input("Enter numbers: ").split()))
max_min = lambda lst: (max(lst), min(lst))
print("(max, min):", max_min(values))
