# 4. Count the total number of upper case, lower case, and digits used in the text file “merge.txt”.


with open('MergedFile.txt','r') as file1:
    # print(len(file1),"length of all chars..")

  
    upper_count = 0
    lower_count = 0
    digit_count = 0
    for char in file1.read():
        print(char)
        if char.isupper():
            upper_count +=1
        elif char.islower():
            lower_count +=1
        elif char.isdigit():
            digit_count +=1 
print("lower_count: ",lower_count)
print("upper_count:",upper_count)
print("digit_count:",digit_count)



#   for char in file1:
        # print(len(char))
# s = 'hi'
# print(help(s.isdigit))