class Vehicle:
    def general_usage(self):
        print("general use: transportation")

class Car(Vehicle):
    def __init__(self):
        print("I am car")
        self.wheels=4
        self.has_roof=True

    def specific_usage(self):
        self.general_usage()
        print("specific use: commute to work")

class Motorcycle(Vehicle):
    def __init__(self):
        print("I am Motorcycle")
        self.wheels=2
        self.has_roof= False

    def specific_usage(self):
        self.general_usage()
        print("specific: road trip & racing")

c=Car()
c.specific_usage()
m=Motorcycle()

print(issubclass(Motorcycle,Vehicle))
