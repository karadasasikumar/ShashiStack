# Create class Person with a constructor __init__(name). Create class
# Student(Person) with constructor __init__(name, roll). Use super() to call the
# parent constructor

class Person:
    def __init__(self,name):
        self.name=name

class Student(Person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll=roll


s=Student("Shashi",44)

print(s.name)
print(s.roll)




