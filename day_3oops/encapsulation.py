# Encapsulation:

# by using encapsulation we can hide data
# or
# bundling

# if that method or variable are private that we cant access outside a class directly
class Test:

    a = 10
    _b = 20
    __c = 30

    def show(self): # public
        print("i am in show method")

    def _display(self):#protected
        print("i am in _display method protected ")

    def __pprint(self):#private
        print("i am in __pprint method")

    def local_test(self):
        # we cant access pprint method outside

        self.__pprint()
        print(self.__c)

obj = Test()
obj.show()
print(obj.a)
# print(obj.__c)
obj._display()

# obj.__pprint()
obj.local_test()
print("accessing proetected variable _b:",obj._b)

print(obj._Test__c,"private varibale")


