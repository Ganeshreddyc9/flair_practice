#  Write a Python program that calculates the area of a circle based on the radius entered by the user.
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504

from math import pi


r = float(input("enter the radius:"))

area = pi * r **2

print(f"the area of the circle with radius {r} is {area}")

