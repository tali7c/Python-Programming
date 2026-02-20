# Armstrong number check
num = int(input("Enter an integer: "))

temp = abs(num)
digits = [int(d) for d in str(temp)]
power = len(digits)

armstrong_sum = sum(d ** power for d in digits)

if armstrong_sum == temp:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
