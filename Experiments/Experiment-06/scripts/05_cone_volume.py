# Lambda function to compute volume of a cone
import math

volume_cone = lambda r, h: (1/3) * math.pi * r * r * h

r = float(input("Enter radius: "))
h = float(input("Enter height: "))
print("Volume:", volume_cone(r, h))
