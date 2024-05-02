#  Write a Python program that prints the calendar for a given month and year.
# Note : Use 'calendar' module.

import calendar

# print(help(calendar))
y = int(input("enter the year:"))
m = int(input("enter the month:"))

print(calendar.month(y,m))