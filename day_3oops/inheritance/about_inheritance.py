# Override the existing method
# You can enhance the existing method
# You can create new method


class Parent:

    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def foo(self):
        print("i am in parent.foo")

    def bar(self):
        print ("i am in parent.bar")

class Child(Parent):

    def __init__(self,fname,lname,age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def display(self):
        print("i am in child.display method")

    def show(self):
        print("i am in child.show")
    #here updating the existing method
    def bar(self):
        print("i am in child.bar")


obj = Child("suresh","kumar",24)

obj.foo()
obj.bar()
obj.display()
print(obj.__dict__)
