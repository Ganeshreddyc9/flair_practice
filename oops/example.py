class File:

    def __init__(self,name,company):
        self.name = name
        self.comany = company
    def method(self):
        return self.name,self.comany


        


obj = File('ganesh',"xyz")
# print(obj.method())
print(obj.method())