# Create a class Student that:
# •	Keeps track of the total number of students created.
# •	Determines whether a student passed or failed based on a shared passing mark.
# •	Provides a method to curve marks by increasing everyone’s marks by a percentage.
# •	Has a utility to convert marks (0–100) into letter grades (A, B, C, etc.).
# Demonstrate:
# 1.	Creating multiple students.
# 2.	Applying a grading curve.
# 3.	Displaying updated results with letter grades.


class Student:
    total=0
    pass_mark=35
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        Student.total+=1
    def result(self):
        if self.marks>Student.pass_marks:
            return "Pass"
        else:
            return "Fail"
    @classmethod
    def cuvre(self,percent):
        self.marks=self.marks+(self.marks*percent/100)
    @staticmethod
    def grade(marks):
        if marks>=90:
            return "A"
        elif marks>=80:
            return "B"
        elif marks>=70:
            return "C"
        else:
            return "D"

s1=Student("shashi",70)
s2=Student("lucky",85)

print(Student.total)

Student.curve(10)