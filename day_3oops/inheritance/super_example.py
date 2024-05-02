class Parent:

    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def foo(self):
        print("i am in parent.foo")

    def bar(self):
        print("i am in parent.bar")

class Child(Parent):

    def __init__(self,fname,lname,age):
        super(Child,self).__init__(fname,lname)
        self.age = age

    def display(self):
        print("i am in child.display method")

    def show(self):
        print("i am in child.show")

    def bar(self):
        super().bar()
        super().foo()
        print("i am in child.bar")
obj = Child('suresh','kumar',25)
obj.bar()
# obj.foo()