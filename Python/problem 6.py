# Create a class Car with:
# •	instance attribute mileage
# •	class attribute wheels = 4
# Add an instance method display_specs() that prints mileage and wheels.
# Then change wheels using a class method, and print again


class Car:
    wheels=4
    def __init__(self,mileage):
        self.mileage=mileage
    def display_specs(self):
        print(self.mileage,Car.wheels)
    @classmethod
    def change_wheels(cls,new_wheels):
        cls.wheels=new_wheels

c1=Car(20)
c1.display_specs()

#afterchanging
Car.change_wheels(6)
c1.display_specs()..