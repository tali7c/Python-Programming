# Check whether all values in a dictionary are the same using lambda

d = {"a": 5, "b": 5, "c": 5}

values = list(d.values())
all_same = (lambda vals: all(v == vals[0] for v in vals))(values)

print("All values same:", all_same)
