#Write a program to remove duplicates from the given list.
#[2,3,5,6,6,7,23,45,10,10,45,2]

# l = [2,3,5,6,6,7,23,45,10,10,45,2]

# print(l)
# print(set(l))

# res = []
# for i in l:

#     if i not in res:
#         res.append(i)
# print("loop",res)


string_1='hello world'

string=""
for char in string_1:
    # print(char)
    if char not in string:
        string=string+char

print(string)