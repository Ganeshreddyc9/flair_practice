
# inheritance
# 1 --> inheritance allows that allows one class to inherit the properties and methods of another class

# parent class: the class is being inherited from is called the parent or base class
# child class : the class that inherits from its called the child or derived
"""
inheritance allows the child class to reuse the code from parent class and also enables the child class to extend or override the
behavior of parent class .
The child class inherits the properties and methods and it can have its own additional attributes and methods
"""

class Animal:

    def __init__(self,name):
        self.name = name


    def speak(self):
        pass

class Dog(Animal):

    def speak(self):
        return f"woof"

class Cat(Animal):

    def speak(self):
        return "Meow"

# obj
dog_instance = Dog("Buddy")
print(dog_instance.speak())

cat_instance = Cat("Luna")
print(cat_instance.speak())
