# Write a Python program that 
# accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')


values = input("enter the values seperated by comma:")
# data = 3, 5, 7, 23
list = values.split(",")

tuple = tuple(list)

print("List:",list)
print("tuple:",tuple)


# print("list:",list(data))
# print("tuple:",data)