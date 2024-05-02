class StudentInfo:

    def __init__(self, fname, lname, per, phone):
        self.fname = fname
        self.lname = lname 
        self.per = per
        self.phone = phone

    def update_phone(self, new_phone):
         self.phone = new_phone 
         return self.phone


obj = StudentInfo('HI', 'THERE', '55', 998765432)

print(obj.fname)

print(obj.phone)

new_phone = (obj.update_phone(7989806289))
print(new_phone)