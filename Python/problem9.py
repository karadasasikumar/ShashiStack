# Create a class Student with
# •	class variable passing_marks = 40
# •	instance attributes name, marks
# •	instance method result() → prints pass/fail using class variable
# •	class method update_passing_marks(cls, new_marks)
# •	static method grade_category(marks) → returns "A", "B", "C" based on score ranges


class Student:
    passing_marks=40
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def result(self):
        if self.marks>=Student.passing_marks:
            print("Pass")
        else:
            print("Fail")
    @classmethod
    def update_passing_marks(cls,new_marks):
        cls.passing_marks=new_marks
    @staticmethod
    def grade_category(marks):
        if marks>=80:
            return "A"
        elif marks>=70:
            return "B"
        else:
            return"C"
s1=Student("sashi",70)
print(s1.name,s1.marks)

s1.result()
print(Student.grade_category(80))
