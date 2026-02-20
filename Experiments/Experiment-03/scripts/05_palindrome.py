# Palindrome check
value = input("Enter a number or string: ")

if value == value[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
