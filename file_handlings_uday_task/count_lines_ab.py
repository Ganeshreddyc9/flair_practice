# Write a program to count a total number of lines 
# and count the total number of lines starting with ‘A’, ‘B’, and ‘C’. (Consider the merge.txt file)
# The readlines() method reads all lines in the file and advances the file pointer to the end.
# When you use it in the loop, it will not iterate over the lines again.

with open('MergedFile.txt','r') as lines:

    all_lines = lines.readlines()
    # print(all_lines)
    # print(lines.readlines()) 
    # # num = lines.read() # it will read all chars at a time 
    
A_count= 0
B_count= 0
C_count= 0
    
    # print(len(lines.readlines()))
for line in all_lines:
    print(line)
    if line.startswith('A'):
        A_count +=1
    elif line.startswith('B'):
        B_count +=1
    elif line.startswith('C'):
        C_count +=1


total_lines = len(all_lines)
print("A_count",A_count)
print("B_count",B_count)
print("C_count",C_count)

print("count of all chars starts A and B and C")


