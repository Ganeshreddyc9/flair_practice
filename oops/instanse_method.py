# instance method 

# for instance method it's an object specific first parameter  passed as an self and 
    
# Instance method, 1st argument has to be self
# Below Instance instance we can able to call only from the `objec
# If you call with class it will raise an TypeError error


# staticmethod

# @ static method is decorated with @ staticmethod
#stactic method arguments 
# 1st arguement is not self and not cls 
# we can able to call from class or an object 

# @cls
# first methods has to be decorated with @classmethod 
# 1st argument shuld be cls 
# we can able to call from class or an object 
import datetime

class Student:

    collage_student = 'cbit'

    def __init__(self,fname, lname, age):

        self.fname = fname
        self.lname = lname
        self.age = age
    @staticmethod
    def full_name(fname, lname):
        return f"{fname} {lname}"

    # instance method
    def get_full_name(self):
        return  self.full_name(self.fname, self.lname)
    
    @classmethod

    def student_from_dob(cls, fname, lname, dob):
        age = datetime.datetime.now().year - dob.year

        return cls(fname, lname,age)
    

suresh = Student('suresh','kumar',25)


print(suresh.full_name('suresh','kumar'))
# instance method
# by using object ---- we can call
# by using class ---- No
print(suresh.get_full_name())

# print(Student.get_full_name())

# static method
# by using object ---- we can call
# by using class ---- we can call

print(suresh.full_name(suresh.fname, suresh.lname))


print(suresh.full_name("Naresh", "Kumar"))

#class name
print(Student.full_name("Naresh", "Kumar"))

# class method
# by using object ---- we can call
# by using class ---- we can call

# using object

    
naresh = suresh.student_from_dob('naresh', 'kumar', datetime.datetime(1998,4,9))
# naresh = suresh.student_from_dob("naresh", 'kumar', datetime.datetime(1996,5,12))

# using class

cnaresh = Student.student_from_dob('naresh', 'kumar', datetime.datetime(1996,5,12))

print(naresh.__dict__)

print(cnaresh.__dict__)