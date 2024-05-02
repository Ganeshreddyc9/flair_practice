class StudentInfo:

    country = 'India'
    location = 'Bangalore'

    def __init__(self, fname, lname, per, phone):
        self.fname = fname
        self.lname = lname 
        self.per = per
        self.phone = phone 
        print("i am in __init__")
    def full_name(self):
        return f"{self.fname}--{self.lname}"
    
    def info(self):
        return f"{self.full_name()}--{self.per}--{self.phone}--{self.country},{self.location}"

obj = StudentInfo('ganesh','c','54','987654312345')

print(obj.full_name())
print(obj.info())