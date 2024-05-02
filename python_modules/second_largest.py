# nums = [3, 5, 7, 2, 8, 4]
nums = [3, 5, 7]
max_product = float('-inf')
second_max_product = float('-inf')
    
    # Iterate through the list to find the maximum and second maximum products
for num in nums:
    if num > max_product:
        second_max_product = max_product
        max_product = num
    elif num > second_max_product:
        second_max_product = num

print(second_max_product)
print(max_product)