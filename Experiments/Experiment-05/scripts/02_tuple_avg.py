# Tuple average
n = int(input("Enter number of values: "))
values = list(map(float, input("Enter values: ").split()))

t = tuple(values[:n])
avg = sum(t) / len(t) if t else 0

print("Tuple:", t)
print("Average:", avg)
