

class StudentDetails:
    #static / class varibales
    country = 'India'
    state = 'Karnataka'
    #__init__ is a constructor method
    # in this method object initilization will happen
    def __init__(self,fname,lname,collage):

        #instance varibales
        self.fname = fname
        self.lname = lname
        self.collage = collage
        print("i am in __init__")

    def full_name(self):
        return f"{self.fname} {self.lname}"

    def details(self):
        return f"{self.full_name()} - {self.collage}-{self.state}-{self.country}"

obj = StudentDetails('ganesh','c','Rljit')
# (obj.full_name()) # i am in __init__
print(obj.details())
print(obj.collage, obj.country, obj.state, obj.fname, obj.lname)

print(obj.__dict__)

# to access instanse methods inside a class have to use self.name
