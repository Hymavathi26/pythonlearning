# #Hierarchical inheritance----one parent have multiple child class
#
class vehicle:
    def info(self):
        return "this is a vehical"

class Car(vehicle):
    def info(self):
        return "this is a car"

class Bicycle(Car):
    def info(self):
        return "This is a bicycle"

car=Car()
print(car.info())

bicycle=Bicycle()
print(bicycle.info())

class Vehicle:
    def info(self):
        return "This is a vehicle."


class Car(Vehicle):
    def info(self):
        return "This is a car."


class Bicycle(Vehicle):
    def info(self):
        return "This is a bicycle."


car = Car()
bicycle = Bicycle()
print(car.info())
print(bicycle.info())