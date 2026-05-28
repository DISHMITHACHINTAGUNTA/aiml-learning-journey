class Engine:
    def __init__(self,horse_power):
        self.horse_power=horse_power

class Wheel:
    def __init__(self,size):
        self.size=size

class Car:
    def __init__(self,model,horse_power,wheel_size):
        self.model=model
        self.engine=Engine(horse_power)
        self.wheels=Wheel(wheel_size)

    def display_car(self):
        return f"{self.model} {self.engine.horse_power} (hp) {self.wheels.size}(inches)"

car1=Car("ford",500,18)
car2=Car("BMW",677,19)
print(car1.display_car())
print(car2.display_car())

#EXAMPLE 2

class Room:
    def __init__(self, name):
        self.name = name

class House:
    def __init__(self):
        # We create the Room object INSIDE the House
        # The Room is "composed" of this house
        self.kitchen = Room("Kitchen")
        self.bedroom = Room("Bedroom")

# When I create a house...
my_house = House()

# The rooms were created automatically inside it.
# If I delete the house:
del my_house
print(my_house.kitchen)# The kitchen and bedroom objects are now gone too!
# They weren't created anywhere else, so they disappear with the house.