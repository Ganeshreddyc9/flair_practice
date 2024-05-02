# Class Methods:

# Defined using the @classmethod decorator.
# The first parameter is always cls, representing the class itself.
# Class methods can access and modify class-level variables.
# They are often used as alternative constructors or to manipulate class-level data.
# Example:


# class MyClass:

#     class_varibale = 0
      

#     def class_method(cls):

#         cls.class_variable += 1
#         print(cls.class_variable)

# MyClass.class_method()  # Output: 1
# MyClass.class_method()  # Output: 2

class MyClass:
    class_variable = 0

    @classmethod
    def class_method(cls):
        cls.class_variable += 1
        print(cls.class_variable)

MyClass.class_method()  # Output: 1
MyClass.class_method() 

