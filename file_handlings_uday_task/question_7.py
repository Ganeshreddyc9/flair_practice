# 7. Read first N no. letters from a text file, read the first line, read a specific line from a text file.

# import linecache
# linecache.getline('Sample.txt', Number_of_Line)

file = 'MergedFile.txt'

N = int(input("enter the values to read: "))

with open(file ,'r') as textfile:
   
    N_no_letters = textfile.read(N)
    

    textfile.seek(0)
   
   # Read the first line
    first_line = textfile.readline()
    
    # Move the cursor back to the beginning of the file
    textfile.seek(0)
   
    # Read a specific line (for example, the third line)
    specific_line_number = 3
    for _ in range(specific_line_number - 1):
        # print(_)
        textfile.readline()
    specific_line = textfile.readline()
   
# Print the results
print(f"First {N} letters: {N_no_letters}")
print(f"First line: {first_line}")
print(f"Specific line {specific_line_number}: {specific_line}")








