# Movie dictionary operations
n = int(input("Enter number of movies: "))
movies = {}

for _ in range(n):
    name = input("Movie name: ").strip()
    year = int(input("Year: "))
    director = input("Director: ").strip()
    cost = float(input("Production cost: "))
    collection = float(input("Collection: "))
    movies[name] = {
        "year": year,
        "director": director,
        "cost": cost,
        "collection": collection,
    }

print("All movie details:")
for name, info in movies.items():
    print(name, info)

print("Movies released before 2015:")
for name, info in movies.items():
    if info["year"] < 2015:
        print(name)

print("Movies that made a profit:")
for name, info in movies.items():
    if info["collection"] > info["cost"]:
        print(name)

dir_name = input("Enter director to search: ").strip()
print("Movies by director:", dir_name)
for name, info in movies.items():
    if info["director"].lower() == dir_name.lower():
        print(name)
