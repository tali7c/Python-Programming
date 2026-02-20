# Find max and min without built-in functions

def find_max_min(nums):
    if not nums:
        return None, None
    max_val = nums[0]
    min_val = nums[0]
    for n in nums[1:]:
        if n > max_val:
            max_val = n
        if n < min_val:
            min_val = n
    return max_val, min_val

values = list(map(int, input("Enter numbers: ").split()))
mx, mn = find_max_min(values)
print("Max:", mx)
print("Min:", mn)
