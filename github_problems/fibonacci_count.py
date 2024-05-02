# 2. fib(20) --- I need first 20 fibonacci series
# Result: 0 1 1 2 3 5 8 13 21 34 55 89 * * * * * * * *

def fibonacci(num):

    x, y = 0, 1
    counter = 0

    while num > counter:
        print(x,end=" ")
        x, y = y, x+y
        counter += 1
fibonacci(20)
