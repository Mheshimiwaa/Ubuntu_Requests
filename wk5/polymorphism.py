# Parent class
class Vehicle:
    def move(self):
        print("Vehicle is moving...")


# Child classes
class Car(Vehicle):
    def move(self):
        print("Driving")


class Plane(Vehicle):
    def move(self):
        print("Flying")


class Bike(Vehicle):
    def move(self):
        print("Cycling")


# Testing polymorphism
if __name__ == "__main__":
    vehicles = [Car(), Plane(), Bike()]

    for v in vehicles:
        v.move()
