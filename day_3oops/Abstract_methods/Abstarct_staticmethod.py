from abc import ABC,abstractstaticmethod


class MyUtility(ABC):

    @abstractstaticmethod
    def static_method():
        pass

class ConcreteUtility(MyUtility):
    @staticmethod
    def static_method():

        print("ConcreteUtility static method ")

ConcreteUtility.static_method()