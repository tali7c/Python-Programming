# Keyword, default, and variable-length arguments

def greet(name, msg="Hello"):
    print(f"{msg}, {name}")


def add_all(*nums):
    return sum(nums)


def student_info(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")

# Demonstration

greet("Riya")
greet(name="Aman", msg="Welcome")
print("Total:", add_all(3, 5, 7))
student_info(name="Riya", sap_id="500001", branch="CSE")
