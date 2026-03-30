#  Create a base class Animal with a method sound(). Create a derived class Dog
# that overrides the sound() method. Demonstrate method overriding

class Animal:
    def sound(self):
        print("This is a Animal")
class Dog(Animal):
    def sound(self):
        super().sound()
        print("This is a Dog")

obj=Dog()
obj.sound()