"""
1. instance method -- It's an object specific
    1st Argument should be self and we can able to call with only an object
2. class method
    1st arg should be class decorated with and classmethod we are able to call it with an object or a class
3. static method
    1st arg not be a self or class and decorated with staticmethod we can able to call with object or a class
"""


import datetime


class Student:
    # class/static variable -->we can able to call from `class` or an `object`
    college_name = "CBIT"

    def __init__(self,fname,lname,age):

        # Below Instance variable we can able to call only from the `object`
        # If you call with class it will raise an AttributeError error
        self.fname = fname
        self.lname = lname
        self.age = age
    # Static method has to be decorated with @staticmethod
    # 1st argument not self and not a cls
    # We can able to call from `class` or an `object`
    @staticmethod
    def full_name(fname,lname):
        return f"{fname} {lname}"

    # Instance method, 1st argument has to be self
    # Below Instance instance we can able to call only from the `object`
    # If you call with class it will raise an TypeError error

    def get_full_name(self):

        return self.full_name(self.fname, self.lname)

    # Class method has to be decorated with @classmethod
    # 1st argument should be cls
    # We can able to call from `class` or an `object`

    @classmethod
    def student_from_dob(cls,fname,lname,dob):
        age = datetime.datetime.now().year - dob.year
        return cls(fname,lname,age)



obj = Student("ganesh","kumar",25)


#calling class varible
print("collage name using object:",obj.college_name)
#calling by classname
print("class name",Student.college_name)

#instance methods
print("instance method-obj:",obj.get_full_name())
print("instance by cls:",Student.get_full_name(obj))

#static methods
print("static with obj:",obj.full_name(obj.fname,obj.lname))
#static with class
print("static with class:",Student.full_name(obj.fname,obj.lname))

# static with class
print("with class:",Student.full_name("naresh","kumar"))

# class method

print("date,time: ",datetime.datetime.now())
print("year: ",datetime.datetime.now().year)

# with class

ganesh= obj.student_from_dob("ganesh", "kumar", datetime.datetime(1998,9,4))

print(ganesh.__dict__)
shakthi = Student.student_from_dob("Sakthi","reddy",datetime.datetime(1999,4,25))
print(shakthi.__dict__)

# by class
print(Student.student_from_dob("ganesh", "kumar", datetime.datetime(1998,9,4)))
ganesh= Student.student_from_dob("ganesh", "kumar", datetime.datetime(1998,9,4))
print(ganesh.__dict__)
# print(ganesh())