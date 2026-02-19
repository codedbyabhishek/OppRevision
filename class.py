#class
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f"{self.brand} is driving.")

# Object 
my_car = Car("Toyota", "Red")
my_car.drive()  # Output: Toyota is driving.