
class Fibonacci:


    def display(self):
        x = 0
        y = 1

        for i in range(10):
            print(x)
            x, y = y, x+y
# print(x)

# print(y)

fib = Fibonacci()
fib.display()