# Encapsulation

# by using Encspsulation we can able to hide the data 

# or 

# Process of hiding or putting on restrictions on accessing the methods varibles and properties from outside the class 

# or 

# We can able to class private method or variable by 
# obj._classname<method/variable>

class Test:

    a = 10 # public
    _b = 20 # protected
    __c = 30 # private


    def show():

        print("i am in show method")

    def _display(self):
        print("I am in _display method private")

    def __pprint(self):
        # private --> you unable to access we will get AttributeError
        print("i am in __pprint method")

    def local_test(self):
        # we unable to access __pprint from outside but we
        # can able access in the class
        print(self.__pprint())
        # print(self.__c)


obj = Test()

obj.show()

obj._display()

# obj.__pprint()

# obj._Test__c

# obj.<_classname>.<method/variable>
# obj._Test__pprint()

obj.local_test()