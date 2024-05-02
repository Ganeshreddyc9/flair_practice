fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# Use list comprehension to remove "a" from each fruit
fruits_without_a = [fruit for fruit in fruits if "a" not in fruit]

print(fruits_without_a)
