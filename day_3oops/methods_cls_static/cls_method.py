class MathOperations:
    # num1 = 100
    @classmethod
    def average(cls, num1, num2):
        # cls.num1 = 15
        return (num1 + num2) / 2

# Using the class method
avg = MathOperations.average(10, 20)
print(avg)
# print(avg.__dict__)

# avg1 = MathOperations()
# print(avg1.num1)
# print(avg.num1)