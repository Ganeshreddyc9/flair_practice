# 11. Read the contents of file in reverse order.

# file_path = 'MergedFile.txt'
# with open(file_path,'r') as file:

#     content = file.read()
  
#     print(content[::-1])



file_path = 'MergedFile.txt'

with open(file_path,'r') as file1:

  content = file1.readlines()

    
reversed_content = reversed(content)
print(reversed_content)
# Print the reversed content
for line in reversed_content:
    print(line.strip())