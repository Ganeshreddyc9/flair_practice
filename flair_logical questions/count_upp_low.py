
# Write a Python program that accepts a string and calculate the number of upper case letters and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Uppercase characters : 3
# No. of Lower case Characters : 12

Sample_String = 'The quick Brow Fox'


up_case_count = 0
lc_case_count = 0

for char in Sample_String:
    if char.isalpha():
        if char.islower():
            lc_case_count +=1
        else:
            up_case_count +=1
print(f"No of Uppercase count {up_case_count}")
print(f"No of Uppercase count {lc_case_count}")

