# Count occurrences of values 0-3
n = int(input("Enter number of values: "))
values = list(map(int, input("Enter values (0-3): ").split()))

counts = {0: 0, 1: 0, 2: 0, 3: 0}
for v in values[:n]:
    if v in counts:
        counts[v] += 1

for k in range(4):
    print(f"{k} -> {counts[k]}")
