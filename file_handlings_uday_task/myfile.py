# 2. Create a text file “MyFile.txt” in python and 
# ask the user to write separate 3 lines with three input statements from the user.


file = open('MyFile.txt','w')

file.write(input("enter the first line text: ")+'\n')
file.write(input("enter the second line text: ")+'\n')
file.write(input("enter the third line text: ")+'\n')