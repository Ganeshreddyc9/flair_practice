# a = int(input("enter the start  number: "))
# b = int(input("enter the  end number: "))


# if a <= 1:
#     print(a, "is not a prime number")
# elif a > 1:

#     for i in range(a,b//2):
#         if a % i == 0:
#             # print()
#             break
#     else:
#         print(a, 'is a prime number')

# Python program to display all the prime numbers within an interval

lower = 0
upper = 10

# print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)