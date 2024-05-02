class Test:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def __repr__(self):
        return 11234
    def __str__(self):
        return 100
    

obj1 = Test('hi', 'There')

print(obj1)