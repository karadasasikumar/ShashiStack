# Q1. Create a class Student with instance attributes name and marks.
# Add an instance method is_passed() that returns True if marks > 40.
# Then create 2 student objects and print whether each has passed or failed.


class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def is_passed(self):
        if self.marks > 40:
            return True
        else:
            return False

s1=Student("shashi",50)
s2=Student("sasi",30)
print(s1.name,"Passed" if s1.is_passed() else "Failed")
print(s2.name,"Passed" if s2.is_passed() else "Failed")



