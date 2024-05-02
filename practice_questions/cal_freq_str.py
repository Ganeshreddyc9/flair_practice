# Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

Sample_String = input("enter the string:")

res_dict = {}

for i in Sample_String:
    print(i)
    if i in res_dict:
        res_dict[i] +=1
    else:
        res_dict[i] =1
print(res_dict)
