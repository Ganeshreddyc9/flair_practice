class Person:

    def __init__(self,fname,age):
        self.fname = fname
        self.age = age


    def __str__(self):

        return f"person:{self.fname},age:{self.age}"

    def __repr__(self):
        return f"Person('{self.fname}', {self.age})"
obj = Person("suresh",34)

#It's typically used for display purposes
print("string always gives output as a readeble way",str(obj))
# method is meant to provide an unambiguous and ideally executable string representation of the object
print("there will ",repr(obj))