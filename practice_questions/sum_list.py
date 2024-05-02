# Write a program to find the sum of all numbers in a list?\

# The hiring manager expects the candidate to write clean and 
# readable code as well as their problem-solving skills.

l = [1,2,3,4,4,56,7]

sum_1 = 0
for i in l:
    # print(i)
    sum_1 = sum_1 +i
print(f"sum of the given list {sum_1}")

print("or")

print(sum(l))