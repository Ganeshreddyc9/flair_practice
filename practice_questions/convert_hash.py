
    
n = int(input())
integer_list = map(int, input().split())
print(integer_list)
    
    # Create a tuple
my_tuple = tuple(integer_list)
    
    # Calculate and print the hash
result = hash(my_tuple)
print(my_tuple)
print(result)