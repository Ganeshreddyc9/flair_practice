# Write logic it has to work for n number of parameters
# Problem 4
# fibonacci series
# 0 1 1 2 3 5 8 13 21 34 55 89
# 1. fib(100) --- I need series 100 < fibonacci series
# Result: 0 1 1 2 3 5 8 13 21 34 55 89
def fibonacci(num):
    x, y = 0, 1
    # print("x...",x)
    while num > y:
        print(x, end=" ")
        x, y = y, x + y
        # print(x,end=" ")
        # print(y,"value y")
fibonacci(100)