# Sum of digits
n = int(input("Enter an integer: "))

temp = abs(n)
result = 0
while temp > 0:
    result += temp % 10
    temp //= 10

print("Sum of digits:", result)
