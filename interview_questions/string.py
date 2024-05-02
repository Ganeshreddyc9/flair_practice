string_1='hello world'

string=""
for char in string_1:
    # print(char)
    if char not in string:
        string=string+char

print(string)