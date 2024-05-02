

a = [3,4,5]
b = list[1,2,3]

print(type(a)) # <class 'list'>
print(type(type(a))) #<class 'type'>

# All data types are inherited from type class


class Test:

    def foo(self):
        pass
    def show(self):
        return []

obj = Test()

print("checked in class Test foo method is there or not:",hasattr(Test,'foo'))
print(getattr(obj,'show')())

# print(getattr(obj,'show'))
# print("hgjk")
# getattr(obj,'show')()
# print("gkjbj")

help(type)