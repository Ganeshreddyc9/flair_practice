#  Write a program to find the largest number in a list.


# l = [21,32,45,23,65]



# first_value = l[0]
# length = len(l)

# this is way is correct but  logic is wrong 

# Comparison Condition:

# The condition if first_value > l[i]: # is checking if first_value is greater than l[i]. 
# However, for finding the largest number, you should check if first_value is less than l[i].
       
# Print Statement Inside the Loop:

# You are printing values inside the loop, which means it will print every comparison result.
# Instead, you should only print the final largest number after the loop.


# for i in range(1,length+1):

#     if first_value > l[i]:
#         print(first_value)
#     else:
#         print(l[i])

l = [21,32,45,23,65]

# l = [32,21]

largest_value = l[0]

length = len(l)


for i in range(1, len(l)):
    # print(l[i])
    if largest_value < l[i]: # if this statements is true it will execute and replace that with l[i] , elseit will print largest num
        
        largest_value = l[i] 
   
    print(largest_value,".........",l[i])

print(f"the largest value in the list is:{largest_value}")

    