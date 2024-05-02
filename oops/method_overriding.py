class StudentInfo:

    country = 'India'
    location = 'Bangalore'

    def __init__(self, fname, lname, per, phone):
        self.fname = fname
        self.lname = lname 
        self.per = per
        self.phone = phone 
        print("i am in __init__")
    def student_info(self):
        return f"{self.fname}--{self.lname}"
    
    def info(self):
        return f"{self.student_info()}--{self.per}--{self.phone}--{self.country},{self.location}"

        # return f"{self.info()}--{self.per}--{self.phone}--{self.country},{self.location}" recurtion error

obj = StudentInfo('ganesh','c','54','987654312345')

print(obj.info())

print(obj.fname, obj.lname, obj.phone, obj.per)

print(obj.country,obj.location)


print(obj.__dict__)

print(obj.student_info())

print(type(StudentInfo))