class File:

    def __init__(self,name,company):
        self.name = name
        self.comany = company
    def method(self):
        return self.name , self.comany

obj = File('ganesh',"xyz")
m = obj.method()
print(m[0])
print(m[1])






