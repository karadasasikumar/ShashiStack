# Create an abstract class Shape with an abstract method area(). Create class
# Rectangle(Shape) that implements the area() method

from abc import ABC, abstractmethod
class Shape:
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def area(self):
        print(5*2)

r=Rectangle()
r.area()



