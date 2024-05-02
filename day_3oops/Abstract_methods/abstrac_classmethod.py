from abc import ABC ,abstractclassmethod


class MyClass(ABC):
    @abstractclassmethod
    def class_method(cls):
        pass

class ConcreteClass(MyClass):

    @classmethod
    def class_method(cls):
        print("Concrete class classmethod")

ConcreteClass.class_method()