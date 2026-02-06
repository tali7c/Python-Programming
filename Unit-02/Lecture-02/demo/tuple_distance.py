import math

p1 = (2, 3)
p2 = (7, 9)

x1, y1 = p1
x2, y2 = p2

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print("Point 1:", p1)
print("Point 2:", p2)
print("Distance:", round(distance, 2))
