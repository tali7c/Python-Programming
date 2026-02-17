# Create dictionary from two lists
keys = input("Enter keys: ").split()
values = input("Enter values: ").split()

d = dict(zip(keys, values))
print("Dictionary:", d)
