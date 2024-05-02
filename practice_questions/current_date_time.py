# Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14

import datetime

# Get the current date and time
now = datetime.datetime.now()

#creting a object representing  the current data and time 
print(now)

# displaying a message indicating what is being printed 

print("current date and time:")

# strftime means string from time

print(now.strftime("%Y-%M-%D %H:%M:%S"))
