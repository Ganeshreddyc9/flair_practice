"""
how to create an Abstract class ?

sol: the class must be inherit from abc and one method should be any one of
1. abstractclassmethod
2. abstractmethod
3. abstractstaticmethod
4. abstactproperty
"""


from abc import(ABC,
                abstractclassmethod,
                abstractmethod,
                abstractproperty,
                abstractstaticmethod)

class Parent(ABC):
    @abstractmethod
    def foo(self):
        print("I am in Abstract.foo")

    def bar(self):
        print("I am in Abstract.bar")


"""
obj = Parent()

# 1st point For a abstract class we unable to create an object
# obj.foo()
# obj.bar()
   obj = Parent()
TypeError: Can't instantiate abstract class Parent with abstract method foo
"""

# in child class have to override all the methods that time we can create object or else raise type error
# class Test(Parent):
#
#     def show(self):
#         print("I am in Test.show")
# obj = Test()
# obj.show()

"""
in child class you have to override all the abstract methods ,
then only you can create an object for child class.
abstractmethod
abstractclassmethod
abstractstaticmethod
abstractproperty 
"""

class Test(Parent):

    def foo(self):
        print("I am in Test.foo")
    def show(self):
        print("I am in Test.show")
obj = Test()
obj.foo()
obj.show()
obj.bar()