

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def drive(self, drive=0):
        self.mileage = self.mileage + drive

    def __str__(self):
        return f"The {self.color} car has {self.mileage:,} miles."


blue_car = Car("blue", 2000)
red_car = Car("red", 3000)
print(blue_car)
print(red_car)

red_car.drive(100)
print(red_car.mileage)
print(blue_car)
print(red_car)
