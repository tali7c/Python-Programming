# Dictionary of persons and cities
n = int(input("Enter number of persons: "))
people = {}

for _ in range(n):
    name = input("Name: ").strip()
    city = input("City: ").strip()
    people[name] = city

print("All names:")
for name in people.keys():
    print(name)

print("All cities:")
for city in people.values():
    print(city)

print("Name and city:")
for name, city in people.items():
    print(f"{name} -> {city}")

city_counts = {}
for city in people.values():
    city_counts[city] = city_counts.get(city, 0) + 1

print("Count per city:")
for city, count in city_counts.items():
    print(f"{city}: {count}")
