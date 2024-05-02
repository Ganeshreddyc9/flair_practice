# str and repr

#
# class Test:
#
#     def __init__(self,fname,lname):
#         self.lname = lname
#         self.fname = fname
#
# obj1 = Test("suresh","kumar")
# obj2 = Test("naresh","kumar")
# # obj1,obj2
# print(obj1,obj2)
# #<__main__.Test object at 0x000002437D765AE0> <__main__.Test object at 0x000002437DBB39D0>

class Test:

    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def __repr__(self):
        return ( f"{self.fname}")
    def __str__(self):
        return f"{self.fname} -- {self.lname}"


obj = Test("naresh","kumar")
# obj()
print(repr(obj)) # 
print("this will call str function",obj)

