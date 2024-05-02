class Test:


    def __init__(self, fname, lname ):

        self.fname = fname 
        self.lname = lname 

    def __str__(self):
        
        return  f" {self.fname} {self.lname}"

obj = Test('ganesh', 'kumar')

print(obj)
