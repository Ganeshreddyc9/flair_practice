class MyClass:
    def __init__(self, value):
        self.value = value

    def instance_method(self):
        return self.value

# Creating an instance of MyClass
obj = MyClass(10)

# Accessing instance method using the class name (not recommended)
result = MyClass.instance_method(obj)

print(result)  # Output: 105

