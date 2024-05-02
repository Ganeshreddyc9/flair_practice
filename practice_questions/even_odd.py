#  Write a program to check if a number is even or odd. 


# An interviewer expects the candidate
# to demonstrate their knowledge of conditional statements and basic arithmetic operations.

number = int(input("enter the number:"))

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")