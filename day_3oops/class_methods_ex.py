class Student:
    # import datetime
    # time = datetime.datetime.now()
    def __init__(self, name):
        self.name = name

    def name_s(self):
        print(self.name)

    @classmethod
    def name_c(cls):pass
        # cls.name = cls.name + "       garu from c-method"
        # print(cls.name)


a = Student("raja")
print(dir(a), vars(a))
a.name_s()
