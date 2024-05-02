# 10. Append the contents in entered by the user in the text file.

file_path = 'MergedFile.txt'
with open(file_path,'r') as file:

    content = file.read()

    l = content.split()

user_input = input('enter the text: ')
    
l.append(user_input)
    # content.seek(0

with open(file_path,'a') as file:

    file.write(" ".join(l))
# print(f"Updated content: {' '.join(l)}")
print(" ".join(l))
    



