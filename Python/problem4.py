# Create a class Temperature with:
# •	instance attribute celsius
# •	a static method to_fahrenheit(celsius)
# •	an instance method show_conversion() that uses the static method to print both values.


class Temperature:
    def __init__(self,celsius):
        self.celsius=celsius
    @staticmethod
    def to_fahrenhiet(celsius):
        return  celsius*9/5+32
    def show_conversion(self):
        print(self.celsius,"C")
        print(Temperature.to_fahrenhiet(self.celsius),"F")

t1=Temperature(16)
t1.show_conversion()