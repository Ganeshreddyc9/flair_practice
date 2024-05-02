#
'''
@classmethod

1) if we want to use classmethod we have to use @classmethod as decorated and first parameter is as cls

2) when we use
--->  if we want to modify the class level attributes we have use cls.var = 1 like that .
---> it provides multiple ways to create objects

3) @classmethod decorator is a convinient way to define a class method .
--> it signals to the interpreter that it is a class method.
--> without this decorator this method would be instance method by default

'''


class MyClass:
    class_varibale = 0
    def __init__(self,value):
        self.instance_varibale = value
        MyClass.class_varibale +=1
    @classmethod
    def get_class_variable(cls):
        # here we can access with both with class name or cls
        return MyClass.class_varibale
        # return cls.class_varibale


obj = MyClass(10)
obj1 = MyClass(23)

print(obj.get_class_variable())
# obj = MyClass.class_varibale
# print(obj)

