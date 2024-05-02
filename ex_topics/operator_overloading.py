
a = [1,2,3]
m = list([1,2,3])

print(isinstance(a,list))

print(isinstance(m,list))


a = list([1,2,3])
b = list([4,5,6])
print(a+b)

# print(a*b)

print("class method __add__ method operator overloading ")

class Mylist(list):

    def __add__(self,obj):
        return [x+y for x,y in zip(self,obj)]
c = Mylist([1,2,3])
d = Mylist([4,5,6])

print(c+d)
print(c ,d )

print(Mylist)
print(isinstance(c,Mylist))




class MyList(list):

    def __add__(self,obj):
        return [x+y for x,y in zip(self,obj)]
    
    def __mul__(self,obj):

        return [x*y for x ,y in zip(self,obj)]
    
c = MyList([1,2,3])
d = list([4,5,6])

print(c)
print(d)

print(id(c))
print(id(d))

print(c*d)

print(c.__mul__(d),"multiplication")
print(c.__add__(d),"addition")