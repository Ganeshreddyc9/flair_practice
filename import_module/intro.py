# ways to import module in same directory 
# import my_module as mm
from my_module import find_index, test
import sys

courses = ['History', 'Math', 'Physics', 'Comsci']

# first way
# index = my_module.find_index(courses, 'Math')
# second way
index = mm.find_index(courses, 'Math')

# here we are using directly 

index1 = find_index(courses,'Physics')


# print(index)
# print(index1)
# print(test)

# to find the path of file location 
print("find the path of the file location:......",sys.path)


'''
here we are using from my_module import find index what ever ur using the function name 

that funcion name access not for others 

test = 'Test String' -- test is also part of mymodule and we have to incule in the importing 

def find_index(to_search, target):
    'Find the index of a value in a sequence

    for i, value in enumerate(to_search):
        if value == target:
            return i
        
    return -1 

'''


