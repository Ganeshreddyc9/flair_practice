# method resolution order

class AA:

    def foo(self):
        print("AA.foo")

    def bar(self):
        print("AA.bar")

class A(AA):

    def foo(self):
        print("A.foo")

    def bar(self):
        print("A.bar")

class B(A):
    #
    # def foo(self):
    #     print("B.foo")

    def bar(self):
        print("B.bar")

class C:

    def foo(self):
        print("C.foo")

    def bar(self):
        print("C.bar")

class D(B,C):

    pass
    # def foo(self):
    #     print("D.foo")

obj = D()
obj.foo()

print(D.__bases__)
print(D.__mro__)
