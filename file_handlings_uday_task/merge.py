# 3. Write a program to read the contents of both the files created 
# in the above programs and merge the contents into “merge.txt”.
# Avoid using the close() function to close the files.

with open('intro.txt','r') as file1:
    
    content1 = file1.read()

with open('MyFile.txt','r') as file2:

    content2 = file2.read()

merged_content = content1 + '\n' +content2

with open('MergedFile.txt','w') as mergedfile:
    mergedfile.write(merged_content)

print("files merged sucussfully..!!")