class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    @classmethod
    def create_sports_car(cls):
        print(cls.__dict__)
        return cls("Ferrari", "F40")



    def __str__(self):

        return f"Car(make={self.make}, model={self.model})"


# Using the factory method
sports = Car.create_sports_car()
print(sports)
# print(sports.__dict__)