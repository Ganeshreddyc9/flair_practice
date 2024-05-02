# in given string replace d with w and w with d

string = "abcdefghijklmnopqrstuvwxyz"

result = ""

for char in string:

    if char == 'd':
        result += 'w'
    elif char =='w':
        result += 'd'
    else:
        result += char
print(result)

# string = "abcdefghijklmnopqrstuvwxyz"

# result_1= string.replace('d','^')
# result_2 = string.replace('d','^').replace('^','w')
# result_3 = string.replace('d','^').replace('^','w')
# # .replace("w",'^^').replace("^^","d")
# print("result_!:",result_1)
# print("result_!:",result_2)
# print("result_!:",result_3)

# # original_string = "abcdefghijklmnopqrstuvwxyz"
# # new_string = original_string.replace('d', 'w').replace('w', 'd')

# # print(new_string)   



