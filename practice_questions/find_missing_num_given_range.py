# Find Missing Number in Array:
# Given an array nums containing n distinct numbers taken from the range 0 to n, where one number is missing.
# Write a Python function to find the missing number.

def find_missing_num(nums):

    n = len(nums)+1
    exepted_sum = n *(n+1)//2
    actual_sum = sum(nums)
    missing_num = exepted_sum - actual_sum

    return missing_num

nums = [1,3,4,5]

result = find_missing_num(nums)
print(result)

ums = [1,3,5]

result = find_missing_num(nums)
print(result)

